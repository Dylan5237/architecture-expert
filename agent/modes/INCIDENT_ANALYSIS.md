---
id: MODE-INCIDENT-ANALYSIS
type: agent-mode
stage: 9
maps_to: DP-005
---
# INCIDENT_ANALYSIS

## Stage 8 mapping

`decision-playbooks/DP-005.md`

## Trigger

Object is an observed failure, near-miss, or production symptom; question is architecture contribution and minimum containment.

## Overlay behavior

Start from the symptom → `00_ROUTER.md` need-table → one domain; add a second only for a named discriminator (D-02, D-04, D-05, D-07, D-09). Overlay table in `decision-playbooks/index.md`. Competing mechanisms, not a single favorite pattern.

## Default context load

Router → Constitution → DP-005 → Q-INT, Q-EVD, Q-PRP, Q-OBS, Q-ALT, Q-UNK + the surviving-mechanism section → one (or discriminator-forced two) domains → linked FP/T/GC.

RUNTIME is usual first *emphasis* for the timeline, not a global origin rank. USER_ASSERTION (“it must be Kafka”) stays HYPOTHESIS until grounded — verification, not automatic drift.

## Stop / output nuance

Stop when attributed and min correction for **this path** is clear. `terminal_outcome` NO_DEFECT if GC applies or the cause is not architectural. Two remaining FPs → NEEDS_EVIDENCE with the discriminating observation; do not average into a BLOCKER. Do not smuggle a full ARCH_REVIEW or unrelated CHANGE_REVIEW into this pass.

## Handoff

After attribution: broader health → ARCH_REVIEW; the fix PR → CHANGE_REVIEW. No failure observed → do not use this mode.
