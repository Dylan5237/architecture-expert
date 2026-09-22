# Stage 10 API Runner Harness (Phase C0)

Isolated direct-model evaluation harness for the frozen Architecture Expert Agent v0.1.

## What this is

- `runner.py` — SUT snapshot materialization (`git archive` of the frozen SUT SHA into a temp dir), path sandbox, the single evaluated-model tool, fresh per-case conversation loop, and the Phase C0 preflight + sandbox selftest.
- `provider_openai_compatible.py` — minimal OpenAI-compatible chat-completions adapter (SYSTEM messages + function/tool calling, stateless per call).

## Isolation guarantees (by construction)

1. SYSTEM slot 1 = exact `agent/system-prompt-v0.1.md`; SYSTEM slot 2 = exact selected `agent/modes/<MODE>.md`; USER = exact public case payload. Both contracts verbatim, never paraphrased.
2. Every case = a brand-new messages array; no conversation/session/previous-response IDs ever sent.
3. Exactly one tool exposed to the evaluated model: `read_sut_file` (relative path, single file, read-only, SUT snapshot only, per-call and per-case byte budgets).
4. Denied by sandbox: `eval/**`, `.git/**`, `tasks/**`, traversal (`..`), absolute paths, anything outside the snapshot. No web/shell/list/write/git/env tools.
5. The SUT snapshot is materialized from exactly `96d9ae3...` — never the moving branch; private eval material is absent by construction (asserted at materialization).

## Configuration

Environment (preferred): `STAGE10_API_BASE_URL`, `STAGE10_API_KEY`, `STAGE10_MODEL`, optional `STAGE10_API_HEADERS_JSON` (non-secret headers only).

If env is unset, the harness bridges provider config at runtime from the local `~/.opencodex/config.json` registry (`kimi-code` OpenAI-compatible endpoint). Secrets are read at runtime, never printed, never committed.

## Usage

    python runner.py selftest    -- sandbox unit checks (no model call)
    python runner.py preflight   -- full P0-1..P0-8 preflight incl. one synthetic call
    python runner.py run-case --case-file <public-case.md> --mode <MODE>   -- Phase C (not in C0)

Status and evidence are recorded in `PREFLIGHT.md`.
