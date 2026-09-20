# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent.

## Current phase

Stage 6 — First-Principles Reduction.

Stage 2 — Source Collection is sealed and accepted in `main`.
Stage 3 — Vocabulary Normalization is sealed and accepted in `main`.
Stage 4 — Principle Extraction is sealed and accepted in `main`.
Stage 5 — Contradiction & Counterexample Review is sealed and accepted in `main`:
- canonical falsification corpus and final dispositions: PR #13
- independent adversarial audit + Codex/GLM reconciliation: PR #14
- final Stage 5 gate: PASS
- Stage 6 inputs:
  - NARROW: P-001, P-002, P-003, P-007, P-008, P-009, P-012
  - SURVIVES: P-004, P-010
  - SURVIVES + TAUTOLOGY_RISK: P-013
  - DEMOTE / excluded from principle reduction: P-006

Current control issue: #15.

## Source of truth

This repository is the **canonical durable source of truth for accepted distillation artifacts**. Chat transcripts are not authoritative project state.

External authoritative sources remain the evidentiary basis for architecture claims. Repository acceptance does not replace source provenance.

## Start here

1. Read `AGENTS.md`.
2. Read `TASK.md`.
3. Read `planning/STAGE1_RESEARCH_PLAN.md`.
4. Read `02_VOCABULARY.md` and the canonical `principles/` candidate set.
5. Read the Stage 5 synthesis, adversarial audit, reconciliation, and atomic dossiers.
6. Read `source-manifest.yaml`, `sources/`, and `review-queue.yaml`.
7. Follow GitHub Issue #15 and your assigned branch.
8. Do not enter Stage 7 or build the ontology before the Stage 6 gate.

## Current orchestration

- Kimi Web K3 Cluster: Primary First-Principles Reducer
- Codex harness + GLM 5.3: Independent Reduction Challenger
- Cursor: deterministic repository/eval engineering when needed
- ChatGPT Chief Architect: reduction adjudication, Constitution promotion and architecture gate

Kimi here means the browser-based K3 model-cluster research mode, not a local CLI harness.
Codex owns deterministic repository integrity for the challenger track; GLM 5.3 owns semantic/reduction challenge.

Historical evaluation/research branches remain preserved as execution evidence. Canonical accepted artifacts live in `main`.
