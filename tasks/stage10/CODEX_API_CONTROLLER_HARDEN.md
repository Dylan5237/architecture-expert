# Stage 10 Phase C1 — Versioned Controller Hardening + Re-Preflight

## Role

You are the **Stage 10 Evaluation Controller Engineer** for `Dylan5237/architecture-expert`.

The previous Phase C full-run attempt is INVALID and preserved separately as an incident on:

`eval/stage10-api-runner@ab2f439cee339893b9e9f3c6476f5004eef25fe9`

Do not reuse that branch for the rerun.

This task builds a **versioned, fail-closed suite controller** on a clean branch and re-preflights it before any E10 execution.

## Clean branch

Work only on:

`eval/stage10-api-runner-v2`

Starting HEAD:

`78059179e103dd7275cad4493c70443b4562c647`

This branch starts from the previously accepted C0 harness and contains no invalid run outputs/status.

Use a dedicated worktree or single-branch clone.

Do not inspect/repair any other local checkout.

## Fixed inputs

Frozen Agent v0.1 SUT:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Frozen suite:

`ff157eb1947860345a305fb29452b51e09dd3a2b`

Frozen PUBLIC pack:

`23a49382c949702446325d30e18d3321d8550c36`

Frozen C0 harness:

`78059179e103dd7275cad4493c70443b4562c647`

Provider/model to preserve:

- API host: `api.kimi.com`
- model: `kimi-for-coding-highspeed`

Read this task from:

`origin/main:tasks/stage10/CODEX_API_CONTROLLER_HARDEN.md`

Do not merge main.

## Why this task exists

The failed attempt demonstrated that the ephemeral controller itself is part of evaluation integrity.

Observed incident classes:

1. two controller processes ran concurrently against one output set;
2. exception path reused a previous iteration's `result`;
3. disk raw files and metadata SHA values diverged;
4. cross-case duplicate outputs appeared;
5. E10-032 hit provider 403 quota exhaustion;
6. registry default model drifted, although the run correctly pinned the intended model via environment.

No valid Agent behavior evidence survived that run.

The controller must therefore become a tracked, reviewable, frozen evaluation artifact.

## Scope

Do NOT run E10-001..032 in this task.

Build + locally selftest + provider-smoke only.

Do not read oracle/rubric/private coverage/design report.

Do not change:
- `runner.py`;
- provider adapter;
- SUT;
- Agent prompt/modes;
- PUBLIC cases.

## Required new files

Create only:

- `eval/stage10/harness/controller.py`
- `eval/stage10/harness/CONTROLLER_PREFLIGHT.md`

No other tracked file may change.

## Controller requirements

### C1-1 Single-process exclusion

The controller must prevent two suite instances from targeting the same run directory.

Use an atomic OS-level creation primitive, e.g.:
- exclusive lockfile creation with `O_CREAT|O_EXCL`, or
- equivalent cross-platform atomic mechanism.

Requirements:
- acquire before provider initialization or output creation;
- second process fails closed immediately;
- lock records PID/run-id for diagnostics but no secret;
- stale lock is NOT silently deleted;
- stale-lock recovery requires explicit operator action after verifying no live process;
- lock removed only on a clean/controlled controller exit.

Do not rely on "we only start it once".

### C1-2 Fresh per-case state

At the top of every case iteration:

`result = None`

and initialize all case-local state from scratch.

No exception/fallback path may read a prior iteration's result object.

If both permitted attempts fail:
- no raw output is created for that case;
- metadata records TECHNICAL_ERROR;
- no previous case content can be substituted.

### C1-3 One-attempt semantics

For each case:
- one substantive conversation;
- max one technical retry only if no non-empty final answer exists;
- retry uses a fresh `run_case` call;
- no quality rerun.

### C1-4 Atomic raw writes

Write each raw output:
1. to a case-specific temp file;
2. flush + fsync where practical;
3. atomically replace/rename into the canonical raw path.

Do not stream directly into the canonical path.

Never overwrite an already-completed canonical raw file in the same run.

### C1-5 Atomic metadata writes

Metadata updates must use temp-file + atomic replace.

After each case:
- record raw SHA-256 computed from the canonical file;
- persist metadata atomically.

A controller crash must not leave syntactically half-written metadata.

### C1-6 Fail-closed output directory

For a new full run:
- canonical run directory must not already contain prior raw outputs/metadata from another attempt;
- controller refuses to start if it detects an existing completed/partial run evidence set;
- do not auto-delete prior evidence.

The v2 branch starts clean.

### C1-7 Provider/model pin

Before any case:
- provider host must equal `api.kimi.com`;
- resolved model must equal `kimi-for-coding-highspeed`.

Model may be supplied by `STAGE10_MODEL` environment override.

If registry default differs, env pinning is acceptable and must be recorded.

If resolved host/model differs after all overrides:
- stop with provider drift;
- do not substitute another endpoint/model.

### C1-8 Quota/provider readiness gate

Before E10-001 in the future full-run path, perform one unscored synthetic readiness call, not an E10 case.

Purpose:
- prove provider is currently callable;
- detect 401/403/quota/provider outage before partial suite execution.

If 403/quota exhaustion occurs:
- stop before E10-001;
- produce BLOCKED_QUOTA technical status;
- do not start a partial suite.

This readiness call is not scored and must not alter Agent/SUT.

For this C1 task, execute this readiness call only if quota is available.

If quota is still exhausted:
- controller code may still be committed after all local deterministic tests pass;
- `CONTROLLER_PREFLIGHT.md` status must be `READY_PENDING_PROVIDER_QUOTA`, not PASS;
- no E10 case is authorized.

### C1-9 Final reconciliation gate

A future full run may be marked COMPLETE only if all checks pass:

- exactly 32 canonical raw files;
- exactly 32 metadata records;
- IDs match 1:1;
- every raw file non-empty;
- every metadata SHA recomputes equal to disk file SHA;
- no path collision;
- no missing case;
- no orphan raw;
- no orphan metadata;
- every attempt/retry count legal;
- harness/provider/controller frozen identifiers recorded.

### C1-10 Duplicate-content integrity check

Compute SHA-256 groups across the 32 raw outputs before COMPLETE.

If two or more distinct case IDs have byte-identical raw output:
- do NOT automatically call the Agent wrong;
- do NOT score it;
- mark run `HOLD_INTEGRITY_REVIEW`;
- list duplicate case IDs + SHA;
- stop before final COMPLETE commit;
- require Chief Architect adjudication.

This catches controller misassociation without assuming duplicates are impossible.

### C1-11 Run-id / controller identity

Metadata for the future run must include:
- controller Git SHA or controller blob SHA;
- runner.py blob SHA;
- provider adapter blob SHA;
- run_id;
- process PID;
- started_at/completed_at;
- provider host/model.

No secrets.

### C1-12 No hidden fallback

Forbidden:
- previous-result reuse;
- substitute provider/model;
- fabricate empty answer;
- copy another case output;
- silently skip failed case;
- resume from a different model under same run-id.

## Controller selftest mode

Implement:

`python controller.py selftest`

It must NOT call the model and must test at least:

1. single-process lock rejection:
   - acquire lock;
   - second acquisition fails;
2. stale/existing lock fails closed;
3. per-case state helper initializes result empty;
4. double-failure path leaves no raw file;
5. atomic raw write + SHA recomputation;
6. atomic metadata write + YAML/JSON parse;
7. mismatch between metadata SHA and disk SHA is detected;
8. missing raw is detected;
9. orphan raw is detected;
10. duplicate raw SHA group is detected and returns HOLD condition;
11. existing run directory/evidence prevents fresh start;
12. provider host/model validation accepts only frozen host/model;
13. no secret is written to metadata/test output.

Selftests use synthetic temp directories only.

## Provider readiness smoke

Implement a controller command such as:

`python controller.py readiness`

It must:
- use the existing frozen provider adapter/harness;
- make exactly one synthetic non-E10 call;
- verify expected provider host/model;
- not create any E10 raw output;
- not modify SUT/PUBLIC files.

If current quota returns 403:
- report `READY_PENDING_PROVIDER_QUOTA`;
- do not classify controller as failed.

If successful:
- report `PASS`.

## CONTROLLER_PREFLIGHT.md

Record only technical evidence:

- status:
  - PASS
  - READY_PENDING_PROVIDER_QUOTA
  - BLOCKED_CONTROLLER
  - BLOCKED_PROVIDER_DRIFT
- SUT SHA
- public-pack SHA
- base harness SHA
- controller file SHA-256
- runner.py blob SHA
- provider adapter blob SHA
- provider host/model
- model pin source (e.g. env override; no value for secret)
- lock mechanism
- atomic-write mechanism
- retry semantics
- reconciliation checks
- duplicate-output policy
- selftest results
- readiness result
- no E10 executed
- no private eval material read
- exact blocker if not PASS.

Do not put API keys/tokens in the report.

## Security / secrecy

No secret value may:
- be printed;
- be logged;
- enter Git diff;
- enter test fixtures;
- enter metadata.

If you inspect local provider config, report only source name and non-secret host/model.

## Mechanical validation

Before return:

1. branch HEAD before work = `78059179e103dd7275cad4493c70443b4562c647`;
2. diff contains exactly the two new authorized files;
3. `runner.py` blob unchanged;
4. provider adapter blob unchanged;
5. no E10 file changed;
6. no Stage 2–9/SUT file changed;
7. no `eval/stage10/run/raw/` exists;
8. no oracle/rubric/private coverage/design report read or added;
9. controller Python syntax check passes;
10. controller selftest passes all required checks;
11. no secret-like material in Git diff;
12. if readiness PASS, exactly one synthetic model call occurred;
13. if readiness quota-blocked, zero E10 calls occurred;
14. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. controller preflight status
4. controller file SHA-256
5. lock mechanism result
6. per-case state/fallback result
7. atomic-write result
8. reconciliation result
9. duplicate-detection result
10. provider/model pin result
11. readiness result
12. selftest summary
13. changed-files list
14. mechanical validation
15. exact blocker if not PASS
