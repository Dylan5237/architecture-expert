# Stage 9 Task — Cursor Primary Agent Compiler / Prompt Architect

## Role

You are the **Primary Agent Compiler / Prompt Architect** for Stage 9 of `Dylan5237/architecture-expert`.

Repository state + GitHub Issue #24 are authoritative.

## Branch / worktree

Work only in a dedicated worktree on:

`research/stage9-agent-v0.1`

Fail closed unless:
- branch is correct;
- HEAD matches the Stage 9 baseline in Issue #24;
- worktree is dedicated to this task;
- shared/primary checkout is not your execution workspace.

Do not repair/switch/reset/stash another Agent's checkout.

## Read first

1. `AGENTS.md`
2. `TASK.md`
3. Issue #24 latest checkpoint
4. `planning/STAGE1_RESEARCH_PLAN.md`
5. `00_ROUTER.md`
6. `01_CONSTITUTION.md`
7. `02_VOCABULARY.md`
8. `decision-playbooks/index.md`
9. `decision-playbooks/DP-001..DP-005.md`
10. `question-bank/index.md`
11. relevant Stage 7 router/domain/MP/FP/T/GC files
12. `reports/STAGE8_REASONING_MODEL.md`
13. `reports/STAGE8_REASONING_AUDIT.md`
14. `reports/STAGE8_RECONCILIATION.md`

Do not read the Stage 9 challenger branch.

## Mission

Compile the sealed Stage 6–8 contracts into a compact **provider-independent Architecture Expert Agent v0.1**.

The output is an executable behavioral contract, not a knowledge dump.

Preserve exactly:
- pre-routing + S1..S6;
- five DPs;
- overlay routing;
- project-fact authority matrix;
- Evidence Origin / Claim Epistemic State / Finding Disposition / Terminal Outcome separation;
- GOOD CASE / discriminating-evidence gate;
- blocker/refutation requirement;
- KNOWLEDGE_DRIFT scope;
- ARCH_CONFLICT;
- minimum correction;
- stop/escalation;
- progressive disclosure.

## Required artifacts

Create only:

- `agent/system-prompt-v0.1.md`
- `agent/README.md`
- `agent/modes/index.md`
- `agent/modes/AUTO.md`
- `agent/modes/ARCH_DESIGN.md`
- `agent/modes/ARCH_REVIEW.md`
- `agent/modes/CHANGE_REVIEW.md`
- `agent/modes/ADR_REVIEW.md`
- `agent/modes/INCIDENT_ANALYSIS.md`
- `reports/STAGE9_AGENT_V0_1.md`

Do not modify sealed Stage 2–8 artifacts.

## System prompt requirements

`agent/system-prompt-v0.1.md` must be compact, executable and provider-neutral.

It must encode behavior only:
- role / non-goals;
- routing;
- evidence-first project-fact handling;
- six-stage reasoning contract;
- context loading;
- typed finding/output contract;
- GC/falsification;
- min correction;
- drift/conflict;
- stop/escalation;
- anti-framework bias;
- concise rationale rather than hidden chain-of-thought.

It must reference the repository for:
- Constitution;
- DPs;
- question sections;
- MP/FP/T/GC details;
- sources.

Do NOT inline:
- all MPs;
- all 55 questions;
- FP/T catalog;
- source prose;
- Stage reports.

No provider-specific API/tool syntax.

## Modes

Canonical modes only:

- AUTO
- ARCH_DESIGN -> DP-001
- ARCH_REVIEW -> DP-002
- CHANGE_REVIEW -> DP-003
- ADR_REVIEW -> DP-004
- INCIDENT_ANALYSIS -> DP-005

AUTO is a router, not a sixth reasoning procedure.

Runtime/concurrency/resources/overload/reliability/trust/observability/integration/evolution/state-data are overlays only.

Mode files must remain thin and reference DPs.

## AUTO routing

AUTO should:
1. identify the object of reasoning;
2. select exactly one primary DP;
3. select only justified overlays;
4. ask one targeted clarification only if routing ambiguity changes the procedure;
5. otherwise proceed.

Do not create “specialized mode personas” from overlays.

## Context loading

Compile this behavior:

Router -> Constitution -> selected DP -> activated Q sections -> 1–2 domains -> linked MP/FP/T -> relevant GC -> named RQ/relationship only if needed -> source evidence only when generic claim is disputed/high-risk/low-confidence.

Project evidence comes before generic knowledge for project facts.

Do not default-load reports or the full corpus.

## Output behavior

Preserve typed fields.

Findings:
- BLOCKER/MUST_FIX
- HIGH_CONFIDENCE_RISK
- NEEDS_EVIDENCE
- NON_BLOCKING_IMPROVEMENT
- PERSONAL_PREFERENCE

Run terminal:
- NO_DEFECT
- MIN_SAFE_FIX_IDENTIFIED
- NEEDS_EVIDENCE
- OWNER_TRADE_OFF
- ARCH_CONFLICT
- NO_DECISION_CHANGING_WORK

BLOCKER/HIGH_CONFIDENCE_RISK must carry `refutation_or_invalidation`.

Do not collapse terminal outcomes into finding severity.

## Communication

Do not request or expose hidden chain-of-thought.

The Agent should present concise decision rationale:
- evidence;
- mechanism;
- finding/decision;
- min correction/alternatives;
- uncertainty;
- terminal outcome;
- escalation authority if any.

## Stage 10 boundary

Explicitly label Agent v0.1 as **unevaluated** until Stage 10.

No eval scenarios, expected findings, scorecards or prompt tuning against future cases.

## Mechanical checks

Before completion verify:

1. branch descends from assigned Stage 9 baseline;
2. diff contains only the 10 authorized artifacts;
3. system prompt does not enumerate all MPs/questions/FPs/Tactics;
4. exactly 6 mode files + mode index exist;
5. exactly 5 explicit reasoning modes map one-to-one to DP-001..005;
6. AUTO maps to no DP of its own and selects exactly one primary DP;
7. overlays are not separate mode files/personas;
8. all DP/Q/domain/GC references resolve;
9. typed evidence/finding/terminal values match Stage 8;
10. blocker refutation rule present;
11. narrowed drift and ARCH_CONFLICT preserved;
12. stop/escalation present;
13. no provider-specific tool/API syntax;
14. no Stage 10 artifact;
15. no sealed Stage 2–8 artifact modified;
16. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. artifact inventory
4. system-prompt structure/size
5. mode mapping
6. AUTO routing contract
7. context-loading contract
8. evidence/finding/terminal preservation
9. drift/conflict/stop/escalation preservation
10. duplication/provider-independence audit
11. mechanical validation
12. genuine owner decisions
