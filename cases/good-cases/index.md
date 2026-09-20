---
id: IDX-GOOD-CASES
type: good-case-registry
stage: 7
status: CANONICAL
provenance: "Stage 5 falsification §3 register + Stage 6 reduction §10 / reconciliation §8"
---
# GOOD CASE registry

Stable IDs for accepted Stage 5/6 non-violation boundaries. Not eval scenarios. Naive flags listed here are false positives.

| ID | Title | MP / lineage |
|---|---|---|
| [GC-001](#gc-001) | OTP supervised daemon | MP-001 |
| [GC-002](#gc-002) | Managed-heap GC + runtime soft budget | MP-001, MP-003 |
| [GC-003](#gc-003) | Exploration with unknown variation axes | MP-002 |
| [GC-004](#gc-004) | Indefinite lifetime, bounded per-work | MP-003 |
| [GC-005](#gc-005) | SQLite single-process economics | MP-004 |
| [GC-006](#gc-006) | Arrakis dimension-specific I/O protection | MP-004 |
| [GC-007](#gc-007) | Broad but healthy coordinated change | P-006 / MP-002 signal |
| [GC-008](#gc-008) | seL4 proof-scope | MP-006 |
| [GC-009](#gc-009) | Governed security/correctness compatibility break | MP-007 |
| [GC-010](#gc-010) | Governed ecosystem migration | MP-007 |
| [GC-011](#gc-011) | Linux internal API vs stable syscall | MP-007 |
| [GC-012](#gc-012) | Closed / coarse-grained trust | MP-005 |
| [GC-013](#gc-013) | CRDT / local-first multi-writer | MP-008 |
| [GC-014](#gc-014) | Append-only log / read-only derived view | MP-008 |
| [GC-015](#gc-015) | Gateway / path-level overload control | MP-009 |
| [GC-016](#gc-016) | Model-provided execution guarantees | MP-010 |

## GC-001 OTP supervised daemon

- **Context/shape:** Erlang/OTP supervised process; may run indefinitely.
- **Naive false-positive:** missing lifecycle/ownership; “unbounded lifetime.”
- **Why compliant:** supervisor is explicit ownership (S-114). Indefinite lifetime is not ownerlessness. Supervision is not a universal invariant.
- **Refs:** MP-001; FP-001; T-001; S-114. Stage 5 §3.1; Stage 6 §10.

## GC-002 Managed-heap GC + runtime soft budget

- **Context/shape:** GC language plus runtime memory budget (GOMEMLIMIT-class, S-116).
- **Naive false-positive:** no memory owner; unbounded memory.
- **Why compliant:** GC exempts managed-heap *reclamation only*. Semantic ownership, write authority, and aggregate budget remain answerable. Soft budget is a legal MP-003 bound.
- **Refs:** MP-001, MP-003; S-116. Stage 5 §3.2; Stage 6 §10.

## GC-003 Exploration with unknown variation axes

- **Context/shape:** prototype / exploration before a likely change decision is identifiable.
- **Naive false-positive:** missing modularity / no boundaries.
- **Why compliant:** MP-002 does not require speculative boundaries.
- **Refs:** MP-002; FP-002. Stage 5 §3.3; Stage 6 §10.

## GC-004 Indefinite lifetime, bounded per-work

- **Context/shape:** daemon/stream/service (runtime-role sense, V-002-C) with bounded per-work dimensions.
- **Naive false-positive:** “runs forever ⇒ unbounded.”
- **Why compliant:** MP-003 separates lifetime from per-work bounds.
- **Refs:** MP-003; FP-003; T-003; T-004. Stage 5 §3.4; Stage 6 §10.

## GC-005 SQLite single-process economics

- **Context/shape:** embedded single-process database with high reliability claims in its documented testing scope (S-117).
- **Naive false-positive:** no isolation / no distributed containment / no process boundary.
- **Why compliant:** MP-004 is graded; process boundary is not required when the cost model does not justify one.
- **Refs:** MP-004; T-010; S-117. Stage 5 §3.5; Stage 6 §10.

## GC-006 Arrakis dimension-specific I/O protection

- **Context/shape:** hardware-delegated I/O protection (S-122).
- **Naive false-positive:** missing process-boundary isolation.
- **Why compliant:** only the constrained I/O/failure-power dimension is credited. Not generic replacement for all containment.
- **Refs:** MP-004; S-122. Stage 5 §3.6; Stage 6 §10.

## GC-007 Broad but healthy coordinated change

- **Context/shape:** wide but coherent upgrade/migration of units that legitimately share a decision.
- **Naive false-positive:** large change spread ⇒ bad structure (P-006 misread as principle).
- **Why compliant:** P-006 is a review signal/property, not an MP. Spread alone is not a violation.
- **Refs:** P-006; MP-002; D-03. Stage 5 §3.7; Stage 6 §10.

## GC-008 seL4 proof-scope

- **Context/shape:** seL4-class static proof under an explicit assumption set (S-118); similarly DO-178C-class minimal embedded observation.
- **Naive false-positive:** missing service-style telemetry / “no diagnostic-surface design.”
- **Why compliant:** MP-006 discharges only questions actually proved under satisfied assumptions. Hardware/integration/ops questions outside proof still need evidence if attribution matters.
- **Refs:** MP-006; FP-007; T-014; S-118; D-11. Stage 5 §3.8; Stage 6 §10.

## GC-009 Governed security/correctness compatibility break

- **Context/shape:** RFC 7568-class break (S-120) where a higher-priority security/correctness requirement explicitly governs the change.
- **Naive false-positive:** any compatibility break is an MP-007 violation.
- **Why compliant:** MP-007 allows an explicit higher-priority override with migration/governance.
- **Refs:** MP-007; T-012; S-120. Stage 5 §3.9; Stage 6 §10.

## GC-010 Governed ecosystem migration

- **Context/shape:** PEP 404-class coordinated ecosystem evolution (S-121).
- **Naive false-positive:** not perpetually backward compatible.
- **Why compliant:** governed coordinated migration is an explicit exception, not “breaking is fine.”
- **Refs:** MP-007; T-012; S-121. Stage 5 §3.9; Stage 6 §10.

## GC-011 Linux internal API vs stable syscall

- **Context/shape:** unstable internal kernel interfaces with a stable external syscall contract (S-124).
- **Naive false-positive:** internal interface churn is always a contract violation.
- **Why compliant:** MP-007 is triggered by independent consumers; tightly coordinated internals may have a different stability policy. Not a license that internal APIs should be unstable.
- **Refs:** MP-007; S-124. Stage 5 §3.10; Stage 6 §10.

## GC-012 Closed / coarse-grained trust

- **Context/shape:** closed single-user or same-team single deploy unit without relevant untrusted-input / cross-privilege / external-integration / agent-action boundaries.
- **Naive false-positive:** missing fine-grained internal zero trust.
- **Why compliant:** MP-005 does not universalize zero trust. Supply-chain/external-input boundaries remain in scope when present.
- **Refs:** MP-005; FP-006; T-011. Stage 5 §3.11; Stage 6 §10.

## GC-013 CRDT / local-first multi-writer

- **Context/shape:** CRDT or local-first multi-writer with declared merge/conflict semantics (S-119/S-107).
- **Naive false-positive:** no central authority / missing single writer.
- **Why compliant:** MP-008 requires authority × conflict dimensions, not single-writer (D-14).
- **Refs:** MP-008; T-013; S-119; S-107. Stage 5 §3.12; Stage 6 §10.

## GC-014 Append-only log / read-only derived view

- **Context/shape:** append-only source plus derived read models.
- **Naive false-positive:** no conflict rule / no writer authority.
- **Why compliant:** explicit append and derivation semantics are a defined authority/conflict model.
- **Refs:** MP-008; S-046; S-040. Stage 6 §10.

## GC-015 Gateway / path-level overload control

- **Context/shape:** admission/shedding/backpressure implemented on gateway/mesh/path, not necessarily in service code.
- **Naive false-positive:** service has no local load-shedding/degradation code.
- **Why compliant:** MP-009 requires an effective governed boundary on the path, not service-local tactics.
- **Refs:** MP-009; T-006..T-009; S-048/S-050. Stage 5 §3.13; Stage 6 §10.

## GC-016 Model-provided execution guarantees

- **Context/shape:** actor per-pair mailbox ordering, non-preemptive event-loop segments, or concrete DBMS isolation actually provided by the model (S-115 precedent).
- **Naive false-positive:** “implicit timing assumption.”
- **Why compliant:** MP-010 flags assumed ≠ provided, not guarantees the model truly gives. Do not require application prose to restate them. ANSI isolation *names* are not this GC (RQ5-005).
- **Refs:** MP-010; FP-012; S-115. Stage 5 §3.14; Stage 6 §10.
