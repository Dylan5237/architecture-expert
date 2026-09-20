# Stage 7 Task — Codex + GLM Pass B Reconciliation

## Role

Continue as the **Independent Knowledge-Architecture Challenger** for Stage 7 of `Dylan5237/architecture-expert`.

This is **Pass B — Reconciliation**. Blindness is now intentionally lifted.

Division:
- GLM 5.3: semantic/category/ontology/retrieval reconciliation.
- Codex harness: deterministic Git/ref/path/ID validation, diff integrity, persistence and fail-closed delivery.

## Fixed inputs

Primary:
`research/stage7-knowledge-architecture@62614d4eaec91233d973666e4398368a39d3597c`

Blind Pass A:
`challenge/stage7-knowledge-architecture@49e8031f8f83c5fdfd57bfe576dd12613c86e5ed`

Control:
GitHub Issue #18 latest Chief Architect checkpoint.

Work on:
`challenge/stage7-knowledge-architecture`

Create only:

`reports/STAGE7_RECONCILIATION.md`

Do not edit the Primary branch or any sealed artifact.

## Chief Architect fixed decisions

### OD7-1 — Minimal ontology model

Approve the Pass A minimality direction with this clarification:

**Durable runtime knowledge types** are:
- MP
- FP
- Tactic
- GOOD CASE
- Domain index

The following are **not runtime knowledge types**:
- Router: navigation infrastructure
- relationship edge: graph claim
- S-* / RQ*: evidence/gap references
- historical P-* / AX-* / retired tombstones: lineage/governance references

`relationship-map.yaml` MAY materialize AX/P/S/RQ/retired IDs as lightweight **reference nodes** solely to make lineage/evidence/gap edges machine-checkable. That does not promote them into runtime knowledge types or default load targets.

Pass B must verify the Primary report/map makes this distinction explicit enough. If not, require a bounded wording/schema fix rather than deleting useful reference endpoints.

MP-011 may exist only as a `retired-reserved` reference node with no causal semantics and no ID reuse.

### OD7-2 — Relation vocabulary

Approve exactly these eight Stage 7 predicates:

- DERIVED_FROM
- EXPLAINS
- MITIGATED_BY
- RELATED_TO
- DISTINCT_FROM
- EVIDENCED_BY
- HAS_GOOD_CASE
- HAS_GAP

`OPERATIONALIZED_BY` remains deferred.

Every predicate must explicitly document:
- allowed direction;
- symmetry, if any;
- transitivity;
- whether causal;
- whether evidence inheritance is allowed.

Evidence inheritance is never allowed.

`RELATED_TO` is intentionally weak and must not become a garbage association edge.

Pre-authorized:
- MP-004 RELATED_TO MP-005, navigation only, no parent/evidence semantics.

Other RELATED_TO edges may survive only when they add concrete retrieval value and carry a precise note. Domain-home membership does not automatically justify a RELATED_TO edge because the domain index already routes to its nodes.

### OD7-3 — Domain count / consolidation

No numeric target.

Do NOT force the Challenger's speculative “5–8 domains”.

The Primary's ten domains may be accepted if:
- each materially routes at least two durable runtime nodes/references;
- indexes remain compact routing views rather than prose duplication;
- the five required retrieval demonstrations stay within the progressive-disclosure budget;
- no empty or source-taxonomy domains exist.

Keep `resources` and `overload` separate for Stage 7 because D-04 requires independently diagnosable peers.

### OD7-4 — Review-signal/property layer

`RS-* = NOT_NEEDED` for Stage 7.

P-006 remains MP-002-associated review-signal/property lineage.
RQ5-001 remains an MP-004 gap.

Reopen only if a later stage requires stable executable review-signal fixtures or multiple evidence-forced signals that cannot be represented without category confusion.

### OD7-5 — GOOD CASE atomization

Approve `GC-001..GC-016`.

Sixteen entries are the accepted granular representation of Stage 5/6 non-violation boundaries.

### OD7-6 — Router budget

Router must be navigation-only and <=150 lines.

The Primary's 47-line Router passes the size constraint; semantic role still needs V7 review.

## Chief Architect findings against the fixed Primary

### CA7-1 — Relationship predicate documentation is incomplete

Primary `relationship-map.yaml` currently gives one-line meanings, but does not explicitly encode/document for every predicate:
- direction;
- symmetry;
- transitivity;
- causality;
- evidence inheritance.

This is expected to be at least PARTIAL under V7-16.

Pass B must propose the smallest compliant schema/header fix.

### CA7-2 — Knowledge ontology vs graph reference nodes is conflated

Primary reports “109 nodes” and the map contains:
- AX references;
- canonical MP;
- retired MP-011 tombstone;
- historical P-*;
- P-006 lineage;
- FP/T/GC;
- RQ gaps;
- domains;
- S-* references.

This is mechanically coherent but semantically mixes runtime knowledge nodes with graph reference endpoints.

Pass B must classify each node type as:
- RUNTIME_KNOWLEDGE
- NAVIGATION_VIEW
- REFERENCE_ONLY
- RETIRED_TOMBSTONE

and verify that progressive disclosure never treats REFERENCE_ONLY/TOMBSTONE nodes as default load targets.

Do not demand deletion solely because a reference is represented in the graph.

### CA7-3 — RELATED_TO needs pruning/reconciliation

Primary has 16 RELATED_TO edges.

Audit every one.

Especially inspect:
- 10 domain -> MP “retrieval home” edges: likely redundant because domain indexes already perform routing;
- AX-001 RELATED_TO AX-004: likely low-value;
- P-006 RELATED_TO MP-002: potentially valid lineage/navigation;
- FP-010 RELATED_TO FP-011: potentially valid but must not replace causal distinction;
- FP-001 RELATED_TO FP-012: potentially valid D-02 navigation;
- T-005 RELATED_TO T-015: potentially valid retry/idempotency distinction;
- MP-004 RELATED_TO MP-005: fixed KEEP.

For each return:
- KEEP
- REMOVE_REDUNDANT
- REWRITE_NOTE
- WRONG_RELATION

Do not add a new predicate merely to preserve redundant edges.

### CA7-4 — Domain architecture must be judged by retrieval value, not 1:1 MP symmetry

Primary created 10 domains and explicitly says each is the retrieval home of one promoted MP.

That is not automatically wrong, but it risks becoming a renamed MP index.

Pass B must check:
- each domain routes multiple durable nodes (MP + FP/T/GC/gap);
- it has useful scope/exclusions/cross-domain navigation;
- it does not duplicate MP mechanism prose;
- a focused query normally resolves through <=2 domains.

Do not merge domains merely to reduce count.

### CA7-5 — FP-003 category test

`FP-003 Unbounded Per-Work Dimension` is close to the Pass A trap “property/metric disguised as FP”.

However the actual Primary file includes:
- a concrete failure signature;
- causal mechanism;
- triggers;
- amplification;
- consequences;
- GOOD CASES;
- mitigation links.

Pass B must decide from the actual content:
- KEEP_FP
- REWRITE_AS_CAUSAL_FP
- DEMOTE_TO_PROPERTY

Do not demote solely because the title contains “Unbounded”.

### CA7-6 — T-015 category/effect boundary

`T-015 Idempotency under Explicit Delivery Semantics` is allowed only as a tactic/contract mechanism.

Verify:
- it does not claim to mitigate retry storm itself;
- it only mitigates duplicate-effect damage under explicit delivery semantics;
- retry != idempotency remains explicit;
- no new delivery-semantics MP is implied.

### CA7-7 — Sparse EVIDENCED_BY must not become a second source manifest

Primary intentionally uses sparse load-bearing evidence edges while full source lists live on atomic MP/FP/T pages.

Pass B should keep this sparse design if:
- no unsupported claim relies on a missing direct citation;
- sparse graph edges are clearly navigation/load-bearing references, not exhaustive source truth;
- atomic page source_ids remain the authoritative local evidence list.

### CA7-8 — Retired/reference node handling

Allow:
- MP-011 as RETIRED_TOMBSTONE reference only;
- AX-001..004 as Constitution reference nodes;
- historical P-* as lineage references;
- S/RQ as reference endpoints.

Fail if:
- any becomes a new runtime knowledge type;
- MP-011 receives causal/navigation semantics as a live principle;
- AX-005 appears as a live node;
- P-006 is promoted to MP/FP/T.

### CA7-9 — Progressive-disclosure examples need budget check against actual paths

Primary examples:
- overload/retry storm;
- stale async/ownership;
- contract migration;
- trust boundary/agent action;
- observability vs formal guarantee.

Pass B must count actual default loads and judge against:
- <=2 domains for a focused query;
- <=4 MP-equivalent knowledge nodes before optional source/RQ expansion;
- sources/reports never loaded by default.

Do not count GC or tactic links that are optional rather than required for the focused answer.

### CA7-10 — Mechanical graph integrity

Re-run against the fixed Primary:
- node ID uniqueness;
- path existence;
- edge endpoint resolution;
- FP/T/GC uniqueness;
- frontmatter refs resolve;
- source_ids exist in manifest;
- rq_refs exist in review queue;
- no unexplained orphan durable runtime node;
- no Stage 8 artifact.

The Chief Architect independently confirmed:
- 109 declared nodes;
- 126 edges;
- no duplicate node IDs;
- all edge endpoints resolve inside the declared graph node set.

Path/frontmatter/source/RQ resolution still requires the Challenger's deterministic full audit.

## Pass B required work

1. Execute `V7-01..V7-34` against the actual Primary.
2. For each return:
   - PASS
   - PARTIAL
   - FAIL
   - CHECK_INVALID
   plus exact evidence, mechanism/risk, and minimal correction.
3. Evaluate OD7-1..OD7-6 as fixed decisions.
4. Evaluate CA7-1..CA7-10 explicitly.
5. Classify every FP:
   - KEEP_FP
   - KEEP_WITH_REWRITE
   - DEMOTE
   - REMOVE
6. Classify every T:
   - KEEP_TACTIC
   - KEEP_WITH_REWRITE
   - DEMOTE
   - REMOVE
7. Classify every domain:
   - KEEP_DOMAIN
   - MERGE_CANDIDATE
   - REMOVE_REDUNDANT
8. Classify every RELATED_TO edge.
9. Verify all 16 GCs preserve exact qualifier/non-violation semantics.
10. Verify D-01..D-14 remain navigable.
11. Verify lexical gates and high-risk term senses.
12. Verify no hidden evidence inheritance.
13. Verify source/RQ traceability.
14. Verify progressive-disclosure budget.
15. Verify no Stage 8 smuggling.
16. Reconfirm RS layer NOT_NEEDED under the actual implementation.

## Output

Create only:

`reports/STAGE7_RECONCILIATION.md`

It must include:

1. V7-01..V7-34 matrix;
2. ontology node-type reconciliation;
3. FP disposition matrix;
4. Tactic disposition matrix;
5. domain disposition matrix;
6. RELATED_TO edge audit;
7. predicate-schema recommendation;
8. GC-001..016 integrity matrix;
9. D-01..D-14 preservation;
10. graph/ref/path/source/RQ mechanical audit;
11. progressive-disclosure budget results;
12. bounded Primary remediation set;
13. Stage 8 handoff implications;
14. genuine new owner decisions only.

## Gate recommendation

Return exactly one:

`PASS | PASS_WITH_REMEDIATION | HOLD`

No new research.
No new sources.
No Stage 8 work.
Do not edit Primary artifacts.

## Fail-closed delivery

Before returning:

1. branch descends from accepted Stage 7 challenger Pass A lineage;
2. diff since Pass A contains only `reports/STAGE7_RECONCILIATION.md`;
3. report non-empty;
4. remote HEAD equals reported SHA;
5. remote read-back contains V7-01..V7-34, FP/T/domain matrices, all 16 GCs, D-01..D-14 and CA7-1..10;
6. sealed Stage 2–6 and Primary Stage 7 artifacts remain unmodified.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. gate recommendation
4. V7 summary
5. FP/T/domain dispositions
6. RELATED_TO audit summary
7. graph integrity summary
8. progressive-disclosure budget summary
9. bounded Primary remediation
10. genuine owner decisions
