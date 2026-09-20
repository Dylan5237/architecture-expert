# Stage 7 Agent Tasks

Stage 7 execution prompts are stored here so chat handoff can remain minimal.

- Cursor Primary: `tasks/stage7/CURSOR_PRIMARY.md`
- Codex + GLM Challenger Pass A: `tasks/stage7/CODEX_CHALLENGER.md`
- Codex + GLM Challenger Pass B: `tasks/stage7/CODEX_PASS_B.md`

Control issue: GitHub Issue #18.

Agents must treat the repository and Issue #18 as project truth. Chat-transcribed copies of these prompts are non-authoritative.

Current orchestration:
- Cursor = Primary Knowledge Architect / Ontology Builder
- Codex harness + GLM 5.3 = Independent Knowledge-Architecture Challenger
- ChatGPT = Chief Architect / gate authority

For Pass B, Codex should read the prompt directly from `origin/main:tasks/stage7/CODEX_PASS_B.md` without merging main into the challenger branch.

Both agent branches must preserve their assigned lineages and fail-closed rules.
