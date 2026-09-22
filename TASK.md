Read `AGENTS.md`, GitHub Issue #27, `planning/STAGE1_RESEARCH_PLAN.md`, and your current Stage 10 task under `tasks/stage10/`.

Execute **Stage 10 evaluation only** against the frozen SUT:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Current authorization:
- Phase A only — Codex + GLM Independent Eval Designer / Oracle Author
- task: `tasks/stage10/CODEX_EVAL_DESIGNER.md`

Do not run the Agent yet.
Do not modify Stage 2–9 artifacts.
Do not repair Agent v0.1.
Do not expose PRIVATE oracle content to any future runner.

Mandatory:
- dedicated worktree;
- branch/worktree fail-closed checks;
- public case inputs and private oracle remain separable;
- Stage 10 suite design must be independent of future Agent outputs.

When Phase A completes, stop and return the fixed suite-design SHA to the Chief Architect. No Phase C runner begins before the Chief Architect suite-freeze gate.
