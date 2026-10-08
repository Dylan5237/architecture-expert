# Stage 11C — Paired Blinded Holdout Run (Agent v0.1 vs v0.2)

## Objective and boundaries

Execute **one clean, paired 12-case holdout evaluation** of Agent v0.1 and Agent v0.2 under the same company-gateway model and runtime policy. This is **execution and raw-evidence preservation only**, not scoring.

Reuse the proven Stage 10 `glm-5.3` provider/CaseRunner and integrity primitives. **Do not reopen transport investigations or expand the harness.**

The Stage 11 holdout is frozen on a separate commit. **PUBLIC case files are now authorized for the runner, but private oracle/coverage, rubric, manifest and design report remain forbidden until both raw runs have been fixed.**

## Clean executor and branch

Use a **fresh Codex session**, not the holdout designer or an inherited design-context session. Do not load any holdout oracle/coverage contents or prior private design conversation.

- Repository: `Dylan5237/architecture-expert`
- Branch: `eval/stage11-paired-holdout`
- Exact starting HEAD: `c12b67c7410878960c45a9934ded6ae52ae6c42f`
- Dedicated clean worktree; no `main` merge.
- Task source: `origin/main:tasks/stage11/CODEX_STAGE11_PAIRED_HOLDOUT.md`

Source identities:
- Agent v0.1: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`, system prompt `agent/system-prompt-v0.1.md`.
- Agent v0.2 candidate: `c12b67c7410878960c45a9934ded6ae52ae6c42f`, system prompt `agent/system-prompt-v0.2.md`.
- Sealed holdout design: `69cab5ab750c350ce719a0d37e7680bbc96bdf21`.
- Frozen 12 PUBLIC files only: `eval/stage11/holdout/design/public/H11-001.md` through `H11-012.md`, at the above design commit.
- No other holdout design files may be opened, checked out, copied, listed for content, or sent to the model.

Do not merge or checkout the entire holdout design branch. If necessary, fetch its frozen commit and extract **only the 12 exact PUBLIC paths**. A Git object being locally present does not authorize reading private files.

## Fixed model and execution contract

Both candidates use the SAME:

- Company gateway `glm-5.3`, OpenAI-compatible chat completions.
- Frozen Stage 10 company-gateway provider at `7db2639044d3a8f0b8706d70161513238ed29670`; reuse its existing implementation in the current branch.
- `httpx==0.28.1`, DIRECT, `trust_env=False`, no proxy/redirect/model fallback.
- Timeouts connect/read/write/pool = 30/360/30/30s.
- Existing bounded transport retry and 429 semantics unchanged.
- Temperature 0, fixed `max_tokens=32000`, `max_tool_rounds=24`.
- Fresh messages and unique session per case/attempt, one case-level technical retry at most.
- Exactly two SYSTEM messages: candidate-specific system prompt, then its candidate-specific mode contract; one USER equals the exact PUBLIC byte content decoded as UTF-8.
- Exactly one model-visible tool: `read_sut_file(path)`; same tool schema, path sandbox and read budgets.
- No web, shell, git, list, write, or evaluation tool visible to either SUT.
- Hidden reasoning text NEVER persisted.

Run all 12 v0.1 cases **sequentially**, then all 12 v0.2 cases **sequentially**. No concurrency. A new persistent provider/client may be created for each version's run; all cases within that version reuse it. Close before switching versions. Do not change settings or adapter between versions.

## Only allowed adaptation

Add **one small Stage 11 adapter** at:

`eval/stage11/harness/paired_holdout.py`

Optionally add a short `eval/stage11/harness/README.md` if necessary. No other harness code changes.

Prefer imports/reuse of the existing Stage 10 provider, CaseRunner, RunLock, atomic writes and diagnostics over code copying. The Stage 10 provider/runner/controller themselves must remain byte-for-byte unchanged.

The adapter's only specializations are:

- candidate SHA and active prompt filename;
- case IDs `H11-001..012`;
- verbatim PUBLIC retrieval;
- isolated `v0.1` and `v0.2` result paths;
- paired metadata and integrity reporting.

**No scenario-specific logic, hard-coded expected answers, or output-quality condition.**

### SUT snapshot isolation

Create separate read-only candidate snapshots using explicit Git archive path whitelists, **not a whole-repository archive**:

- `00_ROUTER.md`, `01_CONSTITUTION.md`, `02_VOCABULARY.md`, needed top-level knowledge indexes/maps;
- existing knowledge dirs (`domains/`, `principles/`, `failure-patterns/`, `tactics/`, `decision-playbooks/`, `question-bank/`, `cases/`, `sources/`);
- the five existing explicit mode files and `agent/modes/AUTO.md`;
- **only that candidate's active system-prompt file**.

Do not materialize `eval/`, `reports/`, `tasks/`, the alternative candidate's prompt, any holdout file, or Git metadata into the model-visible snapshot.

Before execution, verify that common KB/DP/mode files match across candidate snapshots, except the expressly version-neutralized AUTO reference; only the active system prompt differs behaviorally. Stop if unaccounted differences exist.

### PUBLIC payload isolation

Retrieve only the 12 exact PUBLIC blobs from the frozen design commit. Preserve their original bytes; do not rely on Windows CRLF checkout conversion. Both candidate runs must use byte-identical PUBLIC payloads in identical H11 case order. Record each case's content SHA256 in run metadata.

Do not read the design manifest to obtain hashes. The frozen PUBLIC commit and recorded bytes are sufficient.

## Mechanical gate before model execution

Using `PYTHONDONTWRITEBYTECODE=1` and `python -B`:

1. Syntax compile Stage 11 adapter in memory.
2. Reuse Stage 10 provider-free selftest and integration-selftest.
3. Adapter deterministic fake-provider test: both candidate prompts are correctly mapped; exactly two SYSTEMs; tool read allowed only under snapshot; `eval/`, `reports/`, `tasks/`, traversals blocked; fresh case isolation; raw write and reconciliation work.
4. Check 12 exact PUBLIC IDs, mode parsing and original-byte hashes for the run using only allowed PUBLIC content.
5. Check output directories absent and tracked worktree clean.
6. One provider readiness check is permitted (no full-Agent smoke matrix).

If the gate fails, stop without any H11 model execution. Do not inspect the private oracle to debug.

Freeze the adapter in **one code commit**, record its full SHA and checksum. No code changes after this freeze.

## Measured authorization and run

Set:

`STAGE11_PAIRED_AUTH_SHA=<exact adapter-freeze SHA>`

Recheck `git rev-parse HEAD` equals this SHA, tracked worktree clean, and the paired run root absent.

Execute the adapter's measured command **once**. This single invocation owns both sequential candidate runs; no manual per-case or per-version re-execution.

Outputs, all canonical:

`eval/stage11/holdout/run/v0.1/raw/H11-001.md..H11-012.md`
`eval/stage11/holdout/run/v0.1/metadata.json`
`eval/stage11/holdout/run/v0.1/RUN_STATUS.md`

`eval/stage11/holdout/run/v0.2/raw/H11-001.md..H11-012.md`
`eval/stage11/holdout/run/v0.2/metadata.json`
`eval/stage11/holdout/run/v0.2/RUN_STATUS.md`

`eval/stage11/holdout/run/PAIR_STATUS.json`

Full COMPLETE inventory: **29 files**.

Metadata must contain candidate SUT SHA, active system prompt path + SHA256, adapter SHA, provider/model/settings/transport policy, run and case IDs, exact input SHA, output SHA, model observed, technical retries, terminal status and sanitized per-round usage/diagnostics. No secrets or hidden reasoning text.

`PAIR_STATUS.json` records both run IDs, shared adapter SHA and common input hashes; it is **technical only, without scoring, judgments, or outcome comparisons**.

A content-identical output across *versions* is not automatically a duplicate failure; duplicate content within one version is governed by the existing HOLD rule. If all 12 paired raw outputs are identical, flag `HOLD_IDENTITY_REVIEW` for candidate/prompt injection review without scoring.

If a version has terminal technical failure, preserve exactly what was produced and STOP; do not proceed to the other version if the first is incomplete. No retry outside the tracked controller's fixed policy. No code patch, no rerun, no tuning after seeing output.

## Evidence freeze and return

After execution, reconcile:
- 12 cases and 12 nonempty raw for **each** version;
- each raw SHA;
- PUBLIC input SHA equality across versions;
- same adapter/provider/model/settings;
- observed model identity;
- no duplicate raw within a version;
- no evidence leakage, additional tool, or private-path read;
- exactly 29 canonical run files if COMPLETE.

Commit canonical evidence in **one evidence-only commit**, push normally, no amend/force push. Do not merge branches.

Return:

1. branch
2. adapter-freeze SHA
3. evidence SHA
4. status: COMPLETE / PARTIAL_TECHNICAL_FAILURE / HOLD_INTEGRITY_REVIEW / BLOCKED
5. v0.1 case count and run ID
6. v0.2 case count and run ID
7. provider/model/settings and model identity
8. fixed candidate SUT SHAs
9. common input-hash check
10. prompt identity check
11. deterministic/fake-provider gate result
12. technical retry and error counts
13. raw inventories and reconciliation
14. privacy/secret/isolation checks
15. changed files
16. exact blocker, if any

**Do not unseal the private oracle, do not score, do not modify v0.2, and do not claim Stage 11 PASS.** The next independent scorer phase begins only after both candidate runs and hashes are fixed.
