``
id: STAGE10-EVAL-SUITE-DESIGN
title: "Stage 10 Phase A — Independent Eval Suite Design"
stage: 10
phase: A
role: independent-eval-designer-oracle-author
designer: "Codex harness + GLM 5.3"
branch: eval/stage10-suite-design
frozen_sut: 96d9ae333ffc5a8076d635b86634b5151ec0bbc5
date: 2026-09-22
issue: 27
status: DESIGNED_AWAITING_GATE
``

# Stage 10 Phase A — Eval Suite Design Report

## 1. Suite inventory

32 public cases (E10-001..E10-032), one private oracle entry per case (single-file layout `private/oracle.yaml` — the per-case alternative added no maintainability at this size), rubric with 10 dimensions + 11 hard-failure IDs, coverage matrix, manifest.

## 2. Case count

32 (floor 30; quality preferred over padding — near-duplicate candidates were merged: two stampede variants into E10-009; two orphan-worker variants into E10-003).

## 3. Task/mode distribution

ARCH_REVIEW/DP-002: 12; CHANGE_REVIEW/DP-003: 9; INCIDENT_ANALYSIS/DP-005: 6; ARCH_DESIGN/DP-001: 3; ADR_REVIEW/DP-004: 2; explicit-AUTO-ambiguity: E10-024/E10-031 plus 15 AUTO-requested cases whose object identification is itself exercised (17 total AUTO-routing stress points; 6 strict challenge cases: E10-002/003/006/013/024/031 test decoy vocabulary vs object).

## 4. Shape distribution

backend 14 (incl. OTP 1, batch 1, product-org 1), desktop 1, embedded 1, developer-CLI 2, local-first 2, single-process/SQLite 1, formal/proof 1, agent-tool 1, mobile 1, prototype 1, media-pipeline 1, CI 1. Backend is under half; 15 non-backend shapes.

## 5. GOOD CASE count

8 strict non-alarmist cases: E10-006 (supervised daemon), E10-008 (multi-writer design with explicit merge), E10-013 (proof-scope), E10-022 (SQLite economics), E10-025 (exploration), E10-026 (split verdict: CRDT GOOD CASE + growth risk), E10-010 (anti-alarm ADR: current mechanism passes), E10-012 (anti-overengineering: fleet telemetry rejected). Each oracle entry records the naive false positive that must NOT appear (e.g. E10-006: "unbounded lifetime" flag; E10-022: "not production-grade" confirmation; E10-013: blanket observability BLOCKER).

## 6. Ambiguity count

6 strict ambiguity cases: E10-010 (ADR cost unquantified → NEEDS_EVIDENCE/OWNER_TRADE_OFF), E10-012 (evidence gone → NEEDS_EVIDENCE), E10-018 (ADR axis absent → NEEDS_EVIDENCE/OWNER_TRADE_OFF), E10-021 (sampler missed bursts → NEEDS_EVIDENCE with named observation), E10-024 (two accepted authorities collide → ARCH_CONFLICT), E10-031 (resolved incident + pending PR → route-basis ambiguity). Plus partial-evidence tension inside E10-004/015/026.

## 7. Cross-domain count

8 strict: E10-002 (retry bound vs overload policy, D-04), E10-007 (cancellation vs execution bound, D-07), E10-009 (stampede + propagation), E10-016 (contract vs evolution boundary), E10-019 (fan-out bound + class policy, D-04), E10-023 (ownership vs execution guarantee, D-02), E10-026 (multi-writer D-14 + growth bound), E10-029 (bound + policy combination, D-04). D-05 (containment vs trust) exercised inside E10-017/027.

## 8. Failure-family coverage

All 25 required families covered, most via cross-domain combination: main-thread blocking (001), execution-model mismatch (023, D-02), unbounded queue (002, 019, 029), retry amplification (002, 011), orphan ownership (003), stale async (003/023), large-scan bound (014, 032-adjacent), pool exhaustion (009, 031), global lock HOL (020), herd/stampede (009), stale authority (004, 026-adjacent), consumer migration break (005, 016), partial-failure propagation (009, 019), duplicate delivery/idempotency (011, 015, 028), ordering ambiguity (023, 032), resource leak (003-adjacent, 026 growth), noisy neighbor (019 DM starvation), timeout/deadline mismatch (015, 023), unbounded fan-out (019), hidden SPOF (012 svc-inventory-7), overload distinctions (029, 030, 011), trust/least privilege (017, 027), observability gap (012, 021, 030), evolution/change-boundary (018, 025, 005), product-contract conflict (024, 005, 016).

## 9. Rubric

10 dimensions (routing, property understanding, evidence discipline, mechanism accuracy, GC precision, min-correction, product-contract/authority, uncertainty, finding+terminal, scope), 0/1/2 anchors with concrete pass conditions, explicit N/A rules, verbosity-neutral. See `rubric.md`.

## 10. Hard-failure registry

HF-01 unsupported_blocker; HF-02 goodcase_false_positive; HF-03 invented_fact; HF-04 generic_overrides_project; HF-05 silent_contract_weakening; HF-06 wrong_route_material; HF-07 framework_prescription; HF-08 missed_needs_evidence; HF-09 conflict_for_inconvenience; HF-10 false_certainty; HF-11 eval_leakage. Frozen now; not weakenable after runs.

## 11. Leakage audit

Pass over all 32 public files: no MP/FP/T/GC/D/Q IDs; no mechanism names a real user would not use; titles describe symptoms, not ontologies; no expected-verdict vocabulary; `notes_for_runner` contains only logistics (fresh context), no classification hints; public metadata (requested_mode where present, evidence field presence/absence) does not trivially reveal good/bad: GOOD CASEs span all evidence-richness levels and both modes; constraint fields carry realistic project texture. Decoy vocabulary deliberately present where it tests routing (microservices in E10-002, best-practice in E10-018) — these are user-realistic framings the agent must see through, not leakage.

## 12. Oracle ambiguity review

Every entry re-checked for two-acceptable-conclusion situations: encoded as allowed alternates (E10-010 two terminals; E10-018 two terminals; E10-024 any-DP-with-basis; E10-026 split verdict; E10-027 severity band; E10-031 two routes with basis requirement). No case remains too ambiguous for stable scoring. E10-024's routing ambiguity is intentional and the oracle accepts either ADR_REVIEW or DP-002 with coherent basis — ambiguity resolved at oracle level, not deferred to scoring.

## 13. Expected evaluation limitations

(1) Phase C runner context isolation depends on host; limitation must be recorded if per-case fresh context unavailable. (2) Scoring D4/D5 requires judgment; scorer notes constrain but do not eliminate interpretation — Chief Architect adjudicates material disagreements. (3) PUBLIC cases with sparse evidence intentionally elicit NEEDS_EVIDENCE; a runner that "helpfully" adds repository context beyond the case could change answers — runner protocol must forbid supplementary retrieval beyond the SUT repo. (4) Verbose-but-correct outputs must not be penalized on content dimensions (verbosity handled only via D10 discipline).

## 14. Runner-safe files

`eval/stage10/design/public/E10-001..032.md` + `manifest.yaml` (case list/structure only). Nothing else.

## 15. Private/forbidden files

`private/oracle.yaml`, `private/coverage.yaml`, `rubric.md` (scorer-only), this report. The design branch is not merged before blinded runs; Chief Architect exports only the runner-safe set.

## 16. Suite-freeze recommendation

**FREEZE.** 32 cases pass mechanical validation (below); ambiguity resolved at oracle level; leakage audited; hard failures frozen. Recommend the Chief Architect gate freeze the suite and export PUBLIC files to the runner-visible artifact.

## 17. Genuine owner decisions

1. **OD-1 Scorer panel**: confirm Codex+GLM as Phase D scorer (per Issue #27) — designer-scorer identity overlap exists by design (oracle author scores); the CA adjudication step is the counterweight. If the CA prefers a second independent scorer for material-failure confirmation, authorize now.
2. **OD-2 D5 severity band**: E10-027 accepts a MIN_SAFE_FIX↔NON_BLOCKING band. Confirm the band, or tighten to one disposition before freeze.
3. **OD-3 Runner protocol detail**: authorize the runner-protocol author to forbid supplementary context retrieval beyond the SUT repo (limitation 3) — this is a Phase C document not yet written; the constraint should be mandatory, and the CA should confirm.

No other decisions: suite structure, rubric, hard failures, and exposure rules follow Issue #27 + task contract directly.

---

# Remediation Addendum (Phase A pass 2, 2026-09-22)

Status: REMEDIATED_AWAITING_GATE (was HOLD_PENDING_REMEDIATION). All CA10-A1..A11 findings applied on top of 51c4cc3.

## Remediation matrix

| Finding | Resolution |
|---|---|
| CA10-A1 oracle YAML invalid | Rewritten as typed YAML v2 (PyYAML safe_dump); 32 entries one schema; arrays real lists; terminal/disposition separate fields |
| CA10-A2 E10-031 field-shift | Rebuilt: DP-003 preferred, DP-005 alternate with framing; overlays [overload, resources]; fields realigned per CA content |
| CA10-A3 terminal/disposition mixing | E10-013 terminal NO_DEFECT (doc suggestion = NBI disposition); E10-025 terminal NO_DEFECT (testability = NBI); E10-026 terminal MIN_SAFE_FIX (growth = HCR finding; multi-terminal removed); E10-027 per OD10-A2 (HCR + MIN_SAFE_FIX). All 32 audited: terminals exclusively the six canonical values |
| CA10-A4 HF split | HF-11 eval_leakage (narrowed) + HF-12 hidden_cot_exposure added; rubric/manifest updated to HF-01..12; nothing weakened |
| CA10-A5 HF misassignment | E10-004: HF-05 / HF-03-conditional (HF-04 removed); E10-021: HF-10 + HF-03-conditional (HF-04 removed); E10-022: HF-07 (HF-04 removed); E10-026: growth-miss removed from HF-02 (scored in D4/D9). Full audit: no other mismatches |
| CA10-A6 E10-031 leakage | Title -> 'Checkout pool tuning after rollback'; note -> 'Fresh context.'; evidence unchanged |
| CA10-A7 mojibake | U+9225/U+6402 replaced with em-dash in E10-004/015/018/021/023/030; PRD refs normalized to 'PRD Sec. N'; suite scan: only U+2014 remains; zero replacement chars |
| CA10-A8 count reconciliation | Canonical: 32 total; unambiguous DP-001:3/DP-002:10/DP-003:8/DP-004:2/DP-005:7 (sum 30); route-ambiguous 024/031; requested-AUTO 19; strict route-challenge 6 [002,003,006,013,024,031]; strict goodcase 8; strict ambiguity 6; strict cross-domain 8; coverage summary derives from these |
| CA10-A9 E10-024 route | allowed_alternate = ['ADR_REVIEW/DP-004 with object-based basis'] only; AUTO->any removed |
| CA10-A10 coverage YAML | Typed YAML v2; list arrays; normal keys; counts derived+asserted |
| CA10-A11 machine validation | PyYAML validation: manifest/oracle/coverage parse; 32=32; ID sets identical; keys complete; types correct; terminals within six canonical; dispositions never in terminals; HF refs exist; coverage IDs match; counts reconcile; no dups; no crossover; no run outputs |

## OD10 decisions applied

OD10-A1: scorer stays Codex+GLM, CA adjudicates. OD10-A2: applied to E10-027. OD10-A3: recorded as Phase C constraint in manifest exposure rules (runner = frozen SUT + public payload only; no web/external/private context; stop if unenforceable).

## Validation record

Tool: Python 3.11.9 + PyYAML (yaml.safe_load). Results: oracle 32/32 parse, schema uniform, terminal/disposition separation OK; coverage 32 IDs, strict counts 6/8/6/8, unambiguous sum 30; manifest parses; public mojibake scan zero.

## Freeze recommendation

FREEZE — remediation complete; all CA findings resolved; machine validation green.

## Owner decisions

None new. Prior OD-2 resolved by OD10-A2; OD-3 resolved by OD10-A3 (manifest constraint); OD-1 settled by OD10-A1.
---

# Final Gate Microfix (Phase A pass 3, 2026-09-22)

R10A2-1: E10-024 finding-disposition list corrected — ARCH_CONFLICT removed from acceptable_finding_dispositions (now empty; ARCH_CONFLICT remains the terminal outcome with its record expectations in correction/authority fields). All 32 records mechanically revalidated: every disposition value within the canonical five families; every terminal value within the six canonical outcomes; E10-024 was the only violation.

R10A2-2: E10-024 public metadata neutralized — title 'Quarter planning: feature freeze and regulatory export deadline'; task_object 'quarter planning architecture decision under fixed team capacity'. User request, evidence, constraints, AUTO mode, and runner note unchanged; the discoverable tension remains in the evidence.

R10A2-3: manifest status READY_FOR_FREEZE; exposure rules and Phase C isolation constraints preserved. No coverage-count, rubric, HF-registry, or case-count change.

Recommendation remains FREEZE.