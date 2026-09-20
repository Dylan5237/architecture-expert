---
id: REPORT-STAGE8-REASONING-MODEL
type: stage-report
stage: 8
author: Cursor (Primary Reasoning-Model Architect)
branch: research/stage8-reasoning-model
date: 2026-09-20
issue: 21
baseline: 818e098ae0ed9a20fac1e90d603e4d3dc4052ea9
---
# Stage 8 Reasoning Model

Compact reusable spine + five procedurally distinct playbooks + a conditional question bank. Sealed Stage 2–7 semantics were not changed. No Stage 9 system prompt, provider mode files, eval fixtures, or source collection.

## 1. Final reasoning spine + rationale

Issue #21’s 18 labels were tested as a **coverage inventory**, not a required path.

**Core (always, 6 steps):** (1) task class → DP; (2) intent & required properties & applicable non-negotiables; (3) evidence baseline with origin ≠ epistemic state; (4) activate only justified mechanism dimensions; (5) GC check, then min-correction / alternatives / `ARCH_CONFLICT`; (6) verdict, stop, or escalate.

**Conditional dimensions:** ownership, change-decision boundaries, per-work bounds, failure propagation, trust, diagnostic evidence, contracts, state authority, overload path, execution-model honesty. Each maps to one Stage 7 domain. Skip any dimension that cannot change the decision.

**Merged Issue #21 steps:** 1–3 → core 2; 4 → core 3; 5–13 → conditional dimensions (optional, not ordered); 14–18 → core 5–6.

**Rationale:** a mandatory 18-step tour would violate progressive disclosure, AX-004, and the “not a checklist” constraint. The core is the smallest sequence that still enforces properties-first, evidence-before-verdict, GC discipline, and stop/escalation.

Entry: `00_ROUTER.md` for knowledge need, then `decision-playbooks/index.md` for procedure. Exit: shared output contract when a stop rule fires.

## 2. Playbook inventory and why each is distinct

| ID | Title | Object of reasoning | Procedure |
|---|---|---|---|
| DP-001 | Architecture Design | not-yet-built capability | forward synthesis, min-sufficient |
| DP-002 | Architecture Review | existing system as-is | diagnose vs properties; `NO_DEFECT` legal |
| DP-003 | Change / PR Architecture Review | a delta | delta-scoped evidence; min correction to the PR |
| DP-004 | Architecture Decision Review | ADR/RFC/options | alternatives, reversibility, authority |
| DP-005 | Incident Architecture Analysis | observed failure | backward attribution; competing mechanisms |

Issue #21 candidates **not** given files: Runtime/Concurrency, Performance/Resource/Overload, Failure/Reliability, Integration/Contract/Evolution. They share DP-002/003/005’s procedure and differ only in first domain + question section. They are **overlays** in the index.

P-005 reversibility is a DP-004 question, not a revived principle. H7 locality is not instantiated (D-13).

## 3. Playbook trigger / overlap matrix

| Situation | DP | If confused with |
|---|---|---|
| Greenfield / new slice | 001 | 002 (no current object) |
| Existing system health | 002 | 001 (redesign first); 003 (no delta) |
| PR / migration / flag | 003 | 002 full tour; 005 unless already failing |
| ADR / options paper | 004 | 001 (no artifact); 003 (implementation) |
| Live incident / near-miss | 005 | 001 rewrite; 003 unrelated diff |

**Overlap rule:** choose the *object*, not the vocabulary. A PR that caused an incident is DP-005 until attribution, then DP-003 for the fix. Overlay never creates a sixth DP.

## 4. Question-bank taxonomy

`question-bank/index.md`: 16 sections, **Q-001..Q-055**.

| Section | IDs | Role |
|---|---|---|
| Q-INT Intent / product contract | Q-001..003 | properties, AX-002, consumers |
| Q-EVD Evidence / baseline | Q-004..007 | precedence, drift, discriminating observation |
| Q-PRP Properties / constraints | Q-008..010 | AX-003 contextual, ARCH_CONFLICT vs inconvenience |
| Q-OWN Ownership | Q-011..014 | MP-001, D-02, D-06, D-07 |
| Q-XCN Execution / concurrency | Q-015..017 | MP-010, assumed vs provided |
| Q-STA State / conflict | Q-018..020 | MP-008, V-010, D-14 |
| Q-FLW Data / control flow | Q-021..022 | late/dup/reorder, continuations |
| Q-RES Per-work bounds | Q-023..025 | MP-003, D-04 split |
| Q-OVL Overload path | Q-026..029 | MP-009, V-008 aliases, retry≠idempotency |
| Q-FAL Failure / propagation | Q-030..033 | domain≠blast, D-05, RQ5-001 |
| Q-TRS Trust | Q-034..036 | MP-005, GC-012 carve-out |
| Q-OBS Observability | Q-037..039 | FP-007 vs stack, GC-008 |
| Q-INTG Integration | Q-040..042 | GC-009..011 |
| Q-EVL Evolution | Q-043..045 | GC-003/007, P-006 signal |
| Q-ALT Min correction / alternatives | Q-046..049 | AX-004 |
| Q-VAL / Q-UNK | Q-050..055 | proof, stop, escalate, ARCH_CONFLICT |

No technology trivia. No per-playbook duplicated question text.

## 5. Evidence model

**Origin:** PRODUCT_INTENT, ARCHITECTURE_INTENT, CODE, CONFIG, TEST, RUNTIME, HISTORY, GENERIC_KNOWLEDGE, USER_ASSERTION.

**Epistemic state:** CONFIRMED, HIGH_CONFIDENCE_RISK, HYPOTHESIS, UNKNOWN, CONTESTED, NEEDS_EVIDENCE, NON_BLOCKING_IMPROVEMENT, PERSONAL_PREFERENCE.

Same token may appear as verdict and as epistemic state (`HIGH_CONFIDENCE_RISK`, `NEEDS_EVIDENCE`). They are not interchangeable: origin never implies confidence; a RUNTIME point can be `HYPOTHESIS`.

## 6. Evidence sufficiency / verdict thresholds

| Verdict | Sufficiency |
|---|---|
| BLOCKER / MUST_FIX | Accepted requirement or applicable non-negotiable violated; **evidence + mechanism + failure mode + material impact**; GC does not apply |
| HIGH_CONFIDENCE_RISK | Strong evidence of material architecture risk; not a proven requirement violation |
| NEEDS_EVIDENCE | Named next discriminating evidence; stop allowed (all DPs) |
| NON_BLOCKING_IMPROVEMENT | Properties already protected |
| PERSONAL_PREFERENCE | Taste; never blocker; never sole escalation |
| NO_DEFECT | Mechanism absent or GC matches |
| ARCH_CONFLICT | Fundamental capability vs constraint; not inconvenience |

Fluent “might be bad” is below threshold.

## 7. Project-fact precedence

- Current behavior: CODE/CONFIG/TEST/RUNTIME > GENERIC_KNOWLEDGE > USER_ASSERTION.
- Intended behavior: PRODUCT_INTENT > GENERIC_KNOWLEDGE > inference.
- Architecture intent/history: ARCHITECTURE_INTENT / HISTORY / explicit owner decision > inference.

Generic knowledge names mechanisms. It does not rewrite project facts.

## 8. KNOWLEDGE_DRIFT

Emit when project-fact origins disagree, or generic knowledge would deny a project fact, or USER_ASSERTION contradicts higher-precedence origin.

Record claims, origins, epistemic states, next evidence. Do not silently pick. Drift is not automatically BLOCKER; the drifted behavior vs required property may be.

## 9. ARCH_CONFLICT

Required fields: capability/required property; conflicting constraint; evidence; fundamental-vs-inconvenience; alternatives; trade-offs; reversibility; authority owner; evidence still needed.

Inconvenience alone is invalid. Silent product-contract shrink is forbidden (AX-002). Q-010, Q-055.

## 10. Stop conditions

Shared six (index): properties protected; defect+min correction clear; owner trade-off among viable options; NEEDS_EVIDENCE with next observation; ARCH_CONFLICT needs authority; further detail would not change the decision.

DP-specific additions: DP-001 stops if properties cannot be stated; DP-002/005 treat `NO_DEFECT` as success; DP-003 stops at delta-scope even if the rest of the system is imperfect; DP-004 stops when multiple viable options remain (escalate preference).

Do not continue to fill unused sections.

## 11. Escalation conditions

Escalate: product capability trade-off; cross-team commitment; AX-003 interpretation; irreversible data/contract migration; security/trust policy; material cost; decision-changing contested evidence.

Do not escalate: routine mechanism choice with evidence; non-property implementation detail; personal preference; “more microservices”.

## 12. Minimum-correction / anti-overengineering

Identify property → mechanism → smallest owner/bound/boundary/contract/evidence change that breaks it → compare to redesign → redesign only if local fix cannot protect the property or creates worse systemic risk.

Default bans as *starting* moves: microservices, async-for-its-own-sake, workers, event-driven, cache, retry, queues, Kubernetes, DDD, Clean Architecture, generic extra layers. Any of these may appear only as the min mechanism for a named property.

Omitted buzzword nodes from Stage 7 (circuit breaker file, strangler, event sourcing, USE/SLO, hedged requests, expand-contract) stay omitted as knowledge; they are not Stage 8 tactics.

## 13. GOOD CASE / false-positive handling

Before defect: load relevant GC. Test mechanism presence, not surface resemblance.

| Suspicious surface | GC to load first |
|---|---|
| daemon with no “lifecycle story” | GC-001 |
| GC language / soft budget | GC-002 |
| prototype without modules | GC-003 |
| long-lived process | GC-004 |
| single-process DB | GC-005 |
| hardware-delegated I/O isolation | GC-006 |
| large coordinated change | GC-007 |
| little ops telemetry + proof | GC-008 |
| compatibility break | GC-009 GC-010 GC-011 |
| no internal zero-trust | GC-012 |
| multi-writer | GC-013 |
| append-only / derived views | GC-014 |
| no service-local shedding | GC-015 |
| implicit-looking ordering | GC-016 |

## 14. Uncertainty handling

UNKNOWN / NEEDS_EVIDENCE / CONTESTED / HYPOTHESIS remain first-class. Gaps stay gaps (RQ5-001, RQ3-006, RQ5-005, RQ2-008, RQ3-004, …). Q-006/Q-052/Q-054: name the next observation; do not average two FPs into a BLOCKER.

## 15. Output-severity model

Shared schema in `decision-playbooks/index.md`. Severity is the verdict table in §6. Rhetoric does not upgrade PERSONAL_PREFERENCE. A blocker without the four-part package is a process defect in the reasoning pass, not a system defect.

## 16. Progressive-disclosure integration with Stage 7

Default load: Router → Constitution → playbook index (DP + overlay) → **one or two** domain indexes → linked MP/FP/T → GC if surface looks like a violation → named RQ → sources only if disputed/high-risk/low-confidence.

Matches Stage 7 budget: not all 10 MPs, not the source corpus. Relationship-map is loaded only when a relation/distinction/gap must be machine-checked. Playbooks reference IDs; they do not restate MP statements.

## 17. Representative reasoning traces

Navigation/reasoning demonstrations, not Stage 10 fixtures. No hidden chain-of-thought.

### 17.1 Retry storm / overload

- **Trigger:** production saturation with retries (DP-005); or as-is review of that path (DP-002 + overload overlay).
- **Questions:** Q-001, Q-004, Q-025, Q-026..Q-029, Q-046.
- **Route:** `overload/` MP-009 FP-010 FP-011 T-006..T-009 T-005 T-015 GC-015; add `resources/` MP-003 FP-003 only if retry *count* is the unbounded dimension.
- **Evidence:** RUNTIME retry/admit/queue; CODE retry policy; CONFIG timeouts.
- **GC:** GC-015 — path-level control is not a defect.
- **Stop:** mechanism attributed (amplifier vs missing admission vs unbounded count); min correction named (bound retry and/or path admission). Not “rewrite event-driven”.
- **Shape:** BLOCKER if uncontrolled retry with material saturation and a required availability/latency property; else HIGH_CONFIDENCE_RISK or NEEDS_EVIDENCE.

### 17.2 Stale async result / ownership vs execution guarantee

- **Trigger:** DP-002 or DP-005; overlay runtime/concurrency.
- **Questions:** Q-011, Q-013, Q-015, Q-016; never skip D-02.
- **Route:** `lifecycle/` MP-001 FP-001 T-002 **and** `concurrency/` MP-010 FP-012; GC-001 GC-016.
- **Evidence:** CODE cancel/ownership; RUNTIME late completion; model docs for provided guarantees.
- **Stop:** attributed to FP-001 or FP-012 (or both as two findings). No third FP.
- **Shape:** BLOCKER only with evidence of the surviving mechanism + impact; GC-016 if the model truly provides the guarantee.

### 17.3 Independent-consumer contract migration

- **Trigger:** DP-003 (delta is the migration).
- **Questions:** Q-003, Q-040, Q-041, Q-042, Q-046.
- **Route:** `integration/` MP-007 FP-008 T-012 GC-009..011. Do not load expand-contract. Distinct from `evolution/` MP-002 unless the issue is hidden variation-axis leak (FP-002).
- **Evidence:** PRODUCT_INTENT + consumer inventory (ARCHITECTURE_INTENT/HISTORY); CODE of published contract.
- **Stop:** governed break → `NO_DEFECT` (GC-009/010); internal-only → GC-011; ungoverned independent break → BLOCKER/MUST_FIX with min correction = governance or compatibility direction.
- **Shape:** as above; AX-002 if the PR shrinks the contract for convenience.

### 17.4 CRDT / local-first multi-writer

- **Trigger:** DP-002 (existing) or DP-001 (proposed).
- **Questions:** Q-018, Q-019, Q-047.
- **Route:** `state-data/` MP-008 T-013 GC-013; D-14.
- **Evidence:** declared merge/conflict semantics (CODE or ADR).
- **GC:** GC-013 — explicit merge is not “missing single writer”.
- **Stop:** `NO_DEFECT` when merge/conflict is explicit. If missing, FP-009 + min correction T-013, not “add a single leader” as universal.

### 17.5 seL4 / proof-scope vs operational evidence

- **Trigger:** DP-002 + observability overlay; add concurrency only if the question is whether a guarantee *exists*.
- **Questions:** Q-037, Q-038, Q-039, Q-051.
- **Route:** `observability/` MP-006 FP-007 T-014 GC-008; D-11.
- **Evidence:** proof/assumption set (ARCHITECTURE_INTENT / GENERIC_KNOWLEDGE of the proved artifact); remaining ops questions.
- **Stop:** questions inside the proof + satisfied assumptions → `NO_DEFECT` for missing service telemetry. Questions outside proof still `NEEDS_EVIDENCE` if attribution matters. Missing OTel is not FP-007.

### 17.6 Good architecture, no defect (OTP supervised daemon)

- **Trigger:** DP-002 + lifecycle overlay on an OTP-supervised long-running process.
- **Questions:** Q-011, Q-012, Q-023.
- **Route:** `lifecycle/` MP-001 T-001 GC-001; do not jump to FP-003 solely from lifetime.
- **Evidence:** supervisor spec (CODE/RUNTIME).
- **GC:** GC-001 — supervision is ownership; indefinite lifetime ≠ ownerlessness. Supervision is not a universal invariant for other runtimes.
- **Stop:** `NO_DEFECT`. Naive flags “unbounded lifetime / no owner” are false positives.

## 18. Mode-overlap / mode-selection rules for Stage 9

Stage 9 may map:

- Design mode → DP-001
- Review mode → DP-002
- PR/change mode → DP-003
- ADR mode → DP-004
- Incident mode → DP-005

Specialized “concurrency review” / “overload review” / etc. should be **the same mode as 002/003/005 plus overlay**, not extra personas. If Stage 9 creates extra modes, they must share this procedure and only change default overlay.

Do not encode this report as a system prompt here.

## 19. Deliberate omissions / Stage 9 boundary

Not created: Agent system prompt; provider wrappers; mode files; eval scenarios/expected findings/scorecards; new ontology types; RS-* ; new MP/FP/T/GC/domain/predicate; source research; expand-contract tactic; circuit-breaker node.

Stage 9 should consume: spine, five DPs, overlay table, question IDs, evidence/verdict/drift/conflict/stop/escalation contracts. It should not duplicate Constitution prose.

## 20. Genuine owner decisions only

None that require a new Chief Architect ontology or product-policy call.

Authorized compressions already in Issue #21 (“smallest set”, “test candidate families”, “may merge/reorder/conditionalize”):

1. Five DPs; four Issue families kept as overlays.
2. Eighteen candidate spine steps reduced to six core + conditional dimensions.

Reopen only if Stage 9 cannot route specialized reviews via overlays.
