# Stage 10 HTTPX Sequential Qualification — Match Measured Lifecycle and Qualify Output Budget

## Role

You are the **Stage 10 Runtime Qualification Engineer** for `Dylan5237/architecture-expert`.

Chief Architect reviewed the httpx migration at:

`eval/stage10-httpx-transport@ed70a80c034198f62a480bbf346a41fac11f84bc`

Accepted:
- urllib was replaced by httpx 0.28.1;
- DIRECT / trust_env=False / no proxy / no redirects;
- timeouts 30/360/30/30;
- narrow transport retry;
- deterministic tests and integration tests pass;
- readiness 10/10;
- complex full-Agent synthetic 5/5 non-empty;
- E10 execution count remains 0.

Two unresolved validity issues prevent Attempt #4:

1. required tool-loop gate = 0/3;
2. 3/5 complex full-Agent finals ended with `finish_reason=length` at max_tokens=16000.

The first migration preflight also ran full-Agent synthetic conversations with concurrency up to 2 and a fresh provider/client per conversation, while the actual measured controller executes cases **sequentially** through **one persistent ReferenceProvider/httpx.Client**.

Therefore this task does not change harness code. It re-qualifies the runtime using the same lifecycle as the measured suite and separately characterizes whether 16000 is an evaluation-distorting output cap.

Do NOT run E10.
Do NOT read private oracle/rubric/coverage/design-report artifacts.
Do NOT score Agent quality.
Do NOT modify Agent/SUT/PUBLIC content.

## Work branch

Use only:

`eval/stage10-httpx-sequential-qualification`

Starting HEAD:

`ed70a80c034198f62a480bbf346a41fac11f84bc`

Dedicated clean worktree only.

Read this task from:

`origin/main:tasks/stage10/CODEX_HTTPX_SEQUENTIAL_QUALIFICATION.md`

Do not merge main.

## Output

Create only:

`reports/STAGE10_HTTPX_SEQUENTIAL_QUALIFICATION.md`

No harness code changes.
No requirements changes.
No run evidence directory.

All diagnostic drivers must remain ephemeral/outside the repo.

---

# Part 1 — Reproduce actual measured provider lifecycle

The measured controller constructs one `ReferenceProvider` and reuses it sequentially across the suite.

Your formal qualification must therefore use:

- one persistent `ReferenceProvider`;
- one persistent underlying httpx.Client;
- conversations executed sequentially;
- no parallel threads/tasks/processes;
- fresh `CaseRunner` / messages / PathSandbox state per synthetic conversation;
- same DIRECT route;
- same 30/360/30/30 timeouts;
- same transport retry policy;
- temperature=0;
- initial max_tokens=16000;
- max_tool_rounds=24.

Do not create a fresh provider/client between formal sequential conversations unless a specific subtest explicitly says so.

## Part 1A — Sequential readiness

Run 5 synthetic readiness conversations sequentially through the one shared provider.

Wait at least 5 seconds between conversation starts.

Require:
- 5/5 usable;
- no model drift;
- record transport retries.

## Part 1B — Sequential complex full-Agent

Use the exact frozen system prompt and AUTO mode.

Use one newly invented PRE10 architecture scenario, fixed across all repeats.

Run 3 conversations sequentially through the same provider/client.

Scenario requirements:
- multiple architecture dimensions;
- evidence vs assumption;
- minimum correction;
- explicit uncertainty;
- tool available but not required.

Record:
- total conversation elapsed;
- provider rounds;
- finish_reason;
- visible final length;
- prompt/completion/reasoning token usage if available;
- transport attempts/retries;
- whether final is `stop`, `length`, or other.

No prompt tuning.

## Part 1C — Sequential required tool-loop

Use the same system/AUTO and same synthetic scenario, but require:

1. read `00_ROUTER.md`;
2. read at least one related knowledge file selected by the Agent;
3. then return final visible analysis.

Run **5 conversations sequentially** through the same persistent provider/client.

Wait at least 10 seconds between conversation starts.

No concurrency.

Formal success for a conversation requires:
- required `00_ROUTER.md` read occurred;
- at least one additional allowed knowledge read occurred;
- final visible content is non-empty;
- no terminal transport failure;
- model identity stable.

Record the exact round at which transport failure occurs if any.

Do not persist full model answers or tool-return content in the report.

---

# Part 2 — Fresh-client cross-check

To determine whether persistent connection-pool state contributes to failure, repeat the required tool-loop probe **3 times**, but this time:

- create a new `ReferenceProvider` / httpx.Client per conversation;
- still run strictly sequentially;
- close each provider before starting the next;
- same scenario and settings;
- no concurrency.

Compare with Part 1C.

Classification signal:
- shared-client fails, fresh-client passes -> persistent pool/lifecycle issue;
- both pass -> prior 0/3 was likely concurrency/intermittent transport;
- both fail similarly -> provider/tool-loop transport remains unstable.

---

# Part 3 — ConnectError cause-chain characterization

For any `httpx.ConnectError` occurring in this task, capture only sanitized structural diagnostics:

- exception class;
- bounded cause/context chain class names;
- errno values if present;
- whether an SSL exception class appears;
- whether certificate verification failure appears;
- whether DNS/gaierror appears;
- whether connection refused/reset/aborted appears.

Do NOT store free-form exception text if it may contain sensitive route details.
Do NOT store request headers.

If no ConnectError occurs, record NONE.

This is diagnostic only; do not change retry classification.

---

# Part 4 — Output-budget qualification

The migration preflight had 3/5 complex finals end with `finish_reason=length`, with completion_tokens approximately 16000 and substantial reasoning-token use.

A truncated final is not acceptable as clean evaluation evidence unless we establish that 16000 is sufficient for the target workload.

Use an ephemeral httpx diagnostic client that preserves all frozen semantics except max_tokens for this characterization.

Test:

- 16000
- 24000
- 32000

For each budget:

## Part 4A — Complex no-required-tool
Run 2 fresh sequential conversations.

## Part 4B — Required tool-loop
Run 2 fresh sequential conversations.

Use:
- same DIRECT route;
- same timeouts;
- same retry policy;
- exact frozen system/AUTO;
- same fixed synthetic scenario;
- no concurrency.

Do not adapt the prompt between budgets.

### Budget qualification criteria

For each successful final record:
- finish_reason;
- completion_tokens;
- reasoning token count if available;
- visible final length;
- total prompt tokens on final round;
- transport retries.

A budget is considered **cleanly qualified** only if all 4 conversations at that budget:
- complete with non-empty visible final;
- have no terminal transport failure;
- finish with `stop` rather than `length`;
- have no model drift.

If provider rejects a budget or context limit prevents completion, record that exactly.

Do not alter the tracked harness in this task.

---

# Part 5 — Interpretation rules

Return one runtime-lifecycle classification:

- `CONCURRENCY_PREFLIGHT_ARTIFACT`
- `PERSISTENT_CLIENT_POOL_DEFECT`
- `TOOL_LOOP_TRANSPORT_UNSTABLE`
- `INTERMITTENT_TRANSPORT_NOT_ISOLATED`
- `SEQUENTIAL_RUNTIME_STABLE`

Return one output-budget classification:

- `16000_SUFFICIENT`
- `16000_TRUNCATES_24000_SUFFICIENT`
- `16000_24000_TRUNCATE_32000_SUFFICIENT`
- `NO_TESTED_BUDGET_CLEANLY_QUALIFIED`
- `PROVIDER_REJECTS_HIGHER_BUDGET`

Do not choose a classification not supported by the matrix.

## Recommendation

Return exactly one:

- `READY_TO_HARDEN_24000`
- `READY_TO_HARDEN_32000`
- `KEEP_16000_AND_PREPARE_ATTEMPT4`
- `HARDEN_CLIENT_LIFECYCLE`
- `HARDEN_TRANSPORT_RETRY`
- `RETIRE_OPENCODE_ZEN_REFERENCE_TRANSPORT`
- `REPEAT_QUALIFICATION_LATER`

Attempt #4 remains unauthorized in this task.

---

# Report requirements

`reports/STAGE10_HTTPX_SEQUENTIAL_QUALIFICATION.md` must contain:

1. starting SHA
2. migration SHA
3. frozen provider/model/route/timeouts/retry
4. shared-provider measured-lifecycle definition
5. Part 1A readiness matrix
6. Part 1B complex sequential matrix
7. Part 1C required tool-loop sequential matrix
8. Part 2 fresh-client matrix
9. Part 3 sanitized ConnectError cause-chain findings
10. Part 4 budget matrices for 16000/24000/32000
11. finish_reason distribution
12. token-budget observations
13. transport retry observations
14. model identity result
15. runtime-lifecycle classification
16. output-budget classification
17. recommendation
18. residual uncertainty
19. `E10_EXECUTION_COUNT: 0`
20. no-private-eval confirmation
21. secret-handling result

## Mechanical validation

Before return:

1. starting HEAD exactly `ed70a80c034198f62a480bbf346a41fac11f84bc`;
2. diff contains only `reports/STAGE10_HTTPX_SEQUENTIAL_QUALIFICATION.md`;
3. no harness/requirements changes;
4. no run directory;
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
3. runtime-lifecycle classification
4. output-budget classification
5. recommendation
6. shared-provider readiness 5/5 result
7. shared-provider complex 3/3 result
8. shared-provider tool-loop 5/5 result
9. fresh-provider tool-loop 3/3 result
10. ConnectError cause-chain result
11. 16000 budget result
12. 24000 budget result
13. 32000 budget result
14. finish_reason distribution
15. transport retry summary
16. model identity result
17. E10 execution count
18. changed-files list
19. mechanical validation
20. exact residual uncertainty
