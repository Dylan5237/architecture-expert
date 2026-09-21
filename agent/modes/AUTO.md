---
id: MODE-AUTO
type: agent-mode
stage: 9
maps_to: none
---
# AUTO

Router only. Not a sixth reasoning procedure. Not mapped to a DP of its own.

## Trigger

Default when the host does not set an explicit reasoning mode.

## Routing

1. Identify the object of reasoning (capability-to-build, existing system, delta, named decision, observed failure).
2. Select **exactly one** primary DP using `decision-playbooks/index.md` “Select a playbook” plus `agent/system-prompt-v0.1.md` §3.
3. Start with **zero overlays**. Activate an overlay only when task shape, symptom, or evidence justifies that mechanism family (`decision-playbooks/index.md` overlay table). “For completeness” is never a valid activation reason. Overlay never replaces the DP.
4. If two objects could apply **and** the DP choice would change the procedure, ask one targeted clarification. Otherwise proceed.
5. Hand off to the corresponding explicit mode contract (ARCH_DESIGN … INCIDENT_ANALYSIS) and execute that DP. Do not keep a separate AUTO reasoning path.

## Default context load

After DP selection: `00_ROUTER.md` → `01_CONSTITUTION.md` → the selected DP file → overlay-activated question sections only. Do not load all five DPs.

## Stop / output nuance

AUTO itself does not produce findings. The selected DP’s stop/output rules apply unchanged.

For AUTO, the user-visible result must include `route: {mode, dp, overlays, basis}`: selected explicit mode, exactly one primary DP, overlays or `none`, and one concise routing reason based on the object of reasoning. The basis is a routing explanation for user-correctability, not hidden chain-of-thought and not a step-by-step deliberation transcript.

## Handoff

If the object changes mid-pass (e.g. incident attributed, now reviewing the fix PR), re-route once and name the new mode/DP. Do not run two primary DPs in parallel.
