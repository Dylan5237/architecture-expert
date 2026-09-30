# Stage 10 Attempt #5 — Minimal 429 Capacity Handling + Full Rerun

## Role

You are the Stage 10 final measured-run executor for `Dylan5237/architecture-expert`.

Attempt #4 proved the frozen runtime itself is now usable:

- final runtime freeze PASS;
- E10-001..007 completed cleanly;
- 40 successful provider rounds, all `deepseek-v4-pro`;
- zero transport retries;
- all seven finals substantive;
- failure occurred only when E10-008 received HTTP 429 twice.

This task must NOT reopen transport research.

Goal:

1. make one minimal 429-capacity patch;
2. run deterministic checks + one live readiness/capacity check;
3. immediately execute one fresh full Attempt #5;
4. preserve evidence and stop.

Do not resume Attempt #4 outputs.
Do not mix runs.
Do not read private oracle.
Do not score.

## Work branch

Use only:

`eval/stage10-429-capacity-attempt5`

Starting HEAD:

`9f361246c4a877b22ca338721b1dffe5130c0813`

Dedicated clean worktree.

Read this task from:

`origin/main:tasks/stage10/CODEX_429_CAPACITY_AND_ATTEMPT5.md`

Do not merge main.

## Frozen semantics

Keep unchanged:

- SUT `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- suite `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC pack `23a49382c949702446325d30e18d3321d8550c36`
- OpenCode Zen Go
- `https://opencode.ai/zen/go/v1`
- `deepseek-v4-pro`
- httpx 0.28.1
- DIRECT / trust_env=False / no proxy / no redirects
- timeout 30/360/30/30
- temperature 0
- max_tokens 32000
- max_tool_rounds 24
- system/mode/user/tool/SUT/path-sandbox semantics
- case-level retry maximum = one
- duplicate HOLD
- hidden reasoning text never persisted
- no provider/model fallback
- no Kimi/Moonshot

## Authorized tracked changes

Only:

- `eval/stage10/harness/provider_openai_compatible.py`
- `eval/stage10/harness/controller.py`
- `eval/stage10/harness/PREFLIGHT.md`
- `eval/stage10/harness/README.md`

No runner change unless mechanically required for metadata propagation only.

After the run, allow canonical `eval/stage10/run/**` evidence only.

---

# A — Minimal 429 policy

Current behavior fails 429 immediately, causing the case-level retry to occur seconds later. That is ineffective for a rate/capacity response.

Do not classify 429 as a transport error.

Implement a separate fixed 429 capacity wait inside one provider round:

- maximum 3 total HTTP-429 attempts for the same application request;
- same byte-identical body/messages/model/settings/session;
- if response has a valid `Retry-After`:
  - use it;
  - support integer seconds;
  - support HTTP-date if straightforward;
- if no valid Retry-After:
  - wait 60 seconds before attempt 2;
  - wait 120 seconds before attempt 3;
- cap any single Retry-After wait at 600 seconds;
- if Retry-After exceeds 600 seconds, fail closed instead of sleeping longer;
- after the third 429, fail closed.

Existing transport retry policy remains independent and unchanged.

Do not retry:
- 400/401/403;
- other 4xx;
- HTTP 500;
- malformed JSON;
- model drift;
- semantic errors.

## Metadata

Record only technical data:

- `rate_limit_attempt_count`
- `rate_limit_retry_count`
- `rate_limit_wait_seconds`
- sanitized `retry_after_seconds` if present
- terminal HTTP status

No response body required.
No secret headers.

---

# B — Deterministic checks only

Update provider-free tests for:

1. 429 + Retry-After=1 -> waits 1 and succeeds;
2. 429 without header -> fixed 60s policy (mock sleep; do not actually sleep);
3. repeated 429 exhausts after 3;
4. Retry-After >600 -> fail closed;
5. 429 reuses byte-identical request body;
6. 429 does not change provider/model/settings/session;
7. existing transport retry tests remain green;
8. HTTP 403/500 remain immediate fail;
9. max_tokens remains 32000;
10. existing controller/integration tests remain green.

Use mocked sleep in deterministic tests.

No new characterization matrix.

---

# C — Pre-run gate

Use `PYTHONDONTWRITEBYTECODE=1` and `python -B`.

Run:

1. in-memory compile;
2. controller selftest;
3. integration-selftest;
4. public-dry-run;
5. exactly one live readiness call.

Also call the existing usage endpoint once if available.

Record the non-secret usage status/percentages only.

If readiness itself returns 429 and the bounded 429 policy cannot recover, do not run E10.

No repeated soak.

If all pass, create exactly one capacity-patch/freeze commit.

No further code changes after that commit.

---

# D — Attempt #5

On the exact capacity-patch freeze SHA:

`STAGE10_MEASURED_AUTH_SHA=<freeze SHA>`

Verify:
- HEAD exact;
- tracked worktree clean;
- no `eval/stage10/run/`.

Execute exactly once:

`python -B controller.py run-suite`

No second invocation.
No manual reruns.
No resume.
No output-quality inspection.
No private oracle.
No code patch during run.

---

# E — Terminal handling

If COMPLETE:
- require 32 raw + metadata.json + RUN_STATUS.md = 34 canonical run files;
- reconcile all SHA values;
- require exact E10-001..032;
- no duplicates;
- model identity intact;
- max_tokens 32000;
- preserve any recovered 429 waits in metadata.

If PARTIAL/HOLD:
- preserve exactly controller output;
- do not rerun in this task.

Create one evidence commit after the run.
Push normally.
Do not amend or force.

---

# Return format

Return only:

1. branch
2. capacity-freeze SHA
3. evidence SHA
4. run state
5. deterministic gate result
6. readiness + usage result
7. 429 policy summary
8. measured run_id
9. completed case count
10. cases that encountered 429 + wait/recovery result
11. case-level technical retries
12. terminal technical errors
13. model identity result
14. raw inventory
15. duplicate-content result
16. reconciliation result
17. changed-files summary
18. secret scan
19. mechanical validation
20. exact blocker if not COMPLETE

If pre-run fails:
- evidence SHA = NONE
- E10 execution count = 0
- exact blocker.
