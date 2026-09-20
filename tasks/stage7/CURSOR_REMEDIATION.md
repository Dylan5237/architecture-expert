# Stage 7 Task — Cursor Primary Bounded Remediation

## Role

You are the **Primary Knowledge Architect / Ontology Builder** for Stage 7 of `Dylan5237/architecture-expert`.

This is a **bounded remediation pass only** after accepted Codex + GLM Pass B.

Do not reopen research, ontology design, source collection, or Stage 8 work.

## Fixed inputs

Primary starting point:

`research/stage7-knowledge-architecture@62614d4eaec91233d973666e4398368a39d3597c`

Accepted Challenger Pass B:

`challenge/stage7-knowledge-architecture@ddd715e26ce8754890f6752e237a208bd18db334`

Control:

GitHub Issue #18 latest Chief Architect checkpoint.

Work only on:

`research/stage7-knowledge-architecture`

Before editing, verify:
- current branch is correct;
- HEAD is exactly the fixed Primary SHA above;
- you are in a dedicated worktree per agent-project-ops;
- the primary/shared checkout is not being used as the feature worktree.

If any precondition fails, stop and report the mismatch.

## Allowed files

Modify only:

- `relationship-map.yaml`
- `reports/STAGE7_KNOWLEDGE_ARCHITECTURE.md`
- `cases/good-cases/index.md`

No other file may change.

## Required remediation

### R7-1 — Encode explicit predicate schema

In `relationship-map.yaml`, replace the current one-line predicate meanings with an explicit schema for the same eight predicates only:

- DERIVED_FROM
- EXPLAINS
- MITIGATED_BY
- RELATED_TO
- DISTINCT_FROM
- EVIDENCED_BY
- HAS_GOOD_CASE
- HAS_GAP

For every predicate encode/document:

- allowed direction / endpoint kinds;
- symmetry;
- transitivity;
- causality;
- evidence inheritance.

Evidence inheritance must be false for all predicates.

Do not add new predicates.

`OPERATIONALIZED_BY` remains absent/deferred.

Use the accepted Pass B recommendation in `reports/STAGE7_RECONCILIATION.md §6` as the canonical guide.

### R7-2 — Make node classes explicit

In `relationship-map.yaml` header, explicitly classify node categories as:

- RUNTIME_KNOWLEDGE:
  - mother-principle
  - failure-pattern
  - tactic
  - good-case
- NAVIGATION_VIEW:
  - domain
- REFERENCE_ONLY:
  - evaluation-axiom
  - historical-candidate
  - review-signal-lineage
  - gap
  - source
- RETIRED_TOMBSTONE:
  - retired-reserved

State that REFERENCE_ONLY and RETIRED_TOMBSTONE nodes are graph endpoints for lineage/evidence/gap validation and are not default runtime load targets.

Router and relationship edges remain infrastructure, not knowledge node types.

In `reports/STAGE7_KNOWLEDGE_ARCHITECTURE.md §1`, add the same classification clearly, preferably as a classification column or compact note.

Do not delete useful reference endpoints merely because they are not runtime knowledge.

### R7-3 — Prune redundant RELATED_TO edges

From `relationship-map.yaml`, remove exactly these 11 redundant RELATED_TO edges:

- AX-001 → AX-004
- all 10 DOM-* → MP-* “retrieval home” RELATED_TO edges

Do not replace them with another predicate.

Keep exactly these five RELATED_TO edges:

- MP-004 → MP-005
- P-006 → MP-002
- FP-010 → FP-011
- FP-001 → FP-012
- T-005 → T-015

Preserve their existing semantic notes.

Domain routing remains represented by the domain index files themselves.

After pruning, the graph should have:

- same 109 declared nodes;
- 115 total edges;
- RELATED_TO count = 5.

All other predicate counts should remain unchanged.

### R7-4 — Complete GC naive-false-positive fields

In `cases/good-cases/index.md` only:

- GC-003: add an explicit naive false-positive line stating the incorrect flag would be to require a stable modular boundary during genuine exploration when the variation axis is not yet identifiable.
- GC-012: sharpen/add the naive false-positive line so it explicitly states the incorrect flag would be to require fine-grained internal trust separation in a genuinely closed/coarse-trust context, while preserving the existing supply-chain/external trust-boundary carve-out.

Do not alter the accepted compliance qualifiers, provenance, IDs, or count.

GC count remains exactly 16.

## Fixed decisions that must remain unchanged

- 10 canonical MPs remain unchanged.
- 12 FPs remain KEEP_FP.
- 15 tactics remain KEEP_TACTIC.
- 10 domains remain KEEP_DOMAIN.
- GC-001..GC-016 remain the accepted set.
- RS-* remains NOT_NEEDED.
- AX-005 remains reserved and not live.
- MP-011 remains retired/reserved with no live semantics.
- P-006 remains review-signal/property lineage only.
- resources and overload remain separate domains.
- no new source, RQ, type, relation predicate, domain, FP, Tactic, GC, or ID.

## Mechanical validation

Before completion, verify deterministically:

1. diff from `62614d4eaec91233d973666e4398368a39d3597c` changes only the three allowed files;
2. graph node count = 109;
3. graph edge count = 115;
4. RELATED_TO count = 5;
5. other relation counts unchanged from Pass B baseline:
   - DERIVED_FROM 10
   - EXPLAINS 12
   - MITIGATED_BY 19
   - DISTINCT_FROM 18
   - EVIDENCED_BY 21
   - HAS_GOOD_CASE 18
   - HAS_GAP 12
6. no duplicate node IDs;
7. every edge endpoint resolves;
8. every node path still resolves;
9. all FP/T/GC IDs remain unique;
10. GC count = 16;
11. GC-003 and GC-012 now each have an explicit naive-false-positive field/line;
12. no sealed Stage 2–6 file changed;
13. no Stage 8 artifact was created;
14. remote branch HEAD equals the reported SHA.

Commit and push exactly one remediation commit, then stop.

## Return format

Return only:

1. branch
2. SHA
3. R7-1..R7-4 completion matrix
4. final graph counts by predicate
5. node-classification confirmation
6. GC-003/GC-012 completion confirmation
7. changed-files list
8. mechanical validation result
9. any incomplete item + exact reason
10. genuine new owner decisions
