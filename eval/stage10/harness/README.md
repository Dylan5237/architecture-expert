# Stage 10 Reference Runner Harness (OpenCode Zen / deepseek-v4-pro)

Versioned runner + controller for the frozen Stage 10 reference evaluation.
Built by Phase C0-R preflight; no E10 case has been executed by this harness.

## Frozen contract

- SUT: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- Suite: `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC pack: `23a49382c949702446325d30e18d3321d8550c36`
- Provider: OpenCode Zen `https://opencode.ai/zen/go/v1`
- Model: `deepseek-v4-pro` (identity checked on every round)
- Settings: `temperature=0`, `max_tokens=16000`, no top_p/penalty
- Transport: fixed LOCAL_PROXY `http://127.0.0.1:7897` (process `NO_PROXY` cannot bypass it); at most 3 attempts per chat round with 1s/3s backoff for the explicit transient-error allowlist
- Response diagnostics: per-round model, finish reason, attempt/retry counts, sanitized retry errors, HTTP status, visible-content presence/length, reasoning presence/length, and numeric usage summary
- Hidden reasoning text: never returned to the runner or persisted
- Kimi/Moonshot: prohibited; no fallback path exists (fail closed)

## Files

- `provider_openai_compatible.py` — OpenAI chat-completions adapter; fixed host/model/settings and proxy; provider-round transient retry; runtime-only key loading (`STAGE10_API_KEY` or local OpenCode provider config); session-header policy.
- `runner.py` — SUT snapshot via `git archive`, path sandbox, single `read_sut_file` tool, fresh per-case conversations, per-round technical diagnostics without reasoning text.
- `controller.py` — single-process lock (O_EXCL + OS record lock), clean-run gate, per-case fresh state, one case-level retry, atomic raw/metadata writes, SHA reconciliation, duplicate-content HOLD, and provider-free deterministic selftests.

## Usage (future full run; NOT executed in C0-R)

```powershell
cd eval/stage10/harness
python controller.py selftest
```

Future full-run integration will drive `CaseRunner` per E10 case through the controller's
lock/gate/atomic-write/reconcile lifecycle with `finalize_case` / `technical_error_case`.

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

Each provider chat round sends one byte-identical request body for up to three attempts. Only remote disconnect/reset/abort/refusal, socket or URL timeout, TLS EOF, and HTTP 502/503/504 are retryable; 429, other 4xx, model drift, malformed successful JSON, and semantic/provider errors fail closed. There is no provider or route fallback.

The controller records each case attempt and each provider round, including transport counts/errors, model, finish reason, visible-content shape/length, reasoning presence/length, and numeric token usage. Reasoning text is removed by the adapter and is never stored.

