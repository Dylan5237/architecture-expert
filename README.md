# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent.

## Current phase

Stage 5 — Contradiction & Counterexample Review.

Stage 2 — Source Collection is sealed and accepted in `main`.
Stage 3 — Vocabulary Normalization is sealed and accepted in `main`.
Stage 4 — Principle Extraction is sealed and accepted in `main`:
- canonical remediated candidate set: PR #10
- independent boundary audit + Codex/GLM reconciliation: PR #11
- final Stage 4 gate: PASS
- Stage 5 input candidates: P-001, P-002, P-003, P-004, P-006, P-007, P-008, P-009, P-010, P-012, P-013

Current control issue: #12.

## Source of truth

This repository is the **canonical durable source of truth for accepted distillation artifacts**. Chat transcripts are not authoritative project state.

External authoritative sources remain the evidentiary basis for architecture claims. Repository acceptance does not replace source provenance.

## Start here

1. Read `AGENTS.md`.
2. Read `TASK.md`.
3. Read `planning/STAGE1_RESEARCH_PLAN.md`.
4. Read `02_VOCABULARY.md` and the canonical `principles/` candidate set.
5. Read `reports/STAGE4_EXTRACTION.md`, `reports/STAGE4_PRINCIPLE_BOUNDARY_AUDIT.md`, and `reports/STAGE4_RECONCILIATION.md`.
6. Read `source-manifest.yaml`, `sources/`, and `review-queue.yaml`.
7. Follow GitHub Issue #12 and your assigned branch.
8. Do not enter Stage 6 or draft the Constitution without the Stage 5 gate.

## Current orchestration

- Kimi Web K3 Cluster: Primary Falsification Researcher
- Codex harness + GLM 5.3: Independent Adversarial Falsifier
- Cursor: deterministic repository/eval engineering when needed
- ChatGPT Chief Architect: evidence adjudication, candidate disposition and architecture gate

Kimi here means the browser-based K3 model-cluster research mode, not a local CLI harness.
Codex owns deterministic repository integrity for the challenger track; GLM 5.3 owns semantic/adversarial challenge.

Historical evaluation/research branches remain preserved as execution evidence. Canonical accepted artifacts live in `main`.
