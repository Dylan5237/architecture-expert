# Stage 8 Task — Codex + GLM Pass B Reconciliation

## Role

Continue as the **Independent Reasoning-Model Challenger** for Stage 8 of `Dylan5237/architecture-expert`.

This is **Pass B — Reconciliation**. Blindness is now intentionally lifted.

- GLM 5.3: semantic reasoning-model challenge and reconciliation.
- Codex harness: deterministic branch/worktree/ref/ID validation, persistence and fail-closed delivery.

## Fixed inputs

Primary:
`research/stage8-reasoning-model@af5e431fd8a913590b89f981b4890288d270e560`

Blind Pass A:
`challenge/stage8-reasoning-model@4899120e216ab383a76b49bda8e7eeabd9cc5e1e`

Control:
GitHub Issue #21 latest Chief Architect checkpoint.

Work only on:
`challenge/stage8-reasoning-model`

Create only:
`reports/STAGE8_RECONCILIATION.md`

Do not edit Primary artifacts or sealed Stage 2–7 files.

## Worktree invariant

Use a dedicated worktree for this task.

The shared/primary checkout may currently be detached or used by another Cursor session. Do not repair, switch, stash, reset, or otherwise mutate that checkout.

Fail closed unless your dedicated worktree:
- is on `challenge/stage8-reasoning-model`;
- descends from accepted Pass A;
- has no unrelated changes;
- is not shared with another Agent.

## Chief Architect fixed decisions

### OD8-1 — Reasoning spine

Adopt a **six-stage reasoning spine plus pre-routing**, synthesizing Primary and Blind Pass A.

Pre-routing (not a reasoning stage):
- identify the object/task and select the DP + optional overlay.

Canonical reasoning stages:

S1. **Intent / Required Properties / Applicable Non-negotiables**
S2. **Evidence Baseline**
S3. **Mechanism Hypotheses + Conditional Knowledge Activation**
S4. **GOOD CASE / Falsification / Discriminating-Evidence Gate**
S5. **Adjudication + Minimum Correction / Alternatives / ARCH_CONFLICT**
S6. **Terminal Outcome / Stop / Escalation**

Issue #21's 18 labels remain a coverage map, not a procedure.

Rationale:
- Cursor's compact six-step direction is correct;
- task-class selection is routing, not substantive architecture reasoning;
- the Challenger is correct that GOOD CASE/falsification and evidence adjudication must remain explicit enough not to disappear inside a generic “correction” step.

Do not add a seventh stage merely to separate a terminal label from the close operation unless it creates a real procedural distinction.

### OD8-2 — Playbook set

Approve the Primary's **five canonical DPs**:

- DP-001 Architecture Design
- DP-002 Architecture Review
- DP-003 Change / PR Architecture Review
- DP-004 Architecture Decision Review
- DP-005 Incident Architecture Analysis

Runtime/concurrency, resource/overload, failure/reliability, trust, observability, integration/contract/evolution, state/data remain **overlays / knowledge routes**, not separate DPs.

Reason:
- they change activated questions, evidence emphasis and first knowledge route;
- they do not create a sufficiently distinct end-to-end reasoning procedure beyond DP-002/003/005;
- separate files would create Stage 9 mode explosion.

The Challenger's V8-06 must therefore test **coverage of all candidate task families by DP or explicit overlay**, not require a separate Runtime/Operational or Integration DP.

Reopen only if Pass B demonstrates a concrete task that cannot be routed without changing trigger/evidence/stop/output procedure.

### OD8-3 — Question-bank organization

Approve dimension-keyed reusable questions with activation conditions.

No playbook-local copies.

Stable item IDs remain `Q-001...`.

### OD8-4 — Three-axis reasoning classification

The Primary currently mixes epistemic states and verdict/disposition terms.

Canonical Stage 8 model must explicitly separate:

1. **Evidence Origin**
   - PRODUCT_INTENT
   - ARCHITECTURE_INTENT
   - CODE
   - CONFIG
   - TEST
   - RUNTIME
   - HISTORY
   - GENERIC_KNOWLEDGE
   - USER_ASSERTION

2. **Claim Epistemic State**
   - CONFIRMED
   - HYPOTHESIS
   - UNKNOWN
   - CONTESTED
   - NEEDS_EVIDENCE

3. **Finding / Decision Disposition**
   - BLOCKER / MUST_FIX
   - HIGH_CONFIDENCE_RISK
   - NEEDS_EVIDENCE
   - NON_BLOCKING_IMPROVEMENT
   - PERSONAL_PREFERENCE
   - NO_DEFECT
   - ARCH_CONFLICT

`NEEDS_EVIDENCE` may appear on both axes only when the field is typed: claim-state vs task/finding disposition. Do not use one unlabeled enum.

`HIGH_CONFIDENCE_RISK`, `NON_BLOCKING_IMPROVEMENT`, and `PERSONAL_PREFERENCE` are not claim epistemic states.

This is a category correction, not a new evidence claim.

### OD8-5 — Escalation authority

Keep the Issue #21 authority categories as the canonical default **criteria**, not a brittle closed vocabulary.

Escalate when resolution requires authority over one of:
- product capability / required-property trade-off;
- cross-team/external commitment;
- regulatory/compliance/non-negotiable interpretation;
- irreversible material data/contract migration;
- trust/security policy;
- material cost/budget commitment;
- decision-changing contested evidence or project-intent conflict.

Project-specific governance may name additional owners, but implementation detail and routine mechanism choice do not become escalations merely because an owner exists.

## Chief Architect findings against the fixed Primary

### CA8-1 — KNOWLEDGE_DRIFT is too broad

Primary currently says drift may fire when “generic knowledge would require denying a project fact.”

Correct rule:
- GENERIC_KNOWLEDGE explains mechanisms/risks and cannot itself contradict a project fact into drift;
- a mismatch between a generic pattern expectation and actual project behavior is ordinary applicability/adjudication, not KNOWLEDGE_DRIFT.

KNOWLEDGE_DRIFT should fire for inconsistent **project truth surfaces**, including:
- observed/current behavior vs accepted product intent;
- observed behavior vs accepted architecture intent/history;
- conflicting accepted product/architecture intent records;
- stale project documentation/ADR/history that claims project behavior inconsistent with current evidence.

USER_ASSERTION is an unverified claim. Its conflict with project evidence is normally a verification issue; call it drift only if the assertion is itself an accepted/project-authoritative statement.

Pass B must propose the minimal correction.

### CA8-2 — Project-fact precedence must be claim-type scoped, not a total order

Primary's:
`CODE / CONFIG / TEST / RUNTIME > GENERIC_KNOWLEDGE > USER_ASSERTION`
is directionally useful but too coarse.

CODE, CONFIG, TEST and RUNTIME can disagree and answer different questions.

Require a claim-type authority matrix:

- **Current behavior:** CODE + CONFIG + RUNTIME + relevant TEST are complementary evidence; disagreement is surfaced, not silently ranked.
- **Product intent:** accepted PRODUCT_INTENT is authoritative for required capability.
- **Architecture intent/history:** accepted ADR/Issue/owner decision + HISTORY establish recorded intent/history, not current runtime truth.
- **Generic mechanism knowledge:** never establishes a project-specific fact.
- **USER_ASSERTION:** claim requiring classification/verification unless explicitly accepted as authority.

Pass B must check every DP/question that currently embeds a simplistic precedence statement.

### CA8-3 — Three-axis category correction

See OD8-4.

Primary's report/index says the same token may be both epistemic state and verdict. That is too easy for Stage 9 to encode incorrectly.

Pass B must identify the minimal files/lines needing remediation.

### CA8-4 — Question taxonomy count mismatch

Primary report claims **16 sections**, but the actual question bank has **17 section IDs**:

Q-INT, Q-EVD, Q-PRP, Q-OWN, Q-XCN, Q-STA, Q-FLW, Q-RES, Q-OVL, Q-FAL, Q-TRS, Q-OBS, Q-INTG, Q-EVL, Q-ALT, Q-VAL, Q-UNK.

The bank itself appears coherent. Correct the inventory/count, not the questions, unless Pass B finds a real duplicate.

### CA8-5 — Verdict falsifiability is under-specified

Blind Pass A correctly requires refutability/invalidation evidence for load-bearing findings.

Primary has Q-048/Q-050 for alternatives/validation, but the shared output contract does not require a finding to name what evidence would falsify or downgrade it.

Pass B must test a minimal field/rule such as:

`refutation_or_invalidation: <evidence/condition that would overturn or downgrade this finding>`

Require it at least for:
- BLOCKER/MUST_FIX
- HIGH_CONFIDENCE_RISK

Do not turn every NON_BLOCKING/PREFERENCE item into a formal proof obligation.

### CA8-6 — GOOD CASE gate should be explicit in the spine

Primary behavior is substantively correct, but Stage 9 must not be able to interpret “GC then correction” as optional decoration.

Pass B should require S4 to state:

Before a material defect/risk verdict:
1. identify candidate mechanism;
2. check relevant GC qualifier(s);
3. seek the cheapest discriminating evidence when mechanism remains ambiguous;
4. only then adjudicate.

### CA8-7 — Terminal outcomes and finding dispositions must stay distinct

Primary uses verdicts plus stop reasons.

Preserve:
- a finding can be BLOCKER/HIGH_CONFIDENCE_RISK/etc.;
- a reasoning pass terminates because of NO_DEFECT, minimum safe fix identified, NEEDS_EVIDENCE, owner trade-off, ARCH_CONFLICT, or no decision-changing work remaining.

`OWNER_TRADE_OFF` is a terminal reason, not necessarily a finding severity.

Pass B should make this distinction explicit enough for Stage 9.

### CA8-8 — Five DPs need coverage proof, not file-count expansion

Test the following tasks against actual Primary routing:

- runtime/concurrency review without incident;
- resource/overload capacity review without incident;
- reliability/failure-containment review without incident;
- contract/integration as-is review;
- contract migration/change review;
- evolution/boundary review;
- trust/agent-action review.

Each must resolve cleanly to DP-002/003/005 + overlay and preserve evidence/stop/output semantics.

If all route cleanly, KEEP five DPs.

### CA8-9 — Cross-shape neutrality needs a concrete check

Primary's logic is mostly shape-neutral and includes OTP/seL4/local-first cases.

Pass B must inspect wording for hidden server/backend assumptions and, if needed, recommend one small non-server retrieval/reasoning demonstration (desktop/local tool/embedded) rather than adding a new DP.

### CA8-10 — Stage 9 boundary

Primary report's “Stage 9 may map…” handoff is acceptable as a mapping note.

Fail only if DP/question artifacts themselves contain persona/system-prompt/provider-runtime instructions.

## Pass B required work

1. Execute `V8-01..V8-36` against the fixed Primary.
2. Adjust V8-06 according to OD8-2: coverage may be via DP + overlay.
3. For every V8 check return:
   - PASS
   - PARTIAL
   - FAIL
   - CHECK_INVALID
   plus exact evidence, risk/mechanism, minimal correction.
4. Evaluate OD8-1..OD8-5 as fixed decisions.
5. Evaluate CA8-1..CA8-10 explicitly.
6. Audit all five DPs:
   - trigger;
   - distinct procedure;
   - evidence model;
   - GC/falsification;
   - stop;
   - escalation;
   - output contract;
   - anti-overengineering.
7. Audit all 55 Q IDs:
   - unique/stable;
   - section count/taxonomy;
   - activation conditions;
   - no trivia;
   - no duplicated playbook-local copies.
8. Audit all Stage 7 references from DPs/questions.
9. Verify representative traces remain navigation/reasoning demonstrations rather than eval fixtures.
10. Verify progressive-disclosure budget.
11. Verify no Stage 9 smuggling.
12. Produce a bounded Primary remediation set only; no new research.

## Output

Create only:

`reports/STAGE8_RECONCILIATION.md`

It must include:

1. V8-01..V8-36 matrix;
2. final spine reconciliation;
3. DP disposition/coverage matrix;
4. overlay coverage matrix;
5. question-bank integrity/taxonomy audit;
6. evidence-origin / claim-state / finding-disposition reconciliation;
7. project-fact authority matrix;
8. KNOWLEDGE_DRIFT correction;
9. ARCH_CONFLICT verification;
10. blocker/refutation threshold audit;
11. stop vs terminal-outcome reconciliation;
12. escalation audit;
13. GOOD CASE/falsification audit;
14. minimum-correction/overengineering audit;
15. progressive-disclosure results;
16. mechanical ID/ref/path audit;
17. bounded Primary remediation set;
18. Stage 9 handoff implications;
19. genuine new owner decisions only.

## Gate recommendation

Return exactly one:

`PASS | PASS_WITH_REMEDIATION | HOLD`

No new sources.
No Stage 9 work.
Do not edit Primary.

## Fail-closed delivery

Before returning:

1. dedicated worktree only;
2. branch descends from accepted Pass A;
3. diff since Pass A contains only `reports/STAGE8_RECONCILIATION.md`;
4. report non-empty;
5. remote HEAD equals reported SHA;
6. report read-back contains V8-01..36, all 5 DPs, all 55 Qs/taxonomy, OD8-1..5, CA8-1..10;
7. sealed Stage 2–7 and Primary Stage 8 artifacts remain unmodified.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. gate recommendation
4. V8 summary
5. spine verdict
6. DP/overlay verdict
7. question-bank verdict
8. evidence/drift/verdict model verdict
9. stop/escalation verdict
10. bounded remediation
11. Stage 9 handoff
12. genuine owner decisions
