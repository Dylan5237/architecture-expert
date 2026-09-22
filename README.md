# Architecture Expert

A durable, model-agnostic knowledge engineering project for distilling a general-purpose software architecture expert agent.

## Current phase

Stage 10 — Blinded Evaluation.

Stage 2 — Source Collection: sealed.  
Stage 3 — Vocabulary Normalization: sealed.  
Stage 4 — Principle Extraction: sealed.  
Stage 5 — Contradiction & Counterexample Review: sealed.  
Stage 6 — First-Principles Reduction: sealed.  
Stage 7 — Knowledge Architecture: sealed.  
Stage 8 — Reasoning Model: sealed.  
Stage 9 — Agent v0.1: sealed and accepted in `main`:
- canonical Agent v0.1: PR #25
- blind Agent audit + Pass B reconciliation: PR #26
- final Stage 9 gate: PASS
- frozen Stage 10 SUT SHA: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`

Current control issue: #27.

## Source of truth

This repository is the canonical durable source of truth for accepted distillation artifacts. Chat transcripts are not authoritative project state.

External authoritative sources remain the evidentiary basis for architecture claims. Repository acceptance does not replace source provenance.

## Stage 10 rule

Stage 10 evaluates a **frozen** Agent v0.1. Do not evaluate moving `main`, and do not repair the Agent during evaluation.

Evaluation is separated into:
1. independent suite/oracle design;
2. Chief Architect suite freeze;
3. blinded Agent run using PUBLIC cases only;
4. independent scoring against PRIVATE oracle;
5. Chief Architect adjudication and Stage 11 repair backlog.

## Current authorized phase

Only Phase A — independent suite + oracle design — is authorized.

Task:
- Codex + GLM: `tasks/stage10/CODEX_EVAL_DESIGNER.md`

No Cursor runner should begin until the Chief Architect freezes the suite and exports runner-safe PUBLIC case inputs.

## Execution isolation

`one task = one dedicated worktree = one branch`

Oracle and runner artifacts must remain separated. Shared/primary checkout is sync-only.

## Current orchestration

- Codex harness + GLM 5.3: Independent Eval Designer / Oracle Author
- Cursor: future blinded SUT runner, currently STOPPED
- ChatGPT Chief Architect: suite gate, evaluation integrity and final Stage 10 adjudication
