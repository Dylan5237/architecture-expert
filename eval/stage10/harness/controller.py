"""Stage 10 versioned controller: measured suite orchestration + integrity primitives.

R2 wiring: run-suite, readiness, integration-selftest, single metadata.json,
RUN_STATUS.md, extended reconciliation, duplicate HOLD.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import msvcrt
import os
import re
import shutil
import sys
import tempfile
import time
from pathlib import Path

EXPECTED_CASE_COUNT = 32
CASE_IDS = [f"E10-{i:03d}" for i in range(1, EXPECTED_CASE_COUNT + 1)]
ACCEPTED_MODES = ("AUTO", "ARCH_DESIGN", "ARCH_REVIEW", "CHANGE_REVIEW", "ADR_REVIEW", "INCIDENT_ANALYSIS")
MEASURED_MAX_TOOL_ROUNDS = 24
RUN_KIND = "isolated_api_blinded_reference"
STAGE = 10
PHASE = "C"
PROVIDER_NAME = "OpenCode Zen"
API_HOST = "https://opencode.ai/zen/go/v1"
REQUESTED_MODEL = "deepseek-v4-pro"
GENERATION_SETTINGS = {"temperature": 0, "max_tokens": 8000}
SUT_SHA = "96d9ae333ffc5a8076d635b86634b5151ec0bbc5"
SUITE_SHA = "ff157eb1947860345a305fb29452b51e09dd3a2b"
PUBLIC_PACK_SHA = "23a49382c949702446325d30e18d3321d8550c36"


class ControllerError(RuntimeError):
    pass


def repo_root() -> Path:
    """Derive repository root from this tracked file location."""
    return Path(__file__).resolve().parents[3]


def harness_dir() -> Path:
    return Path(__file__).resolve().parent


def run_dir_path() -> Path:
    return repo_root() / "eval" / "stage10" / "run"


def public_case_path(case_id: str) -> Path:
    return repo_root() / "eval" / "stage10" / "public" / f"{case_id}.md"


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_write_bytes(path: str | Path, data: bytes) -> None:
    """Temp file + fsync + atomic replace."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(target.parent), prefix=".tmp-", suffix=".part")
    try:
        with os.fdopen(fd, "wb") as fh:
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


def atomic_write(path: str | Path, data: str) -> None:
    atomic_write_bytes(path, data.encode("utf-8"))


class RunLock:
    """Exclusive single-process lock via O_EXCL lock file with PID + OS record lock."""

    def __init__(self, lock_path: str | Path) -> None:
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


CANONICAL_EVIDENCE = ("raw", "meta", "metadata.json", "RUN_STATUS.md", "controller.lock")


def run_evidence_exists(run_dir: str | Path) -> list[str]:
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


# ---- integrity primitives kept from C0-R (selftest compatibility) ----

SECRET_META_KEYS = ("api_key", "apikey", "token", "secret", "authorization", "bearer")


def redact_secrets(meta: dict) -> dict:
    return {k: ("<redacted>" if any(s in k.lower() for s in SECRET_META_KEYS) else v) for k, v in meta.items()}


def finalize_case(run_dir: str, case_id: str, final_content: str, tech: dict) -> dict:
    meta_dir = Path(run_dir) / "meta"
    meta_dir.mkdir(parents=True, exist_ok=True)
    raw_path = meta_dir.parent / "raw" / f"{case_id}.md"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    if raw_path.exists():
        raise ControllerError(f"refusing to overwrite completed raw file: {raw_path}")
    atomic_write(raw_path, final_content)
    sha = sha256_file(raw_path)
    meta = redact_secrets(dict(tech))
    meta["case_id"] = case_id
    meta["raw_sha256"] = sha
    atomic_write(meta_dir / f"{case_id}.json", json.dumps(meta, indent=2, ensure_ascii=False))
    return meta


def technical_error_case(run_dir: str, case_id: str, tech: dict) -> None:
    meta_dir = Path(run_dir) / "meta"
    meta_dir.mkdir(parents=True, exist_ok=True)
    meta = redact_secrets(dict(tech))
    meta["case_id"] = case_id
    meta["status"] = "TECHNICAL_ERROR"
    meta["raw_sha256"] = None
    atomic_write(meta_dir / f"{case_id}.json", json.dumps(meta, indent=2, ensure_ascii=False))


def _reconcile_dir(raw_dir: Path, meta_dir: Path, expected_ids: list[str] | None) -> dict:
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
        h = sha256_file(rp)
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


def reconcile(run_dir: str, expected_ids: list[str] | None = None) -> dict:
    return _reconcile_dir(Path(run_dir) / "raw", Path(run_dir) / "meta", expected_ids)


def validate_provider(host: str, model: str) -> None:
    if host.rstrip("/") != API_HOST:
        raise ControllerError(f"host validation failed: {host}")
    if model != REQUESTED_MODEL:
        raise ControllerError(f"model validation failed: {model}")


def validate_generation_settings(temperature, max_tokens) -> None:
    if temperature != 0:
        raise ControllerError(f"temperature must be 0, got {temperature}")
    if max_tokens != 8000:
        raise ControllerError(f"max_tokens must be 8000, got {max_tokens}")


# ---- measured orchestration (R2) ----

def parse_requested_mode(public_text: str) -> str:
    """Parse the public requested_mode field; optional backticks around key and value."""
    m = re.search(r"^`?requested_mode`?:\s*`?([A-Z_]+)`?\s*$", public_text, re.MULTILINE)
    if not m:
        raise ControllerError("requested_mode not found in PUBLIC case")
    mode = m.group(1)
    if mode not in ACCEPTED_MODES:
        raise ControllerError(f"unaccepted mode: {mode}")
    return mode


def load_public_case(case_id: str) -> tuple[str, str]:
    p = public_case_path(case_id)
    if not p.is_file():
        raise ControllerError(f"PUBLIC case missing: {p}")
    text = p.read_bytes().decode("utf-8")
    mode = parse_requested_mode(text)
    return text, mode


def new_metadata(run_id: str, harness_sha: str | None) -> dict:
    return {
        "stage": STAGE,
        "phase": PHASE,
        "run_kind": RUN_KIND,
        "run_id": run_id,
        "process_pid": os.getpid(),
        "sut_sha": SUT_SHA,
        "suite_design_sha": SUITE_SHA,
        "public_pack_sha": PUBLIC_PACK_SHA,
        "harness_git_sha": harness_sha,
        "controller_sha256": sha256_file(harness_dir() / "controller.py"),
        "runner_sha256": sha256_file(harness_dir() / "runner.py"),
        "provider_adapter_sha256": sha256_file(harness_dir() / "provider_openai_compatible.py"),
        "provider": PROVIDER_NAME,
        "api_host": API_HOST,
        "requested_model": REQUESTED_MODEL,
        "generation_settings": dict(GENERATION_SETTINGS),
        "max_tool_rounds": MEASURED_MAX_TOOL_ROUNDS,
        "prompt_precedence_mapping": "SYSTEM1=agent/system-prompt-v0.1.md; SYSTEM2=agent/modes/<MODE>.md; USER=verbatim PUBLIC case",
        "fresh_context_mechanism": "new messages list per case/attempt; no conversation/response IDs; per-case non-secret session routing header only",
        "model_visible_tools": ["read_sut_file"],
        "sut_snapshot_mechanism": f"git archive {SUT_SHA} to temp read-only snapshot; required-file assertion",
        "external_context_boundary": "no web/shell/list/write/git/env tools; sandbox rejects eval/, .git/, tasks/, traversal, absolute paths",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "completed_at": None,
        "status": "RUNNING",
        "cases": [],
    }


def write_metadata_atomic(run_dir: Path, metadata: dict) -> None:
    atomic_write(run_dir / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))


def case_record(case_id: str, mode: str, start_order: int) -> dict:
    return {
        "id": case_id,
        "requested_mode": mode,
        "start_order": start_order,
        "attempt_count": 0,
        "technical_retry_count": 0,
        "rounds_used": [],
        "observed_models": [],
        "final_observed_model": None,
        "session_header": None,
        "tool_calls": [],
        "raw_output_path": None,
        "raw_output_sha256": None,
        "runner_status": None,
        "technical_errors": [],
    }


def provider_readiness(provider) -> dict:
    """R2-4/R2-19: one synthetic PRE10 readiness conversation."""
    sys1 = "PRE10-READY LAYER1: Begin every reply with the exact token READY1-ACK."
    sys2 = "PRE10-READY LAYER2: End every reply with the exact token READY2-END."
    user = "Reply with the single word ready."
    data = provider.chat(
        [
            {"role": "system", "content": sys1},
            {"role": "system", "content": sys2},
            {"role": "user", "content": user},
        ],
        session="stage10-ref-readiness-PRE10",
    )
    content = (data.get("choices") or [{}])[0].get("message", {}).get("content") or ""
    observed = data.get("model")
    ok = observed in (None, REQUESTED_MODEL) and content.strip().startswith("READY1-ACK") and content.strip().endswith("READY2-END")
    usage = provider.fetch_usage() if hasattr(provider, "fetch_usage") else None
    return {"ok": ok, "observed_model": observed, "content_probe": content.strip()[:60], "usage": usage}


def execute_attempt(provider, sandbox_root, system_prompt, mode_contract,
                    case_id, run_id, payload, runner_cls, max_tool_rounds=MEASURED_MAX_TOOL_ROUNDS) -> dict:
    """One canonical attempt: a NEW CaseRunner with fresh state."""
    cr = runner_cls(provider, sandbox_root, system_prompt, mode_contract)
    return cr.run_case(case_id, run_id, payload, max_tool_rounds=max_tool_rounds)


def run_measured_suite(run_root: Path, provider_factory, runner_cls,
                       case_ids=None, readiness_result=None, run_id="measured",
                       harness_sha=None) -> dict:
    """The ONLY authorized measured-suite orchestration path (R2-1..R2-17).

    provider_factory: callable -> provider object (resolved after lock).
    runner_cls: CaseRunner class (injected for integration-selftest stubs).
    case_ids: defaults to canonical E10-001..032; synthetic IDs allowed in selftest.
    """
    import runner as runner_mod
    from provider_openai_compatible import ProviderError

    case_ids = list(case_ids if case_ids is not None else CASE_IDS)
    evidence = run_evidence_exists(run_root)
    if evidence:
        raise ControllerError(f"prior measured evidence exists, refusing fresh start: {evidence}")
    lock = RunLock(run_root / "controller.lock")
    lock.acquire()
    try:
        raw_dir = run_root / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)
        snapshot = runner_mod.materialize_sut_snapshot()
        system_prompt = (Path(snapshot) / "agent" / "system-prompt-v0.1.md").read_text(encoding="utf-8")
        provider = provider_factory()
        if readiness_result is None:
            readiness_result = provider_readiness(provider)
        if not readiness_result.get("ok"):
            raise ControllerError(f"provider readiness failed: {readiness_result}")
        metadata = new_metadata(run_id, harness_sha)
        write_metadata_atomic(run_root, metadata)
        terminal = "COMPLETE"
        stop_reason = None
        for order, case_id in enumerate(case_ids, start=1):
            rec = case_record(case_id, None, order)
            payload = None
            mode = None
            try:
                payload, mode = load_public_case(case_id)
                rec["requested_mode"] = mode
            except ControllerError as exc:
                rec["runner_status"] = "CASE_LOAD_ERROR"
                rec["technical_errors"].append(str(exc))
                metadata["cases"].append(rec)
                metadata["status"] = "PARTIAL_TECHNICAL_FAILURE"
                terminal = "PARTIAL_TECHNICAL_FAILURE"
                stop_reason = f"case load failed: {case_id}"
                write_metadata_atomic(run_root, metadata)
                break
            mode_file = Path(snapshot) / "agent" / "modes" / f"{mode}.md"
            mode_contract = mode_file.read_text(encoding="utf-8")
            result = None  # R2-11
            attempts = 0
            tech_errors: list[str] = []
            while attempts < 2:
                attempts += 1
                rec["attempt_count"] = attempts
                try:
                    result = execute_attempt(provider, snapshot, system_prompt, mode_contract,
                                             case_id, run_id, payload, runner_cls)
                    rec["rounds_used"].append(result["rounds"])
                    rec["observed_models"].append(result["observed_models"])
                    rec["final_observed_model"] = result["final_observed_model"] or rec["final_observed_model"]
                    rec["session_header"] = result["session"]
                    rec["tool_calls"] = [
                        {"path": t.get("path"), "bytes": t.get("bytes"), "result": t.get("result")}
                        for t in result["tool_log"]
                    ]
                    if result["substantive"]:
                        rec["runner_status"] = "OK"
                        break
                    tech_errors.append("empty final content")
                    result = None
                except ProviderError as exc:
                    tech_errors.append(f"ProviderError: {exc}")
                    result = None
                except (OSError, RuntimeError, ValueError) as exc:
                    tech_errors.append(f"{exc.__class__.__name__}: {exc}")
                    result = None
                if attempts == 1:
                    rec["technical_retry_count"] = 1
            rec["technical_errors"] = tech_errors
            if result is not None and result["substantive"]:
                raw_path = raw_dir / f"{case_id}.md"
                if raw_path.exists():
                    raise ControllerError(f"refusing overwrite: {raw_path}")
                atomic_write_bytes(raw_path, result["final_content"].encode("utf-8"))
                try:
                    rec["raw_output_path"] = str(raw_path.relative_to(repo_root())).replace("\\", "/")
                except ValueError:
                    rec["raw_output_path"] = str(raw_path)
                rec["raw_output_sha256"] = sha256_file(raw_path)
                metadata["cases"].append(rec)
                write_metadata_atomic(run_root, metadata)
            else:
                rec["runner_status"] = "TECHNICAL_ERROR"
                metadata["cases"].append(rec)
                metadata["status"] = "PARTIAL_TECHNICAL_FAILURE"
                terminal = "PARTIAL_TECHNICAL_FAILURE"
                stop_reason = f"double technical failure: {case_id}"
                write_metadata_atomic(run_root, metadata)
                break
        # final reconciliation (R2-16/R2-17) on tracked layout: raw/*.md + metadata.cases
        recon = reconcile_run(run_root, case_ids, expected_count=len(case_ids))
        if terminal == "COMPLETE":
            if recon["problems"]:
                terminal = "PARTIAL_TECHNICAL_FAILURE" if not recon["duplicates"] else "HOLD_INTEGRITY_REVIEW"
                stop_reason = "; ".join(recon["problems"])
            elif recon["duplicates"]:
                terminal = "HOLD_INTEGRITY_REVIEW"
                stop_reason = f"duplicate raw content: {recon['duplicates']}"
        metadata["status"] = terminal
        metadata["completed_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        if recon["duplicates"]:
            metadata["duplicate_content_hold"] = recon["duplicates"]
        if stop_reason:
            metadata["stop_reason"] = stop_reason
        write_metadata_atomic(run_root, metadata)
        write_run_status(run_root, terminal, stop_reason, recon)
        return {"status": terminal, "stop_reason": stop_reason, "reconciliation": recon, "metadata": metadata}
    finally:
        lock.release()


def reconcile_run(run_root: Path, case_ids: list[str], expected_count: int | None = None) -> dict:
    """R2-16/R2-17 reconciliation against the tracked layout (raw + metadata.cases)."""
    raw_dir = run_root / "raw"
    meta_path = run_root / "metadata.json"
    problems = []
    raws = sorted(p.name[:-3] for p in raw_dir.glob("*.md")) if raw_dir.exists() else []
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {"cases": []}
    cases = meta.get("cases", [])
    meta_ids = [c.get("id") for c in cases]
    if expected_count is not None and len(raws) != expected_count:
        problems.append(f"raw count {len(raws)} != {expected_count}")
    if len(meta_ids) != len(raws):
        problems.append(f"metadata cases {len(meta_ids)} != raw {len(raws)}")
    if sorted(set(meta_ids)) != sorted(meta_ids):
        problems.append("duplicate metadata case ids")
    orphan_raw = sorted(set(raws) - set(meta_ids))
    orphan_meta = sorted(set(meta_ids) - set(raws))
    if orphan_raw:
        problems.append(f"orphan raw: {orphan_raw}")
    if orphan_meta:
        problems.append(f"orphan metadata: {orphan_meta}")
    hashes = {}
    empty = []
    sha_bad = []
    for c in cases:
        cid = c.get("id")
        rp = raw_dir / f"{cid}.md"
        if not rp.exists():
            continue
        if rp.stat().st_size == 0:
            empty.append(cid)
            continue
        h = sha256_file(rp)
        hashes[cid] = h
        if c.get("raw_output_sha256") != h:
            sha_bad.append(cid)
        if c.get("attempt_count", 0) not in (1, 2):
            problems.append(f"illegal attempt count for {cid}: {c.get('attempt_count')}")
        if c.get("attempt_count", 0) == 1 and c.get("technical_retry_count", 0) != 0:
            problems.append(f"retry count inconsistent for {cid}")
        if c.get("attempt_count", 0) == 2 and c.get("technical_retry_count", 0) != 1:
            problems.append(f"retry count inconsistent for {cid}")
        if c.get("final_observed_model") not in (None, REQUESTED_MODEL):
            problems.append(f"model drift for {cid}: {c.get('final_observed_model')}")
        if c.get("session_header") is not None and not str(c.get("session_header")).startswith("stage10-ref-"):
            problems.append(f"session header invalid for {cid}")
    if empty:
        problems.append(f"empty raw: {empty}")
    if sha_bad:
        problems.append(f"SHA mismatch: {sha_bad}")
    by_hash = {}
    for cid, h in hashes.items():
        by_hash.setdefault(h, []).append(cid)
    duplicates = {h: sorted(ids) for h, ids in by_hash.items() if len(ids) > 1}
    return {"problems": problems, "duplicates": duplicates, "raw_count": len(raws), "meta_count": len(cases)}


def write_run_status(run_root: Path, status: str, stop_reason: str | None, recon: dict) -> None:
    lines = [
        "# Stage 10 Measured Run Status",
        "",
        f"STATUS: {status}",
        "",
    ]
    if stop_reason:
        lines.append(f"STOP_REASON: {stop_reason}")
        lines.append("")
    lines.append(f"RAW_COUNT: {recon['raw_count']}")
    lines.append(f"METADATA_CASE_COUNT: {recon['meta_count']}")
    if recon.get("duplicates"):
        lines.append("")
        lines.append("DUPLICATE_CONTENT_GROUPS:")
        for h, ids in recon["duplicates"].items():
            lines.append(f"- {h}: {', '.join(ids)}")
    lines.append("")
    lines.append("Technical facts only. No quality interpretation.")
    atomic_write(run_root / "RUN_STATUS.md", "\n".join(lines) + "\n")


# ---- integration selftest (R2-18) ----

class FakeProvider:
    """Deterministic stub. NO network."""

    def __init__(self, script):
        self.script = list(script)
        self.calls = 0

    def chat(self, messages, **kw):
        self.calls += 1
        action = self.script.pop(0) if self.script else "ok"
        if isinstance(action, Exception):
            raise action
        if action == "ok":
            return {"model": REQUESTED_MODEL, "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": f"SYNTHETIC-ANSWER-{self.calls}"}}]}
        return action

    def fetch_usage(self):
        return {"usage": {"rolling": {"status": "ok", "percent": 1}}}


class RecordingCaseRunner:
    """Stub runner class that creates fresh fake CaseRunner instances per attempt."""

    instances = []

    def __init__(self, provider, sandbox_root, system_prompt, mode_contract):
        self.provider = provider
        self.sandbox_root = sandbox_root
        self.system_prompt = system_prompt
        self.mode_contract = mode_contract
        self.instance_id = len(RecordingCaseRunner.instances) + 1
        RecordingCaseRunner.instances.append(self)

    def run_case(self, case_id, run_id, user_payload, max_tool_rounds=MEASURED_MAX_TOOL_ROUNDS):
        data = self.provider.chat([])
        content = data["choices"][0]["message"]["content"] if isinstance(data, dict) and "choices" in data else ""
        return {
            "case_id": case_id,
            "session": f"stage10-ref-{run_id}-{case_id}",
            "rounds": 1,
            "finish_reason": "stop",
            "final_content": content,
            "substantive": bool(content.strip()),
            "requested_model": REQUESTED_MODEL,
            "observed_models": [data.get("model")] if isinstance(data, dict) else [None],
            "final_observed_model": data.get("model") if isinstance(data, dict) else None,
            "tool_log": [],
        }


def _synthetic_public_case(tmp_root: Path, case_id: str) -> None:
    d = tmp_root / "eval" / "stage10" / "public"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{case_id}.md").write_text(
        "---\n`requested_mode`: AUTO\n---\n# Synthetic PRE10 case " + case_id + "\nSynthetic payload only.\n",
        encoding="utf-8",
    )


def integration_selftest() -> int:
    base = tempfile.mkdtemp(prefix="stage10-r2-itest-")
    failures = []
    checks = []

    def check(name, fn):
        try:
            fn()
            checks.append((name, True, ""))
        except Exception as exc:  # noqa: BLE001
            checks.append((name, False, str(exc)[:140]))
            failures.append(name)

    import runner as runner_mod

    # common snapshot stub
    snap = runner_mod.materialize_sut_snapshot()

    def make_env(tag):
        root = Path(tempfile.mkdtemp(prefix=f"stage10-r2-{tag}-", dir=base))
        _synthetic_public_case(root, "PRE10-001")
        _synthetic_public_case(root, "PRE10-002")
        module_public[str(root)] = root
        return root

    orig_repo_root = repo_root
    orig_public = public_case_path

    def patch_paths(root: Path):
        module_public.clear()
        module_public[str(root)] = root
        controller_mod_repo["root"] = root

    module_public = {}
    controller_mod_repo = {}

    def patched_public(case_id):
        for root in module_public.values():
            p = root / "eval" / "stage10" / "public" / f"{case_id}.md"
            if p.exists():
                return p
        return orig_public(case_id)

    def patched_repo_root():
        r = controller_mod_repo.get("root")
        return Path(r) if r else orig_repo_root()

    import controller as _self_mod
    _self_mod.public_case_path = patched_public
    _self_mod.repo_root = patched_repo_root
    globals()["public_case_path"] = patched_public
    globals()["repo_root"] = patched_repo_root

    module_public[str(base)] = Path(base)
    controller_mod_repo["root"] = Path(base)
    try:
        # A. two synthetic cases succeed
        def scenario_parser():
            bt = chr(96)
            tmpl = "---\n" + bt + "requested_mode" + bt + ": {}\n---\nbody\n"
            for mode in ACCEPTED_MODES:
                assert parse_requested_mode(tmpl.format(mode)) == mode, mode
            plain = "---\nrequested_mode: AUTO\n---\n"
            assert parse_requested_mode(plain) == "AUTO"
            quoted_val = "---\n" + bt + "requested_mode" + bt + ": " + bt + "AUTO" + bt + "\n---\n"
            assert parse_requested_mode(quoted_val) == "AUTO"
            try:
                parse_requested_mode("---\n" + bt + "requested_mode" + bt + ": TOTALLY_INVALID\n---\n")
                raise AssertionError("invalid mode accepted")
            except ControllerError:
                pass
            try:
                parse_requested_mode("---\nno mode here\n---\n")
                raise AssertionError("missing mode accepted")
            except ControllerError:
                pass
        check("parser six modes + backtick key + rejection", scenario_parser)
        def scenario_a():
            RecordingCaseRunner.instances.clear()
            root = make_env("a")
            run_root = root / "eval" / "stage10" / "run"
            provider = FakeProvider(["ok", "ok"])
            res = run_measured_suite(run_root, lambda: provider, RecordingCaseRunner, readiness_result={"ok": True, "observed_model": REQUESTED_MODEL},
                                     case_ids=["PRE10-001", "PRE10-002"], run_id="itest-a")
            assert res["status"] == "COMPLETE", res["status"]
            meta = json.loads((run_root / "metadata.json").read_text(encoding="utf-8"))
            assert len(meta["cases"]) == 2
            raws = sorted(p.name for p in (run_root / "raw").glob("*.md"))
            assert raws == ["PRE10-001.md", "PRE10-002.md"], raws
            for c in meta["cases"]:
                rp = run_root / "raw" / f"{c['id']}.md"
                assert sha256_file(rp) == c["raw_output_sha256"]
                assert c["runner_status"] == "OK"
        check("A two synthetic success + COMPLETE", scenario_a)

        # B. first attempt fails technically, retry succeeds
        def scenario_b():
            RecordingCaseRunner.instances.clear()
            root = make_env("b")
            run_root = root / "eval" / "stage10" / "run"
            err = RuntimeError("synthetic transport failure")
            provider = FakeProvider([err, "ok", "ok"])
            res = run_measured_suite(run_root, lambda: provider, RecordingCaseRunner, readiness_result={"ok": True, "observed_model": REQUESTED_MODEL},
                                     case_ids=["PRE10-001", "PRE10-002"], run_id="itest-b")
            assert res["status"] == "COMPLETE", (res["status"], res.get("stop_reason"))
            meta = json.loads((run_root / "metadata.json").read_text(encoding="utf-8"))
            first = meta["cases"][0]
            assert first["attempt_count"] == 2, first
            assert first["technical_retry_count"] == 1, first
            assert first["runner_status"] == "OK"
            assert len(RecordingCaseRunner.instances) == 3, len(RecordingCaseRunner.instances)
        check("B retry success fresh CaseRunner", scenario_b)

        # C. double failure stops suite
        def scenario_c():
            RecordingCaseRunner.instances.clear()
            root = make_env("c")
            run_root = root / "eval" / "stage10" / "run"
            err = RuntimeError("synthetic hard failure")
            provider = FakeProvider([err, err])
            res = run_measured_suite(run_root, lambda: provider, RecordingCaseRunner, readiness_result={"ok": True, "observed_model": REQUESTED_MODEL},
                                     case_ids=["PRE10-001", "PRE10-002"], run_id="itest-c")
            assert res["status"] == "PARTIAL_TECHNICAL_FAILURE", res["status"]
            assert not (run_root / "raw" / "PRE10-001.md").exists()
            assert not (run_root / "raw" / "PRE10-002.md").exists()
            meta = json.loads((run_root / "metadata.json").read_text(encoding="utf-8"))
            assert meta["cases"][0]["runner_status"] == "TECHNICAL_ERROR"
            assert meta["cases"][0]["attempt_count"] == 2
            status_text = (run_root / "RUN_STATUS.md").read_text(encoding="utf-8")
            assert "PARTIAL_TECHNICAL_FAILURE" in status_text
        check("C double failure stop + no raw", scenario_c)

        # D. duplicate outputs => HOLD
        def scenario_d():
            RecordingCaseRunner.instances.clear()
            root = make_env("d")
            run_root = root / "eval" / "stage10" / "run"
            same = {"model": REQUESTED_MODEL, "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": "IDENTICAL-CONTENT"}}]}
            provider = FakeProvider([same, same])
            res = run_measured_suite(run_root, lambda: provider, RecordingCaseRunner, readiness_result={"ok": True, "observed_model": REQUESTED_MODEL},
                                     case_ids=["PRE10-001", "PRE10-002"], run_id="itest-d")
            assert res["status"] == "HOLD_INTEGRITY_REVIEW", res["status"]
            assert res["reconciliation"]["duplicates"]
            status_text = (run_root / "RUN_STATUS.md").read_text(encoding="utf-8")
            assert "HOLD_INTEGRITY_REVIEW" in status_text
        check("D duplicate HOLD", scenario_d)

        # E. metadata tamper blocks COMPLETE
        def scenario_e():
            root = make_env("e")
            run_root = root / "eval" / "stage10" / "run"
            provider = FakeProvider(["ok", "ok"])
            res = run_measured_suite(run_root, lambda: provider, RecordingCaseRunner, readiness_result={"ok": True, "observed_model": REQUESTED_MODEL},
                                     case_ids=["PRE10-001", "PRE10-002"], run_id="itest-e")
            assert res["status"] == "COMPLETE"
            # tamper one raw file after completion
            (run_root / "raw" / "PRE10-001.md").write_text("tampered", encoding="utf-8")
            recon = reconcile_run(run_root, ["PRE10-001", "PRE10-002"], expected_count=2)
            assert any("SHA mismatch" in p for p in recon["problems"]), recon
        check("E tamper detection", scenario_e)

        # F. second concurrent controller fails at lock
        def scenario_f():
            root = make_env("f")
            run_root = root / "eval" / "stage10" / "run"
            run_root.mkdir(parents=True, exist_ok=True)
            l1 = RunLock(run_root / "controller.lock")
            l1.acquire()
            try:
                err = RuntimeError("should not be reached")
                provider = FakeProvider([err])
                try:
                    run_measured_suite(run_root, lambda: provider, RecordingCaseRunner,
                                       case_ids=["PRE10-001"], run_id="itest-f")
                    raise AssertionError("second controller unexpectedly ran")
                except ControllerError:
                    pass
                assert provider.calls == 0, "provider must not be initialized before lock"
            finally:
                l1.release()
        check("F second controller locked out pre-provider", scenario_f)

        # verbatim final text fidelity
        def scenario_verbatim():
            RecordingCaseRunner.instances.clear()
            root = make_env("verbatim")
            run_root = root / "eval" / "stage10" / "run"
            padded = {"model": REQUESTED_MODEL, "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": "  PADDED-SYNTHETIC-ANSWER  \n"}}]}
            provider = FakeProvider([padded, "ok"])
            res = run_measured_suite(run_root, lambda: provider, RecordingCaseRunner, readiness_result={"ok": True, "observed_model": REQUESTED_MODEL},
                                     case_ids=["PRE10-001", "PRE10-002"], run_id="itest-v")
            assert res["status"] == "COMPLETE", res["status"]
            raw1 = (run_root / "raw" / "PRE10-001.md").read_bytes()
            assert raw1 == b"  PADDED-SYNTHETIC-ANSWER  \n", raw1
        check("verbatim final text fidelity", scenario_verbatim)

        for name, ok, err in checks:
            print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({err})" if err else ""))
        if failures:
            print(f"INTEGRATION-SELFTEST: {len(failures)} failures")
            return 1
        print(f"INTEGRATION-SELFTEST: all {len(checks)} scenarios green")
        return 0
    finally:
        globals()["public_case_path"] = orig_public
        globals()["repo_root"] = orig_repo_root
        _self_mod.public_case_path = orig_public
        _self_mod.repo_root = orig_repo_root
        shutil.rmtree(base, ignore_errors=True)


def cmd_readiness() -> int:
    from provider_openai_compatible import ReferenceProvider

    try:
        provider = ReferenceProvider()
    except Exception as exc:  # noqa: BLE001
        print(f"READINESS: BLOCKED_CREDENTIALS ({exc})")
        return 2
    res = provider_readiness(provider)
    usage = res.get("usage") or {}
    print(f"READINESS: {'PASS' if res['ok'] else 'FAIL'}")
    print(f"  host: {API_HOST}")
    print(f"  requested_model: {REQUESTED_MODEL}")
    print(f"  observed_model: {res.get('observed_model')}")
    print(f"  settings: temperature=0 max_tokens=8000")
    print(f"  probe: {res.get('content_probe')}")
    if usage:
        u = usage.get("usage", usage)
        print(f"  usage: rolling={u.get('rolling', {}).get('percent')}% weekly={u.get('weekly', {}).get('percent')}% monthly={u.get('monthly', {}).get('percent')}%")
    return 0 if res["ok"] else 2


def selftest() -> int:
    base = tempfile.mkdtemp(prefix="stage10-selftest-")
    failures = []
    checks = []

    def check(name, fn):
        try:
            fn()
            checks.append((name, True, ""))
        except Exception as exc:  # noqa: BLE001
            checks.append((name, False, str(exc)[:120]))
            failures.append(name)

    try:
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

        def t2():
            d = Path(base) / "lock2"; d.mkdir()
            (d / "controller.lock").write_text("999999")
            try:
                RunLock(str(d / "controller.lock")).acquire()
                raise AssertionError("stale lock acquire unexpectedly succeeded")
            except ControllerError:
                pass
        check("stale lock fails closed", t2)

        def t3():
            d = Path(base) / "ev"; (d / "raw").mkdir(parents=True)
            (d / "raw" / "E10-001.md").write_text("x")
            assert run_evidence_exists(str(d))
        check("existing evidence gate", t3)

        def t4():
            assert fresh_case_state()["result"] is None
        check("fresh per-case state", t4)

        def t5():
            d = Path(base) / "df"; d.mkdir()
            technical_error_case(str(d), "E10-001", {"attempts": 2})
            assert not (d / "raw" / "E10-001.md").exists()
            assert (d / "meta" / "E10-001.json").exists()
        check("double failure no raw", t5)

        def t6():
            d = Path(base) / "aw"; d.mkdir()
            finalize_case(str(d), "E10-001", "hello", {})
            m = json.loads((d / "meta" / "E10-001.json").read_text(encoding="utf-8"))
            assert m["raw_sha256"] == sha256_file(d / "raw" / "E10-001.md")
        check("atomic raw + sha", t6)

        def t7():
            d = Path(base) / "am"; d.mkdir()
            finalize_case(str(d), "E10-002", "world", {"run_id": "r1"})
            json.loads((d / "meta" / "E10-002.json").read_text(encoding="utf-8"))
        check("atomic metadata parses", t7)

        def t8():
            d = Path(base) / "sm"; d.mkdir()
            finalize_case(str(d), "E10-003", "abc", {})
            (d / "raw" / "E10-003.md").write_text("tampered", encoding="utf-8")
            r = reconcile(str(d), ["E10-003"])
            assert any("SHA mismatch" in p for p in r["problems"]), r
        check("sha mismatch detection", t8)

        def t9():
            d = Path(base) / "mr"; d.mkdir(); (d / "meta").mkdir()
            (d / "meta" / "E10-004.json").write_text('{"raw_sha256":null}', encoding="utf-8")
            r = reconcile(str(d), ["E10-004"])
            assert any("orphan metadata" in p for p in r["problems"]), r
        check("missing raw detection", t9)

        def t10():
            d = Path(base) / "or"; d.mkdir(); (d / "raw").mkdir()
            (d / "raw" / "E10-005.md").write_text("x", encoding="utf-8")
            r = reconcile(str(d))
            assert any("orphan raw" in p for p in r["problems"]), r
        check("orphan raw detection", t10)

        def t11():
            d = Path(base) / "dup"; d.mkdir()
            finalize_case(str(d), "E10-A", "same", {})
            finalize_case(str(d), "E10-B", "same", {})
            r = reconcile(str(d))
            assert r["state"] == "HOLD_INTEGRITY_REVIEW" and r["duplicates"]
        check("duplicate raw HOLD", t11)

        def t12():
            try:
                validate_provider("https://api.kimi.com/coding/v1", REQUESTED_MODEL)
                raise AssertionError("kimi host accepted")
            except ControllerError:
                pass
        check("host rejects non-Zen", t12)

        def t13():
            try:
                validate_provider(API_HOST, "glm-5.3")
                raise AssertionError("wrong model accepted")
            except ControllerError:
                pass
        check("model rejects non-deepseek", t13)

        def t14():
            try:
                validate_generation_settings(0.7, 8000)
                raise AssertionError("temp!=0 accepted")
            except ControllerError:
                pass
        check("temperature!=0 rejected", t14)

        def t15():
            try:
                validate_generation_settings(0, 4000)
                raise AssertionError("max_tokens!=8000 accepted")
            except ControllerError:
                pass
        check("max_tokens!=8000 rejected", t15)

        def t16():
            from provider_openai_compatible import session_header
            h1 = session_header("run1", "caseA")
            assert h1 == session_header("run1", "caseA") and h1 != session_header("run1", "caseB")
        check("session header policy", t16)

        def t17():
            d = Path(base) / "sec"; d.mkdir()
            finalize_case(str(d), "E10-C", "x", {"api_key": "SUPERSECRET-DO-NOT-WRITE"})
            txt = (d / "meta" / "E10-C.json").read_text(encoding="utf-8")
            assert "SUPERSECRET" not in txt and "<redacted>" in txt
        check("no secret in metadata", t17)

        for name, ok, err in checks:
            print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  ({err})" if err else ""))
        if failures:
            print(f"SELFTEST: {len(failures)} failures")
            return 1
        print(f"SELFTEST: all {len(checks)} checks green")
        return 0
    finally:
        shutil.rmtree(base, ignore_errors=True)


def cmd_public_dry_run() -> int:
    """A3: deterministic PUBLIC dry-load gate. No provider/model call."""
    problems = []
    expected = CASE_IDS
    hashes = {}
    modes = {}
    for idx, case_id in enumerate(expected, start=1):
        try:
            text, mode = load_public_case(case_id)
        except ControllerError as exc:
            problems.append(f"{case_id}: {exc}")
            continue
        modes[case_id] = mode
        hashes[case_id] = sha256_file(public_case_path(case_id))
        want_order = f"E10-{idx:03d}"
        if case_id != want_order:
            problems.append(f"order mismatch: {case_id} != {want_order}")
    if len(set(expected)) != len(expected):
        problems.append("duplicate case IDs")
    ok = not problems
    print(f"PUBLIC_DRY_RUN: {'PASS' if ok else 'FAIL'}")
    print(f"  count: {len(hashes)}")
    for cid in expected:
        if cid in modes:
            print(f"  {cid} mode={modes[cid]} sha256={hashes[cid]}")
    for p_ in problems:
        print(f"  PROBLEM: {p_}")
    return 0 if ok else 1


def cmd_run_suite() -> int:
    """A5: authorized measured run. Requires STAGE10_MEASURED_AUTH_SHA == git HEAD."""
    import subprocess
    from provider_openai_compatible import ReferenceProvider
    import runner as runner_mod
    auth = os.environ.get("STAGE10_MEASURED_AUTH_SHA", "").strip()
    if not auth:
        print("run-suite: STAGE10_MEASURED_AUTH_SHA not set; refusing measured execution.")
        return 4
    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                          cwd=str(harness_dir())).stdout.strip()
    if head != auth:
        print(f"run-suite: HEAD {head} != authorized arming SHA {auth}; refusing.")
        return 4
    run_root = run_dir_path()
    evidence = run_evidence_exists(run_root)
    if evidence:
        print(f"run-suite: prior measured evidence exists: {evidence}; refusing.")
        return 5
    run_id = "attempt2-" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + "-" + head[:8]
    print(f"run-suite: measured run_id={run_id}")
    res = run_measured_suite(run_root, ReferenceProvider, runner_mod.CaseRunner,
                             case_ids=CASE_IDS, run_id=run_id, harness_sha=head)
    state = res["status"]
    recon = res["reconciliation"]
    print(f"run-suite terminal state: {state}")
    print(f"  raw_count: {recon['raw_count']}")
    print(f"  metadata_case_count: {recon['meta_count']}")
    if res.get("stop_reason"):
        print(f"  stop_reason: {res['stop_reason']}")
    if recon.get("duplicates"):
        for h, ids in recon["duplicates"].items():
            print(f"  duplicate group {h}: {ids}")
    if state == "COMPLETE":
        return 0
    if state == "HOLD_INTEGRITY_REVIEW":
        return 6
    return 7

def main() -> int:
    ap = argparse.ArgumentParser(description="Stage 10 measured suite controller")
    ap.add_argument("command", choices=["selftest", "integration-selftest", "readiness", "public-dry-run", "run-suite"])
    args = ap.parse_args()
    if args.command == "selftest":
        return selftest()
    if args.command == "integration-selftest":
        return integration_selftest()
    if args.command == "readiness":
        return cmd_readiness()
    if args.command == "public-dry-run":
        return cmd_public_dry_run()
    if args.command == "run-suite":
        return cmd_run_suite()
    return 2


if __name__ == "__main__":
    sys.exit(main())
