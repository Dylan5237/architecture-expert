---
id: MODE-ARCH-DESIGN
type: agent-mode
stage: 9
maps_to: DP-001
---
# ARCH_DESIGN

## Stage 8 mapping

`decision-playbooks/DP-001.md`

## Trigger

Object is a system, slice, or capability that does not yet exist (or exists only as intent). Propose a min-sufficient structure.

## Overlay behavior

Overlays are optional and rare (shape-implied dimensions only). They tune Q sections / first domain; they do not turn this mode into a specialized “concurrency designer” persona. Retrieve overlay table from `decision-playbooks/index.md`.

## Default context load

Router → Constitution → DP-001 → Q-INT, Q-PRP, Q-EVD, Q-ALT, Q-UNK → at most two domains implied by the shape → linked MP/FP/T → GC if a proposed form looks like a naive violation (e.g. GC-003 exploration).

Do not start from current-system audit files as the primary object.

## Stop / output nuance

`findings` describe the **proposal**, not a defect list. Typical `terminal_outcome`: NO_DECISION_CHANGING_WORK when min-sufficient structure is named; NEEDS_EVIDENCE if properties cannot be stated; OWNER_TRADE_OFF if multiple viable options remain; ARCH_CONFLICT if a required capability cannot be protected. Do not use NO_DEFECT as a finding disposition.

## Handoff

If the task becomes “review this existing system” → ARCH_REVIEW. If an ADR/options paper is the object → ADR_REVIEW. If production is failing → INCIDENT_ANALYSIS first.
