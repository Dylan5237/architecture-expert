"""Stage 10 reference runner: fresh per-case execution against the frozen SUT snapshot.

No E10 case is executed by this module; it only provides the machinery.
R2 wiring: verbatim final text, observed-model capture, max_tool_rounds=24.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile

from provider_openai_compatible import (
    REQUIRED_MAX_TOKENS,
    REQUIRED_MODEL,
    REQUIRED_TEMPERATURE,
    TECHNICAL_RESPONSE_KEY,
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
MEASURED_MAX_TOOL_ROUNDS = 24
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

ROUND_DIAGNOSTIC_FIELDS = (
    "transport_attempt_count", "transport_retry_count", "retry_errors", "http_status",
    "observed_model", "finish_reason", "content_field_present", "content_present",
    "content_length", "reasoning_present", "reasoning_length", "usage_summary",
)


def _round_diagnostics(metadata: dict | None) -> dict:
    """Copy the allowlisted technical fields; never carry provider reasoning text."""
    source = metadata if isinstance(metadata, dict) else {}
    out = {key: source.get(key) for key in ROUND_DIAGNOSTIC_FIELDS if key in source}
    retries = out.get("retry_errors")
    if isinstance(retries, list):
        out["retry_errors"] = [
            {
                key: error.get(key)
                for key in ("attempt", "error_class", "error_message", "http_status")
                if key in error
            }
            for error in retries if isinstance(error, dict)
        ]
    usage = out.get("usage_summary")
    if not isinstance(usage, dict):
        out["usage_summary"] = None
    return out


def materialize_sut_snapshot(sut_sha: str = SUT_SHA, dest: str | None = None) -> str:
    """Create a SUT snapshot from exactly the frozen SUT SHA via git archive."""
    root = dest or tempfile.mkdtemp(prefix="stage10-sut-")
    os.makedirs(root, exist_ok=True)
    repo_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
    proc = subprocess.run(
        ["git", "archive", sut_sha],
        capture_output=True,
        cwd=repo_root,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git archive failed for {sut_sha}: {proc.stderr.decode('utf-8', 'replace')[:200]}")
    import tarfile
    import io

    with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as tf:
        tf.extractall(root)
    missing = [f for f in REQUIRED_SUT_FILES if not os.path.isfile(os.path.join(root, f))]
    if missing:
        raise RuntimeError(f"SUT snapshot missing required files: {missing}")
    return root


def ntpath_backslash(p: str) -> bool:
    return "\\" in p


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


class CaseRunner:
    """One fresh case execution: new messages list, no prior state.

    R2-6: build a new CaseRunner per case and per retry.
    """

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
                 max_tool_rounds: int = MEASURED_MAX_TOOL_ROUNDS) -> dict:
        """Fresh conversation. Returns result dict with technical metadata.

        R2-7: final_content preserves the provider's final visible
        message.content string exactly as returned (no strip). The
        substantive check uses final_content.strip() != "" only for the
        attempt decision, never for the stored raw bytes.
        R2-8: observed model values are captured across rounds.
        R2-9: measured default ceiling is 24 tool rounds.
        """
        if not user_payload or not user_payload.strip():
            raise ValueError("case payload must be non-empty")
        session = session_header(run_id, case_id)
        messages: list[dict] = [
            {"role": "system", "content": self.system_prompt},
            {"role": "system", "content": self.mode_contract},
            {"role": "user", "content": user_payload},
        ]
        rounds = 0
        final_content: str = ""
        finish_reason = None
        observed_models: list[str | None] = []
        rounds_diagnostics: list[dict] = []

        def attach_case_diagnostics(exc: ProviderError) -> None:
            exc.case_diagnostics = {
                "rounds": rounds,
                "final_finish_reason": finish_reason,
                "substantive": False,
                "rounds_metadata": list(rounds_diagnostics),
            }

        while rounds < max_tool_rounds:
            rounds += 1
            try:
                data = self.provider.chat(
                    messages,
                    tools=[TOOL_SCHEMA],
                    tool_choice="auto",
                    session=session,
                    temperature=REQUIRED_TEMPERATURE,
                    max_tokens=REQUIRED_MAX_TOKENS,
                )
            except ProviderError as exc:
                round_meta = _round_diagnostics(exc.technical_metadata)
                rounds_diagnostics.append(round_meta)
                if round_meta.get("finish_reason") is not None:
                    finish_reason = round_meta["finish_reason"]
                attach_case_diagnostics(exc)
                raise
            round_meta = _round_diagnostics(data.get(TECHNICAL_RESPONSE_KEY))
            rounds_diagnostics.append(round_meta)
            observed_model = round_meta.get("observed_model", data.get("model"))
            observed_models.append(observed_model)
            choices = data.get("choices") or []
            if not choices:
                exc = ProviderError("provider returned no choices", round_meta)
                attach_case_diagnostics(exc)
                raise exc
            msg = choices[0].get("message") or {}
            finish_reason = choices[0].get("finish_reason")
            tool_calls = msg.get("tool_calls") or []
            if not tool_calls:
                content = msg.get("content")
                if content is None:
                    final_content = ""
                elif isinstance(content, str):
                    final_content = content
                else:
                    final_content = str(content)
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
        final_observed = None
        for m in reversed(observed_models):
            if m is not None:
                final_observed = m
                break
        return {
            "case_id": case_id,
            "session": session,
            "rounds": rounds,
            "finish_reason": finish_reason,
            "final_content": final_content,
            "substantive": final_content.strip() != "",
            "rounds_diagnostics": rounds_diagnostics,
            "requested_model": REQUIRED_MODEL,
            "observed_models": observed_models,
            "final_observed_model": final_observed,
            "tool_log": list(self.tool_log),
        }
