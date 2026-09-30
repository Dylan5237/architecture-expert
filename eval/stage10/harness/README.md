# Stage 10 Reference Runner Harness (OpenCode Zen / deepseek-v4-pro)

Versioned runner + controller for the frozen Stage 10 reference evaluation.
Built by Phase C0-R preflight. The final freeze gate and one authorized Attempt #4 follow `CODEX_FINAL_RUNTIME_FREEZE_AND_ATTEMPT4.md` from origin/main.

## Frozen contract

- SUT: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- Suite: `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC pack: `23a49382c949702446325d30e18d3321d8550c36`
- Provider: OpenCode Zen `https://opencode.ai/zen/go/v1`
- Model: `deepseek-v4-pro` (identity checked on every round)
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

Before provider calls, compile provider/runner/controller source in memory. Then run exactly two fresh full-Agent synthetic conversations sequentially with the same persistent provider/client: a complex architecture scenario, followed by a required router plus related-knowledge tool loop. Both must return non-empty visible finals, `finish_reason=stop`, and the exact reference model without terminal transport failure. No failed smoke is repeated.

If both pass, create one runtime-freeze commit and set `STAGE10_MEASURED_AUTH_SHA` to that exact SHA. Confirm HEAD matches, tracked worktree is clean, and `eval/stage10/run/` is absent; invoke `python -B controller.py run-suite` exactly once. The controller owns all retries and terminal evidence. Freeze failure means zero E10 execution; measured partial/HOLD means preserve evidence and stop without another run or patch.

## Credential policy

`STAGE10_API_KEY` env var, else the local `opencode-go` provider key in
`~/.opencodex/config.json`. The key is never printed, logged, or committed;
metadata redacts secret-named fields by construction.


## R2 wiring (C0-R2)

- `python controller.py run-suite` is the ONLY authorized measured-suite orchestration path (refuses to execute without an explicit measured-run task authorization).
- `python controller.py readiness` performs the single synthetic PRE10 readiness conversation (host/model/settings/identity/quota).
- `python controller.py integration-selftest` exercises the same orchestration functions with a deterministic fake provider and synthetic PRE10 cases only (no network, no E10 payload).
- Measured defaults: `max_tool_rounds = 24`; verbatim final visible content (no strip before raw write); observed model captured per round.
- Future measured run IDs use `phasec-<UTC timestamp>-<arming-short-sha>`.
- Canonical measured outputs (34 files): `eval/stage10/run/raw/E10-001.md..E10-032.md`, `eval/stage10/run/metadata.json`, `eval/stage10/run/RUN_STATUS.md`.

## Phase C runtime hardening

Each provider chat round builds one UTF-8 request body and sends those identical bytes, URL, headers and session for up to three attempts. Retryable errors are httpx ConnectTimeout/ReadTimeout/WriteTimeout/PoolTimeout, ReadError, RemoteProtocolError, all ConnectError except explicit TLS certificate verification failure, and HTTP 502/503/504. Explicit certificate verification failures, HTTP 500, 429, all other 4xx, redirects, model drift, malformed successful JSON, response-shape errors and unlisted errors fail closed. Backoff remains 1s/3s. There is no provider or route fallback and no adaptive timeout.

The controller records each case attempt and each provider round, including httpx version, DIRECT route, timeout policy, transport counts/sanitized errors, model, finish reason, visible-content shape/length, reasoning presence/length, numeric token usage and elapsed time. Successful-response latency measures time from that transport attempt's start to HTTP response headers; a separate flag records arrival after 240 seconds. Round elapsed time includes retries and backoff. Reasoning text is removed by the adapter and is never stored.

The request remains a non-streaming chat completion (no `stream=true`). The httpx response context is used to measure header arrival and then read the complete JSON response in memory. Synthetic preflight never persists full model answers and never creates repository run evidence. See the final runtime freeze section in `PREFLIGHT.md` for the current gate; earlier sections are historical results.

