# Stage 10 Reference Model Selection — Non-Kimi

## Role

You are the **Stage 10 Reference Model Evaluator** for `Dylan5237/architecture-expert`.

The user has explicitly decided:

> **Do not use Kimi.**

This decision is authoritative.

Your job is to identify and preflight a **non-Kimi reference model/provider** for the frozen Stage 10 evaluation before any E10 case is run.

Do NOT run E10-001..032.
Do NOT read the private oracle/rubric/coverage/design report.
Do NOT score anything.
Do NOT modify the frozen Agent v0.1 or PUBLIC cases.

## Fixed frozen inputs

Frozen Agent v0.1 SUT:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Frozen suite:

`ff157eb1947860345a305fb29452b51e09dd3a2b`

Frozen PUBLIC pack:

`23a49382c949702446325d30e18d3321d8550c36`

Work branch:

`eval/stage10-reference-model`

Start from exactly the PUBLIC-pack baseline above.

Read this task from:

`origin/main:tasks/stage10/CODEX_REFERENCE_MODEL_SELECTION.md`

Do not merge main.

## Hard exclusion: Kimi

The following are prohibited for Stage 10 reference evaluation:

- `api.kimi.com`
- any Moonshot/Kimi provider endpoint
- any model whose selected identity is Kimi-branded or Kimi-hosted
- local provider aliases that ultimately resolve to Kimi/Moonshot
- the previous `kimi-for-coding-highspeed` path
- silent fallback to Kimi if another provider fails

Historical Kimi harness/incident branches remain evidence only and are not reusable as the reference-model run line.

If a provider configuration is ambiguous about whether it resolves to Kimi/Moonshot, treat it as excluded until proven otherwise.

## Selection goal

Select **one reference model** that can support a trustworthy Stage 10 baseline evaluation.

The selected model is not claimed to be universally “best”.

It is the controlled reference execution model for Agent v0.1.

Later Stage 10/11 work may add a separate cross-model portability check.

## Reference-model criteria

A candidate is viable only if all **mandatory gates** pass.

### M1 — Direct API / controllable instruction stack

Must support a direct programmatic API where the harness can place:

- frozen Agent system prompt in SYSTEM / highest available custom-instruction role;
- frozen mode contract as a second SYSTEM/developer/custom-instruction layer or an equivalent deterministic composition;
- PUBLIC case as USER content.

An IDE/chat host that injects uncontrollable project/user instructions is not acceptable.

### M2 — Fresh stateless case context

Must allow one brand-new independent request context per E10 case with:

- no inherited prior conversation;
- no previous-response/session ID;
- no cross-case memory.

### M3 — Controlled tool boundary

Must support either:

- function/tool calling so the model gets exactly one constrained `read_sut_file` tool;

or another equivalently strict mechanism that preserves progressive disclosure without granting web/shell/general filesystem.

No model-visible browsing/search tool may be implicitly enabled.

### M4 — Stable model identity

Must expose a concrete model identifier that can be pinned for the whole run.

Aliases that silently float between materially different models are disfavored.

Record:
- requested model ID;
- returned/observed model identity if the API provides it.

### M5 — Context capacity

Must comfortably hold:

- Agent system prompt;
- mode contract;
- one PUBLIC case;
- multiple progressively loaded SUT files;
- tool-call history;
- final reasoning response.

Do not select a candidate whose effective context is obviously too small.

### M6 — Suite capacity / quota

Must have enough usable quota/rate capacity to complete:

- 32 cases;
- likely multi-round tool calls;
- one readiness probe;
- limited technical retries.

A model/provider that is already quota-blocked or has a known hard short window insufficient for the suite is not viable as reference.

### M7 — Architecture reasoning adequacy

The model should be a strong general reasoning/coding/architecture model, not a lightweight autocomplete model.

Do not infer this only from marketing names.

Use a small synthetic non-E10 probe set described below.

### M8 — Reproducible transport

The same endpoint/model/auth path must be usable by the future frozen runner without interactive login steps during each case.

Credentials may be loaded at runtime from local secure config/env.

Never commit secrets.

## Candidate discovery

Discover non-Kimi candidates from locally available direct API/provider configuration.

You may inspect:
- environment variable names/availability;
- local provider registries/config metadata;
- endpoint hosts;
- model IDs;
- adapter types.

You must NOT:
- print secret values;
- commit secret values;
- send secrets to logs/report;
- use web search to find credentials;
- invent unavailable credentials.

If a candidate endpoint is available through an OpenAI-compatible adapter, record that.

If native Anthropic/Google/etc. adapters would be required, record the exact transport capability gap; do not build a large framework in this selection task.

## Selection methodology

Create a candidate table.

For each discovered non-Kimi candidate record:

- candidate ID
- provider family
- API host
- model ID
- adapter type
- system-role support
- tool-calling support
- stateless request support
- observed context limit if available from local config/API metadata
- quota/readiness result
- synthetic probe result
- mandatory-gate result
- limitations

Do not rank candidates by brand prestige.

## Synthetic probe set

Use only synthetic `PRE10-*` probes.

Never use an E10 case.

At minimum:

### PRE10-R1 — System instruction obedience

A tiny prompt that proves the custom Agent system slot is actually controlling behavior.

Do not ask for hidden chain-of-thought.

### PRE10-R2 — Tool-call loop

Expose only `read_sut_file` and require reading a benign frozen SUT file such as `00_ROUTER.md`.

Verify the returned answer depends on the tool result.

### PRE10-R3 — Fresh-context separation

Issue two independent requests with distinct synthetic markers.

Verify request B does not receive marker/content from request A.

No provider conversation/session ID may be reused.

### PRE10-R4 — Architecture reasoning smoke

Give one compact, synthetic, non-suite architecture scenario that requires:

- distinguishing evidence from assumption;
- mechanism reasoning;
- a minimum correction;
- no framework-name default.

This probe is not scored against the private Stage 10 oracle.

Use only to reject obviously unsuitable weak models.

### PRE10-R5 — Good-case precision smoke

Give one compact synthetic scenario where a naive “best practice” recommendation would be wrong.

The model should avoid an obviously alarmist rewrite.

This is a coarse suitability probe, not Stage 10 scoring.

## Probe isolation

Probe cases must be newly invented and must not reproduce E10 case facts, titles, mechanisms, or expected answers.

Do not tune candidate prompts after seeing weak responses.

Each candidate gets the same probe payloads and same harness logic where transport allows.

## Generation settings

Prefer controlled settings for the future reference run.

If the candidate supports `temperature=0` consistently:
- record support;
- prefer it for reference reproducibility.

If the model/provider ignores or forbids temperature:
- record this;
- do not exclude solely for that reason if all mandatory gates pass.

Do not vary settings per probe to improve one candidate.

## Selection rule

A candidate may be selected only if M1..M8 all pass.

If multiple pass:

Prefer, in this order:

1. strongest isolation/control guarantees;
2. stable exact model identity;
3. reliable quota/capacity for the full suite;
4. strong synthetic architecture reasoning;
5. simple reproducible harness integration;
6. lower operational fragility.

Cost may be recorded but must not override evaluation integrity.

## Output decision states

Return exactly one:

- `REFERENCE_MODEL_SELECTED`
- `NO_VIABLE_NON_KIMI_MODEL`
- `BLOCKED_CREDENTIALS`
- `BLOCKED_PROVIDER_CAPABILITY`

If no candidate passes all mandatory gates, do not choose the “least bad” one.

## Required artifacts

Create only:

- `reports/STAGE10_REFERENCE_MODEL_SELECTION.md`

No harness code in this task unless absolutely required to run a tiny ephemeral probe; such probe code must stay uncommitted/outside the repo.

No E10 outputs.

## Selection report

`reports/STAGE10_REFERENCE_MODEL_SELECTION.md` must include:

1. status
2. explicit Kimi exclusion
3. frozen SUT/suite/public-pack SHAs
4. candidate inventory
5. M1..M8 matrix
6. synthetic probe methodology
7. per-candidate probe summary
8. selected reference model/provider, if any
9. exact reason for selection
10. rejected candidates + exact reason
11. generation-parameter recommendation
12. expected suite-capacity/quota note
13. required future harness adapter
14. secret-handling result
15. no-E10 confirmation
16. genuine owner decisions only

Do not include secret values.

## Mechanical validation

Before return:

1. branch starts from exact PUBLIC-pack baseline;
2. diff contains only `reports/STAGE10_REFERENCE_MODEL_SELECTION.md`;
3. no E10 file changed;
4. no Stage 2–9/SUT file changed;
5. no oracle/rubric/private coverage/design report read or added;
6. no E10 raw output exists;
7. no Kimi/Moonshot candidate is selected;
8. no secret value appears in Git diff;
9. every selected candidate passes M1..M8;
10. report names exact selected provider/model/host if selected;
11. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. selection status
4. candidate inventory
5. M1..M8 result matrix
6. synthetic probe summary
7. selected reference provider/model/host
8. selection rationale
9. rejected candidate reasons
10. generation setting recommendation
11. quota/capacity result
12. required harness adapter
13. secret-handling result
14. changed-files list
15. mechanical validation
16. exact blocker if not selected
