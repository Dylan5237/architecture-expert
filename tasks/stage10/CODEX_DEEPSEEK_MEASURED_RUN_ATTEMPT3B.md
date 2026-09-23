# Stage 10 Phase C Attempt #3B — Clean Workspace Restart, No Code Changes

## Role

You are the **Stage 10 Measured Reference Run Controller** for `Dylan5237/architecture-expert`.

Attempt #3 never started. It was blocked before `run-suite` because Python cache files made the local worktree non-clean and the execution environment refused deletion.

This is **not** a harness defect and **not** an Agent result.

Attempt #3B restarts from the same frozen arming SHA in a brand-new clean branch/worktree and must avoid generating repository-local bytecode caches before measured execution.

Do NOT modify tracked code.
Do NOT read private oracle/rubric/coverage/design-report artifacts.
Do NOT inspect prior Attempt #2/#3 raw outputs.
Do NOT use Kimi/Moonshot.

## Clean branch

Work only on:

`eval/stage10-deepseek-runner-attempt3b`

Starting HEAD:

`c78b8cdd0eb88647170d10256d5139bd6c6a502e`

Create a fresh dedicated worktree/clone for this branch.

The first command after entering it must confirm:

`git status --porcelain`

returns empty.

If not empty, STOP with `BLOCKED_PRE_RUN_CLEANLINESS`.

Do not delete files to force cleanliness; use a new clean workspace instead.

## Frozen execution contract

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

Network route:
- fixed `LOCAL_PROXY`
- `127.0.0.1:7897`
- use the same proxy environment for all readiness calls and the measured run
- no route switching after soak begins

If the proxy is unavailable, STOP before E10 with `BLOCKED_NETWORK_ROUTE`.

## No-bytecode-cache pre-run rule

Before any Python command, set for the whole shell/process environment:

`PYTHONDONTWRITEBYTECODE=1`

Run Python commands with `python -B` where applicable.

Do NOT use `python -m py_compile`, because it can create `__pycache__` / `.pyc`.

For syntax validation, use an in-memory compile check such as:

`python -B -c "from pathlib import Path; [compile(Path(p).read_text(encoding='utf-8'), p, 'exec') for p in [...]]"`

covering:
- provider_openai_compatible.py
- runner.py
- controller.py

After EACH deterministic pre-run command, run:

`git status --porcelain`

It must remain empty.

If any untracked/tracked file appears before measured execution, STOP. Do not delete it in-place.

## Deterministic pre-run gates

On exact clean HEAD:

1. in-memory syntax compile;
2. `python -B controller.py selftest`;
3. `python -B controller.py integration-selftest`;
4. `python -B controller.py public-dry-run`.

All must PASS.

After each, verify clean Git status.

Require:
- E10 IDs 001..032 complete;
- requested_mode parsing 32/32;
- `eval/stage10/run/` absent;
- no E10 provider call yet.

## Network stability soak

Using the fixed LOCAL_PROXY route, run:

`python -B controller.py readiness`

exactly 3 times, at least 10 seconds between starts.

All 3 must PASS.

After each readiness call:
- verify requested=observed=`deepseek-v4-pro`;
- verify temperature=0/max_tokens=8000;
- verify no connection reset/refused/disconnect;
- verify `git status --porcelain` still empty.

If any readiness fails or workspace becomes dirty:
- do not run E10;
- return the corresponding blocker.

## Measured authorization

Set only for the measured process:

`STAGE10_MEASURED_AUTH_SHA=c78b8cdd0eb88647170d10256d5139bd6c6a502e`

Immediately before measured execution verify again:

- HEAD equals arming SHA;
- Git status empty;
- `eval/stage10/run/` absent;
- proxy route unchanged.

## Measured execution

Execute exactly once:

`python -B controller.py run-suite`

No second invocation.
No manual parallelism.
No resume.
No case-level manual rerun.
No code edits.

The tracked controller owns retries and terminal state.

## Post-run

Accept the controller terminal state as produced.

For COMPLETE require:
- 32 raw files;
- metadata.json;
- RUN_STATUS.md;
- exactly 34 run files;
- SHA reconciliation passes;
- no duplicates;
- observed model integrity passes.

For HOLD/PARTIAL, preserve exactly the evidence produced.

Do not inspect output quality.

## Evidence commit

Create exactly one evidence commit after the measured command terminates.

Do not amend arming history.
Do not force-push.

Push branch and stop.

## Return format

Return only:

1. branch
2. starting arming SHA
3. final evidence SHA
4. run state
5. initial clean-workspace result
6. no-bytecode-cache result
7. network route
8. deterministic pre-run gates
9. 3x readiness soak
10. measured run_id
11. completed case count
12. technical retry count + case IDs
13. technical error cases
14. observed-model integrity
15. raw inventory
16. duplicate-content result
17. reconciliation result
18. changed-files summary
19. secret scan
20. mechanical validation
21. exact blocker if not COMPLETE
