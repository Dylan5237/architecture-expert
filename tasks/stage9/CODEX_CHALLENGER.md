# Stage 9 Task — Codex + GLM Blind Agent-Contract Challenger Pass A

## Role

You are the **Independent Agent-Contract Challenger** for Stage 9 of `Dylan5237/architecture-expert`.

This is Blind Pass A.

- GLM 5.3: semantic/prompt-contract challenge.
- Codex: worktree/ref/file integrity and deterministic validation.

## Branch / worktree

Use a dedicated worktree on:

`challenge/stage9-agent-v0.1`

Fail closed on branch/HEAD/worktree mismatch.

Do not repair/switch/reset the shared checkout.

## Blindness

Do NOT read:
- `research/stage9-agent-v0.1`;
- any Cursor Stage 9 artifact;
- unmerged Stage 9 Primary commits/PRs.

Read only canonical main through the Stage 9 baseline + Issue #24.

## Mission

Independently define what an Agent v0.1 compilation must preserve and attack likely prompt/compiler failure modes.

Create only:

`reports/STAGE9_AGENT_AUDIT.md`

Do not build a competing Agent.

## Challenge areas

1. minimum system-prompt responsibilities;
2. prompt bloat / knowledge duplication;
3. AUTO routing correctness;
4. exact five DP mode mapping;
5. overlay vs persona boundary;
6. progressive disclosure;
7. project-fact authority;
8. Evidence Origin / Claim State / Finding Disposition / Terminal Outcome separation;
9. GOOD CASE / discriminating-evidence gate;
10. blocker/refutation threshold;
11. KNOWLEDGE_DRIFT scope;
12. ARCH_CONFLICT scope;
13. minimum correction;
14. stop/escalation;
15. output contract;
16. provider independence;
17. hidden framework bias;
18. excessive clarification / failure to act;
19. hidden chain-of-thought leakage;
20. Stage 10 boundary;
21. “unevaluated v0.1” status;
22. stable refs / mechanical integrity.

## High-risk traps

Attack designs where:
- system prompt becomes a knowledge encyclopedia;
- all 55 questions are pasted into prompt;
- overlays become personas/modes;
- AUTO chooses multiple primary DPs simultaneously;
- project generic knowledge overrides code/runtime/product intent;
- verdict axes collapse again;
- NO_DEFECT / ARCH_CONFLICT are treated as severities;
- GC gate is omitted;
- blocker lacks refutation condition;
- min correction disappears;
- Agent never stops;
- every ambiguity causes user clarification;
- prompt assumes a specific tool/provider/harness;
- “best practice” language reappears as blocker;
- system prompt asks for hidden CoT;
- Stage 10 expected answers leak into prompt.

## V9 preregistration

Create `V9-01..` checks covering at least:
- system-prompt compactness/duplication;
- role/non-goals;
- routing;
- one-primary-DP rule;
- five-mode mapping;
- overlay boundary;
- reasoning-spine fidelity;
- project-fact authority;
- typed axes;
- blocker threshold/refutation;
- GC gate;
- drift;
- ARCH_CONFLICT;
- min correction;
- terminal outcomes;
- stop;
- escalation;
- output contract;
- progressive disclosure;
- context-expansion conditions;
- provider independence;
- framework neutrality;
- no hidden CoT request;
- no eval leakage;
- v0.1 unevaluated label;
- file/ref integrity;
- worktree/branch integrity.

## Output

Create only:

`reports/STAGE9_AGENT_AUDIT.md`

Include:
1. minimal prompt contract;
2. canonical mode recommendation;
3. AUTO risk model;
4. highest-risk compilation traps;
5. context-loading requirements;
6. project-fact/evidence requirements;
7. GC/findings/terminal requirements;
8. stop/escalation requirements;
9. provider-independence requirements;
10. output-contract requirements;
11. Stage 10 boundary;
12. V9 checks;
13. genuine owner decisions only.

## Fail-closed

Before returning verify:
- dedicated worktree;
- branch descends from Stage 9 baseline;
- diff contains only the audit report;
- report non-empty;
- remote HEAD equals reported SHA;
- report read-back includes V9 checks and required sections;
- sealed Stage 2–8 untouched;
- no Primary Stage 9 artifact read.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. minimal prompt contract
4. mode recommendation
5. AUTO risks
6. highest-risk traps
7. context-loading requirements
8. evidence/output requirements
9. V9 checks
10. genuine owner decisions
