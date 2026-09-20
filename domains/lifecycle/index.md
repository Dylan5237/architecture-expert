---
id: DOMAIN-LIFECYCLE
type: domain-index
stage: 7
---
# Domain: lifecycle

## Scope
Runtime ownership of entities and mutable state: create/mutate/stop/cleanup, including cancellation. Not resource quantity bounds; not state conflict rules; not execution-model guarantees.

## AX / MP
MP-001. AX-001 still frames any evaluation.

## FP
FP-001

## T
T-001, T-002

## GC
GC-001, GC-002

## Cross-domain
resources (D-07 bounds vs ownership); concurrency (D-02 stale overwrite attribution); state-data (D-06).

## Gaps
RQ3-002

## Exclusions
GC heap reclamation is not semantic ownership. Mailbox capacity is MP-003.
