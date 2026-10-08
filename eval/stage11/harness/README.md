# Stage 11C paired blinded holdout adapter

Task source: `477ea2ecf05a9e0512ba5432d837e98ed6cc3454:tasks/stage11/CODEX_STAGE11_PAIRED_HOLDOUT.md`.
Task original-byte SHA256: `6a257e58f33937a3e06397509bae230b2a6f6014336084ab1426df187149d6e5`.

This adapter reuses the byte-unchanged Stage 10 company gateway provider,
CaseRunner, RunLock, atomic writers and reconciliation. It adds only candidate
mapping, explicit whitelist Git archives, exact PUBLIC blobs, sequential pair
orchestration and technical integrity metadata. No answer-quality rules exist.

Run from the dedicated `eval/stage11-paired-holdout` worktree, using
`PYTHONDONTWRITEBYTECODE=1`, `PYTHONUTF8=1` and `python -B`:

1. `paired_holdout.py gate --gate-record <external-technical-JSON>`
2. Commit only this adapter and README, record the full freeze SHA.
3. Set `STAGE11_PAIRED_AUTH_SHA` to that exact SHA.
4. Invoke `paired_holdout.py measured --gate-record <same-JSON>` exactly once.

The gate runs provider-free Stage 10 tests with the integration snapshot loader
bound to the v0.1 whitelist; it never whole-archives the repository. Fake tests
exercise prompt injection, exact USER, tool boundaries, fresh retry sessions,
serial client closure, verbatim writes, failure stop, duplicate/identity HOLD and
tamper reconciliation. One readiness conversation follows those checks. The
gate record contains only hashes, runtime facts and sanitized diagnostics and is
embedded in canonical metadata; it contains no synthetic answer or reasoning.

Only twelve exact PUBLIC paths at the frozen design SHA are read. Private
design/scoring material is neither enumerated nor opened. Snapshots exclude
eval/reports/tasks/holdout/.git and the alternative prompt. A first-version
technical failure or integrity HOLD stops before the second version. No code
change, tuning, manual rerun or scorer phase is authorized after freeze.

## Executor stop record — 2026-10-08

Mechanical gate: in-memory syntax/whitelist/PUBLIC checks passed; Stage 10
selftest 38/38, integration-selftest 9/9 and adapter fake-provider checks passed.
The single readiness conversation returned a failed readiness predicate:
`AssertionError: single readiness check failed` (gate process exit 1).
The gate record was not written because its write follows the readiness
assertion; observed identity, per-round diagnostics and readiness retry counts
are unavailable. No readiness retry or H11 execution was performed.

Status: BLOCKED. Adapter-freeze and evidence commits were not created; no push.
Both candidate case counts are zero and the canonical run root remains absent.
The adapter and this README remain local untracked artifacts for review. No
private design/scoring/history/memory material was opened.

## Narrow recovery authority

Recovery source: `3be72546265bcd8ace0aa538ed628888ac136468:tasks/stage11/CODEX_STAGE11_READINESS_RECOVERY.md`.
Recovery original-byte SHA256: `e533195af695c35f2bd1da96342e0fa9f40099e1e4257a62faf3d84540bfa5c2`.
The initial adapter hash was verified before recovery edits. Only readiness
diagnosis, its deterministic tests and the preflight decision are changed;
measured settings/orchestration and frozen Stage 10 files are unchanged.
In-memory reversal of only the recovery patch reproduces the initial adapter
SHA256 exactly; all 14 pre-existing non-gate functions/classes have equal ASTs.

The recovery sends the original Stage 10 readiness request exactly once. It
requires HTTP200, exact glm-5.3, nonempty visible content and finish_reason=stop
without terminal error. Exact prefix/suffix marker checks are diagnostic only.
Only sanitized technical fields are saved to this README and the gate record,
before any readiness failure is raised; response/reasoning/exception text is
never persisted. A failed operational check stops without commits or H11 calls.

## Readiness recovery — 2026-10-08

STAGE11_C: READINESS_RECOVERY_READY

```json
{
  "ok": true,
  "category": "READY",
  "request_outcome": "SUCCESS",
  "http_status": 200,
  "observed_model": "glm-5.3",
  "finish_reason": "stop",
  "content_length": 27,
  "marker_prefix_ok": true,
  "marker_suffix_ok": true,
  "error_class": null,
  "provider_attempt_count": 1,
  "transport_attempt_count": 1,
  "provider_retry_count": 0,
  "transport_retry_count": 0,
  "elapsed_s": 5.902
}
```
