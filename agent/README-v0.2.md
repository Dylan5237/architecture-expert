---
id: AGENT-README-V0.2
type: agent-invocation
stage: 11
status: CANDIDATE / HOLDOUT_UNEVALUATED
issue: 24
---
# Agent v0.2

Provider-independent Architecture Expert candidate. **CANDIDATE / HOLDOUT_UNEVALUATED**; no evaluation result is claimed.

## Runtime contract

- Active system prompt: `agent/system-prompt-v0.2.md`.
- Reuse the five existing explicit mode contracts under `agent/modes/` unchanged:
  - `ARCH_DESIGN` → DP-001
  - `ARCH_REVIEW` → DP-002
  - `CHANGE_REVIEW` → DP-003
  - `ADR_REVIEW` → DP-004
  - `INCIDENT_ANALYSIS` → DP-005
- `AUTO` remains the router: identify the object, select exactly one primary DP, then activate only justified overlays. It is not a sixth reasoning procedure. If AUTO and an explicit mode are both supplied, the explicit mode wins.
- Modes use the repository Constitution, domain knowledge, decision playbooks, question bank, and linked principles, failure patterns, tactics, and good cases through progressive disclosure. Do not load the whole repository.
- For project-specific work, provide accepted product intent, architecture decisions, current code/config/tests/runtime evidence, and the relevant change when available. Generic knowledge explains mechanisms; it does not establish project facts.

The shared typed fields and output contract remain defined by the active system prompt and repository knowledge. A finding describes a load-bearing local result; `terminal_outcome` describes why the pass stopped. A blocker can coexist with `MIN_SAFE_FIX_IDENTIFIED`.

Any host that can supply the active system prompt, the selected mode file, and repository file access can run this contract. No provider-specific setup is specified or required.
