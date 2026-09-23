# Stage 10 Phase C Attempt #3 — Clean Full Measured Rerun on Frozen DeepSeek Harness

## Role

You are the **Stage 10 Measured Reference Run Controller** for `Dylan5237/architecture-expert`.

Attempt #2 ended as a legitimate:

`PARTIAL_TECHNICAL_FAILURE`

because of a transient transport outage during E10-003.

The prior two raw outputs (E10-001/E10-002) are preserved as technical evidence only. They MUST NOT be reused, copied, resumed, or mixed into Attempt #3.

Attempt #3 is a completely fresh full-suite rerun from the same frozen arming harness.

Do NOT modify harness code.
Do NOT read private oracle/rubric/coverage/design-report artifacts.
Do NOT score anything.
Do NOT inspect Attempt #2 raw outputs.

## Clean branch

Work only on:

`eval/stage10-deepseek-runner-attempt3`

Starting HEAD:

`c78b8cdd0eb88647170d10256d5139bd6c6a502e`

This branch was created directly from the accepted arming SHA and contains NO measured run evidence.

Use a dedicated worktree or single-branch clone.

Do not inspect or repair:
- `eval/stage10-deepseek-runner`
- historical Kimi branches
- suite-design/private-eval branches
- any other local checkout

Read this task from:

`origin/main:tasks/stage10/CODEX_DEEPSEEK_MEASURED_RUN_ATTEMPT3.md`

Do not merge main.

## Fixed frozen inputs

SUT:
`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Suite:
`ff157eb1947860345a305fb29452b51e09dd3a2b`

PUBLIC pack:
`23a49382c949702446325d30e18d3321d8550c36`

Harness/arming SHA:
`c78b8cdd0eb88647170d10256d5139bd6c6a502e`

Provider/model:
- OpenCode Zen
- `https://opencode.ai/zen/go/v1`
- `deepseek-v4-pro`

Generation:
- temperature = 0
- max_tokens = 8000
- max_tool_rounds = 24

Kimi/Moonshot remains prohibited.

## Attempt #2 disposition

Attempt #2 evidence is frozen at:

`c255b9dc45adeb806db17e27558a1ead7d96a8a8`

Do NOT read its raw outputs.

Chief Architect classification:

- the two successful raw outputs are individually intact;
- the suite is incomplete;
- Phase D scoring will NOT mix Attempt #2 and Attempt #3 outputs;
- Attempt #2 remains runtime/transport evidence only.

## No-code-change rule

Attempt #3 must run the EXACT arming code at:

`c78b8cdd0eb88647170d10256d5139bd6c6a502e`

Before any model call verify:
- current HEAD exactly equals arming SHA;
- working tree clean;
- controller/runner/provider files unchanged.

If any code change appears necessary, STOP with:

`HOLD_NEW_DEFECT`

Do not patch and continue.

## Network-route stabilization gate

Attempt #2 failed because the local machine experienced a transient connection failure to OpenCode Zen.

Do NOT change provider/model.

Before measured execution, choose exactly one stable transport route for the entire run:

- DIRECT; or
- LOCAL_PROXY using the user's existing local proxy if discoverable and non-secret.

### Route selection rules

1. Do not use an external/VPN provider other than the user's already-running local network/proxy setup.
2. Do not change route after measured execution begins.
3. Do not silently fall back between DIRECT and PROXY mid-run.
4. Record the chosen route in the final return.
5. Proxy address/port is non-secret and may be recorded; credentials, if any, must not be logged.

If using proxy:
- configure standard runtime proxy environment variables supported by Python/urllib;
- use the same proxy environment for all readiness calls and the measured run;
- verify the provider call actually succeeds under that environment.

If using direct:
- leave proxy variables unset for both soak and measured run.

Do not modify tracked code for transport selection.

## Pre-run deterministic gates

Run on the exact clean arming HEAD:

1. Python compile checks for provider/runner/controller.
2. `python controller.py selftest`
3. `python controller.py integration-selftest`
4. `python controller.py public-dry-run`

All must PASS.

Require:
- 32 PUBLIC IDs E10-001..032;
- all requested_mode values parsed;
- zero E10 provider calls so far;
- `eval/stage10/run/` absent.

## Network stability soak

Before the measured command, run:

`python controller.py readiness`

exactly **3 times** on the chosen transport route.

Requirements:
- all 3 PASS;
- requested model = observed model = `deepseek-v4-pro`;
- temperature 0 / max_tokens 8000;
- no 401/403/connection reset/refused/disconnect;
- space the three readiness calls by at least 10 seconds;
- do not use E10 payloads.

If ANY of the 3 fails:
- do not run E10;
- return `BLOCKED_NETWORK_STABILITY`;
- preserve no measured raw output.

The tracked `run-suite` will still perform its own internal readiness gate after acquiring the run lock.

## Authorization

Set only for the measured process:

`STAGE10_MEASURED_AUTH_SHA=c78b8cdd0eb88647170d10256d5139bd6c6a502e`

No other authorization SHA is valid.

## Measured execution

If all gates pass, execute exactly once:

`python controller.py run-suite`

Do not launch twice.
Do not parallelize.
Do not resume from Attempt #2.
Do not manually rerun any case.

The tracked controller owns:
- single-process lock;
- provider readiness;
- case order;
- technical retry;
- raw writes;
- metadata;
- reconciliation;
- duplicate HOLD.

## During execution

Do NOT:
- inspect output quality;
- alter prompts;
- read private oracle;
- give clarifications/hints;
- edit raw files;
- change provider/model/settings;
- change network route;
- start a second controller;
- patch code.

If the controller stops, accept its terminal state.

## Valid terminal states

### COMPLETE

Expected evidence:
- 32 raw files
- metadata.json
- RUN_STATUS.md

Exactly 34 files.

### HOLD_INTEGRITY_REVIEW

Preserve all evidence.
Do not rerun or score.

### PARTIAL_TECHNICAL_FAILURE

Preserve all evidence.
Do not resume or score.

### BLOCKED_PROVIDER

Zero/partial evidence as produced by tracked controller.
Do not rerun outside the controller.

## Post-run validation

For COMPLETE verify:

1. exactly 32 raw files;
2. exactly 32 metadata case records;
3. exact E10-001..032 1:1 mapping;
4. every raw non-empty;
5. every disk SHA equals metadata SHA;
6. all successful final observed models are `deepseek-v4-pro`;
7. no illegal attempt/retry counts;
8. generation settings fixed;
9. max_tool_rounds = 24;
10. no duplicate raw SHA groups;
11. RUN_STATUS = COMPLETE;
12. no harness/PUBLIC/SUT file changed;
13. no secret in diff.

Do not manually repair reconciliation failures.

## Evidence commit

After terminal state and validation:

- create exactly one final evidence commit;
- do not amend arming history;
- do not force-push;
- push branch;
- stop.

For COMPLETE, diff from arming SHA must be exactly 34 run files.

For HOLD/PARTIAL, commit only the evidence produced by the tracked controller.

## Return format

Return only:

1. branch
2. starting/frozen arming SHA
3. final evidence SHA
4. run state
5. chosen network route
6. provider/model
7. generation settings
8. deterministic pre-run gate result
9. 3x readiness soak result
10. measured run_id
11. completed case count
12. technical retry count + case IDs
13. technical error cases
14. observed-model integrity result
15. raw-output inventory result
16. duplicate-content result
17. reconciliation result
18. changed-files summary
19. secret scan
20. mechanical validation
21. exact blocker/limitation if not COMPLETE

If pre-run network stability fails, return with:
- final evidence SHA = NONE
- state = BLOCKED_NETWORK_STABILITY
- E10 execution count = 0
- exact failed readiness call(s)
