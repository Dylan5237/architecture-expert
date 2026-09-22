# Stage 10 Phase C0-R — Non-Kimi Reference Runner + Controller Preflight

## Role

You are the **Stage 10 Reference Runner Harness Engineer** for `Dylan5237/architecture-expert`.

The reference model has been selected and frozen by Chief Architect:

- Provider: **OpenCode Zen**
- API base: `https://opencode.ai/zen/go/v1`
- Model: **deepseek-v4-pro**
- Transport: OpenAI-compatible chat-completions
- Owner constraint: **Kimi/Moonshot is prohibited**

This task builds and preflights a clean, versioned runner + controller for that reference model.

Do NOT run E10-001..032.
Do NOT read private oracle/rubric/coverage/design-report artifacts.
Do NOT score anything.
Do NOT modify the frozen Agent v0.1 or PUBLIC cases.

## Fixed frozen inputs

Frozen Agent v0.1 SUT:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Frozen suite:

`ff157eb1947860345a305fb29452b51e09dd3a2b`

Frozen PUBLIC pack:

`23a49382c949702446325d30e18d3321d8550c36`

Reference-model selection record:

`reports/STAGE10_REFERENCE_MODEL_SELECTION.md` on `main`

Work branch:

`eval/stage10-deepseek-runner`

Starting HEAD:

`23a49382c949702446325d30e18d3321d8550c36`

Read this task from:

`origin/main:tasks/stage10/CODEX_DEEPSEEK_RUNNER_PREFLIGHT.md`

Do not merge main.

## Hard exclusion

Executable harness/controller code must contain **no Kimi/Moonshot fallback path**.

Forbidden:
- `api.kimi.com`
- Kimi/Moonshot model aliases
- automatic fallback to a Kimi provider config
- provider substitution if OpenCode Zen fails

If OpenCode Zen / deepseek-v4-pro is unavailable, fail closed.

Historical Kimi branches are not evaluation inputs and must not be read for this task.

## Reference provider contract

Required provider/model:

- base URL: `https://opencode.ai/zen/go/v1`
- endpoint: `/chat/completions`
- model: `deepseek-v4-pro`
- expected response model identity: `deepseek-v4-pro`
- `temperature = 0`
- `max_tokens = 8000`
- no top_p/penalty override
- non-secret routing header:
  `x-opencode-session: stage10-ref-<run_id>-<case_id>`

The session header MUST:
- be unique across different cases;
- remain stable across tool-call rounds within the same case;
- contain no secret;
- never carry prior-case content.

Provider credentials may be loaded only at runtime from:
- `STAGE10_API_KEY`; or
- the local OpenCode/OpenCode-Zen provider configuration discovered during reference selection.

Never print/log/commit the key.

## System/custom-instruction mapping

For each case:

1. SYSTEM message 1 = exact bytes/text of frozen `agent/system-prompt-v0.1.md`
2. SYSTEM message 2 = exact selected `agent/modes/<MODE>.md`
3. USER message = exact current PUBLIC case file
4. tool messages only from constrained `read_sut_file`

No IDE/project/user-rule instruction is injected into the evaluated-model request.

If OpenCode Zen rejects dual SYSTEM messages in the actual harness path, do not silently concatenate or change semantics. Return BLOCKED_PROVIDER_CAPABILITY for Chief Architect adjudication.

## Required tracked files

Create only:

- `eval/stage10/harness/README.md`
- `eval/stage10/harness/provider_openai_compatible.py`
- `eval/stage10/harness/runner.py`
- `eval/stage10/harness/controller.py`
- `eval/stage10/harness/PREFLIGHT.md`

Optional only if genuinely necessary:

- `eval/stage10/harness/requirements.txt`

No other tracked file may change.

Prefer Python standard library.

## Runner requirements

### R1 — Exact SUT snapshot

Materialize a temporary snapshot from exactly:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Recommended:

`git archive <SUT_SHA>`

The evaluated model's file tool root must be this snapshot, never the worktree.

Assert required SUT files exist.

### R2 — Fresh context

Every future E10 case creates:
- a brand-new messages list;
- no previous response ID;
- no conversation ID;
- no model-side thread reuse.

No prior case content can be passed to the next case.

### R3 — Single model-visible tool

Expose exactly:

`read_sut_file(path)`

It must:
- accept relative file paths only;
- reject traversal;
- reject absolute paths;
- reject `eval/**`;
- reject `.git/**`;
- reject `tasks/**`;
- read one file only;
- have a per-call byte cap;
- have a per-case aggregate read budget;
- log only path + byte count + allow/deny result.

No web/shell/list/write/git/env model tools.

### R4 — Fixed generation settings

Every model round for the measured suite uses:
- model `deepseek-v4-pro`
- temperature `0`
- max_tokens `8000`

No per-case tuning.

Provider response model identity must be checked on every round if returned.
Any mismatch = provider drift -> stop the run.

### R5 — Exact PUBLIC payload

Future measured case USER content must be the PUBLIC file verbatim.

No paraphrase, hint, hidden rubric, normalization, or appended instruction.

## Versioned controller requirements

The controller is a tracked evaluation-integrity artifact.

### C1 — Atomic single-process lock

Acquire an exclusive lock before:
- provider initialization;
- readiness call;
- output creation.

Second controller targeting the same run directory must fail immediately.

Do not silently delete stale locks.

### C2 — Clean-run directory gate

A measured run must refuse to start if canonical run evidence already exists:
- raw outputs;
- metadata;
- status files from another attempt.

Never auto-delete prior evidence.

### C3 — Fresh per-case state

At the start of every case:

`result = None`

All case-local variables are newly initialized.

No exception/fallback path may reuse a previous case result.

### C4 — Attempt policy

Per case:
- one substantive conversation;
- max one technical retry;
- retry only if no non-empty substantive final response exists;
- retry uses a fresh `run_case` conversation;
- never rerun for quality.

Double technical failure:
- no raw file;
- metadata TECHNICAL_ERROR;
- no fallback answer.

### C5 — Atomic raw writes

Write:
- case-specific temporary file;
- flush/fsync where practical;
- atomic replace to canonical raw path.

Never overwrite an already completed raw file in the same run.

### C6 — Atomic metadata/status

Use temp + atomic replace.

After each completed case:
- compute SHA-256 from canonical raw file;
- persist technical metadata.

Crash must not leave half-written metadata.

### C7 — Provider readiness gate

Before E10-001 in future full execution, make exactly one synthetic, non-E10 readiness call using the exact frozen reference provider/settings.

It must verify:
- host;
- requested model;
- observed response model identity;
- SYSTEM placement;
- tool-call loop or minimal system response;
- quota/readiness.

Failure -> stop before E10-001.

### C8 — Final reconciliation

COMPLETE is impossible unless:

- exactly 32 raw files;
- exactly 32 metadata records;
- IDs match 1:1;
- all raw files non-empty;
- every metadata SHA equals recomputed disk SHA;
- no orphan raw;
- no orphan metadata;
- legal attempt/retry counts;
- frozen provider/model/settings/harness/controller identities recorded.

### C9 — Duplicate-content integrity HOLD

Compute SHA-256 groups across all raw files before COMPLETE.

If distinct case IDs have byte-identical raw output:
- do not score;
- do not call it model failure;
- final technical state = `HOLD_INTEGRITY_REVIEW`;
- record case IDs + hash;
- require Chief Architect adjudication.

### C10 — Run identity

Technical metadata must record:
- run_id;
- controller SHA-256 / later Git blob SHA if available;
- runner SHA-256;
- provider adapter SHA-256;
- SUT SHA;
- PUBLIC-pack baseline SHA;
- provider host;
- requested model;
- observed model;
- generation settings;
- process PID;
- timestamps.

No secrets.

## Controller selftest

Implement:

`python controller.py selftest`

No provider call.

Must test at least:

1. exclusive lock: second acquisition fails;
2. stale/existing lock fails closed;
3. existing run evidence refuses fresh start;
4. per-case result initializes empty;
5. double-failure path writes no raw;
6. atomic raw write and SHA reconciliation;
7. atomic metadata write parses cleanly;
8. SHA mismatch detection;
9. missing raw detection;
10. orphan raw detection;
11. duplicate raw detection => HOLD;
12. provider host validation rejects non-OpenCode-Zen host;
13. provider model validation rejects non-`deepseek-v4-pro`;
14. generation settings validator rejects temperature != 0;
15. generation settings validator rejects max_tokens != 8000;
16. session-header generator produces different header per case, stable for repeated rounds of same case;
17. no secret written in synthetic metadata.

Synthetic temp directories only.

## Provider preflight probes

No E10 payloads.

Run synthetic probes sufficient to establish:

### P1 — exact dual SYSTEM placement

Prove both frozen-style custom SYSTEM slots are accepted through the actual adapter path.

### P2 — read-only tool loop

Synthetic prompt must call `read_sut_file("00_ROUTER.md")` and answer from returned content.

### P3 — fresh-context separation

Two fresh synthetic conversations with distinct marker; second must not know first marker.

### P4 — fixed generation settings

Log request metadata proving:
- temperature 0;
- max_tokens 8000;
- model deepseek-v4-pro.

Do not log full prompts beyond tracked files.

### P5 — model identity

Observed response model identity must equal requested model whenever API returns the field.

### P6 — session-header isolation

Use:
- one synthetic case header for all rounds of a probe;
- a different header for another probe.

Record only non-secret header values.

### P7 — capacity/readiness

Make a non-E10 readiness call.
If usage metadata is available through the provider configuration/API used during selection, record non-secret remaining/used percentages.

Do not run if provider already indicates insufficient suite headroom.

## PREFLIGHT status

Return exactly one:

- `PASS`
- `BLOCKED_PROVIDER`
- `BLOCKED_CONTROLLER`
- `BLOCKED_CREDENTIALS`
- `BLOCKED_CAPACITY`

PASS requires:
- controller selftest fully green;
- provider synthetic preflight fully green;
- reference model identity stable;
- no E10 case executed.

## PREFLIGHT.md

Record:

- status
- SUT SHA
- suite SHA
- public-pack SHA
- provider/model/host
- generation settings
- secret source name only
- system/mode role mapping
- runner/controller hashes
- lock mechanism
- atomic write mechanism
- fresh-context mechanism
- model-visible tool list
- path sandbox result
- provider probes
- model-identity result
- session-header policy
- readiness/quota result
- controller selftest matrix
- no-E10 confirmation
- no-private-eval confirmation
- exact blocker if any.

## Private eval prohibition

Do not read or materialize:
- private oracle;
- private coverage;
- scoring rubric;
- suite-design report;
- prior invalid raw outputs.

Do not inspect historical Kimi runner branches.

## Mechanical validation

Before return:

1. starting HEAD = exact PUBLIC-pack baseline;
2. diff contains only authorized harness files;
3. no PUBLIC E10 file changed;
4. no SUT/Agent/Stage 2–9 file changed;
5. no raw E10 output exists;
6. no private eval artifact exists/read;
7. no Kimi/Moonshot executable fallback exists;
8. Python syntax checks pass;
9. controller selftest passes;
10. path sandbox selftest passes;
11. provider probes use no E10 payload;
12. provider host/model exactly match frozen reference selection;
13. temperature=0 and max_tokens=8000 proven;
14. no secret in Git diff;
15. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. preflight status
4. provider/model/host
5. generation settings
6. system/mode instruction mapping
7. fresh-context result
8. model-visible tool boundary
9. SUT snapshot/path-sandbox result
10. controller lock result
11. atomic-write/reconciliation result
12. duplicate-output HOLD result
13. provider synthetic probe result
14. model-identity result
15. readiness/quota result
16. secret-handling result
17. changed-files list
18. mechanical validation
19. exact blocker if any
