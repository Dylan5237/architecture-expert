# Stage 11A — Fresh 12-Case Holdout Design and Freeze

## Role

You are the **Independent Holdout Designer** for `Dylan5237/architecture-expert`.

Stage 10 is complete and adjudicated.

Canonical baseline:
- Agent v0.1 SUT: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- Stage 10 evidence: `d6ac48c16f7285f53fbc7af6e5aae4f64f83123b`
- Stage 10 scorer: `c32adbdac7f4a74077d2ec3235e8feb76aadc0ce`
- Chief Architect adjudication: `1621916b4f0bef8c5ceb7f43b30ca473416dea03`
- final score: 434/538 = 80.67%
- dominant defect: evidence discipline
- secondary defects: terminal selection and correction-guarantee boundaries

This task designs a **fresh sealed holdout before Agent v0.2 is implemented**.

Do NOT repair the Agent.
Do NOT edit Stage 10 cases.
Do NOT reuse Stage 10 scenario facts, titles, numbers, or answer structures.

## Work branch

Use only:

`eval/stage11-holdout-design`

Starting HEAD:

`1621916b4f0bef8c5ceb7f43b30ca473416dea03`

Dedicated clean worktree.

Read this task from:

`origin/main:tasks/stage11/CODEX_STAGE11_HOLDOUT_DESIGN.md`

Do not merge main.

## Reuse the frozen scoring contract

Reuse Stage 10 rubric semantics exactly:

- D1..D10
- HF-01..HF-12
- typed terminal outcomes
- route/DP semantics
- GOOD CASE precision
- authority/evidence rules

Do not invent a new scoring taxonomy.

You may copy the rubric file unchanged into the holdout design tree only if needed for self-contained scoring; otherwise reference the Stage 10 frozen rubric by SHA.

## Holdout size

Exactly **12 cases**.

All cases must be newly authored and materially different from Stage 10 scenarios.

The holdout should be small but discriminating.

## Coverage requirements

Design exactly:

### H-EVIDENCE — 4 cases
Stress sentence-level epistemic discipline:
- unsupported numeric inference;
- missing/ambiguous temporal order;
- absent-vs-not-provided distinction;
- causal inference from incomplete telemetry.

At least:
- 1 incident case;
- 1 change-review case;
- 1 architecture-design/review case;
- 1 case where the correct result is still a positive finding but project-specific detail must remain unknown.

### H-TERMINAL — 2 cases
Stress terminal selection:
- one true OWNER_TRADE_OFF;
- one true NEEDS_EVIDENCE or NO_DECISION_CHANGING_WORK where a local fix exists but does not resolve the main decision.

### H-GUARANTEE — 2 cases
Stress minimum-correction sufficiency:
- proposed local correction protects only part of the accepted guarantee;
- hidden relationship/bound must remain explicit rather than being assumed.

### H-GOODCASE — 2 cases
Protect existing strengths:
- materially compliant architecture that looks suspicious by pattern name;
- bounded/legal use of retry/cache/async/shared state where a naive reviewer would over-flag.

### H-ROUTING — 1 case
Genuine object/routing ambiguity with an explicitly allowed alternate route.

### H-CROSS — 1 case
Cross-domain case combining:
- product contract/authority;
- one runtime mechanism;
- one evolution/integration dimension.

Total: 12.

## Shape diversity

Across the 12 include at least 7 distinct system shapes, selected from:
- desktop/local
- backend
- embedded
- data pipeline
- developer tooling
- mobile/backend
- local-first
- distributed workflow
- public API/integration
- batch/ML platform
- edge/IoT

Do not overuse microservices/backend-only scenarios.

## Difficulty

Each case must:
- contain enough project evidence to support a bounded architecture judgment;
- contain at least one tempting but invalid inference;
- avoid trivia or word-match answers;
- require mechanism reasoning, not pattern recall;
- be answerable from frozen Architecture Expert knowledge plus case evidence.

At least 3 cases must be GOOD/non-alarm or partial-non-alarm.
At least 3 cases must require explicit uncertainty.
At least 3 cases must exercise accepted product/architecture authority.

## Files

Create:

`eval/stage11/holdout/design/manifest.yaml`
`eval/stage11/holdout/design/public/H11-001.md` .. `H11-012.md`
`eval/stage11/holdout/design/private/oracle.yaml`
`eval/stage11/holdout/design/private/coverage.yaml`
`reports/STAGE11_HOLDOUT_DESIGN.md`

Do not create run outputs.

## Public case format

Use the same general public format as Stage 10:
- id
- neutral title
- task_object
- requested_mode
- user_request
- project_evidence
- constraints
- notes_for_runner

No oracle IDs, mechanism names, tactic IDs, verdict hints, or scoring hints in PUBLIC text.

## Private oracle

One entry per case with:
- primary mode
- primary DP
- allowed alternate routes
- overlays
- required properties
- candidate mechanisms
- knowledge refs
- must_find
- must_not_find
- acceptable finding dispositions
- expected terminal outcomes
- minimum correction expectations
- uncertainty expectations
- product-contract authority
- hard-failure triggers
- ambiguity notes
- scoring notes

Do not weaken the frozen HF taxonomy.

## Coverage

coverage.yaml must make the 12-case distribution auditable:
- category above (H-EVIDENCE etc.)
- mode
- DP
- shape
- domains
- goodcase/nonalarm
- ambiguity
- product-contract surface
- expected terminal family

## Pass criteria for Stage 11 validation

Freeze these criteria now, before v0.2 exists.

Stage 11 will run **both v0.1 and v0.2** on the same sealed 12-case holdout before oracle unsealing.

The v0.2 holdout gate passes only if:

1. D3 evidence-discipline percentage improves by **at least 20 percentage points** vs v0.1 on this holdout;
2. HF-03 count decreases by **at least 50%** vs v0.1;
3. no new HF-02, HF-05, HF-06, HF-07, or HF-09 appears compared with v0.1;
4. primary-route acceptance is not lower than v0.1;
5. strict GOOD CASE false-positive count is not higher than v0.1;
6. overall applicable-point percentage is not lower than v0.1;
7. no v0.2 case reveals holdout/private-eval leakage.

If v0.1 has zero HF-03 on this holdout, criterion 2 becomes:
- v0.2 must also have zero HF-03,
while criterion 1 still applies unless v0.1 D3 is already >=90%, in which case v0.2 must not regress D3 by more than 2 percentage points.

These criteria are frozen before any v0.2 measured output.

## Blindness / isolation

After design freeze:
- repair executor must not read this branch or any holdout public/private file;
- neither v0.1 nor v0.2 runner may access private oracle/coverage;
- private oracle/rubric unseals only after both holdout runs are fixed;
- do not merge this branch before both runs.

## Design self-review

Before freeze, verify:
- exactly 12 public cases;
- exactly 12 oracle entries;
- no duplicate scenario family copied from Stage 10;
- coverage totals match;
- at least 7 shapes;
- category counts exactly 4/2/2/2/1/1;
- public leakage scan passes;
- pass criteria recorded in manifest/report;
- no Agent v0.2 content exists or is assumed.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. status
4. 12-case category distribution
5. mode/DP distribution
6. shape count and list
7. GOOD CASE count
8. uncertainty count
9. product-contract count
10. leakage audit result
11. frozen Stage 11 pass criteria
12. changed-files summary
13. mechanical validation
14. blocker if any
