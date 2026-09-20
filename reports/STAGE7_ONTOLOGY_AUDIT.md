``
id: STAGE7-ONTOLOGY-AUDIT
title: "Stage 7 Independent Knowledge-Architecture Challenger — Pass A (Blind)"
stage: 7
pass: A
role: independent-knowledge-architecture-challenger
challenger: "Codex harness + GLM 5.3"
branch: challenge/stage7-knowledge-architecture
baseline: 93f507369d56b355a21bf7e287f1f36e11c1d2f6
date: 2026-09-20
issue: 18
blind: true
status: COMPLETE
``

# Stage 7 Independent Knowledge-Architecture Challenger — Pass A（Blind）

## 0. Scope, blindness, and method

Read (sealed inputs only): `AGENTS.md`, `TASK.md`, GitHub Issue #18 including both Chief Architect checkpoints, `01_CONSTITUTION.md`, `02_VOCABULARY.md`, `reports/STAGE6_REDUCTION.md`, `reports/STAGE6_REDUCTION_AUDIT.md`, `reports/STAGE6_RECONCILIATION.md`, `reports/STAGE5_FALSIFICATION.md`, `reports/STAGE5_RECONCILIATION.md`, `source-manifest.yaml`, `review-queue.yaml`.

Not read: the `research/stage7-knowledge-architecture` branch, any Primary Stage 7 artifact (Router, MP pages, domains, FP/T files, GOOD CASE registry, relationship map, Stage 7 synthesis report), and any unmerged Primary Stage 7 commit or PR. No source collection was performed. No sealed Stage 2–6 artifact was modified.

Method: this audit challenges the knowledge architecture Stage 7 **should permit**. It does not build a competing canonical ontology, allocates no canonical ID, creates no Router/domain/MP/FP/T/GC/relationship-map artifact, and preregisters deterministic Pass B checks (`V7-01..`) to be run against the Primary implementation.

Division per Issue #18: GLM 5.3 owns the semantic/category/retrieval/ontology challenge below; the Codex harness owns ID/path/ref determinism, persistence, and fail-closed delivery of this report.

---

## 1. Minimal entity types (recommendation)

The smallest sufficient durable set is **seven types**. Everything else in the Issue #18 output set is either a navigation view over these types or stays sealed.

| # | Type | ID form | Durable content | Count guidance |
|---|---|---|---|---|
| 1 | Mother Principle (canonical) | `MP-001..` | Atomic operationalization of one Constitution MP; semantics must not diverge from `01_CONSTITUTION.md` | Exactly 10: MP-001..MP-010, no more |
| 2 | Failure Pattern | `FP-001..` | Reusable causal failure mechanism (signature, trigger, amplification, consequences) | Evidence-forced only; no target count |
| 3 | Tactic | `T-001..` | Reusable intervention mechanism with trade-offs and Does-Not-Solve | Evidence-forced only; no target count |
| 4 | GOOD CASE registry entry | `GC-001..` | Non-violation boundary with qualifier, false-flag surface, provenance | 14 Stage 5 register rows, atomized to 16 entries (see §5) |
| 5 | Domain index | `domains/<name>/index.md` | Retrieval view: scope, refs, exclusions. Knowledge-bearing content: none | Create only where ≥2 durable nodes route through it |
| 6 | Relationship edge | `relationship-map.yaml` | Typed, machine-readable claim between existing nodes | Only predicates in §3 |
| 7 | Evidence reference | `S-*` / `RQ*` | Pointer into `source-manifest.yaml` / `review-queue.yaml`; never prose, never a node | Governed by manifest/queue; Stage 7 adds none |

Non-types, explicitly:

- **Router** (`00_ROUTER.md`) is navigation infrastructure, not a knowledge type; it must carry no principle, mechanism, or reasoning content (§8).
- **AX-001..AX-004** stay in the Constitution. No separate AX files; AX-005 remains moved-to-usage-contract and reserved (§9).
- **Historical P-* files** are sealed evidence; they are `DERIVED_FROM` lineage targets, never rewritten, never re-indexed as canonical (§9).
- **Review-signal/property (RS-*)**: verdict **NOT_NEEDED** for Stage 7 — see §10 for the P-006 / RQ5-001 test cases and reopen conditions.
- **Stage 5/6 reports** are provenance, not runtime knowledge; the progressive-disclosure path must never load them by default (§8).

The ten canonical MPs this architecture must carry, with their Constitution anchors:

| MP | Title | One-line semantic anchor (must survive operationalization) |
|---|---|---|
| MP-001 | Explicit Ownership | Runtime entities and mutable state have answerable create/modify/stop/cleanup ownership; GC exempts only managed-heap reclamation. |
| MP-002 | Change-Decision Boundaries | Partition around reasonably identifiable volatile decisions; unknown-variation-axis exploration is a GOOD CASE, not a violation. |
| MP-003 | Bounded Execution | Lifetime may be indefinite; per-work execution/wait/retention/retry/queue/concurrency/memory/fan-out need effective bounds or governed policy. |
| MP-004 | Failure Containment by Scoped Propagation Boundaries | Failure domains designed against acceptable blast radius; no default process boundary; Arrakis is dimension-specific. |
| MP-005 | Trust Minimization | Minimize granted trust/privilege at real trust boundaries; reduces directly available actions, not total damage; no zero-trust universalization. |
| MP-006 | Obtainable Diagnostic Evidence | Question-relative: evidence for operational questions not discharged by stronger guarantees must be designed to be obtainable; seL4 discharges only proved questions under satisfied assumptions. |
| MP-007 | Contract Preservation | Explicit compatibility direction and migration path where independent consumers exist; governed breaks (RFC 7568 / PEP 404 / Linux-internal) are GOOD CASES. |
| MP-008 | State Authority & Conflict Semantics | Two explicit orthogonal dimensions per state class: write/state authority (V-003-D) and conflict/consistency semantics (V-010 with sense suffix); multi-writer + explicit merge is compliant (D-14). |
| MP-009 | Governed Overload Boundary | Demand-exceeds-capacity paths meet a governed boundary before uncontrolled growth; admission/backpressure/rejection-shedding/degradation are distinct mechanisms, not aliases, and not service-local mandates. |
| MP-010 | Execution-Model-Honest Correctness | Correctness must not assume timing/order/interruption/cancellation/clock guarantees the model does not provide; model-provided guarantees are GOOD CASES. |

### Challenge: is any additional review-signal/property type necessary?

No (full argument in §10). The two live candidates — P-006 change amplification and RQ5-001 blast-radius measurement — are representable as qualified MP metadata plus vocabulary entries plus gap references. An RS layer would currently instantiate at most one honest node (P-006) while the second (RQ5-001) lacks measurement-methodology evidence, failing the Issue #18 rule "only instantiate evidence-forced examples."

---

## 2. Highest-risk category traps (from the sealed corpus)

| # | Trap | Concrete corpus instance | Pass B loss signal |
|---|---|---|---|
| T1 | Principle disguised as tactic | "Admission control", "zero trust", "single writer", "universal backward compatibility" — all non-prescriptions of MP-005/007/008/009 — re-entering as T-node parents or tactic prose that re-states the MP | A T page whose Intent is an MP restatement; tactic families listed as MP requirements |
| T2 | Tactic disguised as principle | Supervision (S-114), structured concurrency (S-084..086), GOMEMLIMIT soft budget (S-116), strangler fig (V-021-F), expand-contract (V-021-G, NEEDS_EVIDENCE) | Any new MP-like claim, domain rule, or "always/never" navigation assertion built from a mechanism source |
| T3 | Property/metric disguised as FP | "Unbounded queue" (property), "change amplification" (P-006, demoted), "blast radius" (measure) — an FP must be the causal amplification path (e.g., retry storm, cascade), not the dimension | FP body with signature but no causal mechanism, or whose mechanism is a measurable dimension |
| T4 | Protected property disguised as FP | Evolvability, operability, reliability are `protects` fields; "low observability" is not an FP unless phrased as MP-006's non-derivability failure (distinguishing information neither captured nor derivable) | FP entries named after missing properties with no failure signature |
| T5 | Pattern name disguised as tactic | Circuit breaker, bulkhead, Saga, CQRS, event sourcing, cells — V-017-B/C: a pattern is a context-bound solution form, a tactic is a reusable intervention mechanism | T nodes created because the name appears in S-0xx; body with no Does-Not-Solve / trade-offs |
| T6 | GOOD CASE generalized into a rule | "Supervised daemons are always compliant" (S-114 is scoped), "CRDTs are always compliant" (requires explicit merge semantics, D-14), "internal APIs may break" (S-124 is single-owner governance), "Arrakis replaces isolation" (I/O dimension only) | GC entries whose qualifier ("why compliant") has been dropped or weakened; domain prose citing GCs as licenses |
| T7 | Evidence/source artifact promoted into an ontology node | S-117 SQLite testing page, S-122 Arrakis, S-118 seL4 — each supports a scoped claim or GC but has no independent retrieval value as a node | Any `nodes:` entry in relationship-map with type source/rq or an FP/T page whose content restates one source |
| T8 | Vocabulary collision promoted into structure | failure domain vs blast radius (V-005-E/V-021-A), backpressure vs load shedding vs admission control vs degradation (V-008 family), consistency senses (V-010), isolation senses (N-5) | Domain names or edge predicates that re-merge terms the vocabulary gate split |

---

## 3. Relation vocabulary (recommendation)

Smallest defensible set: **eight predicates**. `OPERATIONALIZED_BY` is deferred together with the RS-layer verdict (§10) and must not appear unless the owner approves an RS type.

| Predicate | Direction | Meaning | Transitive | Causal | Evidence inheritance |
|---|---|---|---|---|---|
| `EXPLAINS` | MP → FP | The MP mechanism, when violated, causally produces this failure family | No | **Yes** (violation→failure) | No — FP carries own `source_ids` |
| `MITIGATED_BY` | FP → T | The tactic intervenes in this failure mechanism | No | **Yes** (intervention) | No — T carries own evidence |
| `DISTINCT_FROM` | node ↔ node (symmetric) | Independently violable mechanisms; must carry the discriminator (D-01..D-09/D-14 or V-* boundary) in `note` | No | No | No |
| `RELATED_TO` | MP ↔ MP | Navigation-only association; explicitly no support, no parent semantics | No | **No** | **No** |
| `EVIDENCED_BY` | claim node → S-* | Direct citation of an admitted manifest source | No | No | **No cross-node inheritance of any kind** |
| `HAS_GOOD_CASE` | MP/FP/T → GC | Non-violation boundary attached to this node | No | No | No |
| `HAS_GAP` | node → RQ* | Open evidence gap attached to this node | No | No | No |
| `DERIVED_FROM` | MP → P-* / Constitution | Historical lineage pointer | No | No | No |

Header documentation requirement: `relationship-map.yaml` must define direction, meaning, transitivity, causality, and evidence-inheritance for every predicate in its file header (per Issue #18 §7).

### Bad edges to attack in Pass B

| # | Bad edge | Why it fails | Deterministic check |
|---|---|---|---|
| E1 | Sibling evidence inheritance | MP-009 does not inherit MP-003's Little's Law support; MP-005 does not inherit MP-004's containment evidence (Stage 6 reduction §9 explicitly forbids this) | For every MP page, `source_ids` must be a subset of that MP's Constitution Sources line; no S-* may appear on an MP whose Constitution entry lacks it, added via edge reasoning |
| E2 | Parent/child overreach | No MP is parent of another MP (MP-011 retired; OD6-1 keeps MP-003/MP-009 peers; MP-004/MP-005 peers). Domain membership is aggregation, not parentage | No predicate in the map expresses containment between MPs; domain indexes must not use parent/child language about MPs |
| E3 | RELATED_TO interpreted as support | `MP-004 RELATED_TO MP-005` is the only pre-authorized Stage 7 edge (Stage 6 §14): navigation hypothesis via constrained cross-component impact/power; **peer only** | The edge note must state "navigation only, no parent semantics, no evidence inheritance"; any second RELATED_TO MP pair needs owner approval |
| E4 | DISTINCT_FROM without context | A bare DISTINCT_FROM edge cannot be evaluated later | Every DISTINCT_FROM edge must carry the D-* number or V-* collision family in `note` |
| E5 | Causal implication hidden in navigation edges | Domain indexes and RELATED_TO must not claim "X supports Y" or "X causes Y"; only EXPLAINS/MITIGATED_BY are causal | Grep domain indexes and Router for causal verbs (cause/support/justify/therefore) applied across nodes |

---

## 4. Domain taxonomy / retrieval risks

| # | Risk | Sealed-corpus basis | Pass B criterion |
|---|---|---|---|
| R1 | Duplicate content across domains | 10 MPs is a small base; `runtime/`+`concurrency/` both paraphrasing MP-003/MP-010, or `reliability/`+`resources/` both paraphrasing MP-009, is the likely duplication | Domain index contains scope + refs + exclusions only; any restatement of MP/FP/T body prose = duplication FAIL |
| R2 | One question → many domains → wide loading | "Overload/retry storm" symptomatically touches runtime, reliability, performance, resources, distributed — but mechanism-routes to MP-009 (±MP-003) | Example retrieval paths in the Primary report must resolve to ≤2 domain indexes for each of the five Issue #18 examples; symptom-keyword routing = FAIL |
| R3 | Cloud/backend bias | RQ2-014 standing risk: backend/distributed examples ≈55–60%; MP-004/006/009 evidence concentration acknowledged in Stage 6 §11 | Domain indexes must carry shape-scope caveats where evidence is backend-concentrated (MP-004/006/009); no implication of universal cross-shape coverage |
| R4 | Domains classify sources rather than route retrieval | `source-manifest.yaml` already has `clusters` (source classification). Domains must be retrieval views over accepted knowledge, not a second source taxonomy | No domain index organized by S-* enumeration; sources appear only inside node `source_ids` |
| R5 | Empty domain bureaucracy | Issue #18 lists 14 domain-family hypotheses but forbids empty folders; with 10 MPs + evidence-forced FP/T, `5–8 domains are plausible; `observability` alone (MP-006) and `security` alone (MP-005) may be too thin to stand alone | Every domain index must route ≥2 durable nodes or be merged; creation of all 14 folders = FAIL; merge/split decision must be explained in the Primary report |
| R6 | Domain names collide with V-* vocabulary | `boundaries/` vs N-4/V-002 four boundary types; `state-data/` vs V-010/V-011 sense families; `integration/` vs V-012; `concurrency/` vs V-007 | Each domain index must carry an explicit exclusions line naming the V-* collisions it refuses to re-merge (Issue #18 already requires "explicit exclusions where collision risk exists") |
| R7 | Domain as reasoning surface | Domain prose drifting into "how to evaluate X" | Domain index contains no evaluation procedure, no question bank, no checklist (Stage 8 boundary, §12) |

---

## 5. GOOD CASE registry requirements

The registry is the future false-positive eval fixture input (Stage 10), so what must be stable is **the boundary, not the story**.

### 5.1 Required stable fields per GC entry

1. stable ID `GC-xxx` (append-only, never reused);
2. short title + shape/context (the architectural form);
3. **what a naive reviewer would falsely flag** (the false-positive surface — this is the eval payload);
4. **why it is compliant, including the qualifier** — the exact condition that makes it legal (this is what Stage 5/6 fought to preserve; losing it turns a boundary into a blanket exemption);
5. MP/FP/T refs (`HAS_GOOD_CASE` edges);
6. source IDs where applicable (`EVIDENCED_BY`);
7. Stage 5/6 provenance pointer (register row / reduction §10 row).

### 5.2 Count and atomization

The Stage 5 falsification register (§3) has 14 numbered entries, but two rows pack multiple boundaries (row 9: RFC 7568 + PEP 404; row 12: CRDT + log + local-first + append-only/derived). The Stage 6 reduction §10 matrix is the most granular accepted form with **16 single-boundary rows**. Recommendation: atomize to 16 GC entries, each keeping exactly one qualifier; never fewer than the 14 register rows.

### 5.3 Anti-flattening requirements (the boundaries must not become generic examples)

| GC family (Stage 6 §10 row) | Qualifier that must survive |
|---|---|
| OTP supervised daemon | supervision is a compliant ownership mechanism, not a universal invariant |
| Managed-heap GC | exemption covers reclamation dimension only; total-volume and write-authority responsibility not exempted |
| Exploration unknown-axis | no-boundary legal only while variation axis genuinely unidentified |
| Indefinite lifetime | bounds judged per-work, not by service lifetime |
| SQLite single-process | supported only by the testing-page scope; no distributed-mechanism inference either way |
| Arrakis | I/O protection dimension only; not generic containment replacement |
| Broad coordinated change | P-006 is a signal, not a violation; spread alone never structural failure |
| seL4 proof-scope | only proved questions under satisfied assumptions; outside the assumption set, MP-006 applies |
| Governed security break (S-120) | higher-priority security/correctness requirement, explicitly governed |
| Governed ecosystem evolution (S-121) | explicit governance decision, not technical-debt authorization |
| Linux internal API (S-124) | single-owner/consumer-independence grading; not a general internal-API license |
| Closed coarse-grained trust | only absent relevant trust boundaries; supply-chain boundary excepted |
| CRDT/local-first multi-writer | requires explicit merge/conflict semantics (D-14) |
| Append-only / read-only derived | explicit append/derivation semantics define the conflict/authority model |
| Gateway/path-level admission | placement is architectural; no service-local shedding mandate |
| Model-provided guarantees | guarantee must be actually provided by the model (S-115 precedent), not assumed |

A GC entry missing field 3 or 4 is not a fixture; it is decorative. A GC whose qualifier is dropped produces false exemptions — the exact failure mode Stage 5 falsification existed to prevent.

---

## 6. D-01..D-14 preservation requirements

| D-test | Required navigability in Stage 7 | Most likely loss vector |
|---|---|---|
| D-01 P-001/P-002 DISTINCT | MP-001 ↔ MP-002 DISTINCT_FROM edge or explicit distinction retained in both pages | A generic "boundaries" domain absorbing both; MP-002 page framing ownership as a boundary problem |
| D-02 P-001/P-013 DISTINCT | Stale-overwrite attribution (MP-010 timing) vs orphan/cleanup failure (MP-001) remain separately diagnosable | "Runtime correctness" domain/index merging execution-model and ownership concerns |
| D-04 P-003/P-012 PEER | MP-003 ↔ MP-009 peer; bounded-no-policy and policy-with-unbounded-retries both representable | A "capacity" domain implying one shared mechanism; cross-inheritance of Little's Law support to MP-009 |
| D-05 P-004/P-009 PEER | MP-004 ↔ MP-005 RELATED_TO (navigation only, §3 E3); propagation vs privilege mechanisms independently testable | Any parent edge, shared evidence, or "power≤responsibility" heading with causal language |
| D-06 P-010/P-001 DISTINCT | State authority/conflict semantics never derived from lifecycle ownership | "Single owner/source of truth" collapse in domain prose; single-writer implication |
| D-07 P-001/P-003 DISTINCT | Cancellation/cleanup (MP-001) vs bounds (MP-003) stay separate | One undifferentiated timeout/cancellation control narrative |
| D-09 P-013/P-010 DISTINCT | Execution-order/timing guarantees vs state conflict/authority semantics | "Consistency/correctness" umbrella without V-010 suffix discipline |
| D-11 P-007 proof-scope | MP-006 page + seL4 GC keep question-relative scope and proof-scope boundary | "Formal proof replaces observability" or service-telemetry universal in either direction |
| D-12 P-012 gap | MP-009 carries D-12 NEEDS_EVIDENCE (embedded admission; priority scheduling ≠ admission) | Domain prose claiming cross-shape admission coverage; priority-as-admission equivalence |
| D-14 CRDT multi-writer GC | MP-008 page + CRDT GC keep multi-writer + explicit merge semantics compliant | Authority flattened to single-writer anywhere in the architecture |
| D-03 / D-08 / D-10 / D-13 (context tests) | P-006 stays demoted (§10); AX-003 contextual wording untouched; RQ5-001 gap visible on MP-004 (`HAS_GAP`); no locality node | Respectively: RS resurrection without evidence; universal safety floor; silent metric invention; H7 locality umbrella |

---

## 7. Source/RQ traceability requirements

1. Every `S-*` referenced by any Stage 7 artifact must exist in `source-manifest.yaml`; every `RQ*` must exist in `review-queue.yaml`. No new S-*/RQ* may be created (no source collection).
2. Evidence scope discipline is claim-relative (V-018-B): a source cited on a new FP/T page may support only claims within its admitted scope notes (e.g., S-115 Tier A only for Erlang semantics; S-112/113 platform-normative; S-119 for D-14 multi-writer explicitly).
3. Claim-to-evidence coupling: any new FP/T/GC assertion with no `source_ids` and no sealed-report provenance is an unsupported claim (V7-29).
4. Sources are references, not content: no FP/T/domain page may duplicate source prose; the corpus stays in `sources/`.
5. Gaps stay visible: RQ5-001 (MP-004), RQ5-002 (MP-010), RQ5-003 (MP-006), RQ5-004 (MP-009), RQ5-005 (integration/state), RQ3-002/004, RQ2-009 attach via `HAS_GAP` and must not be silently resolved by operationalization.

---

## 8. Progressive disclosure / context-efficiency requirements

Required runtime path: `00_ROUTER -> 01_CONSTITUTION -> relevant domain index -> linked MP/FP/T -> source/RQ only when needed`.

Pass criteria (preregistered):

1. **Router is navigation only**: routing table (knowledge need / domain → file), progressive-disclosure explanation, when-to-load-evidence rules. No principle statements, no mechanism prose, no evaluation procedure, no question bank, no "if the user asks X, do Y" sequences. Bounded size (see OD-6).
2. **Domain index loads once**: a focused question resolves through at most 1–2 domain indexes (Issue #18's five example paths: overload/retry storm; stale async result/ownership; contract migration; trust boundary/agent action; observability vs formal guarantee).
3. **Node loading is selective**: an ordinary focused question must not require loading all MPs, all FP/T files, all domains, all sources, or any Stage 5/6 report by default. Stage 5/6 reports are provenance links only.
4. **No default source load**: sources load only for disputed/high-risk/low-confidence claims (Issue #18 router contract item 5).
5. **No reconciliation burden**: if domain prose duplicates MP/FP/T content, an agent must reconcile duplicates — that is a context-efficiency failure even when semantically consistent (R1).

Fail examples (attack surface):

- Router containing reasoning steps or a decision workflow (Stage 8 smuggling, §12);
- "observability vs formal guarantee" path requiring MP-006 + MP-010 + S-118 + S-115 + both Stage 6 reports to answer a scoped question;
- contract-migration path loading all of `evolution/` + `integration/` + MP-002 + MP-007 + five sources;
- domain indexes so granular (empty bureaucracy) that every question touches 3+ of them.

---

## 9. Stable IDs / retirement rules

Protected invariants (failure = FAIL CLOSED):

| Rule | Requirement | Failure criterion |
|---|---|---|
| AX-005 | Reserved, moved to usage-contract rule 2; not an AX | `AX-005` appearing as a live axiom/node/edge in any Stage 7 artifact |
| MP-011 | RETIRED / NOT PROMOTED (category error); tombstone in Stage 6 reduction §2; ID never reused | Any live MP-011 node; any new entity assigned ID MP-011; renumbering of MP-001..010 |
| P-006 | Not promoted; MP-002-associated review signal only | P-006 as MP/FP/T node; change-locality principle under any name |
| H7 | Not resurrected (D-13) | Any locality Mother Principle or locality umbrella node |
| V-* namespace | Frozen (V-001..V-021); vocabulary is sealed | New V-* IDs; edits to existing entries |
| S-* / RQ* | Manifest/queue-governed; Stage 7 adds none | New S-*/RQ* IDs from Stage 7 artifacts |
| New namespaces | FP-001.., T-001.., GC-001.. sequential append-only from 1 | Gaps implying deletion; duplicate IDs; ID reuse with different meaning; cross-namespace collision (e.g., FP id colliding with legacy P-*) |

Deterministic collision checks for Pass B: uniqueness of every ID within its namespace; every referenced ID/path resolves; no `AX-005`/`MP-011`/`H7` token used as a live entity; `MP-001..` set is exactly ten with no insertions.

---

## 10. Review-signal / property layer verdict

**Verdict: NOT_NEEDED.**

Test case 1 — P-006 change amplification: V-014-D already carries the working definition (STABLE, S-001/S-005); Stage 6 §4 fixes its home as an MP-002-associated measurable review signal. Representation: `review_signals` frontmatter on MP-002 + V-014-D reference + provenance to Stage 6 §4. No retrieval or reasoning need requires a standalone RS-001 node; creating one adds a fourth knowledge category for exactly one honest instance.

Test case 2 — RQ5-001 blast-radius measurement: the measurement **methodology** is the open gap (D-10, NEEDS_EVIDENCE; no authoritative source for proxy metrics). An RS node here would either be an empty placeholder (violating no-empty-bureaucracy) or would invent a metrics ontology the evidence does not force (violating the Issue #18 RS rule). Representation: `HAS_GAP` edge MP-004 → RQ5-001.

This honors "do not invent a metrics ontology merely for symmetry": the two candidates fail the evidence-forced instantiation bar in opposite directions (one representable without a new type; one lacking evidence to instantiate).

Reopen conditions (owner decision OD-4): if Pass B finds metric-shaped FPs (T3) or property nodes smuggled into tactics, or if Stage 8+ needs executable review-signal fixtures, a minimal RS layer may be **proposed** at that gate — not silently introduced.

---

## 11. FP / T stop criteria

A proposed FP is rejected unless **all** hold:

1. specific causal failure mechanism (signature + mechanism + trigger + amplification path);
2. reusable failure family — not a one-incident narrative (S-062/S-064 postmortems support FPs only where the mechanism generalizes);
3. not a protected property, tactic, metric, checklist item, or pattern name (§2 T3/T4/T5);
4. accepted evidence or Stage 5 failure reasoning supports it;
5. links to ≥1 MP via `EXPLAINS` without stretching MP scope (an FP explainable only by stretching two MPs is two FPs or none).

A proposed T is rejected unless **all** hold:

1. reusable intervention mechanism (intent + mechanism + applies-when + **does-not-solve** + trade-offs);
2. not a principle restatement, pattern name, or vendor feature;
3. distinct from sibling tactics by mechanism, not by vendor/tool/runtime (no T-retry-aws vs T-retry-grpc split);
4. links ≥1 FP via `MITIGATED_BY` or explicitly serves an MP scope;
5. honors V-008-family distinctions (backpressure ≠ load shedding ≠ admission control ≠ degradation; retry ≠ idempotency; failure isolation ≠ generic process split; compatibility tactic ≠ universal compatibility principle).

Global stop rules: no node created solely because a named pattern exists in a source; no node where metadata/reference suffices; every index file routes ≥2 nodes (R5); total FP/T count is evidence-bounded, and the Primary report must justify each node's retrieval value rather than coverage symmetry across MPs (MP with few links is acceptable per Issue #18).

---

## 12. Stage 8 boundary

Stage 7 must deliver a knowledge substrate; the following constitute smuggling and fail V7-30:

| Smuggled artifact | Detection signal |
|---|---|
| Decision playbook | Ordered evaluation steps, "first check… then…", decision trees in Router/domains/FP pages |
| Question bank | Lists of questions an agent "should ask" (including FP "questions to ask" sections, forbidden by Issue #18 §4) |
| Explicit reasoning sequence | Any prescribed inference chain across nodes beyond navigation links |
| Review checklist | Checklist semantics in GC entries or domain indexes (GCs are boundaries, not checks) |
| Agent mode / system prompt | Prompt-like prose, role instructions, output-format contracts in Router |
| Tool-routing runtime logic | Router telling the agent which tool/agent/mode to invoke rather than which file to load |
| Eval scenario/result | GC entries expanded into scenarios, fixtures, or expected outputs (Stage 10 material) |

The test: an artifact is Stage 7 iff it answers "where is the knowledge and what does it claim", never "what should the agent do next".

---

## 13. V7 preregistered checks (Pass B)

Status vocabulary: PASS / PARTIAL / FAIL / CHECK_INVALID. Checks run against the Primary Stage 7 implementation on `research/stage7-knowledge-architecture`.

| Check | Pass condition | Failure signal |
|---|---|---|
| V7-01 MP semantic fidelity | MP-001..MP-010 pages each consistent with Constitution statement/mechanism/scope/good-case/distinctions; all ten present, no more | Missing MP; semantic drift; new MP-like content |
| V7-02 Canonical vs historical | `principles/index.md` separates canonical MP / historical P-* / retired MP-011 / P-006 lineage; no P-* rewritten | Blended index; P-* edits in diff |
| V7-03 AX boundary | AX-001..004 remain Constitution-level; no AX files; AX-005 absent as entity | New AX; AX-005 live node |
| V7-04 FP category purity | Every FP has signature + causal mechanism + trigger + amplification; no property/metric/tactic FPs | §2 T3/T4 instances |
| V7-05 Tactic category purity | Every T has intervention mechanism + does-not-solve + trade-offs; no principle/pattern-name tactics | §2 T1/T2/T5 instances |
| V7-06 No pattern-name-only nodes | Every FP/T justifies existence by mechanism, not name presence | Saga/CQRS/bulkhead/etc. nodes without mechanism bodies |
| V7-07 No vendor/tool tactic duplicates | Tactic split by mechanism only | Same mechanism under two vendor-named tactics |
| V7-08 GC traceability | Every GC-xxx maps to Stage 5/6 accepted case with provenance; 14 register rows covered (16-entry atomization recommended); no arbitrary new GCs | Missing row; invented GC; count mismatch unexplained |
| V7-09 GC boundary integrity | §5.3 qualifiers intact on every GC (OTP scope, GC-heap dimension, Arrakis dimension, seL4 proof-scope, governed-break governance, Linux single-owner, CRDT explicit merge, gateway placement, model-provided verification) | Genericized "example" GCs; missing false-flag field |
| V7-10 D-01..D-07/D-09 peer-distinct preservation | DISTINCT_FROM edges or page distinctions with discriminators for D-01, D-02, D-04, D-05, D-06, D-07, D-09 | Collapsed pairs per §6 loss vectors |
| V7-11 D-08 contextual wording | AX-003 wording unchanged; no universal safety floor anywhere | Safety-floor phrasing in domains/GCs |
| V7-12 D-10/D-12 gap carry | MP-004→RQ5-001 and MP-009→D-12/RQ5-004 gaps visible as NEEDS_EVIDENCE | Silent resolution; priority=admission; invented blast-radius metric |
| V7-13 D-11 proof-scope | MP-006 + seL4 GC keep question-relative scope | Proof-replaces-observability or telemetry-universal |
| V7-14 D-13 no locality resurrection | No H7/locality node or umbrella | Locality principle under any name |
| V7-15 D-14 multi-writer compliant | MP-008 + CRDT GC preserve multi-writer + explicit merge as compliant | Single-writer implication |
| V7-16 Relationship semantics documented | Every predicate has direction/meaning/transitivity/causality/inheritance in map header or report | Undocumented predicate; new predicate without owner approval |
| V7-17 No hidden evidence inheritance | EVIDENCED_BY direct only; MP source_ids ⊆ Constitution Sources lines; MP-003↮MP-009 and MP-004↮MP-005 cross-checks clean | Sibling citation borrowing |
| V7-18 MP-004/MP-005 edge form | Exactly peer RELATED_TO with navigation-only note; no parent semantics | Parent/child edge; support inference |
| V7-19 All refs resolve | Every node path, ID, S-*, RQ* in map + frontmatter resolves to existing file/manifest/queue entry | Dangling references |
| V7-20 No orphan durable nodes | Every FP/T/GC reachable from ≥1 index/MP/edge; every domain routes ≥2 nodes | Unreachable nodes; empty domains |
| V7-21 Stable IDs | Namespaces unique, sequential, append-only; MP-011/AX-005/P-006/H7 rules hold; V-*/S-*/RQ* untouched | Renumbering; ID reuse; namespace edits |
| V7-22 Lexical gate | High-risk terms qualified everywhere: service/component (V-002), write/state authority (V-003-D), consistency with V-010 suffix, V-008 four-way distinctions, failure domain vs blast radius, isolation/atomicity/stateless senses, flow control ≠ backpressure | Unqualified high-risk vocabulary; alias re-merge |
| V7-23 Source/RQ traceability | §7 rules hold; no uncited new claims; no source-prose duplication | Unsupported claims; corpus copying |
| V7-24 Progressive disclosure | Issue #18's five example paths resolve within path budget (§8); Router navigation-only | Corpus-wide loading defaults |
| V7-25 Router size/role | Router bounded and non-reasoning (OD-6 budget); no workflow/prompt/tool-routing | Playbook Router |
| V7-26 Domain duplication | Domain indexes route without restating node prose | Duplicate content across domains/nodes |
| V7-27 Domain routing quality | Each domain has scope + exclusions; symptom-keyword routing absent; shape-scope caveats on backend-concentrated domains | Ambiguous multi-domain fan-out |
| V7-28 Context efficiency | Focused question path ≤2 domains, ≤4 MP-equivalent nodes, sources on demand | Wide-loading design |
| V7-29 No unsupported claims | No new architecture claims beyond sealed semantics; no new evidence; claim-relative evidence classes respected | Invented universals; evidence-class inflation |
| V7-30 No Stage 8 smuggling | §12 table clean across all artifacts | Any smuggled artifact type |
| V7-31 RS ontology necessity | RS layer absent (verdict honored) or owner-approved proposal with evidence-forced instances only | Silent metrics ontology; symmetry-driven RS |
| V7-32 No arbitrary node count | Each FP/T/GC justified by retrieval value; thin-MP links acceptable | Coverage symmetry; count targets |
| V7-33 No empty-domain bureaucracy | All domain folders non-empty and routing ≥2 nodes | 14-folder mirror; one-line stubs |
| V7-34 No sibling evidence borrowing | Explicit re-run of V7-17 cross-checks on final tree | Late-added cross-citations |

---

## 14. Genuine owner decisions

1. **OD-1 Entity type set**: approve the seven-type minimum (§1) or direct otherwise. Challenger recommends approval with RS deferred.
2. **OD-2 Relation vocabulary**: approve the eight predicates and the five bad-edge rules (§3), including deferral of `OPERATIONALIZED_BY`.
3. **OD-3 Domain consolidation rule**: confirm "create only domains routing ≥2 durable nodes; merge thin ones; explain in report" (§4 R5), accepting that fewer than 14 domains is the expected outcome.
4. **OD-4 RS layer final gate**: accept NOT_NEEDED (§10) with the stated reopen conditions, or require Primary to propose a minimal RS layer despite the evidence bar.
5. **OD-5 GC atomization**: approve 16-entry atomization of the Stage 5 register (§5.2) or fix a different count with rationale.
6. **OD-6 Router budget**: set the concrete size/role bound for `00_ROUTER.md` (challenger suggests ≤150 lines, navigation table + disclosure rules only).

No other decision is new: MP-011 retirement, AX-005 disposition, P-006 demotion, D-01..D-14 results, RQ5 non-blocking status, and the Stage 8 boundary are already fixed by Issues #15/#18 and sealed Stage 5/6 artifacts.
