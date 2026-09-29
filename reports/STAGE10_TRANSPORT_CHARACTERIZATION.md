# Stage 10 Synthetic Transport Characterization

## Scope and fixed inputs

- Starting SHA: d6f1716f34623aecf97eb80c225c282e78748cf7
- Work branch: eval/stage10-transport-characterization
- Frozen SUT SHA for Agent prompt, AUTO contract, and 00_ROUTER.md: 96d9ae333ffc5a8076d635b86634b5151ec0bbc5
- Provider: OpenCode Zen; host: https://opencode.ai/zen/go/v1; requested model: deepseek-v4-pro
- R1 LOCAL_PROXY: forced HTTP CONNECT via http://127.0.0.1:7897
- R2 DIRECT: urllib ProxyHandler({}) and proxy environment removed for the request; no route fallback
- Primary diagnostic client: Python urllib. Phase 6 cross-check: locally installed httpx 0.28.1 with trust_env=False.
- Temperature: 0. All phases except Phase 4 request max_tokens=16000.
- Each independent probe has a new conversation and session ID. Each HTTP round allows at most 3 attempts with 1 s / 3 s backoff for the fixed transport error allowlist and HTTP 502/503/504. Per-attempt socket timeout: 240 s.
- Reported request sizes are UTF-8 JSON body bytes, excluding headers. On retries, the same body bytes are resent within that HTTP round.
- A usable result requires HTTP 200, a final visible response, and observed identity deepseek-v4-pro. Intermediate tool calls are followed within the same synthetic conversation; each row counts a fresh conversation.

## Exact synthetic probe classes

All user scenarios below are newly invented PRE10 material. No E10 case title, facts, expected answer, or mechanism was used.

| ID | System/user shape | Expected diagnostic role |
|---|---|---|
| R1/R2 and S4 | Full frozen Agent system prompt and AUTO contract as separate system messages. Synthetic fleet of 42,000 fictional instruments; 20-second batches, 36-hour resend, 72-hour correction, 18x regional recovery burst, 4-minute freshness, 400-day retention, and three invented write-path options. User asks for acknowledgement crash windows, duplicate/loss distinction, correction and capacity interactions, invariant table, staged change and repair plan. read_sut_file exposed with tool_choice=auto, but the user facts are self-contained. | Complex full-Agent request; identical body across R1/R2 route comparison. |
| S1 | Short system asks for exactly OK; short user says “Reply exactly OK.” No tool. | Small input/trivial output baseline. |
| S2 | Same short system; user says to reply exactly OK and carries repeated inert synthetic filler. No tool. Body 15,917 bytes, close to the roughly 15.8 KB full-Agent-plus-AUTO medium-case target. | Isolate input byte size from inference demand. |
| S3 | Short system; fictional command plane writes to audit store X then queue Y, with ambiguous commit timeout, crash windows and redelivery; user requests a concise protocol, crash-state table and safety/freshness distinction. No tool. | Small input/hard reasoning without full Agent prompt. |
| T1 | Same full-Agent synthetic fleet scenario; no tools exposed. | Tool-schema absence. |
| T2 | Same full-Agent synthetic fleet scenario; read_sut_file exposed, no read required. | Tool-schema presence. |
| T3 | Same full-Agent synthetic fleet scenario plus explicit instruction to call read_sut_file for frozen 00_ROUTER.md before answering. | Actual tool-call round. |
| M4000/M8000/M16000 | Same full-Agent synthetic fleet scenario and exposed tool; only max_tokens changes. | Output-budget reservation check. |
| STREAM | Same full-Agent synthetic fleet scenario and exposed tool, max_tokens 16000, stream=true. | SSE acceptance, first event, visible completion and tool delta handling. |
| HTTPX | Same full-Agent synthetic fleet scenario, non-streaming, max_tokens 16000, chosen route. | Independent HTTP stack cross-check. |

The ephemeral diagnostic client assembled only visible content and tool-call arguments in process memory to follow tool rounds. It did not persist output text, tool arguments, or any hidden reasoning fields. The single allowed synthetic tool read was frozen 00_ROUTER.md; any other path was denied.

## Phase 1 — Route isolation

Same 16,209-byte non-streaming full-Agent request; tools exposed; temperature 0; max_tokens 16000. Three fresh requests per route.

| Route | Repeats usable | Attempts per repeat | Elapsed to terminal failure (s) | HTTP/model/visible final | Technical errors |
|---|---:|---|---|---|---|
| LOCAL_PROXY | 0/3 | 3, 3, 3 | 254.890, 490.141, 19.328 | none / none / none | TLS EOF and timeout; all before response |
| DIRECT | 0/3 | 3, 3, 3 | 726.140, 726.063, 726.594 | none / none / none | timeout on every attempt; all before response |

Neither route met the stable criterion (3/3 usable without transport retries). Phase 2 therefore ran on both routes, twice per cell. Phase 1 alone does not isolate a proxy defect.

## Phase 2 — Request-shape matrix

Each cell has two fresh non-streaming calls at max_tokens 16000 and temperature 0. The first-byte/failure values below are seconds from request start. Success rows include HTTP 200, observed deepseek-v4-pro, and finish_reason=stop.

| Class | Route | Body bytes | Usable | First byte or terminal failure, repeats 1/2 (s) | Attempts | HTTP status / visible length |
|---|---|---:|---:|---|---|---|
| S1 | LOCAL_PROXY | 259 | 2/2 | 2.625 / 2.063 first byte | 1 / 1 | 200 / 2 chars each |
| S1 | DIRECT | 259 | 2/2 | 2.656 / 2.547 first byte | 1 / 1 | 200 / 2 chars each |
| S2 | LOCAL_PROXY | 15,917 | 2/2 | 2.875 / 2.687 first byte | 1 / 1 | 200 / 2 chars each |
| S2 | DIRECT | 15,917 | 2/2 | 3.422 / 3.250 first byte | 1 / 1 | 200 / 2 chars each |
| S3 | LOCAL_PROXY | 1,107 | 0/2 | 490.094 / 19.281 failure | 3 / 3 | no HTTP/model/final; TLS EOF/timeout |
| S3 | DIRECT | 1,107 | 2/2 | 210.031 / 157.281 first byte | 2 / 1 | 200 / 2,544 and 2,288 chars |
| S4 | LOCAL_PROXY | 16,209 | 0/2 | 19.422 / 19.282 failure | 3 / 3 | no HTTP/model/final; TLS EOF |
| S4 | DIRECT | 16,209 | 0/2 | 728.516 / 362.938 failure | 3 / 2 | no final; no status then HTTP 500 |

S2 passed 4/4 at almost the S4 body size, so request-body byte count alone did not reproduce the fault. S3 direct passed 2/2 but took 157–210 seconds to first byte; one repeat required a transport retry and 451.766 seconds total. S3 through the proxy failed 2/2. S4 failed on both routes. These comparisons leave full-Agent prompt shape, harder inference, and provider/gateway idle behavior unresolved.

Phase 2 showed 6/8 usable on DIRECT versus 4/8 on LOCAL_PROXY. DIRECT is the chosen route for Phases 3, 4, and 6.

## Phase 3 — Tool-shape isolation

Chosen route: DIRECT. Two fresh non-streaming requests per class, max_tokens 16000.

| Class | Body bytes by round | Usable | First byte or terminal failure (s) | Attempts | Observed result |
|---|---|---:|---|---|---|
| T1, no tools | 15,849 | 0/2 | 726.406 / 543.687 failure | 3 / 3 | no model or visible final; timeout, with one HTTP 503 on an intermediate attempt |
| T2, tool exposed/no read required | 16,209 | 0/2 | 726.781 / 720.812 failure | 3 / 3 | no model or visible final; timeout/remote disconnect |
| T3, tool read required | 16,383 then 19,095 | 0/2 final | 3.985 / 16.891 first byte for round 1; 518.375 / 276.875 terminal conversation time | 4 / 4 across two rounds | both repeats returned HTTP 200, deepseek-v4-pro, finish_reason=tool_calls and read_sut_file(00_ROUTER.md); the final round then exhausted 3 attempts with timeout/remote disconnect/reset |

T1 and T2 both failed 0/2, so merely exposing the tool schema did not materially change the non-streaming failure rate. T3 established that the gateway can accept the full prompt and produce the requested tool call quickly; failure moved to the hard second inference round after tool content was supplied. Tool use adds another long-response opportunity but is not the primary trigger.

## Phase 4 — max_tokens reservation check

Chosen route: DIRECT. Same non-streaming full-Agent hard request and exposed tool; two fresh calls per budget.

| max_tokens | Usable visible final | HTTP response | First byte or terminal failure (s) | Attempts | Finish/content/error |
|---:|---:|---:|---|---|---|
| 4,000 | 0/2 | 1/2 | 101.813 failure / 111.907 first byte | 3 / 2 | first repeat: remote disconnect; second: deepseek-v4-pro, finish_reason=length, 0 visible chars after one recovered reset |
| 8,000 | 0/2 | 2/2 | 216.360 / 210.140 first byte | 1 / 2 | both deepseek-v4-pro, finish_reason=length, 0 visible chars; one recovered remote disconnect |
| 16,000 | 0/2 | 0/2 | 522.046 / 622.235 failure | 3 / 3 | timeout/remote disconnect/reset before HTTP response |

Lower budgets improved the probability of receiving an HTTP response, but every 4,000/8,000 response exhausted its budget without visible content. At 16,000 both repeats failed before a response. Output reservation therefore changes failure timing and surface, but none of the tested budgets produced a usable final. This diagnostic does not justify changing the frozen future 16,000 setting.

## Phase 5 — Streaming diagnostic

Exact S4 full-Agent request with stream=true, max_tokens 16000. Three fresh requests per route. A transport-accepted row means the client received HTTP 200 and at least one SSE event; usable additionally requires visible content and model identity.

| Route | Repeat | Attempts | First SSE event (s) | Total (s) | Model / finish | Visible chars | Result |
|---|---:|---:|---:|---:|---|---:|---|
| LOCAL_PROXY | 1 | 1 | 1.407 | 327.454 | deepseek-v4-pro / length | 10,042 | usable visible content |
| LOCAL_PROXY | 2 | 1 | 1.359 | 313.718 | deepseek-v4-pro / length | 0 | transport accepted; no visible content |
| LOCAL_PROXY | 3 | 1 | 1.610 | 168.032 | deepseek-v4-pro / not surfaced | 0 | transport accepted; no visible content |
| DIRECT | 1 | 1 | 1.937 | 296.453 | deepseek-v4-pro / length | 3,027 | usable visible content |
| DIRECT | 2 | 2 | 2.875 on successful attempt | 528.860 | deepseek-v4-pro / length | 0 | first attempt timed out after HTTP acceptance; retry transport accepted, no visible content |
| DIRECT | 3 | 1 | 4.172 | 204.718 | deepseek-v4-pro / stop | 14,356 | usable visible completion |

Streaming established HTTP 200 plus SSE on all 6 independent requests and surfaced the requested model on all 6. The equivalent Phase 1 non-streaming shape produced no HTTP response on 6/6 requests. This route-independent contrast isolates the non-streaming idle/response-buffering path as the primary transport defect.

Streaming is not by itself a complete readiness result: only 3/6 calls produced visible content, four surfaced finish_reason=length, and one ended without a surfaced finish reason. These are provider/output-utility concerns distinct from accepting and sustaining the response stream. A streaming adapter would also need an explicit visible-final check, finish handling, technical timeout policy, and the existing retry/identity safeguards.

## Phase 6 — Alternate HTTP client

Chosen route: DIRECT. httpx 0.28.1, trust_env=False, non-streaming, same 16,209-byte S4 body and settings. Two fresh requests.

| Repeat | Usable | Attempts | First byte on successful attempt (s) | Total (s) | Model / finish / visible chars | Earlier attempt errors |
|---:|---:|---:|---:|---:|---|---|
| 1 | yes | 3 | 233.406 | 725.500 | deepseek-v4-pro / length / 522 | ReadTimeout, ReadTimeout |
| 2 | yes | 2 | 191.031 | 435.391 | deepseek-v4-pro / stop / 18,124 | ReadTimeout |

The independent HTTP stack produced a usable visible result in 2/2 full-Agent non-streaming conversations. The equivalent urllib/direct shape produced 0/9 usable results across Phase 1 R2, Phase 2 S4, Phase 3 T2, and Phase 4 M16000. This case-level A/B makes the urllib non-streaming transport the primary suspect rather than the local proxy or request size.

The cross-check is still marginal at the attempt level: httpx succeeded on only 2/5 attempts, both successes arrived close to the 240-second timeout, and one ended by length. The result supports replacing the client, but does not prove a specific urllib internal bug or provider implementation detail.

## Latency and transport-error taxonomy

S1/S2 returned first byte in 2.1–3.4 seconds. S3/direct needed 157.3–210.0 seconds. T3 tool calls arrived in 4.0–16.9 seconds, while their second non-streaming rounds failed. Full-Agent urllib non-streaming terminal failures took 19.3–728.5 seconds. Streaming delivered its first SSE event in 1.36–4.17 seconds and ran for 168.0–528.9 seconds. Successful httpx non-streaming attempts delivered first byte at 191.0 and 233.4 seconds; retries raised conversation totals to 435.4 and 725.5 seconds.

Observed technical categories: TLS EOF, TimeoutError/socket timeout, RemoteDisconnected, ConnectionResetError, HTTP 500, HTTP 503, and httpx ReadTimeout. HTTP 500 was terminal under the fixed retry policy; HTTP 503 was retried. Response-before-failure calls exposed status/model/finish metadata; pre-response failures exposed none. The timing pattern places complex non-streaming calls close to or beyond the 240-second response wait boundary.

## Identity, privacy, and scope

Every accepted response across all phases surfaced deepseek-v4-pro; no model drift was observed. Failed calls with no HTTP response surfaced no model identity. No hidden reasoning text was printed, retained in the metrics, or written to the report. Runtime credentials were loaded in memory only; API key, Authorization header, and proxy credentials were not printed or committed. The local proxy URL has no embedded credentials.

Only the three named frozen public SUT files were read for provider payload/tool handling. No private oracle, rubric, coverage, or design-report artifact was read. No E10 payload was sent. No quality score was computed. No harness code or run evidence directory was changed/created.

E10_EXECUTION_COUNT: 0

## Classification, confidence, and recommendation

- Primary classification: `URLLIB_TRANSPORT_DEFECT`
- Confidence: moderate. httpx produced a usable result in 2/2 independent full-Agent non-streaming conversations where urllib/direct produced 0/9 across equivalent cells. Streaming through urllib also established prompt acceptance and model identity on 6/6 calls, which rules against request size, route availability, or total provider rejection as sufficient explanations.
- Secondary contributing factor: complex generation latency sits near or beyond the 240-second response wait, amplifying differences in response handling and retry timing.
- Recommendation: `CHANGE_HTTP_CLIENT`
- OpenCode Zen viability for Stage 10: not viable with the existing urllib transport. It remains a candidate after an independent client is integrated without changing the frozen Agent/SUT and then passes synthetic visible-final, tool-round, identity, retry, and timeout preflight. This characterization does not authorize E10.
- Exact unresolved uncertainty: only two alternate-client conversations were run; both needed retries and their successful first bytes arrived at 191–233 seconds. The matrix therefore cannot distinguish a specific urllib implementation defect from a provider/gateway latency distribution that interacts badly with urllib and the 240-second boundary. Streaming produced visible content in only 3/6 calls, so provider output utility at max_tokens 16000 also remains unresolved.

## Mechanical validation

- Starting worktree HEAD before the report commit: exactly d6f1716f34623aecf97eb80c225c282e78748cf7.
- Intended commit diff: only reports/STAGE10_TRANSPORT_CHARACTERIZATION.md.
- Harness changes: none.
- Run evidence directory: absent.
- E10 provider calls: 0.
- Private evaluation reads: 0.
- Kimi/Moonshot calls: 0.
- Secret handling: PASS; runtime-only credentials, with zero known-secret-pattern hits in the staged diff.
- Remote readback is the post-commit gate; the final task return records the matching commit SHA.
