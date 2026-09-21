``
id: STAGE9-RECONCILIATION
title: "Stage 9 Agent-Contract Challenger — Pass B Reconciliation"
stage: 9
pass: B
role: independent-agent-contract-challenger
challenger: "Codex harness + GLM 5.3"
branch: challenge/stage9-agent-v0.1
date: 2026-09-21
issue: 24
fixed_primary: "research/stage9-agent-v0.1@9b4bc0cc0aa21a9ebd38409a3d898f8d2ed764ae"
fixed_blind_pass_a: "challenge/stage9-agent-v0.1@d99c8e2bfd6b1079303964f8f5dcdfe9f8b59807"
control: "GitHub Issue #24 latest Chief Architect checkpoint; tasks/stage9/CODEX_PASS_B.md@origin/main"
status: COMPLETE
``

# Stage 9 Agent-Contract Challenger — Pass B Reconciliation

## 0. Scope, method, and gate

Blindness lifted per contract. Read in full at fixed Primary `9b4bc0c`: the 158-line system prompt, mode index, all six mode files, `agent/README.md`, and `STAGE9_AGENT_V0_1.md`, plus Issue #24's Pass B checkpoint (OD9-1..5, CA9-1..9). Primary artifacts and sealed Stage 2-8 files were not modified. Deterministic audits executed: Q-body duplication scan, MP/DP-body duplication check, provider-term scan, mode-file line counts, primary diff audit (10 authorized files only).

**Gate recommendation: PASS_WITH_REMEDIATION.**

The Primary is an unusually faithful compilation: all fourteen behavioral blocks present in `157 content lines with zero knowledge duplication (no Q-body, no MP statements, no FP/T/GC prose); typed four-axis schema carried exactly (claim-state five-token set with the not-claim-states exclusion note; finding dispositions excluding NO_DEFECT/ARCH_CONFLICT; terminal run-level with coexistence rule); S4 four-step subsequence verbatim; drift narrowed to the three project-truth triggers with both not-drift clarifications; authority as claim-type matrix; closed expansion conditions; six modes mapping 1:1 with genuinely thin files; AUTO as router-only with one-clarification rule; provider-term scan clean (the single "tool-call" hit is the prohibition sentence itself); v0.1 UNEVALUATED in prompt/README/report frontmatter. Three bounded remediations remain: AUTO route transparency is absent from compiled output behavior (CA9-2/OD9-4 — the strongest finding); overlay default-zero is implicit rather than fail-closed (CA9-3); §11 buzzword wording over-restricts legitimate minimum corrections relative to sealed Stage 8 (CA9-4). All are wording-level; none redesigns the Agent.

---

## 1. V9-01..V9-32 reconciliation matrix

| Check | Status | Exact Primary evidence | Mechanism / risk | Minimal correction |
|---|---|---|---|---|
| V9-01 Prompt compactness | **PASS** | 158 lines, 14 sections, behavioral only (OD9-1 semantic test met) | Encyclopedia drift | None |
| V9-02 No knowledge duplication | **PASS** | Zero Q-body matches; no MP statements, FP/T/GC bodies, source prose; navigation by path+condition throughout | Corpus copy | None |
| V9-03 Role/non-goals | **PASS** | §1 nine-behavior role + four non-goals; §2 three non-goal classes | Scope creep | None |
| V9-04 Routing contract | **PARTIAL** | §3 exact-one-DP table + object-not-vocabulary rule + one-clarification; but AUTO output does not state selection/basis (CA9-2) | Silent routing uncorrectable by user | R9-1: routing transparency field |
| V9-05 Five-mode mapping | **PASS** | Index + five files map 1:1 to DP-001..005; no sixth mode | Mode explosion | None |
| V9-06 Overlay boundary | **PARTIAL** | §3 "only justified overlays" + locks (not personas, no threshold/stop/escalation/typing changes); but default-zero is not stated fail-closed (CA9-3) | "For completeness" activation | R9-2: explicit zero-default + non-reason |
| V9-07 Mode thinness | **PASS** | All five at 34 lines: mapping/trigger/overlay/context-load/stop-nuance/handoff only; no DP body copy (CA9-5: count not a gate) | Mode = DP duplicate | None |
| V9-08 AUTO = router only | **PASS** | AUTO.md: "Router only. Not a sixth reasoning procedure"; five-step routing; delegates after selection; no findings of its own | AUTO as procedure | None |
| V9-09 Object-based routing | **PASS** | §3 table by object; incident-then-fix sequencing rule preserved in prompt + AUTO handoff + report trace | Keyword routing | None |
| V9-10 Spine fidelity | **PASS** | §4 S1..S6 with S4 four-step subsequence (mechanism→GC qualifier→discriminating evidence→adjudicate); "do not add a seventh stage" | S4 diluted | None |
| V9-11 Navigation contract | **PASS** | §5 ten-step order + negative-space list + closed expansion (four conditions); project evidence before GENERIC_KNOWLEDGE | Default corpus loading | None |
| V9-12 Project-fact authority | **PASS** | §6 claim-type matrix: complementary current-behavior origins with surfaced disagreement; PRODUCT_INTENT/ARCHITECTURE_INTENT scoped; GENERIC_KNOWLEDGE lockout; USER_ASSERTION rule; task-emphasis-not-total-order note | Total-order regression | None |
| V9-13 Typed axes | **PASS** | §7 exact vocabularies with exclusion annotations ("Not claim-states: HCR/NBI/PP"; "Not finding dispositions: NO_DEFECT/ARCH_CONFLICT"); typed-dual-use NEEDS_EVIDENCE rule | Axis collapse | None |
| V9-14 Terminal vs disposition | **PASS** | §7 terminal run-level; §8 BLOCKER+MIN_SAFE_FIX coexistence; ARCH_DESIGN mode "Do not use NO_DEFECT as finding disposition" | Severity misclassification | None |
| V9-15 Blocker threshold | **PASS** | §8 six-part package; "not best practice"/unpopularity/"might be bad" excluded; PREFERENCE never blocker/sole escalation | Rhetoric blocker | None |
| V9-16 Refutation rule | **PASS** | §8 BLOCKER/HCR require `refutation_or_invalidation`; README restates | Missing field | None |
| V9-17 GC gate | **PASS** | §4 S4 qualifier-level check; §13 lexical discipline; mode files route GC rows on suspicion | Title-level GC | None |
| V9-18 No pattern-name verdicts | **PASS** | §8/§11 mechanism-first; DP category mistakes carried via compilation | "No circuit breaker" finding | None |
| V9-19 Drift scope | **PASS** | §9 three triggers + two not-drift clarifications (generic mismatch; bare USER_ASSERTION) | Broad drift | None |
| V9-20 ARCH_CONFLICT scope | **PASS** | §10 nine fields; inconvenience invalid; AX-002; terminal classification | Convenience escalation | None |
| V9-21 Minimum correction | **PARTIAL** | §11 five-step rule + default-ban list correct; but final sentence ties omitted-buzzword techniques to "the retrieved tactic ID is the min correction", which Stage 8 does not require (CA9-4) | Legitimate concrete technique (e.g. circuit breaker as exact min mechanism) forbidden when no T-* node exists | R9-3: wording correction |
| V9-22 Framework neutrality | **PASS** | §11 ban-as-default + only-as-min-mechanism-for-named-property | Prescribed style | None |
| V9-23 Stop conditions | **PASS** | §12 six rules referenced to Stage 8 home; anti-continuation | Non-termination | None |
| V9-24 Escalation criteria | **PASS** | §12 seven authority criteria + do-not-escalate list | Over/under-escalation | None |
| V9-25 Output contract | **PASS** | §13 Stage 8 fields by reference + explicit show-list (evidence/mechanism/finding/correction/uncertainty/terminal/authority); fill-only-activated | Missing fields | None |
| V9-26 No hidden CoT | **PASS** | §13 "concise decision rationale, not hidden chain-of-thought" (CA9-8: user-visible rationale required; private deliberation not exposed) | CoT request | None |
| V9-27 Provider independence | **PASS** | Term scan: prompt's single "tool-call" hit is the prohibition sentence; report's hits are the audit statements; no syntax/names/wrappers anywhere | Provider capture | None |
| V9-28 No eval leakage | **PASS** | §2 non-evaluator clause; §14 no-tuning clause; report §16 traces are routing/context only, explicitly "not expected findings"; §17 omissions | Leaked answers | None |
| V9-29 Unevaluated label | **PASS** | Frontmatter `status: UNEVALUATED` on prompt/README/report + §14 + README bold statement | Validated claims | None |
| V9-30 File/ref integrity | **PASS** | All paths referenced by prompt/modes exist in the Primary tree; DP/Q/GC/MP references resolve; mode index matches the six files | Dangling refs | None |
| V9-31 No sealed modification | **PASS** | Primary diff = exactly the 10 authorized agent/report files; Stage 2-8 untouched | Semantic drift via edit | None |
| V9-32 Worktree/branch integrity | **PASS** | Dedicated worktree; descends from Pass A; diff adds only this report; shared checkout untouched | Contamination | None |

**V9 totals: 29 PASS, 3 PARTIAL, 0 FAIL, 0 CHECK_INVALID.** The three PARTIALs map to exactly three remediations (R9-1/R9-2/R9-3), all CA findings.

---

## 2. System-prompt contract verdict

**KEEP with three wording-level corrections.** Block-by-block against sealed Stage 8: §1 role ✓; §2 non-goals ✓; §3 routing (transparency gap → R9-1; overlay default → R9-2); §4 spine with S4 subsequence ✓ (verbatim four steps); §5 navigation with negative space ✓; §6 authority matrix ✓ (best single block in the prompt — the "task-specific emphasis is legal... not a universal total order" note preemptively kills the CA8-2 regression); §7 typed axes ✓ (exclusion annotations are exactly the OD8-4 discipline); §8 findings ✓; §9 drift ✓ (three triggers + two clarifications); §10 ARCH_CONFLICT ✓; §11 min correction (buzzword wording → R9-3); §12 stop/escalation ✓; §13 output + lexical discipline ✓; §14 status ✓. The prompt compiles Stage 8 semantics without restating them — the traceability table in report §3 confirms section-by-section lineage.

## 3. Compactness / duplication audit

| Check | Result |
|---|---|
| Prompt length | 158 lines (OD9-1: diagnostic only; semantically behavioral) |
| Q-001..055 bodies in prompt | **0 matches** |
| MP statements / FP-T-GC bodies / source prose | absent; navigation by path+condition only |
| Mode files | 5 × 34 lines; trigger/mapping/overlay/context/nuance/handoff shape; zero DP-procedure duplication (CA9-5: KEEP) |
| Stage report prose in prompt/modes | none |
| Question references | section IDs only (Q-INT, Q-OWN...) as activation keys — the correct form |

## 4. Mode mapping + thinness matrix

| Mode | DP | Thin content | DP-body copy | Verdict |
|---|---|---|---|---|
| AUTO | none (selects one) | routing 5 steps + context + handoff | none — contains no reasoning steps | **KEEP** |
| ARCH_DESIGN | DP-001 | trigger/overlay(rare)/load incl. GC-003 example/stop nuance (proposal not defects; NO_DEFECT ban)/handoff | none | **KEEP** |
| ARCH_REVIEW | DP-002 | overlay rule + D-02 lock/load/NO_DEFECT success + refutation/handoff | none | **KEEP** |
| CHANGE_REVIEW | DP-003 | delta-scoped overlay/load with Q-INTG/Q-EVL conditions/delta findings + drift nuance (commit-msg vs code = verification not drift)/handoff | none | **KEEP** |
| ADR_REVIEW | DP-004 | options-scoped overlay/ADR-as-text-not-behavior rule/OWNER_TRADE_OFF success + ARCH_CONFLICT not "pragmatic"/handoff | none | **KEEP** |
| INCIDENT_ANALYSIS | DP-005 | symptom→domain table reference/competing mechanisms/RUNTIME emphasis not rank/two-FP NEEDS_EVIDENCE rule/handoff | none | **KEEP** |

The mode files add real compilation value beyond pointing: each carries exactly the mode-specific nuance that would otherwise be lost (delta-vs-carryover, ADR-text-epistemics, incident competing-mechanics), which is what "thin" should mean.

## 5. AUTO routing / transparency audit (CA9-2)

Routing correctness: object-based selection, exact-one-DP, one-clarification rule, delegation after selection, mid-pass object-change re-route-once — all present and correct. **Gap (R9-1)**: neither the prompt's §13 output behavior nor `AUTO.md` requires the user-visible result to state selected mode/DP, overlays (including none), and a one-line routing basis. OD9-4 makes this mandatory. Minimal fix: add one output line — `route: {mode, dp, overlays, basis}` — required for AUTO passes; explicit modes may state mode/DP without a basis (no AUTO decision occurred). This is user-correctability, not CoT (CA9-8 boundary respected: the basis is the routing decision's grounds, not private deliberation).

## 6. Overlay-boundary audit (CA9-3)

Locks are intact everywhere: prompt §3, mode index, every mode file ("tune question sections and first domain only... must not change finding thresholds, stop rules, escalation, product-contract protection, or evidence typing"). **Gap (R9-2)**: "only justified overlays" implies zero-default but does not state it fail-closed. Minimal fix, one sentence in prompt §3: "AUTO/modes start with **zero overlays**; activate only when task shape/symptom/evidence names the mechanism family; 'for completeness' is never an activation reason."

## 7. Context-loading / negative-space audit (CA9-6)

Ten-step order ✓; negative-space list (never default-load all MPs/FPs/Ts/GCs/55Q/sources/Stage reports) ✓ in prompt §5 and README; four expansion conditions closed ✓ (no mode/README wording opens "for completeness" expansion — the only adjacent phrase is the overlay justification, addressed by R9-2); Stage reports as audit/provenance ✓; relationship-map only-when-machine-check ✓; project evidence before GENERIC_KNOWLEDGE ✓. **PASS** post-R9-2 (the overlay default and expansion conditions share the fail-closed wording pattern).

## 8. Project-fact authority audit

Prompt §6 carries the full claim-type matrix; README "what to attach" section teaches the origin classification to the operator; mode files add task-emphasis without total-order regression (CHANGE_REVIEW "not a universal origin ranking"; INCIDENT_ANALYSIS "RUNTIME is usual first *emphasis*... not a global origin rank"). GENERIC_KNOWLEDGE lockout stated three times (prompt/README/authority row). **PASS.**

## 9. Typed-axis audit

Four vocabularies exact; the exclusion annotations in §7 ("Not claim-states: ...", "Not finding dispositions: ...") are the OD8-4 discipline compiled into the prompt itself — stronger than Pass A demanded. `NEEDS_EVIDENCE` dual-use typed by field name. ARCH_DESIGN's "Do not use NO_DEFECT as a finding disposition" is the terminal/disposition boundary enforced at mode level. README "how to read the close" teaches the distinction to users. **PASS.**

## 10. Finding / GC / refutation audit

S4 subsequence verbatim (four steps, qualifier-level); §8 six-part blocker incl. GC-not-applicable + refutation; HCR refutation; README restates refutation requirement; ARCH_REVIEW mode restates refutation on BLOCKER/HCR. Lexical discipline block (§13) carries the high-risk gates. **PASS.**

## 11. Drift / ARCH_CONFLICT audit

Three project-truth triggers + two not-drift clarifications, compiled exactly from the R8-3-narrowed Stage 8; CHANGE_REVIEW adds the delta nuance (commit-message-vs-code is verification, not automatic drift; accepted-intent-vs-delta is drift) and ADR_REVIEW the stale-ADR trigger-2 example — both consistent applications, not new rules. ARCH_CONFLICT nine fields + inconvenience-invalid + AX-002 in §10. **PASS.**

## 12. Minimum-correction / framework-neutrality audit (CA9-4)

Five-step rule ✓; default-ban list ✓ ("appears only as the minimum mechanism for a named property") ✓. **Gap (R9-3)**: the final §11 sentence — "Stage 7 omitted buzzword nodes (...) stay omitted **unless the retrieved tactic ID is the min correction**" — is narrower than sealed Stage 8 (report §12: such techniques are allowed "when their exact mechanism is the minimum correction **and they are not already covered by an existing T-***"). Stage 7 omission governs canonical knowledge promotion, not runtime naming: an Agent forbidden from naming circuit-breaker as the min mechanism (when no T-* covers it) would under-correct — the over-restriction CA9-4 flags. Minimal fix, one sentence: "Stage 7 omission means: do not promote these into canonical nodes or recommend them as best practice; a concrete technique may still be **named** as the minimum correction when its exact mechanism fits and no existing T-* already covers it (do not mint new IDs at runtime)."

## 13. Stop / escalation audit

Six stop rules by reference + anti-continuation ("Do not continue to fill unused sections") ✓; seven escalation criteria with both-direction guards ✓; mode-level stops add the DP-specific mappings (ARCH_DESIGN NEEDS_EVIDENCE-when-properties-unstated; ARCH_REVIEW NO_DEFECT-success; CHANGE_REVIEW delta-scope; ADR_REVIEW OWNER_TRADE_OFF-success; INCIDENT_ANALYSIS attributed-then-stop). **PASS.**

## 14. Output-contract audit (CA9-7)

§13 references the Stage 8 shared schema by name + encodes the show-list (evidence with origin+claim-state, mechanism, finding/decision, correction/alternatives, uncertainty, terminal, authority) + fill-only-activated + lexical discipline. CA9-7's field inventory is surfaceable: playbook/mode/overlay (post-R9-1 explicitly), intent/properties (S1 → output), evidence+claim-state ✓, drift ✓, GC ✓, findings+refutation ✓, conflict record ✓, terminal ✓, stop ✓, escalation ✓. Compact reference + explicit fields preserves behavior without bloat — exactly the CA9-7 standard. **PASS post-R9-1.**

## 15. Provider-independence audit

Deterministic scan: the only regex hits for provider/vendor/tool terms are prohibition/audit sentences themselves ("No provider-specific APIs, **tool-call** schemas, or vendor wrappers"; report §14 "No vendor chat completions, function/tool schemas..."). Zero syntax, names, wrappers, harness flags. README hosting section: "Any host that can supply this system prompt, the selected mode file, and repository file access." **PASS.**

## 16. Stage 10 boundary / unevaluated audit (CA9-9)

§2 non-evaluator + §14 no-tuning; report §16 traces explicitly "not expected findings"; §17 deliberate omissions; `status: UNEVALUATED` in three frontmatters + README bold + report header. No benchmark labels, no scorecard logic, no expected-finding vocabulary anywhere. **PASS.**

## 17. Deterministic path/ref/file audit

| Check | Result |
|---|---|
| Primary diff vs baseline | exactly 10 authorized files, one commit |
| Prompt-referenced paths | all exist (decision-playbooks/*, question-bank/*, 00_ROUTER.md, 01_CONSTITUTION.md, cases/good-cases/index.md, sources/S-*.md pattern, relationship-map.yaml) |
| Mode index ↔ files | 6/6 match |
| Q section IDs referenced by modes | all exist in bank (Q-INT/EVD/PRP/OWN/XCN/INTG/EVL/ALT/VAL/UNK/OBS/RES...) |
| GC/D/MP references | resolve against Stage 7 substrate |
| Sealed Stage 2-8 | untouched |

## 18. Bounded Primary remediation set

| # | Remediation | File(s) | Nature |
|---|---|---|---|
| R9-1 | Add routing-transparency output requirement: AUTO passes state selected mode + primary DP + overlays (incl. none) + one-line basis; explicit modes state mode/DP (basis optional) | system-prompt §13, AUTO.md output nuance | one field/line |
| R9-2 | Fail-closed overlay default: "start with zero overlays; activate only on named mechanism family; 'for completeness' is never a reason" | system-prompt §3 (+ AUTO.md routing step 3 optional echo) | one sentence |
| R9-3 | Reconcile buzzword wording with Stage 8: omission forbids canonical promotion/best-practice prescription, not naming a concrete technique as minimum correction when no existing T-* covers it (no runtime ID minting) | system-prompt §11 | one sentence |

Three wording-level edits; no redesign, no new files, no semantic change to Stage 8.

## 19. Stage 10 handoff implications

Stage 10 receives an Agent whose contract is deterministic enough to evaluate: six modes with object-based triggers; typed four-axis outputs; refutation-bearing findings; six terminal outcomes; routing transparency (post-R9-1) making mode-selection itself auditable — the eval harness can score routing correctness from the output without instrumenting the prompt. CA9-8 boundary matters for eval design: the harness must evaluate the **visible rationale** (evidence/mechanism/correction), never demand private deliberation; the routing basis (R9-1) is legitimately visible. The unevaluated label must survive until the first adversarial eval completes; Stage 10 must not retune the prompt against its own eval cases (the §14 clause binds the compiler and the evaluator alike — separate authorship matters here). The desktop/workspace-switch trace in report §16 gives Stage 10 a ready cross-shape probe.

## 20. Genuine new owner decisions

**None.** R9-1/R9-2 implement OD9-4/CA9-3 exactly; R9-3 implements CA9-4 exactly. The OD9-1..5 decisions are all applied (OD9-1 semantic compactness ✓; OD9-2 one-clarification ✓ in §3+AUTO; OD9-3 concise-rationale default ✓ in §13, no JSON-only; OD9-5 README scope ✓). No new mode, enum, file, or semantic question is open.
