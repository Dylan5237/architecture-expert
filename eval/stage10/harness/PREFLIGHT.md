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

## HTTPX transport migration — current synthetic re-preflight (2026-09-30)

This section supersedes the historical urllib readiness gate above. This task authorizes transport migration and synthetic preflight only; it does not authorize Attempt #4.

### Scope, dependency and fixed policy

- Task source: refreshed `origin/main:tasks/stage10/CODEX_HTTPX_TRANSPORT_MIGRATION.md` (`origin/main` at `e22be15` when read).
- Dedicated branch: `eval/stage10-httpx-transport`.
- Verified starting HEAD: `d6f1716f34623aecf97eb80c225c282e78748cf7`; main was not merged.
- Characterization source: `e7d57cc085c6dcfb3a21252742ae32a0a0866ffe`; recommendation `CHANGE_HTTP_CLIENT`.
- Production chat transport: persistent `httpx.Client`, version **0.28.1**, pinned exactly in `requirements.txt`; no urllib chat path.
- Route: **DIRECT**; `trust_env=False`, `proxy=None`, `follow_redirects=False`; no implicit environment proxy, redirect or route/provider fallback.
- Fixed timeout policy in seconds: **connect 30 / read 360 / write 30 / pool 30**. No adaptive timeout or probe-time increase.
- Per provider round: **3 total transport attempts**; backoff before attempts 2/3 is **1s/3s**; request body is built once as UTF-8 bytes, with fixed URL/settings/messages/session/application headers across retries.
- Retry allowlist: httpx ConnectTimeout/ReadTimeout/WriteTimeout/PoolTimeout, ReadError, RemoteProtocolError, ConnectError caused by connection refusal/reset/abort/TLS EOF, HTTP 502/503/504.
- Fail closed without retry: HTTP 500, all 4xx including 403/429, redirects, malformed successful JSON, response-shape errors, model drift, semantic/capability errors and unlisted failures. No retry based on answer quality.
- Frozen SUT / suite / PUBLIC SHAs: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5` / `ff157eb1947860345a305fb29452b51e09dd3a2b` / `23a49382c949702446325d30e18d3321d8550c36`.
- Host/model/settings: OpenCode Zen `https://opencode.ai/zen/go/v1`, `deepseek-v4-pro`, temperature **0**, max_tokens **16000**. Tool ceiling **24**, read budgets/path sandbox, dual SYSTEM mapping, exact PUBLIC payload rules, case-level retry maximum and duplicate-HOLD semantics remain fixed.

### Deterministic verification

- `PYTHONDONTWRITEBYTECODE=1; python -B controller.py selftest`: **36/36 PASS**, no provider/network calls.
- `PYTHONDONTWRITEBYTECODE=1; python -B controller.py integration-selftest`: **9/9 PASS**, fake provider and synthetic PRE10 cases only.
- Coverage includes actual httpx Client/MockTransport path, environment/proxy/redirect settings, exact timeouts, persistent client reuse/close, retry recovery/exhaustion, body/header/session identity, narrow ConnectError classification, HTTP 500/403/429 immediate failure, 502/503/504 retry, malformed JSON/shape/model failures, version pin, fixed settings, recursive reasoning stripping and transport diagnostics propagation.
- Existing lock/atomic/reconciliation/duplicate/verbatim tests remain green. Empty-final attempt 1 retains httpx/DIRECT/timeout/latency/reasoning-count diagnostics before its case-level retry succeeds. Measured run IDs retain `phasec-...`.
- After deterministic tests: no repository run directory or bytecode; diff confined to authorized harness files.

### Synthetic method and privacy

- Readiness uses the fixed short dual-SYSTEM PRE10 readiness payload, independently repeated 10 times.
- Complex probes use the exact frozen Agent system prompt plus exact AUTO contract, and one newly invented cold-chain calibration scheduling scenario: three regions, offline return/duplicate windows, ambiguous DB/queue confirmation, cancellation vs correction, bounded consumers/fan-out/connection pools, overload, alternative state-write designs, partition-policy uncertainty and staged minimum correction/repair.
- The same scenario is repeated unchanged in 5 independent fresh conversations, with `read_sut_file` exposed but no read required. The tool variant is repeated unchanged in 3 fresh conversations and explicitly requires `00_ROUTER.md` plus a related knowledge file before final visible analysis.
- Each conversation has a fresh provider/CaseRunner/messages list and unique session header. Readiness is sequential; complex and tool groups each use fixed concurrency of at most **2** independent conversations. Each formal probe is fresh and uses only the specified per-round transport retries. The technical loader correction below is separate from answer-quality retry.
- Only frozen public knowledge/Agent paths are materialized in an external temporary snapshot; no tasks/reports/evaluation paths are included. The production PathSandbox and budgets handle actual tool reads.
- Payload SHA-256: complex `0ba0870d50ba42c6e64285fbd73e7a975130fb0d3aa2190f29675c776ac6f37a`; required-tool variant `35cab72a421a5802e92bb6ebccd32cf37b2d29eebce6359864b811afec493b12`.
- Frozen system/AUTO content SHA-256: `e25cca7e108963a75ee6b64581460029f1ebe7977122cd314e43eee953129fd1` / `cf9d3d49c5d060891a356624b503be4e2e7d391df6321a5a88a31aeae615f198`.
- Non-streaming request semantics remain unchanged (no `stream=true`). Successful-response latency is measured from that attempt's start to response headers; conversation and provider-round elapsed times include retries/backoff. The prior-boundary counter counts successful provider rounds whose headers arrive **after 240s**.
- **Hidden reasoning text is never persisted**: recursive stripping occurs before responses reach CaseRunner. Technical metrics retain only reasoning presence and length/count, numeric usage, status/model/finish/content lengths, timeouts and sanitized errors. Full synthetic model answers, prompts in provider logs, API keys and Authorization values are not stored. No scoring is performed.
- `E10_EXECUTION_COUNT: 0`; `run-suite` is not invoked.

### Frozen-prompt loader correction before the formal gate

- Mechanical review of the initial eight full-Agent pilot conversations found a representation mismatch: Windows git archive produced CRLF files; the external synthetic loader decoded raw bytes, while the production controller reads text with universal-newline normalization.
- Those eight pilot conversations are excluded from the formal 5+3 gate, despite returning visible finals. Their technical-only external metrics are preserved (SHA-256 aa93f598ab3c5c3588cd828038461a53857ff394452560583fd476b0173127af); no answer text was persisted.
- The corrected synthetic loader uses the same UTF-8 read_text behavior as the production controller and asserts SYSTEM/AUTO strings equal the exact frozen Git blobs before any full-Agent provider call. No Agent/SUT file, synthetic scenario wording, output budget, transport code/route/timeout/retry policy was changed.
- The original 10 independent short readiness calls are unaffected and remain valid. The final formal gate combines those ten records with eight newly identified fresh canonical-loader conversations; pilot full-Agent outcomes do not contribute to the final gate counters.
- Tool reads already used the production PathSandbox text loader. CRLF/LF disk-byte differences are archive conversion; the model-visible text is checked against frozen Git content, and all denied pilot paths were also absent from the frozen SUT.

### Real synthetic results and current decision

**Recommendation: HOLD_HTTPX_TRANSPORT_UNSTABLE**

- Readiness: **10/10 usable**; recovered retries **0**.
- Complex full-Agent: **5/5 non-empty visible finals**.
- Required actual tool-loop: **0/3 completed reads plus non-empty visible finals**.
- Empty-final count: **0**. Terminal transport-failure count: **3**.
- Recovered transport retries across all successful rounds: **0**; successful-response arrivals after 240s: **0**.
- Model identity: **PASS**; all 38 accepted provider rounds reported `deepseek-v4-pro`.
- max_tokens **16000** / temperature **0**: adapter enforcement and successful live responses confirm acceptance; no per-probe budget change.
- Reasoning metadata policy: **PASS**, presence/length/count plus numeric token accounting only; no hidden reasoning text or full synthetic model answers persisted.
- `E10_EXECUTION_COUNT: 0`; no Attempt #4 or `run-suite` invocation.
- Technical metrics SHA-256 (18 completed unique conversations, external temporary JSONL): `deceece1e5e754e85d43fb27fe3a83db17925de03b171e7272d3ec4b16ce34d4`.

#### Conversation observations

Times are seconds; visible lengths are characters. Intermediate tool-call rounds with zero visible content are not empty finals.

| Probe | Usable | Total elapsed | Rounds | Final finish | Visible final length | Attempts/retries | Successful rounds >240s |
|---|---|---:|---:|---|---:|---|---:|
| ready-01 | PASS | 5.617 | 1 | stop | 27 | 1/0 | 0 |
| ready-02 | PASS | 6.734 | 1 | stop | 27 | 1/0 | 0 |
| ready-03 | PASS | 7.598 | 1 | stop | 27 | 1/0 | 0 |
| ready-04 | PASS | 4.425 | 1 | stop | 27 | 1/0 | 0 |
| ready-05 | PASS | 7.796 | 1 | stop | 27 | 1/0 | 0 |
| ready-06 | PASS | 4.870 | 1 | stop | 27 | 1/0 | 0 |
| ready-07 | PASS | 4.465 | 1 | stop | 27 | 1/0 | 0 |
| ready-08 | PASS | 13.152 | 1 | stop | 27 | 1/0 | 0 |
| ready-09 | PASS | 7.505 | 1 | stop | 27 | 1/0 | 0 |
| ready-10 | PASS | 11.893 | 1 | stop | 27 | 1/0 | 0 |
| complex-01 | PASS | 387.924 | 2 | length | 8340 | 2/0 | 0 |
| complex-02 | PASS | 231.041 | 1 | length | 4222 | 1/0 | 0 |
| complex-03 | PASS | 324.877 | 2 | stop | 10723 | 2/0 | 0 |
| complex-04 | PASS | 356.557 | 5 | stop | 11660 | 5/0 | 0 |
| complex-05 | PASS | 255.782 | 7 | length | 9796 | 7/0 | 0 |
| tool-01 | FAIL | 173.129 | 6 | — | — | 8/2 | 0 |
| tool-02 | FAIL | 173.128 | 7 | — | — | 9/2 | 0 |
| tool-03 | FAIL | 0.721 | 1 | — | — | 1/0 | 0 |

#### Full-Agent provider-round observations

Content = field-present / value-present / character length; reasoning = field-present / length or count. Usage = prompt / completion / total / reasoning tokens. Missing values use `—`. Every accepted round below returned HTTP 200 and `deepseek-v4-pro`; the route, version and timeout policy are identical throughout.

| Probe/round | Round elapsed | Successful-attempt header arrival | Finish | Content | Reasoning | Numeric usage | Attempts/retries | >240s |
|---|---:|---:|---|---|---|---|---|---|
| complex-01/1 | 169.509 | 169.276 | tool_calls | true/true/34 | true/48798 | 3947/11290/15237/11109 | 1/0 | false |
| complex-01/2 | 217.58 | 217.559 | length | true/true/8340 | true/38151 | 35659/16000/51659/11250 | 1/0 | false |
| complex-02/1 | 230.218 | 229.785 | length | true/true/4222 | true/48827 | 3947/16000/19947/13500 | 1/0 | false |
| complex-03/1 | 136.943 | 136.411 | tool_calls | true/true/0 | true/37650 | 3947/8712/12659/8550 | 1/0 | false |
| complex-03/2 | 187.503 | 186.531 | stop | true/true/10723 | true/30089 | 33081/14191/47272/8447 | 1/0 | false |
| complex-04/1 | 18.795 | 18.795 | tool_calls | true/true/0 | true/4878 | 3947/1283/5230/1121 | 1/0 | false |
| complex-04/2 | 22.747 | 22.746 | tool_calls | true/true/0 | true/5724 | 25652/1617/27269/1340 | 1/0 | false |
| complex-04/3 | 9.021 | 9.02 | tool_calls | true/true/0 | true/1713 | 32071/822/32893/494 | 1/0 | false |
| complex-04/4 | 206.488 | 206.466 | tool_calls | true/true/0 | true/57686 | 36720/14809/51529/14635 | 1/0 | false |
| complex-04/5 | 99.103 | 99.092 | stop | true/true/11660 | true/5508 | 52447/8543/60990/2240 | 1/0 | false |
| complex-05/1 | 9.15 | 9.15 | tool_calls | true/true/0 | true/2117 | 3947/626/4573/425 | 1/0 | false |
| complex-05/2 | 9.717 | 9.717 | tool_calls | true/true/0 | true/1749 | 26521/597/27118/396 | 1/0 | false |
| complex-05/3 | 5.879 | 5.879 | tool_calls | true/true/0 | true/549 | 31552/433/31985/179 | 1/0 | false |
| complex-05/4 | 5.889 | 5.889 | tool_calls | true/true/0 | true/180 | 35191/388/35579/56 | 1/0 | false |
| complex-05/5 | 3.664 | 3.663 | tool_calls | true/true/0 | true/148 | 37285/92/37377/40 | 1/0 | false |
| complex-05/6 | 5.257 | 5.257 | tool_calls | true/true/0 | true/715 | 39950/309/40259/145 | 1/0 | false |
| complex-05/7 | 215.837 | 215.602 | length | true/true/9796 | true/39991 | 41200/15999/57199/10314 | 1/0 | false |
| tool-01/1 | 3.81 | 3.81 | tool_calls | true/true/0 | true/367 | 4012/176/4188/89 | 1/0 | false |
| tool-01/2 | 8.274 | 8.274 | tool_calls | true/true/0 | true/1599 | 18092/509/18601/384 | 1/0 | false |
| tool-01/3 | 3.52 | 3.519 | tool_calls | true/true/0 | true/200 | 19440/279/19719/40 | 1/0 | false |
| tool-01/4 | 11.409 | 11.409 | tool_calls | true/true/0 | true/2902 | 20924/995/21919/745 | 1/0 | false |
| tool-01/5 | 10.126 | 9.674 | tool_calls | true/true/0 | true/1973 | 24883/746/25629/576 | 1/0 | false |
| tool-01/6 | 135.083 | — | — | false/false/— | false/— | —/—/—/— | 3/2 | false |
| tool-02/1 | 22.952 | 19.639 | tool_calls | true/true/0 | true/5678 | 4012/1307/5319/1257 | 1/0 | false |
| tool-02/2 | 3.239 | 3.238 | tool_calls | true/true/0 | true/448 | 6021/191/6212/105 | 1/0 | false |
| tool-02/3 | 3.715 | 3.712 | tool_calls | true/true/0 | true/605 | 19852/234/20086/145 | 1/0 | false |
| tool-02/4 | 17.439 | 14.869 | tool_calls | true/true/0 | true/4307 | 26608/1135/27743/970 | 1/0 | false |
| tool-02/5 | 12.467 | 12.466 | tool_calls | true/true/0 | true/520 | 28568/265/28833/102 | 1/0 | false |
| tool-02/6 | 11.3 | 11.3 | tool_calls | true/true/0 | true/2637 | 29638/826/30464/652 | 1/0 | false |
| tool-02/7 | 101.102 | — | — | false/false/— | false/— | —/—/—/— | 3/2 | false |
| tool-03/1 | 0.001 | — | — | false/false/— | false/— | —/—/—/— | 1/0 | false |

#### Transport retry errors and tool-loop outcome

- tool-01, round 6, attempt 1: `RemoteProtocolError` / `remote protocol failure`, status —.
- tool-01, round 6, attempt 2: `RemoteProtocolError` / `remote protocol failure`, status —.
- tool-02, round 7, attempt 1: `RemoteProtocolError` / `remote protocol failure`, status —.
- tool-02, round 7, attempt 2: `RemoteProtocolError` / `remote protocol failure`, status —.

The four retries above all belong to terminally failed rounds; **none recovered**. tool-01 round 6 and tool-02 round 7 each made three attempts (two retryable RemoteProtocolError failures, then an unlisted ConnectError). tool-03 failed immediately on its first provider round/attempt with the same unlisted ConnectError. All three terminal rounds returned no HTTP status, observed model or visible final.

tool-01 and tool-02 returned the successful tool-call rounds shown above before failure. Their partial tool-read logs were not retained by the external synthetic driver on the failed CaseRunner path, so completed-read counts are unavailable. tool-03 failed before any tool call. No successful required-tool completion is claimed; the formal gate is 0/3.

### Final mechanical validation

- Starting HEAD was exactly the required d6f1716 commit; the final migration commit has that parent. Dedicated branch/worktree used throughout; no main merge/history rewrite.
- Only the six authorized harness files are changed: provider adapter, runner diagnostics allowlist, controller metadata/selftests, PREFLIGHT, README and exactly pinned requirements.
- AST comparison against the starting commit confirms CaseRunner, PathSandbox, tool schema, read budgets, frozen SHAs, generation settings, measured orchestration/reconciliation and run-id function are unchanged. Controller function changes are confined to metadata and deterministic tests.
- Production chat uses httpx only; DIRECT, fixed 30/360/30/30 timeouts, three transport attempts and 1s/3s backoff. No route/provider fallback exists.
- Deterministic gates: 36/36 selftest, 9/9 integration-selftest. Live gate results and any failures are recorded above.
- No repository run evidence directory/bytecode; no PUBLIC/SUT/Agent edits or private evaluation reads. E10 provider execution count remains zero.
- Runtime key is loaded only in memory; final diff is checked for the actual known runtime secret before commit. Technical evidence contains no hidden reasoning or model-answer text.
- Ordinary branch push and remote SHA readback are the final publication check; the exact matching SHA is returned in the task handoff.

### Exact blocker / handoff

**HOLD_HTTPX_TRANSPORT_UNSTABLE**: required tool-loop gate is 0/3 visible finals. tool-01 round 6 / tool-02 round 7 terminated after two retryable RemoteProtocolError failures followed by a non-retryable ConnectError; tool-03 round 1 failed immediately with a non-retryable ConnectError. No terminal HTTP/model response was available. The sanitized diagnostic is `provider transport failure: ConnectError (non-retryable transport failure)`; it does not establish a client/provider/network root cause. Do not advance to Attempt #4 from this preflight.

## Final bounded runtime freeze gate (2026-09-30)

This section supersedes the historical migration gate above for this task. The user authorizes exactly one full Phase C Attempt #4 immediately after both final sequential smokes pass.

### Scope and fixed policy

- Task source: `origin/main:tasks/stage10/CODEX_FINAL_RUNTIME_FREEZE_AND_ATTEMPT4.md`, read after fetch at `f6906ab`; task blob SHA-256 `043b505476047de733fabdbb750736a12a076130124d2ebf2e400a31a4e943bf`.
- Dedicated clean worktree/branch: `eval/stage10-final-runtime-freeze-attempt4`; exact starting HEAD `ed70a80c034198f62a480bbf346a41fac11f84bc`; main was not merged.
- Final patch: all generic httpx.ConnectError are retryable except explicit TLS certificate verification failure; certificate causes are checked before accepting generic connection errors. No other transport category was added.
- Final fixed global settings: temperature **0**, max_tokens **32000** for synthetic and measured execution. No adaptive budget or other sampling override.
- Persistent **httpx 0.28.1**, **DIRECT**, trust_env=false, proxy=None, follow_redirects=false; connect/read/write/pool timeouts **30/360/30/30 seconds**.
- Maximum **3 total transport attempts per provider round**, fixed **1s/3s** backoff, byte-identical application body/settings/session/route across retries. Timeout/read/protocol and HTTP 502/503/504 retry categories are unchanged; other HTTP/identity/shape/capability failures remain fail-closed.
- Frozen SUT/suite/PUBLIC SHAs remain `96d9ae333ffc5a8076d635b86634b5151ec0bbc5` / `ff157eb1947860345a305fb29452b51e09dd3a2b` / `23a49382c949702446325d30e18d3321d8550c36`.
- Host/model remain OpenCode Zen `https://opencode.ai/zen/go/v1` / `deepseek-v4-pro`; max_tool_rounds=24, dual SYSTEM/exact PUBLIC USER, single read_sut_file, sandbox/budgets, one case-level retry maximum and duplicate-HOLD semantics are unchanged.

### Deterministic and mechanical gate

- PYTHONDONTWRITEBYTECODE=1 and python -B used throughout. Before provider calls: in-memory source compile **3/3 PASS**, selftest **36/36 PASS**, integration-selftest **9/9 PASS**, PUBLIC dry-run **32/32 PASS**.
- Directly affected assertions cover generic ConnectError recovery/exhaustion, explicit/chained certificate failure without retry, 32000 acceptance/old-budget rejection, httpx/DIRECT/timeouts and generation metadata. Existing lock/atomic/reconciliation/duplicate/verbatim/empty-final diagnostics remain green.
- AST comparison against the starting commit confirms measured orchestration, lock, atomic writes, reconciliation, parser and run-id functions unchanged. runner.py, PUBLIC and Agent files are unchanged; requirements still pins httpx==0.28.1.

### Two sequential synthetic conversations

- Exactly two new PRE10 conversations; one persistent ReferenceProvider/httpx.Client reused sequentially, with a fresh CaseRunner/messages/sandbox for each. No 10x readiness soak, matrix, parallel provider conversation, failed-smoke repeat or prompt tuning.
- New scenario: inter-library transfer label dispatch/reprint/cancellation across 420 branches/two regions, 10-hour offline windows, 6-hour deduplication, DB/queue confirmation gaps, dispatcher lease/partition conflicts, burst backlog, bounded concurrency and staged minimum correction.
- Smoke #1 exposes the tool without requiring a read. Smoke #2 adds a fixed requirement to read 00_ROUTER.md then a related allowed knowledge file before the visible final.
- Exact frozen SYSTEM/AUTO strings are loaded with the same UTF-8 universal-newline text semantics as the controller and asserted equal to frozen Git blobs before calls. SYSTEM SHA-256 `e25cca7e108963a75ee6b64581460029f1ebe7977122cd314e43eee953129fd1`; AUTO `cf9d3d49c5d060891a356624b503be4e2e7d391df6321a5a88a31aeae615f198`.
- Scenario SHA-256 `9505947427e0112c29281d935fbaa5924dc4300cd22448f5f9c2f58129c85742`; required-tool variant `2c94276e49850e88050cb38f5f3add7849a7523cac3eb63dd796c953709ba00b`.
- Synthetic run/session namespace: `final-freeze-20260930T083302Z`; only public knowledge/Agent paths were materialized in an external temporary snapshot.
- Synthetic model answers and hidden reasoning text were never persisted. Only sanitized technical fields, numeric usage, content/reasoning lengths and completed tool-read path/byte/result facts are retained. No output-quality assessment.

| Smoke | Result | Elapsed seconds | Rounds | Final finish | Visible characters | Completed allowed reads | Transport retries |
|---|---|---:|---:|---|---:|---:|---:|
| PRE10-FINAL-SMOKE-01 | PASS | 284.114 | 7 | stop | 19767 | 27 | 0 |
| PRE10-FINAL-SMOKE-02 | PASS | 207.047 | 6 | stop | 14673 | 26 | 0 |

#### Provider-round technical facts

| Smoke/round | HTTP | Model | Finish | Round seconds | Attempts/retries | Visible length | Reasoning length/count |
|---|---:|---|---|---:|---|---:|---:|
| PRE10-FINAL-SMOKE-01/1 | 200 | deepseek-v4-pro | tool_calls | 7.594 | 1/0 | 0 | 1623 |
| PRE10-FINAL-SMOKE-01/2 | 200 | deepseek-v4-pro | tool_calls | 8.631 | 1/0 | 0 | 1434 |
| PRE10-FINAL-SMOKE-01/3 | 200 | deepseek-v4-pro | tool_calls | 9.79 | 1/0 | 0 | 1782 |
| PRE10-FINAL-SMOKE-01/4 | 200 | deepseek-v4-pro | tool_calls | 5.04 | 1/0 | 0 | 293 |
| PRE10-FINAL-SMOKE-01/5 | 200 | deepseek-v4-pro | tool_calls | 2.538 | 1/0 | 0 | 78 |
| PRE10-FINAL-SMOKE-01/6 | 200 | deepseek-v4-pro | tool_calls | 159.333 | 1/0 | 0 | 51169 |
| PRE10-FINAL-SMOKE-01/7 | 200 | deepseek-v4-pro | stop | 91.144 | 1/0 | 19767 | 10144 |
| PRE10-FINAL-SMOKE-02/1 | 200 | deepseek-v4-pro | tool_calls | 3.268 | 1/0 | 0 | 391 |
| PRE10-FINAL-SMOKE-02/2 | 200 | deepseek-v4-pro | tool_calls | 9.305 | 1/0 | 0 | 2655 |
| PRE10-FINAL-SMOKE-02/3 | 200 | deepseek-v4-pro | tool_calls | 17.353 | 1/0 | 0 | 5193 |
| PRE10-FINAL-SMOKE-02/4 | 200 | deepseek-v4-pro | tool_calls | 17.742 | 1/0 | 0 | 5366 |
| PRE10-FINAL-SMOKE-02/5 | 200 | deepseek-v4-pro | tool_calls | 8.002 | 1/0 | 0 | 1399 |
| PRE10-FINAL-SMOKE-02/6 | 200 | deepseek-v4-pro | stop | 151.334 | 1/0 | 14673 | 36466 |

#### Tool-read completion and terminal facts

| Smoke | Path | Bytes | Result |
|---|---|---:|---|
| PRE10-FINAL-SMOKE-01 | 00_ROUTER.md | 2377 | allow |
| PRE10-FINAL-SMOKE-01 | 01_CONSTITUTION.md | 16753 | allow |
| PRE10-FINAL-SMOKE-01 | decision-playbooks/index.md | 17652 | allow |
| PRE10-FINAL-SMOKE-01 | decision-playbooks/DP-003.md | 5609 | allow |
| PRE10-FINAL-SMOKE-01 | question-bank/index.md | 12968 | allow |
| PRE10-FINAL-SMOKE-01 | domains/state-data/index.md | 493 | allow |
| PRE10-FINAL-SMOKE-01 | domains/concurrency/index.md | 626 | allow |
| PRE10-FINAL-SMOKE-01 | domains/resources/index.md | 617 | allow |
| PRE10-FINAL-SMOKE-01 | domains/overload/index.md | 611 | allow |
| PRE10-FINAL-SMOKE-01 | domains/reliability/index.md | 634 | allow |
| PRE10-FINAL-SMOKE-01 | failure-patterns/FP-009.md | 1807 | allow |
| PRE10-FINAL-SMOKE-01 | failure-patterns/FP-012.md | 2155 | allow |
| PRE10-FINAL-SMOKE-01 | failure-patterns/FP-011.md | 1790 | allow |
| PRE10-FINAL-SMOKE-01 | failure-patterns/FP-010.md | 1756 | allow |
| PRE10-FINAL-SMOKE-01 | failure-patterns/FP-003.md | 1806 | allow |
| PRE10-FINAL-SMOKE-01 | failure-patterns/FP-001.md | 2061 | allow |
| PRE10-FINAL-SMOKE-01 | tactics/T-013.md | 1143 | allow |
| PRE10-FINAL-SMOKE-01 | tactics/T-015.md | 1346 | allow |
| PRE10-FINAL-SMOKE-01 | tactics/T-005.md | 1337 | allow |
| PRE10-FINAL-SMOKE-01 | tactics/T-003.md | 1119 | allow |
| PRE10-FINAL-SMOKE-01 | cases/good-cases/GC-013.md | 0 | deny: not a file |
| PRE10-FINAL-SMOKE-01 | cases/good-cases/GC-014.md | 0 | deny: not a file |
| PRE10-FINAL-SMOKE-01 | cases/good-cases/GC-015.md | 0 | deny: not a file |
| PRE10-FINAL-SMOKE-01 | cases/good-cases/GC-016.md | 0 | deny: not a file |
| PRE10-FINAL-SMOKE-01 | tactics/T-004.md | 1154 | allow |
| PRE10-FINAL-SMOKE-01 | tactics/T-006.md | 1039 | allow |
| PRE10-FINAL-SMOKE-01 | cases/good-cases/index.md | 8597 | allow |
| PRE10-FINAL-SMOKE-01 | tactics/T-002.md | 1239 | allow |
| PRE10-FINAL-SMOKE-01 | tactics/T-010.md | 1307 | allow |
| PRE10-FINAL-SMOKE-01 | tactics/T-007.md | 1237 | allow |
| PRE10-FINAL-SMOKE-01 | tactics/T-008.md | 1228 | allow |
| PRE10-FINAL-SMOKE-02 | 00_ROUTER.md | 2377 | allow |
| PRE10-FINAL-SMOKE-02 | decision-playbooks/index.md | 17652 | allow |
| PRE10-FINAL-SMOKE-02 | decision-playbooks/DP-003.md | 5609 | allow |
| PRE10-FINAL-SMOKE-02 | 01_CONSTITUTION.md | 16753 | allow |
| PRE10-FINAL-SMOKE-02 | domains/index.md | 1454 | allow |
| PRE10-FINAL-SMOKE-02 | domains/state-data/index.md | 493 | allow |
| PRE10-FINAL-SMOKE-02 | domains/reliability/index.md | 634 | allow |
| PRE10-FINAL-SMOKE-02 | domains/concurrency/index.md | 626 | allow |
| PRE10-FINAL-SMOKE-02 | domains/resources/index.md | 617 | allow |
| PRE10-FINAL-SMOKE-02 | domains/overload/index.md | 611 | allow |
| PRE10-FINAL-SMOKE-02 | domains/lifecycle/index.md | 646 | allow |
| PRE10-FINAL-SMOKE-02 | principles/MP-008.md | 2089 | allow |
| PRE10-FINAL-SMOKE-02 | principles/MP-010.md | 2378 | allow |
| PRE10-FINAL-SMOKE-02 | failure-patterns/FP-009.md | 1807 | allow |
| PRE10-FINAL-SMOKE-02 | failure-patterns/FP-012.md | 2155 | allow |
| PRE10-FINAL-SMOKE-02 | tactics/T-015.md | 1346 | allow |
| PRE10-FINAL-SMOKE-02 | tactics/T-013.md | 1143 | allow |
| PRE10-FINAL-SMOKE-02 | principles/MP-003.md | 2259 | allow |
| PRE10-FINAL-SMOKE-02 | principles/MP-009.md | 2635 | allow |
| PRE10-FINAL-SMOKE-02 | principles/MP-001.md | 2122 | allow |
| PRE10-FINAL-SMOKE-02 | principles/MP-004.md | 2267 | allow |
| PRE10-FINAL-SMOKE-02 | failure-patterns/FP-003.md | 1806 | allow |
| PRE10-FINAL-SMOKE-02 | failure-patterns/FP-010.md | 1756 | allow |
| PRE10-FINAL-SMOKE-02 | failure-patterns/FP-011.md | 1790 | allow |
| PRE10-FINAL-SMOKE-02 | failure-patterns/FP-001.md | 2061 | allow |
| PRE10-FINAL-SMOKE-02 | failure-patterns/FP-005.md | 1847 | allow |

### Freeze decision and pre-measured inventory

**FINAL_RUNTIME_FREEZE: PASS**

- `E10_EXECUTION_COUNT: 0` before measured execution; eval/stage10/run/ is absent.
- Tested working-file SHA-256 values (the controller hashes the same bytes into measured metadata):
- `controller.py`: `7558c12ddce28d92f41d9727c1a4329a2c090102f7ec2202efc59b0234336cc7`.
- `runner.py`: `c9ac016a20093279f19fd2f2482f369982e608f00c44be682475861548c4e517`.
- `provider_openai_compatible.py`: `35c249ee7928549d9570a7fea0f9ce8848e75c01ef1b90de4c8c47434a2bf48b`.
- External technical metrics SHA-256: `9be7214f0f56134b6325723d0daa4d8159ecb14ee6522ab4d13dd7d265d20883`.
- Both smoke finals are non-empty, finish_reason=stop, and all observed provider-round identities equal deepseek-v4-pro. Required router and related-knowledge reads completed in Smoke #2.
- The exact runtime-freeze SHA is the commit containing this final gate. After commit it is recorded in the external freeze manifest, final handoff and measured metadata.harness_git_sha; no tracked code change is permitted after that commit.
- Next authorized action: verify clean frozen HEAD and absent run directory, set STAGE10_MEASURED_AUTH_SHA to that HEAD, execute tracked controller.py run-suite exactly once, then preserve and commit only controller-produced canonical evidence.
- Actual runtime credential bytes are scanned without printing them; hidden reasoning policy remains NEVER STORE TEXT. No private oracle/rubric/coverage/design-report read, no SUT/PUBLIC/Agent edits, and no provider/model/route fallback.
