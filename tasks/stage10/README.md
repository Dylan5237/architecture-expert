# Stage 10 Tasks

Stage 10 evaluates the frozen Agent v0.1 at:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

## Suite status

Phase A suite is FROZEN at:

`ff157eb1947860345a305fb29452b51e09dd3a2b`

Chief Architect gate:

`STAGE10_SUITE_GATE: PASS / FROZEN`

The private suite-design branch remains unmerged during blinded runs.

## Current authorized phase

Phase C — blinded SUT execution — is authorized.

Runner-visible branch:

`eval/stage10-blinded-run`

Frozen public-pack baseline:

`23a49382c949702446325d30e18d3321d8550c36`

Runner protocol lives inside that runner-visible branch:

`tasks/stage10/CURSOR_BLINDED_RUNNER.md`

The runner branch contains:
- the frozen SUT lineage;
- 32 PUBLIC cases;
- a PUBLIC manifest;
- the runner protocol.

It does NOT contain the oracle, rubric, private coverage, scorer notes, or suite-design report.

## Historical Phase A tasks

- Initial suite design:
  `tasks/stage10/CODEX_EVAL_DESIGNER.md`
- Bounded remediation:
  `tasks/stage10/CODEX_SUITE_REMEDIATION.md`
- Final suite-gate microfix:
  `tasks/stage10/CODEX_SUITE_FINAL_MICROFIX.md`

## Phase C isolation

- use a dedicated runner workspace;
- one fresh model context/session per case;
- no web, external repos, connected project sources, other branches/refs, or private eval artifacts;
- if fresh context or prompt precedence cannot be enforced, fail closed before running cases;
- no scoring or Agent repair during Phase C.

Control issue: #27.

Phase D scoring is NOT authorized until the blinded runner returns a fixed raw-output SHA.


## Alternate Phase C harness preflight

The initial Cursor/Grok IDE runner failed closed before E10-001 because prompt precedence and case-context/tool isolation could not be guaranteed.

A direct-model isolated runner harness preflight is now authorized on:

`eval/stage10-api-runner`

Task:

`tasks/stage10/CODEX_API_RUNNER_PREFLIGHT.md`

This C0 preflight must not run any E10 case.
