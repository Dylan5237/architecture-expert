# Stage 7 Task — Codex + GLM Independent Knowledge-Architecture Challenger

## Role

You are the **Independent Knowledge-Architecture Challenger** for Stage 7 of `Dylan5237/architecture-expert`.

Division of responsibility:

- GLM 5.3: semantic/category/retrieval/ontology challenge.
- Codex harness: deterministic Git/repository validation, ID/path/ref checks, persistence and fail-closed delivery.

This is **Blind Pass A**.

## Branch

Work only on:

`challenge/stage7-knowledge-architecture`

Before editing, verify branch HEAD matches the latest Stage 7 control baseline recorded in GitHub Issue #18.

If it does not match, stop and report the mismatch.

## Blindness rule

Do NOT read:

- `research/stage7-knowledge-architecture`
- any Stage 7 Primary artifact created by Cursor
- any unmerged Primary Stage 7 commit/PR

You may read sealed main/canonical artifacts and GitHub Issue #18.

## Read first

1. `AGENTS.md`
2. `TASK.md`
3. GitHub Issue #18, including latest Chief Architect checkpoint
4. `01_CONSTITUTION.md`
5. `02_VOCABULARY.md`
6. `reports/STAGE6_REDUCTION.md`
7. `reports/STAGE6_REDUCTION_AUDIT.md`
8. `reports/STAGE6_RECONCILIATION.md`
9. Stage 5 final falsification/reconciliation artifacts
10. `source-manifest.yaml`
11. `review-queue.yaml`

No source collection is allowed.

## Mission

Independently challenge the **knowledge architecture that Stage 7 should permit**, without building a competing canonical ontology.

Your job is to identify the smallest sufficient structure and preregister checks that will later be run against the Primary implementation.

Create only:

`reports/STAGE7_ONTOLOGY_AUDIT.md`

Do not create Router/domain/MP/FP/T/GC/relationship-map artifacts.

## Required analysis

### 1. Minimal entity types

Determine the minimal durable entity types Stage 7 needs.

Start from:

- canonical MP;
- Failure Pattern;
- Tactic;
- Domain index;
- GOOD CASE registry;
- relationship graph;
- source/RQ evidence references.

Explicitly challenge whether any additional review-signal/property type is necessary.

### 2. Category traps

Identify likely category errors from the sealed corpus, especially:

- principle disguised as tactic;
- tactic disguised as principle;
- property/metric disguised as FP;
- protected property disguised as FP;
- pattern name disguised as tactic;
- GOOD CASE generalized into a rule;
- evidence/source artifact promoted into an ontology node without retrieval value.

### 3. Relation vocabulary

Recommend the smallest relation vocabulary that preserves required semantics.

For each predicate, define:

- direction;
- meaning;
- whether transitive;
- whether it implies causality;
- whether it permits evidence inheritance.

Attack likely bad edges:

- sibling evidence inheritance;
- parent/child overreach;
- RELATED_TO interpreted as support;
- DISTINCT_FROM used without context;
- causal implication hidden in navigation edges.

MP-004 / MP-005 may be RELATED_TO only; no parent semantics.

### 4. Domain taxonomy risks

Analyze:

- duplicate content across domains;
- one question mapping to too many domains and causing wide loading;
- cloud/backend bias;
- domains that classify sources rather than route retrieval;
- empty domain bureaucracy;
- domain names that collide with V-* vocabulary.

### 5. GOOD CASE registry requirements

Define what must be stable so GOOD CASES can later become false-positive eval fixtures.

Check that Stage 5/6 boundaries are not flattened into generic examples.

### 6. D-01..D-14 preservation

Specify how Stage 7 must keep each discriminator navigable.

At minimum protect:

- D-01 P-001/P-002
- D-02 P-001/P-013
- D-04 P-003/P-012
- D-05 P-004/P-009
- D-06 P-010/P-001
- D-07 P-001/P-003
- D-09 P-013/P-010
- D-11 P-007 proof-scope
- D-12 P-012 gap
- D-14 CRDT multi-writer GOOD CASE

### 7. Progressive disclosure

Define pass/fail criteria for this path:

`00_ROUTER -> 01_CONSTITUTION -> relevant domain index -> linked MP/FP/T -> source/RQ only when needed`

Attack designs where an ordinary focused question requires loading:

- all domains;
- all MPs;
- all FP/T files;
- all sources;
- Stage 5/6 reports by default.

Router must remain navigation, not reasoning.

### 8. Stable IDs / retirement

Explicitly protect:

- AX-005 reserved, not an AX;
- MP-011 retired/not promoted, ID never reused;
- P-006 not promoted;
- H7 not resurrected.

Define ID collision/renumbering failure criteria.

### 9. Review-signal/property layer

Give a verdict:

- NOT_NEEDED
- PROPOSE_MINIMAL_RS_LAYER
- NEEDS_PRIMARY_EVIDENCE

Use P-006 change amplification and RQ5-001 blast-radius measurement as the test cases.

Do not invent a metrics ontology merely for symmetry.

### 10. FP/T stop criteria

Define what should prevent ontology/file-count growth.

Examples:

- no FP without a reusable causal failure mechanism;
- no tactic without a reusable intervention mechanism;
- no node created solely because a named pattern exists;
- no duplicate tactic split by vendor/tool;
- no node where metadata/reference is sufficient.

### 11. Stage 8 boundary

Specify what would constitute Stage 8 smuggling:

- decision playbook;
- question bank;
- explicit reasoning sequence;
- review checklist;
- Agent mode;
- tool-routing runtime logic;
- eval scenario/result.

## V7 preregistration

Create a detailed `V7-01..` checklist for Pass B.

It must cover at least:

- 10 MP semantic fidelity;
- canonical vs historical principles;
- FP category purity;
- Tactic category purity;
- GOOD CASE traceability;
- D-test preservation;
- relationship semantics;
- no hidden evidence inheritance;
- all refs resolve;
- no orphan durable nodes;
- stable IDs;
- retired IDs;
- lexical gate;
- source/RQ traceability;
- progressive disclosure;
- router size/role;
- domain duplication;
- context efficiency;
- no unsupported claims;
- no Stage 8 smuggling;
- review-signal ontology necessity;
- no arbitrary node count;
- no empty-domain bureaucracy;
- no source-prose duplication;
- no sibling evidence borrowing.

## Output contract

Create:

`reports/STAGE7_ONTOLOGY_AUDIT.md`

It must include:

1. minimal ontology recommendation;
2. highest-risk category traps;
3. relationship predicate recommendation;
4. domain/retrieval risks;
5. GOOD CASE requirements;
6. D-01..D-14 preservation risks;
7. source/RQ traceability requirements;
8. progressive-disclosure/context-efficiency requirements;
9. stable-ID/retirement rules;
10. review-signal/property verdict;
11. FP/T stop criteria;
12. Stage 8 boundary;
13. V7 preregistered checks;
14. genuine owner decisions only.

## Fail-closed delivery

Before returning:

1. branch descends from the assigned Stage 7 baseline;
2. diff contains only the challenger Stage 7 audit artifact;
3. report is non-empty;
4. remote HEAD equals reported SHA;
5. remote read-back contains:
   - MP-001..MP-010;
   - GOOD CASE concern;
   - relation/predicate analysis;
   - V7 checks;
6. no sealed Stage 2/3/4/5/6 artifact is modified or deleted.

If any check fails, stop and report FAIL CLOSED.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. minimal ontology recommendation
4. highest-risk category traps
5. relationship predicate recommendation
6. domain/retrieval risks
7. review-signal/property verdict
8. V7 preregistered checks
9. genuine owner decisions
