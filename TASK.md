Read `AGENTS.md`, GitHub Issue #21, `planning/STAGE1_RESEARCH_PLAN.md`, the sealed Stage 7 knowledge substrate, and your role-specific prompt under `tasks/stage8/`.

Execute **Stage 8 — Reasoning Model only**.

Primary:
- Cursor: `tasks/stage8/CURSOR_PRIMARY.md`

Independent Blind Challenger:
- Codex + GLM 5.3: `tasks/stage8/CODEX_CHALLENGER.md`

The role-specific repository prompt is authoritative for execution details.

Shared objective:
- create a compact reusable reasoning spine;
- create materially distinct decision playbooks;
- create a conditional mechanism-oriented question bank;
- define evidence/verdict, KNOWLEDGE_DRIFT, ARCH_CONFLICT, stop, escalation and minimum-correction rules;
- preserve Stage 7 progressive disclosure.

Mandatory execution rule:
- one task = one dedicated worktree = one branch;
- shared/primary checkout is sync-only;
- fail closed on branch/HEAD/worktree mismatch.

Do not modify sealed Stage 2–7 semantics.
No broad source collection.
No Stage 9 system prompt or Agent mode files.
No formal eval scenarios/results.

Use the branch assigned in Issue #21. Commit/push only authorized Stage 8 artifacts, then stop and report the fixed SHA to the Chief Architect gate.
