``
id: STAGE8-REASONING-AUDIT
title: "Stage 8 Independent Reasoning-Model Challenger — Pass A (Blind)"
stage: 8
pass: A
role: independent-reasoning-model-challenger
challenger: "Codex harness + GLM 5.3"
branch: challenge/stage8-reasoning-model
baseline: 818e098ae0ed9a20fac1e90d603e4d3dc4052ea9
date: 2026-09-20
issue: 21
blind: true
status: COMPLETE
``

# Stage 8 Independent Reasoning-Model Challenger — Pass A（Blind）

## 0. Scope, blindness, and method

Read (sealed only): `AGENTS.md`, `TASK.md`, GitHub Issue #21 (body + kickoff checkpoint), `planning/STAGE1_RESEARCH_PLAN.md` (RQ-C/RQ-D/RQ-E), `00_ROUTER.md`, `01_CONSTITUTION.md`, `02_VOCABULARY.md`, the full Stage 7 substrate on `main@818e098` (10 MP pages, 12 FP, 15 T, 16 GC, 10 domains + index, `relationship-map.yaml` including the applied R7 predicate schema), and the Stage 7 audit/reconciliation reports.

Not read: `research/stage8-reasoning-model`, any Cursor Stage 8 artifact, any unmerged Stage 8 Primary commit/PR. No source collection. No sealed artifact modified.

Method: this audit determines what a Stage 8 reasoning model **must and must not do**, independently of the Primary's design, and preregisters deterministic Pass B checks (`V8-01..`). It creates no competing playbook or question bank.

Division per Issue #21: GLM 5.3 owns the semantic/reasoning challenge; the Codex harness owns worktree/branch integrity, deterministic validation, and fail-closed delivery.

---

## 1. Minimum reasoning spine (recommendation)

The 18-step candidate spine in Issue #21 is a **coverage map, not a procedure**. As a fixed sequence it fails three ways: it implies every task traverses all 18 (checklist rigidity); steps 5-13 are knowledge domains that should activate on demand (a contract-migration review needs State/Authority only when a schema changes); and its center of mass assumes a backend/cloud service shape. The minimum reusable spine is **seven stages**, each with explicit entry conditions:

| # | Stage | Always active? | Content | Entry/exit rule |
|---|---|---|---|---|
| S1 | Intent & Required Properties | **Yes** | task mode, required properties (V-004-C), constraints, applicable non-negotiables (AX-003 contextual rule) | Exit when the protected-property set is stated or explicitly unknown |
| S2 | Evidence Baseline | **Yes** | inventory by evidence origin (§4), epistemic state per claim; project-fact precedence applied (§5) | Exit when each load-bearing claim has origin+state, or drift is flagged |
| S3 | Mechanism Hypotheses | On suspicion | candidate FP mechanisms routed via domains; shape-neutral wording (no default deployment topology) | Enter when a property is at risk or a suspicious surface exists; exit when hypotheses are enumerable |
| S4 | GOOD CASE Gate | On suspicion, **before verdict** | check `GC-001..016` qualifiers against the surface (§9) | Mandatory pass-through for any candidate defect; exit = eliminated or surviving hypotheses |
| S5 | Evidence Adjudication | On surviving hypothesis | discriminate hypotheses via cheapest discriminating evidence; epistemic state updated | Exit when CONFIRMED / HIGH_CONFIDENCE_RISK / NEEDS_EVIDENCE per hypothesis |
| S6 | Verdict & Minimum Correction | On adjudicated finding | severity by §6 thresholds; smallest correction breaking the mechanism (§8); alternatives/trade-offs when design task | Exit when correction is clear or escalation condition holds |
| S7 | Stop / Escalate / Unknowns | **Yes** | terminal state selection (§7); unresolved recorded as NEEDS_EVIDENCE, never fluent filler | Terminal — no continuation to fill sections |

Steps of the 18-spine not listed map as conditionals: Boundaries/Ownership, Execution Topology, State/Authority, Data/Control Flow, Resource Model, Failure Model, Trust, Observability, Change/Compatibility become **activation dimensions** under S3, keyed to the knowledge routes of Stage 7 domains — they are inputs to hypothesis formation, not mandatory stations. Alternatives/Trade-offs/Validation fold into S6 (design tasks) and S5 (review tasks). This keeps the spine shape-neutral (a desktop app, an embedded RTOS task, a CLI tool enter the same S1-S7 with different dimensions activated) and terminates by construction (S7 is terminal).

Missing from the Issue #21 candidate spine — and therefore must be explicit in the Primary's model: **intent recovery** (when the task statement itself is ambiguous, recover intent before required properties), **uncertainty tracking as a first-class output** (not a section to fill), and **validation of the verdict itself** (what evidence would falsify this conclusion).

---

## 2. Playbook-family recommendation (challenge area 2)

Task families must be justified by **differing reasoning procedures**, not by differing knowledge domains. Test each candidate family by: does it change the entry conditions, the evidence expectations, the stop conditions, or the output contract? If only the knowledge routes change, it is a routing parameter, not a playbook.

| Family | Distinct procedure? | Recommendation |
|---|---|---|
| Architecture Design (greenfield/major extension) | Yes — S6 outputs alternatives+trade-offs, not corrections; validation/proof dimension mandatory | Playbook |
| Architecture Review (as-is assessment) | Yes — S3 enters broad, S6 outputs severity-classified findings | Playbook |
| PR / Change Review | Yes — diff-scoped S2 (HISTORY origin dominant), minimum-correction rule central, regression-of-mechanism check | Playbook |
| Runtime / Concurrency Review | **Shared with Performance/Overload and Failure/Reliability** — same procedure (runtime evidence dominant, FP-hypothesis loop); different knowledge routes | Merge into one **Runtime/Operational Review** playbook with route parameters |
| Performance / Resource / Overload | — | Merge (above) |
| Failure / Reliability | — | Merge (above) |
| Integration / Contract / Evolution | Partially — independent-consumer analysis is a distinct evidence pattern (who are the consumers, compatibility direction) | Playbook, but scoped to contract-facing tasks |
| ADR / Decision Review | Yes — different output: decision quality (alternatives considered, reversibility, authority), not defect finding | Playbook |
| Incident Architecture Analysis | Yes — S2 starts from RUNTIME origin, timeline reconstruction, S5 is diagnostic-evidence adjudication | Playbook |

Result: **six playbooks** (Design; Review; PR/Change; Runtime/Operational [absorbing Performance/Overload/Failure]; Integration/Contract; ADR; Incident) — seven if Incident stays separate, which I recommend. Trigger rules must be disjunctive keywords on task intent, with an explicit overlap-routing rule (§ V8-04): when two playbooks match, route by **primary question** (what answer does the asker need), not by artifact type.

Anti-patterns to fail in Pass B: one playbook per label with identical internals (mode explosion — the 8-family hypothesis list copied verbatim); a single universal playbook (S1-S7 only, no family specialization — loses diff-scoping and incident-timeline procedures); unclear overlap (both PR-Review and Design claiming "add a service to existing system").

---

## 3. Highest-risk reasoning traps

| # | Trap | Concrete shape | Pass B detection |
|---|---|---|---|
| RT1 | Linear checklist | 18 sections every task must fill; completeness = filled sections | A reasoning trace showing untouched-dimension continuation |
| RT2 | Domain-as-dimension | "Step 7: State" forcing every task through state analysis even when no mutable state is in scope | Question activation not conditional on mechanism hypothesis |
| RT3 | Backend default | Examples/wording assuming services, queues, K8s; embedded/desktop/CLI treated as deviations | Shape-neutral spine wording; cross-shape demonstrations |
| RT4 | Pattern-name verdicts | "uses no circuit breaker" as finding; GC gate skipped | Verdict without GC-qualifier check in trace |
| RT5 | Best-practice blocker | "violates SOLID/best practice" without mechanism | BLOCKER lacking evidence+mechanism+failure+impact quadruple |
| RT6 | Rewrite reflex | Recommendation defaulting to re-architecture; minimum correction absent | Correction section lacking smallest-fix comparison |
| RT7 | Fluent certainty | Unknowns dressed as conclusions; no NEEDS_EVIDENCE output anywhere | Missing terminal unknown state |
| RT8 | Escalation both ways | Escalating queue-implementation choice; NOT escalating genuine product-capability trade-off | Escalation list not matching Issue #21 categories |
| RT9 | Evidence conflation | "S-xxx says" (origin) treated as "therefore confirmed" (state); count of sources as certainty | Origin and state fields collapsed into one |
| RT10 | Knowledge prose duplication | Playbook bodies re-explaining MP-009 mechanisms instead of routing | Playbook length; duplicated corpus content |
| RT11 | Stage 9 smuggling | Playbook written as system prompt ("You are..."; output format contracts for the agent runtime) | Prompt-language scan |
| RT12 | Question-bank trivia | "What is the CAP theorem?"-style recall questions | Questions not mechanism-oriented |
| RT13 | Eval leakage | Demonstrations phrased as expected findings/scorecards for future eval cases | Scenario/result semantics in report |

---

## 4. Evidence and verdict model requirements (challenge areas 4, 6)

Two orthogonal axes, never collapsed:

**Evidence origin** (where a claim comes from): `PRODUCT_INTENT / ARCHITECTURE_INTENT / CODE / CONFIG / TEST / RUNTIME / HISTORY / GENERIC_KNOWLEDGE / USER_ASSERTION`. Origin constrains what a claim can support: CODE origin cannot establish product intent; GENERIC_KNOWLEDGE cannot override RUNTIME for a project-specific behavior claim (V-018-B claim-relative discipline carried into reasoning).

**Epistemic state** (how decisive it is): `CONFIRMED / HIGH_CONFIDENCE_RISK / HYPOTHESIS / UNKNOWN / CONTESTED / NEEDS_EVIDENCE / NON_BLOCKING_IMPROVEMENT / PERSONAL_PREFERENCE`.

Rules the Primary must encode:

1. **Source authority ≠ claim confidence.** An A-tier source cited for an out-of-scope claim is still a HYPOTHESIS (Stage 7's claim-relative rule at reasoning level).
2. **Source count ≠ certainty.** Three sources of one lineage (CA4-10 concentration discipline) are one evidence family, not three.
3. **Every load-bearing claim in a verdict carries origin+state.** A finding with neither is rhetoric.
4. **Blocker threshold** (all four required): evidence in hand; causal mechanism (MP/FP link); concrete failure mode; material impact on a required property. "Might be bad", "not best practice", and taste are never blockers — respectively NEEDS_EVIDENCE, NON_BLOCKING_IMPROVEMENT, PERSONAL_PREFERENCE.
5. **NEEDS_EVIDENCE is terminal, not shameful**: a playbook must state when stopping there is correct (next discriminating evidence known but not obtainable now) versus lazy (discriminating evidence was available).
6. **Verdict falsifiability**: each CONFIRMED/HIGH_CONFIDENCE_RISK finding names what evidence would refute it.

---

## 5. Project-fact precedence and KNOWLEDGE_DRIFT (challenge area 5)

Four tiers for project-specific claims, highest wins:

1. Behavior truth: `CODE / CONFIG / TEST / RUNTIME` (current actual behavior)
2. Product intent: `PRODUCT_INTENT` (PRD, accepted requirements)
3. Architecture intent/history: `ARCHITECTURE_INTENT / HISTORY` (ADRs, accepted decisions, commits)
4. Generic mechanism knowledge: `GENERIC_KNOWLEDGE` (Stage 7 substrate — explains mechanisms and risks, never rewrites project facts)

`USER_ASSERTION` enters as a claim requiring an origin assignment (it may report RUNTIME observations), not as a tier.

**KNOWLEDGE_DRIFT** must fire on disagreement *within the project tiers* or *between project tiers and observed behavior*: (a) behavior vs product intent (code no longer implements accepted requirement); (b) behavior vs architecture intent (ADR says X, runtime does Y); (c) intent sources conflict (two accepted requirements contradict). The output is a drift record — both claims, origins, the delta, and the owner question — never a silent pick of one side. Generic-knowledge disagreement with project facts is not drift (that is the normal case of a generic risk applying or not); it is a hypothesis to adjudicate under S5.

---

## 6. ARCH_CONFLICT requirements (challenge area 7)

The model must separate **fundamental conflict** (two accepted requirements/non-negotiables cannot both hold under real constraints) from **implementation inconvenience** (satisfying both is possible but costly). Tests: does a concrete constraint pair exist? does relaxing the cost side preserve both properties? who owns each side?

Required ARCH_CONFLICT record fields (per Issue #21 core rule 5, operationalized): capability/required property; conflicting constraint; evidence for both sides; fundamental-vs-inconvenience judgment **with reason**; alternatives considered; trade-offs; reversibility; decision authority; evidence still needed. Product capability is preserved — the conflict is surfaced to its owner, never resolved by silently weakening the requirement (AX-002).

---

## 7. Stop conditions and escalation boundaries (challenge areas 8, 9)

Terminal states (any one ends reasoning): **NO_ARCHITECTURE_DEFECT** (properties protected, no material unresolved risk — the "no defect" answer must be representable and rewarded); **MINIMUM_SAFE_FIX** clear; **NEEDS_EVIDENCE** (with named next discriminating evidence); **OWNER_TRADE_OFF** (viable alternatives differ on owner-held preferences); **ARCH_CONFLICT** (authority beyond the agent). Unused sections are never a reason to continue — the anti-RT1 rule.

Escalate (authority decisions per Issue #21): product capability trade-off; cross-team commitment; regulatory/compliance interpretation; irreversible data/contract migration; security/trust policy; material cost/budget; contested evidence that changes the decision. Do NOT escalate: routine mechanism selection with sufficient evidence; implementation detail not altering required properties; personal preference. Under-escalation check: every ARCH_CONFLICT and every product-contract weakening must reach an owner. Over-escalation check: mechanism choices inside one team's authority with adequate evidence must terminate at MINIMUM_SAFE_FIX or NON_BLOCKING_IMPROVEMENT.

---

## 8. Minimum-correction requirements (challenge area 10)

For every review/change finding, the model must answer in order: which protected property is at risk; which mechanism causes the risk (MP/FP link); what is the **smallest** boundary/ownership/bound/resource/contract/evidence correction that breaks that mechanism; when would wider redesign actually be necessary (local fix cannot protect the property, or creates worse systemic risk). Default rewrites, fashionable substitution (microservices/queues/K8s/DDD/Clean per Issue #21 core rule 4), and abstraction-for-its-own-sake are RT6 failures. "No rewrite unless necessary" is a comparison rule, not a blanket prohibition — the model must show the comparison.

---

## 9. GOOD CASE / false-positive requirements (challenge area 11)

Before any verdict, S4 must check the sixteen GC qualifiers against the suspicious surface: supervised daemon indefinite run (GC-001), managed-heap reclamation (GC-002), unknown-axis exploration (GC-003), indefinite lifetime with per-work bounds (GC-004), SQLite single-process (GC-005), Arrakis dimension-specific protection (GC-006), broad coordinated change (GC-007), seL4 proof-scope (GC-008), governed breaks (GC-009/010), Linux internal API (GC-011), closed coarse trust (GC-012), CRDT explicit merge (GC-013), append-only/derived (GC-014), gateway-level admission (GC-015), model-provided guarantees (GC-016). The check is **qualifier-level, not title-level**: "it's a CRDT" eliminates nothing — "multi-writer **with declared merge semantics**" does. A surface matching a GC is not a defect; a surface not matching still needs the mechanism (RT4). Pattern-name matching (naming a missing pattern as the finding) is a categorical failure.

---

## 10. Progressive-disclosure requirements (challenge area 12)

Reasoning routes through Stage 7 without corpus loading: Router → one domain index → linked MP/FP/T → GC on suspicion → RQ when named → sources only on disputed/high-risk claims. Playbooks reference knowledge by ID and route, never by re-explaining mechanisms (RT10 — playbook prose duplicating MP content is both a context-efficiency and a drift risk). Question bank organized by reasoning dimension (activation keys), not technology. Budget expectation carried over from Stage 7 Pass B: focused question ≤2 domains, ≤4 MP-equivalent nodes before optional expansion; Stage 5/6/7 reports are provenance links, never default loads.

---

## 11. Stage 9 boundary (challenge area 13)

Stage 8 defines the reasoning contract. Stage 9 encodes it into prompts. Fail any Stage 8 artifact containing: system-prompt voice ("You are an architecture expert..."); agent role instructions beyond reasoning-procedure definitions; provider-specific formatting/wrappers; tool-runtime orchestration contracts; mode files as prompt files (playbook ≠ prompt: a DP file defines trigger/inputs/paths/stop/output **shape**, not persona or runtime behavior). The Stage 8 output is what Stage 9 **may** encode, and the reasoning demonstrations must be decision traces (route + activated sets + adjudication + terminal state), not hidden chain-of-thought or eval fixtures.

---

## 12. V8 preregistered checks (Pass B)

Status vocabulary: PASS / PARTIAL / FAIL / CHECK_INVALID. Executed against the Primary Stage 8 implementation on `research/stage8-reasoning-model`.

| Check | Pass condition | Failure signal |
|---|---|---|
| V8-01 Spine conditionality | Spine stages have entry conditions; dimensions activate on hypothesis, not sequence; no mandatory full traversal | 18-step linear procession; completeness = filled sections |
| V8-02 Spine minimality | ≤`10 stages; every stage changes procedure, not just topic | Domain-name stations; padding stages |
| V8-03 Spine shape-neutrality | Wording/examples cover backend + embedded/desktop/CLI without deviation framing | Backend-only center of gravity |
| V8-04 Playbook trigger clarity | Disjunctive intent-keyed triggers; overlap rule routes by primary question | Ambiguous dual-claim playbooks |
| V8-05 Playbook distinctness | Each playbook differs in entry/evidence/stop/output, not just knowledge routes; no label-per-file mode explosion | Identical internals under different names |
| V8-06 Playbook completeness | All seven families covered (incl. merged Runtime/Operational with parameters) | Missing task class |
| V8-07 Overlap routing | Explicit rule for multi-match; no gap where no playbook claims a task | Unclaimed task; contradictory claims |
| V8-08 No checklist rigidity | Questions activate on mode/shape/mechanism/uncertainty; traces show skipped dimensions terminating cleanly | Every-question designs; section-filling continuation |
| V8-09 Evidence-origin separation | Every load-bearing claim carries one of the nine origins | Origin collapsed or absent |
| V8-10 Epistemic-state separation | Every claim carries one of the eight states; origin ≠ state enforced | "Authoritative source ⇒ confirmed" |
| V8-11 Severity separation | Verdicts use the five-class scale; blocker quadruple (evidence+mechanism+failure+impact) enforced | "Best practice violation" blocker |
| V8-12 Blocker threshold | No blocker without the full quadruple | Rhetoric-severity findings |
| V8-13 NEEDS_EVIDENCE terminal | Representable, correct-vs-lazy distinction defined per playbook | Unknowns dressed as findings |
| V8-14 Project-fact precedence | Four tiers ordered; generic knowledge never rewrites project facts | Generic claim overriding RUNTIME |
| V8-15 KNOWLEDGE_DRIFT | Defined for the three intra/inter-project disagreement classes; output is a drift record, never silent pick | Silent resolution |
| V8-16 ARCH_CONFLICT completeness | All nine record fields present; fundamental-vs-inconvenience reasoned | Missing authority/reversibility |
| V8-17 Product-contract preservation | No silent weakening; AX-002 link | Requirement silently dropped |
| V8-18 Minimum correction | Four-question sequence present in review/change playbooks; comparison shown | Default rewrite; missing smallest-fix analysis |
| V8-19 No framework bias | No default-to-list (microservices/async/queues/K8s/DDD/Clean); alternatives compared neutrally | Fashionable substitution |
| V8-20 GOOD CASE gate | S4-equivalent mandatory pre-verdict check; qualifier-level matching | Title-level GC match; skipped gate |
| V8-21 No false-positive pattern matching | Findings name mechanisms, not missing pattern names | "No circuit breaker" finding |
| V8-22 Stop conditions | Five terminal states representable; unused-section continuation prohibited | Non-terminating analysis |
| V8-23 No-defect terminal | NO_ARCHITECTURE_DEFECT reachable and legitimate | Model cannot answer "no defect" |
| V8-24 Escalation conditions | Matches Issue #21 categories both directions; over/under tests present | Queue choice escalated; conflict unescalated |
| V8-25 Uncertainty handling | Unknowns tracked as output, not section filler | Fluent certainty |
| V8-26 Validation/proof | Design playbooks require falsifiability/refutation evidence per verdict | Unfalsifiable conclusions |
| V8-27 Progressive disclosure | Routes by ID into Stage 7; ≤2 domains / ≤4 MP-equivalents in demonstrations; no default report loads | Corpus-wide loading |
| V8-28 Knowledge refs resolve | All MP/FP/T/GC/RQ/S IDs cited by playbooks/questions exist and match graph paths | Dangling refs |
| V8-29 Question IDs stable | Namespaced, sequential, append-only; no reuse | Renumbering; duplicate IDs |
| V8-30 No technology trivia | All questions mechanism-oriented | Recall/definition questions |
| V8-31 No duplicated question sets | Overlapping playbooks reference shared bank sections, not copies | Copy-pasted question lists |
| V8-32 No corpus duplication | Playbooks route rather than re-explain; ≤ routing + procedure content | MP prose restated |
| V8-33 Cross-shape applicability | Demonstrations span ≥3 system shapes (e.g. service, embedded, desktop/CLI) | Single-shape demos |
| V8-34 No Stage 9 smuggling | No system prompt/persona/provider wrapper/tool-runtime contract/mode-as-prompt | Prompt-language in artifacts |
| V8-35 No eval leakage | Demonstrations are decision traces; no expected-findings/scorecard semantics | Eval fixtures in disguise |
| V8-36 Worktree/branch integrity | Challenger artifacts only on assigned branch/worktree; blind rule held | Cross-contamination |

---

## 13. Genuine owner decisions

1. **OD-1 Spine form**: approve the seven-stage conditional spine (§1) as the required minimum, or direct a different stage set. The 18-step candidate should be recorded as a coverage map, not a procedure.
2. **OD-2 Playbook count**: approve six-or-seven playbooks with the Runtime/Operational merge (§2), or require the Issue #21 hypothesis list verbatim (eight files) — the merge trades label familiarity for procedure honesty.
3. **OD-3 Question-bank granularity**: approve dimension-keyed organization with activation keys (per §10), versus playbook-local question copies — affects Stage 9 mode compilation.
4. **OD-4 Verdict vocabulary**: confirm the five-class severity scale and eight epistemic states as canonical names (refinements allowed but mapping must be total), or fix different names now before Stage 9 encodes them.
5. **OD-5 Escalation authority list**: confirm the Issue #21 escalation categories as the closed list, or amend (e.g. data-regulatory interpretation may need a named owner role in some organizations).

No other decision is new: Constitution semantics, Stage 7 substrate, progressive-disclosure budgets, GC boundaries, and the Stage 9 boundary are sealed by Issues #15/#18/#21.
