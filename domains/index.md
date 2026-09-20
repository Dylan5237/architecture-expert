---
id: IDX-DOMAINS
type: domain-index
stage: 7
---
# domains/

Retrieval taxonomy for sealed Constitution knowledge. Folders exist only when they route to MP/FP/T/GC. Candidate families from Issue #18 that did **not** earn a folder: `boundaries/` (cross-cuts evolution/reliability/security/integration), `runtime/` (split into lifecycle + concurrency), `performance/` and `scalability/` (no independent causal MP; resources/overload cover capacity), `distributed/` (cross-cuts reliability/state-data/concurrency).

| Domain | Primary MP | Open when the need is |
|---|---|---|
| [lifecycle](lifecycle/index.md) | MP-001 | owner, cleanup, cancel, orphan |
| [evolution](evolution/index.md) | MP-002 | change-decision boundary; P-006 signal |
| [resources](resources/index.md) | MP-003 | per-work bounds |
| [reliability](reliability/index.md) | MP-004 | failure domain / cascade |
| [security](security/index.md) | MP-005 | trust, privilege, agent action |
| [observability](observability/index.md) | MP-006 | evidence vs proof |
| [integration](integration/index.md) | MP-007 | independent-consumer contract |
| [state-data](state-data/index.md) | MP-008 | authority × conflict |
| [overload](overload/index.md) | MP-009 | admission/backpressure/shedding/degradation/retry storm |
| [concurrency](concurrency/index.md) | MP-010 | assumed vs provided guarantees |

`decision-making` is Stage 8. AX-* stay in `01_CONSTITUTION.md`.
