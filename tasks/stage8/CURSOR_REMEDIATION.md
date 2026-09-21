# Stage 8 Task — Cursor Primary Bounded Remediation

## Role

You are the **Primary Reasoning-Model Architect** for Stage 8 of `Dylan5237/architecture-expert`.

This is a **bounded remediation pass only** after accepted Codex + GLM Pass B.

Do not reopen research, playbook decomposition, question-bank design, Stage 7 knowledge, or Stage 9 prompt work.

## Fixed inputs

Primary starting point:

`research/stage8-reasoning-model@af5e431fd8a913590b89f981b4890288d270e560`

Accepted Challenger Pass B:

`challenge/stage8-reasoning-model@bce50e392b83889fdc906e43296aae7129e67f39`

Control:

GitHub Issue #21 latest Chief Architect checkpoint.

Read from `origin/main` without merging main into the Primary branch:
- `tasks/stage8/CURSOR_REMEDIATION.md`

Read the accepted Pass B report from the Challenger ref:
- `reports/STAGE8_RECONCILIATION.md`

## Worktree invariant

Work only in a dedicated worktree for:

`research/stage8-reasoning-model`

Before editing, verify:
- branch is exactly `research/stage8-reasoning-model`;
- HEAD is exactly `af5e431fd8a913590b89f981b4890288d270e560`;
- `git worktree list` shows this task has its own path;
- the shared/primary checkout is not your execution workspace.

The shared checkout may be detached or owned by another Cursor session. Do not repair, reset, switch, stash, or mutate it.

Fail closed on any mismatch.

## Allowed files

Modify only these existing Stage 8 Primary files:

- `decision-playbooks/index.md`
- `decision-playbooks/DP-001.md`
- `decision-playbooks/DP-002.md`
- `decision-playbooks/DP-003.md`
- `decision-playbooks/DP-004.md`
- `decision-playbooks/DP-005.md`
- `question-bank/index.md`
- `reports/STAGE8_REASONING_MODEL.md`

No other file may change.

Do not add new files.

## Fixed model decisions

These are not open for redesign:

- pre-routing + six reasoning stages;
- exactly five DPs: DP-001..DP-005;
- specialized reviews remain overlays/routes;
- Q-001..Q-055 remain unchanged in identity and meaning;
- 17 question-bank sections;
- no new source or Stage 7 knowledge node;
- no Stage 9 system prompt/mode file;
- no formal eval fixture.

## R8-1 — Separate typed reasoning categories

Replace the current mixed epistemic/verdict vocabulary with explicit typed fields.

### Evidence Origin

Keep the nine origins unchanged:

- PRODUCT_INTENT
- ARCHITECTURE_INTENT
- CODE
- CONFIG
- TEST
- RUNTIME
- HISTORY
- GENERIC_KNOWLEDGE
- USER_ASSERTION

### Claim Epistemic State

The `claim_epistemic_state` enum is only:

- CONFIRMED
- HYPOTHESIS
- UNKNOWN
- CONTESTED
- NEEDS_EVIDENCE

Remove these from the claim-state list:
- HIGH_CONFIDENCE_RISK
- NON_BLOCKING_IMPROVEMENT
- PERSONAL_PREFERENCE

### Finding Disposition

Use a separately typed `finding_disposition` field for load-bearing findings:

- BLOCKER / MUST_FIX
- HIGH_CONFIDENCE_RISK
- NEEDS_EVIDENCE
- NON_BLOCKING_IMPROVEMENT
- PERSONAL_PREFERENCE

`NEEDS_EVIDENCE` may appear both as a claim-state and a finding/task disposition only because the field name makes the type explicit.

Do not use one unlabeled shared enum.

### Decision/terminal values

Do not encode `NO_DEFECT` or `ARCH_CONFLICT` as ordinary defect severity.

They are represented by the run-level terminal/output structures defined in R8-8.

Update:
- shared schema in `decision-playbooks/index.md`;
- report evidence/verdict sections;
- all five DP Output Contract sections only as needed to remove contradictory terminology.

Do not change DP triggers/procedures.

## R8-2 — Replace total precedence chains with claim-type authority matrix

Remove formulations such as:

`CODE / CONFIG / TEST / RUNTIME > GENERIC_KNOWLEDGE > USER_ASSERTION`

for project current behavior.

Use this authority model:

| Claim type | Evidence/authority rule |
|---|---|
| Current behavior | CODE + CONFIG + RUNTIME + relevant TEST are complementary evidence, not a fixed total order. Surface disagreement and determine which evidence answers which sub-question. |
| Product intent | accepted PRODUCT_INTENT is authoritative for required capability/product contract. |
| Architecture intent/history | accepted ARCHITECTURE_INTENT / HISTORY record intended decisions/history; they do not establish current runtime truth. |
| Generic mechanisms | GENERIC_KNOWLEDGE explains mechanisms/risks; it never establishes or overrides a project-specific fact. |
| User assertion | USER_ASSERTION is an unverified claim unless explicitly accepted/grounded as an authoritative project statement. |

Required edit sites:
- `decision-playbooks/index.md`
- Q-004 in `question-bank/index.md`
- `reports/STAGE8_REASONING_MODEL.md` §7/equivalent
- DP wording only where it implies a total precedence chain or says all evidence disagreement is drift.

Task-specific evidence emphasis remains legal:
- DP-005 may start from RUNTIME for an incident timeline;
- DP-003 may emphasize CODE/CONFIG/TEST for a delta;
- DP-004 may treat the ADR as authoritative for what the ADR says.

That emphasis is not a universal total order.

## R8-3 — Narrow KNOWLEDGE_DRIFT

Canonical `KNOWLEDGE_DRIFT` triggers are project-truth-surface conflicts:

1. observed/current behavior vs accepted PRODUCT_INTENT;
2. observed/current behavior vs accepted ARCHITECTURE_INTENT / accepted historical decision record;
3. conflicting accepted intent records (product-vs-product, product-vs-architecture, or equivalent accepted project authorities).

A stale ADR/doc that claims current behavior inconsistent with actual evidence is covered by trigger 2.

Remove these automatic triggers:
- generic knowledge disagrees with a project fact;
- bare USER_ASSERTION disagrees with project evidence.

Those are ordinary applicability/verification questions unless the assertion has itself become an accepted authoritative project statement.

Drift output still records:
- competing claims;
- origins;
- claim epistemic states;
- next discriminating evidence/authority action.

Drift is not automatically a BLOCKER.

Update:
- `decision-playbooks/index.md`
- `reports/STAGE8_REASONING_MODEL.md`
- DP-002 / DP-003 wording where needed so unverified descriptions do not automatically become drift.

Keep DP-004 ADR-vs-current-behavior drift when the ADR is accepted architecture intent.

## R8-4 — Make the six-stage spine and S4 gate explicit

Canonical model:

**Pre-routing (not a reasoning stage):**
identify task/object → choose DP + optional overlay.

Then exactly six reasoning stages:

S1. Intent / Required Properties / Applicable Non-negotiables  
S2. Evidence Baseline  
S3. Mechanism Hypotheses + Conditional Knowledge Activation  
S4. GOOD CASE / Falsification / Discriminating-Evidence Gate  
S5. Adjudication + Minimum Correction / Alternatives / ARCH_CONFLICT  
S6. Terminal Outcome / Stop / Escalation

S4 must explicitly encode:

1. identify the candidate mechanism;
2. check the relevant GC qualifier(s), not only the GC title;
3. when mechanisms remain ambiguous, seek the cheapest discriminating evidence;
4. only then adjudicate a material defect/risk.

Do not add a seventh stage.

Update the spine in:
- `decision-playbooks/index.md`
- `reports/STAGE8_REASONING_MODEL.md`

Individual DPs may keep their current conditional flow if semantically consistent.

## R8-5 — Add finding refutation/invalidation

In the shared output contract, every finding with disposition:

- BLOCKER / MUST_FIX
- HIGH_CONFIDENCE_RISK

must include:

`refutation_or_invalidation: <evidence or condition that would overturn or downgrade the finding>`

Optional for:
- NEEDS_EVIDENCE
- NON_BLOCKING_IMPROVEMENT
- PERSONAL_PREFERENCE

Do not turn preferences or low-severity notes into proof obligations.

Document this rule in:
- `decision-playbooks/index.md`
- `reports/STAGE8_REASONING_MODEL.md`

Individual DPs inherit the shared schema; update their Output Contract text only if it currently contradicts the rule.

## R8-6 — Add one non-server reasoning demonstration

Add exactly one additional representative reasoning demonstration to `reports/STAGE8_REASONING_MODEL.md`.

Use this non-server shape:

**Desktop/local tool workspace switch with stale background work**

Shape:
- a desktop/local developer tool starts a background scan/index/import for workspace A;
- user switches to workspace B while the old work remains in flight;
- a late completion could update state for the wrong active workspace unless ownership/cancellation or the execution model prevents it.

Use existing Stage 8/7 knowledge only:
- DP-002 (or DP-003 only if framed as a change review);
- lifecycle + concurrency overlay;
- Q-011, Q-013, Q-015/Q-016 as appropriate;
- MP-001 / FP-001 and MP-010 / FP-012 discriminator;
- GC-016 when the execution model truly provides the assumed guarantee;
- evidence from CODE/CONFIG/RUNTIME/TEST as available;
- terminal may be NO_DEFECT, MIN_SAFE_FIX_IDENTIFIED, or NEEDS_EVIDENCE depending on evidence.

This is a reasoning/navigation demonstration only.
Do not turn it into an eval scenario or expected-findings fixture.

## R8-7 — Correct question-bank inventory count

In `reports/STAGE8_REASONING_MODEL.md`:

- change the claimed section count from 16 to **17**;
- list/retain the existing 17 section IDs;
- do not change Q-001..Q-055;
- do not merge Q-VAL and Q-UNK merely to make a count match.

## R8-8 — Separate run-level terminal outcome from finding disposition

Add a typed run-level field:

`terminal_outcome`

Allowed canonical terminal outcomes:

- NO_DEFECT
- MIN_SAFE_FIX_IDENTIFIED
- NEEDS_EVIDENCE
- OWNER_TRADE_OFF
- ARCH_CONFLICT
- NO_DECISION_CHANGING_WORK

These represent why the reasoning pass stops.

A terminal outcome is not a per-finding severity.

Examples:
- a review may contain a BLOCKER finding and end with `MIN_SAFE_FIX_IDENTIFIED`;
- a review with no material mechanism may end with `NO_DEFECT`;
- design may end with `NO_DECISION_CHANGING_WORK` once a min-sufficient proposal is established and nothing further can change the decision;
- multiple viable alternatives may end with `OWNER_TRADE_OFF`;
- insufficient evidence may end with `NEEDS_EVIDENCE`;
- a real authority conflict ends with `ARCH_CONFLICT`.

Keep the separate `arch_conflict` record with its required fields when terminal outcome is ARCH_CONFLICT.

Update:
- shared output contract in `decision-playbooks/index.md`;
- report stop/output sections;
- each DP Output Contract only as needed so it no longer treats NO_DEFECT / ARCH_CONFLICT as ordinary finding severities.

Do not change the six existing stop-condition semantics.

## Required consistency cleanup

After R8-1..R8-8, search all eight allowed files for stale formulations:

- the old eight-token “epistemic state” list;
- `HIGH_CONFIDENCE_RISK` described as claim epistemic state;
- `NON_BLOCKING_IMPROVEMENT` described as claim epistemic state;
- `PERSONAL_PREFERENCE` described as claim epistemic state;
- total-order `CODE/CONFIG/TEST/RUNTIME > ...`;
- generic-knowledge disagreement described as KNOWLEDGE_DRIFT;
- bare USER_ASSERTION conflict described as KNOWLEDGE_DRIFT;
- “16 sections”;
- findings treating NO_DEFECT / ARCH_CONFLICT as ordinary severity;
- output schema without `terminal_outcome`;
- BLOCKER/HIGH_CONFIDENCE_RISK schema without `refutation_or_invalidation`.

Keep legitimate task-specific uses of these tokens in their correctly typed roles.

## Mechanical validation

Before completion, verify:

1. branch descends from `af5e431fd8a913590b89f981b4890288d270e560`;
2. exactly one remediation commit is added;
3. diff changes only the eight allowed existing Stage 8 files;
4. no new file exists;
5. DP count remains 5 with IDs DP-001..DP-005;
6. Q count remains 55 with IDs Q-001..Q-055, unique and gap-free;
7. question section count is 17;
8. all DP→Q references resolve;
9. all Stage 7 MP/FP/T/GC/RQ references still resolve;
10. all five DPs retain Trigger + Do Not Use When + Stop + Escalation + Output Contract;
11. all five DPs still route the accepted overlay families;
12. evidence origin / claim state / finding disposition / terminal outcome are type-distinct;
13. shared output schema contains `refutation_or_invalidation`;
14. KNOWLEDGE_DRIFT has only the narrowed project-truth triggers;
15. S4 contains the four-step mechanism→GC→discriminating-evidence→adjudication gate;
16. report contains the new desktop/local-tool demonstration;
17. no Stage 9 system prompt/mode file exists;
18. no sealed Stage 2–7 artifact changed;
19. remote HEAD equals the reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. R8-1..R8-8 completion matrix
4. final six-stage spine
5. evidence-origin / claim-state / finding-disposition / terminal-outcome schemas
6. KNOWLEDGE_DRIFT trigger set
7. project-fact authority matrix
8. refutation-field confirmation
9. non-server demonstration summary
10. DP/Q mechanical counts
11. changed-files list
12. mechanical validation result
13. incomplete item + exact reason
14. genuine new owner decisions
