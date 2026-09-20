# Stage 7 Agent Tasks

Stage 7 execution prompts are stored here so chat handoff can remain minimal.

- Cursor Primary: `tasks/stage7/CURSOR_PRIMARY.md`
- Codex + GLM Challenger: `tasks/stage7/CODEX_CHALLENGER.md`

Control issue: GitHub Issue #18.

Agents must treat the repository and Issue #18 as project truth. Chat-transcribed copies of these prompts are non-authoritative.

Current orchestration:
- Cursor = Primary Knowledge Architect / Ontology Builder
- Codex harness + GLM 5.3 = Independent Knowledge-Architecture Challenger
- ChatGPT = Chief Architect / gate authority

Both agent branches must start from the latest Stage 7 control baseline recorded in Issue #18.
