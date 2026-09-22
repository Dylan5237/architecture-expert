# Stage 10 Phase A — Codex + GLM Suite Remediation

## Role

Continue as the **Independent Eval Designer / Oracle Author** for Stage 10 of `Dylan5237/architecture-expert`.

This is a **bounded suite-remediation pass only** after Chief Architect review of Phase A.

Do not run the Agent.
Do not score outputs.
Do not modify the frozen SUT.
Do not create Stage 11 repairs.

## Fixed inputs

Frozen SUT:

`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Current suite-design head:

`eval/stage10-suite-design@51c4cc324eada3d77f29b908e644d66372a77cd4`

Control:

GitHub Issue #27 latest Chief Architect checkpoint.

Work only on:

`eval/stage10-suite-design`

Read this task from:

`origin/main:tasks/stage10/CODEX_SUITE_REMEDIATION.md`

without merging main into the eval-design branch.

## Worktree invariant

Use a dedicated worktree.

Fail closed unless:
- branch is exactly `eval/stage10-suite-design`;
- HEAD is exactly `51c4cc324eada3d77f29b908e644d66372a77cd4`;
- worktree is dedicated;
- shared/primary checkout is not your workspace.

Do not repair/switch/reset/stash another Agent's checkout.

## Gate status

Current suite status:

`STAGE10_SUITE_GATE: HOLD_PENDING_REMEDIATION`

The suite is NOT frozen yet.
Phase C runner remains unauthorized.

The initial case concepts/coverage are broadly accepted, but evaluation infrastructure and several oracle/public-input defects must be corrected before freeze.

## Fixed Chief Architect decisions

### OD10-A1 — Scorer panel

Keep Codex + GLM as the Phase D primary scorer.

This is acceptable because:
- the scorer is independent from the Stage 9 Agent author;
- the oracle is frozen before runs;
- raw outputs are immutable;
- ChatGPT Chief Architect independently adjudicates material failures/false positives.

No second scorer is mandatory now.

If a material scoring dispute remains after Chief Architect review, an additional scorer may be commissioned then. Do not pre-expand the panel.

### OD10-A2 — E10-027 severity/terminal

Tighten the oracle.

E10-027:
- finding: genuine excess privilege at a real trust boundary;
- acceptable finding disposition: `HIGH_CONFIDENCE_RISK`;
- BLOCKER/MUST_FIX is not acceptable without a separate material-impact argument satisfying the blocker contract;
- terminal outcome: `MIN_SAFE_FIX_IDENTIFIED`;
- minimum correction remains a read-only account + credential rotation; template fix is systemic follow-up.

Do not use NON_BLOCKING_IMPROVEMENT as the run-level terminal.

### OD10-A3 — Runner context isolation

Phase C MUST forbid supplementary context outside:

1. the frozen SUT repository at the exact SUT SHA; and
2. the current PUBLIC case payload.

No web search.
No external project repository.
No private oracle/rubric/coverage/report.
No scorer notes.
No hidden extra evidence.

The evaluated Agent may progressively load its own frozen SUT knowledge files as designed.

If the host cannot enforce this boundary or fresh-enough per-case context isolation, record the limitation and stop; do not claim a fully blinded run.

## CA10-A1 — oracle.yaml is not valid machine-readable YAML

The current `private/oracle.yaml` contains structurally invalid list indentation: 63 of 64 `must_find` / `must_not_find` list bodies begin at root indentation.

This is unacceptable for Phase D deterministic scoring.

Rewrite the oracle as valid YAML.

Canonical top-level shape:

```yaml
id: STAGE10-ORACLE
version: 2
sut_sha: 96d9ae333ffc5a8076d635b86634b5151ec0bbc5
cases:
  - id: E10-001
    expected:
      primary_mode: ARCH_REVIEW
      primary_dp: DP-002
      allowed_alternate_routes: []
      overlays: [resources, concurrency]
      required_properties: [...]
      candidate_mechanisms: [...]
      knowledge_refs: [...]
      must_find: [...]
      must_not_find: [...]
      acceptable_finding_dispositions: [...]
      expected_terminal_outcomes: [MIN_SAFE_FIX_IDENTIFIED]
      minimum_correction_expectations: [...]
      uncertainty_expectations: [...]
      product_contract_authority: [...]
      hard_failure_triggers: [...]
      ambiguity_notes: "..."
      scoring_notes: "..."
```

Exact wording may vary, but:
- valid YAML parser must load it;
- list fields must be actual YAML arrays;
- terminal outcomes and finding dispositions must be separate fields;
- every case must use the same typed schema;
- do not encode multiple list items via semicolon-delimited prose.

Do not change case meaning unless required by the corrections below.

## CA10-A2 — E10-031 oracle entry is field-shift corrupted

The current E10-031 entry is semantically misaligned:
- alternate routing contains overlays;
- overlays contain properties;
- required properties contain mechanisms;
- knowledge refs contain must-find text;
- must-find contains must-not-find text;
- must-not-find contains terminal;
- terminal contains correction;
- correction contains uncertainty;
- product contract contains HF text;
- hard-failure field contains scoring prose.

Repair E10-031 to:

- primary route: `CHANGE_REVIEW / DP-003` preferred because the incident is resolved and the live object is the pending PR;
- allowed alternate: `INCIDENT_ANALYSIS / DP-005` if the Agent explicitly frames the pass as re-attribution of the resolved incident;
- overlays: `[overload, resources]`;
- required properties:
  - checkout success/availability;
  - approved cost-efficiency goal as a real constraint/intent;
- candidate mechanism:
  - pool 500→200 reduces capacity;
  - queue remains unbounded;
  - no admission/load-control;
  - rollback correlation is strong evidence but not by itself proof of full causality;
- knowledge refs: FP-010, MP-009, D-04, Q-006 as appropriate;
- must-find:
  - capacity reduction + missing queue/admission governance;
  - availability and approved cost goal must coexist;
  - causal certainty must stay proportionate to evidence;
- must-not-find:
  - definitive “PR caused outage” without reservation;
  - abandon the approved cost goal as the architecture fix;
  - BLOCKER on the cost initiative itself;
- terminal: `MIN_SAFE_FIX_IDENTIFIED`;
- minimum correction:
  - re-land reduced pool only with capacity-aligned admission/shedding/bounds;
  - load test above baseline;
  - monitor checkout success at new capacity;
- uncertainty:
  - correlation-vs-causation gap;
- hard failures:
  - HF-10 for false causal certainty;
  - HF-06 only if wrong route materially changes result/procedure;
- ambiguity notes:
  - route choice is intentionally dual-acceptable only with concise route basis.

## CA10-A3 — terminal/disposition category mixing

Correct at least these entries:

### E10-013
- terminal: `NO_DEFECT`;
- optional documentation suggestion, if present, is a finding/disposition such as NON_BLOCKING_IMPROVEMENT, not a terminal.

### E10-025
- terminal: `NO_DEFECT` for the boundary question;
- optional testability cleanup is NON_BLOCKING_IMPROVEMENT, not a terminal.

### E10-026
- terminal: `MIN_SAFE_FIX_IDENTIFIED` because the growth mechanism has a clear correction;
- CRDT merge/convergence portion is a GOOD CASE / no-defect subfinding;
- growth finding should be `HIGH_CONFIDENCE_RISK`, not encoded as a terminal;
- do not encode “NO_DEFECT + HCR” as multiple terminal outcomes.

### E10-027
Apply OD10-A2:
- finding disposition: HIGH_CONFIDENCE_RISK;
- terminal: MIN_SAFE_FIX_IDENTIFIED.

Audit all 32 entries for the same category error.

Only canonical terminal values are:
- NO_DEFECT
- MIN_SAFE_FIX_IDENTIFIED
- NEEDS_EVIDENCE
- OWNER_TRADE_OFF
- ARCH_CONFLICT
- NO_DECISION_CHANGING_WORK

Finding dispositions are separate.

## CA10-A4 — hard-failure taxonomy needs diagnostic separation

The current HF-11 combines eval leakage and hidden-CoT behavior.

Split them:

- `HF-11 eval_leakage`: oracle/private-eval knowledge appears in Agent output or Agent behavior exploits unavailable eval information.
- `HF-12 hidden_cot_exposure`: Agent requests/exposes private step-by-step chain-of-thought contrary to the sealed contract.

Update rubric/report/manifest counts accordingly.

Do not weaken any existing hard failure.

## CA10-A5 — correct misassigned hard-failure triggers

At minimum:

- E10-004: search-team USER_ASSERTION overriding accepted product intent is not HF-04 by itself. Use HF-05 if the Agent silently weakens the accepted product contract; use HF-03 only if it invents/promotes unsupported project fact.
- E10-021: senior-engineer USER_ASSERTION producing confident cause is primarily HF-10 (false certainty) and may be HF-03 if promoted as fact without basis; remove HF-04.
- E10-022: consultant “production-grade” prescription is a framework/best-practice authority failure → HF-07, not HF-04 unless the Agent independently invokes GENERIC_KNOWLEDGE to override project evidence.
- E10-026: ignoring the real growth risk is a serious D4/D9 miss but is NOT HF-02. HF-02 is a GOOD CASE false positive, not a false negative. Remove that HF-02 trigger.

Audit all remaining hard-failure references against the registry semantics.

Do not invent new hard-failure IDs merely to make every serious miss a hard failure.

## CA10-A6 — E10-031 PUBLIC leakage/meta cue

The current PUBLIC input leaks evaluation intent through both title and runner note:

- title: `Ambiguous object: incident or PR review?`
- note: `This case deliberately combines ... the reasoning object should be identified by the agent.`

Replace with neutral plausible project wording.

Use:
- title: `Checkout pool tuning after rollback`
- notes_for_runner: `Fresh context.`

Do not otherwise change the case evidence/intent.

## CA10-A7 — public-case mojibake

Fix encoding corruption in:

- E10-004
- E10-015
- E10-018
- E10-021
- E10-023
- E10-030

Examples currently include `鈥?`, `搂`, etc.

Restore ordinary UTF-8 punctuation / section symbols without changing semantics.

After repair, scan all 32 public cases and all private design files for:
- Unicode replacement character;
- mojibake fragments;
- accidental invalid byte-decoding artifacts.

Result must be zero.

## CA10-A8 — coverage/report count reconciliation

The current self-report, coverage summary and design report disagree.

Use one explicit counting model and make all files agree.

Canonical counts to record:

- total cases: 32;
- unambiguous primary DP cases:
  - DP-001: 3
  - DP-002: 10
  - DP-003: 8
  - DP-004: 2
  - DP-005: 7
- intentionally route-ambiguous:
  - E10-024: ARCH_REVIEW/DP-002 or ADR_REVIEW/DP-004 with basis;
  - E10-031: CHANGE_REVIEW/DP-003 preferred, INCIDENT_ANALYSIS/DP-005 accepted with basis.
- public `requested_mode: AUTO` count: 19;
- strict object-vs-vocabulary / route-challenge subset: explicitly list and count it; current intended strict set is 6:
  - E10-002
  - E10-003
  - E10-006
  - E10-013
  - E10-024
  - E10-031
- strict GOOD CASE/non-alarmist count: 8;
- strict ambiguity count: 6;
- strict cross-domain count: 8.

Do not inflate counts with “partial” cases in the strict summary.

You may retain broader tagged sets separately, but name them differently.

## CA10-A9 — E10-024 allowed route must not say “any”

E10-024 is intentionally ambiguous but not route-free.

Allowed routes are only:
- ARCH_REVIEW / DP-002, or
- ADR_REVIEW / DP-004,

with a concise object-based basis.

Do not encode `AUTO→any`.

Terminal remains ARCH_CONFLICT.

## CA10-A10 — coverage.yaml must also be valid, typed YAML

Normalize `private/coverage.yaml` to proper YAML.

Requirements:
- valid parser load;
- arrays use comma-separated YAML list items, not semicolon-packed single strings;
- summary keys are normal keys, not backtick-literal pseudo-keys;
- per-case domain/tag arrays are machine-readable;
- summary counts are derived/reconciled from the 32 entries;
- ambiguous-route cases are represented without double-counting primary DP distribution.

## CA10-A11 — machine validation before freeze

Use an actual YAML parser on:

- `manifest.yaml`
- `private/oracle.yaml`
- `private/coverage.yaml`

If `rubric.md` remains Markdown, that is fine.

Validation must assert:

1. 32 public cases exactly;
2. 32 oracle entries exactly;
3. ID sets identical;
4. all required oracle keys present;
5. typed array/scalar fields have expected types;
6. terminal values belong only to the six canonical values;
7. finding-disposition values never appear in terminal fields;
8. hard-failure IDs referenced by oracle all exist in rubric registry;
9. coverage IDs exactly match public/oracle IDs;
10. summary counts reconcile to per-case data;
11. no duplicate IDs;
12. no public/private path crossover;
13. no run outputs exist.

Record the validation command/tool and result in the report.

## Allowed files

Modify only:

- `eval/stage10/design/manifest.yaml`
- `eval/stage10/design/rubric.md`
- `eval/stage10/design/private/oracle.yaml`
- `eval/stage10/design/private/coverage.yaml`
- `eval/stage10/design/public/E10-004.md`
- `eval/stage10/design/public/E10-015.md`
- `eval/stage10/design/public/E10-018.md`
- `eval/stage10/design/public/E10-021.md`
- `eval/stage10/design/public/E10-023.md`
- `eval/stage10/design/public/E10-030.md`
- `eval/stage10/design/public/E10-031.md`
- `reports/STAGE10_EVAL_SUITE_DESIGN.md`

No other file may change.
No new case may be added or removed.

## Delivery

Add exactly one remediation commit on top of `51c4cc324eada3d77f29b908e644d66372a77cd4`.

Push and stop.

## Return format

Return only:

1. branch
2. SHA
3. remediation matrix CA10-A1..A11
4. YAML parser validation result
5. final oracle schema
6. final hard-failure registry IDs
7. E10-013/025/026/027 terminal/disposition confirmation
8. E10-031 oracle confirmation
9. E10-024 allowed-route confirmation
10. public mojibake/leakage scan result
11. final canonical coverage counts
12. changed-files list
13. mechanical validation
14. suite-freeze recommendation
15. genuine new owner decisions
