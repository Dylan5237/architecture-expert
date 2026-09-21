# Stage 9 Task — Cursor Primary Bounded Remediation

## Role

You are the **Primary Agent Compiler / Prompt Architect** for Stage 9 of `Dylan5237/architecture-expert`.

This is a **bounded remediation pass only** after accepted Codex + GLM Pass B.

Do not reopen Agent architecture, mode decomposition, Stage 8 reasoning semantics, knowledge design, or Stage 10 evaluation work.

## Fixed inputs

Primary starting point:

`research/stage9-agent-v0.1@9b4bc0cc0aa21a9ebd38409a3d898f8d2ed764ae`

Accepted Challenger Pass B:

`challenge/stage9-agent-v0.1@c450275c583fc38100553db3335c7e0a88df7dc5`

Control:

GitHub Issue #24 latest Chief Architect checkpoint.

Read from `origin/main` without merging main into the Primary branch:

- `tasks/stage9/CURSOR_REMEDIATION.md`

Read the accepted Pass B report from the Challenger ref:

- `reports/STAGE9_RECONCILIATION.md`

## Worktree invariant

Work only in a dedicated worktree for:

`research/stage9-agent-v0.1`

Before editing, verify:

- branch is exactly `research/stage9-agent-v0.1`;
- HEAD is exactly `9b4bc0cc0aa21a9ebd38409a3d898f8d2ed764ae`;
- `git worktree list` shows this task has its own path;
- the shared/primary checkout is not your execution workspace.

The shared checkout may be detached or owned by another Cursor session. Do not repair, reset, switch, stash, or mutate it.

Fail closed on any mismatch.

## Allowed files

Modify only:

- `agent/system-prompt-v0.1.md`
- `agent/modes/AUTO.md`
- `reports/STAGE9_AGENT_V0_1.md`

No other file may change.

Do not add new files.

## Fixed model decisions

These are not open for redesign:

- AUTO + five explicit modes only;
- AUTO is router only, no DP of its own;
- explicit modes map 1:1 to DP-001..DP-005;
- overlays remain parameters, never personas;
- system prompt remains behavior-focused and provider-independent;
- Stage 8 typed evidence/finding/terminal semantics remain unchanged;
- Stage 8 KNOWLEDGE_DRIFT / ARCH_CONFLICT / GC / min-correction / stop / escalation semantics remain unchanged;
- v0.1 remains UNEVALUATED until Stage 10.

## R9-1 — Add AUTO routing transparency

Add a compact user-visible route declaration for AUTO passes.

Canonical behavior:

For AUTO:

`route: {mode, dp, overlays, basis}`

Where:
- `mode` = selected explicit mode;
- `dp` = exactly one primary DP;
- `overlays` = selected overlays or `none`;
- `basis` = one concise routing reason based on the object of reasoning.

The basis is:
- a routing explanation for user-correctability;
- not hidden chain-of-thought;
- not a step-by-step deliberation transcript.

Explicit mode invocation:
- may state `mode` + `dp`;
- does not require an AUTO routing basis because no AUTO routing decision occurred.

Required edit sites:
- `agent/system-prompt-v0.1.md` §13 Output;
- `agent/modes/AUTO.md` Stop / output nuance;
- `reports/STAGE9_AGENT_V0_1.md` output/routing traceability sections.

Do not expand the shared Stage 8 schema into a large duplicated block.

## R9-2 — Make overlay activation fail-closed

In the system prompt routing section, state explicitly:

- start with **zero overlays**;
- activate an overlay only when task shape, symptom, or evidence justifies that mechanism family;
- “for completeness” is never a valid activation reason.

AUTO should reflect the same rule.

This is a wording hardening only.

Do not change:
- the overlay list;
- overlay-to-domain mappings;
- any DP procedure;
- finding thresholds;
- stop/escalation;
- evidence typing.

Required edit sites:
- `agent/system-prompt-v0.1.md` §3 Routing;
- `agent/modes/AUTO.md` routing step 3 or equivalent;
- `reports/STAGE9_AGENT_V0_1.md` overlay/routing preservation note.

## R9-3 — Reconcile omitted-technique wording with Stage 8

Replace the over-restrictive final wording in system prompt §11.

Canonical rule:

Stage 7 omission of a named technique means:

- do not promote it into a canonical MP/FP/T/GC node merely by name;
- do not recommend it as “best practice” or because it is fashionable;
- do not mint new canonical IDs at runtime.

However, the Agent may still **name a concrete implementation technique** as the minimum correction when:

1. the technique's exact mechanism breaks the identified failure mechanism;
2. the protected property requires that correction;
3. no existing canonical T-* already adequately covers the intervention.

Example category names such as circuit breaker, strangler, event sourcing, hedged requests, expand-contract remain non-canonical labels unless separately promoted by a future governed knowledge change.

The runtime Agent may name them as concrete implementation techniques under the rule above, but may not treat their names as evidence or universal tactics.

Required edit sites:
- `agent/system-prompt-v0.1.md` §11;
- `reports/STAGE9_AGENT_V0_1.md` anti-overengineering / semantic-drift audit note.

Do not add new tactic files or IDs.

## Required consistency cleanup

After R9-1..R9-3, search all three allowed files for stale formulations:

- AUTO output does not expose route;
- overlay activation lacks explicit zero-default;
- “for completeness” is allowed as overlay reason;
- omitted buzzword techniques are forbidden solely because no T-* ID exists;
- any wording implying AUTO may choose more than one primary DP;
- any wording implying route basis is private chain-of-thought;
- any wording implying v0.1 has been validated.

## Mechanical validation

Before completion verify:

1. branch descends from `9b4bc0cc0aa21a9ebd38409a3d898f8d2ed764ae`;
2. exactly one remediation commit is added;
3. diff changes only the three allowed existing files;
4. no new file exists;
5. system prompt remains behavior-focused and provider-independent;
6. mode set remains exactly AUTO + five explicit modes;
7. AUTO still maps to no DP of its own;
8. AUTO selects exactly one primary DP;
9. AUTO starts with zero overlays;
10. AUTO output exposes mode + DP + overlays + one-line routing basis;
11. route basis is explicitly not hidden chain-of-thought;
12. omitted-technique wording matches the canonical R9-3 rule;
13. no Stage 8 semantic artifact changed;
14. no Stage 10 artifact created;
15. v0.1 remains UNEVALUATED;
16. remote HEAD equals the reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. R9-1..R9-3 completion matrix
4. AUTO route-transparency confirmation
5. overlay zero-default confirmation
6. omitted-technique/min-correction wording confirmation
7. changed-files list
8. mechanical validation result
9. incomplete item + exact reason
10. genuine new owner decisions
