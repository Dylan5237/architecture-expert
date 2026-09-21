# Stage 9 Agent Tasks

Canonical execution prompts:

- Cursor Primary: `tasks/stage9/CURSOR_PRIMARY.md`
- Cursor bounded remediation: `tasks/stage9/CURSOR_REMEDIATION.md`
- Codex + GLM Blind Challenger: `tasks/stage9/CODEX_CHALLENGER.md`
- Codex + GLM Pass B: `tasks/stage9/CODEX_PASS_B.md`

Control issue: GitHub Issue #24.

Repository task files + Issue #24 are authoritative.

Mandatory isolation:
- one task = one dedicated worktree = one branch;
- shared/primary checkout is sync-only;
- fail closed on branch/HEAD/worktree mismatch.

Roles:
- Cursor = Primary Agent Compiler / Prompt Architect
- Codex + GLM = Independent Agent-Contract Challenger
- ChatGPT = Chief Architect / Stage 9 gate
