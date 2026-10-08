# Stage 11C Readiness Recovery — One Diagnostic Retry, Then Paired Run

## Authority and scope

This is a **narrow addendum** to `origin/main:tasks/stage11/CODEX_STAGE11_PAIRED_HOLDOUT.md`. It supersedes **only** that task's one-call readiness preflight gate.

The first readiness call ended in `AssertionError: single readiness check failed`. The adapter failed to persist the diagnostic **before** the assertion. No H11 call, adapter freeze, or evidence commit occurred.

This addendum authorizes **one additional instrumented readiness call** and, only if the operational gate passes, the **original paired measured command exactly once**. It does not authorize another characterization phase, model switch, candidate change, or any other retry beyond the existing provider policy.

## Work in place — protect untracked work

- Repository: `Dylan5237/architecture-expert`.
- Same branch: `eval/stage11-paired-holdout`.
- Exact tracked HEAD: `c12b67c7410878960c45a9934ded6ae52ae6c42f`.
- **Reuse the existing dedicated worktree and the two local untracked artifacts**:
  - `eval/stage11/harness/paired_holdout.py`
  - `eval/stage11/harness/README.md`
- The first adapter SHA256 reported by the executor was `de05bd11e0b7870c684eb6745b9d67d564a01be092f67068b943d4a518d02ba8` before any recovery edit.
- Do not `git clean`, reset, overwrite, recreate the worktree, abandon the local files, or merge `main`.
- Read this task from `origin/main:tasks/stage11/CODEX_STAGE11_READINESS_RECOVERY.md` and the original Stage 11C task. Do not read holdout private oracle, coverage, rubric, manifest, report, or any prior private design context.
- The 12 frozen PUBLIC payloads remain permissible **only** as already authorized by the original paired-run task.

## Root-cause classification before live retry

Read only the local Stage 11 adapter's readiness path and the existing Stage 10 provider-readiness helper.

The Stage 10 helper defines `ok` as:
1. observed model matches the requested model;
2. visible output starts exactly with `READY1-ACK`;
3. visible output ends exactly with `READY2-END`.

This is a **synthetic format compliance check**, not by itself evidence that a company gateway is unavailable. An HTTP-200 response with the expected model, nonempty content and a successful terminal status may be operationally ready even if one of those markers is absent.

The original failure diagnostics were not persisted. **Do not claim a root cause from the assertion alone.**

## Only allowed adapter change

In `paired_holdout.py`, make the minimal local change needed to:

1. Persist a sanitized readiness diagnostic **before** raising or returning a failed gate.
2. Distinguish these cases:
   - HTTP/connection/authentication/provider exception;
   - observed-model mismatch;
   - empty visible final / unsuccessful terminal finish;
   - exact-marker mismatch only.
3. The **operational** readiness success condition is:
   - HTTP 200;
   - observed model identity exactly `glm-5.3`;
   - nonempty visible content;
   - successful terminal `finish_reason=stop` (or the provider's documented equivalent);
   - no terminal transport/provider error.
4. Record strict marker checks as `marker_prefix_ok` / `marker_suffix_ok` diagnostics only. If operational readiness passes while marker checks fail, classify `READY_WITH_MARKER_MISMATCH`, **not** `BLOCKED_PROVIDER`.
5. Keep the readiness request itself unchanged and send it exactly once in this recovery task. Existing httpx per-round transport retry remains as frozen; do not add application-level retries or fresh model calls.
6. Do not change any measured-case settings, prompts, mode selection, tool schema, provider model identity requirement, candidate SUT SHA, Stage 11 PUBLIC bytes, controller/runner/provider, or result format.

Record technical fields only: request outcome, HTTP status, observed model ID, finish reason, visible content length, prefix/suffix booleans, sanitized error class, provider/transport attempt counts and elapsed time if available.

Never persist:
- complete readiness response text;
- hidden reasoning content;
- Authorization headers, API key or other credentials;
- arbitrary exception text that could contain private configuration.

The existing `README.md` may contain the non-secret readiness outcome/diagnostic; if the check fails, update that local untracked README before returning, so the failure details survive the exception. No additional tracked paths are authorized.

## Mechanical checks — no extra model runs

Before the new readiness call:

- ensure original provider-free Stage 10 selftest/integration and adapter fake-provider tests remain passing;
- add a deterministic fake-provider check for: (a) HTTP200+correct model+nonempty stop with marker mismatch = operational PASS; (b) model drift or empty content = BLOCK; (c) ProviderError = sanitized diagnosis recorded before fail;
- ensure the two existing local artifacts are preserved;
- no run root exists;
- no private design material has been read.

No new 10-call soak, alternate model/proxy comparison, synthetic full-Agent smoke matrix or model tuning.

## Exactly one additional live readiness

Make **one** additional readiness provider conversation, with the unchanged fixed company-gateway `glm-5.3` config.

If it fails operational readiness:
- set `STAGE11_C: BLOCKED_READINESS_DIAGNOSED`;
- preserve sanitized diagnostic in the local README;
- perform **zero H11 model calls**;
- do not commit or push;
- return the concrete failure category and diagnostic fields;
- stop. No third readiness is authorized.

If it passes operational readiness:
- record strict-marker status separately;
- finish original Stage 11C mechanical validation;
- commit the two authorized Stage 11 adapter/README files in exactly one **adapter-freeze commit** and push;
- from the exact frozen adapter SHA, authorize and execute the original `STAGE11_PAIRED_AUTH_SHA` measured command **once**;
- preserve both version outputs, reconcile, commit canonical evidence separately and push;
- STOP. No scoring or oracle unsealing.

## Still-frozen evaluation boundaries

Keep exactly as the original Stage 11C task:
- v0.1 `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`;
- v0.2 `c12b67c7410878960c45a9934ded6ae52ae6c42f`;
- holdout PUBLIC only from design commit `69cab5ab750c350ce719a0d37e7680bbc96bdf21`;
- provider `glm-5.3`, max_tokens 32000, temperature 0, max_tool_rounds 24;
- 12+12 case order, identical PUBLIC SHA256 across versions;
- same frozen Stage 10 company gateway provider and tool/path-sandbox implementation;
- no web/shell/git/eval/private tools to SUT;
- hidden reasoning never persisted;
- exactly 29 canonical files when the paired run is COMPLETE;
- no score, oracle access, rerun, model fallback, or Agent repair.

This readiness adjustment changes only **preflight operational availability classification**, not any H11 scoring or pass criteria.

## Return

1. branch and final tracked SHA(s);
2. adapter freeze status;
3. readiness diagnostic category + sanitized status/model/finish/content-length/marker booleans;
4. provider and transport attempt counts if known;
5. tests / fake-provider checks;
6. H11 execution count;
7. if COMPLETE: v0.1/v0.2 run IDs, 12+12 raw, common input hashes, model identity and SHA reconciliation, evidence SHA;
8. changed-file scope and secret scan;
9. exact blocker if still blocked.

No repeat readiness call or further harness investigation inside this task.
