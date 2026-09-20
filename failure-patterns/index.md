---
id: IDX-FAILURE-PATTERNS
type: index
stage: 7
---
# failure-patterns/

Atomic reusable **causal failure families** grounded in the sealed corpus. An FP is not a protected property, tactic, metric, checklist item, named architecture pattern, or vague risk.

| ID | Title | Primary MP | Status |
|---|---|---|---|
| [FP-001](FP-001.md) | Unowned Runtime Work | MP-001 | STABLE |
| [FP-002](FP-002.md) | Hidden Variation-Axis Leak | MP-002 | STABLE |
| [FP-003](FP-003.md) | Unbounded Per-Work Dimension | MP-003 | STABLE |
| [FP-004](FP-004.md) | Shared-Resource Failure Cascade | MP-004 | STABLE |
| [FP-005](FP-005.md) | Coupled-Defense Amplification | MP-004 | STABLE |
| [FP-006](FP-006.md) | Excess Privilege at Trust Boundary | MP-005 | STABLE |
| [FP-007](FP-007.md) | Missing Distinguishing Evidence | MP-006 | CONTEXT_QUALIFIED |
| [FP-008](FP-008.md) | Ungoverned Independent-Consumer Contract Break | MP-007 | STABLE |
| [FP-009](FP-009.md) | Undefined Authority or Conflict Semantics | MP-008 | STABLE |
| [FP-010](FP-010.md) | Ungoverned Overload Growth | MP-009 | STABLE |
| [FP-011](FP-011.md) | Retry Amplification | MP-009 | STABLE |
| [FP-012](FP-012.md) | Assumed-vs-Provided Guarantee Mismatch | MP-010 | STABLE |

Stale async overwrite is not a third FP: attribute it via MP-001 (no cleanup owner) or MP-010 (assumed ordering/cancellation), per D-02. Change amplification is not an FP (P-006 / GC-007). Blast radius is an outcome measure, not an FP (RQ5-001).
