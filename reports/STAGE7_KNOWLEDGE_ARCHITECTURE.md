---
id: REPORT-STAGE7-KNOWLEDGE-ARCHITECTURE
type: stage-report
stage: 7
author: Cursor (Primary Knowledge Architect / Ontology Builder)
branch: research/stage7-knowledge-architecture
date: 2026-09-20
issue: 18
baseline: 93f507369d56b355a21bf7e287f1f36e11c1d2f6
---
# Stage 7 Knowledge Architecture

Operationalize the sealed Stage 6 Constitution into a compact, traceable, progressively disclosed substrate. No AX/MP causal semantics were changed. No Stage 8 playbooks, question banks, Agent modes, system prompts, or eval scenarios were created.

## 1. Ontology inventory and stable ID namespaces

| Type | Namespace | Count | Home |
|---|---|---|---|
| Evaluation axiom | AX-001..AX-004 | 4 | `01_CONSTITUTION.md` (unchanged) |
| Mother principle | MP-001..MP-010 | 10 | `principles/MP-*.md` |
| Retired / reserved | AX-005, MP-011, S-123, P-005, P-011 | — | reserved; not reused |
| Historical candidate | P-* | existing files | immutable |
| Review-signal lineage | P-006 only | 1 | historical file + MP-002 + evolution domain |
| Domain | 10 folders | 10 | `domains/` |
| Failure pattern | FP-001..FP-012 | 12 | `failure-patterns/` |
| Tactic | T-001..T-015 | 15 | `tactics/` |
| GOOD CASE | GC-001..GC-016 | 16 | `cases/good-cases/index.md` |
| Relationship map | predicates below | 109 nodes / 126 edges | `relationship-map.yaml` |
| Router | — | 1 | `00_ROUTER.md` |

ID reuse forbidden: AX-005, MP-011, S-123. P-006 is not reactivated as a principle. H7 is not resurrected.

## 2. Domain taxonomy and rationale

Ten domains, each the retrieval home of one promoted MP. Issue #18 candidate folders that would have been empty or duplicative were **not** created:

- `boundaries/` — four boundary kinds (module / failure / trust / contract) would collide; they route from evolution, reliability, security, integration.
- `runtime/` — split into lifecycle vs concurrency (D-02).
- `performance/`, `scalability/` — no independent causal MP; capacity lives in resources + overload. RQ2-006 USL is not used as sole support.
- `distributed/` — cross-cuts MP-004/008/010 rather than a separate causal family.

resources and overload stay separate folders because D-04 requires independently diagnosable peers; merging them into `capacity/` would hide that discriminator.

## 3. MP operationalization map

| MP | Domain | FP | T | GC | Gap |
|---|---|---|---|---|---|
| MP-001 | lifecycle | FP-001 | T-001, T-002 | GC-001, GC-002 | RQ3-002 |
| MP-002 | evolution | FP-002 | — (boundary placement is the MP) | GC-003, GC-007 | RQ3-001 (no P-006 rescue) |
| MP-003 | resources | FP-003 | T-003, T-004, T-005 | GC-002, GC-004 | — |
| MP-004 | reliability | FP-004, FP-005 | T-010 | GC-005, GC-006 | RQ5-001 |
| MP-005 | security | FP-006 | T-011 | GC-012 | RQ3-004, RQ2-008 |
| MP-006 | observability | FP-007 | T-014 | GC-008 | RQ5-003 |
| MP-007 | integration | FP-008 | T-012 | GC-009..011 | RQ3-006 omitted tactic |
| MP-008 | state-data | FP-009 | T-013 | GC-013, GC-014 | RQ5-005, RQ2-004 |
| MP-009 | overload | FP-010, FP-011 | T-006..T-009, T-005 | GC-015 | RQ5-004, D-12 |
| MP-010 | concurrency | FP-012 | — (choose/enforce primitive) | GC-016 | RQ5-002, RQ5-005 |

Atomic MP pages restate Constitution statement/mechanism/scope/non-prescription/GOOD CASE/distinctions and add only navigation links.

## 4. FP inventory and category justification

Each FP has a failure signature, mechanism, trigger, amplification, GOOD CASE boundary, and MP link. None is a protected property, metric, checklist, or pattern name.

| FP | Why an FP |
|---|---|
| FP-001 | ownerless work → leak/orphan/stale mutate |
| FP-002 | identifiable variation axis leaks across dependents |
| FP-003 | unbounded per-work dimension exhausts capacity |
| FP-004 | fault propagates through shared resources beyond failure domain |
| FP-005 | coupled defense amplifies blast radius (S-050/S-063) |
| FP-006 | excess privilege at a real trust/agent-action boundary |
| FP-007 | distinguishing evidence neither captured nor derivable |
| FP-008 | ungoverned break of independent-consumer contract |
| FP-009 | missing authority or conflict/consistency (V-010) rule |
| FP-010 | no governed capacity boundary before uncontrolled growth |
| FP-011 | retry amplification / retry storm (S-052) |
| FP-012 | assumed ≠ model-provided guarantee under perturbation |

Stale async overwrite is **not** a third FP: D-02 keeps FP-001 vs FP-012 attribution. Change amplification is **not** an FP (GC-007 / P-006). Blast radius is **not** an FP (RQ5-001).

## 5. T inventory and category justification

| T | Why a tactic, not a principle |
|---|---|
| T-001 | supervision/structured scope as one ownership mechanism |
| T-002 | cancellation propagation (two V-008-C senses) |
| T-003 | timeout/deadline as a per-work time bound |
| T-004 | occupancy caps (queue/concurrency/fan-out) |
| T-005 | bounded retry; can also *cause* FP-011 |
| T-006 | admission = enter/continue decision |
| T-007 | backpressure = upstream capacity signal; ≠ flow control alias |
| T-008 | rejection/load shedding = refuse/remove work |
| T-009 | degradation = reduce function/quality/cost |
| T-010 | scoped isolation; ≠ generic process split |
| T-011 | least privilege; ≠ MP-004 containment |
| T-012 | compatibility direction + migration path; ≠ universal compatibility MP |
| T-013 | explicit merge/conflict; ≠ single-writer MP |
| T-014 | evidence placement; ≠ telemetry-stack MP |
| T-015 | idempotency under explicit delivery semantics; ≠ retry |

Omitted: circuit breaker node, expand-contract, USE/SLO/hedged requests, event sourcing, strangler files (term-in-source is not a node).

## 6. GOOD CASE registry map

GC-001..GC-016 cover the Stage 5 §3 register at Stage 6 §10 granularity (MP-007's three cases split; append-only split from CRDT). All 16 are non-violation boundaries for later Stage 10 fixtures, not scenarios.

## 7. Relationship predicate definitions

Used: `DERIVED_FROM`, `EXPLAINS`, `MITIGATED_BY`, `RELATED_TO`, `DISTINCT_FROM`, `EVIDENCED_BY`, `HAS_GOOD_CASE`, `HAS_GAP`.

Omitted: `OPERATIONALIZED_BY` (no RS-* type).

`MP-004 RELATED_TO MP-005` is present as a **non-parent** navigation claim with no evidence inheritance.

## 8. Relationship coverage matrix

| From \ To | P-* | FP | T | GC | RQ | S-* | peer MP |
|---|---|---|---|---|---|---|---|
| MP-001..010 | DERIVED_FROM each | EXPLAINS ≥1 except none missing | via FP | HAS_GOOD_CASE | HAS_GAP where Constitution names one | sparse EVIDENCED_BY | DISTINCT_FROM / RELATED_TO |
| FP-002, FP-012 | — | — | no MITIGATED_BY (deliberate) | — | — | — | — |
| T-006..T-009 | — | — | DISTINCT_FROM each other | — | — | — | — |

Edge count: 126. Node count: 109. FP-002 has no tactic file because the intervention *is* MP-002. FP-012 has no tactic file because the intervention is primitive selection, not a buzzword tactic.

## 9. Orphan / dangling-reference audit

See mechanical validation in this workspace (script run at completion):

- all relationship-map paths exist
- all edge endpoints resolve to declared node IDs
- FP/T/GC IDs unique
- AX-005 / MP-011 / S-123 not reused as new entities
- MP-011 node is retired-reserved with no causal edges (explicit reason: tombstone)
- no `review-signals/` tree
- no Stage 8 artifacts

## 10. Source / RQ traceability audit

Sources cited on MP pages match Constitution lists. Sparse `EVIDENCED_BY` edges use only admitted `sources/S-*.md` files. RQ links:

- RQ5-001 → MP-004 HAS_GAP (D-10)
- RQ5-002 → MP-010
- RQ5-003 → MP-006
- RQ5-004 → MP-009
- RQ5-005 → MP-008 and MP-010 (not merged)
- RQ3-001 → MP-002, does not promote P-006
- RQ3-002 → MP-001
- RQ3-004 → MP-005
- RQ3-006 → MP-007 (expand-contract omitted)
- RQ2-004 → MP-008
- RQ2-008 → MP-005
- RQ2-009 not turned into a microservices node

No sibling evidence inheritance: MP-009 does not inherit MP-003's Little's Law edge as its own theoretical support; MP-005 does not inherit MP-004 containment sources.

## 11. D-01..D-14 preservation

| D | Result in Stage 7 |
|---|---|
| D-01 | `MP-001 DISTINCT_FROM MP-002`; separate domains |
| D-02 | `MP-001 DISTINCT_FROM MP-010`; FP-001 RELATED_TO FP-012; stale overwrite not merged |
| D-03 | P-006 remains review-signal lineage; GC-007; no locality MP |
| D-04 | `MP-003 DISTINCT_FROM MP-009`; separate domains; separate FPs |
| D-05 | `MP-004 DISTINCT_FROM MP-005` plus non-parent RELATED_TO; MP-011 not revived |
| D-06 | `MP-001 DISTINCT_FROM MP-008` |
| D-07 | `MP-001 DISTINCT_FROM MP-003`; cancellation on T-002, bounds on T-003/T-004 |
| D-08 | AX-003 only; no safety-floor MP/FP |
| D-09 | `MP-010 DISTINCT_FROM MP-008` |
| D-10 | RQ5-001 HAS_GAP; blast radius not equated with failure domain |
| D-11 | FP-007 / T-014 question-relative; GC-008 |
| D-12 | T-006 states priority scheduling ≠ admission; RQ5-004 on MP-009 |
| D-13 | H7 not instantiated |
| D-14 | GC-013 / T-013 multi-writer legal |

## 12. Lexical-gate preservation

Router and MP-003/004/008/009 pages keep: failure domain ≠ blast radius; write/state authority (V-003-D) ≠ authorization ≠ authority tier; consistency with V-010 suffix; backpressure ≠ load shedding ≠ admission ≠ degradation; flow control ≠ backpressure; retry ≠ idempotency; service qualified as runtime-role when architectural; component/container not used as implicit deploy units.

## 13. Progressive-disclosure path and expected load order

`00_ROUTER` → `01_CONSTITUTION` → one domain index → linked MP/FP/T → GC if the surface looks like a violation → RQ if named → `sources/` only for disputed claims.

A focused question should load on the order of: router + constitution + 1 domain index + 1–2 MP pages + 1–3 FP/T pages. Not all 10 MPs, not the source corpus.

### Retrieval demonstrations (navigation only)

**Overload / retry storm**
`00_ROUTER` → `domains/overload/` → MP-009 → FP-010 and FP-011 → T-006/T-007/T-008/T-009 and T-005 (bound vs amplifier) → DISTINCT_FROM T-015 → GC-015. Optionally `domains/resources/` MP-003 FP-003 if the retry *count* is the unbounded dimension. Do not treat backpressure as shedding.

**Stale async result / ownership**
`00_ROUTER` → `domains/lifecycle/` MP-001 FP-001 T-002; **and** `domains/concurrency/` MP-010 FP-012. Use D-02: missing owner vs assumed ordering/cancellation the model does not provide. GC-001/GC-016 block the two naive flags.

**Contract migration**
`00_ROUTER` → `domains/integration/` MP-007 FP-008 T-012 → GC-009/GC-010/GC-011. Do not load expand-contract. Internal vs independent-consumer split is GC-011. Distinct from `domains/evolution/` MP-002.

**Trust boundary / agent action**
`00_ROUTER` → `domains/security/` MP-005 FP-006 T-011 → GC-012. RQ2-008/RQ3-004 remain in view. Do not route to MP-004 isolation as a substitute (D-05).

**Observability vs formal guarantee**
`00_ROUTER` → `domains/observability/` MP-006 FP-007 T-014 GC-008; **and** `domains/concurrency/` MP-010 if the question is whether a guarantee exists. D-11: proof discharges only proved questions. Missing OTel is not FP-007.

## 14. Duplication / context-efficiency review

Constitution is the semantic source. MP pages do not copy Stage 5/6 reports. Domain indexes are routing tables. `EVIDENCED_BY` is sparse so the graph is not a second source catalog. Historical P-* files were not duplicated into MP prose.

## 15. Review-signal / property ontology decision

**Not instantiated.** No `review-signals/` directory and no `RS-*` IDs.

Homes without category confusion:

- **P-006 change amplification:** historical `principles/P-006.md`; `principles/index.md` non-principle section; MP-002 `review_signal_lineage`; `domains/evolution/`; GC-007; graph node type `review-signal-lineage` RELATED_TO MP-002. It is not an FP (spread is not a failure) and not a T.
- **RQ5-001 blast-radius measurement:** MP-004 HAS_GAP; D-10; `domains/reliability/` exclusions. It is a missing methodology, not a failure family and not a tactic.

MP/FP/T/domain metadata can represent both without a new durable type. A future RS-* layer would need Chief Architect approval; this Primary does not silently add it. `OPERATIONALIZED_BY` is unused for that reason.

## 16. Deliberate omissions / Stage 8 boundary

Not created: decision playbooks, question bank, reasoning workflow, Agent modes, system prompt, eval scenarios/results, runtime logic. Domain/FP/T files have no “questions to ask” sections. Circuit breaker, strangler, event sourcing, USE, SLO, hedged requests were not instantiated. expand-contract omitted (RQ3-006). Metrics ontology omitted with RS-*.

## 17. Genuine owner decisions only

1. **Review-signal type:** Primary recommends *not* adding `RS-*` now (homes above). Approving a minimal RS layer later is a Chief Architect ontology decision, not executed here.
2. **Domain split of MP-003 vs MP-009:** kept as two folders to preserve D-04 retrieval. A later `capacity/` merge would be a taxonomy decision; not done.

No other owner decisions. AX/MP semantics, MP-011 retirement, P-006 demotion, and D-08 contextual AX are already sealed.
