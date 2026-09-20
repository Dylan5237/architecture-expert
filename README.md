# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent.

## Current phase

Stage 8 — Reasoning Model.

Stage 2 — Source Collection: sealed.
Stage 3 — Vocabulary Normalization: sealed.
Stage 4 — Principle Extraction: sealed.
Stage 5 — Contradiction & Counterexample Review: sealed.
Stage 6 — First-Principles Reduction: sealed.
Stage 7 — Knowledge Architecture: sealed and accepted in `main`:
- canonical knowledge substrate: PR #19
- blind ontology audit + Pass B reconciliation: PR #20
- final Stage 7 gate: PASS
- canonical substrate:
  - AX-001..AX-004 in Constitution
  - MP-001..MP-010
  - 10 retrieval domains
  - 12 Failure Patterns
  - 15 Tactics
  - GC-001..GC-016
  - 8 relationship predicates
  - 109 graph nodes / 115 edges
  - RS-* not instantiated

Current control issue: #21.

## Source of truth

This repository is the canonical durable source of truth for accepted distillation artifacts. Chat transcripts are not authoritative project state.

External authoritative sources remain the evidentiary basis for architecture claims. Repository acceptance does not replace source provenance.

## Start here

1. Read `AGENTS.md`.
2. Read `TASK.md`.
3. Read your role-specific Stage 8 task prompt under `tasks/stage8/`.
4. Read GitHub Issue #21.
5. Read `planning/STAGE1_RESEARCH_PLAN.md`.
6. Read `00_ROUTER.md`, `01_CONSTITUTION.md`, and `02_VOCABULARY.md`.
7. Read the Stage 7 MP/domain/FP/T/GOOD CASE/relationship artifacts needed by the task.
8. Read Stage 7 synthesis/audit/reconciliation for lineage and constraints.
9. Do not enter Stage 9 before the Stage 8 gate.

## Stage 8 task prompts

- Cursor Primary: `tasks/stage8/CURSOR_PRIMARY.md`
- Codex + GLM Blind Challenger: `tasks/stage8/CODEX_CHALLENGER.md`

Repository task files are the canonical execution prompts.

## Execution isolation

Stage 8 follows the agent-project-ops invariant:

`one task = one dedicated worktree = one branch`

The shared/primary checkout is sync-only. Parallel Agents must never share a working tree or index.

## Current orchestration

- Cursor: Primary Reasoning-Model Architect
- Codex harness + GLM 5.3: Independent Reasoning-Model Challenger
- ChatGPT Chief Architect: reasoning-contract adjudication and Stage 8 gate

Historical branches remain preserved as execution evidence. Canonical accepted artifacts live in `main`.
