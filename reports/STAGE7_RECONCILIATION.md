``
id: STAGE7-RECONCILIATION
title: "Stage 7 Knowledge-Architecture Challenger — Pass B Reconciliation"
stage: 7
pass: B
role: independent-knowledge-architecture-challenger
challenger: "Codex harness + GLM 5.3"
branch: challenge/stage7-knowledge-architecture
date: 2026-09-20
issue: 18
fixed_primary: "research/stage7-knowledge-architecture@62614d4eaec91233d973666e4398368a39d3597c"
fixed_blind_pass_a: "challenge/stage7-knowledge-architecture@49e8031f8f83c5fdfd57bfe576dd12613c86e5ed"
control: "GitHub Issue #18 latest Chief Architect checkpoint; tasks/stage7/CODEX_PASS_B.md@origin/main"
status: COMPLETE
``

# Stage 7 Knowledge-Architecture Challenger — Pass B Reconciliation

## 0. Scope, method, and gate

Blindness lifted per Pass B contract. Read: the fixed Primary tree at `62614d4` in full (Router, Constitution, all 10 MP pages, 12 FP pages, 15 T pages, GC registry, 10 domain indexes + domains/index, relationship-map.yaml, STAGE7_KNOWLEDGE_ARCHITECTURE.md, principles/index.md), plus Issue #18's latest checkpoint, OD7-1..OD7-6, CA7-1..CA7-10, and the Pass A audit at `49e8031`. Sealed Stage 2-6 artifacts and the Primary branch were not modified. Deterministic validation ran via scripted parse of the map and every MP/FP/T frontmatter (CA7-10): 109 nodes / 126 edges / 0 duplicate IDs / 0 bad paths / 0 dangling endpoints / 0 frontmatter ref failures / 0 orphan durable runtime nodes.

**Gate recommendation: PASS_WITH_REMEDIATION.**

The Primary operationalizes the Constitution without semantic drift, keeps all category boundaries clean, preserves every D-test and all 16 GC qualifiers, passes mechanical integrity in full, and honors OD7-1..OD7-6. The defects are bounded and editorial: predicate metadata is documented only as one-line prose (CA7-1, V7-16 PARTIAL), the runtime-knowledge vs reference-node distinction is implicit in node types rather than explicit (CA7-2, V7-03 PARTIAL), 11 of 16 RELATED_TO edges are redundant with domain routing (CA7-3, V7-18 PARTIAL), and two GC entries lack the qualifier field `SEPARATE_SECTIONS` requires (GC-003, GC-012). None requires new evidence, new nodes, renumbering, or design change.

---

## 1. V7-01..V7-34 reconciliation matrix

| Check | Status | Exact Primary evidence | Mechanism / risk | Minimal correction |
|---|---|---|---|---|
| V7-01 MP semantic fidelity | **PASS** | All 10 MP pages carry the Constitution statement/mechanism/scope verbatim-in-substance; Evidence Status lines match claim-relative format; no 11th MP | Drift would corrupt the canonical base | None |
| V7-02 Canonical vs historical | **PASS** | `principles/index.md` separates canonical / historical / retired (AX-005, MP-011, P-005, P-011) / P-006 lineage; no P-* file edited in 93f5073..62614d4 | Blending would rewrite history | None |
| V7-03 AX boundary | **PARTIAL** | AX-001..004 live only in Constitution; no AX files; AX-005 absent from graph | Distinction between runtime knowledge and reference endpoints is implicit (node `type` values) not explicit (CA7-2) | Add one classification line to map header + report §1 (R7-2) |
| V7-04 FP category purity | **PASS** | All 12 FPs have signature+mechanism+trigger+amplification+consequences; none is a bare property/metric/tactic | Property-as-FP would inflate ontology | None |
| V7-05 Tactic category purity | **PASS** | All 15 Ts have Intent/Mechanism/Applies-When/Does-Not-Solve/Trade-offs; none restates an MP | Principle-as-tactic smuggling | None |
| V7-06 No pattern-name-only nodes | **PASS** | Circuit breaker/strangler/event sourcing/USE/SLO/hedged requests explicitly omitted (`tactics/index.md`); expand-contract omitted (RQ3-006) | Name-presence nodes | None |
| V7-07 No vendor/tool tactic duplicates | **PASS** | One mechanism per T; admission/backpressure/shedding/degradation kept as four distinct Ts with six DISTINCT_FROM edges | Vendor-split duplicates | None |
| V7-08 GC traceability | **PARTIAL** | All 16 GCs map 1:1 to Stage 6 §10 rows with provenance lines; count matches OD7-5 | GC-003 and GC-012 lack an explicit "what a naive reviewer would falsely flag" distinct from "why compliant" (R7-4) | Add naive-flag line to GC-003/GC-012 |
| V7-09 GC boundary integrity | **PASS** | All §5.3 qualifiers present: OTP scope, GC-heap reclamation-only, Arrakis I/O-dimension, seL4 proof-scope, governed-break governance, Linux single-owner, CRDT explicit-merge, gateway placement, model-provided verification | Genericized boundaries | None |
| V7-10 D-01/02/04/05/06/07/09 preservation | **PASS** | Seven DISTINCT_FROM MP edges with D-* notes; peer pairs D-04/D-05 double-protected by separate domains | Collapse of independent mechanisms | None |
| V7-11 D-08 contextual wording | **PASS** | AX-003 untouched in Constitution; `domains/security` scopes it "only when applicable"; no safety-floor claim | Universal safety floor | None |
| V7-12 D-10/D-12 gap carry | **PASS** | MP-004 HAS_GAP RQ5-001 ("not a universal metric"); MP-009/T-006 carry D-12; FP-010 false-positive separates policy quality from bound absence | Silent metric invention / priority=admission | None |
| V7-13 D-11 proof-scope | **PASS** | MP-006 question-relative; FP-007 signature uses the captured-or-derivable predicate; GC-008 keeps proof scope | Proof-replaces-observability | None |
| V7-14 D-13 no locality resurrection | **PASS** | No H7/locality node; `domains/evolution` exclusion line | Locality umbrella | None |
| V7-15 D-14 multi-writer compliant | **PASS** | MP-008 GOOD CASE; GC-013 with D-14; T-013 "not a single-writer principle" | Single-writer flattening | None |
| V7-16 Relationship semantics documented | **PARTIAL** | Map header gives one-line meanings per predicate; report §7 lists them | Direction/symmetry/transitivity/causality/evidence-inheritance not encoded per predicate (CA7-1) | Apply R7-1 schema block |
| V7-17 No hidden evidence inheritance | **PASS** | MP page `source_ids` equal Constitution lists; MP-009 note "not inherited by MP-003" on its S-048 edge; no cross-MP S-* borrowing | Sibling evidence borrowing | None |
| V7-18 MP-004/MP-005 edge form | **PARTIAL** | Edge exists with correct "NOT parent; NO evidence inheritance" note | 11 other RELATED_TO edges are redundant or need note precision (CA7-3) | Prune per §5 audit (R7-3) |
| V7-19 All refs resolve | **PASS** | Deterministic audit: 0 bad paths, 0 dangling endpoints, 0 frontmatter failures | Dangling refs | None |
| V7-20 No orphan durable nodes | **PASS** | Every FP/T/GC has ≥1 incoming edge; every domain folder routes ≥2 nodes | Dead nodes | None |
| V7-21 Stable IDs | **PASS** | Namespaces sequential append-only; AX-005 absent; MP-011 = retired-reserved type with zero edges; V/S/RQ untouched | ID reuse | None |
| V7-22 Lexical gate | **PASS** | Router standing constraints + MP-003/004/008/009 + T-007 flow-control note + FP-009 bare-consistency ban | High-risk term re-merge | None |
| V7-23 Source/RQ traceability | **PASS** | All `source_ids` exist; all `rq_refs` exist; 12 HAS_GAP edges match report §10 | Uncited claims | None |
| V7-24 Progressive disclosure | **PASS** | Report §13 five demonstrations each stay in budget (see §9) | Corpus-wide loading | None |
| V7-25 Router size/role | **PASS** | 47 lines; navigation table + load order + constraints; no reasoning content | Playbook drift | None |
| V7-26 Domain duplication | **PASS** | Domain indexes are routing tables (scope/refs/cross-domain/exclusions); no mechanism prose restated | Duplicate reconciliation burden | None |
| V7-27 Domain routing quality | **PASS** | Every domain has scope + exclusions; symptom rows in Router route by mechanism keyword | Ambiguous fan-out | None |
| V7-28 Context efficiency | **PASS** | Focused query ≈ router+constitution+1 domain+1-2 MP+1-3 FP/T ≈ well under 4 MP-equivalents; sources/reports never default | Wide loading | None |
| V7-29 No unsupported claims | **PASS** | FP/T bodies cite only admitted scope notes; no new universals; concentrations carried | Invented claims | None |
| V7-30 No Stage 8 smuggling | **PASS** | No playbook/question-bank/checklist/prompt/tool-routing/eval content anywhere | Reasoning smuggling | None |
| V7-31 RS ontology necessity | **PASS** | No `review-signals/` tree; P-006 in four homes (file, index, MP-002 lineage, evolution domain, GC-007); RQ5-001 as gap | Silent metrics ontology | None |
| V7-32 No arbitrary node count | **PASS** | 12 FPs / 15 Ts each justified; MP-002/MP-010 honestly have no T; thin links accepted | Coverage symmetry | None |
| V7-33 No empty-domain bureaucracy | **PASS** | 10 folders each route ≥2 nodes; 4 candidate families rejected with reasons (`domains/index.md`) | Folder mirroring | None |
| V7-34 No sibling evidence borrowing (re-run) | **PASS** | Final-tree re-check: MP-003/MP-009 and MP-004/MP-005 share no S-* via edges except pre-authorized navigation | Late cross-citations | None |

**V7 totals: 31 PASS, 3 PARTIAL, 0 FAIL, 0 CHECK_INVALID.**

---

## 2. Ontology node-type reconciliation (OD7-1 / CA7-2)

| Map node type | Classification | Default load target | Verdict |
|---|---|---|---|
| mother-principle (MP-001..010) | RUNTIME_KNOWLEDGE | Yes (via domain index) | Correct |
| failure-pattern | RUNTIME_KNOWLEDGE | Yes (via MP/EXPLAINS) | Correct |
| tactic | RUNTIME_KNOWLEDGE | Yes (via FP/MITIGATED_BY) | Correct |
| good-case | RUNTIME_KNOWLEDGE | Yes (when surface looks like violation) | Correct |
| domain | NAVIGATION_VIEW | Yes (the routing hop) | Correct |
| evaluation-axiom (AX-001..004) | REFERENCE_ONLY | No (Constitution only) | Correct |
| historical-candidate (P-001..013) | REFERENCE_ONLY | No (lineage targets) | Correct |
| review-signal-lineage (P-006) | REFERENCE_ONLY | No (MP-002 + evolution domain carry it) | Correct |
| retired-reserved (MP-011) | RETIRED_TOMBSTONE | No; zero edges attached | Correct |
| gap (RQ*) | REFERENCE_ONLY | No (queue only when named) | Correct |
| source (S-*) | REFERENCE_ONLY | No (disputed claims only) | Correct |

Router and relationship edges are infrastructure, not node types — matches OD7-1. The Primary's five runtime types match the approved set exactly. The only defect is explicitness: the report's "109 nodes" inventory table mixes these classes without the classification column, and the map header does not state which `type` values are runtime vs reference. Bounded fix R7-2 adds the classification without touching semantics.

---

## 3. FP disposition matrix

| FP | Title | Disposition | Basis |
|---|---|---|---|
| FP-001 | Unowned Runtime Work | **KEEP_FP** | Full causal chain; GC-001/GC-002; D-02 cross-ref to FP-012 |
| FP-002 | Hidden Variation-Axis Leak | **KEEP_FP** | Causal leak mechanism; honest no-tactic; D-03 note |
| FP-003 | Unbounded Per-Work Dimension | **KEEP_FP** (CA7-5 answered) | Title is property-flavored but body carries L=λW mechanism, triggers, amplification, GC-004/GC-002, explicit D-04 split from FP-010, dimension-specific evidence caveat. It is the causal family, not the dimension. |
| FP-004 | Shared-Resource Failure Cascade | **KEEP_FP** | Propagation mechanism; D-05 cross-ref; RQ5-001 kept open |
| FP-005 | Coupled-Defense Amplification | **KEEP_FP** | Distinct amplifier mechanism (S-050/S-063); honest scope note vs S-069 |
| FP-006 | Excess Privilege at Trust Boundary | **KEEP_FP** | Granted-authority mechanism; not total-damage theorem; D-05 |
| FP-007 | Missing Distinguishing Evidence | **KEEP_FP** | Question-relative captured-or-derivable predicate; D-11; CONTEXT_QUALIFIED status is correct |
| FP-008 | Ungoverned Independent-Consumer Contract Break | **KEEP_FP** | Cost-transfer mechanism; three governed-break GCs |
| FP-009 | Undefined Authority or Conflict Semantics | **KEEP_FP** | Two-dimension violation; V-010 suffix discipline; D-06/D-09 cross-refs |
| FP-010 | Ungoverned Overload Growth | **KEEP_FP** | Feedback-loop mechanism; D-04 split from FP-003 and FP-011 |
| FP-011 | Retry Amplification | **KEEP_FP** | Named antipattern (S-052); separated from bound issue and storm-vs-duplicate-effect |
| FP-012 | Assumed-vs-Provided Guarantee Mismatch | **KEEP_FP** | Discriminating predicate + perturbation mechanism; D-02 attribution rule |

No FP requires rewrite, demotion, or removal.

---

## 4. Tactic disposition matrix

| T | Title | Disposition | Basis |
|---|---|---|---|
| T-001 | Supervised / Structured Lifecycle | **KEEP_TACTIC** | Mechanism + Does-Not-Solve; not a universal invariant |
| T-002 | Cancellation Propagation | **KEEP_TACTIC** | Two V-008-C senses kept distinct; D-07 |
| T-003 | Timeout / Deadline Bound | **KEEP_TACTIC** | timeout≠deadline; D-07 ownership split |
| T-004 | Bounded Queue, Concurrency, Fan-out | **KEEP_TACTIC** | Occupancy caps; supplies bounds, is not backpressure itself |
| T-005 | Bounded Retry with Backoff/Jitter | **KEEP_TACTIC** | Honest "can cause FP-011"; retry≠idempotency |
| T-006 | Admission Control | **KEEP_TACTIC** | Enter/continue decision; D-12 priority≠admission |
| T-007 | Backpressure | **KEEP_TACTIC** | request(n) spec instance; flow-control≠backpressure |
| T-008 | Rejection / Load Shedding | **KEEP_TACTIC** | Direction opposite backpressure; four-way split |
| T-009 | Functional / Quality Degradation | **KEEP_TACTIC** | Demand reduction; not alias of isolation/shedding |
| T-010 | Scoped Failure-Domain Isolation | **KEEP_TACTIC** | Propagation cut; not generic process split; D-05 |
| T-011 | Least-Privilege Restriction | **KEEP_TACTIC** | Authority reduction; not containment |
| T-012 | Explicit Compatibility Direction and Migration Path | **KEEP_TACTIC** | Not universal compatibility; expand-contract excluded |
| T-013 | Explicit Merge / Conflict Semantics | **KEEP_TACTIC** | Declared semantics; not single-writer mandate |
| T-014 | Diagnostic Evidence Placement and Retention | **KEEP_TACTIC** | Question-relative; not telemetry-stack mandate |
| T-015 | Idempotency under Explicit Delivery Semantics | **KEEP_TACTIC** (CA7-6 verified) | Mitigates duplicate-effect damage only; "does not mitigate the storm itself" explicit; retry≠idempotency in Does-Not-Solve + DISTINCT_FROM; no delivery-semantics MP implied (principle_refs only MP-009) |

No T requires rewrite, demotion, or removal.

---

## 5. Domain disposition matrix and RELATED_TO edge audit (CA7-3 / CA7-4)

### 5.1 Domains

| Domain | Routes | Disposition | Basis |
|---|---|---|---|
| lifecycle | MP-001, FP-001, T-001/002, GC-001/002 | **KEEP_DOMAIN** | Distinct scope; D-02/D-06/D-07 cross-refs |
| evolution | MP-002, FP-002, GC-003/007, P-006 signal | **KEEP_DOMAIN** | Only home for the review signal; RQ2-009 exclusion |
| resources | MP-003, FP-003, T-003/004/005, GC-002/004 | **KEEP_DOMAIN** | D-04 peer with overload; OD7-3 mandates separation |
| reliability | MP-004, FP-004/005, T-010, GC-005/006 | **KEEP_DOMAIN** | Containment family; blast-radius exclusion |
| security | MP-005, FP-006, T-011, GC-012 | **KEEP_DOMAIN** | Trust vs propagation (D-05); RQ3-004/RQ2-008 gaps |
| observability | MP-006, FP-007, T-014, GC-008 | **KEEP_DOMAIN** | Proof-scope boundary; D-11 |
| integration | MP-007, FP-008, T-012/015, GC-009/010/011 | **KEEP_DOMAIN** | Contract family; expand-contract exclusion |
| state-data | MP-008, FP-009, T-013, GC-013/014 | **KEEP_DOMAIN** | Authority×conflict; D-14 |
| overload | MP-009, FP-010/011, T-005..009, T-015, GC-015 | **KEEP_DOMAIN** | Four-tactic distinction; D-12 |
| concurrency | MP-010, FP-012, GC-016 | **KEEP_DOMAIN** | Assumed≠provided; D-02/D-09 attribution |

All ten route ≥2 durable nodes with scope/exclusions; none duplicates mechanism prose; no merge candidates (OD7-3 forbids count-driven merging; resources/overload separation required by D-04). The four rejected candidate families (`domains/index.md`) are correct calls with reasons.

### 5.2 RELATED_TO edges (all 16)

| # | Edge | Disposition | Rationale |
|---|---|---|---|
| 1 | MP-004 → MP-005 | **KEEP** | Fixed by OD7-2; note already correct |
| 2 | P-006 → MP-002 | **KEEP** | Lineage navigation; precise note; not loadable knowledge |
| 3 | FP-010 → FP-011 | **KEEP** | Overload-growth vs retry-amplification navigation; keeps families separable; does not replace causal DISTINCT (they are not distinct-from; the note prevents merge) |
| 4 | FP-001 → FP-012 | **KEEP** | D-02 stale-overwrite attribution aid; note says "do not merge" |
| 5 | T-005 → T-015 | **KEEP** | retry/idempotency cooperation note; complements DISTINCT_FROM |
| 6 | AX-001 → AX-004 | **REMOVE_REDUNDANT** | Both are Constitution reference nodes; no retrieval decision routes through this edge; the relationship is stated in the Constitution itself |
| 7-16 | DOM-* → MP-* (10 edges) | **REMOVE_REDUNDANT** | The domain index file already performs this routing (its "AX / MP" section); the edge duplicates the index's function inside the graph, inviting readers to treat domain membership as a semantic claim. OD7-2: "Domain-home membership does not automatically justify a RELATED_TO edge." |

Summary: 5 KEEP, 11 REMOVE_REDUNDANT, 0 REWRITE_NOTE, 0 WRONG_RELATION. Removal is mechanical pruning of duplicated routing, not a semantic change; domains keep their routing role in their own files.

---

## 6. Predicate-schema recommendation (CA7-1 / R7-1)

Smallest compliant fix: replace the map header's one-line `predicates:` block with an explicit per-predicate schema (same eight predicates, no new ones):

``yaml
predicates:
  DERIVED_FROM:    {from: [MP], to: [P, retired], semantics: lineage, symmetric: false, transitive: false, causal: false, evidence_inheritance: false}
  EXPLAINS:        {from: [MP], to: [FP], semantics: violation-causes-failure, symmetric: false, transitive: false, causal: true, evidence_inheritance: false}
  MITIGATED_BY:    {from: [FP], to: [T], semantics: intervention, symmetric: false, transitive: false, causal: true, evidence_inheritance: false}
  RELATED_TO:      {from: [MP, FP, T, P], to: [MP, FP, T, MP], semantics: navigation-only, symmetric: true, transitive: false, causal: false, evidence_inheritance: false, note_required: true}
  DISTINCT_FROM:   {from: any, to: any, semantics: independently-violable, symmetric: true, transitive: false, causal: false, evidence_inheritance: false, note: discriminator required}
  EVIDENCED_BY:    {from: [MP, FP], to: [S], semantics: direct-citation, symmetric: false, transitive: false, causal: false, evidence_inheritance: false}
  HAS_GOOD_CASE:   {from: [MP, FP, T, P], to: [GC], semantics: non-violation-boundary, symmetric: false, transitive: false, causal: false, evidence_inheritance: false}
  HAS_GAP:         {from: [MP], to: [RQ], semantics: open-gap, symmetric: false, transitive: false, causal: false, evidence_inheritance: false}
``

Plus one header line: `node classes: runtime-knowledge = MP/FP/T/GC/domain-index; reference-only = AX/P/S/RQ; retired-tombstone = MP-011` (resolves CA7-2/V7-03 in the same edit). The Primary's one-line meanings are not wrong — they are insufficient for machine evaluation; this block is the minimal encoding of what OD7-2 requires.

---

## 7. GC-001..GC-016 integrity matrix

| GC | Boundary | Qualifier present | Naive-flag explicit | Provenance | Verdict |
|---|---|---|---|---|---|
| GC-001 | OTP supervised daemon | Yes (supervision=ownership; not universal invariant) | Yes | S5 §3.1 / S6 §10 | KEEP |
| GC-002 | Managed-heap GC + soft budget | Yes (reclamation only) | Yes | S5 §3.2 / S6 §10 | KEEP |
| GC-003 | Exploration unknown-axis | Yes (axis genuinely unidentified) | **No** — implied, not stated as a naive flag | S5 §3.3 / S6 §10 | KEEP + add naive-flag line (R7-4) |
| GC-004 | Indefinite lifetime | Yes (per-work judged) | Yes | S5 §3.4 / S6 §10 | KEEP |
| GC-005 | SQLite single-process | Yes (testing-page scope; graded) | Yes | S5 §3.5 / S6 §10 | KEEP |
| GC-006 | Arrakis I/O protection | Yes (dimension only) | Yes | S5 §3.6 / S6 §10 | KEEP |
| GC-007 | Broad coordinated change | Yes (signal not violation) | Yes | S5 §3.7 / S6 §10 | KEEP |
| GC-008 | seL4 proof-scope | Yes (proved questions under assumptions only) | Yes | S5 §3.8 / S6 §10 | KEEP |
| GC-009 | Governed security break | Yes (higher-priority + governance) | Yes | S5 §3.9 / S6 §10 | KEEP |
| GC-010 | Governed ecosystem migration | Yes (explicit governance, not debt license) | Yes | S5 §3.9 / S6 §10 | KEEP |
| GC-011 | Linux internal API | Yes (single-owner grading; not a license) | Yes | S5 §3.10 / S6 §10 | KEEP |
| GC-012 | Closed coarse-grained trust | Yes (absent relevant boundaries; supply-chain excepted) | **Partial** — supply-chain carve-out in "why compliant" but the naive-flag line is generic | S5 §3.11 / S6 §10 | KEEP + sharpen naive-flag (R7-4) |
| GC-013 | CRDT/local-first multi-writer | Yes (explicit merge, D-14) | Yes | S5 §3.12 / S6 §10 | KEEP |
| GC-014 | Append-only / derived view | Yes (explicit semantics define model) | Yes | S6 §10 | KEEP |
| GC-015 | Gateway/path-level admission | Yes (placement architectural) | Yes | S5 §3.13 / S6 §10 | KEEP |
| GC-016 | Model-provided guarantees | Yes (actually provided; ANSI names excluded) | Yes | S5 §3.14 / S6 §10 | KEEP |

14/16 fully complete; GC-003 and GC-012 need one added line each. No qualifier was weakened anywhere — the Stage 5/6 boundaries survived intact.

---

## 8. D-01..D-14 preservation and graph/ref/path/source/RQ mechanical audit

### 8.1 D-preservation (verified on the fixed tree)

| D | Evidence in Primary | Result |
|---|---|---|
| D-01 | DISTINCT_FROM edge + separate domains + MP-001/MP-002 cross-refs | **PRESERVED** |
| D-02 | DISTINCT_FROM + FP-001 RELATED_TO FP-012 "do not merge" + both FP bodies carrying attribution rule | **PRESERVED** |
| D-03 | P-006 = review-signal-lineage node; GC-007; no FP for change spread | **PRESERVED** |
| D-04 | DISTINCT_FROM MP-003/MP-009 + separate resources/overload domains + FP-003/FP-010/FP-011 three-way split | **PRESERVED** |
| D-05 | DISTINCT_FROM + non-parent RELATED_TO + MP-011 tombstone zero edges | **PRESERVED** |
| D-06 | DISTINCT_FROM MP-001/MP-008 + FP-009 orphan-writer cross-ref | **PRESERVED** |
| D-07 | DISTINCT_FROM + cancellation (T-002, MP-001) vs bounds (T-003/T-004, MP-003) | **PRESERVED** |
| D-08 | AX-003 contextual; no safety-floor node | **PRESERVED** |
| D-09 | DISTINCT_FROM MP-010/MP-008 + V-010 suffix in FP-009 | **PRESERVED** |
| D-10 | RQ5-001 HAS_GAP; no metric invented; FP-004 keeps it open | **PRESERVED** |
| D-11 | MP-006 question-relative; GC-008 proof scope; no scalar law | **PRESERVED** |
| D-12 | T-006 + FP-010 + overload domain carry NEEDS_EVIDENCE | **PRESERVED** |
| D-13 | No locality node; evolution exclusion | **PRESERVED** |
| D-14 | GC-013 + T-013 + MP-008 GOOD CASE | **PRESERVED** |

### 8.2 Mechanical audit (CA7-10, deterministically executed)

| Check | Result |
|---|---|
| Node IDs parsed / duplicates | 109 / **0** |
| Node path existence | **0 failures** |
| Edges parsed / endpoint resolution | 126 / **0 failures** |
| Predicate distribution | DERIVED_FROM 10, EXPLAINS 12, MITIGATED_BY 19, RELATED_TO 16, DISTINCT_FROM 18, EVIDENCED_BY 21, HAS_GOOD_CASE 18, HAS_GAP 12 |
| FP/T file uniqueness | 12 FPs, 15 Ts, **0 duplicates** |
| Frontmatter refs (source_ids → manifest files; rq_refs → queue; MP/FP/T/GC refs → graph nodes) | **0 failures across all 37 pages** |
| EVIDENCED_BY targets in manifest | **0 missing** |
| HAS_GAP targets in queue | **0 missing** |
| Orphan durable runtime nodes (FP/T/GC with no incoming edge) | **0** |
| AX-005 as node | **absent (correct)** |
| MP-011 node | type `retired-reserved`, **0 edges**, path → Stage 6 tombstone (correct) |
| `review-signals/` tree / RS-* IDs | **absent (correct)** |
| Stage 8 artifacts | **absent (correct)** |

---

## 9. Progressive-disclosure budget results (CA7-9)

Counting default loads per the Pass A budget (≤2 domains, ≤4 MP-equivalent knowledge nodes before optional source/RQ expansion; GC/tactic links optional unless the focused answer requires them):

| Demonstration | Default loads | Domains | MP-equiv nodes | Sources/reports default | Verdict |
|---|---|---|---|---|---|
| Overload / retry storm | Router + Constitution + overload index + MP-009 + FP-010 + FP-011 (+T-006..009 on demand) | 1 | 3 | No | **PASS** |
| Stale async / ownership | Router + Constitution + lifecycle index + MP-001 + FP-001 (+concurrency index + MP-010 + FP-012 for D-02 attribution) | 2 | 3-4 | No | **PASS** |
| Contract migration | Router + Constitution + integration index + MP-007 + FP-008 + T-012 (+GC-009..011 on flag) | 1 | 3 | No | **PASS** |
| Trust boundary / agent action | Router + Constitution + security index + MP-005 + FP-006 + T-011 | 1 | 3 | No | **PASS** |
| Observability vs formal guarantee | Router + Constitution + observability index + MP-006 + FP-007 (+concurrency MP-010 only if the question is guarantee-existence) | 1-2 | 2-3 | No | **PASS** |

All five stay within budget. The retry-count sub-path (resources domain, MP-003/FP-003) is optional and correctly marked as such in the demonstration. No path loads a Stage 5/6 report or a source by default.

---

## 10. CA7-1..CA7-10 explicit findings

| CA | Finding | Pass B result | Required action |
|---|---|---|---|
| CA7-1 | Predicate docs incomplete | **CONFIRMED (PARTIAL)** | R7-1 schema block (§6) |
| CA7-2 | Runtime vs reference nodes conflated | **CONFIRMED (PARTIAL)** — types are correct, classification is implicit | R7-2: add node-class line to map header + classification column to report §1 |
| CA7-3 | RELATED_TO needs pruning | **CONFIRMED (PARTIAL)** — 11/16 redundant (10 domain-home + AX edge), 5 KEEP | R7-3: remove 11 edges |
| CA7-4 | Domain 1:1 symmetry risk | **ADDRESSED** — each domain routes multiple nodes with distinct scope/exclusions; no prose duplication; judged by retrieval value | None |
| CA7-5 | FP-003 category | **KEEP_FP** — causal body defeats the title trap (§3) | None |
| CA7-6 | T-015 boundary | **VERIFIED CLEAN** — mitigates duplicate-effect only; retry≠idempotency explicit; no new MP | None |
| CA7-7 | Sparse EVIDENCED_BY | **ACCEPTED** — no unsupported claim found; page source_ids authoritative; edges carry load-bearing notes | None |
| CA7-8 | Reference/tombstone handling | **VERIFIED** — MP-011 zero-edge tombstone; AX/P/S/RQ reference-only; AX-005 absent; P-006 not promoted | None |
| CA7-9 | Budget check | **PASS on all five** (§9) | None |
| CA7-10 | Mechanical integrity | **FULL PASS** (§8.2) | None |

---

## 11. OD7-1..OD7-6 evaluation

| OD | Decision | Evaluation |
|---|---|---|
| OD7-1 | Minimal ontology model | **APPLIED** — five runtime types exactly; reference nodes lightweight; MP-011 tombstone-only |
| OD7-2 | Relation vocabulary | **APPLIED with remediation** — exactly eight predicates, no OPERATIONALIZED_BY; per-predicate metadata incomplete → R7-1 |
| OD7-3 | Domain consolidation | **APPLIED** — ten domains earn their folders; rejected families documented; resources/overload separate |
| OD7-4 | RS NOT_NEEDED | **APPLIED** — no RS tree; homes clean; reopen conditions unnecessary this stage |
| OD7-5 | GC-001..016 | **APPLIED** — all sixteen present at Stage 6 §10 granularity |
| OD7-6 | Router ≤150 lines | **APPLIED** — 47 lines, navigation-only |

---

## 12. Bounded Primary remediation set

| # | Remediation | Scope | Files |
|---|---|---|---|
| R7-1 | Encode per-predicate schema (direction/symmetry/transitivity/causality/evidence-inheritance) in map header | Header-only | `relationship-map.yaml` |
| R7-2 | Make runtime-knowledge vs reference-only vs tombstone classification explicit (map header line + report §1 column) | Two lines | `relationship-map.yaml`, `reports/STAGE7_KNOWLEDGE_ARCHITECTURE.md` |
| R7-3 | Remove 11 redundant RELATED_TO edges (10 DOM→MP + AX-001→AX-004); keep 5 with existing notes | Edge list only | `relationship-map.yaml` |
| R7-4 | Add explicit naive-false-positive lines to GC-003 and GC-012 (GC-012's must include the supply-chain carve-out) | Two lines | `cases/good-cases/index.md` |

All four are wording/schema-level; none changes semantics, IDs, counts, evidence, or structure beyond deleting duplicated routing edges. Executor: Primary (Cursor), one commit, before Stage 7 gate closure.

---

## 13. Stage 8 handoff implications

Stage 8 receives a clean substrate: five runtime knowledge types with stable IDs, an explicit predicate schema (post-R7-1), a pruned graph (post-R7-3), sixteen qualifier-bearing false-positive fixtures, and D-01..D-14 navigation intact. What Stage 8 must not do: re-derive principle semantics (Constitution is authoritative), add reasoning procedures into Router/domains (V7-30 boundary holds), or instantiate GC-001..016 as eval scenarios (that is Stage 10 fixture work). The RS reopen conditions (OD7-4) travel forward: if Stage 8+ needs executable review-signal fixtures, a minimal RS layer is a Chief Architect ontology decision, not an implicit addition.

---

## 14. Genuine new owner decisions

**None.** All findings resolve into the four bounded remediations whose categories (predicate schema, node classification, edge pruning, GC field completion) are already authorized by OD7-1/OD7-2/CA7-1..CA7-3 and the Pass A contract. No new evidence, type, predicate, domain, ID, or semantic change is requested. The only judgment call — whether the 10 domain-home RELATED_TO edges are "redundant" versus "harmless" — is decided by OD7-2's own rule ("Domain-home membership does not automatically justify a RELATED_TO edge"), not by a new owner decision.
