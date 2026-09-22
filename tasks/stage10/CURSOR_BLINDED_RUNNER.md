# Stage 10 Phase C — Cursor Blinded Agent v0.1 Runner

## Role

You are the **Blinded SUT Runner** for Stage 10 of `Dylan5237/architecture-expert`.

You are NOT the scorer.
You are NOT an eval designer.
You are NOT allowed to repair the Agent.

Your job is only to execute the frozen Agent v0.1 against the frozen PUBLIC case set and preserve raw outputs + run metadata.

## Frozen inputs

Frozen Agent v0.1 SUT:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Frozen suite-design SHA:

`ff157eb1947860345a305fb29452b51e09dd3a2b`

Runner-visible branch:

`eval/stage10-blinded-run`

The exact runner baseline SHA is recorded in GitHub Issue #27 latest Chief Architect checkpoint.

Read only files reachable from the current runner branch.

## Isolation is a gate, not a preference

Before any case run, prove all of the following.

### Repository isolation

Use a dedicated runner workspace that exposes only this runner branch.

Preferred setup:
- fresh single-branch clone/workspace of `eval/stage10-blinded-run`;
- no fetch of other branches/refs;
- do not inspect other local clones/worktrees;
- do not inspect branch history/objects outside what is reachable from this branch.

The shared/primary checkout is not part of this task. Do not repair, switch, reset, stash, or inspect it.

### Context isolation

Each E10 case must execute in a **fresh model context/session**.

A case context may receive only:
1. the frozen Agent v0.1 system/behavior contract from this branch;
2. the mode contract selected by the PUBLIC case's `requested_mode` (AUTO or explicit mode);
3. files from the frozen SUT branch that the Agent itself progressively loads;
4. the current PUBLIC case payload.

It must NOT receive:
- another E10 case;
- prior raw outputs;
- controller summaries of prior cases;
- oracle/rubric/coverage/scorer notes;
- Stage 10 suite-design report;
- web results;
- connected apps/project sources;
- external repositories.

If your host cannot guarantee fresh-enough per-case model contexts, STOP before E10-001 and return:

`RUNNER_BLOCKED_CONTEXT_ISOLATION`

Do not degrade to a single long conversation and call it blinded.

### Instruction precedence

For each fresh case run, apply:

`agent/system-prompt-v0.1.md`

as the highest available custom Agent instruction for the evaluated model.

Then provide the PUBLIC requested-mode contract:
- AUTO -> `agent/modes/AUTO.md`
- ARCH_DESIGN -> `agent/modes/ARCH_DESIGN.md`
- ARCH_REVIEW -> `agent/modes/ARCH_REVIEW.md`
- CHANGE_REVIEW -> `agent/modes/CHANGE_REVIEW.md`
- ADR_REVIEW -> `agent/modes/ADR_REVIEW.md`
- INCIDENT_ANALYSIS -> `agent/modes/INCIDENT_ANALYSIS.md`

Record how the host mapped the system-prompt file into the model's instruction hierarchy.

If the host cannot apply the system prompt as a system/custom instruction and can only treat it as ordinary untrusted case text, STOP and record:

`RUNNER_BLOCKED_PROMPT_PRECEDENCE`

Do not silently evaluate a different prompt configuration.

## External-context prohibition

For the entire run:

- no web search;
- no external repositories;
- no GitHub browsing outside the current runner branch;
- no connected project sources;
- no private eval-design branch;
- no oracle/rubric/coverage/design report;
- no extra project facts beyond the current case.

The evaluated Agent MAY load generic architecture source files that already exist inside the frozen SUT repository when its own progressive-disclosure contract justifies doing so.

Missing case evidence must remain missing.

## Case set

Public manifest:

`eval/stage10/public/manifest.yaml`

Cases:

`eval/stage10/public/E10-001.md` through `E10-032.md`

Run in ascending case-ID order.

Do not skip, reorder, merge, rewrite, summarize, or normalize case payloads.

## Per-case execution protocol

For each case:

1. create a fresh model context/session;
2. install/apply the frozen system prompt as described above;
3. provide the matching PUBLIC mode contract;
4. provide the current PUBLIC case file verbatim;
5. allow the evaluated Agent to read only the frozen SUT files it needs under its progressive-disclosure rules;
6. capture the final user-visible Agent response verbatim;
7. save it to:
   `eval/stage10/run/raw/<CASE_ID>.md`;
8. record run metadata;
9. destroy/close the case context before the next case.

Do not add hints, clarifications, critiques, corrections, or follow-up questions to improve the answer.

If the Agent itself asks the user for a clarification, preserve that response as the canonical raw output for that case. Do not answer the clarification on the Agent's behalf unless the PUBLIC case itself already supplies the answer.

## Canonical-attempt policy

Default: exactly **one substantive model attempt per case**.

A technical retry is allowed only when:
- the attempt failed before any substantive model response was produced; and
- the failure is clearly runtime/harness-level.

If a technical retry occurs:
- preserve the failed-attempt metadata/error;
- increment attempt count;
- never overwrite or hide it.

Once a substantive model response exists, do not rerun that case to seek a better answer.

## Raw-output integrity

Raw response files must contain the evaluated Agent's final user-visible response only.

Do not:
- edit wording;
- fix formatting;
- inject route labels that the Agent omitted;
- remove mistakes;
- append runner commentary.

Runner commentary belongs only in metadata/status files.

## Run metadata

Create:

`eval/stage10/run/metadata.yaml`

Top-level fields:

- stage: 10
- phase: C
- sut_sha
- suite_design_sha
- public_pack_sha
- runner_branch
- host
- model
- model_version_if_visible
- prompt_precedence_mapping
- fresh_context_mechanism
- external_context_boundary
- case_order
- started_at
- completed_at
- cases

For every case record:

- id
- requested_mode
- observed_host_model
- fresh_context: true/false
- attempt_count
- technical_retry_count
- start_order
- raw_output_path
- runner_status: OK | TECHNICAL_ERROR | BLOCKED
- technical_errors: []
- notes

Unknown metadata must be written as `UNKNOWN`. Do not invent it.

Do NOT record scores, expected answers, oracle judgments, or runner opinions.

## Status file

Create:

`eval/stage10/run/RUN_STATUS.md`

It may contain only:
- frozen SUT SHA;
- frozen suite SHA;
- public pack SHA;
- number of cases attempted/completed;
- isolation status;
- technical failures/limitations;
- whether any case had a technical retry;
- final run state:
  - COMPLETE
  - BLOCKED
  - PARTIAL_TECHNICAL_FAILURE

No scoring or qualitative evaluation.

## Failure handling

### Before first case

If repository isolation, context isolation, or prompt precedence cannot be enforced:
- do not run any cases;
- create only `eval/stage10/run/RUNNER_BLOCKED.md`;
- describe the exact runtime limitation;
- commit/push it;
- stop.

### During the run

If isolation is compromised after some cases:
- stop immediately;
- preserve completed raw outputs;
- mark run BLOCKED;
- never continue and pretend full blindness.

If one case hits a technical error:
- apply the canonical-attempt policy;
- if unrecoverable, preserve the error and continue only if the failure does not compromise isolation for later cases.

## No evaluation behavior

You must NOT:
- score outputs;
- identify expected findings/non-findings;
- label hard failures;
- compare raw responses to each other;
- tune Agent instructions;
- patch the system prompt/modes/knowledge;
- produce a Stage 11 repair proposal.

Those belong to Phase D / Stage 11.

## Authorized output files

If the full run executes:

- `eval/stage10/run/raw/E10-001.md` .. `E10-032.md`
- `eval/stage10/run/metadata.yaml`
- `eval/stage10/run/RUN_STATUS.md`

No other file may change.

If blocked before case execution:
- only `eval/stage10/run/RUNNER_BLOCKED.md` may be added.

## Git delivery

Start from the exact runner baseline SHA recorded in Issue #27.

Do not merge/fetch another branch.

After the run:
- verify no SUT/public case/task file changed;
- add exactly one run-result commit;
- push `eval/stage10-blinded-run`;
- stop.

## Mechanical validation

For COMPLETE:

1. branch descends from the fixed public-pack baseline;
2. exactly 32 raw files exist;
3. IDs E10-001..032 are complete and unique;
4. each raw file is non-empty;
5. metadata has exactly 32 case records;
6. every metadata raw_output_path resolves;
7. every case says whether context was fresh;
8. no score/oracle/HF fields exist in metadata/status;
9. no public case/SUT/Agent artifact changed;
10. no private eval artifact exists in the runner-visible tree;
11. no web/external-context retrieval was used;
12. one substantive response max per case;
13. any technical retry is preserved in metadata;
14. run status is COMPLETE only if all 32 canonical outputs exist and isolation held throughout;
15. remote HEAD equals reported SHA.

## Return format

Return only:

1. branch
2. SHA
3. run state
4. SUT SHA
5. suite-design SHA
6. public-pack baseline SHA
7. host/model identity
8. prompt-precedence mapping
9. fresh-context mechanism
10. completed case count
11. technical retry count
12. isolation result
13. raw-output inventory result
14. changed-files summary
15. mechanical validation
16. exact blocker/limitation, if any
