# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent.

## Current phase

Stage 4 — Principle Extraction.

Stage 2 — Source Collection is sealed and accepted in `main`.
Stage 3 — Vocabulary Normalization is sealed and accepted in `main`:
- canonical vocabulary: PR #7
- independent collision audit + Codex/GLM reconciliation: PR #8
- final Stage 3 gate: PASS

Current control issue: #9.

## Source of truth

This repository is the **canonical durable source of truth for accepted distillation artifacts**. Chat transcripts are not authoritative project state.

External authoritative sources remain the evidentiary basis for architecture claims. Repository acceptance does not replace source provenance.

## Start here

1. Read `AGENTS.md`.
2. Read `TASK.md`.
3. Read `planning/STAGE1_RESEARCH_PLAN.md` for the canonical research and falsification plan.
4. Read `02_VOCABULARY.md` before extracting or reviewing principles.
5. Read `source-manifest.yaml`, `sources/`, and `review-queue.yaml` for evidence and open backflow items.
6. Follow GitHub Issue #9 and your assigned branch.
7. Do not enter Stage 5 or draft the Constitution without the Stage 4 gate.

## Current orchestration

- Kimi Web K3 Cluster: Primary Researcher / Principle Extractor
- Codex harness + GLM 5.3: Independent Principle-Boundary Challenger
- Cursor: deterministic repository/eval engineering when needed
- ChatGPT Chief Architect: synthesis, evidence adjudication, promotion and architecture gate

Kimi here means the browser-based K3 model-cluster research mode, not a local CLI harness.
Codex owns deterministic repository integrity for the challenger track; GLM 5.3 owns semantic challenge.

Historical evaluation/research branches remain preserved as execution evidence. Canonical accepted artifacts live in `main`.
