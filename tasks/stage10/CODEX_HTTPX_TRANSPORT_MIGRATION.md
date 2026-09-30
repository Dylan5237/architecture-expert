# Stage 10 HTTPX Transport Migration — Replace urllib, Re-preflight Full-Agent Runtime

## Role

You are the **Stage 10 Reference Transport Engineer** for `Dylan5237/architecture-expert`.

Chief Architect accepted the transport characterization at:

`eval/stage10-transport-characterization@e7d57cc085c6dcfb3a21252742ae32a0a0866ffe`

The characterization established:

- urllib/full-Agent/non-streaming: 0/9 usable on equivalent DIRECT cells;
- httpx 0.28.1/full-Agent/non-streaming/DIRECT: 2/2 usable conversations;
- simple requests succeed under both stacks;
- request-body size alone is not sufficient to reproduce the failure;
- streaming accepts all complex requests, but visible completion is only 3/6;
- therefore the next justified intervention is `CHANGE_HTTP_CLIENT`, not a model/provider switch and not a streaming rewrite.

Primary classification:

`URLLIB_TRANSPORT_DEFECT`

This task replaces the Stage 10 provider transport with **httpx**, preserves evaluation semantics, then re-runs synthetic preflight.

Do NOT run E10.
Do NOT read private oracle/rubric/coverage/design-report artifacts.
Do NOT score anything.
Do NOT change Agent/SUT/PUBLIC content.

## Work branch

Use only:

`eval/stage10-httpx-transport`

Starting HEAD:

`d6f1716f34623aecf97eb80c225c282e78748cf7`

Dedicated clean worktree only.

Read this task from:

`origin/main:tasks/stage10/CODEX_HTTPX_TRANSPORT_MIGRATION.md`

Do not merge main.

## Frozen evaluation contract

Keep unchanged:

- SUT SHA: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- suite SHA: `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC pack SHA: `23a49382c949702446325d30e18d3321d8550c36`
- provider: OpenCode Zen
- host: `https://opencode.ai/zen/go/v1`
- model: `deepseek-v4-pro`
- temperature = 0
- max_tokens = 16000
- max_tool_rounds = 24
- dual SYSTEM mapping
- exact PUBLIC USER payload
- single model-visible tool `read_sut_file(path)`
- SUT snapshot and path sandbox
- read budgets
- case-level retry maximum = one retry
- duplicate-HOLD semantics
- no Kimi/Moonshot fallback
- hidden reasoning text must NEVER be persisted

## Authorized files

Modify only:

- `eval/stage10/harness/provider_openai_compatible.py`
- `eval/stage10/harness/runner.py`
- `eval/stage10/harness/controller.py`
- `eval/stage10/harness/PREFLIGHT.md`
- `eval/stage10/harness/README.md`
- optional `eval/stage10/harness/requirements.txt` if needed to pin httpx

No run evidence files.
No PUBLIC/SUT/Agent changes.

---

# H1 — Replace urllib transport with httpx

Use:

`httpx==0.28.1`

If a requirements file is added, pin exactly that version.

The production provider path must no longer use urllib for chat-completions transport.

It is acceptable for unrelated local config/file operations to keep standard library usage.

## H1.1 Client

Use a persistent `httpx.Client` inside `ReferenceProvider`.

Required properties:

- `trust_env=False`
- no implicit system proxy/environment fallback
- no automatic redirect to another host
- no provider fallback
- exact host remains `https://opencode.ai/zen/go/v1`
- exact model remains `deepseek-v4-pro`

Freeze transport route for this migration to:

`DIRECT`

Do NOT use the local proxy for the formal preflight in this task.

Rationale: the characterization's alternate-client evidence was httpx + DIRECT and produced the only 2/2 usable full-Agent non-streaming conversations.

## H1.2 Timeout policy

The characterization observed successful httpx first response bytes at approximately 191–233 seconds, which is too close to the previous 240-second read boundary.

Use fixed httpx timeouts:

- connect: 30 seconds
- read: 360 seconds
- write: 30 seconds
- pool: 30 seconds

No adaptive timeout.

Record these values in technical metadata.

Do not silently increase them during probes.

## H1.3 Byte-identical request retries

Build the JSON request body once as UTF-8 bytes.

On every transport retry:

- same body bytes;
- same URL;
- same headers except transport-managed headers;
- same model/settings/messages;
- same session header.

Selftest must prove the application body bytes are identical across retries.

---

# H2 — Preserve narrow retry semantics

Keep max transport attempts:

`3 total attempts`

Backoff:

- before attempt 2: 1 second
- before attempt 3: 3 seconds

Retry only:

- `httpx.ConnectTimeout`
- `httpx.ReadTimeout`
- `httpx.WriteTimeout`
- `httpx.PoolTimeout`
- `httpx.ConnectError` when caused by connection refused/reset/aborted/TLS EOF-type transport failure
- `httpx.ReadError`
- `httpx.RemoteProtocolError`
- HTTP 502
- HTTP 503
- HTTP 504

Fail closed without retry:

- HTTP 400
- 401
- 403
- 429
- all other 4xx
- HTTP 500
- malformed successful JSON
- model identity drift
- response-shape errors
- semantic/provider capability errors

Do not retry based on answer quality.

No route switching.

---

# H3 — Preserve technical diagnostics

Keep and adapt existing diagnostics to httpx.

For every provider round record only technical fields:

- transport_client = httpx
- httpx_version
- transport_route = DIRECT
- timeout policy
- transport_attempt_count
- transport_retry_count
- sanitized retry error classes/messages
- HTTP status
- observed model
- finish_reason
- content field present
- content present
- content length
- reasoning present
- reasoning length/count only
- numeric usage summary

Never store:
- hidden reasoning text
- full Authorization header
- API key
- full request prompt in provider logs

Keep the existing hidden-reasoning stripping before response data reaches the runner.

---

# H4 — Keep 16000 output budget

Do not change max_tokens from 16000.

The purpose of this task is transport migration, not another output-budget experiment.

The preflight must still explicitly verify:

- provider accepts 16000;
- returned model = deepseek-v4-pro;
- visible final answer exists in realistic full-Agent probes.

---

# H5 — Deterministic tests

Update/add provider-free tests for at least:

1. httpx transport is the production chat path;
2. trust_env is false;
3. route is DIRECT, no proxy configured;
4. timeout values exactly 30/360/30/30;
5. retryable ReadTimeout succeeds on attempt 2;
6. retryable RemoteProtocolError succeeds on retry;
7. retryable transport failures exhaust at 3 attempts;
8. HTTP 502/503/504 retry;
9. HTTP 500 does not retry;
10. HTTP 403 does not retry;
11. HTTP 429 does not retry;
12. model drift fails immediately;
13. malformed JSON fails immediately;
14. application body bytes are identical across retries;
15. no provider fallback;
16. max_tokens != 16000 rejected;
17. temperature != 0 rejected;
18. reasoning text removed, presence/length retained;
19. technical metadata identifies httpx/DIRECT/timeouts;
20. existing controller lock/atomic/reconciliation/duplicate tests remain green;
21. empty-final attempt diagnostics still survive case-level retry;
22. measured run_id remains `phasec-...`.

No network in deterministic selftests.

---

# H6 — Real synthetic preflight

No E10 payloads.

Use the exact frozen Agent system prompt and AUTO mode from the SUT snapshot.

Use a newly invented PRE10 architecture scenario, not any E10 case.

The scenario must require:
- evidence vs assumption separation;
- multiple architecture dimensions;
- minimum correction;
- uncertainty;
- at least one meaningful repository knowledge read in tool-enabled probes.

Do not tune the prompt between repeated runs.

## H6.1 Simple readiness

10 independent readiness calls through httpx DIRECT.

Require:

- 10/10 usable;
- model identity deepseek-v4-pro;
- no terminal transport failure;
- record recovered transport retries.

## H6.2 Full-Agent complex probe, no tool requirement

5 independent fresh conversations:

- full frozen system prompt;
- AUTO mode;
- hard synthetic architecture scenario;
- tool may be exposed but not required;
- max_tokens 16000.

Gate requirement:

- 5/5 must return non-empty visible final content;
- all successful response model identities must be deepseek-v4-pro;
- transport retries are allowed if they recover within the fixed policy;
- no empty final;
- no terminal transport failure.

If any of 5 fails, status is NOT READY.

## H6.3 Full-Agent required tool-loop probe

3 independent fresh conversations:

- full frozen system prompt;
- AUTO mode;
- synthetic scenario explicitly requires reading `00_ROUTER.md`;
- actual `read_sut_file` tool loop;
- final visible answer required.

Gate requirement:

- 3/3 complete the tool call and visible final;
- no terminal transport failure;
- no empty final;
- model identity stable.

## H6.4 Long-response observation

For the 5 complex + 3 tool-loop probes, record:

- total conversation elapsed time;
- each provider-round elapsed time;
- finish_reason;
- visible content length;
- transport attempts/retries;
- whether first successful response arrived after 240 seconds.

This is technical evidence only.

Do not store full synthetic model answers.

---

# H7 — Workspace hygiene

Before Python commands:

`PYTHONDONTWRITEBYTECODE=1`

Use `python -B`.

No repository-local `__pycache__`.

After deterministic tests and after real synthetic preflight, verify no run directory exists and Git diff contains only intended harness/report edits.

---

# H8 — Preflight decision

Update `PREFLIGHT.md` with:

- starting SHA
- characterization source SHA `e7d57cc085c6dcfb3a21252742ae32a0a0866ffe`
- httpx version
- route DIRECT
- timeout values
- retry policy
- deterministic test result
- readiness 10/10 result
- complex full-Agent 5/5 result
- tool-loop 3/3 result
- recovered transport retries
- any response exceeding prior 240s boundary
- empty-final count
- terminal transport failure count
- model identity result
- max_tokens 16000 result
- hidden reasoning policy
- `E10_EXECUTION_COUNT: 0`
- recommendation

Allowed final recommendations:

- `READY_FOR_ATTEMPT4`
- `HOLD_HTTPX_TRANSPORT_UNSTABLE`
- `HOLD_EMPTY_FINAL`
- `BLOCKED_HTTPX_DEPENDENCY`
- `HOLD_NEW_DEFECT`

To return `READY_FOR_ATTEMPT4`, all of the following are mandatory:

- deterministic tests pass;
- readiness 10/10;
- complex full-Agent 5/5 non-empty;
- required tool-loop 3/3 non-empty;
- zero model drift;
- zero terminal transport failures in full-Agent probes;
- zero empty finals in full-Agent probes;
- no E10 execution.

## No measured run

Do NOT invoke `run-suite`.

No Attempt #4 in this task.

---

# Mechanical validation

Before return:

1. starting HEAD exactly `d6f1716f34623aecf97eb80c225c282e78748cf7`;
2. diff only authorized files;
3. no run evidence directory;
4. no PUBLIC/SUT/Agent changes;
5. no private eval access;
6. no Kimi/Moonshot path;
7. production chat path uses httpx, not urllib;
8. httpx pinned to 0.28.1 if requirements file added;
9. route DIRECT;
10. timeouts 30/360/30/30;
11. temperature 0;
12. max_tokens 16000;
13. transport retry = 3 attempts, 1s/3s;
14. deterministic tests pass;
15. real readiness 10/10;
16. complex full-Agent 5/5;
17. tool-loop 3/3;
18. hidden reasoning text never stored;
19. no E10 provider call;
20. no secret in diff;
21. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. migration status
4. httpx version
5. route
6. timeout policy
7. retry policy
8. deterministic selftest result
9. integration-selftest result
10. readiness 10/10 result + recovered retry count
11. complex full-Agent 5/5 result
12. tool-loop 3/3 result
13. empty-final count
14. terminal transport-failure count
15. >240s successful-response count
16. model-identity result
17. max_tokens result
18. reasoning-metadata policy result
19. E10 execution count
20. changed-files list
21. mechanical validation
22. exact blocker if not READY_FOR_ATTEMPT4
