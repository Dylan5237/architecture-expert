``
id: STAGE9-AGENT-AUDIT
title: "Stage 9 Independent Agent-Contract Challenger — Pass A (Blind)"
stage: 9
pass: A
role: independent-agent-contract-challenger
challenger: "Codex harness + GLM 5.3"
branch: challenge/stage9-agent-v0.1
baseline: 1837b10dee4f7efd2c2ab4c68059a5d46820aabd
date: 2026-09-21
issue: 24
blind: true
status: COMPLETE
``

# Stage 9 Independent Agent-Contract Challenger — Pass A（Blind）

## 0. Scope, blindness, and method

Read (sealed only): `AGENTS.md`, `TASK.md`, GitHub Issue #24 (full body + kickoff checkpoint), `00_ROUTER.md`, `01_CONSTITUTION.md` (usage contract + AX set), `02_VOCABULARY.md` (meta-terms and high-risk families), the full sealed Stage 8 substrate on `main@1837b10` — `decision-playbooks/index.md` with the six-stage spine, overlay table, R8-corrected typed axes (`terminal_outcome` distinct from finding dispositions, `refutation_or_invalidation` on BLOCKER/HIGH_CONFIDENCE_RISK), authority matrix, narrowed KNOWLEDGE_DRIFT, all five DP files, `question-bank/index.md` (17 sections / Q-001..055) — plus the Stage 8 synthesis/audit/reconciliation reports and the Stage 7 substrate they reference.

Not read: `research/stage9-agent-v0.1`, any Cursor Stage 9 artifact, any unmerged Stage 9 Primary commit/PR. No sealed artifact modified. No competing Agent built.

Method: independently define what an Agent v0.1 compilation **must preserve**, attack likely prompt/compiler failure modes, and preregister deterministic Pass B checks (`V9-01..`).

Division per Issue #24: GLM 5.3 owns the semantic/prompt-contract challenge; the Codex harness owns worktree/branch/ref/file integrity and fail-closed delivery.

---

## 1. Minimal system-prompt contract (challenge area 1, 2)

The system prompt is a **behavioral compiler target**, not a knowledge base. It must contain exactly fourteen behavioral blocks and nothing else:

| # | Block | Content requirement |
|---|---|---|
| P1 | Role | general-purpose architecture expert; the Issue #24 §1 nine-behavior job description condensed; explicit non-goals (not a pattern recommender / framework advocate / code-style reviewer / best-practices bot) |
| P2 | Scope guard | no re-explanation of corpus; retrieve via navigation; anti-framework-bias default-ban discipline (the ban list is behavior, not knowledge) |
| P3 | Routing contract | AUTO or explicit mode → exactly one primary DP + zero-or-more overlays from the Stage 8 overlay table; overlays tune question/domain selection only; one targeted clarification rule when routing is genuinely ambiguous and procedure-changing |
| P4 | Reasoning spine | the pre-routing + S1..S6 sequence **as behavior**, with the S4 subsequence (mechanism → GC qualifier → cheapest discriminating evidence → adjudicate) explicit; no re-derivation of why each stage exists |
| P5 | Navigation contract | the ten-step runtime load order of Issue #24 §4, including "Stage reports are provenance, not default context" and "project evidence before generic knowledge" |
| P6 | Project-fact authority | the claim-type matrix (current behavior = CODE+CONFIG+RUNTIME+TEST complementary; product intent = accepted PRODUCT_INTENT; architecture intent = ADR/HISTORY records intent not runtime truth; GENERIC_KNOWLEDGE never establishes project facts; USER_ASSERTION requires verification unless accepted authority) |
| P7 | Typed schema | four axes with exact vocabularies: Evidence Origin (9), Claim Epistemic State (5), Finding Disposition (5), Terminal Outcome (6); one line stating they are never collapsed |
| P8 | Findings contract | BLOCKER six-part requirement (evidence, mechanism, failure mode, material impact, GC-not-applicable, `refutation_or_invalidation`); HCR also requires refutation; "not best practice" is not a blocker |
| P9 | GC gate | the S4 subsequence restated as a mandatory pre-verdict check; no pattern-name verdicts |
| P10 | Minimum correction | the five-step rule as behavior |
| P11 | Drift + ARCH_CONFLICT | drift fires on project-truth-surface conflicts (three CA8-1 classes), never silently resolved; ARCH_CONFLICT record fields; AX-002 no silent contract shrink |
| P12 | Stop/escalation | six terminal outcomes honored; escalation = authority criteria only, not routine mechanism choice |
| P13 | Output behavior | concise rationale (evidence, mechanism, finding, correction, uncertainty, terminal outcome, authority question); **no hidden chain-of-thought**; the seven-field shared contract referenced by name, not duplicated |
| P14 | Status label | v0.1 is unevaluated until Stage 10 adversarial validation |

**What must stay outside the prompt** (anti-bloat, Issue #24 rules): the 10 MP statements, 55 questions, FP/T definitions, GC contents, source citations as permanent text, provider/tool syntax, per-overlay personas, framework prescriptions, eval expected answers. The prompt names **where** each lives (file paths) and **when** to load it (P5), never **what** it says. Size expectation: the prompt compresses `8 Stage-8/Constitution contract pages into behavioral instructions; if it approaches corpus size or restates any MP/Q body verbatim, it has failed compilation.

---

## 2. Canonical mode recommendation (challenge areas 4, 5)

Exactly six modes, no more:

| Mode | Maps to | Content allowed in mode file |
|---|---|---|
| AUTO | router only | routing decision procedure; ambiguity→one clarification rule; never a reasoning procedure |
| ARCH_DESIGN | DP-001 | ID/name, DP mapping, trigger, overlay behavior, default context load, stop/output nuance, handoff |
| ARCH_REVIEW | DP-002 | same thin shape |
| CHANGE_REVIEW | DP-003 | same |
| ADR_REVIEW | DP-004 | same |
| INCIDENT_ANALYSIS | DP-005 | same |

Mode files are **thin routing contracts** (≤`30 lines each): they point to their DP, add the mode's default context load and any stop/output nuance, and define handoff when the object of reasoning changes (incident attributed → CHANGE_REVIEW for the fix). They must not copy DP bodies — a mode file that restates the DP's Conditional Reasoning Path has failed thinness.

**Overlay vs persona boundary**: the nine overlays (runtime/concurrency, resources, overload, reliability, trust, observability, integration, evolution, state-data) are parameters that change question sections + first domain(s). They must never change finding thresholds, stop rules, escalation, product-contract protection, or evidence typing (Issue #24 overlay lock). A compiled Agent with CONCURRENCY_REVIEW as a mode persona has already failed: it implies a sixth procedure that does not exist, invites threshold drift per "mode", and recreates the mode explosion Stage 8 explicitly rejected.

---

## 3. AUTO risk model (challenge area 3)

AUTO is the highest-risk compilation surface because it is a **meta-decision compressed into a routing rule**:

| # | Risk | Failure shape | Mitigation the compilation must include |
|---|---|---|---|
| A1 | Multi-DP selection | AUTO activating DP-002 *and* DP-005 "to be thorough" — produces procedure blending and non-termination | Hard rule: exactly one primary DP per pass; if the object changes mid-pass, finish or abort the pass, then handoff |
| A2 | Vocabulary-driven routing | the word "review" in a live incident claim routing to ARCH_REVIEW; a PR mentioned in passing routing to CHANGE_REVIEW | Route by **object of reasoning** (what exists/what changed/what failed/what was decided/what is proposed), matching the Stage 8 overlap rule; the incident-then-fix sequencing example must survive |
| A3 | Overlay over-selection | AUTO attaching all nine overlays "for coverage" — defeats progressive disclosure | Overlays activate only when the trigger names a mechanism family or the shape justifies; default = zero overlays |
| A4 | Clarification paralysis | every ambiguous task producing a user question instead of action | One targeted clarification only when routing is genuinely ambiguous **and** the choice changes procedure; otherwise route and proceed, stating the routing and its basis (correctable by the user) |
| A5 | Routing opacity | silent DP choice the user cannot correct | Output must state which DP+overlays were selected and why (one line each); explicit mode selection always overrides AUTO |
| A6 | AUTO as sixth procedure | AUTO mode file growing its own reasoning steps | AUTO contains routing logic only; after selection it delegates wholly to the selected mode/DP |

---

## 4. Highest-risk compilation traps (challenge areas 6–20)

| # | Trap | Why it recurs | Pass B detection |
|---|---|---|---|
| T1 | Prompt-as-encyclopedia | compiler conflates "preserve semantics" with "include text" | Prompt restating any MP/Q/FP body; prompt length vs corpus ratio |
| T2 | 55-questions inline | "the Agent needs the questions" — no, it needs the *activation rule* | Question text in prompt; Q-IDs beyond routing references |
| T3 | Overlay personas | per-domain modes feel natural to prompt authors | Mode count > 6; overlay names as modes; per-overlay threshold text |
| T4 | Multi-DP AUTO | thoroughness instinct | A1 detection; mode files accepting >1 DP |
| T5 | Generic overrides project | knowledge feels authoritative; RUNTIME evidence is messy | Prompt ranking GENERIC_KNOWLEDGE above project origins; authority matrix inverted |
| T6 | Axis collapse | one "severity+confidence" enum is easier to prompt | Typed vocabularies merged; NO_DEFECT/ARCH_CONFLICT listed as severities (Issue #24: ARCH_CONFLICT is a terminal outcome; NO_DEFECT likewise) |
| T7 | GC gate dropped | "check GOOD CASES" becomes a polite mention | S4 subsequence absent from prompt; verdicts without gc_checked |
| T8 | Refutation dropped | feels like extra work per finding | BLOCKER/HCR without `refutation_or_invalidation`; field absent from output contract |
| T9 | Min-correction disappears | findings without fixes feel incomplete; rewrite instinct | Output without min_correction path; recommendations defaulting to redesign |
| T10 | Non-termination | "unused sections remain" instinct survives from checklist era | Terminal outcomes not honored; analysis continuing past decision point |
| T11 | Clarification paralysis | uncertainty feels like a user question | A4; prompts asking before routing |
| T12 | Provider capture | examples drifting into tool syntax/harness names | Provider/tool syntax; harness-specific terms in prompt |
| T13 | Best-practice blocker regression | "industry standard" rhetoric | BLOCKER without the six-part package; "violates best practice" phrasing |
| T14 | Hidden CoT request | "show your reasoning" instinct | Prompt asking for chain-of-thought; missing concise-rationale rule |
| T15 | Eval leakage | compiler anticipating Stage 10 answers | Expected findings/scorecards anywhere; demo traces with eval semantics |
| T16 | Mode file = DP copy | thinness feels insufficient | Mode file restating DP body sections |
| T17 | v0.1 presented as validated | shipping instinct | Missing unevaluated label in README/prompt |
| T18 | Stage reports as default context | "more context helps" | Load order including Stage 5-8 reports by default |

---

## 5. Context-loading requirements (challenge area 6)

The compiled navigation must preserve the Issue #24 ten-step order and its **negative space**:

- A focused project review never auto-loads: all 10 MPs, all 12 FPs, all 15 Ts, all 16 GCs, all 55 questions, all sources, or Stage reports.
- A mode routes to: one DP + activated question sections + 1-2 domains + linked nodes + relevant GC qualifiers.
- **Expansion conditions** (closed list): a discriminator requires it; evidence remains ambiguous; a cross-domain mechanism genuinely survives; a high-risk generic claim needs source verification. Anything else is not a valid expansion reason — "for completeness" is bloat.
- The relationship-map loads only when a relation/distinction/gap must be machine-checked (Stage 8 rule).
- Project evidence (code/config/runtime/tests/ADRs) is acquired per the authority matrix **before** generic knowledge is applied to project-specific claims.

---

## 6. Project-fact / evidence requirements (challenge areas 7, 8)

The prompt must encode the **claim-type authority matrix** verbatim-as-behavior (P6): four complementary current-behavior origins with surfaced disagreement (never silently ranked); accepted PRODUCT_INTENT governs required capability; accepted ADR/HISTORY governs recorded intent, never current runtime truth; GENERIC_KNOWLEDGE never establishes or overrides a project-specific fact; USER_ASSERTION requires classification/verification unless explicitly accepted authority. KNOWLEDGE_DRIFT stays narrowed to the three project-truth-surface classes; generic-vs-project mismatch is ordinary adjudication, not drift.

Typed axes must survive compilation **exactly**: 9 origins; 5 claim states (CONFIRMED/HYPOTHESIS/UNKNOWN/CONTESTED/NEEDS_EVIDENCE — the OD8-4 five, no verdict tokens inside); 5 finding dispositions (BLOCKER/HCR/NEEDS_EVIDENCE/NON_BLOCKING/PREFERENCE); 6 terminal outcomes (run-level, not severities — NO_DEFECT and ARCH_CONFLICT live here). A BLOCKER finding may coexist with terminal MIN_SAFE_FIX_IDENTIFIED; an ARCH_CONFLICT pass keeps its record. Compiler tests: NO_DEFECT must be reachable and rewarded; "might be bad" must fall below BLOCKER; PREFERENCE must never escalate alone.

---

## 7. GC / findings / terminal requirements (challenge areas 9, 10)

S4 as mandatory subsequence before any material defect/risk verdict: candidate mechanism → GC qualifier check → cheapest discriminating evidence if ambiguous → adjudicate. The GC check is **qualifier-level** (multi-writer *with declared merge* eliminates; "it's a CRDT" eliminates nothing). Pattern-name verdicts are categorical failures. BLOCKER = six parts (evidence, mechanism, failure mode, material impact, GC-checked-not-applicable, refutation). HIGH_CONFIDENCE_RISK = strong evidence + material risk + refutation. Refutation optional for NON_BLOCKING/PREFERENCE — no proof obligations on taste.

---

## 8. Stop / escalation requirements (challenge areas 13, 14)

Six terminal outcomes with their DP-specific mappings (DP-001 NEEDS_EVIDENCE when properties unstated; DP-002/005 NO_DEFECT as success; DP-003 delta-scope stop; DP-004 OWNER_TRADE_OFF among viable options). Stop when further reasoning cannot change the decision; unused sections are never a reason to continue. Escalation: the seven authority criteria (product capability trade-off; cross-team/external commitment; regulatory/non-negotiable interpretation; irreversible material data/contract migration; trust/security policy; material cost; decision-changing contested evidence). Never escalate: routine mechanism selection with sufficient evidence, implementation detail, personal preference. Over-escalation and under-escalation each have a detection: every ARCH_CONFLICT/product-contract weakening must reach an owner; mechanism choices inside one team's authority must terminate without escalation.

## 9. Provider-independence requirements (challenge area 16)

The prompt + modes + README contain no provider names, tool-call syntax, harness-specific terms, model/runtime assumptions, or file-access mechanics tied to a specific agent framework. Navigation is expressed as repository paths and load conditions (any harness that can read files can execute it). If an example needs an action, it is phrased neutrally ("load the domain index", not "call the read_file tool"). The invocation contract in the README describes **what evidence to connect when available**, not how a specific provider wires it.

---

## 10. Output-contract requirements (challenge areas 15, 19)

The compiled Agent references the Stage 8 shared output contract by location and shape: playbook, overlay(s), intent/properties, activated dimensions, question sets, knowledge route, evidence entries (origin+pointer+claim-state), knowledge_drift, gc_checked, findings (disposition+property+mechanism+failure_mode+impact+min_correction+refutation where required), arch_conflict record, terminal_outcome, stop_reason, escalation. Communication shows **concise rationale** — evidence, mechanism, decision, correction, uncertainty, terminal outcome, authority question — and **never hidden chain-of-thought** (T14). The prompt must instruct this directly; an Agent that exposes raw deliberation violates the contract as much as one that hides evidence.

---

## 11. Stage 10 boundary (challenge areas 20, 21)

Stage 9 compiles; Stage 10 evaluates. The compilation must not: create eval scenarios, expected findings, scorecards, benchmarks; optimize routing/output against anticipated eval answers (T15 — the strongest form of leakage, because it poisons the eval before it exists); or include "in case of evaluation, output X" behavior. Representative invocation traces in the Primary report are **routing/context-selection demonstrations only**. Every user-facing artifact (README at minimum; ideally prompt status block) must state: **Agent v0.1 is unevaluated until Stage 10 adversarial validation** — no capability claims beyond contract-preserving compilation.

---

## 12. V9 preregistered checks (Pass B)

Status vocabulary: PASS / PARTIAL / FAIL / CHECK_INVALID. Executed against the Primary Stage 9 implementation on `research/stage9-agent-v0.1`.

| Check | Pass condition | Failure signal |
|---|---|---|
| V9-01 Prompt compactness | Prompt is behavioral instructions only; ≤`1.5x the Issue #24 behavior-contract length; no corpus prose | Encyclopedia prompt; size ratio blown |
| V9-02 No knowledge duplication | No MP statement, Q text, FP/T/GC body, source prose in prompt; navigation by path+condition only | Restated corpus content |
| V9-03 Role/non-goals | Nine-behavior role + four non-goals present; no pattern-recommender/advocate drift | Missing non-goals; scope creep |
| V9-04 Routing contract | AUTO/explicit → exactly one primary DP + overlays; stated in output; explicit selection overrides AUTO | Multi-DP; silent routing |
| V9-05 Five-mode mapping | ARCH_DESIGN..INCIDENT_ANALYSIS map 1:1 to DP-001..005; no extra modes | Sixth mode; missing mode |
| V9-06 Overlay boundary | Nine overlays as parameters; never alter thresholds/stop/escalation/product-protection/typing | Overlay persona; per-overlay rules |
| V9-07 Mode thinness | Mode files contain only ID/mapping/trigger/routing/context-load/nuance/handoff; no DP body copy | Mode = DP duplicate |
| V9-08 AUTO = router only | No reasoning steps in AUTO; delegates after selection; one-clarification rule present | AUTO as sixth procedure |
| V9-09 Object-based routing | Routing by object of reasoning; incident-then-fix handoff preserved; vocabulary routing absent | Keyword matching |
| V9-10 Spine fidelity | Pre-routing + S1..S6 with S4 subsequence (mechanism→GC→discriminating evidence→adjudicate) encoded as behavior | Missing S4 subsequence; reordered semantics |
| V9-11 Navigation contract | Ten-step load order; negative-space list; closed expansion conditions | Default corpus loading; open-ended expansion |
| V9-12 Project-fact authority | Claim-type matrix present; complementary current-behavior origins; GENERIC_KNOWLEDGE lockout; USER_ASSERTION rule | Total-order precedence; inverted authority |
| V9-13 Typed axes | Four vocabularies exact and separate; claim states exclude verdict tokens | Collapsed enum; severity+confidence merge |
| V9-14 Terminal vs disposition | Terminal outcomes run-level; NO_DEFECT/ARCH_CONFLICT not severities; coexistence rule present | NO_DEFECT listed as severity |
| V9-15 Blocker threshold | Six-part package incl. GC-checked + refutation; "not best practice" excluded | Rhetoric blocker |
| V9-16 Refutation rule | `refutation_or_invalidation` required on BLOCKER/HCR; optional for preference-class | Missing field; proof obligations on taste |
| V9-17 GC gate | S4 subsequence mandatory pre-verdict; qualifier-level matching; gc_checked in output | Title-level GC; skipped gate |
| V9-18 No pattern-name verdicts | Findings name mechanisms; missing-pattern findings absent | "No circuit breaker" finding |
| V9-19 KNOWLEDGE_DRIFT scope | Three project-truth-surface triggers only; generic mismatch ≠ drift | Broad drift; silent resolution |
| V9-20 ARCH_CONFLICT scope | Nine record fields; fundamental-vs-inconvenience; terminal classification; AX-002 link | Convenience escalation; severity misclassification |
| V9-21 Minimum correction | Five-step rule present; output carries min_correction; anti-overengineering guard | Rewrite default |
| V9-22 Framework neutrality | Default-ban discipline; no style prescription; alternatives compared by property | Prescribed architecture |
| V9-23 Stop conditions | Six terminal outcomes with DP mappings; anti-continuation rule | Non-termination; section-filling |
| V9-24 Escalation criteria | Seven authority criteria; both-direction guards | Over/under-escalation |
| V9-25 Output contract | Shared schema referenced with typed fields incl. drift/gc/refutation/terminal; concise-rationale rule | Missing fields; prose-only output |
| V9-26 No hidden CoT | Prompt requires concise rationale, forbids chain-of-thought exposure | "Show your reasoning step by step" |
| V9-27 Provider independence | No provider/tool/harness syntax or assumptions; neutral action phrasing | Tool-call syntax; provider names |
| V9-28 No eval leakage | No scenarios/expected findings/scorecards; traces are routing demos; no eval-anticipating behavior | Leaked answers; benchmark framing |
| V9-29 v0.1 unevaluated label | README + prompt status state unevaluated-until-Stage-10 | Validated-capability claims |
| V9-30 File/ref integrity | All repo paths referenced by prompt/modes exist; DP/Q/GC/MP references resolve; mode index matches files | Dangling refs |
| V9-31 No sealed-artifact modification | Stage 2-8 files untouched by Primary diff | Semantic drift via edit |
| V9-32 Worktree/branch integrity | Challenger on assigned branch/worktree; blind rule held | Cross-contamination |

---

## 13. Genuine owner decisions

1. **OD-1 Prompt size budget**: confirm the compactness bound (suggest: prompt ≤ `200 lines / `1.5x Issue #24 §"behavior contract" length; mode files ≤ `30 lines) or fix different numbers before Pass B.
2. **OD-2 Clarification budget**: confirm the single-targeted-clarification rule (one question, only when routing is genuinely ambiguous and procedure-changing; otherwise route-and-state) as the canonical ambiguity policy, or amend for specific product contexts (e.g. regulated environments requiring more upfront confirmation).
3. **OD-3 Output verbosity default**: confirm concise-rationale output as the v0.1 default (full shared schema fields, but compact prose), versus structured-JSON-only output — affects Stage 10 eval harness design and provider-independence claims.
4. **OD-4 AUTO transparency level**: confirm that every AUTO pass states its selected DP+overlays and basis (one line each) in output — my recommendation; the alternative (silent routing, log-only) is thinner but uncorrectable by users.
5. **OD-5 Invocation contract scope**: confirm the README documents "what evidence to connect when available" without any provider setup, and that v0.1 ships without a runtime harness requirement — or authorize a minimal reference-invocation section (still provider-neutral).

No other decision is new: the six-mode set, overlay lock, typed axes, drift/conflict/stop/escalation/min-correction semantics, provider independence, and the Stage 10 boundary are all fixed by Issues #21/#24 and the sealed Stage 8 substrate.
