# Stage 9 Task — Codex + GLM Pass B Reconciliation

## Role

Continue as the **Independent Agent-Contract Challenger** for Stage 9 of `Dylan5237/architecture-expert`.

This is **Pass B — Reconciliation**. Blindness is now intentionally lifted.

- GLM 5.3: semantic/prompt-compiler reconciliation.
- Codex harness: deterministic branch/worktree/ref/file validation, duplication scans, persistence and fail-closed delivery.

## Fixed inputs

Primary:
`research/stage9-agent-v0.1@9b4bc0cc0aa21a9ebd38409a3d898f8d2ed764ae`

Blind Pass A:
`challenge/stage9-agent-v0.1@d99c8e2bfd6b1079303964f8f5dcdfe9f8b59807`

Control:
GitHub Issue #24 latest Chief Architect checkpoint.

Work only on:
`challenge/stage9-agent-v0.1`

Create only:
`reports/STAGE9_RECONCILIATION.md`

Do not edit Primary artifacts or sealed Stage 2–8 files.

## Worktree invariant

Use a dedicated worktree for this task.

The shared/primary checkout may be detached or owned by another Cursor process. Do not repair, switch, reset, stash, or mutate it.

Fail closed unless your worktree:
- is on `challenge/stage9-agent-v0.1`;
- descends from accepted Pass A;
- has no unrelated changes;
- is not shared with another Agent.

## Chief Architect fixed decisions

### OD9-1 — Compactness is semantic first, line-count second

Do **not** make an arbitrary line count a semantic gate.

Canonical compactness test:
- system prompt contains behavioral compiler instructions, not corpus prose;
- no MP/Q/FP/T/GC/source duplication;
- no Stage report prose copied in;
- mode files remain thin routing contracts and do not reproduce DP bodies.

Line counts are diagnostics only.

Current Primary sizes:
- system prompt: ~157 content lines;
- each mode file: ~33 content lines.

These are provisionally acceptable if semantic thinness holds.

A future size increase that adds only formatting is not itself a failure; a shorter prompt that duplicates knowledge or collapses semantics is a failure.

### OD9-2 — Clarification budget

Approve the canonical AUTO ambiguity policy:

Ask **one targeted clarification only when routing ambiguity is real and selecting a different DP would change the procedure**.

Otherwise:
- choose the best-supported route;
- proceed;
- expose the route/basis so the user can correct it.

Explicit mode selection overrides AUTO.

### OD9-3 — Output default

Default output is **concise, human-readable architecture rationale with typed fields/labels where useful**.

Do not require JSON-only output in v0.1.

Host-specific structured adapters may be added later outside the canonical reasoning semantics.

### OD9-4 — AUTO transparency

Every AUTO pass must expose, concisely:
- selected mode;
- selected primary DP;
- overlays (including `none`);
- one-line routing basis.

This is user-correctability, not chain-of-thought.

Do not expose private deliberation.

### OD9-5 — Invocation contract

`agent/README.md` should describe:
- what project evidence to provide/connect when available;
- AUTO vs explicit mode;
- progressive disclosure;
- terminal outcomes;
- unevaluated status.

Do not add provider-specific setup or a required runtime harness in v0.1.

## Chief Architect findings against the fixed Primary

### CA9-1 — Primary is mechanically clean and materially compact

Independent checks confirm:
- exactly one Primary commit from Stage 9 baseline;
- exactly 10 authorized new files;
- system prompt ~157 lines;
- six mode files + mode index;
- five explicit modes map 1:1 to DP-001..005;
- AUTO has no DP of its own;
- no question body from Q-001..055 is copied verbatim into the system prompt;
- no obvious provider/vendor/harness names or tool-call syntax in prompt/modes/README;
- prompt + README both mark v0.1 unevaluated until Stage 10.

Treat this as a strong provisional pass, not an automatic final pass.

### CA9-2 — AUTO route transparency is missing from the compiled output behavior

The Primary routes correctly but does not explicitly require the user-visible result of AUTO to state:
- selected mode/DP;
- overlays;
- concise routing basis.

`agent/modes/AUTO.md` also lacks an explicit output/transparency line.

This conflicts with OD9-4 and Blind Pass A A5.

Expected minimal remediation:
- add a compact `routing` / `route_selected` output field or line;
- require AUTO to populate it;
- explicit modes may state their mode/DP without a routing basis if no AUTO decision occurred.

Do not turn routing transparency into hidden reasoning disclosure.

### CA9-3 — Overlay default should be explicitly zero

Primary says “only justified overlays,” which is directionally correct.

To make A3 fail-closed, Pass B should require:
- AUTO starts with **zero overlays**;
- overlays are activated only when task shape/symptom/evidence justifies the mechanism family;
- “for completeness” is not an overlay activation reason.

This is a wording hardening, not a new routing model.

### CA9-4 — Omitted-buzzword wording risks over-restricting legitimate minimum corrections

Primary system prompt §11 currently says:

> Stage 7 omitted buzzword nodes (...) stay omitted unless the retrieved tactic ID is the min correction.

This is narrower than sealed Stage 8, which allowed a concrete technique such as circuit breaker / strangler / event sourcing / hedged requests **only when its exact mechanism is the minimum correction and it is not already covered by an existing T-***.

Stage 7 omission means:
- do not promote the buzzword into canonical knowledge merely by name;
- do not recommend it as best practice;
- do not create a new tactic ID during runtime.

It must **not** mean:
- the Agent is forbidden from naming a concrete implementation technique solely because no canonical T-* node exists.

Pass B must reconcile this against Stage 8 and propose the smallest wording correction.

### CA9-5 — Thin-mode line counts are not blockers

Blind Pass A suggested ~30 lines; actual mode files are ~33.

Do not request cosmetic trimming merely to meet a number.

Audit whether they duplicate DP procedure/knowledge. If they remain trigger/mapping/overlay/context/stop/handoff contracts, KEEP.

### CA9-6 — Context expansion must remain closed and reports remain negative-space

Primary already has the accepted four expansion conditions:
- discriminator requires it;
- evidence remains ambiguous;
- a cross-domain mechanism survives;
- a high-risk generic claim needs source verification.

Pass B must verify there is no alternate mode/README wording that opens expansion “for completeness”.

Stage reports must remain non-default runtime context.

### CA9-7 — Output-schema compilation needs semantic completeness without prompt bloat

Primary system prompt says “Use the Stage 8 shared output contract fields” and separately encodes the important typed fields.

Pass B must verify Agent v0.1 can still reliably surface:
- selected playbook/mode/overlay;
- intent/properties;
- evidence with origin + claim state;
- knowledge drift;
- GC checked;
- findings + refutation where required;
- ARCH_CONFLICT record;
- terminal outcome;
- stop reason;
- escalation.

Do not demand pasting the full Stage 8 schema if a compact reference + minimum explicit fields preserves behavior.

### CA9-8 — Hidden-CoT boundary

Primary says “concise decision rationale, not hidden chain-of-thought.”

KEEP this.

Pass B should explicitly distinguish:
- user-visible evidence/mechanism/rationale = required;
- private step-by-step deliberation = not requested/exposed.

Do not turn AUTO route basis or finding rationale into a CoT requirement.

### CA9-9 — Stage 10 boundary

Primary representative traces are routing/context demonstrations.

Verify they contain no expected-finding benchmark labels or hidden scorecard logic.

v0.1 must remain explicitly UNEVALUATED.

## Pass B required work

1. Execute `V9-01..V9-32` against fixed Primary.
2. For each return:
   - PASS
   - PARTIAL
   - FAIL
   - CHECK_INVALID
   plus exact evidence, mechanism/risk, minimal correction.
3. Apply OD9-1..OD9-5 as fixed decisions.
4. Evaluate CA9-1..CA9-9 explicitly.
5. Audit system prompt block-by-block against sealed Stage 8.
6. Audit all six mode files + index:
   - exact mapping;
   - thinness;
   - no duplicated DP body;
   - overlay boundary;
   - handoff;
   - AUTO routing/transparency.
7. Audit prompt duplication against:
   - 10 MP statements;
   - Q-001..055 bodies;
   - FP/T definitions;
   - GC prose;
   - Stage report prose.
8. Audit project-fact authority and typed axes.
9. Audit GC/refutation/blocker semantics.
10. Audit KNOWLEDGE_DRIFT and ARCH_CONFLICT.
11. Audit minimum correction and anti-framework neutrality.
12. Audit stop/escalation.
13. Audit provider independence.
14. Audit v0.1 unevaluated/Stage 10 boundary.
15. Produce a bounded Primary remediation set only. No new research or Agent redesign.

## Output

Create only:

`reports/STAGE9_RECONCILIATION.md`

It must include:

1. V9-01..V9-32 matrix;
2. system-prompt contract verdict;
3. compactness/duplication audit;
4. mode mapping + thinness matrix;
5. AUTO routing/transparency audit;
6. overlay-boundary audit;
7. context-loading/negative-space audit;
8. project-fact authority audit;
9. typed-axis audit;
10. finding/GC/refutation audit;
11. drift/ARCH_CONFLICT audit;
12. minimum-correction/framework-neutrality audit;
13. stop/escalation audit;
14. output-contract audit;
15. provider-independence audit;
16. Stage 10 boundary/unevaluated audit;
17. deterministic path/ref/file audit;
18. bounded Primary remediation set;
19. Stage 10 handoff implications;
20. genuine new owner decisions only.

## Gate recommendation

Return exactly one:

`PASS | PASS_WITH_REMEDIATION | HOLD`

No new sources.
No Stage 10 eval work.
Do not edit Primary.

## Fail-closed delivery

Before returning:

1. dedicated worktree only;
2. branch descends from accepted Pass A;
3. diff since Pass A contains only `reports/STAGE9_RECONCILIATION.md`;
4. report non-empty;
5. remote HEAD equals reported SHA;
6. read-back contains V9-01..32, OD9-1..5, CA9-1..9, all six modes, compactness/duplication/output/provider/Stage10 audits;
7. sealed Stage 2–8 and Primary Stage 9 artifacts remain unmodified.

Commit/push and stop.

## Return format

Return only:

1. branch
2. SHA
3. gate recommendation
4. V9 summary
5. system-prompt verdict
6. mode/AUTO verdict
7. context-loading verdict
8. evidence/output verdict
9. drift/conflict/stop/escalation verdict
10. bounded remediation
11. Stage 10 handoff
12. genuine owner decisions
