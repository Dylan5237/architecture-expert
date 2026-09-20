---
id: DOMAIN-RESOURCES
type: domain-index
stage: 7
---
# Domain: resources

## Scope
Per-work execution/wait/retention/retry/queue/concurrency/memory/fan-out bounds. System lifetime may be indefinite.

## AX / MP
MP-003. Peer to MP-009 (overload domain). D-04: do not merge.

## FP
FP-003

## T
T-003, T-004, T-005 (retry bound aspect)

## GC
GC-002, GC-004

## Cross-domain
overload (policy vs bound); lifecycle (D-07).

## Gaps
Do not lend Little's Law coverage to MP-009.

## Exclusions
Overload admission/shedding as if they were bounds. USE method / SLO nodes (not instantiated).
