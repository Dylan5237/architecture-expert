# Stage 10 Phase D — Score the Complete Blinded Run and Diagnose Agent Defects

## Role

You are the **Stage 10 Independent Scorer** for `Dylan5237/architecture-expert`.

Phase C is now COMPLETE.

Canonical measured evidence:

- runtime freeze SHA: `7db2639044d3a8f0b8706d70161513238ed29670`
- evidence SHA: `d6ac48c16f7285f53fbc7af6e5aae4f64f83123b`
- run_id: `phasec-20260930T101227Z-7db26390`
- provider: company compute gateway
- selected model: `glm-5.3`
- 32/32 cases complete
- 32 non-empty raw outputs
- zero case/provider/transport retries
- zero rate-limit events
- zero duplicate outputs
- reconciliation PASS

Frozen evaluation design:

`ff157eb1947860345a305fb29452b51e09dd3a2b`

This task unlocks the private oracle/rubric for the first time after Phase C completion.

Do NOT modify any measured raw output.
Do NOT rerun any case.
Do NOT use web/external information.
Do NOT reinterpret the oracle after seeing scores.

## Work branch

Use only:

`eval/stage10-phase-d-scoring`

Starting HEAD:

`d6ac48c16f7285f53fbc7af6e5aae4f64f83123b`

Dedicated clean worktree.

Read this task from:

`origin/main:tasks/stage10/CODEX_PHASE_D_SCORING.md`

Do not merge main.

## Frozen scoring sources

Read measured outputs from current branch:

- `eval/stage10/run/raw/E10-001.md` .. `E10-032.md`
- `eval/stage10/run/metadata.json`
- `eval/stage10/run/RUN_STATUS.md`
- corresponding PUBLIC cases already present in the branch

Read scorer-only design files directly from the frozen suite-design commit using `git show` or equivalent read-only Git access:

- `ff157eb1947860345a305fb29452b51e09dd3a2b:eval/stage10/design/rubric.md`
- `ff157eb1947860345a305fb29452b51e09dd3a2b:eval/stage10/design/private/oracle.yaml`
- `ff157eb1947860345a305fb29452b51e09dd3a2b:eval/stage10/design/private/coverage.yaml`
- `ff157eb1947860345a305fb29452b51e09dd3a2b:eval/stage10/design/manifest.yaml`

Do not copy or edit the oracle/rubric.

## Scoring contract

Score every case E10-001..032 against the frozen rubric.

Dimensions:

- D1 routing_correctness
- D2 property_understanding
- D3 evidence_discipline
- D4 mechanism_accuracy
- D5 goodcase_precision
- D6 min_correction
- D7 product_contract_authority
- D8 uncertainty_evidence
- D9 finding_terminal
- D10 scope_discipline

Use only:
- 0
- 1
- 2
- N/A only where the rubric explicitly permits it

Verbosity never increases score.

## Hard failures

Evaluate HF-01..HF-12 exactly as frozen.

For every hard failure:

- record case ID
- HF code
- exact output evidence/pointer
- oracle/rubric basis
- affected dimension(s)
- why the trigger is satisfied

Do not infer a hard failure from stylistic disagreement.

One hard failure caps the affected dimension(s) at 0 and is also tracked separately.

## Per-case score record

Create:

`eval/stage10/scoring/case-scores.yaml`

One entry per case with:

- id
- primary route observed
- oracle primary route
- route verdict
- D1..D10 score or N/A
- dimension rationales, concise and evidence-based
- hard_failures
- key strengths
- key defects
- terminal outcome observed
- terminal outcome expected
- scoring confidence: HIGH / MEDIUM / LOW
- adjudication_required: true/false

Set `adjudication_required=true` for:
- any hard failure;
- any material GOOD CASE false positive;
- any route ambiguity where scorer selects a non-oracle primary route outcome;
- any score that depends on genuinely ambiguous interpretation.

## Aggregate score

Create:

`reports/STAGE10_PHASE_D_SCORECARD.md`

Include:

1. canonical evidence SHA / suite-design SHA / SUT SHA / run_id / model
2. integrity statement: 32/32 COMPLETE, no scoring-time rerun
3. overall dimension totals:
   - earned points
   - applicable max points
   - percentage
4. overall aggregate:
   - sum earned / sum applicable max
   - percentage
5. hard-failure count by HF code
6. number of cases with >=1 hard failure
7. per-case score summary
8. route accuracy
9. terminal-outcome accuracy
10. GOOD CASE / non-alarm precision
11. ambiguity / NEEDS_EVIDENCE handling
12. product-contract authority handling
13. cross-domain cases
14. AUTO-route challenge cases
15. scores grouped by DP/mode where coverage permits
16. clear statement that this score is for Agent v0.1 instantiated on `glm-5.3` under the frozen Stage 10 harness, not a provider-independent universal score

For grouped metrics, use frozen `coverage.yaml`; do not invent categories.

## Defect diagnosis

Create:

`reports/STAGE10_PHASE_D_DEFECT_DIAGNOSIS.md`

Cluster observed defects by likely layer:

- AGENT_PROMPT / MODE_ROUTING
- REASONING_PLAYBOOK
- KNOWLEDGE_RETRIEVAL / ROUTER
- KNOWLEDGE_CONTENT / RELATIONSHIP MAP
- EVIDENCE_DISCIPLINE
- OUTPUT_CONTRACT
- MODEL_BEHAVIOR / UNCERTAIN
- EVAL_CASE / ORACLE_AMBIGUITY

For each cluster:

- affected cases
- evidence
- likely mechanism
- severity
- whether the defect is systematic or isolated
- smallest plausible repair
- whether repair risks overfitting Stage 10 cases
- confidence

Do not prescribe broad rewrites where one bounded repair is sufficient.

Do not blame the model merely because an answer is wrong. Use `MODEL_BEHAVIOR / UNCERTAIN` only when evidence does not identify a more specific Agent/KB layer.

## Scoring discipline

Important:

- Score the output actually produced, not what the Agent could have produced.
- Do not reward hidden reasoning or metadata not visible in raw output, except routing/tool metadata may be used only for evaluation-integrity checks, not to fill missing answer content.
- Do not penalize stylistic differences not covered by rubric/oracle.
- Oracle `must_find` and `must_not_find` are evidence for scoring, not a word-matching checklist.
- Mechanism-equivalent wording is acceptable.
- Allowed alternate routes must be honored.
- Where an oracle marks ambiguity, do not force false certainty.
- GOOD CASE false positives are material.
- Unsupported blockers require all frozen HF-01 pillars.
- Do not change the hard-failure taxonomy.

## No repair in Phase D

Do not modify:

- Agent prompt
- mode files
- KB
- harness
- raw outputs
- PUBLIC cases
- oracle/rubric

Phase D is scoring + diagnosis only.

## Mechanical validation

Before return:

1. starting HEAD exactly `d6ac48c16f7285f53fbc7af6e5aae4f64f83123b`;
2. measured evidence files unchanged byte-for-byte;
3. only these new tracked files:
   - `eval/stage10/scoring/case-scores.yaml`
   - `reports/STAGE10_PHASE_D_SCORECARD.md`
   - `reports/STAGE10_PHASE_D_DEFECT_DIAGNOSIS.md`
4. exactly 32 case score entries;
5. every scored case maps to one raw output + one oracle entry;
6. all D1..D10 values valid;
7. N/A only where rubric permits;
8. all hard failures use HF-01..HF-12 only;
9. aggregate arithmetic internally reconciles;
10. no private oracle/rubric copied into new files beyond concise scoring rationale;
11. no web/external research;
12. no secret in diff;
13. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. scoring status
4. overall score earned/max/percentage
5. dimension scores
6. hard-failure count + cases + HF codes
7. route accuracy
8. terminal-outcome accuracy
9. GOOD CASE precision
10. ambiguity/NEEDS_EVIDENCE result
11. product-contract result
12. strongest 3 Agent capabilities
13. highest-impact 3 defect clusters
14. adjudication-required case IDs
15. changed-files list
16. mechanical validation
17. exact scoring uncertainty/limitation
