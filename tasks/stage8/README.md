# Stage 8 Agent Tasks

Stage 8 execution prompts live here so chat handoff remains minimal.

- Cursor Primary: `tasks/stage8/CURSOR_PRIMARY.md`
- Codex + GLM Blind Challenger: `tasks/stage8/CODEX_CHALLENGER.md`

Control issue: GitHub Issue #21.

Repository files and Issue #21 are authoritative; chat copies are not.

Mandatory execution invariant:
- one task = one dedicated worktree = one branch;
- shared/primary checkout is sync-only;
- fail closed on branch/HEAD/worktree mismatch.

Current orchestration:
- Cursor = Primary Reasoning-Model Architect
- Codex harness + GLM 5.3 = Independent Reasoning-Model Challenger
- ChatGPT = Chief Architect / Stage 8 gate authority
