# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent.

## Current phase

Stage 7 — Knowledge Architecture.

Stage 2 — Source Collection is sealed and accepted in `main`.
Stage 3 — Vocabulary Normalization is sealed and accepted in `main`.
Stage 4 — Principle Extraction is sealed and accepted in `main`.
Stage 5 — Contradiction & Counterexample Review is sealed and accepted in `main`.
Stage 6 — First-Principles Reduction is sealed and accepted in `main`:
- canonical Constitution + reduction: PR #16
- independent reduction audit + Codex/GLM reconciliation: PR #17
- final Stage 6 gate: PASS
- canonical Constitution:
  - AX-001..AX-004
  - MP-001..MP-010
  - AX-005 moved to Usage Contract; ID reserved
  - MP-011 retired/not promoted; ID reserved

Current control issue: #18.

## Source of truth

This repository is the **canonical durable source of truth for accepted distillation artifacts**. Chat transcripts are not authoritative project state.

External authoritative sources remain the evidentiary basis for architecture claims. Repository acceptance does not replace source provenance.

## Start here

1. Read `AGENTS.md`.
2. Read `TASK.md`.
3. Read your role-specific Stage 7 task prompt under `tasks/stage7/`.
4. Read `planning/STAGE1_RESEARCH_PLAN.md`.
5. Read `01_CONSTITUTION.md` and `02_VOCABULARY.md`.
6. Read `reports/STAGE6_REDUCTION.md`, `reports/STAGE6_REDUCTION_AUDIT.md`, and `reports/STAGE6_RECONCILIATION.md`.
7. Read the Stage 5 GOOD CASE / falsification artifacts where needed for non-violation boundaries.
8. Read `source-manifest.yaml`, `sources/`, and `review-queue.yaml` only as evidence/gap support.
9. Follow GitHub Issue #18 and your assigned branch.
10. Do not enter Stage 8 before the Stage 7 gate.

## Stage 7 task prompts

- Cursor Primary: `tasks/stage7/CURSOR_PRIMARY.md`
- Codex + GLM Challenger: `tasks/stage7/CODEX_CHALLENGER.md`

These repository files are the canonical execution prompts for Stage 7.

## Current orchestration

- Cursor: Primary Knowledge Architect / Ontology Builder
- Codex harness + GLM 5.3: Independent Knowledge-Architecture Challenger
- ChatGPT Chief Architect: ontology, relationship, progressive-disclosure and architecture gate

Cursor owns the Primary Stage 7 knowledge-architecture implementation.
Codex owns deterministic repository integrity for the challenger track; GLM 5.3 owns semantic/category/retrieval challenge.

Historical evaluation/research branches remain preserved as execution evidence. Canonical accepted artifacts live in `main`.
