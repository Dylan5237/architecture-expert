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

**Pre-routing (not a reasoning stage):** identify task/object → choose DP + optional overlay.

**Six reasoning stages:**

- S1. Intent / Required Properties / Applicable Non-negotiables
- S2. Evidence Baseline (origin + `claim_epistemic_state`)
- S3. Mechanism Hypotheses + Conditional Knowledge Activation
- S4. GOOD CASE / Falsification / Discriminating-Evidence Gate — (1) identify the candidate mechanism; (2) check the relevant GC qualifier(s), not only the title; (3) when mechanisms remain ambiguous, seek the cheapest discriminating evidence; (4) only then adjudicate
- S5. Adjudication + Minimum Correction / Alternatives / ARCH_CONFLICT
- S6. Terminal Outcome / Stop / Escalation

Do not add a seventh stage.

**Conditional dimensions:** ownership, change-decision boundaries, per-work bounds, failure propagation, trust, diagnostic evidence, contracts, state authority, overload path, execution-model honesty. Each maps to one Stage 7 domain. Skip any dimension that cannot change the decision.

**Merged Issue #21 steps:** 1–3 → S1; 4 → S2; 5–13 → S3 conditional dimensions (optional, not ordered); GC/falsification → S4; 14–18 → S5–S6.

**Rationale:** a mandatory 18-step tour would violate progressive disclosure, AX-004, and the “not a checklist” constraint. Pre-routing plus six stages is the smallest sequence that still enforces properties-first, typed evidence, S4 before adjudication, and stop/escalation.

Entry: `00_ROUTER.md` for knowledge need, then `decision-playbooks/index.md` for procedure. Exit: shared output contract when a stop rule fires.

## 2. Playbook inventory and why each is distinct

| ID | Title | Object of reasoning | Procedure |
|---|---|---|---|
| DP-001 | Architecture Design | not-yet-built capability | forward synthesis, min-sufficient |
| DP-002 | Architecture Review | existing system as-is | diagnose vs properties; `terminal_outcome` NO_DEFECT legal |
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

`question-bank/index.md`: **17** sections, **Q-001..Q-055**.

| Section | IDs | Role |
|---|---|---|
| Q-INT Intent / product contract | Q-001..003 | properties, AX-002, consumers |
| Q-EVD Evidence / baseline | Q-004..007 | authority matrix, drift, discriminating observation |
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
| Q-VAL Validation / proof | Q-050..051 | confirming evidence, isolation names |
| Q-UNK Unknowns / escalation | Q-052..055 | stop, escalate, ARCH_CONFLICT |

No technology trivia. No per-playbook duplicated question text.

## 5. Evidence model

Four typed fields. Do not use one unlabeled shared enum.

**Evidence Origin** (unchanged nine): PRODUCT_INTENT, ARCHITECTURE_INTENT, CODE, CONFIG, TEST, RUNTIME, HISTORY, GENERIC_KNOWLEDGE, USER_ASSERTION.

**Claim Epistemic State** (`claim_epistemic_state` only): CONFIRMED, HYPOTHESIS, UNKNOWN, CONTESTED, NEEDS_EVIDENCE.

**Finding Disposition** (`finding_disposition` only): BLOCKER / MUST_FIX, HIGH_CONFIDENCE_RISK, NEEDS_EVIDENCE, NON_BLOCKING_IMPROVEMENT, PERSONAL_PREFERENCE.

**Terminal Outcome** (`terminal_outcome`): NO_DEFECT, MIN_SAFE_FIX_IDENTIFIED, NEEDS_EVIDENCE, OWNER_TRADE_OFF, ARCH_CONFLICT, NO_DECISION_CHANGING_WORK.

`HIGH_CONFIDENCE_RISK`, `NON_BLOCKING_IMPROVEMENT`, and `PERSONAL_PREFERENCE` are finding dispositions, not claim-states. `NO_DEFECT` and `ARCH_CONFLICT` are terminal outcomes, not finding dispositions. `NEEDS_EVIDENCE` may appear as claim-state and as finding/task disposition only because the field name makes the type explicit. Origin never implies confidence; a RUNTIME point can be `HYPOTHESIS`.

## 6. Evidence sufficiency / finding-disposition thresholds

| finding_disposition | Sufficiency |
|---|---|
| BLOCKER / MUST_FIX | Accepted requirement or applicable non-negotiable violated; **evidence + mechanism + failure mode + material impact**; GC does not apply; **`refutation_or_invalidation` required** |
| HIGH_CONFIDENCE_RISK | Strong evidence of material architecture risk; not a proven requirement violation; **`refutation_or_invalidation` required** |
| NEEDS_EVIDENCE | Named next discriminating evidence; stop allowed (all DPs); refutation optional |
| NON_BLOCKING_IMPROVEMENT | Properties already protected; refutation optional |
| PERSONAL_PREFERENCE | Taste; never blocker; never sole escalation; no proof obligation |

Fluent “might be bad” is below BLOCKER threshold. Load-bearing findings without `refutation_or_invalidation` are incomplete.

## 7. Project-fact authority matrix

| Claim type | Evidence/authority rule |
|---|---|
| Current behavior | CODE + CONFIG + RUNTIME + relevant TEST are complementary, not a fixed total order. Surface disagreement and determine which evidence answers which sub-question. |
| Product intent | accepted PRODUCT_INTENT is authoritative for required capability/product contract. |
| Architecture intent/history | accepted ARCHITECTURE_INTENT / HISTORY record intended decisions/history; they do not establish current runtime truth. |
| Generic mechanisms | GENERIC_KNOWLEDGE explains mechanisms/risks; it never establishes or overrides a project-specific fact. |
| User assertion | USER_ASSERTION is unverified unless explicitly accepted/grounded as an authoritative project statement. |

Task-specific emphasis (DP-005 RUNTIME timeline; DP-003 delta CODE/CONFIG/TEST; DP-004 ADR-as-text) is legal and is not a universal ranking.

## 8. KNOWLEDGE_DRIFT

Canonical triggers only:

1. observed/current behavior vs accepted PRODUCT_INTENT;
2. observed/current behavior vs accepted ARCHITECTURE_INTENT / accepted historical decision record (including a stale ADR/doc claiming current behavior);
3. conflicting accepted intent records (product-vs-product, product-vs-architecture, or equivalent accepted project authorities).

Not automatic drift: GENERIC_KNOWLEDGE vs a project fact; bare USER_ASSERTION vs project evidence.

Record competing claims, origins, `claim_epistemic_state`s, next evidence/authority action. Do not silently pick. Drift is not automatically BLOCKER.

## 9. ARCH_CONFLICT

Required fields: capability/required property; conflicting constraint; evidence; fundamental-vs-inconvenience; alternatives; trade-offs; reversibility; authority owner; evidence still needed.

Inconvenience alone is invalid. Silent product-contract shrink is forbidden (AX-002). Q-010, Q-055. `ARCH_CONFLICT` is a `terminal_outcome`, not a `finding_disposition`. Keep the `arch_conflict` record when the pass ends ARCH_CONFLICT.

## 10. Stop conditions

Shared six (index; semantics unchanged): properties protected; defect+min correction clear; owner trade-off among viable options; NEEDS_EVIDENCE with next observation; ARCH_CONFLICT needs authority; further detail would not change the decision.

Mapped `terminal_outcome`: (1) NO_DEFECT, (2) MIN_SAFE_FIX_IDENTIFIED, (3) OWNER_TRADE_OFF, (4) NEEDS_EVIDENCE, (5) ARCH_CONFLICT, (6) NO_DECISION_CHANGING_WORK.

DP-specific additions: DP-001 stops if properties cannot be stated (`terminal_outcome` NEEDS_EVIDENCE) or when a min-sufficient proposal is done (`NO_DECISION_CHANGING_WORK`); DP-002/005 treat `terminal_outcome` NO_DEFECT as success; DP-003 stops at delta-scope even if the rest of the system is imperfect; DP-004 stops when multiple viable options remain (`OWNER_TRADE_OFF`).

A BLOCKER finding may coexist with `terminal_outcome` MIN_SAFE_FIX_IDENTIFIED.

Do not continue to fill unused sections.

## 11. Escalation conditions

Escalate: product capability trade-off; cross-team commitment; AX-003 interpretation; irreversible data/contract migration; security/trust policy; material cost; decision-changing contested evidence.

Do not escalate: routine mechanism choice with evidence; non-property implementation detail; personal preference; “more microservices”.

## 12. Minimum-correction / anti-overengineering

Identify property → mechanism → smallest owner/bound/boundary/contract/evidence change that breaks it → compare to redesign → redesign only if local fix cannot protect the property or creates worse systemic risk.

Default bans as *starting* moves: microservices, async-for-its-own-sake, workers, event-driven, cache, retry, queues, Kubernetes, DDD, Clean Architecture, generic extra layers. Any of these may appear only as the min mechanism for a named property.

Omitted buzzword nodes from Stage 7 (circuit breaker file, strangler, event sourcing, USE/SLO, hedged requests, expand-contract) stay omitted as knowledge; they are not Stage 8 tactics.

## 13. GOOD CASE / false-positive handling

S4 before a material defect/risk finding: identify candidate mechanism → check relevant GC **qualifier(s)** → cheapest discriminating evidence if still ambiguous → only then adjudicate. Test mechanism presence, not surface resemblance.

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

Shared schema in `decision-playbooks/index.md`. `finding_disposition` is §6. `terminal_outcome` is run-level (§10). Rhetoric does not upgrade PERSONAL_PREFERENCE. A blocker without the four-part package plus `refutation_or_invalidation` is a process defect in the reasoning pass, not a system defect.

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
- **Stop:** S4 then S5; mechanism attributed (amplifier vs missing admission vs unbounded count); min correction named (bound retry and/or path admission). Not “rewrite event-driven”. `terminal_outcome` MIN_SAFE_FIX_IDENTIFIED if a material finding has a clear local fix; NO_DEFECT if GC-015 already contains the path.
- **Shape:** `finding_disposition` BLOCKER if uncontrolled retry with material saturation and a required availability/latency property (include `refutation_or_invalidation`); else HIGH_CONFIDENCE_RISK or NEEDS_EVIDENCE.

### 17.2 Stale async result / ownership vs execution guarantee

- **Trigger:** DP-002 or DP-005; overlay runtime/concurrency.
- **Questions:** Q-011, Q-013, Q-015, Q-016; never skip D-02.
- **Route:** `lifecycle/` MP-001 FP-001 T-002 **and** `concurrency/` MP-010 FP-012; GC-001 GC-016.
- **Evidence:** CODE cancel/ownership; RUNTIME late completion; model docs for provided guarantees.
- **Stop:** S4 D-02 gate; attributed to FP-001 or FP-012 (or both as two findings). No third FP.
- **Shape:** BLOCKER finding only with evidence of the surviving mechanism + impact + `refutation_or_invalidation`; `terminal_outcome` NO_DEFECT if GC-016 applies because the model truly provides the assumed guarantee.

### 17.3 Independent-consumer contract migration

- **Trigger:** DP-003 (delta is the migration).
- **Questions:** Q-003, Q-040, Q-041, Q-042, Q-046.
- **Route:** `integration/` MP-007 FP-008 T-012 GC-009..011. Do not load expand-contract. Distinct from `evolution/` MP-002 unless the issue is hidden variation-axis leak (FP-002).
- **Evidence:** PRODUCT_INTENT + consumer inventory (ARCHITECTURE_INTENT/HISTORY); CODE of published contract.
- **Stop:** governed break → `terminal_outcome` NO_DEFECT (GC-009/010); internal-only → GC-011; ungoverned independent break → BLOCKER/MUST_FIX finding + `terminal_outcome` MIN_SAFE_FIX_IDENTIFIED (min correction = governance or compatibility direction).
- **Shape:** as above; AX-002 if the PR shrinks the contract for convenience (`terminal_outcome` ARCH_CONFLICT with record, not a finding severity).

### 17.4 CRDT / local-first multi-writer

- **Trigger:** DP-002 (existing) or DP-001 (proposed).
- **Questions:** Q-018, Q-019, Q-047.
- **Route:** `state-data/` MP-008 T-013 GC-013; D-14.
- **Evidence:** declared merge/conflict semantics (CODE or ADR).
- **GC:** GC-013 — explicit merge is not “missing single writer”.
- **Stop:** `terminal_outcome` NO_DEFECT when merge/conflict is explicit. If missing, FP-009 finding + min correction T-013 (`MIN_SAFE_FIX_IDENTIFIED`), not “add a single leader” as universal.

### 17.5 seL4 / proof-scope vs operational evidence

- **Trigger:** DP-002 + observability overlay; add concurrency only if the question is whether a guarantee *exists*.
- **Questions:** Q-037, Q-038, Q-039, Q-051.
- **Route:** `observability/` MP-006 FP-007 T-014 GC-008; D-11.
- **Evidence:** proof/assumption set (ARCHITECTURE_INTENT / GENERIC_KNOWLEDGE of the proved artifact); remaining ops questions.
- **Stop:** questions inside the proof + satisfied assumptions → `terminal_outcome` NO_DEFECT for missing service telemetry. Questions outside proof still `terminal_outcome` NEEDS_EVIDENCE if attribution matters. Missing OTel is not FP-007.

### 17.6 Good architecture, no defect (OTP supervised daemon)

- **Trigger:** DP-002 + lifecycle overlay on an OTP-supervised long-running process.
- **Questions:** Q-011, Q-012, Q-023.
- **Route:** `lifecycle/` MP-001 T-001 GC-001; do not jump to FP-003 solely from lifetime.
- **Evidence:** supervisor spec (CODE/RUNTIME).
- **GC:** GC-001 — supervision is ownership; indefinite lifetime ≠ ownerlessness. Supervision is not a universal invariant for other runtimes.
- **Stop:** `terminal_outcome` NO_DEFECT. Naive flags “unbounded lifetime / no owner” are false positives.

### 17.7 Desktop/local tool workspace switch with stale background work

Reasoning/navigation demonstration only. Not an eval scenario or expected-findings fixture.

- **Shape:** a desktop/local developer tool starts a background scan/index/import for workspace A; the user switches to workspace B while that work remains in flight; a late completion could update state for the wrong active workspace unless ownership/cancellation or the execution model prevents it.
- **Trigger:** DP-002 + runtime/concurrency overlay (existing tool). Use DP-003 only if the object is a change that introduces the background work.
- **Questions:** Q-011, Q-013, Q-015, Q-016.
- **Route:** `lifecycle/` MP-001 FP-001 T-002 **and** `concurrency/` MP-010 FP-012; D-02 discriminator; GC-016 if the execution model truly provides cancellation/isolation of in-flight work across workspace switch.
- **Evidence:** CODE/CONFIG/RUNTIME/TEST as available (handler ownership, cancel-on-deactivate, which workspace the completion writes). Complementary origins, not a total order. GENERIC_KNOWLEDGE names the FP family; it does not decide this tool’s current behavior.
- **S4:** candidate mechanisms FP-001 (no cancel/cleanup owner for the scan) vs FP-012 (assumed “switch workspace implies cancel” the model does not provide). Check GC-016 qualifier (guarantee actually provided). If still ambiguous, cheapest discriminating evidence is whether deactivate cancels the job (CODE/TEST) or whether late completions still apply to the new active workspace (RUNTIME).
- **Terminal:** NO_DEFECT if ownership+cancel or a model-provided guarantee prevents cross-workspace mutation; MIN_SAFE_FIX_IDENTIFIED if the min correction is bind-completion-to-workspace-id / cancel-on-deactivate; NEEDS_EVIDENCE if that observation is not yet available. Not a third FP. Not an eval expected finding.

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

Stage 9 should consume: pre-routing + six-stage spine with S4 subsequence, five DPs, overlay table, question IDs, typed origin / claim-state / finding-disposition / terminal-outcome fields, authority matrix, narrowed drift, refutation-bearing output contract. It should not duplicate Constitution prose.

## 20. Genuine owner decisions only

None. R8-1..R8-8 implement already-fixed OD8/CA8 decisions at wording/schema level. No new DP, question, ID, or Stage 7 knowledge node.

Prior authorized compressions (unchanged): five DPs with overlays; 18 Issue labels as coverage, not procedure.
