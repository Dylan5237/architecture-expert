---
id: IDX-TACTICS
type: index
stage: 7
---
# tactics/

Reusable **interventions/mechanisms**, not principles. Instantiated only where the sealed corpus supports a distinct mechanism.

| ID | Title | Distinct from |
|---|---|---|
| [T-001](T-001.md) | Supervised / Structured Lifecycle | generic process split; GC |
| [T-002](T-002.md) | Cancellation Propagation | timeout (T-003); kill |
| [T-003](T-003.md) | Timeout / Deadline Bound | cancellation; unbounded retry |
| [T-004](T-004.md) | Bounded Queue, Concurrency, Fan-out | overload policy (T-006..T-009) |
| [T-005](T-005.md) | Bounded Retry with Backoff/Jitter | idempotency (T-015); retry storm cause |
| [T-006](T-006.md) | Admission Control | T-007, T-008, T-009; priority scheduling |
| [T-007](T-007.md) | Backpressure | load shedding; flow control (broader related term) |
| [T-008](T-008.md) | Rejection / Load Shedding | backpressure; admission; degradation |
| [T-009](T-009.md) | Functional / Quality Degradation | shedding; isolation |
| [T-010](T-010.md) | Scoped Failure-Domain Isolation | generic process split; privilege reduction |
| [T-011](T-011.md) | Least-Privilege Restriction | MP-004 containment |
| [T-012](T-012.md) | Explicit Compatibility Direction and Migration Path | universal compatibility principle; expand-contract |
| [T-013](T-013.md) | Explicit Merge / Conflict Semantics | single-writer mandate; MP-001 ownership |
| [T-014](T-014.md) | Diagnostic Evidence Placement and Retention | telemetry-stack mandate |
| [T-015](T-015.md) | Idempotency under Explicit Delivery Semantics | retry |

Omitted on purpose: circuit breaker as a buzzword node (S-069 historical-background; S-056 not sufficient to add a durable node); expand-contract (RQ3-006); USE/SLO/hedged requests/event sourcing/strangler as extra files.
