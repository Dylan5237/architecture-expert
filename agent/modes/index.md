---
id: IDX-AGENT-MODES-V0.1
type: agent-mode-index
stage: 9
status: UNEVALUATED
issue: 24
---
# agent/modes/

Thin mode contracts. Reasoning procedures live in `decision-playbooks/`. Overlays live in `decision-playbooks/index.md` and are **not** modes.

| Mode | Role | Stage 8 DP |
|---|---|---|
| [AUTO](AUTO.md) | Router only | none (selects exactly one of the five) |
| [ARCH_DESIGN](ARCH_DESIGN.md) | Forward synthesis | DP-001 |
| [ARCH_REVIEW](ARCH_REVIEW.md) | Existing system as-is | DP-002 |
| [CHANGE_REVIEW](CHANGE_REVIEW.md) | Delta / PR / migration | DP-003 |
| [ADR_REVIEW](ADR_REVIEW.md) | Named decision / ADR | DP-004 |
| [INCIDENT_ANALYSIS](INCIDENT_ANALYSIS.md) | Observed failure | DP-005 |

Do not add CONCURRENCY_REVIEW, PERFORMANCE_REVIEW, FAILURE_REVIEW, INTEGRATION_REVIEW, TRUST_REVIEW, or similar personas. Those are overlays on ARCH_REVIEW / CHANGE_REVIEW / INCIDENT_ANALYSIS.

Shared behavior (spine, typed fields, GC gate, drift, ARCH_CONFLICT, stop/escalation, min correction) is in `agent/system-prompt-v0.1.md` and `decision-playbooks/index.md`. Mode files must not duplicate it.
