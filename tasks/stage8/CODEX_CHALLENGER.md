# Stage 8 Task — Codex + GLM Independent Reasoning-Model Challenger Pass A

## Role

You are the **Independent Reasoning-Model Challenger** for Stage 8 of `Dylan5237/architecture-expert`.

This is **Blind Pass A**.

- GLM 5.3 owns semantic/reasoning challenge.
- Codex owns repository/worktree integrity, deterministic validation and persistence.

## Branch / worktree invariant

Work only on:

`challenge/stage8-reasoning-model`

Fail closed unless:

1. you are in a dedicated worktree for this task;
2. shared/primary checkout is sync-only;
3. branch is exactly the assigned branch;
4. HEAD equals the Stage 8 baseline recorded in Issue #21;
5. no other Agent shares your worktree.

Do not stash/switch branches in Cursor's worktree.

## Blindness rule

Do NOT read:
- `research/stage8-reasoning-model`;
- any Cursor Stage 8 artifact;
- unmerged Stage 8 Primary commits/PRs.

Read only canonical `main`, Issue #21 and sealed Stage 2–7 artifacts.

## Read first

1. `AGENTS.md`
2. `TASK.md`
3. GitHub Issue #21
4. `planning/STAGE1_RESEARCH_PLAN.md`
5. `00_ROUTER.md`
6. `01_CONSTITUTION.md`
7. `02_VOCABULARY.md`
8. Stage 7 canonical MP/FP/T/domain/GC/relationship artifacts
9. Stage 7 audit/reconciliation reports

No source collection.

## Mission

Independently determine what a Stage 8 reasoning model **must and must not do**, then preregister Pass B checks.

Create only:

`reports/STAGE8_REASONING_AUDIT.md`

Do not create competing canonical playbooks or question bank.

## Required challenge areas

### 1. Reasoning spine minimality

Identify the minimum reusable reasoning dimensions.

Attack:
- rigid 18-step procession;
- dimensions that are merely knowledge domains;
- missing intent/evidence/validation/uncertainty;
- ordering that assumes backend/cloud systems.

### 2. Playbook distinctness

Identify which task families truly require different reasoning procedures.

Attack:
- one playbook per label with identical internals;
- mode explosion;
- a single giant universal playbook;
- unclear trigger/overlap rules.

### 3. Checklist rigidity

A good model activates questions conditionally.

Fail designs where:
- every task must ask every question;
- completeness is measured by filled sections;
- a missing checklist answer is treated as a defect without mechanism.

### 4. Evidence model

Require separation of:
- evidence origin;
- epistemic state;
- verdict/severity.

Attack source-authority = confidence and source-count = certainty.

### 5. Project-fact precedence

Check the required distinctions:
- behavior truth;
- product intent;
- architecture intent/history;
- generic mechanism knowledge.

Define what must happen on disagreement: `KNOWLEDGE_DRIFT`.

### 6. Verdict thresholds

Attack:
- blocker without evidence/mechanism/failure/impact;
- “best practice violation” as blocker;
- personal preference upgraded to architecture defect;
- inability to conclude not represented as NEEDS_EVIDENCE.

### 7. ARCH_CONFLICT

Challenge whether the model:
- distinguishes fundamental conflict from implementation inconvenience;
- preserves product capability;
- identifies decision authority;
- presents alternatives/trade-offs/reversibility.

### 8. Stop conditions

Attack analysis that never terminates because unused sections remain.

The model must allow terminal outcomes including:
- no defect;
- minimum safe fix;
- NEEDS_EVIDENCE;
- owner trade-off;
- ARCH_CONFLICT.

### 9. Escalation boundaries

Attack over-escalation and under-escalation.

Agents should not escalate routine mechanism choices.
They must escalate genuine authority decisions.

### 10. Minimum correction / overengineering

Attack default rewrites and fashionable architecture substitution.

Check whether the model asks:
- what protected property is at risk?
- what mechanism causes the risk?
- what smallest correction breaks the mechanism?
- when is wider redesign actually necessary?

### 11. GOOD CASE / false-positive handling

A reasoning model must explicitly consult accepted non-violation boundaries before a verdict.

Attack pattern-name matching.

### 12. Progressive disclosure

Reasoning must route into Stage 7 without loading the whole corpus.

Attack:
- all MP/FP/T loaded by default;
- sources/reports loaded before a disputed/high-risk claim;
- playbooks duplicating knowledge prose.

### 13. Stage 9 boundary

Fail any design that already writes:
- system prompt;
- Agent mode prompt;
- provider-specific instructions;
- tool-runtime orchestration contract.

Stage 8 defines the reasoning contract, not the Agent prompt.

## V8 preregistration

Create `V8-01..` checks covering at least:

- spine conditionality;
- playbook trigger clarity;
- playbook distinctness;
- overlap routing;
- no checklist rigidity;
- evidence-origin separation;
- epistemic-state separation;
- severity separation;
- blocker threshold;
- NEEDS_EVIDENCE terminal state;
- project-fact precedence;
- KNOWLEDGE_DRIFT;
- ARCH_CONFLICT;
- product-contract preservation;
- minimum correction;
- no framework bias;
- GOOD CASE gate;
- no false-positive pattern matching;
- stop conditions;
- escalation conditions;
- uncertainty;
- validation/proof;
- progressive disclosure;
- knowledge refs resolve;
- question IDs stable;
- no technology trivia;
- no duplicated question sets;
- no corpus duplication;
- cross-shape applicability;
- no Stage 9 smuggling;
- no eval leakage;
- worktree/branch integrity.

## Output contract

Create:

`reports/STAGE8_REASONING_AUDIT.md`

Include:

1. minimum reasoning-spine recommendation;
2. playbook-family recommendation;
3. highest-risk reasoning traps;
4. evidence/verdict model requirements;
5. KNOWLEDGE_DRIFT requirements;
6. ARCH_CONFLICT requirements;
7. stop/escalation requirements;
8. minimum-correction requirements;
9. GOOD CASE requirements;
10. progressive-disclosure requirements;
11. Stage 9 boundary;
12. V8 preregistered checks;
13. genuine owner decisions only.

## Fail-closed delivery

Before returning:

1. branch descends from the assigned Stage 8 baseline;
2. diff contains only `reports/STAGE8_REASONING_AUDIT.md`;
3. report non-empty;
4. remote HEAD equals reported SHA;
5. remote read-back contains the V8 checks and all required sections;
6. sealed Stage 2–7 artifacts are unchanged;
7. no Primary Stage 8 artifact was read.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. minimum reasoning spine
4. playbook-family recommendation
5. highest-risk traps
6. evidence/verdict requirements
7. stop/escalation requirements
8. V8 checks
9. genuine owner decisions
