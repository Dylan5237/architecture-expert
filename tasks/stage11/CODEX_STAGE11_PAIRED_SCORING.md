# Stage 11D — Independent Paired Holdout Scoring

## Mandate

Stage 11C is technically COMPLETE. Both candidate runs are canonical and fixed. This task **unseals the frozen holdout oracle only for independent scoring**. Do not rerun models, tune prompts, or modify evidence.

Repository: `Dylan5237/architecture-expert`.

- Scoring branch: `eval/stage11-paired-scoring`.
- Starting HEAD: `113ac1a4a6ffafeb4af0724c5a7efa2c14ffb21a`.
- Task source: `origin/main:tasks/stage11/CODEX_STAGE11_PAIRED_SCORING.md`.
- Holdout design SHA: `69cab5ab750c350ce719a0d37e7680bbc96bdf21`.
- Original rubric SHA: `ff157eb1947860345a305fb29452b51e09dd3a2b`.
- v0.1 SUT: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`.
- v0.2 SUT: `c12b67c7410878960c45a9934ded6ae52ae6c42f`.
- Adapter freeze SHA: `c3fe4596961cf3abf30296aac169ef73c71034cd`.
- Paired canonical evidence SHA: `113ac1a4a6ffafeb4af0724c5a7efa2c14ffb21a`.
- Provider/model: the same frozen company-gateway `glm-5.3` for both.

Use a dedicated worktree. Prefer a **fresh independent scorer session** without the holdout designer's or repair executor's conversational context. It is **now authorized** to read the private oracle/coverage/manifest **after verifying both fixed runs**; neither runner nor repair agent gets this access retroactively.

## Gate 0 — Integrity before unsealing

First inspect only:
- `eval/stage11/holdout/run/PAIR_STATUS.json`;
- `eval/stage11/holdout/run/v0.1/metadata.json` and `RUN_STATUS.md`;
- `eval/stage11/holdout/run/v0.2/metadata.json` and `RUN_STATUS.md`;
- the recorded SHA identities, complete raw inventories, and the tracked evidence commit.

Require:
- both `COMPLETE`, each exactly 12 nonempty outputs `H11-001..012`;
- canonical evidence frozen in the specified SHA, with exactly 29 run files;
- byte-identical PUBLIC input SHA256 for each case across versions;
- expected candidate and active-system-prompt identity;
- same provider/model/settings/harness apart from the candidate SUT;
- all observed model identities accepted; no integrity HOLD.

If any fails, stop `BLOCKED_INTEGRITY`, without unsealing or scoring.

## Scorer-only source material (unseal after Gate 0)

Read directly from **the frozen design commit**, not a mutable branch tip:

- `eval/stage11/holdout/design/private/oracle.yaml`;
- `eval/stage11/holdout/design/private/coverage.yaml`;
- `eval/stage11/holdout/design/manifest.yaml`;
- `eval/stage11/holdout/design/public/H11-001.md .. H11-012.md` (the exact input cases).

Read the frozen Stage 10 rubric at:

`ff157eb1947860345a305fb29452b51e09dd3a2b:eval/stage10/design/rubric.md`.

The oracle, coverage, rubric, categories and pass criteria **cannot be edited after seeing outputs**. Do not merge the holdout-design branch or place private files in model-visible snapshots.

## Score each version independently

For each of the 12 cases, score **v0.1 and v0.2 separately** against the SAME frozen oracle and D1..D10 0/1/2 anchors. `N/A` only where genuinely permitted by the rubric. Assign D5/D7/D8 applicability based on the **case evidence and oracle**, not which version gave a better answer; if two versions differ in N/A, explicitly justify or flag for adjudication.

For each case/version record:
- observed primary mode/DP and oracle route; `EXACT` / `ALLOWED_ALTERNATE` / `FAIL`;
- explicit overlay quality in D1, separate from primary-route acceptance;
- D1..D10 scores and brief factual rationales with raw line pointers;
- any hard failure (HF-01..HF-12) with exact raw pointer/quote, frozen trigger, and affected dimensions;
- observed and expected **global** `terminal_outcome`, with route-conditioned alternatives honored (especially H11-011);
- whether the designated strict GOOD CASE component was materially falsely flagged;
- material product-contract weakening;
- evidence uncertainty handling;
- genuine scoring ambiguities / adjudication flags.

HF caps only affected dimensions at 0; it does not automatically zero the case. Do not score hidden reasoning or tool metadata as answer substance. Do not count exact word matching where mechanism-equivalent language meets the oracle. Do not label disagreement over writing style an HF.

Keep each version's per-case scoring stable before comparing aggregate outcomes. Do not have one version's polished wording inflate its score merely through verbosity.

## Apply the **pre-registered** seven pass criteria mechanically

Use `manifest.yaml` as the definitive frozen contract, not a memory-based paraphrase:

1. v0.2 D3 improves at least **20 percentage points** over v0.1 (D3 maximum = 24 points per version). Apply only the manifest's exact 0-HF03/high-D3 baseline exception.
2. HF-03 decreases at least **50%** as distinct case/code registrations; if v0.1 has zero, v0.2 must also have zero.
3. v0.2 adds NO new `HF-02/05/06/07/09` **case/code pairs** relative to v0.1.
4. Accepted primary-route count for v0.2 does not decrease.
5. Material false positives on strict designated GOOD CASE components H11-009, 010, 011 do not increase.
6. Overall earned/applicable-max percentage for v0.2 does not decrease.
7. No private-eval/holdout leakage (HF-11) in v0.2.

Compare exact fractional values without relying on rounded display percentages. Do not invent ceiling exceptions; if a frozen criterion is impossible to achieve due to the baseline, record it as a pre-registration limitation, **not a permission to alter the threshold**.

If all seven PASS: `STAGE11_HOLDOUT_GATE: PROVISIONAL_PASS`.
If any FAIL: `STAGE11_HOLDOUT_GATE: FAIL`.
If integrity invalid: `STAGE11_HOLDOUT_GATE: INVALID`.

A provisional pass is **not yet Agent v0.2 release approval**; Chief Architect will adjudicate only disputed HFs, material GOOD CASE mistakes, threshold-changing disagreements and a few stratified spot checks.

## Outputs — ONLY three new files

1. `eval/stage11/holdout/scoring/paired-case-scores.yaml`
   - exactly 24 case/version entries (or 12 paired entries containing both);
   - per-dimension rationale, terminal, route, hard failures, pointers, and adjudication markers.
2. `reports/STAGE11_PAIRED_SCORECARD.md`
   - v0.1/v0.2 D1..D10 earned/applicable-max/% table;
   - overall scores; per-case deltas; 7 gate checks PASS/FAIL with exact arithmetic and affected cases;
   - HF counts/case-code pairs per candidate, terminal accuracy, primary routing, strict GOOD CASE outcomes;
   - clear provenance and run scope.
3. `reports/STAGE11_PAIRED_DEFECT_DELTA.md`
   - improvements/regressions in evidence discipline, terminal choice, correction guarantees;
   - remaining generalizable weaknesses and smallest possible next repair if justified;
   - do not prescribe any new v0.3 work or new benchmark without a measured failure.

All other files, including both versions' 29 canonical run evidence files, Agent prompts, KB, Harness, oracle, manifest and rubric stay byte-for-byte unchanged.

## Mechanical validation and handoff

Require:
- starting HEAD exact;
- both runs revalidated against evidence SHA; no H11 calls/reruns;
- exactly 24 scored records, 12 common IDs;
- legitimate D1..D10/N/A and HF-01..12 rules;
- all arithmetic reconciles, including seven criteria and subgroups;
- no results incorporated from Stage 10 as the v0.1 holdout baseline;
- only the three authorized new files changed;
- no private oracle/rubric content pasted wholesale;
- no secrets or hidden reasoning;
- ordinary commit/push with matching remote SHA.

Return only:

1. branch and scoring SHA;
2. scoring and gate statuses;
3. v0.1 overall and v0.2 overall + delta;
4. D3 scores/percentages/delta;
5. HF-03 case counts and relative reduction;
6. all protected HF case/code comparison;
7. primary-route count comparison;
8. strict GOOD CASE false-positive comparison;
9. all seven gate criterion results;
10. terminal-outcome comparison;
11. highest-impact improvements and regressions;
12. specific adjudication-required cases;
13. changed files, mechanical validation and limits.

No model execution, Agent repair or Stage 11 PASS declaration in this task.
