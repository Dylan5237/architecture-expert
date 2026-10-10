# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent. The Agent protects required system/product properties under real constraints and prefers evidence-based, minimum-sufficient architectural decisions rather than framework fashion.

## Current status (2026-10-10)

- **Stages 1–9:** research, source provenance, vocabulary, first-principles Constitution, knowledge architecture, reasoning playbooks and Agent v0.1 are complete. Frozen v0.1 SUT: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`.
- **Stage 10:** 32-case blinded evaluation on company gateway `glm-5.3`, complete and adjudicated: **434/538 (80.67%)**. The evaluation itself passed; the Agent still has notable evidence-discipline weaknesses. [Stage 10 adjudication](https://github.com/Dylan5237/architecture-expert/blob/eval/stage10-phase-d-adjudication/reports/STAGE10_PHASE_D_ADJUDICATION.md).
- **Stage 11:** 12-case paired holdout, complete and adjudicated: v0.1 **184/212 (86.79%)**, v0.2 **176/212 (83.02%)**; v0.2 **FAILED** preregistered quality gates. Do not treat v0.2 as the default or formally released version. [Stage 11 adjudication](https://github.com/Dylan5237/architecture-expert/blob/eval/stage11-phase-d-adjudication/reports/STAGE11_PAIRED_ADJUDICATION.md).
- **First usable Beta:** v0.1 Codex Skill at `release/architecture-expert-v0.1-beta@34acd74cb4f114e0ef7280e045db6e590957aefa`. The local executor reported user-level installation and one successful cross-workspace invocation. This is **BETA_USABLE / human-reviewed**, not a certified or unattended decision engine.

**Current product priority: real project use and feedback, not another evaluation infrastructure project.** Stage 10/11 evaluation issues #27/#30 are complete and closed. This repository's `main` hosts the accepted research/knowledge artifacts and handoff; the Beta distribution and final adjudications are retained on their explicitly named branches.

## For a new ChatGPT project session

Read these before resuming work:

1. [Short successor entry](docs/handoffs/2026-10-10/00_新会话入口.md)
2. [Full project handoff, evidence refs, state and next steps](docs/handoffs/2026-10-10/01_完整项目交接.md)

Do not re-read all research, assume the newest prompt is best, or infer Windows local installation state from repository commits.

## Use the Codex Beta

Read [Codex distribution README](https://github.com/Dylan5237/architecture-expert/blob/release/architecture-expert-v0.1-beta/distribution/codex/README.md) and [SKILL.md](https://github.com/Dylan5237/architecture-expert/blob/release/architecture-expert-v0.1-beta/distribution/codex/architecture-expert/SKILL.md).

The installed Skill needs a persistent local copy of the **frozen v0.1** knowledge and the user-scoped `ARCHITECTURE_EXPERT_KB_ROOT` variable. The initially reported knowledge root is under a temporary worktree; do not delete it before a confirmed move to stable storage and a successful readback.

Invocation example from another project (model availability depends on the host):

~~~powershell
codex exec -m gpt-5.6-sol -c model_reasoning_effort=max '$architecture-expert 请评审当前项目架构'
~~~

The Codex-host smoke is one usability observation. The scored Stage 10/11 performance was measured with `glm-5.3`, so do not transfer numerical scores across providers.

## Knowledge and reasoning entry points

- `00_ROUTER.md` — progressive-disclosure navigation.
- `01_CONSTITUTION.md` — 4 AX evaluation axioms + 10 canonical causal MP.
- `02_VOCABULARY.md` — scoped lexical distinctions.
- `domains/`, `principles/`, `failure-patterns/`, `tactics/`, `cases/good-cases/`, `relationship-map.yaml`.
- `decision-playbooks/` — five primary decision procedures.
- `question-bank/` — 55 conditionally activated questions.
- `agent/system-prompt-v0.1.md`, `agent/modes/` — frozen v0.1 Agent behavior and mode contracts.

Use these progressively; avoid loading the entire knowledge corpus. `sources/` and `review-queue.yaml` preserve external evidence and unresolved gaps. Runtime project facts must come from the actual user project's code, configuration, tests, runtime, accepted intent and ADRs.

## Project governance

GitHub is the canonical durable control plane; chat transcripts are not project facts. For nontrivial changes, use task documents in the repo and isolated branches/worktrees; let the local Agent receive a concise pointer rather than a massive chat prompt. Preserve Product Contract and GOOD CASE protections, separate fact/inference/unknown, require owner decisions for genuine high-impact trade-offs, and avoid premature or over-engineered gates.

Accepted evaluation results must not be silently overwritten by newer documents. Frozen Stage 10/11 cases have been unsealed and are no longer fresh holdouts.
