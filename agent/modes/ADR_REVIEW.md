---
id: MODE-ADR-REVIEW
type: agent-mode
stage: 9
maps_to: DP-004
---
# ADR_REVIEW

## Stage 8 mapping

`decision-playbooks/DP-004.md`

## Trigger

Object is a named architecture decision: ADR, RFC, options paper, or explicit A vs B vs C.

## Overlay behavior

Activate overlay sections only for dimensions the **options** would change. Not a full-system persona.

## Default context load

Router → Constitution → DP-004 → Q-INT, Q-EVD, Q-PRP, Q-ALT, Q-UNK (Q-VAL / Q-EVL if proof or irreversibility) → domains implicated by the options (usually one or two) → linked nodes → relevant GC for the chosen shape.

The ADR is `CONFIRMED` as text (what it *says*), not automatically `CONFIRMED` current behavior. If an accepted ADR claims current behavior that CODE/RUNTIME contradict → KNOWLEDGE_DRIFT (trigger 2).

## Stop / output nuance

`findings` evaluate the **decision**. `min_correction` means the smallest change to the decision, not a code patch (that is CHANGE_REVIEW). Multiple viable options → `terminal_outcome` OWNER_TRADE_OFF (success, not incomplete work). Dropping a required capability → ARCH_CONFLICT record, not “pragmatic”.

## Handoff

Inventing the first structure with no decision artifact → ARCH_DESIGN. Auditing running code as-is → ARCH_REVIEW first if ADR facts are unverified. Implementing the decision as a PR → CHANGE_REVIEW. Incident → INCIDENT_ANALYSIS.
