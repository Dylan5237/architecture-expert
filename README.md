# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent.

## Current phase

Stage 2 — Source Collection. The canonical Stage 1 research plan is accepted in `main`.

## Source of truth

This repository is the durable project truth. Chat transcripts are not authoritative project state.

## Start here

1. Read `AGENTS.md`.
2. Read `planning/STAGE1_RESEARCH_PLAN.md` for the canonical research plan.
3. Read `prompts/KIMI_ARCHITECTURE_DISTILLATION_TASK.md` for the full mission and deliverable contract.
4. Follow the current Stage 2 control issue and your assigned branch; do not advance to Stage 3 without the Stage 2 gate.

## Current orchestration

- Kimi Research Mode / K3 cluster: Primary Researcher
- WorkBuddy Research Mode / GLM 5.3: Independent Challenger
- Cursor: deterministic repository/eval engineering when needed
- ChatGPT Chief Architect: synthesis, evidence adjudication, architecture gate

The Stage 1 bake-off evidence remains on `eval/stage1-kimi` and `eval/stage1-workbuddy`.
