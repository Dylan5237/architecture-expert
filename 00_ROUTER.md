---
id: ROUTER
type: knowledge-router
stage: 7
status: CANONICAL
---
# 00_ROUTER

Progressive disclosure for this repository. Navigation only. Not a playbook, system prompt, or evaluation procedure.

## Load order

1. `01_CONSTITUTION.md` — AX-001..AX-004 and MP-001..MP-010 semantics.
2. `domains/index.md` — pick the domain that matches the knowledge need.
3. That domain index — load only linked MP / FP / T / GC IDs.
4. Atomic pages under `principles/MP-*`, `failure-patterns/FP-*`, `tactics/T-*`.
5. `cases/good-cases/index.md` when a surface looks like a violation.
6. `review-queue.yaml` when an MP/FP/T names an RQ.
7. `sources/S-*.md` only for disputed, high-risk, or low-confidence claims.
8. `relationship-map.yaml` when a relation, distinction, or gap must be machine-checked.

Do not load the whole corpus for a focused question.

## Need → first domain

| Need | Domain |
|---|---|
| ownership, cleanup, cancellation, orphan work | `domains/lifecycle/` |
| module/change-decision boundaries; change amplification as review signal | `domains/evolution/` |
| per-work time/queue/retry/concurrency/memory/fan-out bounds | `domains/resources/` |
| failure-domain partitioning; blast radius as outcome | `domains/reliability/` |
| trust boundary, privilege, agent action authority | `domains/security/` |
| diagnostic evidence obtainability vs proof scope | `domains/observability/` |
| independent-consumer contracts and migration | `domains/integration/` |
| write/state authority and conflict/consistency (V-010 suffix) | `domains/state-data/` |
| overload path; admission / backpressure / shedding / degradation | `domains/overload/` |
| assumed vs model-provided timing/order/cancel/clock guarantees | `domains/concurrency/` |

## Standing constraints

- Constitution is authoritative for AX/MP meaning. Historical `principles/P-*.md` are immutable candidates.
- AX-005 and MP-011 IDs are reserved. P-006 is not a principle.
- failure domain ≠ blast radius. backpressure ≠ load shedding ≠ admission control ≠ degradation. retry ≠ idempotency. flow control ≠ backpressure.
- Project code/config/runtime/ADRs remain authoritative for a real system's current facts.
- Gaps stay gaps. Do not invent support.

See `reports/STAGE7_KNOWLEDGE_ARCHITECTURE.md` for inventory and retrieval demonstrations.
