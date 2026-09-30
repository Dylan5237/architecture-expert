# Stage 10 Attempt #5 — Company Compute Gateway Migration + Full Measured Run

## Role

You are the **Stage 10 Reference Runtime Executor** for `Dylan5237/architecture-expert`.

Owner decision supersedes the previous OpenCode Go path:

> Do not use OpenCode Go anymore.
> Use the company's compute gateway instead.
> Available models include:
> - `glm-5.3`
> - `glm-5.3-flash`
> - `deepseek-v4.1-flash`

This task replaces the previously planned OpenCode-specific 429-capacity task.

Do NOT implement or retain any OpenCode-Go-specific quota policy as the basis of Attempt #5.

Goal:

1. connect the frozen Stage 10 harness to the company gateway;
2. perform a minimal model/capability selection;
3. freeze exactly one company-gateway model for the entire measured run;
4. execute one fresh full 32-case Attempt #5;
5. preserve evidence and stop.

Do NOT read private oracle before the measured run.
Do NOT score in this task.
Do NOT reuse or splice Attempt #4 raw outputs.

## Work branch

Use only:

`eval/stage10-company-gateway-attempt5`

Starting HEAD:

`9f361246c4a877b22ca338721b1dffe5130c0813`

Dedicated clean worktree only.

Read this task from:

`origin/main:tasks/stage10/CODEX_COMPANY_GATEWAY_ATTEMPT5.md`

Do not merge main.

## Owner decision / supersession

The following path is superseded:

`tasks/stage10/CODEX_429_CAPACITY_AND_ATTEMPT5.md`

Do not execute it.

Do not use:
- OpenCode Go endpoint;
- OpenCode Go quota/usage assumptions;
- OpenCode Go billing fallback;
- Kimi/Moonshot.

Historical evidence remains preserved but is not the runtime for Attempt #5.

---

# A — Company gateway discovery and secret handling

Resolve the company gateway from the user's existing local environment/config.

You must establish:

- base URL / endpoint;
- API protocol;
- authentication source;
- supported exact model identifiers for the three owner-listed models.

Do NOT:
- print or commit API keys/tokens;
- copy secrets into repository files;
- invent an endpoint;
- infer credentials from unrelated services.

If gateway endpoint/authentication is not available locally, stop with:

`BLOCKED_COMPANY_GATEWAY_CONFIGURATION`

Return what non-secret configuration is missing.

Prefer OpenAI-compatible chat-completions if that is what the gateway exposes.

If the protocol is not OpenAI-compatible, make the smallest adapter change necessary; do not redesign the harness.

---

# B — Minimal model selection

This is intentionally small. Do not build another benchmark matrix.

Candidates:

1. `glm-5.3`
2. `glm-5.3-flash`
3. `deepseek-v4.1-flash`

Run exactly one synthetic PRE10 full-Agent required-tool probe per candidate, sequentially.

Use the same synthetic prompt for all three:

- exact frozen Agent system prompt;
- exact AUTO mode;
- newly invented architecture scenario;
- must read `00_ROUTER.md`;
- must read at least one additional allowed knowledge file;
- must return visible final architecture analysis.

Use the same:
- temperature = 0;
- max_tokens = 32000 if accepted by candidate;
- max_tool_rounds = 24;
- SUT/path sandbox/tool schema;
- timeout/retry policy unless protocol requires a mechanical equivalent.

For each candidate record only:
- API/capability success/failure;
- model identity returned by gateway if available;
- tool-call success;
- final visible content non-empty;
- finish_reason;
- terminal transport/provider error if any;
- elapsed time.

Do NOT score answer quality.

## Selection rule

Use this deterministic policy:

1. Prefer `glm-5.3` if it passes all hard capability checks.
2. Otherwise use `glm-5.3-flash` if it passes.
3. Otherwise use `deepseek-v4.1-flash` if it passes.
4. If none pass, stop with:
   `BLOCKED_NO_COMPANY_GATEWAY_MODEL_CAPABLE`

This is a quality-oriented reference-run policy, not a benchmark ranking.

Once selected:
- freeze exactly one model;
- no model fallback during the measured run;
- no per-case model switching.

---

# C — Runtime adaptation

Modify only what is necessary to use the selected company gateway/model.

Keep unchanged wherever possible:

- SUT SHA `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- suite SHA `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC pack SHA `23a49382c949702446325d30e18d3321d8550c36`
- temperature 0
- max_tokens 32000, unless the selected gateway/model explicitly rejects it
- max_tool_rounds 24
- dual SYSTEM mapping
- exact PUBLIC user payload
- one model-visible tool `read_sut_file(path)`
- SUT snapshot/path sandbox/read budgets
- case-level retry maximum one
- atomic raw/metadata writes
- duplicate-HOLD
- hidden reasoning text never persisted

If the selected model rejects max_tokens=32000:
- try 16000 once as a capability fallback;
- record that capability limitation;
- if 16000 works, freeze 16000 for the entire measured run;
- do not search multiple token budgets.

No adaptive per-case token limits.

## Provider metadata

Measured metadata must record:

- provider = company compute gateway
- non-secret gateway base URL/host
- selected model
- generation settings
- transport client/protocol
- timeout/retry policy
- observed model identity if returned
- no secret values

---

# D — Bounded provider retry

Do not carry OpenCode-specific quota logic.

Use generic provider behavior only:

## Transport
Retain the frozen bounded transport retry:
- max 3 attempts per provider round;
- 1s / 3s backoff;
- retry transient connect/read/protocol/TLS failures;
- certificate verification failures fail closed.

## HTTP 429
If company gateway returns 429:
- honor a valid `Retry-After` once inside the provider round;
- cap wait at 120 seconds;
- if no valid Retry-After, fail closed;
- do not invent OpenCode-specific 60s/120s quota waits;
- case-level retry policy remains unchanged.

No fallback model after 429.

---

# E — Deterministic gate

Use:

`PYTHONDONTWRITEBYTECODE=1`

and `python -B`.

Run:

1. in-memory compile;
2. controller selftest;
3. integration-selftest;
4. PUBLIC dry-run 32/32.

Update tests only as mechanically required for the company gateway adapter/model settings.

No large new test matrix.

---

# F — Final smoke on selected model

After model selection and deterministic tests, run exactly two sequential synthetic smoke conversations using the selected frozen model:

## Smoke 1
Full-Agent architecture analysis, tool exposed but not required.

PASS:
- non-empty final;
- finish_reason=stop or equivalent successful terminal;
- no model drift;
- no terminal provider failure.

## Smoke 2
Full-Agent required tool-loop:
- read `00_ROUTER.md`;
- read one additional related allowed knowledge file;
- final visible analysis.

PASS:
- required reads completed;
- non-empty final;
- successful terminal;
- no terminal provider failure.

If either fails:
- do NOT run E10;
- return `FINAL_COMPANY_GATEWAY_FREEZE: FAIL`.

No repeated smoke until pass.

---

# G — Freeze commit

If selection + deterministic gate + both smokes pass:

Create exactly one runtime-freeze commit.

Record:
- selected gateway model;
- gateway host/base URL (non-secret);
- transport/protocol;
- generation settings;
- controller/runner/provider hashes;
- smoke results;
- `E10_EXECUTION_COUNT: 0`.

No tracked code change after freeze.

---

# H — Phase C Attempt #5

On the exact freeze SHA:

Set:

`STAGE10_MEASURED_AUTH_SHA=<freeze SHA>`

Immediately verify:
- HEAD exact;
- tracked worktree clean;
- no `eval/stage10/run/`.

Execute exactly once:

`python -B controller.py run-suite`

No second invocation.
No resume.
No mixing Attempt #4 evidence.
No manual case rerun.
No model switching.
No prompt adjustment.
No private oracle.
No output-quality inspection during execution.

---

# I — Terminal handling

## COMPLETE

Require:
- 32 raw files;
- metadata.json;
- RUN_STATUS.md;
- exactly 34 canonical run files;
- E10-001..032 exactly;
- all raw non-empty;
- all SHA reconcile;
- legal retry counts;
- selected model identity consistent;
- no duplicates;
- RUN_STATUS COMPLETE.

## PARTIAL / HOLD

Preserve exactly controller output.
Do not rerun in this task.
Do not patch in this task.

---

# J — Evidence commit

After the measured command terminates:

Create exactly one evidence commit.

Do not amend freeze commit.
Do not force-push.

Push branch and stop.

---

# Authorized tracked files before measured run

Modify only:

- `eval/stage10/harness/provider_openai_compatible.py`
- `eval/stage10/harness/runner.py` only if metadata/protocol adaptation requires it
- `eval/stage10/harness/controller.py`
- `eval/stage10/harness/PREFLIGHT.md`
- `eval/stage10/harness/README.md`
- `eval/stage10/harness/requirements.txt` only if dependency adaptation is necessary

After measured run:
- canonical `eval/stage10/run/**` only.

No PUBLIC/SUT/Agent changes.

---

# Return format

Return only:

1. branch
2. company gateway non-secret base URL/host
3. candidate capability results for all 3 models
4. selected model
5. selected max_tokens
6. runtime-freeze SHA
7. evidence SHA
8. FINAL_COMPANY_GATEWAY_FREEZE status
9. run state
10. deterministic gate result
11. Smoke #1 result
12. Smoke #2 result
13. measured run_id
14. completed case count
15. provider/transport retries
16. rate-limit events
17. technical error cases
18. observed-model integrity
19. raw inventory
20. duplicate-content result
21. reconciliation result
22. changed-files summary
23. secret scan
24. mechanical validation
25. exact blocker if not COMPLETE
