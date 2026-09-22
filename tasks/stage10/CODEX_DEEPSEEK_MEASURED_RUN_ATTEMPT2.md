# Stage 10 Phase C Attempt #2 — Final Parser Microfix, Arm, and Execute the Measured Reference Run

## Role

You are the **Stage 10 Measured Reference Run Controller** for `Dylan5237/architecture-expert`.

Chief Architect reviewed the C0-R2 wiring head:

`eval/stage10-deepseek-runner@eee10ac4b2042a4ba4921cde6ca04d8ee30d79c1`

The measured orchestration primitives are accepted, but Chief Architect found one real integration defect in the exact PUBLIC-file syntax before authorizing E10 execution:

PUBLIC files use a backtick-quoted key:

``requested_mode`: AUTO`

while the current parser does not accept the backtick after `requested_mode` before the colon.

Therefore this task performs one bounded parser/arming microfix, re-runs deterministic checks, and — if every pre-run gate passes — immediately executes **Phase C Attempt #2**.

There is NO additional Chief Architect gate between the arming commit and the measured execution if and only if this task's exact pre-run conditions pass.

## Fixed inputs

Starting branch:

`eval/stage10-deepseek-runner`

Starting HEAD:

`eee10ac4b2042a4ba4921cde6ca04d8ee30d79c1`

Frozen SUT:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Frozen suite:

`ff157eb1947860345a305fb29452b51e09dd3a2b`

Frozen PUBLIC pack baseline:

`23a49382c949702446325d30e18d3321d8550c36`

Reference provider/model:

- OpenCode Zen
- `https://opencode.ai/zen/go/v1`
- `deepseek-v4-pro`
- temperature = 0
- max_tokens = 8000
- Kimi/Moonshot prohibited

Read this task from:

`origin/main:tasks/stage10/CODEX_DEEPSEEK_MEASURED_RUN_ATTEMPT2.md`

Do not merge main.

Use the existing dedicated worktree only for this branch.
Do not inspect historical Kimi branches or private eval material.

---

# Part A — Exact bounded arming microfix

Before any E10 model call, create exactly one **arming commit** on top of `eee10ac...`.

## A1 — Fix PUBLIC requested_mode parsing

Modify only `eval/stage10/harness/controller.py` so `parse_requested_mode()` correctly accepts the actual frozen PUBLIC syntax, including:

``requested_mode`: AUTO`

and all six canonical values.

Use a narrow parser/regex that accepts optional backticks around the key and optional backticks around the value.

Do not broaden it into arbitrary YAML/markdown interpretation.

All six accepted values remain exactly:

- AUTO
- ARCH_DESIGN
- ARCH_REVIEW
- CHANGE_REVIEW
- ADR_REVIEW
- INCIDENT_ANALYSIS

Unknown value still fails closed.

## A2 — Preserve PUBLIC payload bytes/text without newline normalization

Change `load_public_case()` to read:

`p.read_bytes().decode("utf-8")`

rather than text-mode `read_text()`.

The string sent to the USER role must preserve the checked-out PUBLIC file byte sequence after UTF-8 decoding, including line endings.

Do not reconstruct or strip the payload.

## A3 — Add deterministic PUBLIC dry-load gate

Before measured execution, the controller must have a deterministic helper/command or pre-run check that:

- loads all E10-001..032 PUBLIC files;
- parses exactly one valid requested_mode from each;
- validates IDs are complete and ordered;
- computes SHA-256 of each PUBLIC file's raw bytes for technical evidence;
- performs NO provider/model call;
- sends NO E10 content anywhere;
- does not print full case content.

This may be exposed as:

`python controller.py public-dry-run`

or performed inside the pre-run gate.

Prefer an explicit `public-dry-run` command for auditability.

## A4 — Make integration selftest use the real metadata syntax

Synthetic PRE10 test files must use the same relevant syntax form:

``requested_mode`: AUTO`

Add explicit parser checks covering all six canonical modes with the backtick-quoted key.

Add at least one rejection test for an invalid mode.

## A5 — Arm the measured CLI path

The orchestration function `run_measured_suite()` is already tested and accepted.

Modify ONLY the `main()` dispatch for `run-suite` so it now performs the actual authorized measured run.

The dispatch must:

1. import/use the frozen `ReferenceProvider` and `CaseRunner`;
2. generate a non-secret unique run_id;
3. obtain the current branch HEAD SHA mechanically (e.g. `git rev-parse HEAD`) and pass it as `harness_sha`;
4. require current HEAD to equal the just-created arming commit SHA at execution time;
5. call:
   `run_measured_suite(run_dir_path(), provider_factory, CaseRunner, case_ids=CASE_IDS, run_id=..., harness_sha=<arming_sha>)`;
6. print only technical terminal state / counts / stop reason;
7. return success exit code for COMPLETE;
8. use a distinct non-zero exit code for HOLD_INTEGRITY_REVIEW;
9. use non-zero for PARTIAL_TECHNICAL_FAILURE/BLOCKED conditions.

No quality interpretation.

### Authorization identity

To prevent accidental execution of an unreviewed later checkout, the arming commit SHA must be pinned.

Because the commit SHA is not known until commit creation, use this two-step deterministic procedure:

1. make all arming code changes except the final expected-SHA constant;
2. commit them once;
3. read the resulting commit SHA;
4. if necessary, create ONE tiny follow-up authorization commit that only writes the expected parent/arming identity into an authorization file/constant.

However, prefer a design that does NOT create a self-referential SHA problem.

Accepted pattern:

- controller requires environment variable:
  `STAGE10_MEASURED_AUTH_SHA`
- command compares that value to `git rev-parse HEAD`;
- this task explicitly authorizes setting the variable at runtime to the frozen arming HEAD after all pre-run validation.

This avoids changing code after validation.

No secret is involved.

## A6 — Correct measured metadata phase

For the actual measured run metadata:

`phase = "C"`

Do not leave `C0-R2` in measured evidence.

Synthetic integration selftests may still identify themselves as test context through run_id.

## A7 — No other semantic changes

Do NOT change:

- provider/model/host;
- temperature/max_tokens;
- system/mode role mapping;
- tool schema;
- path sandbox;
- read budgets;
- 24-round ceiling;
- retry policy;
- atomic-write policy;
- reconciliation policy;
- duplicate HOLD policy;
- PUBLIC cases;
- Agent/SUT.

If you discover another measured-path defect requiring semantic code change beyond A1-A6, STOP and return `HOLD_NEW_DEFECT`. Do not improvise and run E10.

---

# Part B — Pre-run validation after the arming commit

After creating the arming commit, do NOT run E10 until every gate below passes on that exact HEAD.

## B1 — Mechanical branch gate

Verify:

- parent is `eee10ac4b2042a4ba4921cde6ca04d8ee30d79c1`;
- arming diff changes ONLY:
  - `eval/stage10/harness/controller.py`
  - optionally `eval/stage10/harness/PREFLIGHT.md`
  - optionally `eval/stage10/harness/README.md`
- runner.py unchanged;
- provider adapter unchanged;
- no PUBLIC/SUT/Agent file changed.

## B2 — Compile/selftests

Run:

- Python compile for provider/runner/controller;
- `python controller.py selftest`;
- `python controller.py integration-selftest`;
- `python controller.py public-dry-run`.

All must PASS.

## B3 — PUBLIC dry-load result

Require:

- exactly 32 IDs;
- E10-001..E10-032;
- all requested_mode values accepted;
- no duplicate/missing ID;
- no file mutation;
- no model call;
- per-file SHA-256 recorded to stdout or a temporary external log, not committed unless already part of metadata design.

Do not expose full case text in logs.

## B4 — Clean measured output gate

Before readiness/run:

`eval/stage10/run/`

must not exist.

If it exists, STOP.

Do not auto-delete measured evidence.

## B5 — Private-eval absence

Do not read/materialize:

- oracle
- private coverage
- rubric
- suite-design report

No historical invalid raw outputs.

## B6 — Live provider readiness

Run exactly once:

`python controller.py readiness`

Require PASS with:

- host = OpenCode Zen;
- requested model = observed model = deepseek-v4-pro;
- temperature 0;
- max_tokens 8000;
- no provider drift;
- capacity not blocked.

If readiness fails, STOP before E10.

## B7 — Freeze arming HEAD

Record:

- arming HEAD SHA;
- controller SHA-256;
- runner SHA-256;
- provider adapter SHA-256.

Set:

`STAGE10_MEASURED_AUTH_SHA=<arming HEAD>`

only for the measured command.

No further code changes are allowed after B7.

---

# Part C — Phase C Attempt #2 measured execution

If and only if Part B fully passes, execute exactly once:

`python controller.py run-suite`

with `STAGE10_MEASURED_AUTH_SHA` set to the exact arming HEAD.

Do not launch the command twice.
Do not run it from another process.
Do not manually parallelize cases.

The controller's own lock remains authoritative.

## C1 — No interaction during run

Do not:

- inspect answers for quality;
- edit raw outputs;
- provide hints;
- restart a weak case;
- open private oracle;
- patch code;
- switch provider/model;
- start a second suite process.

Technical retry behavior is controlled only by the tracked controller.

## C2 — Terminal states

### COMPLETE

Valid measured run candidate.

Expected tracked output set:

- 32 raw files
- metadata.json
- RUN_STATUS.md

Exactly 34 new tracked run files.

### HOLD_INTEGRITY_REVIEW

Preserve all outputs + metadata + status.
Do not score.
Do not rerun.
Return duplicate groups for Chief Architect adjudication.

### PARTIAL_TECHNICAL_FAILURE

Preserve valid outputs produced before stop + metadata + RUN_STATUS.
Do not rerun.
Do not repair during same attempt.

### BLOCKED_PROVIDER

If run-suite fails before E10 because the internal readiness gate fails:
- preserve only technical evidence if controller creates it;
- zero E10 output;
- do not retry outside controller.

---

# Part D — Post-run validation and commit

Do NOT create the final evidence commit until post-run checks complete.

## D1 — Reconciliation

For COMPLETE require:

- exactly 32 raw outputs;
- exactly 32 metadata case records;
- exact E10-001..032 mapping;
- all raw non-empty;
- all disk SHA == metadata SHA;
- legal attempt/retry counts;
- no provider/model drift;
- fixed generation settings;
- max_tool_rounds=24;
- no duplicate raw hashes;
- RUN_STATUS = COMPLETE.

## D2 — Git integrity

For COMPLETE, diff from arming HEAD must contain exactly 34 files:

- `eval/stage10/run/raw/E10-001.md` .. `E10-032.md`
- `eval/stage10/run/metadata.json`
- `eval/stage10/run/RUN_STATUS.md`

No harness/public/SUT file may change during the measured execution.

For HOLD/PARTIAL, commit only the technical evidence actually produced; no cleanup/rewrites except what the tracked controller produced.

## D3 — Secret scan

No API key/token/authorization secret in diff.

The non-secret session headers are allowed.

## D4 — Final evidence commit

Create exactly one post-run evidence commit after the arming commit.

Push branch.

Do not amend the arming commit after measured execution.

Do not force-push after measured execution.

---

# Return format

Return only:

1. branch
2. arming SHA
3. final evidence SHA
4. run state
5. SUT SHA
6. suite SHA
7. PUBLIC pack SHA
8. reference provider/model
9. generation settings
10. PUBLIC dry-run result
11. pre-run selftest/integration/readiness result
12. measured run_id
13. completed case count
14. technical retry count + case IDs
15. technical error cases
16. observed-model integrity result
17. raw-output inventory result
18. duplicate-content result
19. reconciliation result
20. changed-files summary
21. secret scan result
22. mechanical validation
23. exact blocker/limitation if not COMPLETE

If Part B reveals a new measured-path defect before E10, return instead:

- state = `HOLD_NEW_DEFECT`
- zero E10 execution
- exact defect and evidence
- do not proceed to Part C.
