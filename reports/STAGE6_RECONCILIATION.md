---
id: REPORT-STAGE6-RECONCILIATION
type: challenger-reconciliation
stage: 6
status: complete
author: Codex harness + GLM 5.3 (Independent Reduction Challenger)
branch: challenge/stage6-reduction
date: 2026-09-20
issue: 15
fixed_primary: research/stage6-reduction@3f173c6f8c83f16b9367c7fe7e50e5af17997a65
fixed_blind_pass_a: challenge/stage6-reduction@0e82a3cab566bf9e8c30fd9017aaef2bceae604a
---

# Stage 6 Challenger Pass B — Reduction Reconciliation

## 1. Gate recommendation

**PASS_WITH_REMEDIATION**

Primary preserves all ten Stage 5 survivors, P-006 demotion, the decisive D-test distinctions, and the Stage 5 GOOD CASE boundaries. It also keeps P-013 as a discriminating causal claim rather than a tautology. The remaining defects are bounded editorial/category corrections; they do not require new evidence, a new candidate, a renumbering, or a Stage 7 ontology.

Promotion is conditional on these corrections:

1. remove MP-011 from the promoted Constitution, record `MP-011 RETIRED / NOT PROMOTED` in the reduction report, never renumber MP-001..MP-010, and never reuse MP-011;
2. correct the Constitution count to ten promoted MPs;
3. move AX-005's useful instruction into the usage contract and remove it as a standalone AX;
4. rewrite the mechanisms of MP-002, MP-005, MP-006, and MP-009 as specified in §12;
5. add an explicit, claim-relative evidence-status line to every promoted MP without converting source count into evidence strength;
6. remove MP-004/MP-005 references to a shared parent while preserving their peer distinction and GOOD CASE mappings.

## 2. Fixed Chief Architect decisions (OD6-1..OD6-4)

| Decision | Result | Reconciliation evidence |
|---|---|---|
| OD6-1 P-003/P-012 | **APPLIED: peer MPs** | Primary already maps P-003→MP-003 and P-012→MP-009, rejects a counted Resource Governance parent in reduction §5, and preserves D-04. No parent is to be added. |
| OD6-2 MP-011 | **APPLIED AS REQUIRED REMEDIATION: RETIRE / NOT PROMOTED** | Constitution currently contains MP-011 and reduction §§2/5 call it a derived parent with no new evidence. Its mechanism merely restates mechanisms already present in MP-004 and MP-005. Removal loses no mechanism, D-test, GOOD CASE, or source lineage. It must not become an AX. |
| OD6-3 P-007 | **APPLIED WITH REWRITE: retain conditional MP-006** | MP-006 names an operational question, evidence placement at paths/boundaries, and the seL4 proof-scope GOOD CASE. Its absolute sentence “缺失的证据不可事后补推” must be replaced by the non-derivability condition. |
| OD6-4 P-013 | **APPLIED: retain MP-010** | MP-010 explicitly states `assumed guarantee != model-provided guarantee`, names perturbations (scheduling, delay, reordering, cancellation, clock behavior), and exempts model-provided ordering/non-preemption/DBMS guarantees. It passes the tautology gate. |

## 3. V6-01..V6-26 execution

Status vocabulary: `PASS`, `PARTIAL`, `FAIL`, `CHECK_INVALID`. No preregistered check is invalid.

| Check | Status | Exact Constitution/reduction evidence | Mechanism / risk | Minimal correction |
|---|---|---|---|---|
| V6-01 Survivor accounting | **PASS** | Reduction §3 maps P-001/002/003/004/007/008/009/010/012/013 exactly once to MP-001..010; P-006 has a separate non-MP row. | No survivor is missing, duplicated, or silently absorbed. | None. |
| V6-02 P-006 demotion | **PASS** | Constitution “非原则登记” and reduction §4 keep P-006 as MP-002-associated measurable property/review signal; H7 is not revived and RQ3-001 is not triggered. | Change locality remains a metric/property, not a causal principle. | None. |
| V6-03 AX/MP category | **PARTIAL** | Constitution explicitly separates five non-causal AX items from MPs with mechanisms, but MP-011 says it is a “派生父原则” with “无新增证据” and adds no independently testable causal mechanism. | MP-011 is a category/abstraction error inside the MP inventory. | Retire MP-011; do not convert it to AX. |
| V6-04 Purpose fitness AX | **PASS** | AX-001 makes evaluation relative to required properties and constraints; it is not used as evidence for any MP. | Evaluation fitness remains a governing frame rather than an all-swallowing mechanism. | None. |
| V6-05 Product preservation AX | **PASS** | AX-002 forbids silent product-contract weakening; MP-007 separately addresses independent-consumer contract compatibility and governed migration. | Product-policy governance is not conflated with interface compatibility. | None. |
| V6-06 D-08 contextual AX | **PASS** | AX-003 begins “当存在适用的、不可协商的…” and explicitly rejects a domain-independent universal safety floor; reduction §8 repeats the bound. | D-08 remains `CONTEXTUAL ONLY`. | None. |
| V6-07 P-004/P-009 merge validity | **PARTIAL** | MP-004 and MP-005 retain separate propagation and privilege mechanisms, but Constitution adds MP-011 above both and reduction §5 claims shared causal content without independent evidence. | The children remain testable, yet the counted parent is linguistic compression rather than a causal reduction. | Retire MP-011; keep MP-004 and MP-005 as peers. |
| V6-08 D-05 preservation | **PASS** | MP-004 concerns propagation through shared resources/dependencies; MP-005 concerns actions enabled by granted trust/privilege. Reduction §5 explicitly gives low-privilege/high-failure-power and isolated/high-privilege directions. | Neither dimension acts as proxy for the other. | Remove only the parent references; retain both peer mechanisms. |
| V6-09 P-001/P-010 separation | **PASS** | MP-001 covers lifecycle ownership; MP-008 separately declares state authority and conflict/consistency semantics. Reduction §5 rejects an ownership/authority parent. | Cleanup responsibility cannot substitute for state conflict adjudication. | None. |
| V6-10 D-06 preservation | **PASS** | MP-001 Distinctions says it is not MP-008; MP-008 permits CRDT/multi-writer semantics and says it is not MP-001. | An authoritative state with orphan work and an owned cache with undefined conflict semantics remain separately diagnosable. | None. |
| V6-11 P-003/P-012 hierarchy | **PASS** | MP-003 and MP-009 are peers; reduction §5 explicitly rejects a Resource Governance parent as near-tautological. | Per-work bounds do not inherit or donate evidence to aggregate overload handling. | Preserve peer representation per OD6-1. |
| V6-12 D-04 preservation | **PASS** | MP-003 Distinctions names MP-009; MP-009 names MP-003 and D-04. Their statements separately cover bounded dimensions and overload behavior. | A bounded system with no overload policy and an admission-controlled path containing unbounded work can fail independently. | Rewrite MP-009 tactic-neutrally without merging it into MP-003. |
| V6-13 D-07 preservation | **PASS** | MP-001 assigns cancellation/cleanup semantics to ownership; MP-003 assigns execution/resource bounds. Reduction §6 preserves both. | Owned-but-unbounded and bounded-but-unowned work remain different violations. | None. |
| V6-14 P-002/P-008 separation | **PASS** | MP-002 hides identifiable volatile decisions; MP-007 protects contracts used by independent consumers and permits governed breaks. Reduction §15 rejects an evolvability merger. | Internal variation hiding and cross-party migration cost transfer remain distinct. | None. |
| V6-15 P-007 category | **PARTIAL** | MP-006 names a concrete operational question and states that signal/state placement determines obtainability, but its mechanism ends with the absolute “缺失的证据不可事后补推”. | The architecture-placement mechanism is valid; the absolute ignores inference from other retained evidence. | Use: if distinguishing information is neither captured nor otherwise derivable from retained evidence, reliable later attribution is impossible. |
| V6-16 P-007 proof scope | **PASS** | MP-006 excludes only questions “实际被证明且假设成立”; seL4 is a scoped GOOD CASE, and the Distinctions reject a scalar proof/observability substitution law. | Formal verification does not broadly replace operational evidence. | Keep the proof-scope boundary in the rewrite. |
| V6-17 P-013 tautology | **PASS** | MP-010 contains the assumed-vs-provided predicate, perturbation classes, concrete failure behavior, and model-provided GOOD CASES; reduction §7 states the durable demotion trigger. | The claim predicts false assumptions under perturbation and can distinguish compliant execution models. | None. |
| V6-18 D-02 preservation | **PASS** | MP-010 attributes failures to absent timing/order/cancellation/clock guarantees; MP-001 attributes leaks/orphans/stale work to ownership and cleanup. | A stale overwrite can be diagnosed as guarantee mismatch or ownership failure without collapsing the two. | None. |
| V6-19 D-09 preservation | **PASS** | MP-010 Distinctions says it is not MP-008; MP-008 uses authority plus explicitly qualified conflict/consistency semantics. | Execution ordering is not absorbed into an unqualified “consistency” claim. | None. |
| V6-20 GOOD CASE traceability | **PASS** | Constitution gives per-MP GOOD CASE fields; reduction §10 maps the full Stage 5 register to MP-001..010 or the P-006 non-principle disposition. §8 below rechecks each mapping after MP-011 retirement. | Removal of MP-011 loses no GOOD CASE because it only points back to MP-004/005. | Keep the explicit mappings; do not replace them with “preserved”. |
| V6-21 Evidence universality | **PARTIAL** | Reduction §9 lists source families and some concentration/scope caveats, but labels several MPs “强/很强” partly by family count; Constitution lists source IDs without an explicit evidence-status field. | Source quantity and sibling strength can be mistaken for universality; platform evidence remains claim-scoped. | Add the claim-relative status format in §10 and remove count-derived strength labels. |
| V6-22 Cross-shape scope | **PARTIAL** | Reduction §11 acknowledges MP-007 desktop evidence absence and MP-009 embedded/D-12 weakness; MP-004/006 list several shapes but some are examples rather than independent evidence. | The scopes are mostly child-specific, but checkmarks can overstate cross-shape support. | Replace broad checkmarks with claim/scope/concentration notes; retain D-12 `NEEDS_EVIDENCE`. |
| V6-23 Lexical gate | **PARTIAL** | MP-004 correctly separates failure domain from blast radius; MP-008 qualifies state authority and points consistency to V-010; MP-009 does not call backpressure and load shedding aliases. However MP-003 uses bare `service`, and MP-004/005/011 use generic subsystem/component language without the V-002 context note; MP-009 does not explicitly separate admission, backpressure, load shedding, and degradation. | Reduction can reintroduce ambiguous shape terms or let overload mechanisms blur together. | Qualify service/component usage by role/context and add the four-way mechanism distinction to MP-009/reduction. |
| V6-24 No unsupported compression | **FAIL** | MP-011 is justified by shared wording and child evidence, explicitly has no new evidence, and adds no prediction beyond MP-004/005. | A counted parent is unsupported causal compression even though the children remain present. | Retire/not promote MP-011 and preserve only a Stage 7 relationship handoff. |
| V6-25 Non-prescription | **PARTIAL** | Reduction §12 avoids process boundaries, single writer, telemetry stacks, and universal compatibility. MP-009 nevertheless says explicit admission control **and** degradation are mandatory. | The tandem wording over-prescribes two tactic families and can falsely require service-local shedding despite gateway/path-level control. | State a governed capacity boundary; list admission/rejection/backpressure/load shedding/degradation as distinct possible mechanisms selected by context. |
| V6-26 Stable lineage | **PARTIAL** | Every current AX/MP has P-* lineage and reduction §§3/6/10 retain D-tests and GOOD CASES, but the fixed retirement history for MP-011 is not yet recorded. | Deleting MP-011 without a tombstone would permit semantic ID reuse and obscure the rejected reduction. | Record `MP-011 RETIRED / NOT PROMOTED; ID reserved, never reuse`; keep MP-001..010 unchanged. |

**V6 totals:** 17 PASS, 8 PARTIAL, 1 FAIL, 0 CHECK_INVALID. The single FAIL is the unsupported counted MP-011 compression; all partials have bounded corrections.

## 4. Chief Architect findings CA6-1..CA6-10

| Finding | Result | Exact action |
|---|---|---|
| CA6-1 MP count | **CONFIRMED** | Constitution says “当前 12 条” but contains MP-001..011 (11 entries). After retirement, write “10 promoted Mother Principles; MP-011 retired/not promoted in reduction history.” |
| CA6-2 MP-011 category error | **CONFIRMED** | Removal loses no mechanism, D-test, GOOD CASE, or evidence: MP-004 contains propagation/containment and its two GOOD CASES; MP-005 contains privilege/trust minimization and its coarse-trust GOOD CASE; D-05 is stronger as a peer relation. |
| CA6-3 AX-005 redundancy | **CONFIRMED** | AX-005 repeats AX-001, usage-contract item 2, and the non-prescription rule. Classify `MOVE_TO_USAGE_RULE`; retain “Context > Pattern” once in usage contract, remove standalone AX-005. |
| CA6-4 MP-002 pseudo-equation | **CONFIRMED** | Delete `变更成本≈受影响单元数×单元成本`. Replace with: hiding an identifiable volatile decision behind a stable boundary can reduce the dependent units requiring coordinated modification when that decision changes. |
| CA6-5 MP-005 hard inequality | **CONFIRMED** | Delete `攻击者损害 ≤ 被攻破组件持有的权限`. State that less privilege/trust reduces directly available actions after compromise and limits one dimension of blast potential; it is not a bound on total damage. |
| CA6-6 MP-006 absolute irrecoverability | **CONFIRMED** | Replace “缺失的证据不可事后补推” with the captured-or-otherwise-derivable predicate from OD6-3. |
| CA6-7 MP-009 tactic overreach | **CONFIRMED** | The MP-level requirement is that overload encounter a governed capacity boundary before uncontrolled queue/resource growth. Admission control, backpressure, rejection/load shedding, and degradation are distinct mechanisms, not aliases or universally co-required service-local tactics. |
| CA6-8 evidence status | **CONFIRMED** | Source IDs alone are insufficient. Add a compact `Evidence status` line using accepted V-018 evidence classes plus claim scope, lineage concentration, and open RQ; never infer strength from count. |
| CA6-9 GOOD CASE traceability | **PASS WITH RETIREMENT UPDATE** | MP-004/005 retain direct cases after parent removal; MP-003/009 remain peer-scoped; MP-006 retains seL4 proof scope; MP-010 retains model-provided guarantees. Detailed mapping is in §8. |
| CA6-10 stable retirement | **CONFIRMED** | Do not renumber MP-001..010. Keep an explicit MP-011 tombstone in reduction history and reserve the ID permanently. |

## 5. AX final recommendation

| AX | Classification | Reason / final handling |
|---|---|---|
| AX-001 Evaluation Relativity | **KEEP_AX** | Independent evaluation frame: architecture judgments require required properties and real constraints. It is non-causal and does not evidence an MP. |
| AX-002 Product-Contract Protection | **KEEP_AX** | Independent governance constraint against silently deleting product capability; distinct from MP-007 compatibility mechanics. |
| AX-003 Contextual Non-Negotiables | **KEEP_AX** | Correct home for D-08 `CONTEXTUAL ONLY`; “when applicable” prevents a universal safety floor. |
| AX-004 Minimum Sufficient Complexity | **KEEP_AX** | Cost-side meta-objective that evaluates proposed architecture without pretending to cause a specific failure. |
| AX-005 Context > Pattern | **MOVE_TO_USAGE_RULE** | No independent governing function beyond AX-001 plus usage-contract item 2/non-prescription. Preserve the instruction once; remove the AX entry. |

**Final AX set:** AX-001..AX-004. AX-005 moves to the usage contract; its ID should not be reassigned during this remediation.

## 6. MP final recommendation

| MP | Stage 5 lineage | Classification | Required handling |
|---|---|---|---|
| MP-001 Explicit Ownership | P-001 | **KEEP_MP** | Keep managed-heap-only reclamation nuance and semantic lifecycle/ownership obligations. |
| MP-002 Change-Decision Boundaries | P-002 | **KEEP_WITH_REWRITE** | Remove the pseudo-equation and avoid using blast-radius language as a change-cost formula. Keep identifiable variation-axis scope. |
| MP-003 Bounded Execution | P-003 | **KEEP_MP** | Keep lifetime/per-work distinction; remain peer to MP-009. |
| MP-004 Failure Containment | P-004 | **KEEP_WITH_REWRITE** | Keep propagation/containment mechanism and dimension-specific GOOD CASES; remove `∝ Responsibility` title symbolism and all MP-011 parent references. |
| MP-005 Trust Minimization | P-009 | **KEEP_WITH_REWRITE** | Remove hard damage inequality; state direct-action reduction and one-dimensional blast-potential limitation. Remove MP-011 parent reference. |
| MP-006 Obtainable Diagnostic Evidence | P-007 | **KEEP_WITH_REWRITE** | Retain conditional MP and proof-scope boundary; replace absolute irrecoverability with captured-or-derivable wording. |
| MP-007 Contract Preservation | P-008 | **KEEP_MP** | Keep independent-consumer trigger and governed security/correctness/migration exceptions; do not mandate universal backward compatibility. |
| MP-008 State Authority & Conflict Semantics | P-010 | **KEEP_MP** | Keep state-authority qualification, consistency suffix discipline, and CRDT/multi-writer GOOD CASE. |
| MP-009 Governed Overload Boundary | P-012 | **KEEP_WITH_REWRITE** | Replace mandatory “admission + degradation” tandem with tactic-neutral governed capacity boundary and explicit mechanism distinctions; D-12 remains `NEEDS_EVIDENCE`. |
| MP-010 Execution-Model-Honest Correctness | P-013 | **KEEP_MP** | Preserve assumed-vs-provided predicate, perturbation mechanism, and model-provided GOOD CASES. |
| MP-011 Power Proportionality | P-004 + P-009 | **RETIRE_NOT_PROMOTED** | Remove from Constitution, do not convert to AX, do not renumber or reuse. Preserve stable retirement record only. |

**Final promoted MP set (10):** `MP-001, MP-002, MP-003, MP-004, MP-005, MP-006, MP-007, MP-008, MP-009, MP-010`.

## 7. D-01..D-14 preservation after bounded remediation

| D-test | Result | Final non-collapse boundary |
|---|---|---|
| D-01 P-001/P-002 | **PRESERVED — DISTINCT** | Lifecycle ownership (MP-001) vs identifiable change-decision boundaries (MP-002). |
| D-02 P-001/P-013 | **PRESERVED — DISTINCT** | Ownership/cleanup failure (MP-001) vs assumed execution guarantee failure under perturbation (MP-010). |
| D-03 P-002/P-006 | **PRESERVED — DEMOTION** | P-006 remains a review signal/property associated with MP-002, not an MP. |
| D-04 P-003/P-012 | **PRESERVED — PEER MPs** | MP-003 per-work/resource dimensions and MP-009 aggregate overload boundary can fail independently; no counted parent. |
| D-05 P-004/P-009 | **PRESERVED — PEER MPs** | MP-004 failure propagation and MP-005 privilege/trust remain independent; MP-011 retirement strengthens the distinction. |
| D-06 P-010/P-001 | **PRESERVED — DISTINCT** | MP-008 authority/conflict semantics does not follow from MP-001 ownership. |
| D-07 P-001/P-003 | **PRESERVED — DISTINCT** | Ownership/cancellation/cleanup and bounded execution remain separately violable. |
| D-08 safety floor | **PRESERVED — CONTEXTUAL ONLY** | AX-003 applies only when relevant external non-negotiables exist. |
| D-09 P-013/P-010 | **PRESERVED — DISTINCT** | MP-010 execution-model guarantees vs MP-008 state authority/conflict semantics. |
| D-10 blast-radius metric | **PRESERVED — NEEDS_EVIDENCE** | MP-004 does not claim an admitted universal metric; RQ5-001 remains. |
| D-11 P-007 | **PRESERVED — QUESTION-RELATIVE** | MP-006 applies to a concrete operational question not discharged by a stronger proved guarantee; depth remains cost/scope constrained. |
| D-12 P-012 | **PRESERVED — NEEDS_EVIDENCE** | Priority scheduling is not admission control; no universal embedded/cross-shape claim is promoted. |
| D-13 H7 | **PRESERVED — NOT RESURRECTED** | H7/locality remains demoted; P-006 remains a property signal. |
| D-14 P-010 CRDT | **PRESERVED — LEGAL GOOD CASE** | MP-008 explicitly permits multi-writer CRDT/local-first designs with declared authority and merge/conflict semantics. |

## 8. Stage 5 GOOD CASE non-violation mapping

| Stage 5 GOOD CASE | Exact final non-violation mapping |
|---|---|
| OTP supervised daemon | MP-001 is satisfied by explicit supervision/lifecycle ownership; indefinite daemon lifetime is not a violation. MP-003 evaluates relevant per-work dimensions, not total daemon lifetime. |
| Managed-heap GC reclamation | MP-001 exempts managed-heap memory reclamation only; semantic ownership, lifecycle, write authority, and aggregate budget remain answerable. MP-003 accepts a governed runtime soft budget. |
| Exploration with unknown variation axes | MP-002 does not require speculative boundaries before a likely change decision can be identified. |
| Indefinite service/system/stream lifetime with bounded work | MP-003 explicitly separates system lifetime from bounded execution/wait/retry/retention/queue/concurrency/fan-out dimensions. `service` must be read in its stated runtime context, not as an automatic network-service claim. |
| SQLite single-process economics | MP-004 does not require a process boundary or distributed containment when the shape/cost model does not justify one. |
| Arrakis dimension-specific protection | MP-004 credits only the I/O/failure-power dimension actually constrained by the mechanism; hardware delegation is not universal containment. |
| Broad but healthy coordinated change | P-006 is not a principle; wide change is not a violation where the change is coherent and the affected units legitimately share the decision. MP-002 judges whether a known volatile decision was usefully hidden. |
| seL4 proof-scope case | MP-006 discharges only the operational question actually proved under satisfied assumptions. Questions outside proof scope still require obtainable evidence where attribution matters. |
| Governed security/correctness compatibility break | MP-007 permits a deliberate break when a higher-priority security/correctness requirement explicitly governs the decision and migration. |
| Governed ecosystem migration | MP-007 permits coordinated migration with explicit consumer handling; it does not demand perpetual backward compatibility. |
| Linux internal API instability with stable external contract | MP-007 distinguishes tightly coordinated internal interfaces from independent-consumer contracts; internal instability is not automatically a violation. |
| Closed/coarse-grained trust | MP-005 does not require needless internal trust subdivision where no relevant untrusted-input, privilege-level, external-integration, or agent-action boundary exists and economics support coarse scope. |
| CRDT/local-first multi-writer | MP-008 permits multiple writers when authority and merge/conflict semantics are explicit. Single writer is not required. |
| Append-only log / read-only derived view | MP-008 treats explicit append/derivation semantics as a defined conflict/authority model, not a violation. |
| Gateway/path-level overload control | MP-009 requires an effective governed boundary on the request path, not service-local load-shedding code. |
| Actor mailbox ordering, event-loop non-preemption, DB transaction semantics actually provided by the model | MP-010 treats a documented/enforced model guarantee as a GOOD CASE; it flags only assumed guarantees that the selected model does not provide. |

MP-011 contributed no unique GOOD CASE. Its Constitution entry says “同子原则”, confirming that retirement loses none.

## 9. Lexical gate and non-prescription audit

### 9.1 Lexical findings

- **failure domain vs blast radius:** MP-004 correctly identifies failure domain as structural partition and blast radius as resulting impact measure. Keep both terms separate; do not say the domain itself is the radius.
- **authority:** MP-008 uses `write/state authority (V-003-D)`, distinct from authorization/security authority and evidence authority tier. MP-001 ownership must not be renamed to generic authority.
- **consistency:** MP-008 must continue to name the exact V-010 sense (`conflict semantics`, `consistency (replica/cache/transaction as applicable)`) rather than bare consistency.
- **backpressure vs load shedding:** MP-009 remediation must state that backpressure propagates capacity upstream, while load shedding rejects/removes work. Admission control, backpressure, load shedding, and degradation are related overload responses, not aliases.
- **flow control:** do not replace backpressure with flow control; V-008-E makes flow control the broader related term.
- **service/component/container:** qualify runtime role and boundary. `service` does not automatically mean a network-deployed unit; `component` does not imply independent deployment; C4 container and OS container are different senses.
- **evidence meta-language:** evidence class is claim-relative and authority tier is a source property. Neither is a synonym for confidence or universality.

### 9.2 Non-prescription findings

The final Constitution must not require:

- process boundaries for MP-004;
- a single writer for MP-008;
- OpenTelemetry or any telemetry stack for MP-006;
- service-local admission or shedding for MP-009;
- universal backward compatibility for MP-007.

Primary already avoids the first four in reduction §12 except that MP-009's mandatory “admission + degradation” wording is too narrow. The bounded rewrite in §12 resolves that issue without choosing a tactic.

## 10. Evidence universality and minimal evidence-status representation

### 10.1 Minimal compatible field

Add one compact line to every promoted MP:

`Evidence status: <V-018 claim-relative class(es)>; scope: <supported claim/shape>; concentration/gaps: <lineage concentration and open RQ>; Sources: <IDs>.`

Allowed classes come from existing project semantics: `NORMATIVE`, `THEORETICAL`, `EMPIRICAL`, `HEURISTIC`, `CONTESTED`, `CONTEXT_DEPENDENT`. This is not a new strength scale. `NEEDS_EVIDENCE` remains the existing gap/status marker where applicable. Authority tier stays in `source-manifest.yaml` and must not be copied as a claim-strength label.

### 10.2 Per-MP minimum status content

| MP | Minimal evidence-status content |
|---|---|
| MP-001 | `THEORETICAL + EMPIRICAL + CONTEXT_DEPENDENT`; structured-concurrency sources are one lineage; OTP is a scoped realization; GC evidence limits only reclamation. |
| MP-002 | `THEORETICAL + EMPIRICAL`; Parnas lineage supports information hiding; Shopify is an independent empirical shape; S-112 remains platform-scoped. |
| MP-003 | `THEORETICAL + EMPIRICAL + NORMATIVE`; Little's Law supports queue relationships, not every listed bound; incidents/platform contracts are dimension-scoped. |
| MP-004 | `EMPIRICAL + HEURISTIC + CONTEXT_DEPENDENT`; Arrakis constrains one protection dimension; SQLite is a counter-shape; RQ5-001 keeps metric operationalization open. |
| MP-005 | `NORMATIVE + THEORETICAL + CONTEXT_DEPENDENT`; least-privilege evidence supports direct authority reduction, not a theorem bounding total damage; platform examples stay scoped. |
| MP-006 | `EMPIRICAL + NORMATIVE + CONTEXT_DEPENDENT`; evidence-placement claim is question-relative; vendor observability material is not universal; seL4 only discharges proved questions. |
| MP-007 | `NORMATIVE + EMPIRICAL + CONTEXT_DEPENDENT`; contract stability depends on independent consumers/governance; Linux internal API is a boundary case, not a universal license to break contracts. |
| MP-008 | `THEORETICAL + NORMATIVE + EMPIRICAL`; source meanings must retain consistency qualifiers; CRDT/local-first evidence supports explicit multi-writer merge semantics. |
| MP-009 | `EMPIRICAL + CONTEXT_DEPENDENT + NEEDS_EVIDENCE`; vendor/SRE lineage is concentrated; gateway/path-level control is valid; D-12 and naturally bounded scope remain open. |
| MP-010 | `THEORETICAL + NORMATIVE + EMPIRICAL`; formal results are theorem-scope limited; platform guarantees are model-specific; RQ5-002 remains an operationalization gap. |

No MP may borrow a sibling's evidence. In particular, MP-009 may not inherit MP-003's broader theoretical support, and MP-005 may not inherit MP-004's containment evidence. MP-011 has no independent evidence and therefore cannot be promoted.

## 11. MP-011 retirement handling

The Primary remediation must make all four changes atomically:

1. delete MP-011 from the promoted MP section of `01_CONSTITUTION.md`;
2. change the Constitution inventory text to “10 promoted Mother Principles”;
3. add a stable reduction-history row: `MP-011 Power Proportionality — RETIRED / NOT PROMOTED at Stage 6 reconciliation; category/abstraction error; no independent causal mechanism or evidence; ID reserved and MUST NOT be reused`;
4. remove “与 MP-005 同父（MP-011）” and equivalent parent references from MP-004/MP-005, while retaining D-05 peer distinctions.

Retirement does not remove the analogy. Stage 7 may receive only this handoff note: `MP-004 RELATED_TO MP-005 via constrained cross-component impact/power`. This is a navigation/relationship hypothesis, not a Stage 6 AX, MP, parent, or ontology edge created now.

## 12. Bounded Primary remediation

Only `01_CONSTITUTION.md` and `reports/STAGE6_REDUCTION.md` require remediation. No P-*, source, manifest, review queue, or Stage 5 artifact changes are needed.

1. **Inventory/category:** promote MP-001..010 only; retire MP-011 per §11; retain IDs; remove AX-005 as standalone and keep its instruction in usage-contract item 2.
2. **MP-002 mechanism:** replace the pseudo-equation with: “把可事前识别的易变决策隐藏在稳定边界后，可以减少该决策变化时必须同步修改的依赖单元；实际成本仍取决于修改性质、验证、协调与发布条件。”
3. **MP-004 title/relationship:** rename without `∝` (for example `Failure Containment by Scoped Propagation Boundaries`), retain failure-domain/blast-radius distinction, remove parent language.
4. **MP-005 mechanism:** replace the inequality with: “减少授予的 privilege/trust 会减少组件被攻破后攻击者可直接执行的动作集合，并限制 blast potential 的一个维度；不构成总损害的硬上界。”
5. **MP-006 mechanism:** use: “若区分相关运行时状态所需的信息既未被捕获，也无法由其他保留证据推导，则无法可靠完成后续归因。” Keep concrete-question and proof-scope clauses.
6. **MP-009 statement/mechanism:** use a tactic-neutral causal core: “当工作需求可能超过可用容量时，相关请求/工作路径必须在无控制的队列或资源增长之前遇到有效、受治理的容量边界。” Then distinguish admission control, rejection/load shedding, backpressure, and graceful/functional degradation; selection and placement depend on system shape. Preserve gateway/path GOOD CASE and D-12 `NEEDS_EVIDENCE`.
7. **Evidence status:** add the compact field in §10 to each MP; replace “strong because N families” summaries with claim/scope/concentration descriptions.
8. **GOOD CASE and D-test update:** retain the §7/§8 mappings after removing all parent references; state explicitly that MP-011 retirement loses none.
9. **Lexical cleanup:** qualify bare service/component uses where they carry architectural meaning; keep authority and consistency senses explicit.

These changes are statement-level remediation. They do not alter the accepted P-* candidates or require a new source/backflow campaign.

## 13. Stage 7 handoff implications

The following are handoff inputs only; none is implemented in Stage 6:

- relationship/navigation: optionally record `MP-004 RELATED_TO MP-005`, with no parent semantics and no inherited evidence;
- cases/eval: carry every §8 GOOD CASE as a false-positive fixture and D-01..D-14 as discriminator/recall fixtures;
- evidence UI/schema: expose the claim-relative status, scope, concentration, and open RQ without converting source count to a score;
- tactics: represent admission control, backpressure, load shedding/rejection, and degradation as distinct tactics/mechanisms linked to MP-009 where applicable;
- metrics/properties: keep P-006 change amplification and RQ5-001 blast-radius measurement outside the MP set;
- domain layers: retain D-12 for embedded/RTOS capacity behavior, RQ5-003 for evidence/privacy cost, and RQ5-005 for named-vs-actual guarantee gaps;
- lexical validation: enforce V-002/V-003/V-008/V-010 qualifiers when Stage 7 builds relationships and examples.

## 14. Genuine new owner decisions only

**None.** OD6-1..OD6-4 resolve all material reduction choices. The remaining work is bounded conformance remediation and Stage 7 handoff bookkeeping, not a new product-policy, evidence-admission, or ontology decision.
