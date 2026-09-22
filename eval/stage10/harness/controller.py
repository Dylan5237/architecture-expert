"""Stage 10 versioned controller: run integrity, atomic writes, reconciliation.

Implements C1..C10 plus a provider-free selftest.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import msvcrt
import os
import sys
import tempfile
import time
from pathlib import Path

EXPECTED_CASE_COUNT = 32


class ControllerError(RuntimeError):
    pass


def atomic_write(path: str, data: str) -> None:
    """Temp file + fsync + atomic replace."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(target.parent), prefix=".tmp-", suffix=".part")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


class RunLock:
    """Exclusive single-process lock via O_EXCL lock file with PID."""

    def __init__(self, lock_path: str) -> None:
        self.lock_path = Path(lock_path)
        self._fd = None

    def acquire(self) -> None:
        if self.lock_path.exists():
            raise ControllerError(f"lock exists (stale or active): {self.lock_path}")
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(str(self.lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError as exc:
            raise ControllerError("second controller failed to acquire lock") from exc
        self._fd = fd
        os.write(fd, str(os.getpid()).encode())
        try:
            msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
        except OSError:
            os.close(fd)
            self._fd = None
            try:
                self.lock_path.unlink()
            except OSError:
                pass
            raise ControllerError("second controller failed to acquire OS lock")

    def release(self) -> None:
        if self._fd is not None:
            try:
                msvcrt.locking(self._fd, msvcrt.LK_UNLCK, 1)
            except OSError:
                pass
            os.close(self._fd)
            self._fd = None
        if self.lock_path.exists():
            try:
                self.lock_path.unlink()
            except OSError:
                pass

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, *exc):
        self.release()


CANONICAL_EVIDENCE = ("raw", "meta", "status.json", "controller.lock")


def run_evidence_exists(run_dir: str) -> list[str]:
    found = []
    p = Path(run_dir)
    if not p.exists():
        return found
    for name in CANONICAL_EVIDENCE:
        if (p / name).exists():
            found.append(name)
    if (p / "raw").exists() and any((p / "raw").iterdir()):
        found.append("raw/*")
    if (p / "meta").exists() and any((p / "meta").iterdir()):
        found.append("meta/*")
    return found


def fresh_case_state() -> dict:
    return {"result": None}


SECRET_META_KEYS = ("api_key", "apikey", "token", "secret", "authorization", "bearer")


def redact_secrets(meta: dict) -> dict:
    return {k: ("<redacted>" if any(s in k.lower() for s in SECRET_META_KEYS) else v) for k, v in meta.items()}


def finalize_case(run_dir: str, case_id: str, final_content: str, tech: dict) -> dict:
    """C5+C6: atomic raw write then atomic metadata with SHA."""
    raw_dir = Path(run_dir) / "raw"
    meta_dir = Path(run_dir) / "meta"
    raw_dir.mkdir(parents=True, exist_ok=True)
    meta_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f"{case_id}.md"
    if raw_path.exists():
        raise ControllerError(f"refusing to overwrite completed raw file: {raw_path}")
    atomic_write(str(raw_path), final_content)
    sha = sha256_file(str(raw_path))
    meta = redact_secrets(dict(tech))
    meta["case_id"] = case_id
    meta["raw_sha256"] = sha
    atomic_write(str(meta_dir / f"{case_id}.json"), json.dumps(meta, indent=2, ensure_ascii=False))
    return meta


def technical_error_case(run_dir: str, case_id: str, tech: dict) -> None:
    meta_dir = Path(run_dir) / "meta"
    meta_dir.mkdir(parents=True, exist_ok=True)
    meta = dict(tech)
    meta["case_id"] = case_id
    meta["status"] = "TECHNICAL_ERROR"
    meta["raw_sha256"] = None
    atomic_write(str(meta_dir / f"{case_id}.json"), json.dumps(meta, indent=2, ensure_ascii=False))


def reconcile(run_dir: str, expected_ids: list[str] | None = None) -> dict:
    """C8+C9: final reconciliation incl. duplicate-content HOLD."""
    raw_dir = Path(run_dir) / "raw"
    meta_dir = Path(run_dir) / "meta"
    raws = sorted(p.name[:-3] for p in raw_dir.glob("*.md")) if raw_dir.exists() else []
    metas = sorted(p.name[:-5] for p in meta_dir.glob("*.json")) if meta_dir.exists() else []
    problems = []
    if expected_ids is not None:
        if raws != sorted(expected_ids):
            problems.append(f"raw IDs mismatch: {raws}")
        if metas != sorted(expected_ids):
            problems.append(f"metadata IDs mismatch: {metas}")
    if len(raws) != len(metas):
        problems.append(f"count mismatch: raw={len(raws)} meta={len(metas)}")
    orphan_raw = sorted(set(raws) - set(metas))
    orphan_meta = sorted(set(metas) - set(raws))
    if orphan_raw:
        problems.append(f"orphan raw: {orphan_raw}")
    if orphan_meta:
        problems.append(f"orphan metadata: {orphan_meta}")
    hashes = {}
    empty = []
    sha_mismatch = []
    for cid in raws:
        rp = raw_dir / f"{cid}.md"
        if rp.stat().st_size == 0:
            empty.append(cid)
            continue
        h = sha256_file(str(rp))
        hashes[cid] = h
        mp = meta_dir / f"{cid}.json"
        if mp.exists():
            m = json.loads(mp.read_text(encoding="utf-8"))
            if m.get("raw_sha256") != h:
                sha_mismatch.append(cid)
    if empty:
        problems.append(f"empty raw files: {empty}")
    if sha_mismatch:
        problems.append(f"SHA mismatch: {sha_mismatch}")
    by_hash = {}
    for cid, h in hashes.items():
        by_hash.setdefault(h, []).append(cid)
    duplicates = {h: sorted(ids) for h, ids in by_hash.items() if len(ids) > 1}
    state = "COMPLETE" if not problems and not duplicates else (
        "HOLD_INTEGRITY_REVIEW" if duplicates and not problems else "INCOMPLETE"
    )
    return {"state": state, "problems": problems, "duplicates": duplicates,
            "raw_count": len(raws), "meta_count": len(metas)}


def validate_provider(host: str, model: str) -> None:
    from provider_openai_compatible import REQUIRED_BASE_URL, REQUIRED_MODEL
    if host.rstrip("/") != REQUIRED_BASE_URL:
        raise ControllerError(f"host validation failed: {host}")
    if model != REQUIRED_MODEL:
        raise ControllerError(f"model validation failed: {model}")


def validate_generation_settings(temperature, max_tokens) -> None:
    if temperature != 0:
        raise ControllerError(f"temperature must be 0, got {temperature}")
    if max_tokens != 8000:
        raise ControllerError(f"max_tokens must be 8000, got {max_tokens}")


def selftest() -> int:
    import shutil as _sh

    failures = []
    checks = []

    def check(name, fn):
        try:
            fn()
            checks.append((name, True, ""))
        except Exception as exc:  # noqa: BLE001
            checks.append((name, False, str(exc)[:120]))
            failures.append(name)

    base = tempfile.mkdtemp(prefix="stage10-selftest-")
    try:
        # 1 exclusive lock
        def t1():
            d = Path(base) / "lock1"; d.mkdir()
            l1 = RunLock(str(d / "controller.lock")); l1.acquire()
            try:
                RunLock(str(d / "controller.lock")).acquire()
                raise AssertionError("second acquire unexpectedly succeeded")
            except ControllerError:
                pass
            finally:
                l1.release()
        check("exclusive lock", t1)

        # 2 stale lock fails closed
        def t2():
            d = Path(base) / "lock2"; d.mkdir()
            (d / "controller.lock").write_text("999999")
            try:
                RunLock(str(d / "controller.lock")).acquire()
                raise AssertionError("stale lock acquire unexpectedly succeeded")
            except ControllerError:
                pass
        check("stale lock fails closed", t2)

        # 3 existing evidence refuses fresh start
        def t3():
            d = Path(base) / "ev"; (d / "raw").mkdir(parents=True)
            (d / "raw" / "E10-001.md").write_text("x")
            ev = run_evidence_exists(str(d))
            assert ev, "expected evidence detection"
        check("existing evidence gate", t3)

        # 4 fresh case state
        def t4():
            s = fresh_case_state()
            assert s["result"] is None
        check("fresh per-case state", t4)

        # 5 double-failure path writes no raw
        def t5():
            d = Path(base) / "df"; d.mkdir()
            technical_error_case(str(d), "E10-001", {"attempts": 2})
            assert not (d / "raw" / "E10-001.md").exists()
            assert (d / "meta" / "E10-001.json").exists()
        check("double failure no raw", t5)

        # 6 atomic raw + sha reconciliation
        def t6():
            d = Path(base) / "aw"; d.mkdir()
            finalize_case(str(d), "E10-001", "hello", {})
            m = json.loads((d / "meta" / "E10-001.json").read_text(encoding="utf-8"))
            assert m["raw_sha256"] == sha256_file(str(d / "raw" / "E10-001.md"))
        check("atomic raw + sha", t6)

        # 7 atomic metadata parses
        def t7():
            d = Path(base) / "am"; d.mkdir()
            finalize_case(str(d), "E10-002", "world", {"run_id": "r1"})
            json.loads((d / "meta" / "E10-002.json").read_text(encoding="utf-8"))
        check("atomic metadata parses", t7)

        # 8 sha mismatch detection
        def t8():
            d = Path(base) / "sm"; d.mkdir()
            finalize_case(str(d), "E10-003", "abc", {})
            (d / "raw" / "E10-003.md").write_text("tampered", encoding="utf-8")
            r = reconcile(str(d), ["E10-003"])
            assert any("SHA mismatch" in p for p in r["problems"]), r
        check("sha mismatch detection", t8)

        # 9 missing raw detection
        def t9():
            d = Path(base) / "mr"; d.mkdir(); (d / "meta").mkdir()
            (d / "meta" / "E10-004.json").write_text('{"raw_sha256":null}', encoding="utf-8")
            r = reconcile(str(d), ["E10-004"])
            assert any("orphan metadata" in p for p in r["problems"]), r
        check("missing raw detection", t9)

        # 10 orphan raw detection
        def t10():
            d = Path(base) / "or"; d.mkdir(); (d / "raw").mkdir()
            (d / "raw" / "E10-005.md").write_text("x", encoding="utf-8")
            r = reconcile(str(d))
            assert any("orphan raw" in p for p in r["problems"]), r
        check("orphan raw detection", t10)

        # 11 duplicate raw => HOLD
        def t11():
            d = Path(base) / "dup"; d.mkdir()
            finalize_case(str(d), "E10-A", "same", {})
            finalize_case(str(d), "E10-B", "same", {})
            r = reconcile(str(d))
            assert r["state"] == "HOLD_INTEGRITY_REVIEW", r
            assert r["duplicates"], r
        check("duplicate raw HOLD", t11)

        # 12 host validation
        def t12():
            try:
                validate_provider("https://api.kimi.com/coding/v1", "deepseek-v4-pro")
                raise AssertionError("kimi host accepted")
            except ControllerError:
                pass
        check("host rejects non-Zen", t12)

        # 13 model validation
        def t13():
            try:
                validate_provider("https://opencode.ai/zen/go/v1", "glm-5.3")
                raise AssertionError("wrong model accepted")
            except ControllerError:
                pass
        check("model rejects non-deepseek", t13)

        # 14 temperature
        def t14():
            try:
                validate_generation_settings(0.7, 8000)
                raise AssertionError("temp!=0 accepted")
            except ControllerError:
                pass
        check("temperature!=0 rejected", t14)

        # 15 max_tokens
        def t15():
            try:
                validate_generation_settings(0, 4000)
                raise AssertionError("max_tokens!=8000 accepted")
            except ControllerError:
                pass
        check("max_tokens!=8000 rejected", t15)

        # 16 session header
        def t16():
            from provider_openai_compatible import session_header
            h1 = session_header("run1", "caseA")
            h1b = session_header("run1", "caseA")
            h2 = session_header("run1", "caseB")
            assert h1 == h1b and h1 != h2, (h1, h2)
        check("session header policy", t16)

        # 17 no secret in metadata
        def t17():
            d = Path(base) / "sec"; d.mkdir()
            finalize_case(str(d), "E10-C", "x", {"api_key": "SUPERSECRET-DO-NOT-WRITE"})
            txt = (d / "meta" / "E10-C.json").read_text(encoding="utf-8")
            assert "SUPERSECRET" not in txt, "secret leaked into metadata"
        check("no secret in metadata", t17)

        for name, ok, err in checks:
            print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({err})" if err else ""))
        if failures:
            print(f"SELFTEST: {len(failures)} failures")
            return 1
        print(f"SELFTEST: all {len(checks)} checks green")
        return 0
    finally:
        _sh.rmtree(base, ignore_errors=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["selftest"])
    args = ap.parse_args()
    if args.command == "selftest":
        return selftest()
    return 2


if __name__ == "__main__":
    sys.exit(main())
