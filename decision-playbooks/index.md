---
id: IDX-DECISION-PLAYBOOKS
type: playbook-index
stage: 8
status: CANONICAL
issue: 21
---
# decision-playbooks/

Reasoning procedures, not knowledge articles. Constitution/MP/FP/T/GC remain in Stage 7 files. This index is the Stage 8 entry after `00_ROUTER.md` when the task is to *reason*, not to retrieve a definition.

## Playbook set

Five playbooks. Candidate families from Issue #21 that share a procedure are **overlays**, not extra DPs.

| ID | Title | Distinct procedure |
|---|---|---|
| [DP-001](DP-001.md) | Architecture Design | Forward synthesis of a min-sufficient structure from intent and constraints |
| [DP-002](DP-002.md) | Architecture Review | Diagnose an existing system against required properties |
| [DP-003](DP-003.md) | Change / PR Architecture Review | Judge a delta; prefer minimum correction |
| [DP-004](DP-004.md) | Architecture Decision Review | Evaluate a named decision/ADR among alternatives |
| [DP-005](DP-005.md) | Incident Architecture Analysis | Backward from an observed failure to architecture contribution |

Not instantiated as DPs: Runtime/Concurrency, Performance/Resource/Overload, Failure/Reliability, Integration/Contract/Evolution. Those are overlays on DP-002 / DP-003 / DP-005 (see below). Reopen as separate DPs only if Stage 9 needs first-class modes that this overlay table cannot route.

## Select a playbook

| If the object of reasoning is… | Use | Do not start with |
|---|---|---|
| a system/capability that does not yet exist, or a greenfield slice | DP-001 | DP-002 (no current behavior to audit as the primary object) |
| an existing system / subsystem / path, judged as-is | DP-002 | DP-001 (do not redesign as the first move) |
| a proposed or landed change (PR, migration, config delta) | DP-003 | DP-002 full-system tour; DP-005 unless production is already failing |
| a recorded or proposed architecture decision (ADR, RFC, options paper) | DP-004 | DP-002 unless you must first establish current facts |
| an observed incident / production failure / near-miss | DP-005 | DP-001 redesign; DP-003 PR review of an unrelated diff |

If two match, pick the **object**, not the vocabulary: a PR that caused an incident is still DP-005 until the failure mechanism is attributed; then DP-003 for the fix delta.

## Overlays (knowledge focus, not extra procedures)

Apply on DP-002, DP-003, or DP-005 when the trigger names a mechanism family. Overlay changes **question sets + first domain**, not the playbook.

| Overlay | First domain(s) | Discriminator to keep | Question sections |
|---|---|---|---|
| Runtime / concurrency / stale async | `lifecycle/` **and** `concurrency/` | D-02: FP-001 vs FP-012; do not invent a third FP | Q-OWN, Q-XCN |
| Resource / per-work bounds | `resources/` | D-04 vs overload; D-07 vs cancellation | Q-RES |
| Overload / retry storm | `overload/`; add `resources/` only if a per-work *count/size* is unbounded | retry ≠ idempotency; admission ≠ backpressure ≠ shedding ≠ degradation | Q-OVL, optionally Q-RES |
| Failure / reliability / cascade | `reliability/` | failure domain ≠ blast radius; D-05 ≠ trust; RQ5-001 stays a gap | Q-FAL |
| Trust / agent action | `security/` | D-05: not MP-004 isolation as substitute | Q-TRS |
| Observability / proof vs ops | `observability/`; add `concurrency/` only if the question is whether a guarantee *exists* | D-11; missing OTel ≠ FP-007 | Q-OBS, Q-VAL |
| Integration / contract / migration | `integration/` | independent consumer vs internal; GC-009..011 | Q-INTG |
| Evolution / variation axis | `evolution/` | P-006 is a review signal, not an MP; GC-003/GC-007 | Q-EVL |
| State / multi-writer / conflict | `state-data/` | D-14; D-06 vs ownership | Q-STA |

Never load all ten domains for a focused task.

## Reasoning spine

Compact reusable spine. Not a linear checklist. Issue #21's 18 labels are **coverage of possible dimensions**, not a required path.

### Core (every DP, every task)

1. **Task class** — select DP; name the object of reasoning.
2. **Intent & properties** — required properties (V-004-C), real constraints (V-004-D), applicable AX-003 non-negotiables. AX-001: no property-free verdict.
3. **Evidence baseline** — collect origins allowed by this DP; separate origin from epistemic state (see below).
4. **Conditional mechanism pass** — activate only overlays/dimensions that the shape, symptom, or gap justifies.
5. **GC then correction** — before a defect: route relevant GC(s) and test whether the *mechanism* is present. Then minimum correction / alternatives / `ARCH_CONFLICT`.
6. **Close** — verdict, stop, or escalate. Do not continue to fill unused dimensions.

### Conditional dimensions (activate, do not sequence)

Map to Stage 7 domains. Skip any dimension that cannot change the decision.

| Dimension | Activate when | Default domain |
|---|---|---|
| Ownership / lifecycle | concurrent/async work, cleanup, cancellation, orphans | `lifecycle/` |
| Change-decision boundaries | repeated change, identifiable variation axis, module split debate | `evolution/` |
| Per-work bounds | shared resources, queues, retries-as-count, fan-out, memory | `resources/` |
| Failure propagation | shared bottleneck, cascade, isolation debate | `reliability/` |
| Trust | untrusted input, privilege, agent action, cross-tenant | `security/` |
| Diagnostic evidence | attribution needed, “no telemetry” complaint, proof claims | `observability/` |
| Contracts | independent consumers, compatibility, migration | `integration/` |
| State authority / conflict | shared mutable state, multi-writer, consistency word without V-010 suffix | `state-data/` |
| Overload path | saturation, retry storm, admission/shedding/degradation | `overload/` |
| Execution-model honesty | ordering, cancellation, clocks, isolation *names*, async completion | `concurrency/` |

Issue #21 steps 14–18 (alternatives, trade-offs, validation, minimum correction, unknowns) live in core steps 5–6, not as extra mandatory tours.

## Progressive disclosure

Default load for a focused task:

`00_ROUTER.md` → `01_CONSTITUTION.md` → this index (select DP + overlay) → **one or two** domain indexes → linked MP/FP/T → GC entry if the surface looks like a violation → named RQ → `sources/` only if the claim is disputed, high-risk, or low-confidence.

Do not load all MP pages. Do not paste Constitution prose into a playbook answer. Project code/config/runtime/ADRs outrank generic knowledge for project-specific claims.

## Evidence origin ≠ epistemic state

**Origin** (where the claim came from):

| Origin | Typical pointer |
|---|---|
| PRODUCT_INTENT | PRD, accepted requirements, explicit product decision |
| ARCHITECTURE_INTENT | ADR, accepted Issue, owner-signed architecture decision |
| CODE | current implementation |
| CONFIG | deploy/runtime configuration |
| TEST | tests that pin behavior |
| RUNTIME | metrics, logs, traces, incident timeline |
| HISTORY | git/issue history that records what was true |
| GENERIC_KNOWLEDGE | this repository's MP/FP/T/GC/sources |
| USER_ASSERTION | unverified statement in the task |

**Epistemic state** (how far the claim may be used):

`CONFIRMED` · `HIGH_CONFIDENCE_RISK` · `HYPOTHESIS` · `UNKNOWN` · `CONTESTED` · `NEEDS_EVIDENCE` · `NON_BLOCKING_IMPROVEMENT` · `PERSONAL_PREFERENCE`

Origin never implies confidence. RUNTIME can be `HYPOTHESIS` (ambiguous metric). GENERIC_KNOWLEDGE can be `CONFIRMED` for a mechanism *family* and still `UNKNOWN` for *this* system.

### Project-fact precedence

- Current behavior: CODE / CONFIG / TEST / RUNTIME > GENERIC_KNOWLEDGE > USER_ASSERTION.
- Intended behavior: PRODUCT_INTENT > GENERIC_KNOWLEDGE > inference.
- Architecture intent/history: ARCHITECTURE_INTENT / HISTORY / explicit owner decision > inference.

Generic knowledge explains mechanisms and names risks. It does not rewrite project facts.

### KNOWLEDGE_DRIFT

Emit `KNOWLEDGE_DRIFT` when:

- two project-fact origins disagree (e.g. ADR vs code; PRD vs runtime);
- generic knowledge would require denying a project fact;
- USER_ASSERTION contradicts CODE/RUNTIME/PRODUCT_INTENT and has not been resolved.

Do not silently pick a side. Record: claims, origins, epistemic states, and the next discriminating evidence. Drift is not by itself a BLOCKER; the drifted *behavior vs required property* may be.

## Verdict / severity

| Verdict | Allowed only when |
|---|---|
| BLOCKER / MUST_FIX | An accepted requirement or applicable non-negotiable is violated; include evidence + mechanism + failure mode + material impact. GC does not apply. |
| HIGH_CONFIDENCE_RISK | Strong evidence of a material architecture risk; not yet a proven requirement violation. |
| NEEDS_EVIDENCE | A responsible decision needs a named next observation; stop is allowed. |
| NON_BLOCKING_IMPROVEMENT | Useful; required properties already protected. |
| PERSONAL_PREFERENCE | Style/pattern taste. Never a blocker. Never an escalation by itself. |
| NO_DEFECT | GC matches, or mechanism absent, or properties protected. |
| ARCH_CONFLICT | Real conflict between required capability and a real constraint; not mere inconvenience. |

“Might be bad” is not a BLOCKER. Pattern unpopularity is not a verdict.

## ARCH_CONFLICT structure

Required fields:

- capability / required property
- conflicting constraint
- evidence (origins + pointers)
- fundamental vs inconvenience (inconvenience alone → not ARCH_CONFLICT)
- alternatives that still attempt to protect the property
- trade-offs
- reversibility
- authority owner
- evidence still needed

AX-002: do not silently weaken the product contract to make implementation easier.

## Stop (any DP)

Stop when **one** is true:

1. required properties are protected and no material unresolved risk remains (`NO_DEFECT` or only `NON_BLOCKING_IMPROVEMENT` / `PERSONAL_PREFERENCE`);
2. a supported material defect is identified and the minimum safe correction is clear;
3. multiple viable alternatives remain and the trade-off is an owner preference/authority question;
4. evidence is insufficient and the next discriminating evidence is named (`NEEDS_EVIDENCE`);
5. a real `ARCH_CONFLICT` needs authority beyond this reasoning pass;
6. further analysis would add detail but not change the decision.

Do not continue in order to visit every dimension or question.

## Escalate (any DP)

Escalate only genuine authority decisions:

- product capability trade-off
- cross-team commitment
- regulatory/compliance interpretation (AX-003, when applicable)
- irreversible data/contract migration
- security/trust policy
- material cost/budget commitment
- unresolved contested evidence that changes the decision (`KNOWLEDGE_DRIFT` that owners must pick)

Do not escalate: routine mechanism selection with sufficient evidence; implementation detail that does not change required properties; personal preference.

## Minimum correction (review / change / incident)

1. Name the protected property.
2. Name the concrete failure mechanism (FP or equivalent causal account).
3. Name the smallest boundary / ownership / bound / resource / contract / evidence change that breaks that mechanism.
4. Compare to a wider redesign.
5. Prefer wider redesign only if the local fix cannot protect the property or creates worse systemic risk.

“No rewrite unless necessary” is this rule, not a ban on redesign.

## GOOD CASE rule

Before a defect verdict: load the relevant GC row(s). Ask whether the *mechanism* is present in this system. Compliant alternate forms (OTP supervision, path-level admission, explicit CRDT merge, proof-scoped evidence, exploration without a known axis, …) are `NO_DEFECT`, not “missing pattern X”.

## Shared output contract

Every DP closes with:

```text
playbook: DP-00N
overlay: <none | name>
intent_and_properties: [...]
activated_dimensions: [...]
question_sets: [Q-…]
knowledge_route: [domain / MP / FP / T / GC / RQ]
evidence: [{origin, pointer, epistemic_state}]
knowledge_drift: none | {claims, origins, next_evidence}
gc_checked: [GC-…] | none-applicable
findings: [{verdict, property, mechanism, failure_mode, impact, min_correction}]
arch_conflict: none | {fields above}
stop_reason: <1–6>
escalation: none | {owner, decision}
```

Fill only activated parts. Empty sections are a smell that the pass did not stop.

## Question bank

Canonical questions: `question-bank/index.md`. Playbooks reference IDs. Do not copy question text into DP files.

## Relationship to Stage 9

Stage 9 may encode DP triggers as Agent modes. This Stage does **not** write system prompts or mode files. Overlay table above is the mode-overlap contract: specialized reviews are DP-002/003/005 plus overlay, not extra personalities.
