# Stage 8 Task — Cursor Primary Reasoning-Model Architect

## Role

You are the **Primary Reasoning-Model Architect** for Stage 8 of `Dylan5237/architecture-expert`.

Repository state and GitHub Issue #21 are authoritative. Chat is not project state.

## Branch / worktree invariant

Work only on:

`research/stage8-reasoning-model`

Before editing, fail closed unless all are true:

1. you are in a **dedicated git worktree** for this task;
2. no other Agent uses that worktree;
3. the shared/primary checkout is sync-only;
4. `git branch --show-current` is the assigned branch;
5. HEAD matches the Stage 8 baseline recorded in Issue #21;
6. `git worktree list` shows a distinct worktree path for this task.

Do not switch branches or stash in another Agent's worktree.

## Read first

1. `AGENTS.md`
2. `TASK.md`
3. GitHub Issue #21 including latest Chief Architect checkpoint
4. `planning/STAGE1_RESEARCH_PLAN.md`
5. `00_ROUTER.md`
6. `01_CONSTITUTION.md`
7. `02_VOCABULARY.md`
8. `decision-playbooks/` and `question-bank/` if they already exist on your branch
9. `principles/MP-001..MP-010.md`
10. relevant `domains/`, `failure-patterns/`, `tactics/`, `cases/good-cases/index.md`
11. `relationship-map.yaml`
12. Stage 7 synthesis/audit/reconciliation reports

Do not read the Stage 8 challenger branch.

## Mission

Implement the Stage 8 reasoning model defined in Issue #21.

The target is a **small reusable reasoning spine + materially distinct decision playbooks + a conditional question bank**.

The model must:
- reason from required properties and constraints;
- separate project facts from generic knowledge;
- require evidence before verdict;
- detect KNOWLEDGE_DRIFT;
- expose ARCH_CONFLICT instead of silently weakening product intent;
- prefer minimum necessary correction;
- check GOOD CASES before flagging a defect;
- stop when further reasoning cannot change the decision;
- escalate only genuine authority decisions;
- preserve Stage 7 progressive disclosure.

It must NOT become a universal linear checklist.

## Required outputs

Create:

- `decision-playbooks/index.md`
- `decision-playbooks/DP-*.md`
- `question-bank/index.md`
- `reports/STAGE8_REASONING_MODEL.md`

Do not modify sealed Stage 2–7 knowledge artifacts.

No final Agent system prompt.
No provider-specific mode files.
No eval scenarios/results.
No new source research.

## Reasoning spine

Treat the candidate spine in Issue #21 as a hypothesis.

You may:
- merge steps;
- reorder them conditionally;
- make branches optional;
- define entry/exit conditions.

You may not:
- require every task to traverse every dimension;
- reduce the model to “ask all questions”;
- smuggle a system prompt into a playbook.

## Decision playbooks

Use the smallest playbook set that captures genuinely different reasoning procedures.

Test the candidate families in Issue #21 rather than mechanically making one file per label.

Each retained DP must have:

- Trigger
- Do Not Use When
- Goal
- Minimum Inputs
- Evidence Baseline
- Conditional Reasoning Path
- Knowledge Routes
- Question Sets
- Stop Conditions
- Escalation Conditions
- Output Contract
- Anti-overengineering guard
- Common category mistakes

Stable IDs: `DP-001...`.

Do not renumber after commit merely for aesthetics.

## Question bank

Create stable `Q-*` IDs.

Organize by reusable reasoning dimensions, not technology/framework.

Questions must be conditional and mechanism-oriented.

Every question or question family should state activation conditions where useful.

Do not create:
- interview trivia;
- framework preference questions;
- duplicated questions per playbook when a reusable question suffices.

Playbooks should reference question IDs/sections instead of copying the questions.

## Evidence / verdict model

Implement Issue #21's required distinction:

**Evidence origin** != **epistemic state**.

Project-specific claims must obey precedence:

- current behavior: code/config/test/runtime evidence before generic knowledge;
- intended behavior: accepted product requirements before generic knowledge;
- architecture intent/history: ADRs/accepted Issues/history/owner decisions before inference.

Disagreement -> `KNOWLEDGE_DRIFT`.

Define evidence sufficiency for:
- BLOCKER / MUST_FIX
- HIGH_CONFIDENCE_RISK
- NEEDS_EVIDENCE
- NON_BLOCKING_IMPROVEMENT
- PERSONAL_PREFERENCE

A blocker must include evidence + mechanism + failure mode + impact.

## ARCH_CONFLICT

Define an explicit structure containing at least:

- capability / required property;
- conflicting constraint;
- evidence;
- fundamental-vs-inconvenience determination;
- alternatives;
- trade-offs;
- reversibility;
- authority owner;
- evidence still needed.

Never use implementation inconvenience alone as an ARCH_CONFLICT.

## Stopping / escalation

Every DP needs explicit stop and escalation rules.

Do not keep analyzing to fill sections.

The correct terminal result may be:
- no material architecture defect;
- minimum safe correction identified;
- NEEDS_EVIDENCE with next discriminating evidence;
- multiple viable alternatives awaiting owner trade-off;
- ARCH_CONFLICT.

## GOOD CASE discipline

Before classifying a suspicious structure as a defect:
- route to relevant GC(s);
- check whether the concrete mechanism is actually present;
- do not penalize compliant alternate forms.

## Representative demonstrations

The synthesis report must demonstrate the model on the Issue #21 cases using **concise decision traces only**, not private chain-of-thought and not Stage 10 eval fixtures.

## Mechanical validation before completion

Verify:

1. branch descends from the assigned Stage 8 baseline;
2. diff contains only Stage 8 Primary artifacts;
3. every DP ID is unique and indexed;
4. every referenced Q ID exists;
5. every knowledge reference (domain/MP/FP/T/GC) resolves;
6. every DP has Trigger + Stop + Escalation + Output Contract;
7. no DP duplicates the Constitution or MP prose;
8. no question bank technology trivia;
9. no Stage 9 system prompt/mode files;
10. no sealed Stage 2–7 artifact modified;
11. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. reasoning spine
4. DP count + IDs/titles
5. question count + taxonomy
6. evidence/verdict model
7. KNOWLEDGE_DRIFT rule
8. ARCH_CONFLICT rule
9. stop/escalation model
10. representative trace summary
11. mechanical validation
12. genuine owner decisions
