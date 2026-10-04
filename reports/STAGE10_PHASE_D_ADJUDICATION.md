# Stage 10 Phase D Chief Architect Adjudication

Status: **ADJUDICATED / FINAL**

Canonical scorer input:

- scorer SHA: `c32adbdac7f4a74077d2ec3235e8feb76aadc0ce`
- canonical evidence SHA: `d6ac48c16f7285f53fbc7af6e5aae4f64f83123b`
- runtime freeze SHA: `7db2639044d3a8f0b8706d70161513238ed29670`
- suite-design SHA: `ff157eb1947860345a305fb29452b51e09dd3a2b`
- SUT SHA: `96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- run_id: `phasec-20260930T101227Z-7db26390`
- evaluated instance: Agent v0.1 / company compute gateway / `glm-5.3`

## 1. Adjudication result

Chief Architect reviewed:

- every scored hard failure;
- every non-HF case marked adjudication-required;
- the allowed alternate route case;
- a stratified spot check of one medium-scoring defect case, one full-score defect case, and one full-score GOOD CASE / mixed finding case.

**No score adjustment is required.**

Final accepted score:

**434 / 538 = 80.67%**

Final hard-failure register:

- HF-01: E10-004
- HF-03: E10-005, E10-006, E10-007, E10-009, E10-011, E10-012, E10-019, E10-022, E10-028, E10-029, E10-030, E10-031
- HF-05: E10-001
- HF-10: E10-018, E10-021

Total: **16 hard failures in 16 cases**.

Important interpretation: under the frozen rubric, an HF does **not** zero the whole case. It caps the affected dimension(s) and remains separately registered. In particular, HF-03 is deliberately strict: an unsupported project fact is a hard evidence-discipline violation even when the overall architecture direction is correct.

## 2. Hard-failure adjudication

### E10-001 — HF-05 upheld

The accepted requirement is that edits are never lost on force-kill. The answer's proposed "durable write-through ... bounded interval acceptable" leaves a window in which acknowledged/in-memory edits can still be lost, while simultaneously claiming that after the fix a kill can never lose edits.

That silently weakens the accepted product contract without owner adjudication.

Ruling: **HF-05 upheld; D7=0 stands.**

### E10-004 — HF-01 upheld

The answer correctly identifies undefined consistency semantics, but its BLOCKER impact claims that the product property cannot be protected or verified and that a material weakening already shipped.

The same answer explicitly acknowledges a decisive missing fact: checkout may revalidate authoritative stock, in which case stale search is not itself a proven violation of the purchase contract.

The BLOCKER therefore lacks a fully supported material-impact pillar for that finding.

Ruling: **HF-01 upheld; D9=0 stands.**

### HF-03 cluster — all twelve upheld

The following statements are unsupported project facts rather than clearly marked hypotheses or generic mechanism statements:

- E10-005: absence of a payload version/compatibility declaration inferred from a history that only says deprecation was never used;
- E10-006: per-stream `gen_server` asserted to hold session state;
- E10-007: static pool asserted to fit 128KB because packet structs are small;
- E10-009: recovery asserted to occur only after the hot entry reloaded at approximately four minutes;
- E10-011: three attempts converted into up to four requests / 4x amplification;
- E10-012: one observed 14:00–16:00 incident expanded into a daily two-hour failure window;
- E10-019: DM volume asserted small and isolation cost trivial;
- E10-022: greenfield operating point supplemented with short transactions / tens-of-MB state without project evidence;
- E10-028: unknown mobile duplicate rate converted into "not instrumented";
- E10-029: unordered spike measurements converted into a definite temporal ordering, plus proposal coupling described as already broken once;
- E10-030: no synchronous downstream dependency converted into no synchronous inbound dispatch;
- E10-031: manual rollback / rollback-capable pipeline converted into an existing SLO-triggered auto-rollback.

These are not merely stylistic overstatements. Each presents an unverified project-specific fact as established and uses it in the reasoning or proposed correction.

The frozen HF-03 definition does not include a separate materiality threshold. Therefore the scorer was correct to treat these as hard evidence-discipline failures while preserving scores on unaffected dimensions.

Ruling: **all twelve HF-03 findings upheld; D3=0 in those cases stands.**

### E10-018 — HF-10 upheld

The answer correctly identifies change-cadence asymmetry, but deterministically concludes that a shared schema keeps the volatile pricing decision shared and that the proposed boundary therefore fails to provide the claimed locality.

The evidence does not establish which pricing changes touch which tables/interfaces or whether reservation code must co-change. The answer itself later acknowledges that current ripple harm is unverified.

The load-bearing mechanism conclusion therefore exceeds the evidence.

Ruling: **HF-10 upheld; D4=0 and D8=0 stand.**

### E10-021 — HF-10 upheld

The answer states that 1% head sampling cannot capture 0.4% burst errors and that each recurrence yields zero attributable evidence.

Those percentages alone do not prove zero capture without request volume, sampler mechanics, correlation, or conditional sampling behavior. The global NEEDS_EVIDENCE terminal is correct, but this local causal claim is falsely certain.

Ruling: **HF-10 upheld; D4=0 and D8=0 stand.**

## 3. Non-HF adjudication-required cases

### E10-010

The answer's substantive analysis keeps the decision open, but the explicit global terminal is `MIN_SAFE_FIX_IDENTIFIED`, whereas the frozen oracle permits `OWNER_TRADE_OFF` or `NEEDS_EVIDENCE`.

The terminal field is part of the output contract and cannot be replaced by a more nuanced paragraph elsewhere.

Ruling: **D9=0 stands; no HF added.**

### E10-015

The idempotency direction is sound, but the answer does not establish whether payment-intent identity is one-to-one with the order or whether a new intent for the same order can still create a duplicate charge path.

Ruling: **D6=1 and D7=1 stand; no HF.**

### E10-020

The answer reasonably prioritizes shortening lock ownership, but states too strongly that the replica proposal does not break the shared-lock mechanism despite insufficient topology detail.

Ruling: **D3=1 and D4=1 stand; no HF.**

### E10-024

`ADR_REVIEW / DP-004` is an explicitly allowed alternate route and the output gives an object-based basis, so D1=2 is correct.

The partial scores on property/conflict/uncertainty handling are also justified: the final `ARCH_CONFLICT` is correct, but parts of the body conditionally weaken the already-given fixed-capacity conflict and blur "capacity sufficient" with "freeze terms revised".

Ruling: **all current scores stand.**

### E10-027

The scorer's calibration is correct: "the migration ticket" is sufficiently tied to the specific template-migration flow that it does not clearly cross the HF-03 threshold, but the workflow dependency remains under-specified.

Ruling: **no HF; D3=1 and D6=1 stand.**

### E10-032

The answer correctly avoids treating bounded retry as a retry storm and correctly identifies the 40→90 minute feedback regression. However the proposed quarantine/known-flaky path does not fully state how failure evidence and merge blocking remain trustworthy while the six known root causes are deferred.

Ruling: **D4=1 and D6=1 stand; no HF.**

## 4. Stratified spot checks

Three non-adjudication cases were spot-checked against PUBLIC evidence and raw output:

- E10-014: strong mechanism and minimum correction; minor evidence-discipline deduction is proportionate; no hidden HF found.
- E10-023: full-score result is justified; it separates cooperative cancellation from owned compensation and preserves the 500ms product constraint.
- E10-026: full-score result is justified; it rejects the false CRDT-authority alarm while independently identifying unbounded tombstone retention without silently weakening offline capability.

No scorer inflation or systematic under-penalization was found in the spot check.

## 5. Final metrics

Accepted final metrics remain:

- total: **434/538 (80.67%)**
- route primary acceptance: **32/32 (100%)**
- full D1 routing-contract score: **53/64**
- terminal accuracy: **29/32 (90.63%)**
- strict GOOD CASE/non-alarm precision: **100%**
- D2 property understanding: **61/64 (95.31%)**
- D3 evidence discipline: **27/64 (42.19%)**
- D4 mechanism accuracy: **51/64 (79.69%)**
- D6 minimum correction: **48/58 (82.76%)**
- D7 product contract/authority: **47/52 (90.38%)**
- D8 uncertainty/evidence: **11/16 (68.75%)**
- D9 finding/terminal: **51/64 (79.69%)**
- D10 scope discipline: **58/64 (90.62%)**

## 6. Architecture interpretation

The 80.67% aggregate is useful but not the primary conclusion.

Agent v0.1 is already strong at:

1. **routing to the right decision procedure**;
2. **identifying the protected system/product property**;
3. **distinguishing compliant GOOD CASE forms from real defects**;
4. **generally preferring local, mechanism-breaking correction over fashionable redesign**.

Its dominant defect is not architecture-pattern knowledge. It is **epistemic discipline at the sentence level**.

The Agent frequently reaches the right architectural direction, then strengthens the narrative with an unprovided project fact, an unjustified quantitative claim, or a causal certainty that the evidence does not support.

That is why:

- primary routing is 100%;
- product/property understanding is above 95%;
- GOOD CASE precision is 100%;
- but D3 evidence discipline is only 42.19%, with twelve HF-03 findings.

The second-order defects are:

- output-contract / terminal selection;
- minimum-correction guarantee boundaries;
- local uncertainty propagation.

## 7. Final Stage 10 disposition

`STAGE10_PHASE_D: PASS / ADJUDICATED`

`STAGE10_EVALUATION: COMPLETE`

`AGENT_V0.1_STATUS: EVALUATED — REPAIR REQUIRED`

This means the evaluation itself is trustworthy and complete. It does **not** mean Agent v0.1 meets a release-quality threshold.

No further Stage 10 scoring or runtime investigation is required.

## 8. Repair boundary

The next phase should not redesign the architecture knowledge system.

The smallest justified v0.2 repair scope is:

1. **Evidence-discipline guard**  
   Before emitting a load-bearing project-specific fact, require one of:
   - explicit project source;
   - explicit HYPOTHESIS / UNKNOWN / NEEDS_EVIDENCE qualification;
   - generic-knowledge label that does not establish project fact.

   Special guard for numbers, frequencies, temporal ordering, "existing/no/never", capacity/cost, and current operational capabilities.

2. **Terminal selection guard**  
   Before final output, reconcile:
   - unresolved evidence;
   - owner trade-off;
   - identified minimum safe fix;
   - no defect;
   - no decision-changing work.

   The typed terminal must match the actual unresolved state.

3. **Correction-guarantee guard**  
   A proposed minimum correction must not claim a product guarantee stronger than its mechanism proves. If sufficiency depends on an unstated relationship or bound, preserve that uncertainty or escalate it.

Do not add case IDs, Stage 10 constants, or case-specific facts to the Agent/KB.

Because Stage 10 oracle is now unsealed, Stage 10 may be reused as a regression suite after repair, but not as the sole proof of v0.2 generalization. A fresh independently designed holdout should be used for the next true capability gate.
