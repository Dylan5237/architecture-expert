# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent.

## Current phase

Stage 3 — Vocabulary Normalization.

Stage 2 — Source Collection is sealed and accepted in `main`:
- Primary evidence corpus: PR #4
- Independent challenger evidence: PR #5
- Final Stage 2 gate: PASS

Current control issue: #6.

## Source of truth

This repository is the **canonical durable source of truth for accepted distillation artifacts**. Chat transcripts are not authoritative project state.

External authoritative sources remain the evidentiary basis for architecture claims. Repository acceptance does not replace source provenance.

## Start here

1. Read `AGENTS.md`.
2. Read `TASK.md`.
3. Read `planning/STAGE1_RESEARCH_PLAN.md` for the canonical research plan.
4. Read `source-manifest.yaml`, `sources/`, and `review-queue.yaml` for the accepted Stage 2 evidence corpus.
5. Follow GitHub Issue #6 and your assigned branch.
6. Do not begin Stage 4 without the Stage 3 gate.

## Current orchestration

- Kimi Research Mode / K3 cluster: Primary Researcher / Synthesizer
- WorkBuddy Research Mode / GLM 5.3: Independent Challenger
- Cursor: deterministic repository/eval engineering when needed
- ChatGPT Chief Architect: synthesis, evidence adjudication, architecture gate

The Stage 1 bake-off evidence remains on `eval/stage1-kimi` and `eval/stage1-workbuddy`.
The Stage 2 research/challenge branches remain as historical execution evidence.
