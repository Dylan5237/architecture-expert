# Stage 10 Phase C0-R — Reference Runner + Controller Preflight

## Status

**PASS**

## Frozen inputs

- SUT SHA: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- Suite SHA: `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC-pack SHA: `23a49382c949702446325d30e18d3321d8550c36`
- Starting HEAD: `23a49382c949702446325d30e18d3321d8550c36` (verified)

## Provider / model / host

- Provider: OpenCode Zen
- Host: `https://opencode.ai/zen/go/v1` (validated; any other host rejected by adapter and controller)
- Model: `deepseek-v4-pro` (requested and observed identical on every probe response)

## Generation settings

- `temperature = 0`
- `max_tokens = 8000`
- no `top_p` / penalty overrides
- enforced inside `ReferenceProvider.chat()`; controller re-validates; drift raises immediately

## Secret handling

- Secret source name only: `STAGE10_API_KEY` env var, else local `opencode-go` provider key in `~/.opencodex/config.json`
- Key never printed/logged/committed; controller metadata redacts secret-named fields (selftest check 17)

## System / mode role mapping

- SYSTEM message 1 = exact frozen `agent/system-prompt-v0.1.md` bytes from the SUT snapshot
- SYSTEM message 2 = exact frozen `agent/modes/<MODE>.md` bytes from the SUT snapshot
- USER message = exact PUBLIC case payload (verbatim, future runs)
- No IDE/project/user-rule injection; dual SYSTEM accepted by provider through the actual adapter path (probe P1)

## Harness / controller hashes (SHA-256, first 16 hex)

- provider_openai_compatible.py: `3C21AA3ABE21EF4A`
- runner.py: `9557CD02DC1E5E76`
- controller.py: `4FA3A708E0413A9A`

## Lock mechanism

`O_EXCL` creation of `controller.lock` + Windows `msvcrt` record lock + PID file.
Second acquisition fails immediately; existing/stale lock files fail closed; never auto-deleted.

## Atomic write mechanism

Temp file in target directory → write → flush → fsync → `os.replace` atomic replace.
Raw files are never overwritten once written; metadata written after raw with recomputed SHA-256.

## Fresh-context mechanism

Every case constructs a brand-new `messages` list inside `CaseRunner.run_case()`; no conversation/session/response IDs are reused; the only per-case constant is the non-secret routing header, which carries no content. Probe P3 verified marker isolation across two fresh conversations.

## Model-visible tool list

Exactly one tool: `read_sut_file(path)`.
No web/shell/list/write/git/env tools exist in the harness request path.

## Path sandbox result

Rejects: absolute paths, drive-letter paths, backslash paths, `..` traversal, `eval/**`, `.git/**`, `tasks/**`, paths outside the snapshot realpath, non-files.
Caps: 200,000 bytes per call; 2,000,000 bytes aggregate per case.
SUT snapshot materialized read-only from exactly `96d9ae3` via `git archive`; required-file assertion included.

## Provider probes (all synthetic, non-E10)

| Probe | Result | Evidence |
|---|---|---|
| P1 dual SYSTEM placement | PASS | reply began `LAYER1-ACK` and ended `LAYER2-END` |
| P2 read-only tool loop | PASS | model called `read_sut_file("00_ROUTER.md")` (2377 bytes, allow) and answered `knowledge-router` from tool content |
| P3 fresh-context separation | PASS | second conversation answered `NONE`; marker not leaked |
| P4 fixed generation settings | PASS | adapter-enforced temperature=0 / max_tokens=8000; model `deepseek-v4-pro` |
| P5 model identity | PASS | observed model `deepseek-v4-pro` on every response returning the field |
| P6 session-header isolation | PASS | distinct headers per case (`stage10-ref-preflight-P2-PROBE` / `-P3A` / `-P3B`); one header stable across rounds |
| P7 readiness/quota | PASS | usage endpoint reachable: rolling 1%, weekly 15%, monthly 48% (status ok) |

Note: an early P2 variant returned the abbreviated answer "router" from a loosely-worded probe; the harness tool loop itself worked (tool called, file served). The probe was re-issued with an explicit verbatim instruction through the same harness path — recorded as probe wording calibration, not model/harness change.

## Model-identity result

Requested = observed = `deepseek-v4-pro` on all provider responses; adapter hard-fails on any drift.

## Session-header policy

`x-opencode-session: stage10-ref-<run_id>-<case_id>`; unique per case, stable across tool rounds of one case, character-validated, non-secret, no content.

## Readiness / quota result

OpenCode Zen usage at preflight: rolling 1% (resets 2026-09-22T15:56:27Z), weekly 15% (resets 2026-09-28), monthly 48% (resets 2026-10-01) — sufficient headroom for 32 cases.

## Controller selftest matrix

`python controller.py selftest` — **all 17 checks PASS**:

exclusive lock; stale lock fails closed; existing evidence gate; fresh per-case state; double failure no raw; atomic raw + sha; atomic metadata parses; sha mismatch detection; missing raw detection; orphan raw detection; duplicate raw HOLD; host rejects non-Zen; model rejects non-deepseek; temperature!=0 rejected; max_tokens!=8000 rejected; session header policy; no secret in metadata.

## No-E10 confirmation

No E10-001..032 payload was read for execution or sent to the provider. All provider probes used newly invented synthetic payloads. No E10 raw output exists anywhere in this branch.

## No-private-eval confirmation

No private oracle, rubric, coverage, or suite-design artifact was read or materialized. Historical Kimi branches were not inspected.

## Blocker

None. Preflight status: **PASS**.


## R2 — Wiring + re-preflight (C0-R2)

- Old accepted C0-R SHA: `c177ae764703b7741b14e4a9501f176cf3164f27`
- New wiring commit SHA: pending until commit (reported in task return)
- run-suite command implemented: **yes** (`python controller.py run-suite`; refuses to execute without an explicit measured-run task authorization; visible in `--help`)
- `E10_EXECUTION_COUNT: 0`
- max tool rounds: **24** (fixed, recorded in metadata, no per-case variance)
- final-text fidelity: **verbatim** — provider final visible `message.content` written unmodified; substantive check uses `.strip()` for the attempt decision only
- observed-model capture: **yes** — per-round observed model list + final observed model per case; adapter hard-fails on drift
- controller selftest: **all 17 checks green**
- integration-selftest: **all 7 scenarios green** (A two-success COMPLETE; B retry with fresh CaseRunner, attempt_count=2/retry=1; C double failure stop, no raw; D duplicate HOLD; E metadata tamper blocks COMPLETE; F second controller locked out before provider; verbatim fidelity with padded content)
- readiness: **PASS** — OpenCode Zen host, `deepseek-v4-pro` requested=observed, temperature 0, max_tokens 8000, dual-SYSTEM probe `READY1-ACK ready READY2-END`, usage rolling 1% / weekly 15% / monthly 48%
- duplicate-HOLD result: implemented and exercised (scenario D)
- canonical future output set: **34 files** = `run/raw/E10-001.md..E10-032.md` (32) + `run/metadata.json` + `run/RUN_STATUS.md`
- no private eval read
- no Kimi/Moonshot fallback anywhere in executable paths
- recommendation: **READY_FOR_PHASE_C**

R2 file hashes (SHA-256, first 16 hex): controller `6F931D8BA0751803`, runner `C187DAB7527A802B`, provider adapter `3C21AA3ABE21EF4A` (unchanged from C0-R).


## Phase C Runtime Hardening — DeepSeek transport and output diagnostics

**Recommendation: HOLD_TRANSPORT_UNSTABLE**

### Scope and frozen settings

- Task source: refreshed `origin/main:tasks/stage10/CODEX_DEEPSEEK_RUNTIME_HARDENING.md`.
- Starting arming SHA: `c78b8cdd0eb88647170d10256d5139bd6c6a502e`.
- Frozen SUT/suite/PUBLIC-pack SHAs remain unchanged: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5` / `ff157eb1947860345a305fb29452b51e09dd3a2b` / `23a49382c949702446325d30e18d3321d8550c36`.
- Global settings: `temperature=0`, `max_tokens=16000`, no top_p/penalty or adaptive budget.
- 16,000 capability probe: **PASS** — HTTP 200, visible dual-SYSTEM readiness response, observed `deepseek-v4-pro`, finish_reason `stop`.
- Tool-call capability at 16,000: **PASS** — frozen system prompt + AUTO mode read `00_ROUTER.md`, completed 2 rounds (`tool_calls` then `stop`), returned a visible final.

### Transport retry and diagnostics

- Fixed route: `http://127.0.0.1:7897`; `NO_PROXY` cannot bypass the selected route.
- Per chat round: maximum 3 attempts total; fixed backoff of 1 second then 3 seconds; byte-identical body, model, settings, messages, and session header; no route/provider fallback.
- Retryable: RemoteDisconnected; connection reset/aborted/refused; socket/URL timeout; TLS EOF; HTTP 502/503/504.
- Fail closed without retry: HTTP 400/401/403, 429, other 4xx, model drift, malformed successful JSON, semantic/provider capability errors, and other unlisted errors.
- Case-attempt diagnostics preserve rounds, final finish_reason and substantive status. Per-round metadata records observed model, finish_reason, transport attempts/retries, sanitized retry errors, HTTP status, content-field/content presence and length, reasoning presence/length, and numeric usage summary.
- Hidden reasoning storage policy: **NEVER STORE TEXT**. The provider adapter removes reasoning fields before returning a response; only presence and length/count metadata is retained.
- Empty-final preservation: **PASS** — integration scenario G supplied a synthetic `finish_reason=length` with null visible content and reasoning/token counts; diagnostics remained in attempt 1 metadata before the case-level retry succeeded.

### Deterministic and synthetic results

- Deterministic selftest: **27/27 PASS**, provider-free; covers transport retry success/exhaustion, HTTP 403 immediate failure, HTTP 502/503/504 retry, 429 fail-closed, model drift, identical body/no fallback, settings enforcement, malformed JSON no-retry, reasoning-text removal, run-id prefix, fixed-proxy enforcement, and existing lock/atomic/reconciliation/duplicate checks.
- Integration selftest: **9/9 PASS**, provider-free; includes preservation of empty-final diagnostics before retry.
- Complex synthetic full-Agent probe: **0/3 usable responses**. All three independent contexts exhausted the fixed 3 transport attempts with TLS EOF before a model response; no prompt tuning occurred and no model-quality inference is made.
- Fixed-proxy readiness soak: **10/10 usable**, all observed `deepseek-v4-pro`; each completed in one transport attempt; recovered transient retry count: **0**.
- Tool-loop result: **PASS**, one synthetic tool probe read `00_ROUTER.md`, completed its tool round, and returned visible final content. No hidden reasoning text appeared in persisted metadata or output artifacts.
- Model identity: all returned responses in the 16k capability probe, tool-loop probe, and 10-call soak reported `deepseek-v4-pro`; the 3 failed complex probes returned no model response to inspect; no drift observed.
- Run-id hygiene: future measured IDs use `phasec-<UTC timestamp>-<arming-short-sha>`; `run-suite` was not invoked.
- `E10_EXECUTION_COUNT: 0`.
- No run evidence directory was created. No private oracle, rubric, coverage, or suite-design artifact was read or added. No PUBLIC/SUT/Agent file was changed. No Kimi/Moonshot fallback exists.

### Blocker

The simple readiness soak was stable, but all 3 required complex synthetic probes exhausted transport retries before receiving responses. Keep the gate at **HOLD_TRANSPORT_UNSTABLE**; do not authorize an E10 run from this preflight.

