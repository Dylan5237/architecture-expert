# Architecture Expert — First Usable Codex Beta (v0.1 Baseline)

## Decision and objective

Deliver an **invocable, user-installed Architecture Expert Codex skill now**. This task supersedes the earlier `CODEX_FIRST_USABLE_BETA.md` task that targeted v0.2.

Reason: Stage 11 paired holdout was finally adjudicated **FAIL** for v0.2; on the same 12 cases v0.1 scored 184/212 (86.79%) versus v0.2 176/212 (83.02%). v0.2 did not improve evidence discipline. The product must not make the failed candidate the unqualified default.

A usable **human-reviewed Beta** is allowed before a formal quality release. Do not describe v0.1 as bug-free or certified: Stage 10 and Stage 11 found material evidence-discipline and product-contract weaknesses. Its measured results were on `glm-5.3`, not necessarily on the user's Codex host model.

**Scope is strictly one skill, one local installation, one real invocation.** No new evaluation or Agent rewrite.

## Branch and source

- Repository: `Dylan5237/architecture-expert`.
- Dedicated branch: `release/architecture-expert-v0.1-beta`.
- Start exactly at the frozen v0.1 SUT SHA `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`.
- Dedicated clean worktree. Do not merge `main`, Stage 10/11 scoring or Agent v0.2 changes.
- Read this instruction from `origin/main:tasks/release/CODEX_FIRST_USABLE_V01_BETA.md`.

The frozen v0.1 Agent contract is:
- `agent/system-prompt-v0.1.md`;
- `agent/modes/AUTO.md` and five existing explicit modes;
- `00_ROUTER.md`, `01_CONSTITUTION.md`, DPs, question bank, knowledge domains, MP/FP/T/GC.

Do not modify any of these canonical Agent/KB files. The original v0.1 prompt's historical `UNEVALUATED` frontmatter is retained for reproducibility. The **distribution documentation** may accurately describe the subsequent measured evaluations, while distinguishing Beta usability from measured capability and formal release.

## Only allowed tracked additions

Create:
- `distribution/codex/architecture-expert/SKILL.md`;
- `distribution/codex/README.md`.

One minimal install/config helper is optional **only if required** to make Windows user-scoped installation reliable. Do not create scripts merely for convenience. No UI, MCP server, daemon, launcher app, custom Harness, provider API or copies of the whole KB.

## Expected behavior

From an ordinary unrelated project in Codex, the user should be able to invoke **Architecture Expert** and request architecture design/review, change/PR review, ADR review, or incident analysis.

The skill must:
1. find the canonical knowledge repository root using a reliable, documented installation method (for example a user-scoped link/junction to the skill under the local repository clone, or one configured local repository root);
2. read the **actual complete** v0.1 system-prompt contract, the appropriate mode contract and selected canonical knowledge files;
3. use v0.1's object-based routing, one DP, S1..S6, origin/epistemic-state evidence handling, GOOD CASE falsification, authority protection, minimum correction, typed terminal outcome and stop discipline;
4. progressively disclose only needed KB pages (Router → Constitution → selected DP → relevant domain and linked nodes);
5. use the user's project evidence for project facts, never generic knowledge as proof of project state;
6. avoid reading `eval/`, `tasks/`, `reports/`, Git internals, or Stage 11 private materials;
7. when KB root or required file is not accessible, state the missing setup explicitly rather than pretending to have loaded knowledge.

Do not replace the full Agent contract with a generic short prompt. Do not paste all canonical source documents into SKILL.md.

## Windows installation

Verify the actual local Codex installation's supported user skill location and install the skill there **once**, without overwriting unrelated existing skills. Prefer the currently supported `%USERPROFILE%\.agents\skills` convention if the host uses it; use the host-documented location otherwise.

The installed skill must be discoverable from another project workspace.

If installation cannot be completed with current permissions/host configuration, stop `PACKAGED_NOT_INSTALLED` and provide the exact manual step. Do not report success without checking the on-disk installation.

Do not ask a text-only local Agent to inspect screenshots. If Codex UI discovery requires a screenshot, the user takes it and ChatGPT performs visual review.

## One real usability smoke

From a workspace **other than `architecture-expert`**:

- explicitly invoke the skill;
- use a small, nonconfidential architecture question or a user-approved real project task;
- verify that the assistant actually read v0.1 + mode + the relevant canonical KB files;
- verify one primary mode/DP, project evidence origin/state, a concrete mechanism, appropriate minimum correction or NO_DEFECT, relevant uncertainty, and a typed terminal;
- do not expect perfect evaluation-grade scoring or measure pass rates.

No user/company project code, company gateway addresses/keys or project raw outputs may be committed to this public repository.

## Acceptance and return

Status:
- `BETA_USABLE`: skill is installed and explicitly invoked successfully from another project;
- `PACKAGED_NOT_INSTALLED`: tracked distribution is complete but installation blocked;
- `BLOCKED`: cannot package or invoke without material missing capability.

Commit/push only the two distribution files (and strictly necessary install helper if used) after scope and secret scan. No merge, no formal release claim.

Return:
1. branch and SHA;
2. status;
3. on-disk installed skill location and knowledge root (redact personal paths in public commits);
4. exact invocation method;
5. actual knowledge files read during the smoke and result;
6. changed files;
7. worktree/secret/scope validation;
8. blocker if any.

**No new Agent version, holdout rerun or infrastructure project is authorized.**
