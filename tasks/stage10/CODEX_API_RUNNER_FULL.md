# Stage 10 Phase C — Codex Isolated API Runner Full Blinded Execution

## Role

You are the **Stage 10 Isolated API Runner Controller** for `Dylan5237/architecture-expert`.

This phase executes the frozen Agent v0.1 against the 32 frozen PUBLIC cases using the already-preflighted direct-model API harness.

You are NOT the scorer.
You are NOT an eval designer.
You are NOT allowed to repair or tune the Agent, suite, prompt, mode files, or harness semantics.

## Fixed frozen inputs

Frozen Agent v0.1 SUT:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Frozen suite-design SHA:

`ff157eb1947860345a305fb29452b51e09dd3a2b`

Frozen PUBLIC-pack baseline:

`23a49382c949702446325d30e18d3321d8550c36`

Preflighted harness head:

`78059179e103dd7275cad4493c70443b4562c647`

Work branch:

`eval/stage10-api-runner`

Start only if branch HEAD is exactly the preflighted harness head above.

Read this task from:

`origin/main:tasks/stage10/CODEX_API_RUNNER_FULL.md`

Do not merge main.

## Harness freeze

The following harness files are now frozen for this run:

- `eval/stage10/harness/runner.py`
  - Git blob SHA: `46cc9f3b6d45465110da37e4887bf6807f3d67da`
- `eval/stage10/harness/provider_openai_compatible.py`
  - Git blob SHA: `2f10ad21f288841829760ad3d1534505df22fda9`
- `eval/stage10/harness/README.md`
- `eval/stage10/harness/PREFLIGHT.md`

Do NOT edit any harness file during the 32-case run.

If a harness defect appears:
- stop;
- preserve completed outputs;
- return PARTIAL_TECHNICAL_FAILURE;
- do not patch and continue under the same evaluation run.

Any harness change requires a new Chief Architect gate and, if behaviorally relevant, re-preflight.

## Frozen provider path

Use the exact provider class/path proven in Phase C0:

- provider family: OpenAI-compatible chat-completions;
- API host: `api.kimi.com`;
- model: `kimi-for-coding-highspeed`;
- SYSTEM messages + function/tool calling;
- runtime secret source: same local provider configuration path or equivalent environment variables.

Do not switch model/provider during the run.

If the configured endpoint/model no longer matches the above, STOP with:

`RUNNER_BLOCKED_PROVIDER_DRIFT`

Do not substitute another model.

Inference parameters:
- use the frozen harness behavior;
- temperature remains provider default / unspecified because that is what C0 preflight exercised;
- record this explicitly as `provider_default_unspecified`.

Do not change temperature or other generation parameters for individual cases.

## Repository / branch isolation

Use one dedicated worktree or single-branch clone on:

`eval/stage10-api-runner@78059179e103dd7275cad4493c70443b4562c647`

Do not inspect or repair any other worktree/checkout.

Do not fetch/read:
- `eval/stage10-suite-design`;
- `eval/stage10-blinded-run`;
- private eval branches;
- moving `main` after reading this task.

The PUBLIC cases are already present in this branch at:

`eval/stage10/public/E10-001.md` .. `E10-032.md`

## Pre-run fail-closed checks

Before E10-001:

1. confirm branch HEAD = harness head;
2. confirm harness file blob SHAs match the frozen values;
3. run:
   - Python syntax check;
   - harness `selftest`;
4. confirm no `eval/stage10/run/raw/` exists yet;
5. confirm no oracle/rubric/private coverage/design report exists in the branch;
6. resolve provider config WITHOUT printing secrets;
7. confirm provider host = `api.kimi.com`;
8. confirm model = `kimi-for-coding-highspeed`;
9. do NOT rerun PRE10-SMOKE as part of the measured 32-case run;
10. confirm PUBLIC IDs E10-001..032 are complete and unique.

If any check fails, do not run E10 cases.

## Canonical execution controller

Use the existing frozen harness functions.

You may write an **ephemeral, uncommitted controller script** in a temp directory outside the repo or execute equivalent one-off Python from shell.

Do NOT add another runner implementation to Git.

The controller must:

1. import the frozen harness;
2. load the provider exactly once;
3. materialize one temporary SUT snapshot from exact SUT SHA;
4. for each case E10-001..E10-032 in ascending order:
   - read the PUBLIC file verbatim;
   - parse only the public `requested_mode` field;
   - validate it is one of the six canonical mode IDs;
   - call frozen `run_case(...)`;
   - receive a brand-new messages array created inside `run_case`;
   - capture final user-visible `final_text` verbatim;
   - save it immediately to the canonical raw output path;
   - write/update technical metadata after each case;
5. destroy the SUT snapshot after the suite or on stop.

Sharing the same provider object and read-only SUT snapshot across cases is allowed:
- the provider adapter stores only endpoint/model/config and no conversation;
- `run_case` creates a fresh messages array and a fresh `PathSandbox` for every case.

Do not pass any prior response, tool log, messages, case payload, or case-derived summary into another case.

## PUBLIC case payload integrity

Pass the entire PUBLIC file content byte-for-byte as the USER content.

Do not:
- strip metadata;
- paraphrase;
- add hints;
- normalize formatting;
- inject case ID explanation;
- inject scoring criteria.

The mode is read only to select the exact frozen mode contract.

## One-attempt policy

For each case, one canonical substantive conversation only.

A conversation may contain multiple provider rounds because the model can call `read_sut_file`; these are one attempt.

Once `final_text` is non-empty:
- that case is complete;
- never rerun it for a better answer.

Technical retry is allowed only when no final substantive response exists and the failure is transport/runtime-level.

If a retry is required:
- max one technical retry per case;
- record the first failure;
- use a completely fresh `run_case` conversation for the retry;
- increment attempt/retry counts;
- never hide the technical failure.

If the retry also fails:
- record TECHNICAL_ERROR;
- continue to the next case only if isolation/harness integrity is intact.

If isolation/harness integrity itself is compromised, stop the entire run.

## Raw outputs

Create exactly:

`eval/stage10/run/raw/E10-001.md`
...
`eval/stage10/run/raw/E10-032.md`

Each raw file contains ONLY the exact `final_text` returned by the evaluated model.

No frontmatter.
No runner note.
No score.
No correction.
No post-processing except writing the returned Unicode string as UTF-8.

If a case has no final output after allowed technical retry:
- do NOT fabricate a raw answer;
- metadata marks TECHNICAL_ERROR;
- overall status cannot be COMPLETE.

## Technical metadata

Create:

`eval/stage10/run/metadata.yaml`

Required top-level fields:

- stage: 10
- phase: C
- run_kind: isolated_api_blinded
- sut_sha
- suite_design_sha
- public_pack_baseline_sha
- harness_sha
- runner_branch
- provider_class
- api_host
- model
- generation_parameters: provider_default_unspecified
- system_prompt_sha256
- provider_secret_source_name
- prompt_precedence_mapping
- fresh_context_mechanism
- model_visible_tools
- sut_snapshot_mechanism
- external_context_boundary
- case_order
- started_at
- completed_at
- cases

For every case:

- id
- requested_mode
- observed_model
- fresh_context: true
- attempt_count
- technical_retry_count
- rounds_used
- tool_calls:
  - path
  - bytes
  - status
- raw_output_path
- raw_output_sha256
- route_line: exact user-visible line beginning with `route:` if mechanically present, otherwise `UNKNOWN`
- runner_status: OK | TECHNICAL_ERROR
- technical_errors: []
- notes

The route-line extraction is mechanical only.
Do not infer or score route correctness.

Do not include:
- oracle;
- expected answer;
- hard-failure label;
- numeric score;
- runner quality judgment.

## Run status

Create:

`eval/stage10/run/RUN_STATUS.md`

Only technical facts:

- run state;
- frozen SHAs;
- harness SHA;
- provider/model;
- 32-case attempted/completed counts;
- cases with technical retry;
- cases with technical error;
- context-isolation status;
- prompt-precedence status;
- tool-boundary status;
- external-context status;
- raw-output inventory;
- exact technical limitations.

Allowed final states:

- COMPLETE
- PARTIAL_TECHNICAL_FAILURE
- BLOCKED

No qualitative Agent evaluation.

## No web / no external context

The evaluated model receives only the one `read_sut_file` tool.

The runner/controller itself must not obtain case-solving information from:
- web;
- other repositories;
- connected apps;
- suite oracle/rubric;
- prior model outputs.

The network call to `api.kimi.com` is inference transport and is allowed.

## Private-eval prohibition

Do not read or materialize:

- `eval/stage10/design/private/oracle.yaml`
- `eval/stage10/design/private/coverage.yaml`
- `eval/stage10/design/rubric.md`
- `reports/STAGE10_EVAL_SUITE_DESIGN.md`

Do not inspect the frozen suite-design branch at all.

## No evaluation behavior

Do not:
- score;
- compare answers;
- identify misses;
- label hard failures;
- repair prompt/modes/knowledge;
- rerun weak answers;
- summarize Agent quality.

Even obvious mistakes stay untouched.

## Authorized Git diff

After execution, the only new tracked files may be:

- `eval/stage10/run/raw/E10-001.md` .. `E10-032.md`
- `eval/stage10/run/metadata.yaml`
- `eval/stage10/run/RUN_STATUS.md`

Exactly 34 files for a COMPLETE run.

Harness/public/SUT files must remain byte-identical to pre-run HEAD.

Commit all run evidence in exactly one final run-result commit.

Do not commit:
- ephemeral controller;
- temp snapshot;
- pycache;
- provider config;
- secrets;
- debug dumps containing prompts beyond already tracked frozen files.

## Mechanical validation

For COMPLETE, verify:

1. pre-run HEAD was `78059179e103dd7275cad4493c70443b4562c647`;
2. exactly one run-result commit added;
3. diff contains exactly 34 authorized run files;
4. raw E10-001..032 all exist;
5. every raw file non-empty;
6. metadata has exactly 32 unique case records;
7. metadata IDs exactly match raw IDs;
8. every raw_output_sha256 matches file contents;
9. all 32 case records have `fresh_context: true`;
10. every case attempt_count is 1 unless a recorded technical retry occurred;
11. no case has more than one technical retry;
12. no score/oracle/HF/expected-answer fields exist;
13. no harness/public/SUT file changed;
14. frozen harness blob SHAs still match;
15. no private eval file exists in branch;
16. no secret pattern/value appears in Git diff;
17. status = COMPLETE only when 32 non-empty canonical outputs exist and no isolation breach occurred;
18. remote HEAD equals reported SHA.

If not COMPLETE, adapt validation to preserve all evidence and state exact technical failure.

Push and stop.

## Return format

Return only:

1. branch
2. SHA
3. run state
4. SUT SHA
5. suite-design SHA
6. public-pack baseline SHA
7. harness SHA
8. provider/model
9. prompt-precedence mapping
10. fresh-context mechanism
11. completed case count
12. technical retry count
13. technical error cases
14. isolation result
15. raw-output inventory result
16. changed-files summary
17. mechanical validation
18. exact blocker/limitation, if any
