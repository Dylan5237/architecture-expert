> **SUPERSEDED — DO NOT EXECUTE.** Stage 11D final adjudication rejected v0.2 for default Beta packaging. Use `tasks/release/CODEX_FIRST_USABLE_V01_BETA.md` on `release/architecture-expert-v0.1-beta` instead. This historical task is preserved for traceability.

# Architecture Expert — First Usable Beta (Codex-first)

## Objective

**Deliver a real, invocable Architecture Expert, not another evaluation framework.**

The architecture knowledge and Agent v0.2 already exist. This task is **product packaging only**: make the existing v0.2 accessible as a Codex skill from an ordinary project workspace.

Do not wait for Stage 11D scoring. This is a clearly labeled **Beta / HOLDOUT_UNEVALUATED**, not a certified release.

## Branch

- Repository: `Dylan5237/architecture-expert`.
- Dedicated branch: `release/architecture-expert-v0.2-beta`.
- Starting HEAD exactly `c12b67c7410878960c45a9934ded6ae52ae6c42f`.
- Independent clean worktree; do not merge `main`.
- Task source: `origin/main:tasks/release/CODEX_FIRST_USABLE_BETA.md`.

## Product promise

From an ordinary user's project in Codex, the user can explicitly invoke **Architecture Expert** and request:

- design of a new capability;
- as-is architecture review;
- change/PR architecture review;
- ADR/decision review;
- incident architecture analysis.

The response must apply the existing v0.2 behavioral contract and selectively retrieve the existing KB. Do not embed all KB into the skill, invent new principles, or replace the Agent with a short generic architecture prompt.

**First host = Codex.** Cross-host packaging is a later concern.

## Work to do

1. Build a minimal, discoverable Codex skill:
   - `distribution/codex/architecture-expert/SKILL.md`;
   - `distribution/codex/README.md` describing install, configure, invoke, uninstall, limitations.
   - Only add a tiny install/config helper if manually doing so is materially error-prone on Windows. No daemon, UI, MCP service, runtime, web app, or bundled model backend.

2. The skill **must use the canonical repo source**, not duplicate or fork it:
   - `agent/system-prompt-v0.2.md`;
   - `agent/modes/AUTO.md` or one of the five explicit modes;
   - `00_ROUTER.md`, `01_CONSTITUTION.md`, selected DP, then on-demand knowledge.
   - Respect v0.2 evidence/terminal/minimum-correction guards, S1–S6, typed findings, product authority, and progressive disclosure.
   - Do not load all KB files by default.
   - Keep model-facing access confined to the user's project and the architecture knowledge root. Do not load `eval/`, `tasks/`, `reports/`, sealed holdout content or private oracle.

3. Resolve the knowledge-repo root deterministically:
   - user-configured local clone path (preferred); or a fixed, documented local clone of this public repo;
   - do not assume any private Windows absolute path;
   - if missing, give one concise setup instruction instead of pretending to have loaded KB.
   - The skill should be usable from **other project directories**, not only inside `architecture-expert`.

4. For Codex Desktop on Windows, verify the **actual supported USER skill directory** on the local installation before installing. Prefer the current supported `%USERPROFILE%\.agents\skills` convention when available; older installations may use `%USERPROFILE%\.codex\skills`. Do not create duplicate active copies.
   - Install in the verified user-scoped directory, without overwriting unrelated skills.
   - If permissions/host capabilities prevent installation, stop with `PACKAGED_NOT_INSTALLED` and provide exact manual steps. Do not claim installation success.
   - Do not ask a local text-only Agent to inspect screenshots. The user is responsible for visual confirmation that the skill appears in the host selector if necessary.

5. Validate **one real end-to-end invocation**, not an evaluation suite:
   - from a non-`architecture-expert` project workspace;
   - explicitly invoke the skill;
   - supply an actual architecture question (user-approved, or use a small nonconfidential test project);
   - verify the output contains the correct primary mode/DP, project-evidence origin/status, a concrete mechanism and minimum safe correction/decision, uncertainty where needed and a typed terminal;
   - verify actual knowledge files were read, not merely mentioned.
   - Do not push a customer's/proprietary project's source or analysis into this public repository.

## Acceptance

This task is complete when:
- the skill is locally discoverable and invocable from another project;
- it reads v0.2 + selected mode + relevant canonical KB;
- one end-to-end architecture answer is produced and manually evaluated for basic usability;
- documentation tells the owner exactly how to call it again.

A real-world usability smoke is **not** a replacement for Stage 11D holdout scoring.

## Explicit non-goals

- No changes to Agent v0.1/v0.2, KB, DP, Stage 10/11 evaluation, Harness or model settings.
- No new architecture framework, grading rubric or benchmark.
- No staged acceptance gates, additional worktrees, multi-agent review rounds or issue proliferation.
- No Stage 11 holdout PUBLIC/private/oracle/design access.
- No GitHub main merge or formal release certification.

Keep the total implementation bounded to **one skill package, one installation, one usage smoke**.

## Return

1. branch and SHA;
2. installed user-scope skill path and knowledge root (non-secret; redact user-identifying paths when publishing);
3. invocation phrase;
4. end-to-end smoke result and key evidence that canonical knowledge was loaded;
5. changed files;
6. scope/integrity checks;
7. status `BETA_USABLE`, `PACKAGED_NOT_INSTALLED`, or `BLOCKED` with exact reason.

Commit/push the **package/docs only**, and stop. No proprietary files or real user-workspace outputs in commits.
