# Stage 10 Reference Runner Harness (company compute gateway)

Versioned runner + controller for the frozen Stage 10 reference evaluation.
Attempt #5 follows `CODEX_COMPANY_GATEWAY_ATTEMPT5.md` from origin/main. Previous provider results in PREFLIGHT.md are historical; the company gateway is the active runtime.

## Frozen contract

- SUT: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- Suite: `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC pack: `23a49382c949702446325d30e18d3321d8550c36`
- Provider: company compute gateway `http://192.168.3.77:13000/v1`
- Protocol: OpenAI-compatible `/chat/completions`; Bearer credentials loaded at runtime from the owner's WorkBuddy `models.json` zoesoft records bound to this exact gateway
- Model: exactly one selected model fixed in the adapter and recorded in PREFLIGHT.md; returned identity is checked when available, including only the owner's confirmed `deepseek-flash` = `deepseek-v4.1-flash` alias
- Settings: `temperature=0`, `max_tokens=32000`, no top_p/penalty
- Transport: persistent `httpx==0.28.1` Client; fixed DIRECT route, `trust_env=False`, no proxy, no redirects; fixed connect/read/write/pool timeouts = 30/360/30/30 seconds; at most 3 attempts per chat round with 1s/3s backoff
- Response diagnostics: per-round model, finish reason, attempt/retry counts, sanitized retry errors, HTTP status, visible-content presence/length, reasoning presence/length, and numeric usage summary
- Hidden reasoning text: never returned to the runner or persisted
- Kimi/Moonshot: prohibited; no fallback path exists (fail closed)

## Files

- `provider_openai_compatible.py` — httpx OpenAI chat-completions adapter; fixed host/model/settings, DIRECT route and timeout policy; provider-round transient retry; runtime-only key loading (`STAGE10_API_KEY` or local OpenCode provider config); session-header policy.
- `requirements.txt` — exact `httpx==0.28.1` dependency; the adapter rejects another installed version.
- `runner.py` — SUT snapshot via `git archive`, path sandbox, single `read_sut_file` tool, fresh per-case conversations, per-round technical diagnostics without reasoning text.
- `controller.py` — single-process lock (O_EXCL + OS record lock), clean-run gate, per-case fresh state, one case-level retry, atomic raw/metadata writes, SHA reconciliation, duplicate-content HOLD, and provider-free deterministic selftests.

## Final runtime freeze gate

```powershell
cd eval/stage10/harness
$env:PYTHONDONTWRITEBYTECODE = '1'
python -B controller.py selftest
python -B controller.py integration-selftest
python -B controller.py public-dry-run
```

Model selection uses exactly one required-tool full-Agent synthetic probe per candidate, sequentially: glm-5.3, glm-5.3-flash, deepseek-v4.1-flash (gateway request id deepseek-flash). Prefer the first capable model in that order. Record capability facts only; do not score quality. The measured default has no model switch or fallback.

After selection, compile provider/runner/controller in memory and pass all deterministic gates above. Then run exactly two fresh full-Agent synthetic conversations sequentially with the selected model: an architecture analysis with the tool exposed, followed by a required router plus related-knowledge tool loop. Both require non-empty successful finals and no model drift or terminal provider failure. No failed smoke is repeated.

If both pass, create one runtime-freeze commit and set `STAGE10_MEASURED_AUTH_SHA` to that exact SHA. Confirm HEAD matches, tracked worktree is clean, and `eval/stage10/run/` is absent; invoke `python -B controller.py run-suite` exactly once for Attempt #5. The controller owns all retries and terminal evidence. Freeze failure means zero E10 execution; measured partial/HOLD means preserve evidence and stop without another run or patch. Do not reuse Attempt #4 outputs.

## Credential policy

The company credential is loaded only from matching zoesoft records in
`~/.workbuddy/models.json`. The old STAGE10_API_KEY/OpenCode config is ignored. The key is never printed, logged, or committed;
metadata redacts secret-named fields by construction.


## R2 wiring (C0-R2)

- `python controller.py run-suite` is the ONLY authorized measured-suite orchestration path (refuses to execute without an explicit measured-run task authorization).
- `python controller.py readiness` performs the single synthetic PRE10 readiness conversation (host/model/settings/identity/quota).
- `python controller.py integration-selftest` exercises the same orchestration functions with a deterministic fake provider and synthetic PRE10 cases only (no network, no E10 payload).
- Measured defaults: `max_tool_rounds = 24`; verbatim final visible content (no strip before raw write); observed model captured per round.
- Future measured run IDs use `phasec-<UTC timestamp>-<arming-short-sha>`.
- Canonical measured outputs (34 files): `eval/stage10/run/raw/E10-001.md..E10-032.md`, `eval/stage10/run/metadata.json`, `eval/stage10/run/RUN_STATUS.md`.

## Phase C runtime hardening

Each provider chat round builds one UTF-8 request body and sends those identical bytes, URL, headers and generic x-stage10-session for up to three total attempts. Retryable transport errors are httpx ConnectTimeout/ReadTimeout/WriteTimeout/PoolTimeout, ReadError, RemoteProtocolError, all ConnectError except explicit TLS certificate verification failure, and HTTP 502/503/504. Backoff remains 1s/3s. For HTTP 429, a valid delta-seconds or HTTP-date Retry-After is honored once, capped at 120 seconds and within the same total attempt bound. Missing/invalid Retry-After, a second 429, certificate verification failures, HTTP 500, other 4xx, redirects, model drift and invalid responses fail closed. No quota/usage endpoint or provider-specific wait assumption is used. No model/provider/route fallback or adaptive timeout exists.

Diagnostics distinguish total provider attempts, 429 provider retries, transport attempts/retries, and each sanitized 429 event. Header values and provider error-body text are not persisted. An explicit output-token capability rejection is reduced to a boolean in RAM; only the task's single 16000 capability fallback is allowed if needed, then that budget must be frozen globally.

The controller records each case attempt and each provider round, including httpx version, DIRECT route, timeout policy, transport counts/sanitized errors, model, finish reason, visible-content shape/length, reasoning presence/length, numeric token usage and elapsed time. Successful-response latency measures time from that transport attempt's start to HTTP response headers; a separate flag records arrival after 240 seconds. Round elapsed time includes retries and backoff. Reasoning text is removed by the adapter and is never stored.

The request remains a non-streaming chat completion (no `stream=true`). The httpx response context is used to measure header arrival and then read the complete JSON response in memory. Synthetic preflight never persists full model answers and never creates repository run evidence. See the company gateway section in `PREFLIGHT.md` for the current gate; earlier sections are historical results.

