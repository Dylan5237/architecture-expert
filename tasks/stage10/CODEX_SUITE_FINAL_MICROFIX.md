# Stage 10 Phase A — Codex + GLM Final Suite Gate Microfix

## Role

Continue as the **Independent Eval Designer / Oracle Author** for Stage 10.

This is a final bounded suite-gate microfix after Chief Architect re-review.

Do not run the Agent.
Do not score outputs.
Do not modify the frozen SUT.
Do not change case count, rubric dimensions, hard-failure taxonomy, or coverage counts.

## Fixed inputs

Frozen SUT:
`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Current suite head:
`eval/stage10-suite-design@056a6bd08793d9a79b2e75f1548097819aaa9b9c`

Control:
Issue #27 latest Chief Architect checkpoint.

Work only on:
`eval/stage10-suite-design`

Dedicated worktree only. Do not touch shared checkout.

## Why this microfix exists

Chief Architect independently re-audited the typed oracle after the first remediation and found one remaining Stage 8 category error plus one public meta-cue in E10-024.

All other remediated suite-gate findings remain accepted.

## R10A2-1 — Fix E10-024 finding/terminal category error

In `eval/stage10/design/private/oracle.yaml`, E10-024 currently contains:

`acceptable_finding_dispositions: [ARCH_CONFLICT]`

This is invalid.

Stage 8 canonical typing:

Finding dispositions are only:
- BLOCKER / MUST_FIX
- HIGH_CONFIDENCE_RISK
- NEEDS_EVIDENCE
- NON_BLOCKING_IMPROVEMENT
- PERSONAL_PREFERENCE

`ARCH_CONFLICT` is a run-level terminal outcome plus its own conflict record. It is NOT a finding disposition.

For E10-024:
- set `acceptable_finding_dispositions: []` unless a separate ordinary finding is explicitly required (none is required by this oracle);
- keep `expected_terminal_outcomes: [ARCH_CONFLICT]`;
- keep the required ARCH_CONFLICT record expectations in `minimum_correction_expectations` / authority fields;
- do not add a blocker finding merely to fill the list.

Then audit all 32 oracle records and assert:
- every `acceptable_finding_dispositions` value belongs only to the canonical finding-disposition enum;
- every `expected_terminal_outcomes` value belongs only to the canonical terminal enum.

Chief Architect's independent scan found E10-024 as the only remaining violation; verify this after the edit.

## R10A2-2 — Neutralize E10-024 public meta-cue

Current PUBLIC metadata tells the evaluated Agent the answer too directly:

- title: `Feature freeze vs regulatory deadline conflict`
- task_object: `a real conflict between two accepted requirements`

The user_request/evidence already naturally presents the tension. Evaluation metadata must not pre-classify it as a conflict.

Change only the metadata framing to neutral project language.

Use:

- title: `Quarter planning: feature freeze and regulatory export deadline`
- task_object: `quarter planning architecture decision under fixed team capacity`

Keep:
- requested_mode = AUTO;
- user_request unchanged;
- all project evidence unchanged;
- constraints unchanged;
- notes_for_runner = Fresh context.

Do not remove the real user-visible facts that make ARCH_CONFLICT discoverable.

## R10A2-3 — Mark the canonical post-remediation state clearly

Update `eval/stage10/design/manifest.yaml`:
- status: `READY_FOR_FREEZE`
- preserve all existing exposure and Phase C isolation rules.

Append a short final-gate microfix note to `reports/STAGE10_EVAL_SUITE_DESIGN.md` stating:
- E10-024 typed category correction;
- public metadata neutralization;
- all 32 finding-disposition + terminal enums mechanically revalidated;
- no coverage/rubric/case-count change;
- recommendation remains FREEZE.

Do not rewrite historical report sections solely for cosmetic consistency. The remediation addenda are the authoritative later record.

## Allowed files

Modify only:

- `eval/stage10/design/private/oracle.yaml`
- `eval/stage10/design/public/E10-024.md`
- `eval/stage10/design/manifest.yaml`
- `reports/STAGE10_EVAL_SUITE_DESIGN.md`

No other files may change.

## Mechanical validation

Before completion verify:

1. branch descends from `056a6bd08793d9a79b2e75f1548097819aaa9b9c`;
2. exactly one microfix commit added;
3. diff contains only the four authorized files;
4. oracle parses as YAML;
5. oracle still has exactly 32 records;
6. all 32 `acceptable_finding_dispositions` values are in the five canonical finding-disposition families (BLOCKER/MUST_FIX treated as one family);
7. all 32 `expected_terminal_outcomes` values are among the six canonical terminal outcomes;
8. E10-024 finding-disposition list is empty;
9. E10-024 terminal remains ARCH_CONFLICT;
10. E10-024 allowed routes remain only ARCH_REVIEW/DP-002 primary and ADR_REVIEW/DP-004 alternate with basis;
11. E10-024 public title/task_object are neutralized exactly as specified;
12. no PUBLIC oracle/scoring fields introduced;
13. manifest status = READY_FOR_FREEZE;
14. case count, coverage counts, rubric and HF registry unchanged;
15. no run outputs;
16. no Stage 2–9 artifacts changed;
17. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. R10A2-1..3 completion matrix
4. typed-enum validation result
5. E10-024 oracle confirmation
6. E10-024 public leakage confirmation
7. changed-files list
8. mechanical validation result
9. suite-freeze recommendation
10. genuine new owner decisions
