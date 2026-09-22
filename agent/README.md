---
id: AGENT-README-V0.1
type: agent-invocation
stage: 9
status: UNEVALUATED
issue: 24
---
# Agent v0.1

Provider-independent Architecture Expert compiled from sealed Stage 6–8 contracts.

**Status: unevaluated until Stage 10.** This is an invocation/behavior contract, not a benchmarked release.

## What it is

- Core behavior: `agent/system-prompt-v0.1.md`
- Modes: `agent/modes/`
- Knowledge: repository Constitution, domains, MP/FP/T/GC, Stage 8 DPs and question bank
- Reasoning: pre-routing + S1..S6 in `decision-playbooks/index.md`

It is not a pattern catalog, a provider SDK, or an evaluation harness.

## AUTO vs explicit mode

- **AUTO** — router only. Identifies the object, selects exactly one primary DP (DP-001..005), then zero or more overlays. Not a sixth reasoning procedure.
- **Explicit modes** — skip routing:
  - `ARCH_DESIGN` → DP-001
  - `ARCH_REVIEW` → DP-002
  - `CHANGE_REVIEW` → DP-003
  - `ADR_REVIEW` → DP-004
  - `INCIDENT_ANALYSIS` → DP-005

Overlays (concurrency, overload, reliability, …) are parameters on those modes, not extra mode files.

If both AUTO and an explicit mode are supplied, the explicit mode wins.

## What to attach when available

For project-specific work, provide or connect (as the host allows):

- accepted product intent (PRD, requirements);
- ADRs / accepted architecture decisions;
- current code, config, tests, runtime/incident evidence for the path in scope;
- the delta if the object is a change.

The Agent classifies these as PRODUCT_INTENT / ARCHITECTURE_INTENT / CODE / CONFIG / TEST / RUNTIME / HISTORY. USER_ASSERTION stays unverified until grounded. GENERIC_KNOWLEDGE from this repository explains mechanisms; it does not override project facts.

## Progressive disclosure

The Agent must not load the whole repository. Default: Router → Constitution → one DP → activated question sections → one or two domain indexes → linked nodes → relevant GC → named RQ/sources only if needed. Stage reports are not default runtime context.

## How to read the close

`finding_disposition` classifies load-bearing findings (BLOCKER/MUST_FIX, HIGH_CONFIDENCE_RISK, NEEDS_EVIDENCE, NON_BLOCKING_IMPROVEMENT, PERSONAL_PREFERENCE).

`terminal_outcome` is why the **pass** stopped (NO_DEFECT, MIN_SAFE_FIX_IDENTIFIED, NEEDS_EVIDENCE, OWNER_TRADE_OFF, ARCH_CONFLICT, NO_DECISION_CHANGING_WORK). A BLOCKER finding may coexist with MIN_SAFE_FIX_IDENTIFIED.

BLOCKER and HIGH_CONFIDENCE_RISK must include `refutation_or_invalidation`.

## Hosting

Any host that can supply this system prompt, the selected mode file, and repository file access. No provider-specific setup is specified or required.
