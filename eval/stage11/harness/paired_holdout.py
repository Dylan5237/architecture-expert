"""Stage 11C: one sequential pair, frozen Stage 10 transport and integrity APIs."""
from __future__ import annotations

import argparse
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import tarfile
import tempfile
import time

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "eval/stage10/harness"))
import controller as c
import runner as r
import provider_openai_compatible as p

BRANCH = "eval/stage11-paired-holdout"
TASK_SOURCE = "477ea2ecf05a9e0512ba5432d837e98ed6cc3454"
DESIGN = "69cab5ab750c350ce719a0d37e7680bbc96bdf21"
PROVIDER_FREEZE = "7db2639044d3a8f0b8706d70161513238ed29670"
CANDIDATES = {
    "v0.1": ("96d9ae333ffc5a8076d635b86634b5151ec0bbc5", "agent/system-prompt-v0.1.md"),
    "v0.2": ("c12b67c7410878960c45a9934ded6ae52ae6c42f", "agent/system-prompt-v0.2.md"),
}
IDS = [f"H11-{i:03d}" for i in range(1, 13)]
COMMON = ["00_ROUTER.md", "01_CONSTITUTION.md", "02_VOCABULARY.md",
          "relationship-map.yaml", "source-manifest.yaml", "domains", "principles",
          "failure-patterns", "tactics", "decision-playbooks", "question-bank", "cases", "sources"]
MODES = [f"agent/modes/{mode}.md" for mode in c.ACCEPTED_MODES]
RUN_ROOT = ROOT / "eval/stage11/holdout/run"
FROZEN_WORKING_HASHES = {
    "controller.py": "206f9f136eed6b2b83f612c3705dfd1850e244e78a44772d9ac49723d7d6e35a",
    "runner.py": "17bc6afc9cda16570d29c91ae7ea43e33e9f67443196759b16357ca52c6c2654",
    "provider_openai_compatible.py": "8013d03289e34cb784eccb003cde04a7f92564731399953743451d52d919253f",
    "requirements.txt": "b74b60affa8b2087f451e1d0483451f567d54e3d5f0c861cb68e7422e8f51c1f",
}


def git(*args: str) -> bytes:
    proc = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if proc.returncode:
        raise c.ControllerError(f"git command failed ({proc.returncode})")
    return proc.stdout


def identity() -> str:
    assert git("rev-parse", "--show-toplevel").decode().strip().replace("\\", "/").lower() == str(ROOT).replace("\\", "/").lower()
    assert git("branch", "--show-current").decode().strip() == BRANCH
    assert not git("status", "--porcelain=v1", "--untracked-files=no"), "tracked worktree dirty"
    return git("rev-parse", "HEAD").decode().strip()


def frozen_hashes() -> dict:
    for name, digest in FROZEN_WORKING_HASHES.items():
        path = "eval/stage10/harness/" + name
        assert git("show", f"HEAD:{path}") == git("show", f"{PROVIDER_FREEZE}:{path}"), path
        assert c.sha256_file(ROOT / path) == digest, path
    assert p.REQUIRED_MODEL == "glm-5.3" and p.REQUIRED_MAX_TOKENS == 32000
    assert p.httpx.__version__ == "0.28.1"
    return dict(FROZEN_WORKING_HASHES)


def public_payloads() -> dict:
    payloads = {}
    for cid in IDS:
        path = f"eval/stage11/holdout/design/public/{cid}.md"
        data = git("show", f"{DESIGN}:{path}")
        text = data.decode("utf-8")
        assert re.search(rf"^id: {cid}$", text, re.MULTILINE), cid
        assert len(re.findall(r"^requested_mode:", text, re.MULTILINE)) == 1, cid
        payloads[cid] = {"text": text, "sha256": c.sha256_bytes(data),
                         "mode": c.parse_requested_mode(text), "bytes": len(data)}
    assert list(payloads) == IDS
    return payloads


def snapshot(version: str) -> tuple[Path, dict]:
    sha, prompt = CANDIDATES[version]
    root = Path(tempfile.mkdtemp(prefix=f"stage11-{version}-sut-"))
    archive = git("archive", sha, "--", *COMMON, *MODES, prompt)
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive)) as tf:
        for member in tf.getmembers():
            name = member.name.rstrip("/")
            rel = PurePosixPath(name)
            assert not rel.is_absolute() and ".." not in rel.parts
            assert member.isdir() or member.isfile(), "snapshot links forbidden"
            if member.isdir():
                continue
            assert name in COMMON + MODES + [prompt] or rel.parts[0] in COMMON[5:], name
            data = tf.extractfile(member).read()
            dest = root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            dest.chmod(stat.S_IREAD)
            files[name] = c.sha256_bytes(data)
    assert all(name in files for name in COMMON[:5] + MODES + [prompt])
    assert not any(name.split("/")[0] in ("eval", "reports", "tasks", ".git") for name in files)
    assert [name for name in files if name.startswith("agent/system-prompt-")] == [prompt]
    return root, files


def snapshots() -> tuple[dict, dict]:
    roots, inventories = {}, {}
    for version in CANDIDATES:
        roots[version], inventories[version] = snapshot(version)
    a, b = inventories.values()
    common_a = set(a) - {CANDIDATES["v0.1"][1]}
    common_b = set(b) - {CANDIDATES["v0.2"][1]}
    assert common_a == common_b, "common snapshot inventory differs"
    auto = "agent/modes/AUTO.md"
    for name in common_a - {auto}:
        assert a[name] == b[name], f"unaccounted snapshot difference: {name}"
    old = (roots["v0.1"] / auto).read_bytes()
    neutral = old.replace(b"`agent/system-prompt-v0.1.md`", b"the active system prompt")
    assert neutral == (roots["v0.2"] / auto).read_bytes(), "AUTO differs beyond allowed neutral reference"
    assert a[CANDIDATES["v0.1"][1]] != b[CANDIDATES["v0.2"][1]], "active prompt identities equal"
    return roots, inventories


def metadata(version, run_id, freeze, payloads, files, gate):
    meta = c.new_metadata(run_id, freeze)
    sha, prompt = CANDIDATES[version]
    meta.update(stage=11, phase="C", version=version, sut_sha=sha,
                suite_design_sha=DESIGN, public_pack_sha=DESIGN,
                task_source_sha=TASK_SOURCE,
                task_sha256=c.sha256_bytes(git("show", f"{TASK_SOURCE}:tasks/stage11/CODEX_STAGE11_PAIRED_HOLDOUT.md")),
                adapter_git_sha=freeze, adapter_sha256=c.sha256_file(__file__),
                active_system_prompt_path=prompt, active_system_prompt_sha256=files[prompt],
                mode_contract_sha256={mode: files[f"agent/modes/{mode}.md"] for mode in c.ACCEPTED_MODES},
                public_input_sha256={cid: value["sha256"] for cid, value in payloads.items()},
                sut_snapshot_files_sha256=files,
                sut_snapshot_mechanism="explicit Git archive whitelist; original bytes; read-only files",
                prompt_precedence_mapping=f"SYSTEM1={prompt}; SYSTEM2=agent/modes/<MODE>.md; USER=exact PUBLIC UTF-8 bytes",
                fresh_context_mechanism="new CaseRunner/messages/sandbox and unique session per case/attempt",
                external_context_boundary="only read_sut_file; no eval/reports/tasks/holdout/.git materialized; no alternative prompt",
                mechanical_gate=gate)
    return meta


def write_status(root, status, reason, recon):
    c.atomic_write(root / "RUN_STATUS.md", "\n".join([
        "# Stage 11 Paired Candidate Run Status", "", f"STATUS: {status}",
        f"STOP_REASON: {reason or 'NONE'}", f"RAW_COUNT: {recon['raw_count']}",
        f"METADATA_CASE_COUNT: {recon['meta_count']}", "",
        "Technical facts only. No quality interpretation.", ""]))


class EvidenceCaseRunner(r.CaseRunner):
    """Retain path/byte/result audit on technical failure without changing the runner."""

    def run_case(self, *args, **kwargs):
        try:
            return super().run_case(*args, **kwargs)
        except Exception as exc:
            exc.tool_log = list(self.tool_log)
            raise


def run_version(root, version, run_id, freeze, snap, files, payloads, gate, factory=p.ReferenceProvider):
    assert not root.exists(), "candidate output already exists"
    meta = metadata(version, run_id, freeze, payloads, files, gate)
    c.write_metadata_atomic(root, meta)
    system = (snap / CANDIDATES[version][1]).read_bytes().decode("utf-8")
    terminal, reason = "COMPLETE", None
    provider = None
    try:
        provider = factory()
        for order, cid in enumerate(payloads, 1):
            item = payloads[cid]
            mode = item["mode"]
            contract = (snap / f"agent/modes/{mode}.md").read_bytes().decode("utf-8")
            rec = c.case_record(cid, mode, order)
            rec.update(input_sha256=item["sha256"], input_bytes=item["bytes"],
                       system_prompt_sha256=files[CANDIDATES[version][1]],
                       mode_contract_sha256=files[f"agent/modes/{mode}.md"], attempt_sessions=[])
            result = None
            for attempt in (1, 2):
                rec["attempt_count"] = attempt
                rec["technical_retry_count"] = attempt - 1
                attempt_run = f"{run_id}-a{attempt}"
                rec["attempt_sessions"].append(p.session_header(attempt_run, cid))
                try:
                    result = c.execute_attempt(provider, str(snap), system, contract, cid,
                                               attempt_run, item["text"], EvidenceCaseRunner)
                    rec["rounds_used"].append(result["rounds"])
                    rec["observed_models"].append(result["observed_models"])
                    rec["final_observed_model"] = result["final_observed_model"] or rec["final_observed_model"]
                    rec["session_header"] = result["session"]
                    rec["tool_calls"].extend({"attempt": attempt, **tool} for tool in result["tool_log"])
                    rec["attempt_diagnostics"].append({
                        "attempt": attempt, "rounds": result["rounds"],
                        "final_finish_reason": result["finish_reason"], "substantive": result["substantive"],
                        "rounds_metadata": result["rounds_diagnostics"]})
                    if result["substantive"]:
                        rec["runner_status"] = "OK"
                        break
                    rec["technical_errors"].append("empty final content")
                    result = None
                except (p.ProviderError, OSError, RuntimeError, ValueError) as exc:
                    diag = getattr(exc, "case_diagnostics", {})
                    rounds = diag.get("rounds_metadata", [])
                    rec["technical_errors"].append(f"{type(exc).__name__}: {exc}")
                    rec["tool_calls"].extend({"attempt": attempt, **tool} for tool in getattr(exc, "tool_log", []))
                    rec["rounds_used"].append(diag.get("rounds", 0))
                    rec["attempt_diagnostics"].append({
                        "attempt": attempt, "rounds": diag.get("rounds", len(rounds)),
                        "final_finish_reason": diag.get("final_finish_reason"), "substantive": False,
                        "rounds_metadata": rounds, "error_class": type(exc).__name__})
                    if rounds:
                        rec["final_observed_model"] = rounds[-1].get("observed_model") or rec["final_observed_model"]
                    result = None
            if result is not None and result["substantive"]:
                raw = root / "raw" / f"{cid}.md"
                assert not raw.exists(), "raw overwrite forbidden"
                c.atomic_write_bytes(raw, result["final_content"].encode("utf-8"))
                rec["raw_output_path"] = f"eval/stage11/holdout/run/{version}/raw/{cid}.md"
                rec["raw_output_sha256"] = c.sha256_file(raw)
            else:
                rec["runner_status"] = "TECHNICAL_ERROR"
                terminal, reason = "PARTIAL_TECHNICAL_FAILURE", f"double technical failure: {cid}"
            meta["cases"].append(rec)
            c.write_metadata_atomic(root, meta)
            print(f"{version} {cid}: {rec['runner_status']} attempts={rec['attempt_count']}", flush=True)
            if terminal != "COMPLETE":
                break
    except Exception as exc:
        terminal, reason = "PARTIAL_TECHNICAL_FAILURE", f"controller error: {type(exc).__name__}: {exc}"
    finally:
        if provider is not None:
            try:
                provider.close()
            except Exception as exc:
                terminal, reason = "PARTIAL_TECHNICAL_FAILURE", f"provider close error: {type(exc).__name__}"
    recon = c.reconcile_run(root, list(payloads), expected_count=len(payloads))
    if terminal == "COMPLETE" and (recon["problems"] or recon["duplicates"]):
        terminal = "HOLD_INTEGRITY_REVIEW" if recon["duplicates"] else "PARTIAL_TECHNICAL_FAILURE"
        reason = "reconciliation failed"
    meta.update(status=terminal, completed_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                reconciliation=recon, stop_reason=reason)
    c.write_metadata_atomic(root, meta)
    write_status(root, terminal, reason, recon)
    return meta


def reconcile_pair(root, metas, payloads):
    problems, runs = [], {}
    for version, meta in metas.items():
        recon = c.reconcile_run(root / version, list(payloads), expected_count=len(payloads))
        runs[version] = {"run_id": meta["run_id"], "status": meta["status"], "reconciliation": recon}
        if meta["status"] == "COMPLETE":
            problems.extend(f"{version} {problem}" for problem in recon["problems"])
            if recon["duplicates"]:
                problems.append(f"{version} duplicate raw content")
            if [rec["id"] for rec in meta["cases"]] != list(payloads):
                problems.append(f"{version} exact case IDs/order mismatch")
            if sorted(path.stem for path in (root / version / "raw").glob("*.md")) != sorted(payloads):
                problems.append(f"{version} exact raw IDs mismatch")
        for rec in meta["cases"]:
            if rec["input_sha256"] != payloads[rec["id"]]["sha256"]:
                problems.append(f"{version} input hash mismatch: {rec['id']}")
            for tool in rec["tool_calls"]:
                if tool.get("tool") != "read_sut_file":
                    problems.append(f"{version} additional tool: {rec['id']}")
                allowed_paths = {os.path.normcase(os.path.normpath(path)) for path in meta["sut_snapshot_files_sha256"]}
                normalized = os.path.normcase(os.path.normpath(tool.get("path") or ""))
                if tool.get("result") == "allow" and normalized not in allowed_paths:
                    problems.append(f"{version} non-snapshot read: {rec['id']}")
        if meta["active_system_prompt_path"] != CANDIDATES[version][1] or meta["sut_sha"] != CANDIDATES[version][0]:
            problems.append(f"{version} candidate identity mismatch")
    complete = len(metas) == 2 and all(m["status"] == "COMPLETE" for m in metas.values())
    state = "COMPLETE" if complete else next((m["status"] for m in metas.values() if m["status"] != "COMPLETE"), "PARTIAL_TECHNICAL_FAILURE")
    identity_hold = False
    if complete:
        a, b = metas.values()
        for key in ("adapter_git_sha", "adapter_sha256", "provider", "requested_model", "generation_settings", "transport_policy", "public_input_sha256"):
            if a[key] != b[key]:
                problems.append(f"paired {key} mismatch")
        identity_hold = all(x["raw_output_sha256"] == y["raw_output_sha256"] for x, y in zip(a["cases"], b["cases"]))
        if identity_hold:
            state = "HOLD_INTEGRITY_REVIEW"
    actual = sorted(str(path.relative_to(root)).replace("\\", "/") for path in root.rglob("*") if path.is_file() and path.name != "controller.lock")
    expected = ["PAIR_STATUS.json"] + [f"{v}/{f}" for v in CANDIDATES for f in ["metadata.json", "RUN_STATUS.md"] + [f"raw/{cid}.md" for cid in payloads]]
    # PAIR_STATUS is written by the caller immediately after this check.
    if complete and sorted(actual + ([] if "PAIR_STATUS.json" in actual else ["PAIR_STATUS.json"])) != sorted(expected):
        problems.append("canonical inventory mismatch")
    if problems:
        state = "HOLD_INTEGRITY_REVIEW"
    return {"stage": 11, "phase": "C", "status": state, "technical_only": True,
            "adapter_git_sha": next(iter(metas.values()))["adapter_git_sha"],
            "adapter_sha256": c.sha256_file(__file__), "runs": runs,
            "common_input_sha256": {cid: item["sha256"] for cid, item in payloads.items()},
            "common_input_hash_check": not any("input hash" in x or "public_input_sha256" in x for x in problems),
            "integrity_problems": problems, "HOLD_IDENTITY_REVIEW": identity_hold,
            "canonical_file_count": len(actual) + (0 if "PAIR_STATUS.json" in actual else 1)}


def fake_test(roots, inventories):
    calls, closed = [], []
    test_root = Path(tempfile.mkdtemp(prefix="stage11-fake-"))
    payloads = {cid: {"text": f"id: {cid}\nrequested_mode: AUTO\nSynthetic only.\r\n", "mode": "AUTO"} for cid in IDS[:2]}
    for item in payloads.values():
        item.update(sha256=c.sha256_bytes(item["text"].encode()), bytes=len(item["text"].encode()))

    class Fake:
        def __init__(self, version, fail=False, identical=False):
            self.version, self.fail, self.identical = version, fail, identical
            self.sessions, self.started, self.first = set(), [], True

        def chat(self, messages, **kw):
            calls.append((self.version, kw["session"]))
            assert kw["tools"] == [r.TOOL_SCHEMA] and kw["tool_choice"] == "auto"
            assert kw["temperature"] == 0 and kw["max_tokens"] == 32000
            assert messages[0] == {"role": "system", "content": (roots[self.version] / CANDIDATES[self.version][1]).read_bytes().decode()}
            assert messages[1] == {"role": "system", "content": (roots[self.version] / "agent/modes/AUTO.md").read_bytes().decode()}
            assert messages[2]["role"] == "user" and messages[2]["content"] in [x["text"] for x in payloads.values()]
            if len(messages) == 3:
                assert kw["session"] not in self.sessions
                self.sessions.add(kw["session"])
                self.started.append(messages)
                if self.fail or self.first:
                    self.first = False
                    raise p.ProviderError("synthetic technical failure")
                return {"model": p.REQUIRED_MODEL, "choices": [{"finish_reason": "tool_calls", "message": {
                    "role": "assistant", "tool_calls": [{"id": "read", "type": "function", "function": {
                        "name": "read_sut_file", "arguments": '{"path":"./00_ROUTER.md"}'}}]}}]}
            assert len(messages) == 5 and messages[-1]["role"] == "tool"
            text = "  identical\n" if self.identical else "  synthetic " + kw["session"] + "\n"
            return {"model": p.REQUIRED_MODEL, "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": text}}]}

        def close(self):
            closed.append(self.version)

    metas = {}
    for version in CANDIDATES:
        sandbox = r.PathSandbox(str(roots[version]))
        assert sandbox.read("00_ROUTER.md")[0]
        for path in ("eval/x", "reports/x", "tasks/x", ".git/config", "../00_ROUTER.md", "D:/x", "/x", "agent/../00_ROUTER.md", "agent\\x", CANDIDATES["v0.2" if version == "v0.1" else "v0.1"][1]):
            assert not sandbox.read(path)[0], path
        fake = Fake(version)
        meta = run_version(test_root / version, version, f"fake-{version}", "fake", roots[version], inventories[version], payloads, {}, lambda: fake)
        assert meta["status"] == "COMPLETE" and len(meta["cases"]) == 2
        assert [rec["attempt_count"] for rec in meta["cases"]] == [2, 1]
        assert all((test_root / version / "raw" / f"{rec['id']}.md").read_bytes().startswith(b"  synthetic ") for rec in meta["cases"])
        metas[version] = meta
    assert closed == ["v0.1", "v0.2"] and [version for version, _ in calls] == sorted(version for version, _ in calls)
    pair = reconcile_pair(test_root, metas, payloads)
    assert pair["status"] == "COMPLETE" and not pair["integrity_problems"]
    # Identical outputs across versions are permitted; all paired identities HOLD.
    for left, right in zip(metas["v0.1"]["cases"], metas["v0.2"]["cases"]):
        c.atomic_write_bytes(test_root / "v0.2/raw" / f"{right['id']}.md",
                             (test_root / "v0.1/raw" / f"{left['id']}.md").read_bytes())
        right["raw_output_sha256"] = left["raw_output_sha256"]
    c.write_metadata_atomic(test_root / "v0.2", metas["v0.2"])
    identity_pair = reconcile_pair(test_root, metas, payloads)
    assert identity_pair["status"] == "HOLD_INTEGRITY_REVIEW" and identity_pair["HOLD_IDENTITY_REVIEW"]
    c.atomic_write(test_root / "v0.1/raw/H11-001.md", "tampered")
    tampered_pair = reconcile_pair(test_root, metas, payloads)
    assert tampered_pair["status"] == "HOLD_INTEGRITY_REVIEW"
    assert any("SHA mismatch" in x for x in tampered_pair["integrity_problems"])
    fail = Fake("v0.1", fail=True)
    bad = run_version(test_root / "failure", "v0.1", "fake-failure", "fake", roots["v0.1"], inventories["v0.1"], payloads, {}, lambda: fail)
    assert bad["status"] == "PARTIAL_TECHNICAL_FAILURE" and len(bad["cases"]) == 1 and bad["cases"][0]["attempt_count"] == 2
    dup = Fake("v0.1", identical=True)
    hold = run_version(test_root / "duplicate", "v0.1", "fake-dup", "fake", roots["v0.1"], inventories["v0.1"], payloads, {}, lambda: dup)
    assert hold["status"] == "HOLD_INTEGRITY_REVIEW"
    return "PASS: prompt/messages/tool/schema/sandbox/fresh attempts/serial close/raw/retry/failure/HOLD/tamper"


def readiness(factory=p.ReferenceProvider):
    """One unchanged Stage 10 request; retain technical facts, never response text."""
    diag = {"ok": False, "category": "BLOCKED_PROVIDER", "request_outcome": "NOT_SENT",
            "http_status": None, "observed_model": None, "finish_reason": None,
            "content_length": None, "marker_prefix_ok": False, "marker_suffix_ok": False,
            "error_class": None, "provider_attempt_count": None, "transport_attempt_count": None,
            "provider_retry_count": None, "transport_retry_count": None, "elapsed_s": None}
    provider, calls = None, 0
    started = time.perf_counter()

    def technical(meta):
        for key in ("http_status", "observed_model", "finish_reason", "content_length",
                    "provider_attempt_count", "transport_attempt_count",
                    "provider_retry_count", "transport_retry_count"):
            if key in meta:
                diag[key] = meta[key]

    class Probe:
        def chat(self, messages, **kwargs):
            nonlocal calls
            calls += 1
            assert calls == 1, "only one recovery readiness request authorized"
            diag["request_outcome"] = "SENT"
            data = provider.chat(messages, **kwargs)
            technical(data.get(p.TECHNICAL_RESPONSE_KEY, {}))
            choice = (data.get("choices") or [{}])[0]
            content = choice.get("message", {}).get("content")
            visible = content if isinstance(content, str) else ""
            diag.update(observed_model=data.get("model"), finish_reason=choice.get("finish_reason"),
                        content_length=len(visible), marker_prefix_ok=visible.strip().startswith("READY1-ACK"),
                        marker_suffix_ok=visible.strip().endswith("READY2-END"))
            if diag["http_status"] != 200:
                diag["category"] = "BLOCKED_PROVIDER"
            elif diag["observed_model"] != "glm-5.3":
                diag["category"] = "BLOCKED_MODEL_IDENTITY"
            elif not visible.strip() or diag["finish_reason"] != "stop":
                diag["category"] = "BLOCKED_FINAL"
            else:
                diag["ok"] = True
                diag["category"] = "READY" if diag["marker_prefix_ok"] and diag["marker_suffix_ok"] else "READY_WITH_MARKER_MISMATCH"
                diag["request_outcome"] = "SUCCESS"
            return data

    try:
        provider = factory()
        c.provider_readiness(Probe(), session="stage10-ref-stage11-readiness")
    except Exception as exc:
        technical(getattr(exc, "technical_metadata", {}))
        diag.update(ok=False, request_outcome="EXCEPTION", error_class=type(exc).__name__)
        diag["category"] = "BLOCKED_MODEL_IDENTITY" if diag["observed_model"] not in (None, "glm-5.3") else "BLOCKED_PROVIDER"
    finally:
        if provider is not None:
            try:
                provider.close()
            except Exception as exc:
                diag.update(ok=False, category="BLOCKED_PROVIDER", request_outcome="EXCEPTION", error_class=type(exc).__name__)
        diag["elapsed_s"] = round(time.perf_counter() - started, 3)
    return diag


def persist_readiness(diag, readme):
    status = "READINESS_RECOVERY_READY" if diag["ok"] else "BLOCKED_READINESS_DIAGNOSED"
    entry = "\n## Readiness recovery — 2026-10-08\n\nSTAGE11_C: " + status + "\n\n"
    entry += "```json\n" + json.dumps(diag, ensure_ascii=False, indent=2) + "\n```\n"
    c.atomic_write_bytes(readme, readme.read_bytes() + entry.encode("utf-8"))


def readiness_fake_test():
    temp = Path(tempfile.mkdtemp(prefix="stage11-readiness-fake-")) / "README.md"
    temp.write_bytes(b"Synthetic local diagnostics.\n")

    class Fake:
        def __init__(self, model="glm-5.3", content="ready", error=False, finish="stop"):
            self.model, self.content, self.error, self.finish = model, content, error, finish
            self.calls = 0

        def chat(self, messages, **kwargs):
            self.calls += 1
            assert messages == [
                {"role": "system", "content": "PRE10-READY LAYER1: Begin every reply with the exact token READY1-ACK."},
                {"role": "system", "content": "PRE10-READY LAYER2: End every reply with the exact token READY2-END."},
                {"role": "user", "content": "Reply with the single word ready."}]
            assert kwargs == {"session": "stage10-ref-stage11-readiness"}
            if self.error:
                raise p.ProviderError("DO_NOT_PERSIST_PRIVATE_CONFIGURATION", {"http_status": 403, "transport_attempt_count": 1})
            return {"model": self.model, "choices": [{"finish_reason": self.finish, "message": {"content": self.content}}],
                    p.TECHNICAL_RESPONSE_KEY: {"http_status": 200, "transport_attempt_count": 1, "provider_attempt_count": 1}}

        def close(self):
            pass

    for fake, expected in [(Fake(), "READY_WITH_MARKER_MISMATCH"),
                           (Fake(content="READY1-ACK ready READY2-END"), "READY"),
                           (Fake(model="other-model"), "BLOCKED_MODEL_IDENTITY"),
                           (Fake(content=""), "BLOCKED_FINAL"),
                           (Fake(finish="length"), "BLOCKED_FINAL"),
                           (Fake(error=True), "BLOCKED_PROVIDER")]:
        diag = readiness(lambda: fake)
        assert fake.calls == 1 and diag["category"] == expected
        assert diag["ok"] == expected.startswith("READY")
        persist_readiness(diag, temp)
        assert expected in temp.read_text(encoding="utf-8")
        assert "DO_NOT_PERSIST_PRIVATE_CONFIGURATION" not in temp.read_text(encoding="utf-8")
        if fake.error:
            assert diag["error_class"] == "ProviderError" and diag["http_status"] == 403
    return "PASS: unchanged one-call request; marker-only PASS; model/empty/finish BLOCK; sanitized error persisted"


def gate(record):
    assert identity() == CANDIDATES["v0.2"][0], "gate starting HEAD mismatch"
    assert not RUN_ROOT.exists(), "paired run root already exists"
    assert not record.exists(), "gate record already exists"
    compile(Path(__file__).read_bytes(), __file__, "exec")
    hashes = frozen_hashes()
    payloads = public_payloads()
    roots, inventories = snapshots()
    assert c.selftest() == 0
    original = r.materialize_sut_snapshot
    try:
        # The unchanged integration selftest must not whole-archive eval/reports/tasks.
        r.materialize_sut_snapshot = lambda *args, **kw: str(roots["v0.1"])
        assert c.integration_selftest() == 0
    finally:
        r.materialize_sut_snapshot = original
    fake = fake_test(roots, inventories)
    readiness_fake = readiness_fake_test()
    assert identity() == CANDIDATES["v0.2"][0] and not RUN_ROOT.exists()
    # Exactly one additional readiness conversation under the recovery addendum.
    ready = readiness()
    persist_readiness(ready, Path(__file__).with_name("README.md"))
    report = {"status": "PASS" if ready["ok"] else "BLOCKED_READINESS_DIAGNOSED", "syntax": "PASS", "stage10_selftest": "38/38",
              "stage10_integration_selftest": "9/9", "adapter_fake_provider": fake,
              "readiness_fake_provider": readiness_fake,
              "recovery_task_source_sha": "3be72546265bcd8ace0aa538ed628888ac136468",
              "prior_readiness_check_count": 1,
              "readiness_check_count": 1, "readiness": ready,
              "adapter_sha256": c.sha256_file(__file__), "stage10_working_hashes": hashes,
              "public_input_sha256": {cid: x["sha256"] for cid, x in payloads.items()},
              "snapshot_files_sha256": inventories, "tracked_clean": True,
              "paired_root_absent": True, "initial_head": CANDIDATES["v0.2"][0]}
    c.atomic_write(record, json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    if not ready["ok"]:
        raise c.ControllerError("BLOCKED_READINESS_DIAGNOSED: " + ready["category"])
    return 0


def measured(record):
    freeze = identity()
    assert re.fullmatch(r"[0-9a-f]{40}", os.environ.get("STAGE11_PAIRED_AUTH_SHA", ""))
    assert os.environ["STAGE11_PAIRED_AUTH_SHA"] == freeze, "measured authorization SHA mismatch"
    assert git("rev-parse", "HEAD^").decode().strip() == CANDIDATES["v0.2"][0], "freeze parent mismatch"
    assert set(git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").decode().splitlines()) <= {"eval/stage11/harness/paired_holdout.py", "eval/stage11/harness/README.md"}
    assert not RUN_ROOT.exists(), "paired run root already exists"
    gate_report = json.loads(record.read_text(encoding="utf-8"))
    assert gate_report["status"] == "PASS" and gate_report["readiness_check_count"] == 1
    assert gate_report["adapter_sha256"] == c.sha256_file(__file__), "adapter changed after gate"
    assert frozen_hashes() == gate_report["stage10_working_hashes"]
    payloads = public_payloads()
    assert {cid: item["sha256"] for cid, item in payloads.items()} == gate_report["public_input_sha256"]
    roots, inventories = snapshots()
    assert inventories == gate_report["snapshot_files_sha256"]
    assert identity() == freeze and not RUN_ROOT.exists()
    metas = {}
    with c.RunLock(RUN_ROOT / "controller.lock"):
        stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
        for version in CANDIDATES:
            run_id = f"stage11-{stamp}-{freeze[:8]}-{version}"
            print(f"START {version} run_id={run_id}", flush=True)
            metas[version] = run_version(RUN_ROOT / version, version, run_id, freeze,
                                         roots[version], inventories[version], payloads, gate_report)
            pair = reconcile_pair(RUN_ROOT, metas, payloads)
            c.atomic_write(RUN_ROOT / "PAIR_STATUS.json", json.dumps(pair, ensure_ascii=False, indent=2))
            if metas[version]["status"] != "COMPLETE" or pair["status"] == "HOLD_INTEGRITY_REVIEW":
                break
        print(json.dumps(pair, ensure_ascii=False, indent=2), flush=True)
    return 0 if pair["status"] == "COMPLETE" else 7


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=("gate", "measured"))
    ap.add_argument("--gate-record", type=Path, required=True)
    args = ap.parse_args()
    assert os.environ.get("PYTHONDONTWRITEBYTECODE") == "1" and sys.dont_write_bytecode
    return gate(args.gate_record) if args.command == "gate" else measured(args.gate_record)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"BLOCKED: {type(exc).__name__}: {exc}", flush=True)
        sys.exit(4)
