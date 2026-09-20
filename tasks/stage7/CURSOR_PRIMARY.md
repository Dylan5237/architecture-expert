# Stage 7 Task — Cursor Primary Knowledge Architect

## Role

You are the **Primary Knowledge Architect / Ontology Builder** for Stage 7 of `Dylan5237/architecture-expert`.

You replace the previous Kimi Web K3 Cluster primary role for this stage.

You are working locally through Cursor. Treat GitHub/repository state as authoritative; chat text is not project truth.

## Branch

Work only on:

`research/stage7-knowledge-architecture`

Before editing, verify that your branch HEAD matches the latest Stage 7 control baseline recorded in GitHub Issue #18.

If it does not match, stop and report the mismatch instead of rebasing or guessing.

## Read first

Read, in this order:

1. `AGENTS.md`
2. `TASK.md`
3. GitHub Issue #18, including the latest Chief Architect checkpoint
4. `01_CONSTITUTION.md`
5. `02_VOCABULARY.md`
6. `reports/STAGE6_REDUCTION.md`
7. `reports/STAGE6_REDUCTION_AUDIT.md`
8. `reports/STAGE6_RECONCILIATION.md`
9. `reports/STAGE5_FALSIFICATION.md`
10. `reports/STAGE5_ADVERSARIAL_AUDIT.md`
11. `reports/STAGE5_RECONCILIATION.md`
12. `review-queue.yaml`
13. `source-manifest.yaml`
14. relevant `sources/` only when a concrete traceability check requires them

Do not read the Stage 7 challenger branch.

## Mission

Operationalize the sealed Stage 6 Constitution into a **minimal, traceable, progressively disclosed, agent-consumable knowledge architecture**.

This stage is about information architecture and ontology implementation, not new architecture research.

The sealed Constitution is authoritative:

- AX-001..AX-004 are canonical Evaluation Axioms.
- MP-001..MP-010 are canonical promoted Mother Principles.
- AX-005 is a usage rule only; its ID is reserved.
- MP-011 is RETIRED / NOT PROMOTED; its ID is permanently reserved.
- P-006 remains a non-principle review signal/property lineage.
- Historical P-* files are immutable historical artifacts.

Do not change any accepted AX/MP causal semantics.

## Required outputs

Create/update only the Stage 7 knowledge-architecture artifacts required by Issue #18.

### Router

Create:

`00_ROUTER.md`

Keep it short. It should support this progressive-disclosure path:

`00_ROUTER -> 01_CONSTITUTION -> relevant domain index -> linked MP/FP/T -> sources/RQ only when needed`

The Router is navigation, not a reasoning playbook or system prompt.

### Canonical MP pages

Create:

`principles/MP-001.md` through `principles/MP-010.md`

Update:

`principles/index.md`

The index must clearly distinguish:

- canonical MP-001..MP-010;
- historical Stage 4 P-* candidates;
- MP-011 retired/reserved;
- P-006 non-principle review-signal/property lineage.

Do not modify historical P-* files.

Each MP page must remain semantically faithful to `01_CONSTITUTION.md`.

Use compact metadata and avoid copying long Stage 5/6 reports.

### Domains

Create:

`domains/index.md`

Create only domain indexes that materially improve retrieval.

Candidate families from Issue #18 are hypotheses, not mandatory folders:

- boundaries
- lifecycle
- runtime
- concurrency
- resources
- performance
- reliability
- distributed
- state-data
- integration
- security
- observability
- scalability
- evolution

Do not create empty domains for completeness.

Each domain index should be compact and route to relevant MP/FP/T/RQ knowledge.

### Failure Patterns

Create:

`failure-patterns/index.md`

and atomic:

`failure-patterns/FP-*.md`

Create an FP only when the sealed corpus supports a reusable causal failure family.

An FP is not:

- a protected property;
- a tactic;
- a metric;
- a checklist item;
- a named architecture pattern;
- a vague risk.

Each FP must have a concrete failure signature, mechanism, trigger/amplification path, false-positive/GOOD CASE boundary, MP links, tactic links, and evidence/gaps.

Do not add Stage 8 questions/checklists.

### Tactics

Create:

`tactics/index.md`

and atomic:

`tactics/T-*.md`

A Tactic is a reusable intervention/mechanism, not a principle.

Only instantiate tactics materially supported by the sealed corpus.

Keep these distinctions exact:

- admission control != backpressure != rejection/load shedding != degradation;
- retry != idempotency;
- failure isolation != generic process split;
- compatibility tactic != universal compatibility principle;
- flow control != backpressure.

Do not create one file per buzzword.

### GOOD CASE registry

Create:

`cases/good-cases/index.md`

Assign stable IDs:

`GC-001...`

Only register GOOD CASE / non-violation boundaries already accepted in Stage 5/6.

Each GC entry should include:

- title;
- context/shape;
- likely naive false-positive;
- why compliant;
- MP/FP/T refs;
- source refs when applicable;
- Stage 5/6 provenance.

Do not create full eval scenarios.

### Relationship map

Create:

`relationship-map.yaml`

Keep it machine-readable and compact.

Use a small relation vocabulary only when semantically justified.

Candidate predicates:

- DERIVED_FROM
- EXPLAINS
- MITIGATED_BY
- RELATED_TO
- DISTINCT_FROM
- EVIDENCED_BY
- HAS_GOOD_CASE
- HAS_GAP
- OPERATIONALIZED_BY only if a review-signal type is explicitly proposed

Every edge is a claim.

Requirements:

- all node IDs resolve;
- all file paths resolve;
- no dangling references;
- no evidence inheritance between siblings;
- MP-004 RELATED_TO MP-005 may be represented only as a non-parent relationship;
- D-01/02/04/05/06/07/09 distinctions remain navigable.

### Review-signal/property decision

Explicitly evaluate whether a separate reusable type such as:

`review-signals/RS-*`

is necessary for:

- P-006 Change Locality / change amplification;
- RQ5-001 blast-radius measurement.

Do not silently add the ontology.

If you propose it:

- keep it minimal;
- explain why MP/FP/T/domain metadata cannot represent it cleanly;
- instantiate only evidence-forced examples;
- mark it as requiring Chief Architect approval.

If you do not propose it, show exactly where these signals live without category confusion.

### Stage 7 synthesis

Create:

`reports/STAGE7_KNOWLEDGE_ARCHITECTURE.md`

It must contain:

1. ontology inventory and stable ID namespaces;
2. domain taxonomy and rationale;
3. MP operationalization map;
4. FP inventory and category justification;
5. T inventory and category justification;
6. GOOD CASE registry map;
7. relationship predicate definitions;
8. relationship coverage matrix;
9. orphan/dangling-reference audit;
10. source/RQ traceability audit;
11. D-01..D-14 preservation;
12. lexical-gate preservation;
13. progressive-disclosure path and expected load order;
14. duplication/context-efficiency review;
15. review-signal/property ontology decision;
16. deliberate omissions / Stage 8 boundary;
17. genuine owner decisions only.

Include navigation demonstrations for at least:

- overload / retry storm;
- stale async result / ownership;
- contract migration;
- trust boundary / agent action;
- observability vs formal guarantee.

These are retrieval-path demonstrations, not reasoning playbooks.

## Ontology discipline

Keep Principle / Failure Pattern / Tactic / GOOD CASE / Domain distinct.

Do not create new durable node types unless the existing types cannot represent an accepted knowledge need without category confusion.

Do not optimize for file count.

Do not create a node solely because a term appears in a source.

Do not copy source prose into domain files.

Do not introduce new claims just to make the graph look complete.

## Evidence discipline

No broad web research.

Use only the sealed repository corpus.

If a proposed FP/T/relation needs evidence the repository does not contain:

- narrow it;
- mark a gap;
- or omit it.

Do not silently invent support.

## Stable-ID discipline

Never reuse:

- AX-005
- MP-011

Do not reactivate:

- P-006 as a principle
- H7 locality as a principle
- P-005 or P-011 as principles

New FP/T/GC IDs must be stable once committed.

Do not renumber merely for aesthetics.

## Stage 8 boundary

Do not create:

- decision playbooks;
- question bank;
- reasoning workflow;
- Agent modes;
- system prompt;
- eval scenarios/results;
- final Agent runtime logic.

No Stage 8 content should be hidden inside domain/FP/T files.

## Mechanical validation before completion

Before you report completion, verify:

1. only intended Stage 7 files changed;
2. no sealed Stage 2/3/4/5/6 file was modified except `principles/index.md`, which is explicitly authorized;
3. all MP-001..010 pages exist;
4. all relationship-map node paths exist;
5. all edge endpoints resolve;
6. every FP/T/GC ID is unique;
7. no retired/reserved ID is reused;
8. no orphan durable node exists without an explicit reason;
9. no reference points to a missing file/ID;
10. D-01..D-14 remain traceable;
11. GOOD CASES remain navigable;
12. no Stage 8 artifact exists.

Commit and push all Stage 7 Primary artifacts to the assigned branch, then stop.

## Return format

Return only:

1. branch
2. SHA
3. entity/file inventory
4. domain taxonomy
5. FP count + IDs
6. T count + IDs
7. GC count + IDs
8. relationship predicates + edge count
9. review-signal/property proposal
10. dangling/orphan validation result
11. genuine owner decisions
