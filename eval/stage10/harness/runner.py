"""Stage 10 reference runner: fresh per-case execution against the frozen SUT snapshot.

No E10 case is executed by this module; it only provides the machinery.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile

from provider_openai_compatible import (
    REQUIRED_MAX_TOKENS,
    REQUIRED_MODEL,
    REQUIRED_TEMPERATURE,
    ProviderError,
    ReferenceProvider,
    session_header,
)

SUT_SHA = "96d9ae333ffc5a8076d635b86634b5151ec0bbc5"
REQUIRED_SUT_FILES = [
    "00_ROUTER.md",
    "01_CONSTITUTION.md",
    "agent/system-prompt-v0.1.md",
    "agent/modes/AUTO.md",
    "agent/modes/ARCH_DESIGN.md",
    "agent/modes/ARCH_REVIEW.md",
    "agent/modes/CHANGE_REVIEW.md",
    "agent/modes/ADR_REVIEW.md",
    "agent/modes/INCIDENT_ANALYSIS.md",
]
PER_CALL_BYTE_CAP = 200_000
PER_CASE_TOTAL_BUDGET = 2_000_000
TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "read_sut_file",
        "description": "Read exactly one file from the frozen SUT snapshot. Relative paths only. No directory listing.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Relative path inside the SUT snapshot, e.g. 00_ROUTER.md",
                }
            },
            "required": ["path"],
        },
    },
}


def materialize_sut_snapshot(sut_sha: str = SUT_SHA, dest: str | None = None) -> str:
    """Create a read-only SUT snapshot from exactly the frozen SUT SHA via git archive."""
    root = dest or tempfile.mkdtemp(prefix="stage10-sut-")
    os.makedirs(root, exist_ok=True)
    proc = subprocess.run(
        ["git", "archive", sut_sha],
        capture_output=True,
        cwd=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")),
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git archive failed for {sut_sha}: {proc.stderr.decode('utf-8', 'replace')[:200]}")
    # git archive produces tar; extract with tarfile
    import tarfile
    import io

    with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as tf:
        tf.extractall(root)
    missing = [f for f in REQUIRED_SUT_FILES if not os.path.isfile(os.path.join(root, f))]
    if missing:
        raise RuntimeError(f"SUT snapshot missing required files: {missing}")
    return root


class PathSandbox:
    """Path sandbox for the single model-visible tool."""

    def __init__(self, root: str, per_call_cap: int = PER_CALL_BYTE_CAP,
                 total_budget: int = PER_CASE_TOTAL_BUDGET) -> None:
        self.root = os.path.realpath(root)
        self.per_call_cap = per_call_cap
        self.total_budget = total_budget
        self.consumed = 0

    def check(self, rel_path: str) -> tuple[bool, str]:
        """Return (allowed, reason). Pure policy check without reading."""
        if not isinstance(rel_path, str) or not rel_path:
            return False, "deny: empty path"
        if os.path.isabs(rel_path) or re.match(r"^[A-Za-z]:", rel_path):
            return False, "deny: absolute path"
        if ntpath_backslash(rel_path):
            return False, "deny: backslash path"
        if ".." in rel_path.split("/"):
            return False, "deny: traversal"
        top = rel_path.split("/")[0]
        if top in (".git", "tasks", "eval"):
            return False, "deny: forbidden top-level directory"
        if rel_path.startswith(("eval/", ".git/", "tasks/")):
            return False, "deny: forbidden prefix"
        real = os.path.realpath(os.path.join(self.root, rel_path))
        if not real.startswith(self.root + os.sep):
            return False, "deny: outside snapshot"
        if not os.path.isfile(real):
            return False, "deny: not a file"
        return True, "allow"

    def read(self, rel_path: str) -> tuple[bool, str, int]:
        """Policy check then capped read. Returns (ok, content_or_reason, nbytes)."""
        ok, reason = self.check(rel_path)
        if not ok:
            return False, reason, 0
        real = os.path.realpath(os.path.join(self.root, rel_path))
        size = os.path.getsize(real)
        if size > self.per_call_cap:
            return False, f"deny: file exceeds per-call cap ({size} > {self.per_call_cap})", 0
        if self.consumed + size > self.total_budget:
            return False, f"deny: per-case aggregate budget exceeded ({self.consumed}+{size} > {self.total_budget})", 0
        try:
            with open(real, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read()
        except OSError as exc:
            return False, f"deny: read error ({exc.__class__.__name__})", 0
        self.consumed += size
        return True, content, size


def ntpath_backslash(p: str) -> bool:
    return "\\" in p


class CaseRunner:
    """One fresh case execution: new messages list, no prior state."""

    def __init__(self, provider: ReferenceProvider, sandbox_root: str,
                 system_prompt: str, mode_contract: str) -> None:
        if not system_prompt or not system_prompt.strip():
            raise ValueError("system prompt must be non-empty")
        if not mode_contract or not mode_contract.strip():
            raise ValueError("mode contract must be non-empty")
        self.provider = provider
        self.sandbox = PathSandbox(sandbox_root)
        self.system_prompt = system_prompt
        self.mode_contract = mode_contract
        self.tool_log: list[dict] = []

    def run_case(self, case_id: str, run_id: str, user_payload: str,
                 max_tool_rounds: int = 8) -> dict:
        """Fresh conversation. Returns result dict with final content + technical log."""
        if not user_payload or not user_payload.strip():
            raise ValueError("case payload must be non-empty")
        session = session_header(run_id, case_id)
        messages: list[dict] = [
            {"role": "system", "content": self.system_prompt},
            {"role": "system", "content": self.mode_contract},
            {"role": "user", "content": user_payload},
        ]
        rounds = 0
        final_content = ""
        finish_reason = None
        while rounds < max_tool_rounds:
            rounds += 1
            data = self.provider.chat(
                messages,
                tools=[TOOL_SCHEMA],
                tool_choice="auto",
                session=session,
                temperature=REQUIRED_TEMPERATURE,
                max_tokens=REQUIRED_MAX_TOKENS,
            )
            choices = data.get("choices") or []
            if not choices:
                raise ProviderError("provider returned no choices")
            msg = choices[0].get("message") or {}
            finish_reason = choices[0].get("finish_reason")
            tool_calls = msg.get("tool_calls") or []
            if not tool_calls:
                final_content = (msg.get("content") or "").strip()
                break
            messages.append(msg)
            for tc in tool_calls:
                fn = (tc.get("function") or {})
                name = fn.get("name", "")
                try:
                    args = json.loads(fn.get("arguments") or "{}")
                except ValueError:
                    args = {}
                if name != "read_sut_file":
                    result = {"error": "unknown tool"}
                    nbytes = 0
                    self.tool_log.append({"case": case_id, "tool": name, "path": None, "bytes": 0, "result": "deny: unknown tool"})
                else:
                    path = str(args.get("path") or "")
                    ok, content, nbytes = self.sandbox.read(path)
                    result = {"content": content} if ok else {"error": content}
                    self.tool_log.append({"case": case_id, "tool": name, "path": path, "bytes": nbytes, "result": "allow" if ok else content})
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.get("id"),
                    "content": json.dumps(result)[:200_000],
                })
        else:
            final_content = ""
            finish_reason = "max_tool_rounds"
        return {
            "case_id": case_id,
            "session": session,
            "rounds": rounds,
            "finish_reason": finish_reason,
            "final_content": final_content,
            "requested_model": REQUIRED_MODEL,
            "observed_model": None,  # filled by caller from last response if desired
            "tool_log": list(self.tool_log),
        }
