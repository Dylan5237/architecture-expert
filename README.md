# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent.

## Current phase

Stage 9 — Agent v0.1.

Stage 2 — Source Collection: sealed.  
Stage 3 — Vocabulary Normalization: sealed.  
Stage 4 — Principle Extraction: sealed.  
Stage 5 — Contradiction & Counterexample Review: sealed.  
Stage 6 — First-Principles Reduction: sealed.  
Stage 7 — Knowledge Architecture: sealed.  
Stage 8 — Reasoning Model: sealed and accepted in `main`:
- canonical reasoning model: PR #22
- blind reasoning audit + Pass B reconciliation: PR #23
- final Stage 8 gate: PASS
- canonical reasoning substrate:
  - pre-routing + six reasoning stages
  - 5 decision playbooks
  - overlay routing for specialized review families
  - Q-001..Q-055 across 17 sections
  - typed Evidence Origin / Claim Epistemic State / Finding Disposition / Terminal Outcome
  - claim-type project authority matrix
  - narrowed KNOWLEDGE_DRIFT
  - ARCH_CONFLICT / stop / escalation / minimum-correction rules

Current control issue: #24.

## Source of truth

This repository is the canonical durable source of truth for accepted distillation artifacts. Chat transcripts are not authoritative project state.

External authoritative sources remain the evidentiary basis for architecture claims. Repository acceptance does not replace source provenance.

## Start here

1. Read `AGENTS.md`.
2. Read `TASK.md`.
3. Read your role-specific Stage 9 task prompt under `tasks/stage9/`.
4. Read GitHub Issue #24.
5. Read `planning/STAGE1_RESEARCH_PLAN.md`.
6. Read `00_ROUTER.md`, `01_CONSTITUTION.md`, and `02_VOCABULARY.md`.
7. Read the Stage 8 decision playbooks and question bank.
8. Read only the Stage 7 knowledge needed by the task.
9. Do not enter Stage 10 before the Stage 9 gate.

## Stage 9 task prompts

- Cursor Primary: `tasks/stage9/CURSOR_PRIMARY.md`
- Codex + GLM Blind Challenger: `tasks/stage9/CODEX_CHALLENGER.md`

Repository task files are canonical execution prompts.

## Execution isolation

Stage 9 follows the agent-project-ops invariant:

`one task = one dedicated worktree = one branch`

The shared/primary checkout is sync-only. Parallel Agents must never share a working tree or index.

## Current orchestration

- Cursor: Primary Agent Compiler / Prompt Architect
- Codex harness + GLM 5.3: Independent Agent-Contract Challenger
- ChatGPT Chief Architect: Agent-contract adjudication and Stage 9 gate

Historical branches remain preserved as execution evidence. Canonical accepted artifacts live in `main`.
