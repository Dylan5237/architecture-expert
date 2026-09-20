---
id: DOMAIN-INTEGRATION
type: domain-index
stage: 7
---
# Domain: integration

## Scope
Contracts used by independent consumers: compatibility direction (reader/writer) and governed migration.

## AX / MP
MP-007. AX-002 is product-contract governance, not this mechanism.

## FP
FP-008

## T
T-012, T-015 (delivery/idempotency under retry)

## GC
GC-009, GC-010, GC-011

## Cross-domain
evolution (MP-002 internal hiding).

## Gaps
RQ3-006 expand-contract omitted.

## Exclusions
Universal backward compatibility. Treating Linux internal API instability as a license to break independent-consumer contracts.
