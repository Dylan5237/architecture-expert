---
id: MODE-ARCH-REVIEW
type: agent-mode
stage: 9
maps_to: DP-002
---
# ARCH_REVIEW

## Stage 8 mapping

`decision-playbooks/DP-002.md`

## Trigger

Object is an existing system, subsystem, or path, judged as-is against required properties.

## Overlay behavior

Apply overlays from `decision-playbooks/index.md` when the ask names a family (runtime/concurrency, resources, overload, reliability, trust, observability, integration, evolution, state/data). Overlay changes question sets + first domain only. Do not change finding thresholds.

Runtime/stale-async overlay **must** keep D-02 (FP-001 and FP-012; no third FP).

## Default context load

Router → Constitution → DP-002 → Q-INT, Q-EVD, Q-PRP, Q-UNK + overlay sections → one or two domain indexes → linked MP/FP/T → GC rows for suspected surfaces.

## Stop / output nuance

`terminal_outcome` NO_DEFECT is a successful close. BLOCKER/HIGH_CONFIDENCE_RISK need `refutation_or_invalidation`. Min correction is to the current architecture, not a greenfield rewrite.

## Handoff

Delta as object → CHANGE_REVIEW. Live incident → INCIDENT_ANALYSIS. Named ADR as object → ADR_REVIEW. Do not redesign first (that is ARCH_DESIGN).
