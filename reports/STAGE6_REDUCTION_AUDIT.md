---
id: STAGE6-REDUCTION-AUDIT
title: "Stage 6 Independent Reduction Challenger — Pass A (Blind)"
stage: 6
pass: A
role: independent-reduction-challenger
challenger: "Codex harness + GLM 5.3"
branch: challenge/stage6-reduction
baseline: 877d0fe32667eae51d5603357e82e75d6ee77ae1
date: 2026-09-20
blind: true
status: COMPLETE
---

# Stage 6 Independent Reduction Challenger — Pass A（Blind）

## 0. Scope and method

This audit independently reads the sealed Stage 5 candidate set, final dossiers, falsification/adversarial/reconciliation reports, D-01..D-14 results, GOOD CASE register, vocabulary gate, evidence manifest, review queue, and Issue #15. It did not read any content from `research/stage6-reduction`.

The task is reduction challenge, not Constitution authorship. This report allocates no AX-* or MP-* stable IDs, writes no competing `01_CONSTITUTION.md`, performs no Stage 7 work, and changes no canonical source, review queue, P-* or Stage 2/3/4/5 artifact.

Reduction is tested against five non-negotiable questions:

1. Does the abstraction retain a single causal mechanism rather than shared vocabulary?
2. Can the children still fail independently under accepted D-* cases?
3. Does the abstraction preserve the Stage 5 GOOD CASE/non-violation boundary?
4. Is the claim supported across the scope it now asserts?
5. Can the reduced claim be violated, or has it become an axiom, property, aspiration, or tautology?

## 1. Independent candidate-to-abstraction map

| Stage 5 input | Recommended reduction treatment | Category risk | Rationale |
|---|---|---|---|
| P-001 Explicit Ownership | **KEEP SEPARATE as MP candidate** | “explicit responsibility” can become an AX slogan | Causal mechanism is lifecycle/mutation responsibility: absent owner leaves cleanup, cancellation and mutation arbitration unassigned. D-01/02/06/07 show it fails independently from boundaries, execution-model guarantees, state authority and resource bounds. |
| P-002 Change-Decision Boundaries | **KEEP SEPARATE as MP candidate** | “modularity is good” / hindsight heuristic | Causal mechanism is information hiding around a reasonably identifiable variation decision. P-006 is a metric consequence, not a second MP. Exploration with unknown variation axes must remain a non-violation. |
| P-003 Bounded Execution | **PARENT/HIERARCHY with P-012; retain distinct refinement** | broad “resource governance” can become an aspiration | Governs per-work execution/wait/retention/retry/queue/concurrency/memory/fan-out demand against finite capacity. Indefinite service lifetime remains legal. |
| P-004 Failure Containment | **KEEP SEPARATE as MP candidate** | graded heuristic may be mistaken for universal law | Causal mechanism is propagation through shared dependencies/resources and structural failure-domain partitioning. Keep failure domain distinct from blast radius. |
| P-006 Change Locality | **DEMOTE remains final** | property incorrectly re-promoted as MP | Keep only as P-002-associated metric/review signal. No RQ3-001 rescue and no disguised “locality” MP. |
| P-007 Designed Diagnostic Surfaces | **CONDITIONAL KEEP as MP candidate** | required property/operability axiom | It has MP-level content only while it asserts a structural information mechanism: evidence absent at the relevant event/boundary cannot be reconstructed later. If reduced to “systems need observability/evidence,” demote to a required property/AX. |
| P-008 Contract Preservation | **KEEP SEPARATE as MP candidate** | product-policy axiom or “compatibility is good” | Causal mechanism is cost/risk transfer to independently evolving consumers. Governed security/correctness override and coordinated migration are explicit exceptions; internal single-owner interfaces remain a GOOD CASE. |
| P-009 Trust Minimization | **KEEP SEPARATE as MP candidate** | security floor / zero-trust universalization | Causal mechanism is damage authority bounded by granted privilege and validation at trust boundaries. D-05 separates it from dynamic failure propagation. |
| P-010 Authoritative State | **KEEP SEPARATE as MP candidate** | “single source of truth” alias collapse | Causal mechanism requires two explicit dimensions: write/state authority and conflict/consistency semantics. CRDT/multi-writer/log/local-first remain valid forms. D-06/D-09 prohibit ownership/timing merger. |
| P-012 Overload Admission & Graceful Degradation | **CHILD/PEER under resource-governance hierarchy with P-003; no flat merge** | backend/cloud tactic universalization | Governs aggregate arrival vs service capacity and explicit selection/degradation under overload. Priority scheduling is not admission control; D-12 remains NEEDS_EVIDENCE. |
| P-013 Execution-Model-Honest Correctness | **CONDITIONAL KEEP SEPARATE as MP candidate** | TAUTOLOGY_RISK / review rule | It survives only with the empirical, falsifiable predicate `assumed guarantee ≠ model-provided guarantee` and the perturbation failure mechanism. Model-provided guarantees are GOOD CASES. |

### Proposed compact structure

No flat candidate merge is presently lossless. The smallest safe structure is:

- separate causal MP candidates for P-001, P-002, P-004, P-007, P-008, P-009, P-010 and P-013;
- a **Resource/Capacity Governance** conceptual parent with two named, independently violable refinements: P-003 per-work bounds and P-012 aggregate admission/degradation;
- P-006 outside the MP set as a P-002 metric/property signal;
- non-causal evaluation rules kept in an AX section, not used as parents that swallow causal MPs.

If the resource parent is represented as one MP ID, both refinements and D-04 must remain normative subclauses with separate violation examples. A one-sentence parent that omits either refinement is a lossy merge. If that cannot be kept compact, use two peer MPs instead.

This yields **10 MP candidates before the P-007/P-013 category gates**, or 8–9 if either conditional candidate is correctly demoted. There is no evidence-based reason to force a smaller count.

## 2. High-risk merge/hierarchy challenges

### 2.1 P-004 + P-009: shared proportionality frame, different causal mechanisms

**Verdict: KEEP SEPARATE. At most share a non-counting thematic heading; do not create a causal MP parent without new evidence.**

The phrase “power should not exceed responsibility” hides two different variables:

- P-004 failure power is an emergent dynamic propagation capability through shared resources/dependencies. It is constrained by failure-domain design and observed as blast radius after failure.
- P-009 trust/privilege power is granted authority: what a compromised or mistaken component is permitted to read, write or execute. It is constrained by least privilege, validation and trust boundaries.

D-05 is not a minor implementation detail. A low-privilege reporting service can overload a shared database (P-009 satisfied, P-004 violated); isolated cells can still grant excessive privileges inside each cell (P-004 satisfied, P-009 violated). A unified “power≤responsibility” sentence explains neither propagation nor authorization and cannot tell the evaluator which evidence to inspect.

The shared proportionality language may be useful as an Evaluation Axiom or index heading only if it explicitly says the dimensions are not interchangeable. It should not count as a reduction of the two MPs. Making it an MP would be linguistic compression, not causal reduction.

### 2.2 P-001 + P-010: ownership is not state authority

**Verdict: KEEP SEPARATE; reject an “explicit authority/ownership” merge.**

P-001 allocates lifecycle, cleanup, cancellation and mutation responsibility for runtime entities/state. P-010 specifies who may decide state and how concurrent/replicated conflicts are resolved. D-06 demonstrates independent failure:

- an event log can be authoritative while an orphan projection worker has no lifecycle owner;
- a cache worker can have a clear owner while replica/cache consistency and conflict semantics remain undefined.

A generic “every thing needs an authority” parent also creates lexical risk: source of truth, system of record and authoritative state are not automatic aliases under the Stage 3 gate. It would invite single-writer assumptions and false-positive CRDT findings. No common parent adds causal explanatory power beyond a routing label.

### 2.3 P-003 + P-012: real common capacity mechanism, independent controls

**Verdict: PARENT WITH DISTINCT REFINEMENTS; no flat merge.**

Both address finite capacity under demand, so a resource/capacity-governance parent is causally more credible than the P-004/P-009 or P-001/P-010 parents. But D-04 proves two different controls:

- P-003 limits how much one unit/path can retain or amplify over time/space/concurrency/retries/fan-out;
- P-012 decides what aggregate work may enter/continue and which service is preserved when arrivals exceed capacity.

A fully bounded system can still shed critical traffic indiscriminately; an admission policy can still be defeated by unbounded retries or retained work. The parent must preserve both clauses. It must also preserve two GOOD CASE boundaries: indefinite system lifetime with bounded per-work dimensions, and gateway/path-level admission without service-local shedding code.

P-012’s evidence remains more backend/cloud-concentrated and D-12 remains NEEDS_EVIDENCE. Therefore the parent cannot universalize the P-012 child to every shape merely because P-003 has strong cross-shape evidence.

### 2.4 P-002 + P-008: both concern change, but the cost carriers differ

**Verdict: KEEP SEPARATE.**

P-002 controls internal change propagation by hiding volatile decisions. P-008 controls involuntary cost/risk transfer across independently evolving consumers. A well-decomposed module can still break an external contract; a stable external contract can front a poorly decomposed implementation. Merging them into “design for evolution” loses both causal mechanisms and the Linux internal-interface/governed-break GOOD CASES.

P-006 must not reappear as the parent. “Evolvability” is a protected property, not a causal reduction.

### 2.5 P-007 + P-013: evidence availability is not guarantee validity

**Verdict: KEEP SEPARATE.**

P-007 concerns whether evidence needed for unanswered operational questions is produced at the right boundary/path. P-013 concerns whether correctness depends on guarantees the execution model actually provides. Excellent telemetry cannot create an ordering guarantee; a formally specified ordering guarantee does not make hardware/integration/runtime evidence available. A parent such as “make assumptions observable/verifiable” would be a process slogan and erase both mechanisms.

## 3. AX vs MP category boundary

### 3.1 Likely Evaluation Axioms / governing constraints

These are useful Constitution inputs but are not causal Mother Principles:

1. **Required-property fitness:** evaluate architecture relative to required properties and real constraints. This defines the objective function; it does not cause a property to be protected.
2. **Product-contract preservation:** implementation difficulty must not silently delete required capability. This governs evaluation/escalation; it is not P-008’s contract-evolution mechanism.
3. **Contextual hard constraints:** applicable non-negotiable regulatory, safety, security or external contractual constraints bound the trade space. D-08 forbids universal safety-floor wording.
4. **Minimum sufficient complexity:** prefer no more structural/operational complexity than the protected benefit justifies. This is a meta-objective/evaluation heuristic, not a causal mechanism.

Stable AX IDs should be allocated only by the Primary/Chief Architect. The axioms must not be counted as evidence that a broad causal parent exists.

### 3.2 Items at category risk

- **“Power aligned with responsibility”** is AX-like proportionality language unless separate P-004/P-009 mechanisms remain visible. It is not currently a standalone MP.
- **P-004** itself remains causal when expressed as failure propagation + containment, despite its graded/economic scope. If reduced to “impact should be appropriate,” it becomes an AX/heuristic.
- **P-007** remains causal only with architectural placement and irrecoverable-information mechanism. “Evidence is important” is a required property/AX.
- **P-013** remains causal only with assumed-vs-provided mismatch and perturbation. “Correctness relies on true assumptions” is a tautological review rule.
- **P-006** is a property/metric, not AX and not MP.
- **P-008** is not the general product-contract AX: it specifically governs contracts used by independent consumers and migration/override mechanics.

## 4. D-01..D-14 preservation audit

| D-test | Reduction requirement | Loss signal |
|---|---|---|
| D-01 P-001/P-002 | Keep lifecycle/mutation ownership separate from change-decision boundaries. | Generic “clear responsibilities/boundaries” MP. |
| D-02 P-001/P-013 | Keep cleanup ownership separate from execution-model timing/order guarantees. | Stale overwrite and orphan timer assigned to one vague “runtime correctness” MP. |
| D-03 P-002/P-006 | P-006 remains metric/property under P-002 operationalization. | New Change Locality or Locality MP; RQ3-001 rescue. |
| D-04 P-003/P-012 | Parent may exist only with both independently testable refinements. | One resource MP with no bounded-no-admission and admission-no-bound examples. |
| D-05 P-004/P-009 | Preserve propagation containment vs granted privilege. | “Power≤responsibility” used as sole MP. |
| D-06 P-010/P-001 | Preserve state authority/conflict semantics vs lifecycle owner. | “Single owner/source of truth” parent. |
| D-07 P-001/P-003 | Preserve bounded-unowned and owned-unbounded cases. | Cancellation/timeout treated as one undifferentiated control. |
| D-08 safety floor | AX wording must remain contextual. | Universal safety/security floor independent of domain/product. |
| D-09 P-013/P-010 | Preserve execution order/timing guarantees vs state conflict/authority semantics. | Broad “consistency/correctness semantics” MP. |
| D-10 P-004 measurement | Carry NEEDS_EVIDENCE to operationalization. | Constitution invents a universal blast-radius metric or equates failure domain with blast radius. |
| D-11 P-007 | Keep question-relative proof scope and runtime phenomena outside proof. | “Formal proof replaces observability” or “all systems require service-style telemetry.” |
| D-12 P-012 cross-shape | Carry NEEDS_EVIDENCE; priority scheduling is not admission. | Parent inherits P-003’s cross-shape evidence and silently upgrades P-012. |
| D-13 H7 | Do not resurrect locality as MP/parent. | Distance/locality umbrella introduced for elegance. |
| D-14 P-010 | Preserve multi-writer + explicit merge as compliant. | Authority reduced to single-writer/central source. |

## 5. GOOD CASE preservation risks

| GOOD CASE / boundary | Reduction most likely to lose it | Required protection |
|---|---|---|
| OTP supervised daemon; GC reclamation nuance | P-001 merged with P-003/P-013 | Infinite service lifetime is not ownerlessness; GC exempts heap reclamation only. |
| Unknown-variation-axis prototype | P-002 generalized to “always modularize” | Boundary obligation begins only when a plausible variation decision exists and ceremony pays. |
| Indefinite service/stream lifetime | P-003/P-012 flat resource merge | Per-work bounds remain distinct from total service lifetime. |
| SQLite single-process economics | P-004 universalized | Containment degree is graded by propagation surface, risk and economics. |
| Arrakis dimension-specific protection | P-004 tactic abstraction | Hardware I/O protection is not generic replacement for all failure containment. |
| Broad but healthy coordinated change | P-006 resurrection | Change spread is a signal, not a violation by itself. |
| seL4 proof-scope case | P-007 generalized | Proof discharges only proved questions under satisfied assumptions; no service-telemetry universal. |
| RFC 7568 / PEP 404 / Linux internal API | P-008 merged into “compatibility” | Independent consumers and governed higher-priority overrides determine the boundary. |
| Closed coarse-grained local trust | P-009 universalized from enterprise zero trust | Fine-grained internal trust is not mandatory absent relevant boundaries/benefit. |
| CRDT/log/local-first | P-010 merged with P-001 | Distributed/multi-writer authority is valid with explicit merge/conflict semantics. |
| Gateway/path-level admission | P-012 reduced to service-local tactic | Admission location is architectural; service-local code is not required. |
| Actor order/event-loop non-preemption/DB semantics | P-013 abstracted to “explicit assumptions” | Model-provided guarantees are compliant even if application prose does not restate them. |

The reduction report should map each GOOD CASE to the surviving AX/MP/refinement. A generic “GOOD CASES remain applicable” sentence is insufficient traceability.

## 6. Evidence universality and cross-shape risks

| Candidate / abstraction | Evidence/scope risk | Reduction constraint |
|---|---|---|
| P-001 | Structured-concurrency sources form one conceptual lineage; OTP is runtime-specific. | Keep semantic ownership mechanism, not a universal supervision primitive. |
| P-002 | Parnas/SAIP/DDD evidence is theory/heuristic-heavy; variation-axis prediction is uncertain. | Do not state that every system has discoverable stable boundaries. Preserve exploration GOOD CASE. |
| P-003 | Strongest cross-shape evidence among survivors, but “bound” can be misread as finite lifetime. | Qualify per-work/resource dimension; avoid using strength here to upgrade P-012. |
| P-004 | Incident/cell evidence is backend/cloud-heavy; S-117/S-122 are dimension-scoped shape checks. | Keep graded applicability and exact failure dimension. No universal process/cell prescription. |
| P-007 | SRE/observability lineage is service-heavy; seL4 is proof-scope counterweight, not broad substitution law. | Use operational-question scope across embedded/desktop/local tools; do not require telemetry stack. |
| P-008 | Strongest direct evidence is protocol/schema/governance; behavior-semantic compatibility is thinner. | Keep contract scope and consumer independence explicit; do not claim universal machine-checkability. |
| P-009 | Classic least-privilege evidence is strong, but NIST zero-trust assumes enterprise contexts and agent evidence is new. | Scope to actual untrusted/cross-permission/action boundaries. |
| P-010 | DB/distributed/local-first evidence is strong; vocabulary is collision-prone. | Preserve two dimensions and qualification of authority/consistency; no source-of-truth alias shortcut. |
| P-012 | SRE/AWS concentration and D-12 non-server gap remain. | Parent hierarchy must not imply universal cross-shape admission evidence. |
| P-013 | Distributed/concurrency theory is strong; single-process operationalization is less direct. | Keep concrete model-provided GOOD CASES and perturbation failure class; no universal “document every assumption” rule. |

Backend/cloud bias is most likely to enter through P-004/P-007/P-012 and any resource/reliability parent that inherits their examples. Cross-shape scope must be attached per child/refinement, not once at a broad parent.

## 7. Likely lossy reductions

The following reductions should be rejected unless the Primary retains explicit child mechanisms and discriminator tests:

1. **“Explicit semantics/responsibility” umbrella for P-001/P-007/P-010/P-013.** It groups by the word explicit and loses lifecycle, evidence placement, state conflict and execution-guarantee mechanisms.
2. **“Power aligned with responsibility” as the sole P-004/P-009 MP.** It erases D-05 and confuses emergent failure propagation with granted privilege.
3. **“Resource governance” flat merge of P-003/P-012.** It loses D-04, indefinite-lifetime and gateway-admission GOOD CASES.
4. **“Evolvability” merge of P-002/P-006/P-008.** Evolvability is a protected property; it does not explain information hiding, change-spread measurement and consumer contract cost transfer.
5. **“Verifiability/legibility” merge of P-007/P-013.** Evidence availability cannot create model guarantees; model guarantees cannot reconstruct missing operational evidence.
6. **“Authority” merge of P-001/P-010.** It loses D-06 and risks source-of-truth/single-writer collapse.
7. **“Boundaries” merge of P-002/P-004/P-008/P-009.** Module, failure, contract and trust boundaries have different variables and causal effects.
8. **Purpose fitness as a parent MP over all survivors.** It is an AX/objective function and adds no causal explanation.
9. **Dropping child GOOD CASES after retaining a broad parent.** This produces an elastic Constitution that can rationalize any result while increasing false positives.

## 8. P-007 MP-level verdict

**Verdict: CONDITIONAL MP, with a narrow structural core.**

The non-trivial mechanism is not “observability is important.” It is: for an operational question not discharged by a stronger guarantee, information required to distinguish/attribute relevant runtime states must be generated and retained at the path/boundary where it exists, because absent information cannot be reconstructed after the event. This predicts a failure class and guides architecture placement without prescribing telemetry tooling.

Demote P-007 to an AX/required property if the reduction omits any of these:

- a concrete unanswered operational question;
- evidence placement at a relevant path/boundary;
- the irrecoverability mechanism;
- proof/assumption scope;
- a non-service GOOD CASE or explicit shape qualifier.

Privacy/security and telemetry cost are trade-offs, not the causal core. RQ5-003 must not be used to inflate them into a new universal claim.

## 9. P-013 tautology verdict

**Verdict: NOT A TAUTOLOGY IN ITS ACCEPTED STAGE 5 FORM; TAUTOLOGICAL UNDER GENERIC COMPRESSION. Keep as a conditional separate MP candidate.**

The accepted form has discriminating content:

- observable predicate: a correctness dependency can be compared with the actual primitive/contract/model guarantee;
- violation: `assumed guarantee ≠ provided guarantee`;
- causal mechanism: scheduler/network/clock/cancellation perturbation exercises behavior outside the assumed model and causes a specific failure;
- GOOD CASE: a guarantee really provided by actor mailbox ordering, non-preemptive event-loop segments or concrete DB transaction semantics must not be flagged.

This is more than “true assumptions are true.” It identifies a recurring architecture mismatch and an intervention: choose/enforce a primitive that provides the required guarantee or remove the dependency.

However, any reduced statement equivalent to “correct systems must rely on true guarantees,” “document assumptions,” or “understand the execution model” fails the MP gate. In that event, DEMOTE P-013 to an AX/review rule; do not rescue it with confident prose. It must not merge with P-001 or P-010 because D-02/D-09 show independent failure.

## 10. Pass B preregistered checks (V6-01..V6-26)

| Check | Pass condition | Failure signal |
|---|---|---|
| V6-01 Survivor accounting | All P-001/002/003/004/007/008/009/010/012/013 map exactly once to MP/AX/demotion disposition. | Missing, duplicated or silently absorbed survivor. |
| V6-02 P-006 demotion | P-006 remains property/review signal; no MP/H7/RQ3-001 rescue. | Change Locality/Locality reappears as MP. |
| V6-03 AX/MP category | AX items are explicitly non-causal constraints/objectives; MPs retain mechanisms. | Purpose/complexity/safety axiom counted as causal MP. |
| V6-04 Purpose fitness AX | Required-property fitness does not swallow or evidence causal MPs. | “Protect required properties” used as an MP mechanism. |
| V6-05 Product preservation AX | Implementation difficulty cannot silently delete product requirements and remains distinct from P-008. | Product-policy rule merged with contract compatibility. |
| V6-06 D-08 contextual AX | Hard constraints use “when applicable” scope. | Universal safety/security floor. |
| V6-07 P-004/P-009 merge validity | Separate propagation and privilege mechanisms remain independently testable. | Sole “power≤responsibility” MP. |
| V6-08 D-05 preservation | Both low-trust/high-failure-power and isolated/high-privilege cases are retained. | One dimension used as proxy for the other. |
| V6-09 P-001/P-010 separation | Lifecycle ownership and authority×conflict semantics remain distinct. | Generic authority/SSOT parent replaces both. |
| V6-10 D-06 preservation | Authoritative-state/orphan-worker and owned-cache/undefined-consistency cases remain. | Single owner implied to solve consistency. |
| V6-11 P-003/P-012 hierarchy | Resource parent, if used, names per-work bounds and aggregate admission/degradation as separate refinements. | Flat one-clause resource MP. |
| V6-12 D-04 preservation | Bounded-no-policy and policy-with-unbounded-work cases remain. | One child inferred from the other. |
| V6-13 D-07 preservation | Owned-unbounded and bounded-unowned remain separate. | Deadline/cancellation/ownership collapsed. |
| V6-14 P-002/P-008 separation | Variation hiding and independent-consumer contract cost transfer remain distinct. | Generic evolvability MP. |
| V6-15 P-007 category | MP text includes operational question, placement and irrecoverability mechanism. | “Observability/evidence is important.” |
| V6-16 P-007 proof scope | Only proved questions under satisfied assumptions are discharged. | Formal verification broadly replaces observability. |
| V6-17 P-013 tautology | Text retains assumed≠provided predicate, perturbation mechanism and GOOD CASE. | “Correctness relies on true guarantees.” |
| V6-18 D-02 preservation | P-013 timing mismatch and P-001 cleanup ownership remain separately diagnosable. | Unified runtime-correctness slogan. |
| V6-19 D-09 preservation | Execution guarantees and state authority/conflict semantics remain separate. | Timing/order absorbed into “consistency.” |
| V6-20 GOOD CASE traceability | Every Stage 5 GOOD CASE maps to a surviving MP/refinement/AX non-violation rule. | Generic preservation claim without mapping. |
| V6-21 Evidence universality | Each broad MP reports source-family concentration and claim scope. | Source count used as universality proof. |
| V6-22 Cross-shape scope | P-004/P-007/P-012 scopes remain child-specific; D-12 stays NEEDS_EVIDENCE. | Parent inherits stronger sibling evidence. |
| V6-23 Lexical gate | failure domain≠blast radius; authority terms qualified; flow control≠backpressure; P0/high-risk terms qualified. | Alias compression or unqualified high-risk vocabulary. |
| V6-24 No unsupported compression | Every merge demonstrates one deeper mechanism or retains named child mechanisms. | Merge justified by elegance/count/shared words. |
| V6-25 Non-prescription | MPs do not mandate process boundaries, single writer, telemetry stack, service-local admission or universal compatibility. | Tactic/platform choice promoted to principle. |
| V6-26 Stable lineage | Every AX/MP maps back to P-* evidence, D-* and GOOD CASES; removed IDs are not recycled. | Lost provenance or semantic ID reuse. |

## 11. Genuine owner decisions

1. **Resource governance representation:** choose one parent MP with two mandatory named refinements (P-003/P-012) or two peer MPs under a non-counting heading. Challenger recommends the hierarchy only if D-04 and child-specific evidence/scope remain explicit; otherwise keep two peers.
2. **“Power aligned with responsibility” status:** decide whether it appears as a non-counting heading/AX-like interpretation rule or is omitted. Challenger recommends no standalone MP because P-004/P-009 lack one shared causal mechanism.
3. **P-007 promotion threshold:** accept the narrow evidence-placement/irrecoverability mechanism as MP-level, or demote to required property/AX if Primary reduces it further. Challenger recommends conditional MP retention.
4. **P-013 final category:** accept the full assumed≠provided + perturbation + GOOD CASE formulation as a conditional MP, or demote if the Primary compression is generic. Challenger verdict is conditional MP; a tautological compression must be demoted.

No other owner decision is new. P-006 demotion, D-08 contextual scope, Stage 5 dispositions, RQ5 non-blocking status and the no-Stage-7 boundary are already fixed.
