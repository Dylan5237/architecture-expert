# Stage 10 Reference Runner Harness (OpenCode Zen / deepseek-v4-pro)

Versioned runner + controller for the frozen Stage 10 reference evaluation.
Built by Phase C0-R preflight; no E10 case has been executed by this harness.

## Frozen contract

- SUT: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- Suite: `ff157eb1947860345a305fb29452b51e09dd3a2b`
- PUBLIC pack: `23a49382c949702446325d30e18d3321d8550c36`
- Provider: OpenCode Zen `https://opencode.ai/zen/go/v1`
- Model: `deepseek-v4-pro` (identity checked on every round)
- Settings: `temperature=0`, `max_tokens=8000`, no top_p/penalty
- Kimi/Moonshot: prohibited; no fallback path exists (fail closed)

## Files

- `provider_openai_compatible.py` — OpenAI chat-completions adapter; host/model/settings validation; runtime-only key loading (`STAGE10_API_KEY` or local OpenCode provider config); session-header policy.
- `runner.py` — SUT snapshot via `git archive`, path sandbox, single `read_sut_file` tool, fresh per-case conversations, fixed generation settings.
- `controller.py` — single-process lock (O_EXCL + OS record lock), clean-run gate, per-case fresh state, attempt policy, atomic raw/metadata writes, SHA reconciliation, duplicate-content HOLD, and a 17-check provider-free selftest.

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
- Canonical measured outputs (34 files): `eval/stage10/run/raw/E10-001.md..E10-032.md`, `eval/stage10/run/metadata.json`, `eval/stage10/run/RUN_STATUS.md`.

