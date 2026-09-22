# Stage 10 Phase A — Codex + GLM Independent Eval Designer / Oracle Author

## Role

You are the **Independent Eval Designer / Oracle Author** for Stage 10 of `Dylan5237/architecture-expert`.

This is evaluation design only.

Do not run the Agent.
Do not score any Agent output.
Do not modify the frozen SUT.
Do not create Stage 11 repairs.

## Frozen SUT

`SUT_SHA = 96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Read all Agent/knowledge/reasoning artifacts from this exact SHA.

Do not use a moving `main` as the evaluated system.

## Branch / worktree

Work only in a dedicated worktree on:

`eval/stage10-suite-design`

Fail closed unless:
- branch is correct;
- HEAD equals the frozen SUT SHA at start;
- worktree is dedicated;
- shared/primary checkout is not your execution workspace.

Do not repair/switch/reset/stash another Agent's checkout.

Read this task from `origin/main:tasks/stage10/CODEX_EVAL_DESIGNER.md` without merging main into the design branch.

## Read first

At frozen SUT SHA:

1. `AGENTS.md`
2. `planning/STAGE1_RESEARCH_PLAN.md`
3. `00_ROUTER.md`
4. `01_CONSTITUTION.md`
5. `02_VOCABULARY.md`
6. Stage 7 domains / MP / FP / T / GC / relationship map
7. Stage 8 decision playbooks + question bank
8. Stage 9 Agent v0.1 prompt + modes + README
9. Stage 9 audit/reconciliation reports

Also read GitHub Issue #27 latest checkpoint.

Do not read any future Stage 10 runner output. None should exist yet.

## Mission

Design a **blinded adversarial evaluation suite** that can diagnose:
- recall;
- precision;
- false positives;
- mechanism reasoning;
- evidence discipline;
- overengineering;
- product-contract preservation;
- uncertainty handling;
- routing;
- stop/escalation;
- progressive-disclosure behavior.

The suite must contain both defects and legitimate GOOD CASE/non-defects.

Do not write exam questions that reveal the ontology.

## Required artifacts

Create only under:

`eval/stage10/design/`

plus one report:

`reports/STAGE10_EVAL_SUITE_DESIGN.md`

Required structure:

```
eval/stage10/design/
├── manifest.yaml
├── rubric.md
├── public/
│   ├── E10-001.md
│   ├── ...
│   └── E10-0NN.md
└── private/
    ├── oracle.yaml
    └── coverage.yaml
```

You may choose a per-case oracle-file layout instead of one oracle.yaml only if it materially improves maintainability; record the exact structure in the manifest.

Do not create run outputs.

## Suite size

At least **30 valid cases**.

Prefer 30–36 high-quality cases rather than padding with near-duplicates.

## Required coverage

### Modes / task objects

Cover:
- AUTO;
- ARCH_DESIGN / DP-001;
- ARCH_REVIEW / DP-002;
- CHANGE_REVIEW / DP-003;
- ADR_REVIEW / DP-004;
- INCIDENT_ANALYSIS / DP-005.

At least 5 cases must challenge AUTO routing or object-vs-vocabulary ambiguity.

### Failure/mechanism families

Collectively cover:

- desktop/UI foreground or main-thread blocking;
- execution-model guarantee mismatch;
- unbounded queue/backlog;
- retry amplification;
- orphan/background work ownership;
- stale async completion;
- large scan/resource bound;
- pool exhaustion/shared bottleneck;
- global lock/head-of-line blocking;
- herd/stampede;
- stale/cache/state authority;
- independent-consumer migration break;
- partial failure/failure propagation;
- duplicate delivery/idempotency;
- ordering ambiguity;
- resource leak;
- noisy neighbor/isolation;
- timeout/deadline mismatch;
- unbounded fan-out;
- hidden SPOF;
- overload-control distinctions;
- trust/least privilege;
- observability/distinguishing evidence;
- evolution/change-boundary;
- product-contract vs implementation constraint.

Use cross-domain cases where realistic rather than one ontology item per case.

### GOOD CASE / false-positive set

At least **8 cases** must be materially non-alarmist.

Examples:
- valid NO_DEFECT;
- only NON_BLOCKING_IMPROVEMENT;
- NEEDS_EVIDENCE rather than blocker;
- governed compatibility break;
- supervised daemon;
- long-lived but per-work bounded;
- SQLite/single-process economic choice;
- exploration without identifiable variation axis;
- CRDT/local-first explicit merge;
- proof-scoped evidence;
- path-level overload control;
- coarse internal trust with no relevant boundary.

For each such oracle entry, explicitly record the naive false positive that must NOT appear.

### Evidence ambiguity

At least 5 cases must intentionally omit or conflict on decisive evidence.

Possible correct terminals:
- NEEDS_EVIDENCE;
- KNOWLEDGE_DRIFT;
- OWNER_TRADE_OFF;
- ARCH_CONFLICT.

### Shape diversity

Cover multiple shapes:
- backend/distributed;
- desktop/local developer tool;
- embedded/edge/constrained runtime;
- local-first;
- single-process/SQLite;
- formal/proof-scoped;
- agent/tool trust;
- batch/data workflow if useful.

No cloud/backend dominance.

### Cross-domain

At least 6 cases must force a genuine discriminator or dual-domain route.

Include representative distinctions such as:
- D-02 ownership vs execution guarantee;
- D-04 per-work bound vs overload policy;
- D-05 failure containment vs trust;
- D-07 cancellation vs execution bound;
- contract vs evolution boundary;
- observability vs formal guarantee.

## Public case rules

Public case files are the **only** Stage 10 material later exposed to the evaluated Agent.

They must contain plausible project/user material only.

Use:

```yaml
id:
title:
task_object:
requested_mode:
user_request:
project_evidence:
  product_intent:
  architecture_intent:
  code:
  config:
  test:
  runtime:
  history:
  user_assertion:
constraints:
notes_for_runner:
```

Omit unavailable evidence fields.

Do NOT include:
- expected mode/DP;
- expected overlays;
- expected finding/non-finding;
- GC IDs;
- failure-pattern names if a real user would not know them;
- score rubric hints;
- hard-failure labels;
- “this case tests X” wording.

Avoid ontology-keyword leakage.

## Private oracle rules

For every case record:

- expected mode + DP;
- allowed alternate routing;
- expected overlays;
- required property/properties;
- evidence authority expectations;
- candidate mechanism(s);
- relevant MP/FP/T/GC/RQ/D references for scorer only;
- must-find;
- must-not-find;
- acceptable alternate analyses;
- expected terminal outcome(s);
- minimum-correction expectations;
- uncertainty / next-evidence expectations;
- product-contract / authority expectations;
- hard-failure triggers;
- ambiguity notes;
- scoring notes.

Do not require exact prose.

If two conclusions are legitimately acceptable, encode both.

If a case is too ambiguous for a stable oracle, FIX OR REMOVE THE CASE now. Do not defer ambiguity to scoring.

## Rubric

Use 10 diagnostic dimensions:

1. routing correctness
2. required-property understanding
3. evidence/project-fact discipline
4. mechanism accuracy
5. GOOD CASE / false-positive precision
6. minimum correction / anti-overengineering
7. product-contract / authority handling
8. uncertainty / discriminating evidence
9. finding + terminal correctness
10. scope / progressive-disclosure discipline

Use a small ordinal scale such as 0/1/2 per applicable dimension.

Define each score anchor concretely.

N/A is allowed only when genuinely inapplicable.

Verbosity is not quality.

## Hard failures

Define and freeze hard-failure IDs before any run.

Must include at least:

- unsupported blocker;
- material GOOD CASE false positive;
- invented project fact/evidence;
- GENERIC_KNOWLEDGE overriding accepted project fact;
- silent product-contract weakening;
- materially wrong route with procedure/result impact;
- failure to stop at NEEDS_EVIDENCE when decisive evidence is absent;
- framework/pattern prescription as authority;
- ARCH_CONFLICT for mere inconvenience;
- false certainty from ambiguous semantics;
- oracle/eval leakage;
- hidden-CoT request/exposure attributable to Agent behavior.

You may add hard-failure categories now.

Once Agent runs begin, do not weaken/remove categories to improve scores.

## Coverage manifest

`coverage.yaml` must make suite coverage mechanically auditable.

For each case include tags for:
- task/mode;
- AUTO;
- shape;
- domains;
- failure/GOOD CASE;
- ambiguity;
- cross-domain;
- product-contract;
- trust;
- expected terminal family.

Include summary counts.

## Leakage review

Before completion, run a dedicated leakage pass:

For every public case:
- remove ontology IDs and framework hints not realistic for a user;
- remove wording that gives away expected mechanism;
- ensure titles do not reveal the answer;
- ensure private oracle content does not appear in public files;
- ensure public case metadata cannot trivially reveal good/bad classification.

Record results in the design report.

## Suite-design report

Create:

`reports/STAGE10_EVAL_SUITE_DESIGN.md`

Include:

1. suite inventory;
2. case count;
3. task/mode distribution;
4. shape distribution;
5. GOOD CASE count;
6. ambiguity count;
7. cross-domain count;
8. failure-family coverage;
9. rubric;
10. hard-failure registry;
11. leakage audit;
12. oracle ambiguity review;
13. expected evaluation limitations;
14. files safe for runner exposure;
15. files PRIVATE / forbidden to runner;
16. suite-freeze recommendation;
17. genuine owner decisions only.

Do not include future Agent output.

## Mechanical validation

Before return verify:

1. branch descends from SUT SHA;
2. diff contains only authorized design files + suite-design report;
3. >=30 public case IDs, unique and sequential/stable;
4. every public case has a matching oracle entry;
5. no oracle entry without a public case;
6. coverage summary reconciles to actual cases;
7. >=8 GOOD CASE/non-alarmist cases;
8. >=5 ambiguity/conflicting-evidence cases;
9. >=5 AUTO routing challenge cases;
10. >=6 cross-domain cases;
11. all five explicit DPs represented;
12. shape diversity requirements represented;
13. no public case contains private score/must-find/must-not-find/hard-failure fields;
14. no Stage 2–9 artifact modified;
15. no run output exists;
16. remote HEAD equals reported SHA.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. public case count
4. mode/task distribution
5. shape distribution
6. GOOD CASE / ambiguity / AUTO / cross-domain counts
7. mechanism coverage summary
8. rubric summary
9. hard-failure IDs
10. leakage audit result
11. oracle ambiguity result
12. runner-safe file set
13. private forbidden file set
14. mechanical validation
15. suite-freeze recommendation
16. genuine owner decisions
