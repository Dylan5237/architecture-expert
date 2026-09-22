# Stage 10 Phase C0 — Codex Isolated API Runner Harness + Preflight

## Role

You are the **Stage 10 Evaluation Harness Engineer** for `Dylan5237/architecture-expert`.

This is **Phase C0 only**: build and prove an isolated direct-model runner harness.

Do NOT run E10-001..032.
Do NOT read the private oracle/rubric/coverage/design report.
Do NOT score anything.
Do NOT modify the frozen Agent v0.1.

The prior Cursor/Grok attempt correctly failed closed because the IDE host could not guarantee:
- Agent system-prompt precedence;
- fresh per-case context;
- tool/context isolation.

Your task is to remove that **RUNTIME/HARNESS** blocker without changing the SUT.

## Fixed inputs

Frozen Agent v0.1 SUT:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Frozen suite-design SHA:

`ff157eb1947860345a305fb29452b51e09dd3a2b`

Frozen public-pack baseline:

`23a49382c949702446325d30e18d3321d8550c36`

Work branch:

`eval/stage10-api-runner`

The branch is created from the public-pack baseline and therefore contains:
- frozen SUT lineage;
- 32 PUBLIC cases;
- public manifest;
- the earlier Cursor runner protocol.

It contains no private oracle/rubric/coverage/design report.

Read this task from:

`origin/main:tasks/stage10/CODEX_API_RUNNER_PREFLIGHT.md`

Do not merge main.

## Worktree / repository isolation

Use one dedicated worktree or single-branch clone for `eval/stage10-api-runner`.

Do not inspect or repair any other local worktree/checkout.

Do not fetch/read:
- `eval/stage10-suite-design`;
- `eval/stage10-blinded-run`;
- any private evaluation branch/ref.

After reading this task from origin/main, do not use other refs for evaluation content.

## Target harness architecture

Build a small **direct model API** runner that can later execute one fresh, isolated API conversation per case.

The canonical Agent remains provider-independent. The evaluation harness may contain provider adapters.

The runner must guarantee by construction:

1. `agent/system-prompt-v0.1.md` is sent in the provider's SYSTEM / highest available custom-instruction role.
2. The selected mode contract is also supplied as custom instruction beneath/with the Agent system contract, not as project evidence.
3. Each case starts with a new message array / request context and no prior conversation identifier.
4. The model receives only:
   - Agent system contract;
   - selected mode contract;
   - current PUBLIC case payload;
   - explicit read-only SUT file tool results requested during that case.
5. The model has no web, shell, general filesystem, connected-app, GitHub, branch, or arbitrary network tool.
6. The only tool exposed to the evaluated model is a constrained read-only SUT file tool.
7. The SUT file tool reads from a snapshot/materialization of exactly `SUT_SHA`, not from moving main or the runner branch's eval files.
8. The tool cannot read:
   - `.git`;
   - `eval/stage10/**`;
   - Stage 10 tasks/results;
   - other cases;
   - external paths.
9. Missing project evidence remains missing.
10. No private eval material is present in the model-visible context or tool root.

## Provider configuration

Do not assume a provider/model name that is not configured.

Implement a minimal provider adapter boundary.

Required first adapter:
- an OpenAI-compatible chat-completions style endpoint supporting SYSTEM messages and function/tool calling.

Configuration MUST come from runtime environment/config, not committed secrets.

Canonical environment interface:

- `STAGE10_API_BASE_URL`
- `STAGE10_API_KEY`
- `STAGE10_MODEL`

Optional:
- `STAGE10_API_HEADERS_JSON` for non-secret additional headers only; do not permit API keys to be committed through this file/interface.

You MAY safely inspect whether existing local provider configuration can populate these values, including an existing local Codex/model-provider configuration, but:
- never print/log secret values;
- never commit credentials;
- never copy a token into repo files;
- if you cannot obtain a direct endpoint + model + auth without exposing secrets, return BLOCKED_CONFIG.

Do not silently use the Codex/GLM conversational subagent itself as the SUT. The SUT must be invoked through the isolated runner API path you build.

## Model transport exception

The Stage 10 "no web/external context" rule does NOT forbid the network call to the configured model inference endpoint itself.

The inference endpoint is transport, not a source of project facts.

The evaluated model must have no separate web/search/browsing tool.

## SUT snapshot

At harness start:

- materialize a temporary read-only SUT tree from exactly:
  `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- verify required files exist, including:
  - `agent/system-prompt-v0.1.md`
  - `agent/modes/AUTO.md`
  - five explicit mode files
  - Stage 7/8 runtime knowledge files.

Do not use the runner branch worktree as the read tool root.

Recommended implementation:
- `git archive <SUT_SHA>` to a temp directory;
- read-only allowlisted file function rooted there;
- path normalization + traversal rejection.

Do not expose Git itself as a model tool.

## Mode mapping

Use PUBLIC `requested_mode`:

- AUTO -> `agent/modes/AUTO.md`
- ARCH_DESIGN -> `agent/modes/ARCH_DESIGN.md`
- ARCH_REVIEW -> `agent/modes/ARCH_REVIEW.md`
- CHANGE_REVIEW -> `agent/modes/CHANGE_REVIEW.md`
- ADR_REVIEW -> `agent/modes/ADR_REVIEW.md`
- INCIDENT_ANALYSIS -> `agent/modes/INCIDENT_ANALYSIS.md`

Mode text must not be modified.

## System/custom instruction mapping

Preferred canonical mapping:

- provider SYSTEM message = exact `agent/system-prompt-v0.1.md`;
- second SYSTEM message (or equivalent custom-instruction field) = exact selected mode contract;
- USER message = exact current PUBLIC case payload.

If the provider supports only one SYSTEM message:
- concatenate the exact Agent system prompt + an explicit delimiter + exact mode contract;
- record this mapping;
- do not paraphrase either contract.

Provider hidden safety/system instructions are accepted platform constraints.

The requirement is that no IDE/project/user-rule custom instruction sits above the frozen Agent contract.

## Read-only tool

Expose exactly one evaluated-model tool conceptually equivalent to:

`read_sut_file(path: string) -> UTF-8 contents | controlled error`

Requirements:
- relative paths only;
- no traversal;
- file only, no directory listing;
- SUT snapshot root only;
- deny `eval/`, `.git/`, and any path outside snapshot;
- size cap per call;
- total read budget per case;
- log requested path + byte count only, not hidden reasoning;
- no tool for shell/web/write/list/git/env.

The tool is evaluation infrastructure, not a new Agent semantic.

## Fresh-context guarantee

The eventual runner must create a new conversation/messages array for every case.

No:
- previous response IDs;
- conversation/session IDs;
- prior case messages;
- prior raw output;
- shared mutable model-side thread.

Provider-side generic stateless caching is not treated as conversation memory if no prior-case content is referenced.

Record the exact API mechanism used.

## Phase C0 preflight only

Do NOT use any E10 case for preflight.

Create a synthetic non-suite probe inside the harness, e.g. `PRE10-SMOKE`, which contains no oracle knowledge and is never scored.

The preflight must prove:

### P0-1 System instruction placement

Show mechanically from request construction that the frozen Agent system prompt occupies the provider SYSTEM/highest custom slot.

Do not log the whole prompt; record hash + role placement.

### P0-2 Mode instruction placement

Show the synthetic probe uses one real frozen mode contract in the custom-instruction stack.

Record mode file hash + role placement.

### P0-3 Fresh request

Use a brand-new request/messages array with no conversation/previous-response ID.

### P0-4 Tool availability boundary

The evaluated model receives only the read-only SUT file tool.

No web/shell/filesystem/list/write tools.

### P0-5 Allowed SUT read

The synthetic probe must cause or directly test an allowed read such as `00_ROUTER.md`.

### P0-6 Forbidden read rejection

Harness unit/preflight checks must prove reads for:
- `../...`
- `eval/stage10/...`
- absolute path
are rejected before filesystem access.

Do not ask the model to attack the sandbox; test the function directly.

### P0-7 No private eval material

Assert private oracle/rubric/coverage/design report paths do not exist inside the SUT snapshot/tool root.

### P0-8 Model response

Make exactly one synthetic substantive model call through the configured provider.

Its content is not scored.

The purpose is only to prove the transport/system/tool loop works.

Do not tune the Agent based on this response.

## Required artifacts

Create only:

- `eval/stage10/harness/README.md`
- `eval/stage10/harness/runner.py`
- `eval/stage10/harness/provider_openai_compatible.py`
- `eval/stage10/harness/PREFLIGHT.md`

You may additionally create one dependency file ONLY if actually necessary:
- `eval/stage10/harness/requirements.txt`

No E10 raw outputs.
No run metadata for E10 cases.
No SUT/public-case modifications.

## PREFLIGHT.md

Record:

- status: PASS | BLOCKED_CONFIG | BLOCKED_PROVIDER_CAPABILITY | BLOCKED_ISOLATION
- SUT SHA
- public-pack SHA
- harness commit SHA if known at readback
- provider class
- model identity
- API base host (host only; redact query/path if sensitive)
- secret-source names used, never secret values
- system prompt SHA-256
- mode contract SHA-256
- request-role mapping
- fresh-context mechanism
- tool list exposed to model
- SUT snapshot mechanism
- allowed-read result
- forbidden-read tests
- private-eval absence check
- synthetic call result status
- any limitations.

Never include API keys/tokens.

## Fail closed

Return BLOCKED rather than weakening isolation if any of these is true:

- no suitable direct API config;
- provider cannot accept a system/custom instruction;
- provider cannot support the constrained read tool loop required for progressive disclosure;
- model call implicitly gains web/tool access outside harness control;
- fresh stateless request cannot be guaranteed;
- SUT snapshot cannot be isolated from eval/private files.

Do not fall back to Cursor Task subagents, Codex conversational subagents, one long chat, or plain user-prompt injection.

## Mechanical validation

Before return:

1. branch starts from the fixed public-pack baseline;
2. diff contains only the authorized harness files;
3. no E10 public case modified;
4. no SUT/Agent/Stage 2–9 file modified;
5. no `eval/stage10/run/raw/` exists;
6. no oracle/rubric/private coverage/design report exists in branch;
7. no secret value appears in Git diff;
8. Python syntax check passes;
9. path sandbox unit checks pass;
10. if PASS, exactly one synthetic provider call completed;
11. if PASS, SYSTEM mapping and tool isolation are documented;
12. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. preflight status
4. provider/model
5. system-prompt precedence mapping
6. mode-contract mapping
7. fresh-context mechanism
8. model-visible tool list
9. SUT snapshot/isolation result
10. allowed/forbidden read test result
11. synthetic provider call result
12. secret-handling result
13. changed-files list
14. mechanical validation
15. exact blocker if not PASS
