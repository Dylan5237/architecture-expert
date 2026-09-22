# Stage 10 Tasks

Stage 10 evaluates the frozen Agent v0.1 at:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Current authorized phase:

- Phase A — Codex + GLM Independent Eval Designer / Oracle Author:
  `tasks/stage10/CODEX_EVAL_DESIGNER.md`
- Phase A bounded remediation:
  `tasks/stage10/CODEX_SUITE_REMEDIATION.md`
- Phase A final suite-gate microfix:
  `tasks/stage10/CODEX_SUITE_FINAL_MICROFIX.md`

No Agent run is authorized until the Chief Architect freezes the suite and exports PUBLIC inputs.

Control issue: #27.

Isolation:
- one task = one dedicated worktree = one branch;
- shared checkout is sync-only;
- oracle and runner artifacts must remain separated;
- fail closed on branch/HEAD/worktree mismatch.
