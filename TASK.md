Read `AGENTS.md`, GitHub Issue #24, `planning/STAGE1_RESEARCH_PLAN.md`, the sealed Stage 7 knowledge substrate, the sealed Stage 8 reasoning substrate, and your role-specific prompt under `tasks/stage9/`.

Execute **Stage 9 — Agent v0.1 only**.

Primary:
- Cursor: `tasks/stage9/CURSOR_PRIMARY.md`

Independent Blind Challenger:
- Codex + GLM 5.3: `tasks/stage9/CODEX_CHALLENGER.md`

The role-specific repository prompt is authoritative.

Shared objective:
- compile Stage 6–8 semantics into a compact provider-independent system prompt;
- create AUTO + five thin explicit mode contracts;
- preserve progressive disclosure, project-fact authority, typed evidence/finding/terminal schemas, GOOD CASE gate, KNOWLEDGE_DRIFT, ARCH_CONFLICT, minimum correction, stop and escalation;
- avoid duplicating the knowledge corpus.

Mandatory execution rule:
- one task = one dedicated worktree = one branch;
- shared/primary checkout is sync-only;
- fail closed on branch/HEAD/worktree mismatch.

Do not modify sealed Stage 2–8 semantics.
No source research.
No Stage 10 eval scenarios, expected findings, scorecards or benchmark results.
No provider-specific API/tool wrapper.

Use the branch assigned in Issue #24. Commit/push only authorized Stage 9 artifacts, then stop and report the fixed SHA to the Chief Architect gate.
