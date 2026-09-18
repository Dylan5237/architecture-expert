# Agent Operating Contract

## Project purpose

Build a general-purpose Architecture Expert from structured knowledge, reasoning procedures, evidence rules, progressive disclosure, and adversarial evaluation. Do not reduce this project to a long system prompt or a checklist collection.

## Durable control plane and evidence authority

This Git repository is the **canonical durable source of truth for accepted project artifacts**: research plans, source manifests, vocabulary, principles, knowledge structures, evaluations, decisions, and prompts. Chat history is not authoritative project state.

External authoritative sources remain the evidentiary basis for architecture claims. In later project-specific use, code/config/runtime evidence may be authoritative for current behavior. Do not confuse repository acceptance state with external factual authority.

## Work discipline

- Work stage-by-stage; never silently skip a gate.
- Preserve source provenance.
- Distinguish `NORMATIVE`, `THEORETICAL`, `EMPIRICAL`, `HEURISTIC`, `CONTESTED`, and `CONTEXT_DEPENDENT` knowledge.
- Prefer primary/authoritative sources.
- Do not silently promote hypotheses to principles.
- Do not overwrite accepted knowledge when new evidence conflicts; record the conflict and route it to review.
- Use progressive disclosure: short routers and indexes, high-density atomic knowledge files, source evidence only when needed.
- Do not create a monolithic README containing the knowledge base.
- Do not make framework/pattern preferences into universal architecture laws.
- Architecture exists to protect required system properties under real constraints, not architectural aesthetics.

## Human / architect escalation

Stop and explicitly surface a decision when there is a genuine unresolved trade-off, conflicting authoritative evidence, irreversible architectural commitment, product-policy choice, or a scope expansion that changes the mission.

## Current gate

Read `TASK.md` and the active stage control issue before starting work. Complete only the currently authorized stage, persist and commit its artifacts, then stop for the Chief Architect gate. Never advance to the next stage on your own.
