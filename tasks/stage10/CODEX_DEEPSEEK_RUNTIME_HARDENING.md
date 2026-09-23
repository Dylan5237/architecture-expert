# Stage 10 Phase C Runtime Hardening — DeepSeek Transport Retry + Output-Budget Diagnostics

## Role

You are the **Stage 10 Runtime/Harness Hardening Engineer** for `Dylan5237/architecture-expert`.

Two independent measured attempts have now failed before a complete suite could be produced.

Important observed technical facts already established by Chief Architect:

1. Attempt #2:
   - E10-001 first attempt produced an empty final visible response;
   - retry succeeded;
   - E10-003 later failed twice due transport/network errors.
2. Attempt #3B:
   - pre-run deterministic gates passed;
   - fixed LOCAL_PROXY `127.0.0.1:7897`;
   - 3/3 readiness soak passed;
   - E10-001 first attempt again produced an empty final visible response;
   - retry then failed with TLS `UNEXPECTED_EOF_WHILE_READING`.

No complete canonical suite exists yet.

Chief Architect classification:
- recurring network/TLS instability = RUNTIME/TRANSPORT
- recurring empty final = likely RUNTIME/HARNESS output-budget / response-shape issue until proven otherwise
- not an Agent quality result

Do NOT run E10 cases in this task.
Do NOT read Attempt #2/#3B raw outputs.
Do NOT read private oracle/rubric/coverage/design-report artifacts.
Do NOT score anything.

## Work branch

Use only:

`eval/stage10-deepseek-runtime-hardening`

Starting HEAD:

`c78b8cdd0eb88647170d10256d5139bd6c6a502e`

Dedicated clean worktree only.

Read this task from:

`origin/main:tasks/stage10/CODEX_DEEPSEEK_RUNTIME_HARDENING.md`

Do not merge main.

## Frozen evaluation semantics

Do NOT change:

- SUT SHA: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- suite SHA: `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC pack SHA: `23a49382c949702446325d30e18d3321d8550c36`
- provider: OpenCode Zen
- host: `https://opencode.ai/zen/go/v1`
- model: `deepseek-v4-pro`
- system/mode role mapping
- tool schema
- SUT snapshot boundary
- path sandbox
- read budgets
- requested_mode mapping
- 24 tool-round ceiling
- one case-level retry maximum
- duplicate-HOLD semantics
- no Kimi/Moonshot

This task may change only technical transport resilience, output-token budget, and technical observability.

## Authorized tracked files

Modify only:

- `eval/stage10/harness/provider_openai_compatible.py`
- `eval/stage10/harness/runner.py`
- `eval/stage10/harness/controller.py`
- `eval/stage10/harness/PREFLIGHT.md`
- `eval/stage10/harness/README.md`

No run evidence files.
No E10 raw outputs.
No PUBLIC/SUT/Agent changes.

---

# H1 — Provider-round transient retry

The current case-level retry restarts an entire architecture case when a single HTTP round drops.

For a 32-case multi-round suite, this is too fragile.

Implement a narrow **per-HTTP-round transport retry** inside the provider adapter.

## H1.1 Retryable conditions

Retry only failures where no usable model response was obtained and the failure is transport/transient:

- `RemoteDisconnected`
- connection reset / connection aborted
- socket/URL timeout
- TLS unexpected EOF / equivalent SSL EOF
- connection refused to the already-selected local route or upstream
- HTTP 502
- HTTP 503
- HTTP 504

Do NOT retry:
- 400
- 401
- 403
- model identity drift
- malformed successful JSON
- semantic/provider capability errors
- other 4xx by default

429:
- fail closed in this task; do not add hidden rate-limit policy.

## H1.2 Fixed retry policy

For each single provider chat round:

- max transport attempts: 3 total
- backoff before attempt 2: 1 second
- backoff before attempt 3: 3 seconds
- exact same request body/messages/model/settings/session header on all attempts
- no provider/model fallback
- no network-route switching

The retry policy is global and fixed, not per case.

## H1.3 Technical observability

Returned provider result must expose non-user-facing technical metadata sufficient for the runner to record:

- transport_attempt_count for that round
- transport_retry_count for that round
- retry error classes/messages, sanitized
- HTTP status if applicable
- observed model
- finish_reason
- provider usage fields if returned
- presence/length of `message.content`
- presence/length of provider reasoning field if present, without storing hidden reasoning text

Do NOT persist or expose hidden chain-of-thought/reasoning content.

Only record:
- whether a reasoning field exists;
- character/token counts if available.

Do not log full request prompts.

---

# H2 — Empty-final technical diagnostics

The same first measured case produced an empty visible final twice across independent runs.

We need to know whether that is:
- finish_reason = length;
- reasoning budget exhaustion;
- content-null response shape;
- provider anomaly;
- another technical condition.

Modify runner/controller technical metadata so every attempt records:

- rounds
- final finish_reason
- substantive true/false
- per-round:
  - observed model
  - finish_reason
  - transport_attempt_count
  - transport_retry_count
  - content_present
  - content_length
  - reasoning_present
  - reasoning_length/count only, not text
  - usage summary if non-secret
- final visible content remains verbatim only when substantive
- no hidden reasoning text stored

For an empty final:
- metadata must preserve the technical diagnostics before the result object is discarded for retry.

Do not infer model quality from empty output.

---

# H3 — Raise fixed output budget to 16,000

The reference-selection phase already found 2,000 output tokens could be consumed by model reasoning with no visible answer.

Measured runs then observed empty final responses even at 8,000.

This is technical evidence that 8,000 may still be an insufficient output/reasoning budget for this reasoning model.

Change the fixed global setting:

`max_tokens = 16000`

Keep:
- temperature = 0
- no top_p/penalty
- identical 16,000 budget for every round/every case
- no adaptive per-case budget

Before accepting this change, synthetic provider preflight must prove:
- endpoint accepts 16,000;
- observed model remains `deepseek-v4-pro`;
- visible response returns normally;
- tool-calling still works.

If provider rejects 16,000, STOP with:
`BLOCKED_OUTPUT_BUDGET_CAPABILITY`

Do NOT silently choose another number.

---

# H4 — Generic run-id naming

Measured run IDs must no longer embed a stale `attempt2` prefix.

Change future generated measured run_id prefix to:

`phasec-<UTC timestamp>-<arming-short-sha>`

This is evidence hygiene only.

No semantic effect.

---

# H5 — Synthetic diagnostics only

Build synthetic PRE10 probes; no E10 payload may be sent.

## H5.1 Complex full-Agent synthetic probe

Run the real frozen:
- Agent system prompt
- AUTO mode
- SUT read tool

with a newly invented synthetic architecture scenario that is NOT an E10 case and does not reproduce an E10 title/facts.

It must require:
- evidence vs assumption separation;
- at least several knowledge-file reads;
- minimum correction;
- explicit uncertainty;
- no framework-default rewrite.

Goal:
- exercise realistic progressive disclosure;
- verify max_tokens 16000;
- inspect finish_reason/content/reasoning metadata;
- verify no empty final.

Run this complex synthetic probe exactly 3 independent times with fresh contexts.

All 3 must produce non-empty visible final output.

Do not tune the prompt between runs.

## H5.2 Transport soak

Using fixed LOCAL_PROXY:
`http://127.0.0.1:7897`

run 10 synthetic readiness/provider calls using the hardened provider.

Requirements:
- no model identity drift;
- all return a usable response after the provider-level retry policy;
- record how many required transport retries;
- do not fail merely because one transient retry occurred if the request recovered within the fixed provider-round policy.

Space calls by at least 5 seconds.

If any call exhausts all 3 transport attempts:
- status = `HOLD_TRANSPORT_UNSTABLE`
- no E10 authorized.

## H5.3 Tool-loop probe

At least one synthetic probe must:
- call `read_sut_file("00_ROUTER.md")`
- complete tool round(s)
- return a visible final answer
- record per-round transport metadata

---

# H6 — Deterministic tests

Update selftests/integration tests to cover:

1. retryable transport error succeeds on attempt 2;
2. retryable errors exhaust all 3 transport attempts and fail;
3. non-retryable HTTP 403 fails immediately;
4. model drift fails immediately;
5. retry uses byte-identical request body;
6. no provider fallback;
7. technical retry metadata recorded;
8. empty-final diagnostics preserved before case-level retry;
9. max_tokens != 16000 rejected;
10. temperature != 0 rejected;
11. no reasoning text stored;
12. reasoning presence/length only;
13. measured run_id uses `phasec-` prefix;
14. existing lock/atomic/reconciliation/duplicate tests remain green.

No network in deterministic selftests.

---

# H7 — Workspace hygiene

Use:

`PYTHONDONTWRITEBYTECODE=1`

and `python -B`.

Do not create repo-local `__pycache__`.

After each deterministic test, Git status must show only the intended tracked edits.

---

# H8 — Preflight report

Update `PREFLIGHT.md` with a new runtime-hardening section:

- starting arming SHA
- output budget 16000
- transport retry policy
- retryable/non-retryable classes
- technical diagnostic fields
- hidden reasoning storage policy = NEVER STORE TEXT
- deterministic test results
- complex synthetic 3/3 result
- transport soak 10/10 result
- count of recovered transient retries
- tool-loop result
- model identity result
- LOCAL_PROXY route
- no E10 execution
- no private eval access
- recommendation:
  - `READY_FOR_ATTEMPT4`
  - `HOLD_TRANSPORT_UNSTABLE`
  - `BLOCKED_OUTPUT_BUDGET_CAPABILITY`
  - `HOLD_NEW_DEFECT`

## No measured run in this task

Do NOT invoke `run-suite`.

`E10_EXECUTION_COUNT: 0`

---

# Mechanical validation

Before return:

1. starting HEAD exactly `c78b8cdd0eb88647170d10256d5139bd6c6a502e`;
2. diff only the five authorized harness files;
3. no run evidence directory created;
4. no PUBLIC/SUT/Agent file changed;
5. no private eval artifact read/added;
6. no Kimi/Moonshot fallback;
7. temperature 0 globally fixed;
8. max_tokens 16000 globally fixed;
9. transport retry fixed 3 attempts / 1s + 3s;
10. compile checks pass;
11. deterministic selftests pass;
12. integration-selftests pass;
13. complex synthetic probe 3/3 non-empty;
14. transport soak 10/10 usable;
15. tool-loop probe passes;
16. no hidden reasoning text in tracked/test output;
17. no secret in diff;
18. no E10 provider call;
19. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. hardening status
4. transport retry policy
5. max_tokens result
6. complex synthetic probe 3/3 result
7. transport soak 10/10 result + recovered retry count
8. tool-loop result
9. empty-final diagnostics result
10. reasoning-metadata policy result
11. deterministic selftest result
12. integration-selftest result
13. model-identity result
14. run-id hygiene result
15. E10 execution count
16. changed-files list
17. mechanical validation
18. exact blocker if not READY_FOR_ATTEMPT4
