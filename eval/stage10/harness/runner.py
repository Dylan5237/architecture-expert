#!/usr/bin/env python3
"""Stage 10 Phase C0 isolated API runner harness.

Builds a fresh, isolated direct-model conversation per case:
- SYSTEM slot 1: exact frozen agent/system-prompt-v0.1.md
- SYSTEM slot 2: exact selected agent/modes/<MODE>.md
- USER message:  exact PUBLIC case payload
- One evaluated-model tool: read_sut_file (read-only, SUT snapshot only)

No web/shell/list/write/git tools. No conversation reuse. No private eval material.

This file is evaluation infrastructure; it adds no Agent semantics.
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath

from provider_openai_compatible import OpenAICompatibleProvider

SUT_SHA = "96d9ae333ffc5a8076d635b86634b5151ec0bbc5"
PUBLIC_PACK_SHA = "23a49382c949702446325d30e18d3321d8550c36"

MODE_FILES = {
    "AUTO": "agent/modes/AUTO.md",
    "ARCH_DESIGN": "agent/modes/ARCH_DESIGN.md",
    "ARCH_REVIEW": "agent/modes/ARCH_REVIEW.md",
    "CHANGE_REVIEW": "agent/modes/CHANGE_REVIEW.md",
    "ADR_REVIEW": "agent/modes/ADR_REVIEW.md",
    "INCIDENT_ANALYSIS": "agent/modes/INCIDENT_ANALYSIS.md",
}

REQUIRED_SUT_FILES = [
    "agent/system-prompt-v0.1.md",
    "agent/modes/AUTO.md",
    "agent/modes/ARCH_DESIGN.md",
    "agent/modes/ARCH_REVIEW.md",
    "agent/modes/CHANGE_REVIEW.md",
    "agent/modes/ADR_REVIEW.md",
    "agent/modes/INCIDENT_ANALYSIS.md",
    "00_ROUTER.md",
    "01_CONSTITUTION.md",
    "02_VOCABULARY.md",
    "decision-playbooks/index.md",
    "question-bank/index.md",
    "cases/good-cases/index.md",
    "relationship-map.yaml",
]

MAX_FILE_BYTES = 200_000          # per read_sut_file call
TOTAL_READ_BUDGET = 2_000_000     # per case, all reads combined
MAX_TOOL_ROUNDS = 24              # per case


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def materialize_sut_snapshot(repo_root: Path, dest: Path) -> None:
    """git archive SUT_SHA into dest (read-only materialization)."""
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "archive", SUT_SHA],
        cwd=repo_root,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout  # validate the archive builds
    tar = subprocess.Popen(
        ["git", "archive", SUT_SHA],
        cwd=repo_root,
        stdout=subprocess.PIPE,
    )
    subprocess.run(["tar", "-x", "-C", str(dest)], stdin=tar.stdout, check=True)
    tar.stdout.close()
    if tar.wait() != 0:
        raise RuntimeError("git archive failed")
    missing = [f for f in REQUIRED_SUT_FILES if not (dest / f).is_file()]
    if missing:
        raise RuntimeError(f"SUT snapshot missing required files: {missing}")
    # private eval material must NOT exist in the snapshot
    # eval/ and .git/ must not exist in the frozen SUT tree at all;
    # tasks/ exists legitimately (historical prompts) and is denied to the model by PathSandbox.
    for forbidden in ["eval", ".git"]:
        if (dest / forbidden).exists():
            raise RuntimeError(f"forbidden path present in snapshot: {forbidden}/")


class PathSandbox:
    """Read-only, single-file, allowlisted file access rooted at the SUT snapshot."""

    def __init__(self, root: Path):
        self.root = root.resolve()
        self.total_read = 0

    def read_file(self, rel_path: str) -> str:
        p = PurePosixPath(rel_path)
        if p.is_absolute() or rel_path.startswith("/") or rel_path.startswith("\\"):
            return "ERROR: absolute paths are not allowed"
        parts = p.parts
        if ".." in parts:
            return "ERROR: path traversal is not allowed"
        if not parts:
            return "ERROR: empty path"
        top = parts[0]
        if top in {"eval", ".git", "tasks"}:
            return f"ERROR: access to {top}/ is not allowed in this evaluation"
        target = (self.root / Path(*parts)).resolve()
        try:
            target.relative_to(self.root)
        except ValueError:
            return "ERROR: path escapes the SUT snapshot"
        if not target.is_file():
            return "ERROR: not a file (or not present) in the SUT snapshot"
        size = target.stat().st_size
        if size > MAX_FILE_BYTES:
            return "ERROR: file exceeds per-call size cap"
        if self.total_read + size > TOTAL_READ_BUDGET:
            return "ERROR: per-case total read budget exceeded"
        self.total_read += size
        return target.read_text(encoding="utf-8", errors="replace")


TOOL_SPEC = [{
    "type": "function",
    "function": {
        "name": "read_sut_file",
        "description": (
            "Read one UTF-8 file from the frozen Architecture Expert SUT snapshot "
            "( Constitution, router, mode files, decision playbooks, question bank, "
            "domains, principles, failure patterns, tactics, good cases, relationship map, sources ). "
            "Relative paths only. One file per call. No directory listing."
        ),
        "parameters": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "Repository-relative file path, e.g. 00_ROUTER.md"}},
            "required": ["path"],
        },
    },
}]


def load_provider():
    """Resolve provider config from env; optionally bridge from the local
    opencodex provider registry (runtime only; secrets never printed/committed)."""
    base = os.environ.get("STAGE10_API_BASE_URL")
    key = os.environ.get("STAGE10_API_KEY")
    model = os.environ.get("STAGE10_MODEL")
    source = "env"
    if not (base and key and model):
        reg = Path.home() / ".opencodex" / "config.json"
        if reg.is_file():
            cfg = json.loads(reg.read_text(encoding="utf-8"))
            p = cfg.get("providers", {}).get("kimi-code")
            if p and p.get("adapter") == "openai-chat":
                base = base or p["baseUrl"]
                key = key or p["apiKey"]
                model = model or p.get("defaultModel", "kimi-for-coding-highspeed")
                source = "opencodex-registry:kimi-code"
    if not (base and key and model):
        raise RuntimeError("BLOCKED_CONFIG: no STAGE10_API_BASE_URL/KEY/MODEL and no bridged provider")
    return OpenAICompatibleProvider(base, key, model), source


def run_case(provider, case_payload: str, requested_mode: str, sandbox_root: Path,
             max_rounds: int = MAX_TOOL_ROUNDS):
    """One fresh, isolated conversation. Returns (messages_sent_summary, final_text, tool_log)."""
    system_prompt = (sandbox_root / "agent/system-prompt-v0.1.md").read_text(encoding="utf-8")
    mode_file = MODE_FILES[requested_mode]
    mode_text = (sandbox_root / mode_file).read_text(encoding="utf-8")

    sandbox = PathSandbox(sandbox_root)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": mode_text},
        {"role": "user", "content": case_payload},
    ]
    tool_log = []
    final_text = ""
    for _round in range(max_rounds):
        resp = provider.chat(messages=messages, tools=TOOL_SPEC)
        msg = resp["choices"][0]["message"]
        finish = resp["choices"][0].get("finish_reason")
        if msg.get("tool_calls"):
            messages.append(msg)
            for tc in msg["tool_calls"]:
                if tc.get("type") != "function" or tc["function"]["name"] != "read_sut_file":
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc["id"],
                        "content": "ERROR: only read_sut_file is available",
                    })
                    tool_log.append((tc["function"]["name"], 0, "rejected-unknown-tool"))
                    continue
                try:
                    args = json.loads(tc["function"]["arguments"] or "{}")
                except json.JSONDecodeError:
                    args = {}
                rel = str(args.get("path", ""))
                content = sandbox.read_file(rel)
                nbytes = len(content.encode("utf-8")) if not content.startswith("ERROR") else 0
                tool_log.append((rel, nbytes, "ok" if not content.startswith("ERROR") else "denied"))
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "content": content,
                })
            continue
        final_text = msg.get("content") or ""
        if finish != "tool_calls":
            break
    return {
        "system_prompt_sha256": hashlib.sha256((sandbox_root / "agent/system-prompt-v0.1.md").read_bytes()).hexdigest(),
        "mode_file": mode_file,
        "mode_sha256": hashlib.sha256((sandbox_root / mode_file).read_bytes()).hexdigest(),
        "rounds_used": _round + 1,
        "final_text": final_text,
        "tool_log": tool_log,
    }


PRE10_SMOKE = """id: PRE10-SMOKE
title: Synthetic smoke probe (never scored)
task_object: tiny architecture question answerable from the SUT knowledge base
requested_mode: AUTO
user_request: You are evaluating a knowledge base. Read the repository file 00_ROUTER.md with your read tool, then answer in one short sentence: what is the first default load step named in that router?
project_evidence: {}
constraints: []
notes_for_runner: Synthetic probe; contains no suite knowledge; never scored.
"""


def preflight(repo_root: Path) -> dict:
    report = {"status": "PASS", "sut_sha": SUT_SHA, "public_pack_sha": PUBLIC_PACK_SHA}
    tmp = Path(tempfile.mkdtemp(prefix="stage10-sut-"))
    try:
        materialize_sut_snapshot(repo_root, tmp)
        report["sut_snapshot"] = {"mechanism": f"git archive {SUT_SHA} -> temp dir", "root": str(tmp)}

        # P0-1/P0-2 hashes
        sp = tmp / "agent/system-prompt-v0.1.md"
        mf = tmp / "agent/modes/AUTO.md"
        report["system_prompt_sha256"] = sha256_file(sp)
        report["mode_contract"] = {"file": "agent/modes/AUTO.md", "sha256": sha256_file(mf)}

        # P0-6 forbidden reads (direct sandbox tests, no model involvement)
        sb = PathSandbox(tmp)
        forbidden_tests = {
            "../outside": sb.read_file("../outside"),
            "eval/stage10/public/E10-001.md": sb.read_file("eval/stage10/public/E10-001.md"),
            "C:/Windows/win.ini": sb.read_file("C:/Windows/win.ini"),
        }
        report["forbidden_reads"] = {k: v.startswith("ERROR") for k, v in forbidden_tests.items()}
        if not all(report["forbidden_reads"].values()):
            report["status"] = "BLOCKED_ISOLATION"
            return report

        # P0-5 allowed read
        allowed = sb.read_file("00_ROUTER.md")
        report["allowed_read"] = {"path": "00_ROUTER.md", "ok": allowed.startswith("#") or len(allowed) > 100}

        # P0-7 private eval absence
        priv = [p for p in ["private/oracle.yaml", "private/coverage.yaml", "eval/stage10/design"] if (tmp / p).exists()]
        report["private_eval_absent"] = not priv

        # provider + synthetic call (P0-3/4/8)
        try:
            provider, source = load_provider()
        except RuntimeError as e:
            report["status"] = "BLOCKED_CONFIG"
            report["blocker"] = str(e)
            return report
        report["provider_source"] = source
        result = run_case(provider, PRE10_SMOKE, "AUTO", tmp, max_rounds=4)
        report["smoke"] = {
            "system_sha_ok": result["system_prompt_sha256"] == report["system_prompt_sha256"],
            "mode_sha_ok": result["mode_sha256"] == report["mode_contract"]["sha256"],
            "rounds": result["rounds_used"],
            "tool_log": [{"path": p, "bytes": b, "status": s} for p, b, s in result["tool_log"]],
            "read_router_attempted": any(p == "00_ROUTER.md" for p, _, _ in result["tool_log"]),
            "final_text_head": result["final_text"][:200],
        }
        if not result["final_text"]:
            report["status"] = "BLOCKED_PROVIDER_CAPABILITY"
            report["blocker"] = "synthetic call produced no final text"
        return report
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["preflight", "run-case", "selftest"])
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--case-file")
    ap.add_argument("--mode")
    args = ap.parse_args()
    repo = Path(args.repo_root).resolve()

    if args.command == "selftest":
        tmp = Path(tempfile.mkdtemp(prefix="stage10-sut-"))
        try:
            materialize_sut_snapshot(repo, tmp)
            sb = PathSandbox(tmp)
            checks = {
                "allowed_00_ROUTER.md": not sb.read_file("00_ROUTER.md").startswith("ERROR"),
                "deny_traversal": sb.read_file("../x").startswith("ERROR"),
                "deny_eval": sb.read_file("eval/stage10/public/E10-001.md").startswith("ERROR"),
                "deny_absolute": sb.read_file("C:/x").startswith("ERROR"),
                "deny_git": sb.read_file(".git/config").startswith("ERROR"),
                "deny_tasks": sb.read_file("tasks/stage10/CODEX_API_RUNNER_PREFLIGHT.md").startswith("ERROR"),
                "deny_missing": sb.read_file("no/such/file.md").startswith("ERROR"),
            }
            for k, v in checks.items():
                print(f"{'PASS' if v else 'FAIL'} {k}")
            sys.exit(0 if all(checks.values()) else 1)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    if args.command == "preflight":
        print(json.dumps(preflight(repo), indent=2))
        return

    if args.command == "run-case":
        if not (args.case_file and args.mode):
            ap.error("run-case needs --case-file and --mode")
        payload = Path(args.case_file).read_text(encoding="utf-8")
        provider, _ = load_provider()
        tmp = Path(tempfile.mkdtemp(prefix="stage10-sut-"))
        try:
            materialize_sut_snapshot(repo, tmp)
            result = run_case(provider, payload, args.mode, tmp)
            print(json.dumps(result, indent=2, ensure_ascii=False))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
