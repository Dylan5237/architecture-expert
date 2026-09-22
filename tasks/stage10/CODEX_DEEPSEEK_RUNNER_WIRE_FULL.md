# Stage 10 Phase C0-R2 — Wire the Frozen DeepSeek Runner into a Measured Suite Controller

## Role

Continue as the **Stage 10 Reference Runner Harness Engineer** for `Dylan5237/architecture-expert`.

Chief Architect reviewed:

`eval/stage10-deepseek-runner@c177ae764703b7741b14e4a9501f176cf3164f27`

The preflighted primitives are sound, but the branch is **not yet executable as the measured 32-case suite runner**.

This is a bounded wiring + re-preflight task.

Do NOT run E10-001..032.
Do NOT read private oracle/rubric/coverage/design-report artifacts.
Do NOT score anything.
Do NOT change the reference provider/model.

## Fixed inputs

Frozen SUT:
`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Frozen suite:
`ff157eb1947860345a305fb29452b51e09dd3a2b`

Frozen PUBLIC pack:
`23a49382c949702446325d30e18d3321d8550c36`

Accepted C0-R preflight head:
`c177ae764703b7741b14e4a9501f176cf3164f27`

Reference provider:
- OpenCode Zen
- `https://opencode.ai/zen/go/v1`
- `deepseek-v4-pro`
- temperature = 0
- max_tokens = 8000
- no Kimi/Moonshot fallback

Work only on:
`eval/stage10-deepseek-runner`

Start HEAD must be exactly the accepted C0-R head above.

Read this task from:
`origin/main:tasks/stage10/CODEX_DEEPSEEK_RUNNER_WIRE_FULL.md`

Do not merge main.

## Why another gate is required

The accepted `controller.py` currently implements integrity primitives and `selftest` only.

Its README explicitly says:

> Future full-run integration will drive CaseRunner per E10 case...

Therefore a direct authorization to run 32 cases now would recreate the previous failure mode: measured orchestration would again live in ephemeral/unreviewed code.

The full measured execution path must be tracked, reviewed, selftested, and frozen BEFORE E10-001.

## Authorized files

Modify only:

- `eval/stage10/harness/README.md`
- `eval/stage10/harness/provider_openai_compatible.py`
- `eval/stage10/harness/runner.py`
- `eval/stage10/harness/controller.py`
- `eval/stage10/harness/PREFLIGHT.md`

No new tracked file in this task.

No PUBLIC/SUT/Agent file may change.

## R2-1 — Implement a real measured suite command

Add a controller command:

`python controller.py run-suite`

It must be the ONLY authorized measured-suite orchestration path.

No external/ephemeral controller is allowed in the later measured run.

The command must orchestrate E10-001..032 end-to-end using the frozen primitives.

Do not execute it in this task.

## R2-2 — Canonical repository/output paths

The controller must derive repository root robustly from its own tracked location.

Canonical PUBLIC cases:

`eval/stage10/public/E10-001.md` .. `E10-032.md`

Canonical measured output directory:

`eval/stage10/run/`

For a COMPLETE run, the only tracked measured output files must be:

- `eval/stage10/run/raw/E10-001.md` .. `E10-032.md`
- `eval/stage10/run/metadata.json`
- `eval/stage10/run/RUN_STATUS.md`

Exactly 34 files.

Do not track per-case intermediate metadata files.

Internal/checkpoint state may live in an OS temp directory outside the repository, but it must not be needed to interpret the committed evidence.

## R2-3 — Acquire lock before anything measured

`run-suite` sequence:

1. derive canonical run dir;
2. fail if prior measured evidence already exists;
3. acquire exclusive controller lock;
4. only then resolve provider credentials/provider object;
5. perform provider readiness gate;
6. only if readiness passes, begin E10-001.

Second controller must fail before provider initialization and before case/output creation.

The lock itself must not become a final committed evidence file.

A crash-stale lock is fail-closed and requires explicit operator cleanup after verification.

## R2-4 — Provider readiness before E10-001

Before any E10:

- make exactly one synthetic PRE10 readiness conversation;
- use OpenCode Zen / deepseek-v4-pro;
- use temperature 0 / max_tokens 8000;
- use a unique synthetic session header;
- verify response model identity;
- optionally verify usage/capacity endpoint;
- do not use any E10 payload or private eval material.

If readiness fails:
- create NO E10 raw output;
- measured run state = BLOCKED_PROVIDER;
- write only RUN_STATUS.md if Chief Architect later authorizes preserving that blocked attempt;
- for this task, just implement/test the behavior synthetically.

The later measured task will specify commit policy.

## R2-5 — PUBLIC mode parsing

For each E10 PUBLIC file:

- read the entire file bytes/text verbatim for USER content;
- parse only the public `requested_mode` metadata field;
- accepted modes only:
  - AUTO
  - ARCH_DESIGN
  - ARCH_REVIEW
  - CHANGE_REVIEW
  - ADR_REVIEW
  - INCIDENT_ANALYSIS

Do not strip/reconstruct the user payload.

Mode selection reads the exact frozen mode file from the SUT snapshot.

## R2-6 — New CaseRunner per case and per retry

For every canonical attempt:

- create a NEW `CaseRunner`;
- therefore create a NEW `PathSandbox`, tool log, messages list, read budget;
- do not reuse a CaseRunner across cases.

For a permitted technical retry:
- create ANOTHER NEW CaseRunner;
- new messages list;
- new sandbox/read budget;
- same case payload;
- same provider/model/settings;
- same case-specific session header is acceptable, because it is non-conversational routing metadata; if you choose a retry suffix, document it and keep it deterministic.

No previous result/tool-log/messages may enter the retry.

## R2-7 — Fix final-text fidelity

Current runner strips final model content.

For measured raw evidence:
- preserve the provider's final visible `message.content` string exactly as returned;
- do NOT `.strip()` it before raw write.

For the decision "did we receive a substantive final answer?", you MAY test:

`final_content.strip() != ""`

but the stored raw content must remain unmodified.

## R2-8 — Capture observed model identity

Every provider response round already hard-fails if response `model` differs from `deepseek-v4-pro`.

Additionally the runner result must record:
- observed model values returned across rounds;
- final observed model (or UNKNOWN only if provider omitted it on every response).

This is technical metadata, not scoring.

## R2-9 — Increase tool-round ceiling

The current default `max_tool_rounds=8` is too tight for a progressive-disclosure architecture agent.

Set measured default to:

`max_tool_rounds = 24`

Rationale:
- one round may contain multiple tool calls;
- the ceiling remains finite;
- it avoids turning legitimate multi-step knowledge loading into a harness-induced failure.

Do not vary the ceiling per case.

Record the fixed value in metadata.

## R2-10 — Technical retry policy

Per case:

- canonical attempt #1;
- max one retry ONLY if there is no non-empty final visible answer due to provider/transport/runtime technical failure;
- never retry because answer quality seems poor;
- retry is a fresh `CaseRunner`.

If attempt #2 also fails:
- do not create a raw file for that case;
- stop the entire suite immediately;
- overall measured attempt is `PARTIAL_TECHNICAL_FAILURE`;
- preserve technical facts in metadata/status;
- do not continue later cases.

A systemic provider error (auth/model-drift/capacity) may stop immediately without a retry when retry is clearly futile.

## R2-11 — No fallback result

At the start of each case and each attempt:

`result = None`

No branch may access a result from:
- prior case;
- prior attempt after it is classified failed;
- synthetic readiness.

Double failure = no raw output.

## R2-12 — Atomic canonical raw write

On successful substantive final content:

- write case raw to a temp file in the target raw directory;
- flush + fsync;
- atomic replace to canonical `raw/E10-XXX.md`;
- refuse overwrite if canonical file already exists;
- compute SHA-256 from canonical disk bytes after replace.

## R2-13 — One canonical metadata.json

Maintain:

`eval/stage10/run/metadata.json`

as the sole tracked metadata artifact.

It must be updated atomically after each case.

Required top-level fields:

- stage
- phase
- run_kind = isolated_api_blinded_reference
- run_id
- process_pid
- sut_sha
- suite_design_sha
- public_pack_sha
- harness_git_sha
- controller_sha256
- runner_sha256
- provider_adapter_sha256
- provider = OpenCode Zen
- api_host
- requested_model
- generation_settings
- max_tool_rounds
- prompt_precedence_mapping
- fresh_context_mechanism
- model_visible_tools
- sut_snapshot_mechanism
- external_context_boundary
- started_at
- completed_at
- status
- cases

Per case:

- id
- requested_mode
- start_order
- attempt_count
- technical_retry_count
- rounds_used
- observed_models
- final_observed_model
- session_header
- tool_calls:
  - path
  - bytes
  - result
- raw_output_path
- raw_output_sha256
- runner_status
- technical_errors

No:
- score
- oracle
- expected answer
- HF label
- quality judgment.

Do not store secret values.

## R2-14 — Atomic metadata updates

Write metadata.json through temp + fsync + atomic replace.

A process crash must leave either:
- previous complete metadata snapshot; or
- next complete metadata snapshot.

Never half-JSON.

## R2-15 — RUN_STATUS.md

At terminal stop, atomically write:

`eval/stage10/run/RUN_STATUS.md`

Allowed states:

- COMPLETE
- PARTIAL_TECHNICAL_FAILURE
- BLOCKED_PROVIDER
- HOLD_INTEGRITY_REVIEW

Only technical facts.

No Agent quality interpretation.

## R2-16 — Final reconciliation before COMPLETE

Before writing COMPLETE:

Assert:

1. 32 raw files exactly;
2. 32 case metadata records exactly;
3. IDs E10-001..032 exactly;
4. every raw non-empty;
5. every raw SHA equals metadata SHA;
6. no orphan raw;
7. no orphan metadata record;
8. attempt/retry counts legal;
9. all successful cases observed only the frozen model identity or provider omitted model field;
10. fixed settings identical across cases;
11. fixed max_tool_rounds identical across cases;
12. no output path collision.

Any failure => NOT COMPLETE.

## R2-17 — Duplicate-content HOLD

Before COMPLETE:

group the 32 canonical raw files by SHA-256.

If any distinct case IDs have byte-identical content:
- terminal technical state = HOLD_INTEGRITY_REVIEW;
- metadata/status lists hash + case IDs;
- do NOT delete outputs;
- do NOT score;
- do NOT infer Agent failure;
- Chief Architect decides whether duplicate content is plausible model behavior or runner association corruption.

## R2-18 — Full-path integration selftest

Add:

`python controller.py integration-selftest`

It must use:
- synthetic PRE10 cases only;
- fake provider / deterministic stub, NO network;
- temp directories only.

It must exercise the SAME orchestration functions used by `run-suite`.

Minimum scenarios:

A. two synthetic cases succeed:
- distinct outputs;
- metadata matches disk;
- COMPLETE reconciliation.

B. first attempt technical failure then retry success:
- attempt_count=2;
- technical_retry_count=1;
- fresh CaseRunner/fresh per-attempt state proven.

C. double failure:
- no raw file for failed synthetic case;
- suite stops;
- no previous-case output reused;
- state PARTIAL_TECHNICAL_FAILURE.

D. duplicate outputs:
- HOLD_INTEGRITY_REVIEW.

E. metadata tamper:
- SHA reconciliation blocks COMPLETE.

F. second concurrent controller:
- lock acquisition fails before provider/case execution.

No E10 payload may be loaded by integration-selftest.

## R2-19 — Provider readiness command

Add:

`python controller.py readiness`

This command:
- makes only the synthetic readiness call;
- verifies exact host/model/settings;
- outputs non-secret technical result;
- creates no E10 raw output;
- does not create measured run evidence.

Use it in this task once after deterministic tests.

## R2-20 — Measured command exists but MUST NOT run now

`python controller.py run-suite` must be implemented and visible in `--help`.

Do not invoke it in this task.

PREFLIGHT.md must explicitly state:

`E10_EXECUTION_COUNT: 0`

## R2-21 — Re-preflight gates

Run:

- Python compile checks for all three Python files;
- existing controller selftest;
- new integration-selftest;
- runner path-sandbox selftest if exposed, or equivalent deterministic sandbox test;
- `controller.py readiness` exactly once.

Provider readiness must still prove:
- OpenCode Zen host;
- deepseek-v4-pro;
- temperature 0;
- max_tokens 8000;
- stable observed model;
- no Kimi path.

## R2-22 — Report update

Update `PREFLIGHT.md` with a new R2 section containing:

- old accepted C0-R SHA
- new wiring commit SHA if known at readback, else pending
- run-suite command implemented = yes
- E10 execution count = 0
- max tool rounds = 24
- final-text fidelity = verbatim
- observed-model capture = yes
- controller selftest result
- integration-selftest result
- readiness result
- duplicate-HOLD result
- exact canonical future output set = 34 files
- no private eval read
- no Kimi fallback
- recommendation:
  - READY_FOR_PHASE_C, or
  - HOLD with exact blocker.

## Mechanical validation

Before return:

1. starting HEAD exactly `c177ae764703b7741b14e4a9501f176cf3164f27`;
2. exactly one wiring/re-preflight commit added;
3. diff limited to the 5 authorized harness files;
4. no E10 PUBLIC file changed;
5. no E10 raw output exists;
6. no SUT/Agent/Stage 2–9 file changed;
7. no private eval artifact read or added;
8. no Kimi/Moonshot executable fallback;
9. compile checks pass;
10. controller selftest passes;
11. integration-selftest passes;
12. readiness passes;
13. run-suite exists but was not executed;
14. measured output directory does not exist after this task;
15. no secret in Git diff;
16. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. R2 completion matrix
4. measured run command confirmation
5. E10 execution count
6. final-text fidelity result
7. max tool rounds
8. observed-model capture result
9. controller selftest result
10. integration-selftest result
11. readiness result
12. canonical future output set
13. changed-files list
14. mechanical validation
15. Phase C readiness recommendation
16. exact blocker if any
