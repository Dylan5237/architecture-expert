# Stage 10 Transport Characterization — Isolate OpenCode Zen Complex-Request Failure

## Role

You are the **Stage 10 Transport Characterization Engineer** for `Dylan5237/architecture-expert`.

The hardening branch at:

`d6f1716f34623aecf97eb80c225c282e78748cf7`

proved:

- simple readiness soak: 10/10 usable;
- simple tool-loop: PASS;
- max_tokens 16000 capability: PASS;
- complex full-Agent synthetic probe: 0/3 usable, all exhausted transport retries with TLS EOF before a model response.

This is now a repeatable workload-sensitive failure pattern.

Your task is to isolate which dimension is responsible:

- local proxy route;
- request-body size / prompt shape;
- long inference / non-streaming idle behavior;
- tool-call shape;
- provider gateway behavior.

Do NOT run E10.
Do NOT read private oracle/rubric/coverage/design-report artifacts.
Do NOT score Agent quality.
Do NOT change the frozen Agent/SUT/PUBLIC pack.

## Work branch

Use only:

`eval/stage10-transport-characterization`

Starting HEAD:

`d6f1716f34623aecf97eb80c225c282e78748cf7`

Dedicated clean worktree only.

Read this task from:

`origin/main:tasks/stage10/CODEX_TRANSPORT_CHARACTERIZATION.md`

Do not merge main.

## Fixed provider/model

- Provider: OpenCode Zen
- Host: `https://opencode.ai/zen/go/v1`
- Model: `deepseek-v4-pro`

Do not test Kimi/Moonshot.
Do not switch provider/model in this task.

## Output

Create only:

`reports/STAGE10_TRANSPORT_CHARACTERIZATION.md`

No harness code changes in this task.

All probe scripts must stay outside the repo or be ephemeral.

No run evidence directory.

## Secret policy

Use runtime credentials only.

Never print or commit:
- API key
- Authorization header
- proxy credentials

The local proxy route contains no secret:
`http://127.0.0.1:7897`

## Test principle

This is not another “soak and hope” test.

Use controlled A/B probes to isolate one variable at a time.

Every probe must be synthetic PRE10 material.

No E10 title, facts, expected answer, or mechanism may be reused.

Record:
- route;
- request-byte size;
- stream/non-stream;
- tools yes/no;
- system-prompt shape;
- max_tokens;
- elapsed time to first byte or failure;
- transport attempt count;
- HTTP status if any;
- model identity if any;
- finish_reason if any;
- visible content present/length;
- technical error class.

Never store hidden reasoning text.

---

# Phase 1 — Route isolation

Use the same synthetic complex full-Agent scenario from the hardening preflight or a semantically equivalent newly invented PRE10 scenario.

Run it:

### R1 — LOCAL_PROXY
`http://127.0.0.1:7897`

3 independent fresh requests.

### R2 — DIRECT

3 independent fresh requests with proxy environment explicitly removed and a direct opener.

No route fallback.

For both:
- non-streaming;
- full frozen Agent system prompt + AUTO mode;
- exact same synthetic scenario;
- tools enabled;
- max_tokens 16000;
- temperature 0.

Decision signal:

- proxy fails / direct passes -> local proxy implicated;
- both fail -> provider/non-streaming/complex-workload path implicated;
- both pass -> instability is intermittent; continue matrix anyway.

Do not stop after one success/failure.

---

# Phase 2 — Request-shape matrix

Use whichever route is more stable from Phase 1. If neither is stable, run this phase on both routes but keep repeat count to 2 per cell.

Construct four synthetic probe classes:

### S1 — Small input / trivial output / no tool
Short system + short user.
Expected short visible response.

### S2 — Large input / trivial output / no tool
Create synthetic filler text so request body is approximately the same byte size as:
- frozen Agent system prompt
- AUTO mode contract
- one medium synthetic case

But instruct only a trivial short response.

Purpose: isolate request-body size.

### S3 — Small input / hard reasoning / no tool
Short system + a difficult synthetic architecture reasoning problem.

Purpose: isolate long inference from prompt size.

### S4 — Full Agent / hard reasoning / tool
Frozen Agent system prompt + AUTO + synthetic architecture problem + `read_sut_file`.

Purpose: reproduce the real failure shape.

Run each class at least twice.

For every call record elapsed time to:
- first response byte if successful;
- failure if unsuccessful.

No prompt tuning between repeats.

---

# Phase 3 — Tool-shape isolation

Using the full frozen Agent system prompt + same synthetic architecture scenario:

- T1: no tools exposed
- T2: `read_sut_file` exposed, but user scenario can be solved without requiring it
- T3: `read_sut_file` exposed and synthetic instruction requires reading `00_ROUTER.md`

Two repeats each on the chosen route.

Purpose:
determine whether tool schema/tool-call round materially correlates with transport failure.

---

# Phase 4 — max_tokens reservation check

The earlier failures occurred at both 8000 and 16000 in different runs, but characterize this directly.

Using the same full-Agent hard synthetic request, non-streaming:

- 4000
- 8000
- 16000

Two repeats each.

Do not use adaptive retries to improve quality; transport retry may be the fixed 3-attempt policy from the hardening branch.

Record whether failure probability/time changes with the requested output budget.

This is diagnostics only; do not change the frozen future setting in this task.

---

# Phase 5 — Streaming diagnostic

This phase is critical.

Use the exact same full-Agent hard synthetic scenario.

Probe OpenAI-compatible chat-completions with:

`stream=true`

Do NOT modify tracked harness.

Use an ephemeral diagnostic client capable of parsing SSE enough to establish:

- HTTP connection accepted;
- first SSE event time;
- model identity if surfaced;
- finish_reason;
- tool-call deltas if surfaced;
- visible content completion.

Never store hidden reasoning text.

Run:

- STREAM / LOCAL_PROXY: 3 independent runs
- STREAM / DIRECT: 3 independent runs, unless Phase 1 proves DIRECT unusable before request acceptance

Use max_tokens 16000.

Important:
the streaming diagnostic may assemble visible content/tool-call arguments in memory for validation, but do not commit full probe outputs.

Decision signal:

- streaming succeeds while equivalent non-streaming fails -> likely non-streaming idle/gateway transport problem; recommend implementing streaming adapter;
- streaming and non-streaming both fail -> transport/provider complex-workload path remains unsuitable;
- only one route works -> route-specific problem.

---

# Phase 6 — Lightweight alternate HTTP client cross-check

To rule out a Python `urllib` implementation artifact, run a very small cross-check for the full-Agent hard synthetic request using one independent HTTP stack already available locally, for example:

- curl; or
- Python `httpx` / `requests` if already installed.

Do NOT install large dependencies solely for this.

Use the same route/model/settings.

At least 2 runs.

No repo code changes.

If the alternate client consistently succeeds while urllib fails, identify `urllib/proxy stack` as the primary suspect.

If both fail similarly, do not blame urllib.

---

# Classification

Return exactly one primary classification:

- `LOCAL_PROXY_PATH_DEFECT`
- `NON_STREAMING_IDLE_PATH_DEFECT`
- `URLLIB_TRANSPORT_DEFECT`
- `PROVIDER_COMPLEX_REQUEST_DEFECT`
- `INTERMITTENT_TRANSPORT_NOT_ISOLATED`
- `NO_DEFECT_REPRODUCED`

You may include secondary contributing factors.

Do not claim a root cause unless the matrix distinguishes it.

## Recommendation states

Return exactly one:

- `IMPLEMENT_STREAMING_ADAPTER`
- `USE_DIRECT_ROUTE`
- `CHANGE_HTTP_CLIENT`
- `RETIRE_OPENCODE_ZEN_REFERENCE_TRANSPORT`
- `REPEAT_CHARACTERIZATION_LATER`
- `READY_WITH_EXISTING_TRANSPORT`

The recommendation must follow the observed matrix, not preference.

## Report requirements

`reports/STAGE10_TRANSPORT_CHARACTERIZATION.md` must contain:

1. starting SHA
2. provider/model
3. route definitions
4. exact synthetic probe classes
5. Phase 1 route matrix
6. Phase 2 request-shape matrix
7. Phase 3 tool-shape matrix
8. Phase 4 max_tokens matrix
9. Phase 5 streaming matrix
10. Phase 6 alternate-client cross-check
11. latency-to-first-byte/failure observations
12. transport-error taxonomy observed
13. model identity observations
14. hidden reasoning policy confirmation
15. primary classification
16. confidence and unresolved uncertainty
17. recommendation
18. whether OpenCode Zen remains viable for Stage 10
19. `E10_EXECUTION_COUNT: 0`
20. no-private-eval confirmation
21. secret-handling result

## Mechanical validation

Before return:

1. starting HEAD exactly `d6f1716f34623aecf97eb80c225c282e78748cf7`;
2. diff contains only `reports/STAGE10_TRANSPORT_CHARACTERIZATION.md`;
3. no harness code changed;
4. no run directory created;
5. no E10 provider call;
6. no private eval read;
7. no secret in diff;
8. no Kimi/Moonshot;
9. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. classification
4. recommendation
5. Phase 1 route result
6. Phase 2 request-shape result
7. Phase 3 tool-shape result
8. Phase 4 max_tokens result
9. Phase 5 streaming result
10. Phase 6 alternate-client result
11. most important latency/failure observation
12. OpenCode Zen viability conclusion
13. E10 execution count
14. changed-files list
15. mechanical validation
16. exact unresolved uncertainty
