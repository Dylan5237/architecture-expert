# Stage 10 Final Runtime Freeze + Phase C Attempt #4

## Role

You are the **Stage 10 Final Runtime Freeze / Measured Run Executor** for `Dylan5237/architecture-expert`.

This task intentionally collapses the remaining runtime work into one bounded step.

Do **not** continue the superseded sequential-characterization matrix in `CODEX_HTTPX_SEQUENTIAL_QUALIFICATION.md`.

The goal is now:

1. make one final, narrow runtime patch;
2. run two realistic sequential synthetic smoke tests;
3. if both pass, freeze the harness immediately;
4. execute Phase C Attempt #4 exactly once;
5. preserve the resulting evidence and stop.

No additional transport research is authorized in this task.

## Work branch

Use only:

`eval/stage10-final-runtime-freeze-attempt4`

Starting HEAD:

`ed70a80c034198f62a480bbf346a41fac11f84bc`

Dedicated clean worktree only.

Read this task from:

`origin/main:tasks/stage10/CODEX_FINAL_RUNTIME_FREEZE_AND_ATTEMPT4.md`

Do not merge main.

## Frozen evaluation contract

Keep unchanged:

- SUT SHA: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- suite SHA: `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC pack SHA: `23a49382c949702446325d30e18d3321d8550c36`
- Provider: OpenCode Zen
- Host: `https://opencode.ai/zen/go/v1`
- Model: `deepseek-v4-pro`
- httpx: `0.28.1`
- Route: DIRECT
- trust_env = false
- no proxy
- no redirects
- timeouts: connect/read/write/pool = 30/360/30/30
- max_tool_rounds = 24
- dual SYSTEM mapping
- exact PUBLIC USER payload
- single model-visible tool: `read_sut_file(path)`
- SUT snapshot/path sandbox/read budgets
- case-level retry maximum = one retry
- duplicate-HOLD semantics
- no provider/model fallback
- no Kimi/Moonshot
- hidden reasoning text must NEVER be persisted

## Authorized tracked files

Modify only:

- `eval/stage10/harness/provider_openai_compatible.py`
- `eval/stage10/harness/runner.py`
- `eval/stage10/harness/controller.py`
- `eval/stage10/harness/PREFLIGHT.md`
- `eval/stage10/harness/README.md`
- `eval/stage10/harness/requirements.txt` only if required, but httpx must remain exactly 0.28.1

After measured execution, additionally allow only canonical `eval/stage10/run/**` evidence files produced by the tracked controller.

No PUBLIC/SUT/Agent changes.

---

# Part A — Final bounded runtime patch

## A1 — Retry all generic httpx.ConnectError except explicit certificate failure

Current code treats unrecognized `httpx.ConnectError` as non-retryable. This caused tool-loop termination after retryable protocol failures.

Change the fixed transport policy to:

- every `httpx.ConnectError` is retryable;
- EXCEPT explicit TLS certificate verification failure, which remains fail-closed.

Keep:
- max 3 transport attempts total;
- 1s / 3s backoff;
- byte-identical application request body;
- same route/model/settings/session;
- no provider fallback;
- no retry on answer quality.

No additional transport categories or adaptive policy.

## A2 — Raise fixed global output budget to 32000

Set:

`max_tokens = 32000`

globally for measured and synthetic execution.

Keep:
- temperature = 0
- no adaptive per-case budget
- no top_p/penalty override

Rationale:
the accepted httpx preflight produced `finish_reason=length` in 3/5 complex full-Agent finals at 16000.

Do not search for the “minimum sufficient” token value.
32000 is the final fixed evaluation budget for Attempt #4.

If the provider rejects 32000, stop with:

`BLOCKED_32000_CAPABILITY`

## A3 — Update only directly affected tests/metadata

Update deterministic tests and metadata assertions for:
- generic ConnectError retryability;
- certificate verification remains non-retryable;
- max_tokens must equal 32000;
- technical metadata still identifies httpx/DIRECT/timeouts;
- existing lock/atomic/reconciliation/duplicate/empty-final diagnostics remain green.

Do not add another research matrix.

---

# Part B — Minimal final freeze gate

Use:

`PYTHONDONTWRITEBYTECODE=1`

and `python -B`.

Before any provider call:

1. in-memory syntax compile of provider/runner/controller;
2. `python -B controller.py selftest`;
3. `python -B controller.py integration-selftest`;
4. `python -B controller.py public-dry-run`.

All must PASS.

No 10x readiness soak.
No route matrix.
No streaming comparison.
No alternate-client comparison.
No 16k/24k/32k matrix.

## B1 — Smoke #1: sequential complex full-Agent

Use ONE persistent `ReferenceProvider` / httpx.Client.

Run one newly invented PRE10 architecture scenario with:

- exact frozen Agent system prompt;
- exact AUTO mode;
- tool exposed but not required;
- max_tokens 32000;
- sequential single conversation;
- fresh CaseRunner/messages/sandbox.

PASS requires:
- non-empty visible final;
- `finish_reason=stop`;
- model = deepseek-v4-pro;
- no terminal transport failure.

## B2 — Smoke #2: sequential required tool-loop

Using the SAME persistent provider/client after Smoke #1, run a second fresh synthetic conversation that explicitly requires:

1. read `00_ROUTER.md`;
2. read at least one related allowed knowledge file;
3. return final visible architecture analysis.

PASS requires:
- both required reads completed;
- non-empty visible final;
- `finish_reason=stop`;
- model = deepseek-v4-pro;
- no terminal transport failure.

Do not tune prompts between retries/runs.
Do not repeat a failed smoke just to get a pass.

## B3 — Freeze rule

If BOTH smoke tests pass:

`FINAL_RUNTIME_FREEZE: PASS`

Immediately freeze that exact commit SHA.

No further Chief Architect gate is required before Attempt #4.

If either smoke fails:

- do NOT run E10;
- return `FINAL_RUNTIME_FREEZE: FAIL`;
- preserve the technical facts;
- do not start another characterization phase inside this task.

---

# Part C — Runtime patch commit

If Part A/B pass:

Create exactly one runtime-freeze commit.

Record:
- freeze SHA;
- controller SHA256;
- runner SHA256;
- provider SHA256;
- httpx version;
- max_tokens 32000;
- route/timeouts/retry policy;
- Smoke #1 result;
- Smoke #2 result;
- `E10_EXECUTION_COUNT: 0` before measured execution.

No tracked code change after this commit.

---

# Part D — Phase C Attempt #4

On the exact frozen runtime commit:

Set:

`STAGE10_MEASURED_AUTH_SHA=<freeze SHA>`

Verify immediately before run:

- HEAD == freeze SHA;
- tracked worktree clean;
- `eval/stage10/run/` absent;
- no code changed after freeze.

Then execute exactly once:

`python -B controller.py run-suite`

Do not:
- launch twice;
- parallelize;
- resume old evidence;
- manually rerun a case;
- inspect output quality;
- edit raw output;
- change network route;
- patch code;
- read private oracle.

The tracked controller owns all retries and terminal state.

---

# Part E — Terminal handling

## COMPLETE

Expected canonical evidence:

- 32 raw files
- `metadata.json`
- `RUN_STATUS.md`

Exactly 34 run files.

Validate:
- 32 cases exactly E10-001..032;
- all raw non-empty;
- all SHA values reconcile;
- legal retry counts;
- model identity intact;
- max_tokens 32000 recorded;
- no duplicate raw hashes;
- RUN_STATUS = COMPLETE;
- no harness/PUBLIC/SUT changes after freeze.

## HOLD_INTEGRITY_REVIEW

Preserve evidence exactly.
Do not rerun.
Do not score.

## PARTIAL_TECHNICAL_FAILURE / BLOCKED_PROVIDER

Preserve evidence exactly.
Do not rerun in this task.
Do not patch in this task.

A single incomplete Attempt #4 does not authorize another runtime redesign automatically.

---

# Part F — Evidence commit

After the measured command terminates:

Create exactly one evidence commit containing only canonical run evidence produced by the controller.

For COMPLETE:
- exactly 34 new run files.

For partial/HOLD:
- only the evidence actually produced.

Do not amend the freeze commit.
Do not force-push.

Push branch and stop.

---

# Return format

Return only:

1. branch
2. runtime-freeze SHA
3. final evidence SHA
4. FINAL_RUNTIME_FREEZE status
5. run state
6. httpx version
7. route/timeouts
8. transport retry policy
9. max_tokens
10. deterministic gate result
11. Smoke #1 result
12. Smoke #2 result
13. measured run_id
14. completed case count
15. technical retry count + case IDs
16. technical error cases
17. model-identity result
18. raw inventory
19. duplicate-content result
20. reconciliation result
21. changed-files summary
22. secret scan
23. mechanical validation
24. exact blocker if not COMPLETE

If the freeze gate fails before E10:
- final evidence SHA = NONE
- run state = NOT_STARTED
- E10 execution count = 0
- exact failed smoke/gate
