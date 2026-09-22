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


## Authorized Phase C API run

The isolated API harness passed C0 and is frozen at:

`78059179e103dd7275cad4493c70443b4562c647`

Full blinded execution task:

`tasks/stage10/CODEX_API_RUNNER_FULL.md`

Phase D scoring remains blocked until a fixed raw-output SHA returns.


## Controller hardening after invalid Phase C attempt

The first API full-run attempt was invalidated due to controller concurrency/write-integrity defects and provider quota exhaustion.

A clean rerun branch exists at:

`eval/stage10-api-runner-v2@78059179e103dd7275cad4493c70443b4562c647`

Before any E10 rerun, execute:

`tasks/stage10/CODEX_API_CONTROLLER_HARDEN.md`

No E10 case is authorized during controller hardening.


## Reference model reset

Owner decision:

`OD10-RM1: DO_NOT_USE_KIMI`

Kimi/Moonshot is excluded from Stage 10 reference evaluation.

Current gate:

`STAGE10_PHASE_C: HOLD_REFERENCE_MODEL_SELECTION`

Selection branch:

`eval/stage10-reference-model`

Task:

`tasks/stage10/CODEX_REFERENCE_MODEL_SELECTION.md`

No E10 rerun and no controller-hardening continuation is authorized until a non-Kimi reference model is selected and frozen.
