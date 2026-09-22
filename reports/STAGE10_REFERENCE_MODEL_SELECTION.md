# Stage 10 Reference Model Selection — Non-Kimi

## 1. Status

`REFERENCE_MODEL_SELECTED`

Selected: **OpenCode Zen (`https://opencode.ai/zen/go/v1`) / `deepseek-v4-pro` / OpenAI-compatible chat-completions transport**.

## 2. Explicit Kimi exclusion

Owner decision `OD10-RM1: DO_NOT_USE_KIMI` was applied as a hard exclusion during discovery:

- local `kimi-code` provider entry (`https://api.kimi.com/coding/v1`, `k3-256k`) — excluded before any probe;
- all Kimi/Moonshot-hosted models visible on OpenCode Zen (`kimi-k3`, `kimi-k2.7-code`, `kimi-k2.6`, `kimi-k2.5`) — excluded from candidate enumeration;
- no candidate probed, selected, or configured resolves to Kimi/Moonshot;
- no fallback path to Kimi exists in the selected transport.

## 3. Frozen inputs

| Input | SHA |
|---|---|
| Agent v0.1 SUT | `96d9ae333ffc5a8076d635b86634b5151ec0bbc5` |
| Frozen suite-design | `ff157eb1947860345a305fb29452b51e09dd3a2b` |
| Frozen PUBLIC-pack baseline | `23a49382c949702446325d30e18d3321d8550c36` |

Branch `eval/stage10-reference-model` starts from exactly the PUBLIC-pack baseline `23a49382c949702446325d30e18d3321d8550c36` (verified: branch parent = `23a4938`, remote branch tip was already at the baseline).

## 4. Candidate inventory

Discovered from local provider configuration (`~/.opencodex/config.json` providers, local env var names, Ollama local registry). Secret values were read only at probe runtime and never printed or committed.

| ID | Provider family | API host | Model ID | Adapter | Discovery result |
|---|---|---|---|---|---|
| C1 | OpenCode Zen (public) | `https://opencode.ai/zen/go/v1` | `deepseek-v4-pro` | openai-chat | models 200; usage 200; probes executed |
| C2 | Zoe internal gateway | `http://192.168.3.77:13000/v1` | `glm-5.3` | openai-chat | models 200; probes executed |
| C3 | Volcengine Ark (public) | `https://ark.cn-beijing.volces.com/api/v3` | `deepseek-v4-pro-260813`, `doubao-seed-2-1-pro-260915`, `glm-5-3-flash-260828`, `deepseek-v4-flash-ga-260731` | openai-chat | models list 200 but every inference call rejected: `ModelNotOpen` / `InvalidEndpointOrModel.NotFound` (account has not activated any candidate model) |
| C4 | Local Ollama | `http://127.0.0.1:11434` | `qwen3:4b-q4_K_M` | ollama | only a 4B quantized model installed; fails M7 by inspection (lightweight model), not probed further |
| C5 | Local Codex router | `http://127.0.0.1:10100/v1` | `gpt-5.6-sol`, `gpt-6-astra`, … | openai-chat/responses | rejected in discovery: OAuth account-pool identity, floating ChatGPT-backed identity, no stable account-level model pin for a frozen run (M4/M8); historical Phase C quota exhaustion on this path |
| C6 | Kimi local provider | `https://api.kimi.com/coding/v1` | `k3-256k` | openai-chat | hard-excluded per OD10-RM1; never probed |

`openai` provider (`https://chatgpt.com/backend-api/codex`, authMode forward) is the same account-pool path as C5 and is rejected for the same identity-pinning reason. `cursor` provider is OAuth-based with a floating `auto` default; rejected at discovery (M8: interactive OAuth, M4: silent alias float).

## 5. M1..M8 matrix

| Gate | C1 OpenCode Zen / deepseek-v4-pro | C2 Zoe / glm-5.3 | C3 Volcengine |
|---|---|---|---|
| M1 direct API + system slot | PASS — chat-completions; dual system messages both honored (PRE10-TWOSYS: `L1-OK … L2-END`) | PASS — dual system honored on retry (first call returned empty content once; deterministic fallback is concatenation which also passed) | UNTESTABLE — no model callable |
| M2 fresh stateless context | PASS — R3 marker isolation | PASS — R3 marker isolation | UNTESTABLE |
| M3 controlled tool boundary | PASS — only `read_sut_file` exposed; answer depended on tool result | PASS — same | UNTESTABLE |
| M4 stable identity | PASS — requested `deepseek-v4-pro`, response `model: "deepseek-v4-pro"` on all calls | PASS — requested/response `glm-5.3` | UNTESTABLE |
| M5 context capacity | PASS — model catalog + observed multi-file reasoning; large context tier | PASS — 1M-class context per local registry metadata | UNTESTABLE |
| M6 suite capacity/quota | PASS — usage endpoint: rolling 1%, weekly 15%, monthly 48% (2026-09-22) | CONDITIONAL — no published quota; internal gateway stable (3×7ms pings) but capacity unaudited | FAIL — no callable model |
| M7 architecture reasoning | PASS — R4/R5 (R4 needed uniform max_tokens=4000 retry; reasoning-heavy model) | PASS — R4/R5 | UNTESTABLE |
| M8 reproducible transport | PASS — static API key from local config, no interactive login | PASS — static key | FAIL |
| **Overall** | **SELECTED** | **PASS (backup), not selected** | **REJECTED** |

## 6. Synthetic probe methodology

All probes were synthetic `PRE10-*` payloads invented for this task; no E10 case, title, mechanism, oracle fact, or expected answer was used or read. Probe code lives only in `%TEMP%\stage10-pre10` (outside the repo) and is not committed. All probes used `temperature: 0`. Every candidate received the same payloads and the same harness logic. One uniform retry (same payload, same temperature, raised `max_tokens` 2000→4000 for reasoning-heavy models) was applied identically to the affected probes after a truncation artifact; prompts were never tuned.

- PRE10-R1 system obedience: strict ACK-only system contract + user jailbreak attempt; pass = replies `ACK-PRE10` only.
- PRE10-R2 tool loop: single `read_sut_file` tool serving the frozen SUT `00_ROUTER.md` from a `git archive` snapshot; pass = tool actually called and the final answer reports the front-matter `type: knowledge-router` from tool content.
- PRE10-R3 context separation: request A stores `MARKER-ALPHA-7731`; independent request B must answer `NONE`.
- PRE10-R4 architecture reasoning: synthetic cache-aside staleness scenario (evidence/assumption split, mechanism, minimum correction, no unjustified rewrite).
- PRE10-R5 good-case precision: synthetic in-process queue "not best practice" review; pass = migration not justified by evidence, conflation named, measurement-first.
- PRE10-TWOSYS (M1 refinement): two stacked system messages each imposing an observable token; pass = both honored.

## 7. Per-candidate probe summary

### C1 — OpenCode Zen / deepseek-v4-pro (SELECTED)

| Probe | Result | Evidence |
|---|---|---|
| R1 | PASS | `ACK-PRE10` despite jailbreak |
| R2 | PASS | `read_sut_file` called; answered `knowledge-router` from tool content |
| R3 | PASS | B answered `NONE`; no marker leak |
| R4 | PASS (after uniform max_tokens retry) | correctly identified cache-aside race, delayed second delete/CAS as minimum fix, rejected store replacement |
| R5 | PASS | rejected immediate migration, named conflation, listed measurements first |
| TWOSYS | PASS | `L1-OK Hello! L2-END` |

Note: the first R4 attempt exhausted `max_tokens=2000` inside reasoning and returned empty visible content; this is a harness budget artifact, not a model-adequacy failure. The uniform retry with `max_tokens=4000` completed. Future runner must budget reasoning tokens explicitly.

### C2 — Zoe internal / glm-5.3 (backup; all gates pass)

| Probe | Result | Evidence |
|---|---|---|
| R1 | PASS | `ACK-PRE10` |
| R2 | PASS (graded on re-run with tool-loop fix) | tool called; answered `knowledge-router` |
| R3 | PASS | `NONE` |
| R4 | PASS | correct race mechanism, minimum correction, rejected rewrite |
| R5 | PASS (grader false-negative corrected by reading full text; uniform retry also passed) | "Not justified… measure first" |
| TWOSYS | PASS on retry | first dual-system call returned empty content once; retry honored both; concatenated single-system also passed |

Note: one empty-content response on the first TWOSYS call is an availability-quality concern for a frozen 32-case run, which is why C2 is backup rather than selection.

### C3 — Volcengine Ark (REJECTED)

`/models` lists catalog entries, but every actual inference call fails with `ModelNotOpen` / `InvalidEndpointOrModel.NotFound` — the account has not activated any of the listed models for standard API use. No probe could run.

## 8. Selected reference model/provider

- Provider: OpenCode Zen
- Endpoint: `https://opencode.ai/zen/go/v1/chat/completions`
- Model: `deepseek-v4-pro` (response-observed identity matches request on all calls)
- Transport: OpenAI-compatible chat-completions; requires non-secret `x-opencode-session` header per run (session routing only, not auth)

## 9. Exact reason for selection

C1 is the only candidate that passes all eight mandatory gates with stable public-endpoint behavior, a concrete pinned model identity, explicit quota headroom, deterministic stateless contexts, a working single-tool loop, and static-key reproducible transport. It wins over C2 on criterion 3 (audited quota vs unaudited internal capacity) and criterion 6 (no observed empty-response flakiness; C2 had one).

## 10. Rejected candidates + exact reason

- C2 Zoe/glm-5.3: all gates pass but not selected — no quota/capacity audit for a 32-case multi-round run, and one transient empty-content response observed; recorded as backup.
- C3 Volcengine: M6/M8 fail — account has no activated callable model.
- C4 Ollama qwen3:4b: M7 fail — lightweight 4B model.
- C5 local Codex router / openai pool: M4/M8 fail — OAuth account-pool, floating model identity, prior quota exhaustion.
- Cursor provider: M4/M8 fail — interactive OAuth, alias float.
- Kimi: hard-excluded per OD10-RM1.

## 11. Generation-parameter recommendation

- `temperature: 0` — accepted and used on all probes.
- Do not set `top_p`/penalties unless the endpoint documents them; leave default.
- `max_tokens` must be budgeted for reasoning-heavy behavior: ≥ 4000 for reference answers (R4 exhausted 2000 inside reasoning). Recommend 6000–8000 for real cases with multi-round tool history.
- Keep `x-opencode-session` constant per case run (it is routing metadata, not conversation state; each case still sends a fresh message array with no prior IDs).

## 12. Suite-capacity note

OpenCode Zen usage at probe time: rolling 1%, weekly 15%, monthly 48%. A 32-case suite with multi-round tool calls plus retries fits comfortably in the rolling window.

## 13. Required future harness adapter

Reuse the existing frozen Phase C harness (`78059179e103dd7275cad4493c70443b4562c647`, branch `eval/stage10-api-runner-v2`) with config:

- `STAGE10_API_BASE_URL=https://opencode.ai/zen/go/v1`
- `STAGE10_MODEL=deepseek-v4-pro`
- `STAGE10_API_KEY` loaded at runtime from the local OpenCode provider config (never committed)
- add the `x-opencode-session` header (e.g. `stage10-ref-<run-id>`) to the adapter's request headers; non-secret
- adapter type `openai-chat`; dual system messages proven; fallback concatenation path unnecessary

## 14. Secret-handling result

API keys were read only at probe runtime from `~/.opencodex/config.json`, never printed, logged, or committed. This report and the branch diff contain no secret values. Probe scripts stay in `%TEMP%` outside the repository.

## 15. No-E10 confirmation

No E10-001..032 case was read for evaluation, run, or scored. No private oracle/rubric/coverage/design report was read. No SUT or Agent file was modified. The only SUT byte read was `00_ROUTER.md` from a `git archive` snapshot of the frozen SUT SHA, used as benign tool-loop content per this task's own R2 design.

## 16. Genuine owner decisions only

- `OD10-RM1: DO_NOT_USE_KIMI` — applied.
- Selection itself follows the documented selection rule; no other owner decision was invented. C2 remains available as a recorded backup if the owner later prefers the internal gateway.