``
id: STAGE8-RECONCILIATION
title: "Stage 8 Reasoning-Model Challenger — Pass B Reconciliation"
stage: 8
pass: B
role: independent-reasoning-model-challenger
challenger: "Codex harness + GLM 5.3"
branch: challenge/stage8-reasoning-model
date: 2026-09-21
issue: 21
fixed_primary: "research/stage8-reasoning-model@af5e431fd8a913590b89f981b4890288d270e560"
fixed_blind_pass_a: "challenge/stage8-reasoning-model@4899120e216ab383a76b49bda8e7eeabd9cc5e1e"
control: "GitHub Issue #21 latest Chief Architect checkpoint; tasks/stage8/CODEX_PASS_B.md@origin/main"
status: COMPLETE
``

# Stage 8 Reasoning-Model Challenger — Pass B Reconciliation

## 0. Scope, method, and gate

Blindness lifted per contract. Read in full at fixed Primary `af5e431`: all five DP files, the playbook index, the 55-question bank, and `STAGE8_REASONING_MODEL.md`, plus Issue #21's Pass B checkpoint (OD8-1..5, CA8-1..10). Primary artifacts and sealed Stage 2-7 files were not modified. Deterministic audits executed: Q-ID uniqueness/sequence, section count, Stage 7 ref resolution (MP/FP/T/GC/RQ/V/D), DP question-copy scan, prompt-language scan (all hits verified as false positives — §11).

**Gate recommendation: PASS_WITH_REMEDIATION.**

The Primary delivers a genuinely conditional reasoning model: six-stage spine with pre-routing (OD8-1), five procedurally distinct DPs with an overlay table (OD8-2), a 55-question dimension-keyed bank with activation rules (OD8-3), GC-before-verdict discipline, six shared stop rules, a well-scoped escalation list, and minimum-correction throughout. Mechanical integrity is flawless: 55 unique sequential Q-IDs, 17 coherent sections, zero bad refs, zero question duplication, zero real Stage 9 smuggling. The defects are bounded and match the CA findings: the epistemic-state axis mixes claim states with finding dispositions (OD8-4/CA8-3), project-fact precedence is stated as a total order instead of a claim-type matrix (CA8-2), KNOWLEDGE_DRIFT over-fires on generic-knowledge disagreement (CA8-1), the output contract lacks a refutation field for load-bearing findings (CA8-5), terminal outcomes and finding dispositions are not explicitly separated (CA8-7), and the report undercounts question sections as 16 (CA8-4). None changes the model's structure; all are wording/schema-level corrections.

---

## 1. V8-01..V8-36 reconciliation matrix

| Check | Status | Exact Primary evidence | Mechanism / risk | Minimal correction |
|---|---|---|---|---|
| V8-01 Spine conditionality | **PASS** | Index spine core 4 "activate only overlays/dimensions that the shape, symptom, or gap justifies"; DP files repeat activation gating | Linear 18-step tour | None |
| V8-02 Spine minimality | **PASS** | 6 core steps + pre-routing (OD8-1 form); conditional dimensions mapped to domains | Padding stations | None |
| V8-03 Spine shape-neutrality | **PARTIAL** | Wording is largely shape-neutral; GC set spans OTP/SQLite/seL4/local-first; but all six report demonstrations and most examples are server/backend-shaped (retry storm, gateway admission, consumer contracts); no desktop/CLI/embedded trace (CA8-9) | Hidden backend default in examples, not logic | R8-6: one non-server demonstration |
| V8-04 Playbook trigger clarity | **PASS** | Per-DP Trigger + Do-Not-Use-When with object-based disambiguation; index "pick the object, not the vocabulary" + incident-then-fix sequencing rule | Ambiguous dual claims | None |
| V8-05 Playbook distinctness | **PASS** | DP-001 forward synthesis; DP-002 as-is diagnosis; DP-003 delta-scoped; DP-004 alternatives/reversibility/authority; DP-005 backward attribution with competing mechanisms — five different procedures | Label-per-file mode explosion | None |
| V8-06 Playbook coverage (per OD8-2) | **PASS** | CA8-8 task table: runtime/concurrency→DP-002/005+overlay(runtime); resource/overload→DP-002/003+Q-RES/Q-OVL; reliability→DP-002+Q-FAL; contract as-is→DP-002+integration; contract migration→DP-003+Q-INTG; evolution→DP-002/003+Q-EVL; trust/agent→DP-002/003+Q-TRS. All seven resolve to DP+overlay with evidence/stop/output intact | Unroutable task | None |
| V8-07 Overlap routing | **PASS** | Index overlap rule (PR-incident → DP-005 then DP-003); each DP's Do-Not-Use-When cross-references | Unclaimed task | None |
| V8-08 No checklist rigidity | **PASS** | "Ask a question only when its Activate matches. Stop when an answer cannot change the decision"; output contract "Fill only activated parts. Empty sections are a smell" | Every-question designs | None |
| V8-09 Evidence-origin separation | **PASS** | Nine origins defined with typical pointers; every DP's Evidence Baseline section names allowed origins | Origin collapsed | None |
| V8-10 Epistemic-state separation | **PARTIAL** | Eight-state list exists and "origin never implies confidence" is enforced; but the list mixes claim states (`CONFIRMED/HYPOTHESIS/UNKNOWN/CONTESTED/NEEDS_EVIDENCE`) with finding dispositions (`HIGH_CONFIDENCE_RISK/NON_BLOCKING_IMPROVEMENT/PERSONAL_PREFERENCE`); report §5 says "same token may appear as verdict and as epistemic state" (OD8-4/CA8-3) | Stage 9 encodes one unlabeled enum; verdict tokens leak into claim states | R8-1: split into typed axes |
| V8-11 Severity separation | **PASS** | Verdict table with "allowed only when" conditions per verdict | Rhetoric severity | None |
| V8-12 Blocker threshold | **PASS** | BLOCKER requires accepted requirement/non-negotiable violated + evidence+mechanism+failure mode+material impact; "might be bad" explicitly below threshold; Q-054 guards | Best-practice blocker | None |
| V8-13 NEEDS_EVIDENCE terminal | **PASS** | Verdict row "stop is allowed"; Q-054 "named next observation, or an invitation to keep speculating"; DP-005 stop "name that observation; do not average two FPs into a BLOCKER" | Unknowns as findings | None |
| V8-14 Project-fact precedence | **PARTIAL** | Three-scope precedence exists (index + report §7) and is directionally right; but "Current behavior: CODE/CONFIG/TEST/RUNTIME > ..." ranks four complementary origins as a chain instead of a claim-type matrix with surfaced disagreement (CA8-2); Q-004 embeds the same chain | Silent ranking of CODE over RUNTIME (or TEST) when they answer different questions | R8-2: replace chains with authority matrix |
| V8-15 KNOWLEDGE_DRIFT | **PARTIAL** | Drift record shape is correct (claims/origins/states/next evidence; never silent pick); but trigger 2 "generic knowledge would require denying a project fact" and trigger 3 "USER_ASSERTION contradicts ..." over-fire (CA8-1): generic-vs-project mismatch is ordinary adjudication; USER_ASSERTION conflict is verification unless the assertion is accepted authority | Drift noise; ordinary applicability mislabeled as project-truth conflict | R8-3: narrow triggers to project-truth surfaces |
| V8-16 ARCH_CONFLICT completeness | **PASS** | Nine required fields incl. fundamental-vs-inconvenience, authority owner, evidence still needed; Q-010/Q-055 gate it; DP-004 step 6 wires AX-002 | Missing authority/reversibility | None |
| V8-17 Product-contract preservation | **PASS** | AX-002 cited in DP-001/003/004; "silent shrink forbidden"; Q-002; DP-003 category mistake lists it | Silent capability drop | None |
| V8-18 Minimum correction | **PASS** | Five-step rule in index; Q-046/Q-049; every review/change/incident DP ends at min-correction; anti-overengineering sections per DP | Default rewrite | None |
| V8-19 No framework bias | **PASS** | Explicit default-ban list; "any of these may appear only as the min mechanism for a named property"; DP-004 rejects "industry default" options | Fashionable substitution | None |
| V8-20 GOOD CASE gate | **PARTIAL** | Behavior substantively correct (GC-before-defect in spine core 5, every DP, report §13 mapping table); but the spine step is labeled "GC then correction" without the explicit falsification/discriminating-evidence subsequence OD8-1/CA8-6 specifies (candidate mechanism → GC qualifier → cheapest discriminating evidence → adjudicate) | Stage 9 may encode GC check as optional decoration | R8-4: restate S4 subsequence |
| V8-21 No false-positive pattern matching | **PASS** | "Test mechanism presence, not surface resemblance"; DP-002/005 category mistakes name keyword matching; Q-012/Q-029/Q-038 guard specific false flags | Pattern-name verdicts | None |
| V8-22 Stop conditions | **PASS** | Six shared rules + DP-specific additions; "Do not continue to fill unused sections/dimensions" in index, report §10, and DP files | Non-terminating analysis | None |
| V8-23 No-defect terminal | **PASS** | `NO_DEFECT` is a verdict with "GC matches, or mechanism absent, or properties protected"; DP-002/005 call it a successful stop; report §17.6 demonstrates it end-to-end | Model cannot say "no defect" | None |
| V8-24 Escalation conditions | **PASS** | Escalate list matches OD8-5 criteria (seven incl. drift-needs-owner); do-not-escalate list (routine mechanism, implementation detail, preference, "more microservices"); DP-004 frames viable-options escalation as success | Over/under-escalation | None |
| V8-25 Uncertainty handling | **PASS** | UNKNOWN/CONTESTED/HYPOTHESIS first-class; Q-052 decision-changing filter; Q-007 prevents assertion promotion; gaps stay gaps (report §14) | Fluent certainty | None |
| V8-26 Validation/proof | **PARTIAL** | Q-048 (what would invalidate the chosen alternative) and Q-050 (confirming evidence) exist; but the shared output contract has no per-finding refutation field, so BLOCKER/HIGH_CONFIDENCE_RISK findings can close without naming what would overturn them (CA8-5) | Unfalsifiable load-bearing findings | R8-5: add `refutation_or_invalidation` field |
| V8-27 Progressive disclosure | **PASS** | Router→Constitution→DP index→1-2 domains→linked nodes→GC→named RQ→sources only if disputed; DP-001 "at most two domain indexes"; report §16 | Corpus loading | None |
| V8-28 Knowledge refs resolve | **PASS** | Deterministic scan of all 8 Stage 8 files: 0 bad MP/FP/T/GC/RQ/V/D refs | Dangling refs | None |
| V8-29 Question IDs stable | **PASS** | Q-001..Q-055, 0 duplicates, 0 gaps, 0 extras; section IDs stable | Renumbering | None |
| V8-30 No technology trivia | **PASS** | All 55 questions mechanism-oriented (property/owner/bound/guarantee/authority/consumer shaped); zero recall/definition items | Interview questions | None |
| V8-31 No duplicated question sets | **PASS** | DPs reference section IDs only; zero `### Q-` headers in DP files; "do not copy question text" enforced | Copy-paste drift | None |
| V8-32 No corpus duplication | **PASS** | DPs route by ID; no MP statement restated; overlay tables carry discriminators, not mechanism prose | Playbook-as-knowledge-article | None |
| V8-33 Cross-shape applicability | **PARTIAL** | Same as V8-03: logic neutral, demonstrations server-only (CA8-9) | Single-shape demos | R8-6 |
| V8-34 No Stage 9 smuggling | **PASS** | Prompt-language scan: all hits are (a) "does **not** write system prompts/mode files" boundary statements, (b) DP-004 Do-Not-Use-When second-person routing sentences ("You are auditing..." = conditional routing, not persona). No persona/provider/runtime instructions (CA8-10) | Prompt files in disguise | None |
| V8-35 No eval leakage | **PASS** | Report §17 traces are navigation/decision demonstrations with routes/questions/stop/shape; no expected-findings scorecards, no hidden chain-of-thought | Eval fixtures | None |
| V8-36 Worktree/branch integrity | **PASS** | Dedicated worktree `.codex-s8`; branch descends from Pass A; diff adds only this report; shared checkout untouched | Cross-agent contamination | None |

**V8 totals: 31 PASS, 5 PARTIAL, 0 FAIL, 0 CHECK_INVALID.** The five PARTIALs decompose into six bounded remediations (R8-1..R8-6; V8-03/V8-33 share R8-6).

---

## 2. Final spine reconciliation (OD8-1)

Adopted form matches OD8-1 exactly: pre-routing (task/object → DP + optional overlay) then six stages — intent/properties/non-negotiables; evidence baseline; conditional mechanism pass; GC/falsification gate; adjudication + min-correction/alternatives/ARCH_CONFLICT; terminal outcome. The 18 Issue labels are correctly a coverage map. The Primary's implementation adds value beyond the minimum: the conditional-dimension table (activate-when + default domain per dimension) and the DP-005 competing-mechanisms requirement (never one favorite; never average two FPs into a BLOCKER) are exactly the anti-rigidity and anti-premature-verdict discipline Pass A demanded.

Verdict: **ADOPTED**; one wording remediation (R8-4) inside S4 per CA8-6. No seventh stage needed — the Primary's close (step 6) already separates stop/escalate/verdict from adjudication without a separate terminal-label operation, and OD8-1 forbids padding stages.

---

## 3. DP disposition / coverage matrix (OD8-2, CA8-8)

| DP | Trigger object | Distinct procedure element | Verdict |
|---|---|---|---|
| DP-001 | not-yet-built capability | forward synthesis; stops at proposal/owner-trade-off/ARCH_CONFLICT; NO_DEFECT not used (correct — nothing to clear) | **KEEP** |
| DP-002 | existing system as-is | diagnose vs properties; NO_DEFECT legal; one-domain-unless-discriminator rule | **KEEP** |
| DP-003 | a delta | delta-scoped evidence; out-of-scope carry-over rule; min-correction expressible as change to the PR | **KEEP** |
| DP-004 | decision artifact | alternatives-not-straw-men test; reversibility; escalation-as-success framing | **KEEP** |
| DP-005 | observed failure | RUNTIME-first timeline; competing mechanisms; symptom-family route table with D-discriminators | **KEEP** |

### Overlay coverage (CA8-8 task table, routed against the actual index/DP files)

| Task | Route | Evidence/stop/output preserved? | Result |
|---|---|---|---|
| runtime/concurrency review, no incident | DP-002 + overlay runtime/stale-async (Q-OWN+Q-XCN, D-02 dual route) | yes — DP-002 procedure unchanged | **CLEAN** |
| resource/overload capacity review, no incident | DP-002 + Q-RES (D-04 discriminator Q-025) | yes | **CLEAN** |
| reliability/failure-containment review, no incident | DP-002 + Q-FAL (RQ5-001 kept as gap) | yes | **CLEAN** |
| contract/integration as-is review | DP-002 + integration overlay (Q-INTG, GC-009..011) | yes | **CLEAN** |
| contract migration/change review | DP-003 + Q-INTG (T-012, GC-011 internal-vs-independent) | yes | **CLEAN** |
| evolution/boundary review | DP-002/DP-003 + Q-EVL (GC-003/GC-007, P-006 signal) | yes | **CLEAN** |
| trust/agent-action review | DP-002/DP-003 + Q-TRS (GC-012 carve-out, RQ2-008/RQ3-004 gaps) | yes | **CLEAN** |

All seven CA8-8 tasks route to DP + overlay with procedure, evidence expectations, stop conditions, and output semantics intact. **Five DPs KEEP**; no reopen condition fires (no task required changing trigger/evidence/stop/output procedure).

---

## 4. Question-bank integrity / taxonomy audit (OD8-3, CA8-4)

| Check | Result |
|---|---|
| Item IDs | Q-001..Q-055: **55 unique, sequential, no gaps, no extras, no duplicates** |
| Sections | **17**: Q-INT, Q-EVD, Q-PRP, Q-OWN, Q-XCN, Q-STA, Q-FLW, Q-RES, Q-OVL, Q-FAL, Q-TRS, Q-OBS, Q-INTG, Q-EVL, Q-ALT, Q-VAL, Q-UNK |
| Report claim | §4 says "16 sections" — **counting error** (the Q-VAL/Q-UNK row lists two sections as one line; 17 actual). Bank itself coherent; no duplicate content found (CA8-4 confirmed as inventory-only) |
| Activation conditions | Every question has an Activate line keyed to mechanism/shape/uncertainty, not sequence |
| Mechanism orientation | 55/55 property-owner-bound-guarantee-authority-consumer shaped; zero trivia |
| Playbook copies | Zero `### Q-` headers in DP files; DPs reference section IDs |
| Coverage | Every Stage 7 domain has at least one question section routing into it; every GC has at least one guard question (Q-012 GC-001/004, Q-020 GC-014, Q-029 GC-015, Q-035 GC-012, Q-039 GC-008, Q-041/042 GC-009..011, Q-044 GC-007) |
| Standouts | Q-006 (single discriminating observation preferred over BLOCKER), Q-013 (D-02 without third FP), Q-019 (refuse unqualified consistency), Q-025 (D-04 bound-vs-policy), Q-054 (NEEDS_EVIDENCE vs speculation) — precisely the conditional discipline required |

Verdict: **KEEP intact**; correct the report count 16→17 (R8-7, folded into the report-wording remediation set).

---

## 5. Evidence / drift / verdict model reconciliation (OD8-4, CA8-1/2/3)

### 5.1 Three-axis correction (R8-1)

Primary's single eight-token list must split into typed axes per OD8-4:

- **Evidence Origin** (unchanged, nine values) — correct as-is.
- **Claim Epistemic State**: `CONFIRMED / HYPOTHESIS / UNKNOWN / CONTESTED / NEEDS_EVIDENCE` (five).
- **Finding / Decision Disposition**: `BLOCKER / MUST_FIX / HIGH_CONFIDENCE_RISK / NEEDS_EVIDENCE / NON_BLOCKING_IMPROVEMENT / PERSONAL_PREFERENCE / NO_DEFECT / ARCH_CONFLICT` (eight).

`NEEDS_EVIDENCE` appears on both axes **typed** (claim-state vs task/finding disposition). `HIGH_CONFIDENCE_RISK / NON_BLOCKING_IMPROVEMENT / PERSONAL_PREFERENCE` move out of the claim-state list. Minimal edit sites: index "Epistemic state" block, report §5 (and the "same token" sentence, which becomes the typed-dual-use rule), DP output-contract wording where `epistemic_state` is named (the field stays; its enum shrinks), Q-004's precedence line (R8-2 overlap).

### 5.2 Project-fact authority matrix (R8-2, replacing the total-order chains)

| Claim type | Authoritative origins | Conflict handling |
|---|---|---|
| Current behavior | CODE + CONFIG + RUNTIME + relevant TEST — **complementary, not ranked** | Surface disagreement (which origin answers which sub-question); do not silently rank |
| Product intent | accepted PRODUCT_INTENT | authoritative for required capability; conflict with observed behavior → KNOWLEDGE_DRIFT |
| Architecture intent/history | accepted ARCHITECTURE_INTENT + HISTORY | establishes recorded intent, never current runtime truth; drift on mismatch |
| Project-specific fact (any) | GENERIC_KNOWLEDGE **never** establishes it | explains mechanisms/risks only |
| Unverified statement | USER_ASSERTION | classify/verify; drift only if the assertion is itself accepted authority |

Edit sites: index "Project-fact precedence" block; Q-004 Activate line; report §7.

### 5.3 KNOWLEDGE_DRIFT narrowing (R8-3, per CA8-1)

Replace the three current triggers with project-truth-surface triggers:

1. observed/current behavior vs accepted product intent;
2. observed behavior vs accepted architecture intent/history (incl. stale ADR/doc claiming behavior inconsistent with current evidence);
3. conflicting accepted intent records (product vs product, product vs architecture).

Remove: "generic knowledge would require denying a project fact" (generic-vs-project mismatch is ordinary applicability adjudication under S3-S5) and the bare "USER_ASSERTION contradicts" trigger (verification issue unless the assertion is accepted authority). Drift record shape (claims/origins/states/next evidence; never silent pick; not auto-BLOCKER) is correct and stays.

---

## 6. Stop vs terminal-outcome, escalation, GC gate, minimum correction (CA8-5/6/7)

**Terminal vs disposition (R8-8, per CA8-7):** the shared output contract should add a typed `terminal_outcome` field alongside `findings`: terminal reasons = `NO_DEFECT / MIN_SAFE_FIX_IDENTIFIED / NEEDS_EVIDENCE_OWNER_INPUT / OWNER_TRADE_OFF / ARCH_CONFLICT / NO_DECISION_CHANGING_WORK`; finding dispositions stay in the verdict table. `OWNER_TRADE_OFF` and `NO_DEFECT` are terminal reasons; `BLOCKER` etc. are finding dispositions; a finding can coexist with any terminal reason.

**Refutation field (R8-5, per CA8-5):** add to the shared output contract, required for `BLOCKER/MUST_FIX` and `HIGH_CONFIDENCE_RISK` findings: `refutation_or_invalidation: <evidence/condition that would overturn or downgrade this finding>`. Explicitly optional for `NON_BLOCKING_IMPROVEMENT / PERSONAL_PREFERENCE` (no proof obligation on taste).

**GC gate subsequence (R8-4, per CA8-6):** restate spine core 5 as: before a material defect/risk verdict — (1) identify candidate mechanism; (2) check relevant GC qualifier(s); (3) seek the cheapest discriminating evidence when mechanism remains ambiguous; (4) only then adjudicate. Current behavior already does this; the restatement prevents Stage 9 from reading "GC then correction" as optional decoration.

**Stop/escalation/minimum-correction:** verified clean (V8-22/23/24/18). The six stop rules, per-DP additions, escalation authority criteria with both-direction guards, and the five-step minimum-correction rule with Q-046/Q-049 need no change.

---

## 7. Mechanical audit summary

| Check | Result |
|---|---|
| Q-IDs | 55/55 unique sequential |
| Sections | 17 (report miscount 16 → R8-7) |
| Stage 7 refs (MP/FP/T/GC/RQ/V/D) across all 8 Stage 8 files | **0 unresolvable** |
| DP question copies | 0 |
| Prompt language | 0 real occurrences (4 file hits all verified false-positive: prohibition sentences + conditional routing prose) |
| Sealed artifacts touched by Primary | none (checkpoint-verified; re-verified: Primary diff adds only the 8 Stage 8 files) |
| Pass A descent / diff scope | this branch = Pass A + this report only |

---

## 8. Bounded Primary remediation set

| # | Remediation | Files | Nature |
|---|---|---|---|
| R8-1 | Split epistemic axis into typed Claim Epistemic State (5) + Finding Disposition (8); update "same token" sentence to typed-dual-use rule | index, report §5, DP output wording | schema wording |
| R8-2 | Replace precedence chains with claim-type authority matrix (§5.2) | index, Q-004, report §7 | wording |
| R8-3 | Narrow KNOWLEDGE_DRIFT to three project-truth-surface triggers; drop generic-knowledge and bare USER_ASSERTION triggers | index, report §8 | wording |
| R8-4 | Restate S4 subsequence (mechanism → GC qualifier → cheapest discriminating evidence → adjudicate) | index spine core 5, report §1/§13 | wording |
| R8-5 | Add `refutation_or_invalidation` field to shared output contract; required for BLOCKER/HIGH_CONFIDENCE_RISK only | index output contract, report §6/§15 | schema field |
| R8-6 | Add one non-server retrieval/reasoning demonstration (desktop/local tool/embedded; e.g. desktop app stale-async D-02 trace or embedded bounded-execution trace) | report §17 | one demo |
| R8-7 | Correct section count 16→17 | report §4 | count fix |
| R8-8 | Add typed `terminal_outcome` field distinct from finding dispositions | index output contract, report §10 | schema field |

All eight are wording/schema-level except R8-6 (one added demonstration). No structural change, no new DP/question/ID, no knowledge change. Executor: Primary, one commit, before Stage 8 gate closure.

---

## 9. CA8-1..CA8-10 explicit findings

| CA | Result | Action |
|---|---|---|
| CA8-1 KNOWLEDGE_DRIFT too broad | **CONFIRMED** (triggers 2-3 over-fire) | R8-3 |
| CA8-2 precedence too coarse | **CONFIRMED** (total-order chain; Q-004 embeds it) | R8-2 |
| CA8-3 axis mixing | **CONFIRMED** (report §5 "same token" sentence) | R8-1 |
| CA8-4 section count | **CONFIRMED** (17 actual vs 16 claimed; bank coherent, no duplicate) | R8-7 |
| CA8-5 refutation under-specified | **CONFIRMED** (no per-finding field; Q-048 is alternative-level only) | R8-5 |
| CA8-6 GC gate explicitness | **CONFIRMED as wording gap** (behavior correct, subsequence implicit) | R8-4 |
| CA8-7 terminal vs disposition | **CONFIRMED** (`OWNER_TRADE_OFF` used as stop reason while verdict table holds dispositions; not typed in output contract) | R8-8 |
| CA8-8 DP coverage | **ADDRESSED** (all 7 tasks route cleanly; five DPs KEEP) | none |
| CA8-9 cross-shape | **CONFIRMED as demo gap** (logic neutral, demonstrations server-only) | R8-6 |
| CA8-10 Stage 9 boundary | **CLEAN** (mapping note only; no persona/prompt/runtime instructions; scan hits are prohibitions/routing prose) | none |

---

## 10. OD8-1..OD8-5 evaluation

| OD | Evaluation |
|---|---|
| OD8-1 spine | **APPLIED** — six stages + pre-routing; 18 labels as coverage map; S4 wording gap → R8-4 |
| OD8-2 playbook set | **APPLIED** — five DPs; overlays carry the four merged families; coverage proven (§3) |
| OD8-3 question bank | **APPLIED** — dimension-keyed, activation conditions, stable Q-001..055, no local copies |
| OD8-4 three axes | **APPLIED as correction** — Primary predates the decision; remediation R8-1 implements it |
| OD8-5 escalation | **APPLIED** — authority criteria (not closed vocabulary); both-direction guards present |

---

## 11. Stage 9 handoff implications

Stage 9 receives: a six-stage spine with explicit S4 subsequence (post-R8-4), five DPs + overlay table as the mode-overlap contract, 55 stable question IDs with activation rules, typed three-axis evidence model (post-R8-1), authority matrix (post-R8-2), narrowed drift triggers (post-R8-3), refutation-bearing output contract (post-R8-5/R8-8), and six stop rules. Stage 9 must: map modes to DP+overlay without creating persona-per-label modes (the index says this explicitly); keep the output schema fields typed exactly (claim-state ≠ disposition ≠ terminal); not duplicate Constitution prose into prompts; and leave GC routing in. The "You are..." routing sentences in DP Do-Not-Use-When sections are conditional disambiguation, not prompt voice — Stage 9 should convert them to mode-selection logic, not copy them as persona lines.

---

## 12. Genuine new owner decisions

**None.** All eight remediations implement already-fixed decisions (OD8-1/2/4/5) or CA findings (CA8-1..CA8-9) at wording/schema level. The one judgment call — whether R8-6's non-server demonstration should be desktop or embedded — is an executor choice, not an owner decision. No new evidence, DP, question, ID, predicate, or semantic change is requested.
