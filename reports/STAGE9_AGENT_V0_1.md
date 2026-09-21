---
id: REPORT-STAGE9-AGENT-V0.1
type: stage-report
stage: 9
author: Cursor (Primary Agent Compiler / Prompt Architect)
branch: research/stage9-agent-v0.1
date: 2026-09-21
issue: 24
baseline: 1837b10dee4f7efd2c2ab4c68059a5d46820aabd
status: UNEVALUATED
---
# Stage 9 Agent v0.1

Compile sealed Stage 6–8 contracts into a compact provider-independent Agent. No Stage 2–8 semantics changed. No Stage 10 eval fixtures. **v0.1 is unevaluated until Stage 10.**

## 1. Artifact inventory

| Path | Role |
|---|---|
| `agent/system-prompt-v0.1.md` | executable behavioral contract |
| `agent/README.md` | invocation contract |
| `agent/modes/index.md` | canonical mode set |
| `agent/modes/AUTO.md` | router only |
| `agent/modes/ARCH_DESIGN.md` | → DP-001 |
| `agent/modes/ARCH_REVIEW.md` | → DP-002 |
| `agent/modes/CHANGE_REVIEW.md` | → DP-003 |
| `agent/modes/ADR_REVIEW.md` | → DP-004 |
| `agent/modes/INCIDENT_ANALYSIS.md` | → DP-005 |
| `reports/STAGE9_AGENT_V0_1.md` | this synthesis |

Ten authorized files. No provider wrappers. No extra overlay-persona files.

## 2. Prompt design rationale

The system prompt is a **compiler target for behavior**: role, routing, spine, authority matrix, typed fields, GC gate, min correction, drift/conflict, stop/escalation, output, anti-framework guard.

It **points** at Constitution, DPs, question sections, domains, MP/FP/T/GC, sources. Inlining those would violate progressive disclosure and Stage 9 anti-bloat.

AUTO is routing, not a sixth DP. Overlays stay table-driven in Stage 8.

## 3. System-prompt-to-Stage-8 traceability

| Prompt section | Stage 8 home |
|---|---|
| §3 routing table | `decision-playbooks/index.md` select-a-playbook |
| §3 overlays | index overlay table |
| §4 S1–S6 + S4 four-step | index spine |
| §5 load order | Router + index progressive disclosure |
| §6 authority matrix | index project-fact matrix |
| §7 four typed fields | index typed fields |
| §8 blocker/refutation | index finding_disposition |
| §9 drift triggers | index KNOWLEDGE_DRIFT (three only) |
| §10 ARCH_CONFLICT fields | index ARCH_CONFLICT |
| §11 min correction | index minimum-correction |
| §12 stop 1–6 / escalate | index stop + escalate |
| §13 output contract | index shared output schema |
| §13 AUTO `route` field | OD9-4 user-correctable routing; not a new Stage 8 enum |
| lexical notes | Constitution usage contract / Router |

No new enum values. No renamed DPs.

## 4. Mode-to-DP mapping

AUTO → no DP (selects one). ARCH_DESIGN → DP-001. ARCH_REVIEW → DP-002. CHANGE_REVIEW → DP-003. ADR_REVIEW → DP-004. INCIDENT_ANALYSIS → DP-005.

## 5. Overlay handling

Nine overlay families remain parameters (runtime/concurrency, resources, overload, reliability, trust, observability, integration, evolution, state/data). AUTO and explicit modes start with **zero overlays**. Activate an overlay only when task shape, symptom, or evidence justifies that mechanism family. “For completeness” is never a valid activation reason. They tune Q sections and first domain. They must not change finding thresholds, stop, escalation, product-contract protection, or evidence typing. No overlay mode files.

## 6. Context-loading contract

Router → Constitution → selected DP → activated Q sections → 1–2 domain indexes → linked MP/FP/T → relevant GC → named RQ/relationship only if needed → sources only if generic claim is disputed/high-risk/low-confidence.

Never default-load all MPs/FPs/Ts/GCs/questions/sources or Stage reports. Expand only for discriminator, residual ambiguity, surviving cross-domain mechanism, or high-risk generic verification.

## 7. Project-fact authority preservation

Copied as a claim-type matrix, not a CODE>CONFIG>TEST>RUNTIME chain. GENERIC_KNOWLEDGE never establishes project facts. USER_ASSERTION unverified unless accepted. Task-specific emphasis (RUNTIME timeline, delta CODE, ADR-as-text) allowed.

## 8. Typed evidence / finding / terminal preservation

Four fields kept distinct. Claim-state is the five-token set. Finding disposition excludes NO_DEFECT/ARCH_CONFLICT. Terminal outcome is run-level. `refutation_or_invalidation` required on BLOCKER/HIGH_CONFIDENCE_RISK.

## 9. GOOD CASE preservation

S4 four-step gate is mandatory in the system prompt before a material defect/risk. Mode files point at GC rows; they do not list all 16 GCs.

## 10. KNOWLEDGE_DRIFT / ARCH_CONFLICT preservation

Drift: three project-truth-surface triggers only. ARCH_CONFLICT: nine-field record; inconvenience alone invalid; AX-002 no silent contract shrink.

## 11. Stop / escalation preservation

Six stop rules mapped to six `terminal_outcome` values. Escalation remains authority criteria (capability, cross-team, AX-003, irreversible migration, trust policy, material cost, decision-changing contested evidence). Routine mechanism choice is not escalation.

## 12. Anti-overengineering preservation

Min-correction five-step rule; no default microservices/event-driven/K8s/DDD; AX-004 as design goal. Stage 7 omission of a named technique forbids canonical MP/FP/T/GC promotion, best-practice/fashion prescription, and runtime ID minting. The Agent may still **name** a concrete implementation technique as the min correction when (1) its exact mechanism breaks the identified failure, (2) the protected property requires it, and (3) no existing T-* already covers the intervention. Circuit breaker, strangler, event sourcing, hedged requests, expand-contract remain non-canonical labels unless later governed promotion; names are not evidence or universal tactics.

## 13. Duplication / context-efficiency audit

System prompt does not enumerate MP-001..010 statements, Q-001..055 text, FP/T catalogs, or source excerpts. Mode files do not copy DP bodies. Question IDs appear only as section keys (Q-INT, …) where a mode names default activation.

## 14. Provider-independence audit

No vendor chat completions, function/tool schemas, or host-specific CLI flags. Host must supply prompt + mode + repository file access by whatever means it has.

## 15. Prompt-language / Stage 8 semantic-drift audit

Checked against sealed `decision-playbooks/index.md` post-R8: same DP objects, same overlay names, same four typed enums, same three drift triggers, same S4 subsequence, same ARCH_CONFLICT fields, same six stops. No new ontology IDs. P-006 remains non-principle; AX-005/MP-011 reserved. §11 omitted-technique wording now matches Stage 8 DP-002: naming a concrete min-correction technique is allowed when no existing T-* covers it; omission is not a naming ban.

## 16. Representative invocation traces (routing / context only; not eval)

Not expected findings. Not scorecards.

AUTO traces declare user-visible `route: {mode, dp, overlays, basis}`. The basis is a routing explanation for user-correctability, not hidden chain-of-thought. Explicit-mode traces may state mode + DP without an AUTO basis.

**Greenfield capability** — AUTO → ARCH_DESIGN / DP-001; Q-INT/Q-PRP/Q-ALT; at most two shape-implied domains; no current-behavior audit as primary object.

**Existing path health** — AUTO → ARCH_REVIEW / DP-002; overlay if named; 1–2 domains; GC if surface looks like a violation.

**PR / contract migration** — AUTO object = delta → CHANGE_REVIEW / DP-003 + integration overlay; Q-INTG; GC-009..011; do not load expand-contract; do not full-system DP-002.

**ADR A vs B** — explicit ADR_REVIEW / DP-004; Q-ALT; domains of the options only; ADR text ≠ current runtime truth.

**Retry storm incident** — AUTO object = observed failure → INCIDENT_ANALYSIS / DP-005 + overload overlay; optional `resources/` only if retry *count* is the unbounded dimension; competing FP-010/011 vs FP-003; GC-015.

**Stale async / desktop workspace switch** — AUTO or ARCH_REVIEW + runtime/concurrency overlay; Q-OWN+Q-XCN; D-02 both routes; GC-016 if model-provided; no third FP. Same routing for server stale-completion or local-tool workspace switch.

After incident attribution, re-route once to CHANGE_REVIEW for the fix delta. Do not run two primary DPs in parallel.

## 17. Deliberate omissions / Stage 10 boundary

Not created: eval scenarios, expected findings, scorecards, prompt tuning against future cases, provider SDKs, extra modes, RS-*, new MP/FP/T/GC/DP/Q.

v0.1 is **unevaluated**. Stage 10 owns adversarial eval. Do not paper over knowledge gaps by enlarging this prompt.

## 18. Genuine owner decisions only

None. Mode set, overlay-not-persona, and AUTO-as-router are Issue #24 / OD8-2 already fixed. No new DP, overlay, or enum. R9-1..R9-3 implement OD9-4 / CA9-3 / CA9-4 as wording-level compilation fixes.

## 19. Remediation R9-1..R9-3

| ID | Change | Files |
|---|---|---|
| R9-1 | AUTO user-visible `route: {mode, dp, overlays, basis}`; explicit modes may state mode+DP without AUTO basis; basis is not hidden CoT | prompt §13; AUTO.md stop/output; this report §3/§16 |
| R9-2 | Start with **zero overlays**; activate only when shape/symptom/evidence justifies the family; “for completeness” never a reason | prompt §3; AUTO.md routing step 3; this report §5 |
| R9-3 | Stage 7 omission forbids canonical promotion / best-practice / runtime IDs; naming a concrete min-correction technique is allowed when mechanism fits and no existing T-* covers it | prompt §11; this report §12/§15 |
