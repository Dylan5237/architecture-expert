---
id: MODE-CHANGE-REVIEW
type: agent-mode
stage: 9
maps_to: DP-003
---
# CHANGE_REVIEW

## Stage 8 mapping

`decision-playbooks/DP-003.md`

## Trigger

Object is a delta: PR, migration, config/flag change, or precise behavioral change to something that already runs.

## Overlay behavior

Same overlay table as ARCH_REVIEW, scoped to mechanisms the **delta** can introduce. Overlay does not authorize a full-system tour.

## Default context load

Router → Constitution → DP-003 → Q-INT, Q-EVD, Q-PRP, Q-ALT, Q-UNK, plus Q-INTG if any consumer, Q-EVL if boundaries move, overlay sections as needed → one or two domains → linked nodes → GC-009..011 / GC-003 / GC-015 when those surfaces appear.

Emphasize CODE/CONFIG/TEST of the delta and neighbors; not a universal origin ranking.

## Stop / output nuance

Findings must say whether they apply to **the delta**. `terminal_outcome` NO_DEFECT is legal even if the rest of the system is imperfect. Min correction should be expressible as a change to this PR/plan. Unverified commit-message vs code is verification, not automatic KNOWLEDGE_DRIFT; accepted ADR/PRODUCT_INTENT vs delta is drift.

## Handoff

No existing baseline → ARCH_DESIGN. Full as-is review requested → ARCH_REVIEW. Production already failing from this change → INCIDENT_ANALYSIS until attributed, then return here for the fix delta. Options paper rather than a concrete change → ADR_REVIEW.
