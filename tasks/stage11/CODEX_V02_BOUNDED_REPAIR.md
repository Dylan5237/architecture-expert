# Stage 11B — Agent v0.2 Bounded Repair (No Holdout Access)

## Role

You are the **Stage 11 Agent Repair Engineer** for `Dylan5237/architecture-expert`.

Stage 10 evaluation is complete and adjudicated. Its results justify a **small behavioral-contract repair**, not a knowledge-system rewrite.

Your goal is to produce a provider-independent **Agent v0.2 candidate** with exactly three generic guards:

1. project-evidence discipline;
2. terminal-outcome selection;
3. minimum-correction guarantee sufficiency.

Do not expand into a new reasoning spine, new architectural principles, or a new evaluation harness.

## Work branch / isolation

Use ONLY a fresh dedicated worktree for:

`agent/stage11-v0.2-bounded-repair`

Starting HEAD must be:

`1621916b4f0bef8c5ceb7f43b30ca473416dea03`

Read this task from:

`origin/main:tasks/stage11/CODEX_V02_BOUNDED_REPAIR.md`

Do not merge main.

### CRITICAL: sealed Stage 11 holdout is OFF LIMITS

A fresh Stage 11 holdout was independently designed on a separate branch. You are **not permitted to read or inspect it**.

Forbidden:
- any Stage 11 holdout PUBLIC or private file, manifest, coverage, oracle, or design report;
- the Stage 11 holdout branch or commit tree;
- remote branch discovery, `git fetch --all`, GitHub search, or general repo searches targeting Stage 11 holdout;
- reading other agents' holdout scratch or test payloads.

This task is based ONLY on the already-unsealed Stage 10 **aggregate failure diagnosis**, not on any Stage 11 question content.

If isolation cannot be upheld, stop with `BLOCKED_HOLDOUT_ISOLATION`.

## Permitted source material

Read only what is necessary from the starting branch:

- `agent/system-prompt-v0.1.md`
- `agent/modes/AUTO.md`
- `agent/README.md`
- `reports/STAGE10_PHASE_D_ADJUDICATION.md`
- `reports/STAGE10_PHASE_D_DEFECT_DIAGNOSIS.md` if genuinely needed

Use Stage 10 scorer findings as **diagnostic examples only**; do not copy scenario facts, case IDs, thresholds, expected answers, or frozen test cues into the Agent.

No web research needed.

## Authorized output files

Create or change ONLY:

1. `agent/system-prompt-v0.2.md` (new, complete invocation-ready prompt);
2. `agent/README-v0.2.md` (new, short runtime contract);
3. `agent/modes/AUTO.md` (minimal version-neutral reference change, only if needed to avoid pointing the active v0.2 Agent back to the v0.1 prompt).

Do not modify:
- `agent/system-prompt-v0.1.md`;
- any other mode file;
- DPs, Constitution, Router, KB, question bank or relationship map;
- Stage 10 evaluation/rubric/oracle/evidence;
- any Stage 11 design/test material;
- harness/runner/controller.

No stage report is required: the README plus commit body is enough to record this small change.

## Repair 1 — Project-evidence discipline

Current v0.1 already requires `origin + claim_epistemic_state`, but these classifications do not consistently constrain later narrative sentences.

Add a **brief, load-bearing claim check** to the v0.2 system prompt:

- Any project-specific assertion that supports a finding, causal account, severity judgment, or recommended correction must have a corresponding project-evidence basis, or be explicitly marked as HYPOTHESIS / UNKNOWN / NEEDS_EVIDENCE.
- Pay particular attention to quantities, rates, time ordering, causal attribution, resource/price feasibility, and whether an existing feature, guard, log, process or capability is present or absent.
- "Not supplied" is not equivalent to "does not exist." Generic mechanisms are not project observations.
- Derived calculations must distinguish known inputs and assumptions, with sensible units.
- The qualification must survive from evidence table through narrative, finding, and final recommendation; do not silently promote a hypothesis to CONFIRMED later.

Do NOT introduce citation tags on every sentence, an exhaustive evidence ledger, or a hard ban on ordinary technical reasoning.

## Repair 2 — Terminal selection

Keep the existing Stage 8 typed terminal set unchanged.

Add a brief final selection check to S6 / stop-output logic:

- Choose a terminal based on the **state of the main decision**, not merely the existence of some local fix or supporting finding.
- Distinguish: a mechanism-breaking fix is sufficient now; decision-changing evidence is missing; viable owner alternatives remain; an actual accepted capability/constraint conflict requires authority; a reviewed form is compliant; no further decision-changing work is required.
- A local finding/disposition can coexist with a different run-level terminal, but the selected `terminal_outcome` must not contradict the unresolved decision in the body.
- Do not continue to invent missing work after a justified NO_DEFECT or stop boundary.

Do not add a seventh reasoning stage or new terminal categories.

## Repair 3 — Correction-guarantee sufficiency

Add a brief sufficiency check to the existing minimum-correction section:

- Compare the claimed post-fix guarantee to the **actual mechanism**, including relevant races, crash/kill windows, asynchronous completion, authority boundaries, and unproven assumptions **only when applicable**.
- If a local correction does not establish the whole accepted property, say what remains unprotected and what evidence, additional local step, or owner decision is needed.
- Do not quietly substitute a weaker property (e.g. eventual/best-effort) for an accepted absolute or bounded guarantee.
- Do not promise exact costs, bounds, state recovery or safety without the facts needed to establish them.

No giant cross-cutting verification checklist in every answer.

## Minimality

Treat v0.1 as a frozen baseline.

- Copy its full behavioral contract to v0.2.
- Change version/frontmatter/status appropriately.
- Add only short clauses near the existing relevant sections (project fact authority, minimum correction, stop/output).
- Keep the original S1..S6 spine, mode table, evidence enums, terminal set, progressive disclosure rules, GOOD CASE qualifier gate, and anti-dogma guards unchanged.
- Aim for **under 250 words of net new behavioral requirements**. Use precise wording rather than repetition.
- Do not re-author or summarize v0.1; v0.2 must remain a **complete standalone prompt**.
- In the v0.2 README, name the active system prompt and reuse the five existing mode contracts unchanged. If AUTO.md contains a hard-coded reference to v0.1 §3, replace that reference with a version-neutral one-line "active system prompt §3" reference. No other AUTO semantics change.
- Versioning: do not claim v0.2 has passed evaluation. Mark it `CANDIDATE / HOLDOUT_UNEVALUATED`.

## Validation — mechanical only

Do not invoke an Agent model, do not run Stage 10 regression, and do not run Stage 11 holdout.

Verify:

1. branch and starting HEAD exactly as specified;
2. only the three authorized files changed/added;
3. v0.1 prompt and all KB/DP/Stage 10 evidence files unchanged;
4. v0.2 has the complete S1..S6 workflow and all six typed terminals;
5. evidence-origin and claim-state registries unchanged;
6. the three guards are present and brief;
7. no hard-coded Stage 10/11 case IDs, answers or numeric eval thresholds;
8. no additional model/provider-specific instructions;
9. no additional routing modes, DPs or overlays;
10. no unneeded process steps or broad prompt rewrite;
11. no Stage 11 holdout branch/files read;
12. no test/model calls made;
13. `git diff --check` passes;
14. no secret appears in the diff;
15. remote HEAD equals reported SHA after ordinary push.

Commit and push, then STOP.

## Return format

Return only:

1. branch
2. SHA
3. repair status
4. changed files
5. evidence-discipline guard summary
6. terminal-selection guard summary
7. correction-guarantee guard summary
8. net prompt growth
9. unchanged contracts verification
10. holdout isolation confirmation
11. mechanical validation
12. blocker if any

No Stage 11 measured run is authorized by this task.
