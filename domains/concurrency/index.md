---
id: DOMAIN-CONCURRENCY
type: domain-index
stage: 7
---
# Domain: concurrency

## Scope
Correctness vs execution-model guarantees: assumed ≠ provided timing/order/cancel/clock.

## AX / MP
MP-010.

## FP
FP-012 (and FP-001 when stale work is ownerless rather than mis-modeled)

## T
None instantiated for MP-010. T-001/T-002 appear when the structure is ownership.

## GC
GC-016

## Cross-domain
lifecycle (D-02); state-data (D-09); observability (D-11).

## Gaps
RQ5-002, RQ5-005

## Exclusions
Tautological “correct systems use true guarantees.” Document-every-assumption review rule.
