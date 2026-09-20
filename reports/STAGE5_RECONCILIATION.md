---
id: STAGE5-RECONCILIATION
title: "Stage 5 Challenger Pass B — Reconciliation"
stage: 5
pass: B
role: challenger-reconciliation
challenger: "Codex harness + GLM 5.3"
branch: challenge/stage5-falsification
primary_sha: 309e5b59d5437e05c164a0b2f5a39afbf14032c6
blind_pass_a_sha: b9e1901e1b384e47597799b1dc34f2794a7e57fb
historical_baseline: 05cfea4981c77d9a13520762e2e37244d4079bce
date: 2026-09-20
gate_recommendation: PASS_WITH_REMEDIATION
---

# Stage 5 Challenger Pass B — Reconciliation

## 0. Fixed inputs, method, and gate

Fixed inputs were read directly from the named commits: Primary `309e5b59d5437e05c164a0b2f5a39afbf14032c6`, Blind Pass A `b9e1901e1b384e47597799b1dc34f2794a7e57fb`, historical baseline `05cfea4981c77d9a13520762e2e37244d4079bce`, and the latest Issue #12 Chief Architect checkpoint (OD5-1..OD5-5; CA5-1..CA5-10).

The two independent tracks converge strongly enough to close falsification research: P-006 is DEMOTE; P-007 requires a real narrowing; P-010 survives D-14; D-01/02/04/05/06/07/09 preserve boundaries; H7 remains demoted. The Primary is not merge-ready because it rewrites immutable Stage 2/3 history and contains bounded claim/metadata defects. Therefore the gate recommendation is **PASS_WITH_REMEDIATION**. Stage 6 must not start from the unremediated Primary tree.

No canonical P-* file, Primary artifact, manifest, review queue, or source file is modified by this report. No S-* ID is allocated.

## 1. V5-01..V5-20 reconciliation

### V5-01 — P-001 disposition: PASS

- **Exact evidence:** Primary `reports/stage5/P-001.md` says `SURVIVES + NARROW` and limits GC exemption to runtime-managed reclamation while retaining total-budget and write authority. Pass A §1.1 says GC manages reachability, not task/session/business ownership. CA5-8 makes the dimension explicit.
- **Mechanism / risk:** Managed-heap reclamation can discharge “who frees this object”; it cannot discharge lifecycle/semantic ownership of tasks, timers, sessions, handles, side effects, or mutable business state. Primary overstates OTP in two places: S-114 says every process has a superior and the dossier says runtime prevents ownerless entities, while Erlang’s official Processes page exposes plain `spawn()` as well as linked/monitored variants. Primary also calls the mailbox ownerless; the receiving process owns/consumes its mailbox, while unbounded capacity is a P-003 issue.
- **Minimal correction:** Keep NARROW, but remove “runtime prohibits ownerless actors” and “mailbox is ownerless” claims. State that OTP supervision is an explicit ownership pattern for supervised processes. GC exemption is only managed-heap reclamation; semantic ownership/lifecycle and resource budgets remain.

### V5-02 — P-002 disposition: PASS

- **Exact evidence:** Primary `P-002.md` and Pass A §1.2 both retain the candidate only when a plausible variation axis can be identified; both protect exploration/prototype and deliberately permeable performance paths as GOOD CASES.
- **Mechanism / risk:** Without the scope condition, “design around likely change” becomes hindsight or premature abstraction. Primary correctly labels the evidence heuristic-heavy rather than controlled causal proof.
- **Minimal correction:** Carry the scope precondition into Stage 6; no evidence backflow is required.

### V5-03 — P-003 disposition: FAIL

- **Exact evidence:** Primary synthesis says “duration is not a resource dimension”; its proposed statement repeats “持续时间本身不是资源维度”. Pass A §1.3 instead distinguishes indefinite service lifetime from per-unit-of-work time bounds. CA5-2 rejects the Primary wording.
- **Mechanism / risk:** A daemon or stream can live indefinitely, but a request, dependency wait, retry interval/count, lease, retained resource, queue occupancy, concurrent work item, or fan-out can still consume time and capacity without bound. Deleting time as a dimension would erase deadlines/timeouts and permit stuck work.
- **Minimal correction:** Replace the Primary statement with the Stage 6 input in §2: system/service lifetime may be indefinite; relevant per-work execution/wait/retention dimensions still require an effective bound or governed policy.

### V5-04 — P-004 disposition: PARTIAL

- **Exact evidence:** Primary `P-004.md` retains the graded candidate but proposes process boundary / hardware virtualization / static verification / transaction semantics as interchangeable “alternative guarantees”. Pass A §1.4 retains the canonical graded statement and leaves D-10 NEEDS_EVIDENCE. CA5-5 requires claim-level discipline.
- **Mechanism / risk:** S-122 Arrakis preserves **device access, network and disk protection** through virtualized I/O and kernel control-plane setup; it does not prove all failure propagation is contained. S-123’s eBPF verifier checks specific program properties at load time (CFG/termination discipline, pointer types, bounds/alignment and initialized stack access); it does not contain hardware, environment, shared-resource, integration, or operational failures. Treating these as generic replacements for containment creates a category error.
- **Minimal correction:** Final recommendation is SURVIVES on the already graded canonical mechanism. In examples, state the exact protected dimension. Remove “static verification/transaction semantics replace failure containment” from the proposed principle statement. Keep D-10 as a non-blocking operationalization gap.

### V5-05 — P-006 disposition: PASS

- **Exact evidence:** Primary `P-006.md` returns DEMOTE after D-03; Pass A §1.5 independently returns DEMOTE; OD5-1 fixes that decision.
- **Mechanism / risk:** Change locality is a measurable property/review signal produced by mechanisms such as P-002, not an independent causal principle. RQ3-001 must not be used to rescue it.
- **Minimal correction:** Exclude P-006 from Stage 6 principle candidates; preserve its metric idea for later operationalization/Stage 7 design.

### V5-06 — P-007 disposition: PARTIAL

- **Exact evidence:** Primary `P-007.md` and Pass A §1.6 agree on NARROW, but Primary says observability need “decreases with static-guarantee strength” and labels seL4 a system with “no diagnostic-surface design”. S-118 itself proves functional correctness of a kernel implementation under explicit assumptions: compiler, assembly, boot code, cache management, hardware, specification, devices/integration and deployment conditions remain outside or at the boundary of the proof. CA5-3 and OD5-2 give the accepted scope.
- **Mechanism / risk:** Static proof can discharge runtime questions only for properties actually proved under satisfied assumptions. It does not broadly replace evidence for hardware/environment/integration/availability/operational phenomena. “Proof vs observability” is question-relative, not a scalar substitution curve.
- **Minimal correction:** Use OD5-2’s minimum statement: for operational questions not discharged by stronger static guarantees, evidence needed to distinguish and attribute relevant runtime states must be obtainable by design. Preserve proof scope and telemetry privacy/security as separate trade-offs. Do not impose an automatic controlled-study demotion trigger.

### V5-07 — P-008 disposition: PARTIAL

- **Exact evidence:** Primary `P-008.md` uses RFC 7568 and PEP 404 to allow governed breaking changes; Pass A §1.7 adds the single-owner/internal Linux API GOOD CASE; CA5-7 fixes the intended interpretation.
- **Mechanism / risk:** The principle protects independently evolving consumers from involuntary cost transfer. A stronger security/correctness requirement or coordinated migration can dominate compatibility. The Primary phrase “security debt / technical debt makes break legal” is too loose: debt labels alone are not governance or evidence of priority.
- **Minimal correction:** Use the Stage 6 statement in §2: protect contracts where independent consumers depend on them; allow a break only when a higher-priority security/correctness requirement or an explicit governed migration decision dominates. Do not reduce this to “breaking compatibility is sometimes good.”

### V5-08 — P-009 disposition: PASS

- **Exact evidence:** Primary `P-009.md` and Pass A §1.8 scope enforcement to untrusted input, cross-permission boundaries, external integration, or agent action authority; both preserve closed single-user/internal coarse-trust GOOD CASES.
- **Mechanism / risk:** Enterprise zero-trust evidence cannot be universalized to every in-process boundary. The narrowed statement still preserves supply-chain and external-input boundaries.
- **Minimal correction:** Carry the narrowed scope into Stage 6; keep operational cost as a trade-off, not a refutation.

### V5-09 — P-010 disposition: PASS

- **Exact evidence:** Primary `P-010.md`, Pass A §1.9, D-14, and OD5 checkpoint agree: CRDT multi-writer authority plus explicit merge semantics fits the two-dimensional authority × conflict/consistency model; single-writer is not required.
- **Mechanism / risk:** Calling this a new narrowing obscures that Stage 4 R4 canonical P-010 already contains this two-dimensional wording and explicitly permits multi-writer. Stage 5 confirms rather than changes that boundary.
- **Minimal correction:** Final disposition SURVIVES; carry the R4 canonical statement unchanged into reduction and use CRDT as a GOOD CASE/eval discriminator.

### V5-10 — P-012 disposition: PARTIAL

- **Exact evidence:** Primary `P-012.md` and Pass A §1.10 agree on scoped survival and system-path placement of admission. Primary D-12 says RTOS admission is static priority configuration; CA5-4 rejects that equivalence.
- **Mechanism / risk:** Scheduling priority chooses service order among admitted work; admission control decides whether work enters/continues under capacity constraints. Priority alone does not prove bounded admission or shedding. Desktop/mobile and RTOS cross-shape evidence remains thin.
- **Minimal correction:** Keep NARROW for uncontrollable demand and path-level placement, but mark D-12 NEEDS_EVIDENCE. Remove priority scheduling as proof unless a direct RTOS admission-control source is admitted.

### V5-11 — P-013 disposition: PARTIAL

- **Exact evidence:** Primary `P-013.md` returns SURVIVES and supplies actor mailbox ordering and DB transaction semantics as GOOD CASES. Pass A §1.11 and OD5-5 retain `TAUTOLOGY_RISK`. CA5-9 requires discriminating power.
- **Mechanism / risk:** “Correct systems rely on true guarantees” is vacuous unless the candidate predicts the recurring assumed-vs-provided mismatch and distinguishes it from model-provided guarantees. Primary’s claim that a document/implementation distinction makes tautology risk disappear is too strong; it creates a useful review predicate but does not by itself establish Mother-Principle status.
- **Minimal correction:** Final `SURVIVES + TAUTOLOGY_RISK`; preserve empirical failure class and GOOD CASE discrimination. If Stage 6 reduction leaves only the tautology, demote it to a review/Constitution rule.

### V5-12 — D-03 result: PARTIAL

- **Exact evidence:** Primary says the preregistered independence test fails and demotes P-006. Pass A says local change can exist without explicit/formal boundary, but still demotes P-006 because it lacks an independent causal mechanism.
- **Mechanism / risk:** The tracks differ on whether a property-level counterexample counts as candidate independence. Once P-006 is classified as a metric/property, principle-level independent failure is the relevant test and it fails.
- **Minimal correction:** Record final D-03 as `P-006 NOT INDEPENDENT AS A CAUSAL PRINCIPLE → DEMOTE`; retain “locality can vary independently as an observed property” only as an operationalization note.

### V5-13 — D-04/D-07 independent-failure pairs: PASS

- **Exact evidence:** Both tracks construct the same two-way cases: bounded work without overload policy vs admission with unbounded retries (D-04), and bounded-unowned vs owned-unbounded work (D-07).
- **Mechanism / risk:** Merging would erase different failure mechanisms: capacity governance vs overload selection, and lifecycle ownership vs resource bounds.
- **Minimal correction:** None; preserve the discriminator examples as eval fixtures.

### V5-14 — D-14 CRDT handling: PASS

- **Exact evidence:** Primary S-119 dossier and Pass A SC-06 independently map CRDT to multi-writer authority plus explicit merge semantics. CA checkpoint accepts the two-dimensional model.
- **Mechanism / risk:** Central authority is not required; explicit authority distribution and conflict semantics are.
- **Minimal correction:** None beyond calling this confirmation of R4 rather than a new narrowing.

### V5-15 — D-08 safety floor: PARTIAL

- **Exact evidence:** Primary says a floor exists in safety-critical/regulated contexts and cites S-118/S-120 plus indirect ISO evidence; Pass A calls it contextual; CA5-6 forbids inference of a universal floor from seL4/RFC 7568.
- **Mechanism / risk:** A domain can impose non-negotiable constraints, but that does not create a universal architecture property independent of product/domain. seL4 proves a chosen property; RFC 7568 imposes a specific protocol-security requirement.
- **Minimal correction:** Stage 6 input may say only: “non-negotiable regulatory/safety/security constraints, when applicable, bound the trade space.” Do not present a universal floor without direct normative evidence.

### V5-16 — D-10/D-11/D-12 evidence-state discipline: FAIL

- **Exact evidence:** Primary keeps D-10 NEEDS_EVIDENCE but upgrades D-11 to “判别成立” and D-12 to “成立为形态注释”. Pass A preregisters D-11 CONDITIONAL and D-12 NEEDS_EVIDENCE. CA5-3/4 reject the upgrades.
- **Mechanism / risk:** D-11’s seL4 case is proof-scope-specific, not general substitution; D-12 conflates scheduling with admission. Silent upgrades would overstate cross-shape support.
- **Minimal correction:** D-10 NEEDS_EVIDENCE; D-11 supports NARROW only with property/proof-scope distinction; D-12 NEEDS_EVIDENCE.

### V5-17 — GOOD CASE coverage: PARTIAL

- **Exact evidence:** Primary synthesis §8 preserves ten GOOD CASE classes, including SQLite, supervised daemons, GC, actor/DB guarantees, governed breaks, gateway admission, local trust, prototypes and globally coordinated changes. Pass A §3 adds Linux internal API, seL4, CRDT, append-only log, main-loop lifetime and convention-based locality.
- **Mechanism / risk:** GOOD CASES are future false-positive tests. Omitting the strongest internal-contract case (SC-04) and the exact proof-scope/model-provided-guarantee boundaries leaves the evaluator prone to over-reporting.
- **Minimal correction:** Preserve the consolidated register in §8 as first-class Stage 6/eval input; do not collapse it into prose examples.

### V5-18 — SC-01..09 promotion necessity: PARTIAL

- **Exact evidence:** Primary admits S-118/S-117/S-119/S-114/S-115 overlapping SC-01/02/06/07; does not admit SC-08; does not assess SC-04. OD5-4 identifies SC-04 as the strongest novel candidate and blocks automatic promotion.
- **Mechanism / risk:** Duplicate admission inflates source-family independence; rejecting SC-04 without evaluation would lose the cleanest P-008 internal-owner counterexample. SC-05 cannot silently reverse Stage 2 CH-S-04 adjudication.
- **Minimal correction:** Apply the matrix in §5. No challenger source is promoted on this branch; recommend SC-04 for later CA promotion review only.

### V5-19 — P-012 source-family concentration: PASS

- **Exact evidence:** Primary synthesis §9 and P-012 dossier explicitly retain the SRE/AWS concentration warning; Pass A §4 reaches the same conclusion.
- **Mechanism / risk:** S-090 and accident reports diversify evidence but do not erase the operational-narrative concentration.
- **Minimal correction:** Keep the lineage warning through Stage 6; no broad research rerun.

### V5-20 — no Challenger S-* smuggling: PASS

- **Exact evidence:** Diff `05cfea49..b9e1901` contains only `reports/STAGE5_ADVERSARIAL_AUDIT.md`; Pass A allocates SC-* leads only.
- **Mechanism / risk:** Challenger/Primary source ownership remains intact.
- **Minimal correction:** None. Primary’s S-001..113 rewrites are a separate CA5-1 integrity failure addressed in §6.

## 2. Final candidate disposition matrix and minimum Stage 6 input

| Candidate | Primary | Pass A | Final Stage 5 recommendation | Minimum Stage 6 input / scope delta |
|---|---|---|---|---|
| P-001 | SURVIVES + NARROW | SURVIVES (clarify runtime-enforced ownership) | **NARROW** | Runtime entities and mutable state need semantic/lifecycle ownership. GC may discharge managed-heap reclamation only; it does not discharge task/session/handle/side-effect/state ownership or memory-budget responsibility. OTP supervision is a compliant pattern, not a runtime invariant for every spawned process. |
| P-002 | SURVIVES + NARROW | SURVIVES scoped | **NARROW** | When repeated change is expected and a plausible variation axis can be identified, hide volatile decisions behind boundaries whose sides follow different change rules. Exploration with unknown variation axes is a GOOD CASE, not a violation. |
| P-003 | SURVIVES + NARROW (bad wording) | SURVIVES with per-work clarification | **NARROW** | A system/service/stream may live indefinitely. For each relevant unit of work, wait, retry, retained resource, queue, concurrency and fan-out dimension, provide an effective bound or governed degradation policy. Time remains a bound dimension at work/wait scope. |
| P-004 | SURVIVES + NARROW | SURVIVES scoped/graded | **SURVIVES** | Keep the Stage 4 graded outcome-oriented statement: design failure domains against acceptable impact and economics; do not prescribe process boundaries. Arrakis constrains device/network/disk protection; eBPF verifier constrains selected program-safety properties. Neither generically replaces containment. D-10 remains NEEDS_EVIDENCE for measurement. |
| P-006 | DEMOTE | DEMOTE | **DEMOTE** | Remove from Stage 6 principle set. Keep change locality/amplification as a P-002-associated property/review signal; do not trigger RQ3-001 to rescue it. |
| P-007 | SURVIVES + NARROW | NARROW | **NARROW** | For operational questions not discharged by stronger static guarantees, evidence needed to distinguish and attribute relevant runtime states must be made obtainable by design. State proof assumptions and retain runtime evidence for environment/hardware/integration/operational phenomena outside proof scope. |
| P-008 | SURVIVES + NARROW | SURVIVES with strong exemption | **NARROW** | Preserve contracts when independent consumers depend on them. A higher-priority security/correctness requirement or an explicit governed migration decision may legitimately break compatibility; the break remains deliberate, scoped and costed. Single-owner coordinated internals are a GOOD CASE. |
| P-009 | SURVIVES + NARROW | SURVIVES scoped/graded | **NARROW** | Require least trust/privilege at untrusted-input, cross-permission, external-integration and agent-action boundaries. Do not require fine-grained internal boundaries in a closed single-user shape when cost exceeds protected benefit. |
| P-010 | SURVIVES + NARROW (R4 confirmed) | SURVIVES | **SURVIVES** | Carry the existing R4 two-dimensional authority × conflict/consistency statement unchanged. CRDT, append-only log and local-first are GOOD CASES when authority distribution and merge/conflict semantics are explicit. |
| P-012 | SURVIVES + NARROW | SURVIVES scoped | **NARROW** | Where demand can exceed capacity, the request/work path must define admission and degradation: what enters/continues, what is rejected/deferred, and what priority protects. Placement may be gateway/mesh/service/system. Priority scheduling alone is not admission control; D-12 remains NEEDS_EVIDENCE. |
| P-013 | SURVIVES | SURVIVES + tautology warning | **SURVIVES + TAUTOLOGY_RISK** | Preserve the empirical discriminator: failures occur when correctness assumes timing/order/interruption/cancellation/clock guarantees absent from the actual model. Runtime-provided actor mailbox order, non-preemptive event-loop segments and documented DB transaction semantics are GOOD CASES. If reduction leaves only “use true guarantees”, demote to review/Constitution rule. |

No candidate is REJECT or MERGE_CANDIDATE. P-004’s D-10 and P-012’s D-12 evidence gaps are attached operationalization/scope gaps, not alternative final dispositions.

## 3. D-01..D-14 reconciliation

| D-test | Primary | Pass A | Final result | Stage 6 / eval consequence |
|---|---|---|---|---|
| D-01 P-001 vs P-002 | DISTINCT | DISTINCT | **DISTINCT** | Ownership can fail inside a clean boundary; a single owner can govern a change-amplifying monolith. |
| D-02 P-001 vs P-013 | DISTINCT | DISTINCT | **DISTINCT** | Owner-known stale overwrite caused by absent ordering → P-013; timing-correct orphan timer → P-001. |
| D-03 P-002 vs P-006 | P-006 independent test fails | Property can vary but causal content weak | **P-006 NOT INDEPENDENT AS PRINCIPLE → DEMOTE** | Preserve locality only as metric/property. |
| D-04 P-003 vs P-012 | DISTINCT | DISTINCT | **DISTINCT** | Bounded work without admission policy and admission with unbounded retries are two eval fixtures. |
| D-05 P-004 vs P-009 | DISTINCT | DISTINCT | **DISTINCT** | Shared-resource failure power and authority/trust power independently vary. “Power≤responsibility” may be an upper abstraction, not a merge of mechanisms. |
| D-06 P-010 vs P-001 | DISTINCT | DISTINCT | **DISTINCT** | State authority/conflict semantics are separate from lifecycle/semantic owner. |
| D-07 P-001 vs P-003 | DISTINCT | DISTINCT | **DISTINCT** | Bounded-unowned and owned-unbounded fixtures retained. |
| D-08 safety floor | Conditional | Contextual | **CONTEXTUAL ONLY** | Use “applicable regulatory/safety/security constraints bound trade space”; no universal floor claim. |
| D-09 P-013 vs P-010 | DISTINCT | DISTINCT | **DISTINCT** | Model timing/order guarantee differs from state conflict/authority semantics. |
| D-10 P-004 blast-radius operability | NEEDS_EVIDENCE | NEEDS_EVIDENCE | **NEEDS_EVIDENCE** | Non-blocking measurement/operationalization gap. |
| D-11 P-007 structural discrimination | Upgraded to pass | Conditional narrowing | **NARROW, CLAIM-SCOPED** | Static proof discharges only proved questions under assumptions; other runtime questions still need obtainable evidence. |
| D-12 P-012 non-server shape | Claimed RTOS priority as admission | NEEDS_EVIDENCE | **NEEDS_EVIDENCE** | Priority scheduling is not admission control; require direct RTOS admission evidence before cross-shape promotion. |
| D-13 H7 resurrection | Not resurrected | Not resurrected | **NOT RESURRECTED** | No locality Mother Principle. |
| D-14 P-010 CRDT | Framework holds | Framework holds | **FRAMEWORK HOLDS** | R4 statement survives; multi-writer + explicit merge is compliant. |

## 4. CA5-1..CA5-10 explicit audit

| Finding | Audit result | Exact action |
|---|---|---|
| CA5-1 immutable history | **CONFIRMED / BLOCKING REMEDIATION** | Restore 14 S-001..113 manifest records, five review-queue historical text locations, and two `sources/index.md` historical texts listed in §6. Source files S-001..113 themselves are unchanged. |
| CA5-2 P-003 time bound | **CONFIRMED** | Replace “duration is not a resource dimension” with lifetime-vs-work/wait distinction. |
| CA5-3 P-007 seL4 | **CONFIRMED** | Restrict S-118 to functional-correctness proof under assumptions; do not claim broad substitution for runtime diagnosability. |
| CA5-4 P-012 priority/admission | **CONFIRMED** | D-12 NEEDS_EVIDENCE; remove static priority as proof of admission. |
| CA5-5 P-004 alternatives | **CONFIRMED** | S-122: device/network/disk protection via virtualized I/O + control plane. S-123: selected eBPF program safety at load time. No general substitution claim. |
| CA5-6 D-08 | **CONFIRMED** | Context-bound Constitution input only. |
| CA5-7 P-008 governed break | **CONFIRMED** | Use independent-consumer protection + higher-priority requirement/governed migration exception. |
| CA5-8 P-001 GC | **CONFIRMED** | Exemption only for managed-heap reclamation; no semantic/lifecycle exemption. |
| CA5-9 P-013 discrimination | **CONFIRMED** | Actor mailbox order/event-loop non-preemption/DB transaction semantics are GOOD CASES when model-provided. Preserve TAUTOLOGY_RISK. |
| CA5-10 source quality | **CONFIRMED; ADDITIONAL DEFECTS FOUND** | All S-114..123 have dangling `related_rq: RQ-A/RQ-B/RQ-C`; S-117/S-118/S-121 combine materials without complete provenance; S-119 access status is imprecise; S-114/115 and S-123 overstate claims. Apply §5 matrix. |

## 5. Source admission matrix

### 5.1 Primary S-114..S-123

All ten source files contain `related_rq` values (`RQ-A`, `RQ-B`, `RQ-C`) that do not exist in `review-queue.yaml`. For retained sources, remove those references or replace them with actual RQ5 IDs only where the relationship is real. This is a common metadata fix in addition to row-specific fixes.

| Source | Classification | Provenance/tier/verification audit | Disposition/D-test effect and minimal correction |
|---|---|---|---|
| S-114 Armstrong thesis | **KEEP_WITH_METADATA_FIX** | First-party thesis, Tier A appropriate; PDF reachable. | Useful P-001 supervision evidence. Remove claims that every Erlang process has a superior or runtime forbids ownerless processes; plain `spawn()` exists. Supervision is an OTP pattern for supervised trees. Remove unregistered Akka.NET claim or source it separately. |
| S-115 Erlang Processes | **KEEP_WITH_METADATA_FIX** | Official platform contract; URL/title reachable and precise; Tier A only for Erlang semantics, platform-scoped for general claims. | Material to P-013 GOOD CASE. Correct P-001 use: receiver process semantically owns/consumes mailbox; capacity is unbounded, which is P-003, not ownerlessness. |
| S-116 Go GC Guide | **KEEP_WITH_METADATA_FIX** | Official Go documentation; reachable; platform-normative. | Material to GC dimension. Say GOMEMLIMIT is a soft runtime budget and does not cover all process memory; do not describe managed heap as a hard bound. |
| S-117 SQLite testing | **KEEP_WITH_METADATA_FIX** | URL title is exactly “How SQLite Is Tested”; source title also claims “Atomic Commit” while only `testing.html` is registered (the page merely links `atomiccommit.html`). | Keep SQLite reliability/single-process GOOD CASE. Add exact Atomic Commit URL or remove it from title/claims. Remove D-12 attribution: SQLite testing does not establish overload admission. Do not claim testing alone proves absence of all isolation needs. |
| S-118 seL4 SOSP 2009 | **KEEP_WITH_METADATA_FIX** | Paper reachable, Tier A. Source-file title adds “+ seL4 Verification page” but only the SOSP PDF URL is registered. | Material to D-11/P-007. Register the official page separately as provenance metadata or remove it from title. Restrict claims to functional correctness under explicit compiler/assembly/boot/cache/hardware/spec assumptions; no broad observability replacement. |
| S-119 CRDT | **KEEP_WITH_METADATA_FIX** | Paper identity is appropriate; HAL URL redirects to `inria.hal.science` and currently presents a bot challenge, so `access_status: reachable` is too strong for direct access while `search-cross-verified` is defensible. | Material to D-14/P-010. Update canonical URL/access status; retain claim-relative Tier A. |
| S-120 RFC 7568 | **KEEP_WITH_METADATA_FIX** | Exact Standards Track RFC; URL/title reachable; Tier A claim-relative. | Material P-008 security override. Keep, but phrase as a higher-priority normative security requirement, not generic “security debt”. Common dangling-RQ fix only. |
| S-121 PEP 404 | **KEEP_WITH_METADATA_FIX** | PEP URL/title reachable. Source-file title also claims “What’s New in Python 3.0” without registering that URL. | Supports governed ecosystem migration. Add the second exact URL or remove combined title/material. Do not turn “technical debt” into an unsourced general authorization to break contracts. |
| S-122 Arrakis | **KEEP_WITH_METADATA_FIX** | Exact OSDI paper/landing page, Tier A; title/URL match. | Retain as mechanism-diversity evidence. Limit to hardware-virtualized I/O plus kernel-enforced network/disk protection; change `failure-isolation` wording if it implies generic failure containment. |
| S-123 eBPF verifier | **LEAD_ONLY** | Exact official Linux documentation and reachable, but platform-specific. | It verifies selected BPF program safety properties at load time; it does not materially alter P-004 after CA5-5 correction and cannot support “static verification replaces runtime isolation”. Remove from canonical Stage 5 admission or retain outside the admitted corpus as a tactic/platform lead. |

No retained source is currently `KEEP_CANONICAL` without a metadata correction because every S-114..123 file contains a dangling `related_rq` reference.

### 5.2 Challenger SC-01..SC-09

| Lead | Classification | Reconciliation |
|---|---|---|
| SC-01 seL4 | **DUPLICATE/OVERLAP** | Covered by S-118; Challenger homepage lead adds no disposition-changing claim beyond corrected S-118. |
| SC-02 SQLite architecture | **LEAD_ONLY** | Overlaps S-117’s shape but is a distinct architecture source. Useful for future precision; not required for final Stage 5 disposition. |
| SC-03 PostgreSQL WAL | **LEAD_ONLY** | Useful log-as-authority shape; overlaps existing S-040/S-046/P-010 mechanism and does not change D-14/disposition. |
| SC-04 Linux stable-api-nonsense | **PROMOTION_RECOMMENDED** | Strongest novel source: first-party Linux document directly tests P-008’s single-owner/internal-contract exemption. CA must promote later; Challenger allocates no S-* ID. |
| SC-05 The Old New Thing | **LEAD_ONLY** | Do not reverse Stage 2 CH-S-04 `rejected(secondary)` silently. It may remain a desktop/ABI lead only. |
| SC-06 CRDT | **DUPLICATE/OVERLAP** | Covered by S-119. |
| SC-07 Erlang/OTP docs | **DUPLICATE/OVERLAP** | Covered by S-114/S-115; use corrected platform-scoped claims. |
| SC-08 Sandi Metz | **REJECT_UNVERIFIED** | Both claimed first-party URLs returned 404; archive verification was unavailable. OD5-3 prohibits promotion. No Stage 5 decision depends on it. |
| SC-09 Chromium Site Isolation | **LEAD_ONLY** | Useful desktop/browser containment example but not disposition-critical; no promotion needed in Stage 5. |

## 6. Immutable-history audit and exact repair

### 6.1 `source-manifest.yaml`: all S-001..S-113 checked

Mechanical record comparison found exactly **14** changed accepted records. All other S-001..S-113 manifest records are byte-identical, and all `sources/S-001.md`..`S-113.md` files are unchanged. Restore these fields exactly to baseline `05cfea49`:

| ID | Field | Restore exact baseline value |
|---|---|---|
| S-023 | `verification_note` | `锚定 1e (2017)；2e Early Release 存在但未登记为独立条目，Stage 4 引用 2e 主题前须先建条目（持续风险 R-2）` |
| S-028 | `title` | `Consistency Tradeoffs in Modern Distributed Database System Design (PACELC)` |
| S-029 | `title` | `In Search of an Understandable Consensus Algorithm (Raft)` |
| S-030 | `title` | `Impossibility of Distributed Consensus with One Faulty Process (FLP)` |
| S-036 | `title` | `Highly Available Transactions: Virtues and Limitations` |
| S-038 | `title` | `Life Beyond Distributed Transactions: An Apostate's Opinion` |
| S-050 | `title` | `Amazon Builders' Library` |
| S-053 | `verification_note` | `MIT 镜像反爬 403，内容为学界通行引用版本（Pass B 确认）` |
| S-059 | `title` | `Cloudflare 2019-07-02 outage postmortem (WAF regex)` |
| S-062 | `title` | `SEC Order 34-70694 (Knight Capital 2012-08-01)` |
| S-074 | `title` | `Amdahl 1967 (Validity of the Single Processor Approach)` |
| S-078 | `verification_note` | `DOI 已由错误的 3226569 修正为 3232559（ACM 官方确认，Pass B 终验）` |
| S-112 | `verification_note` | `R3/CH-S-03 admitted；platform-normative，非通用架构真理` |
| S-113 | `verification_note` | `R3/CH-S-08 admitted（FreeRTOS 侧；Zephyr 侧 needs_evidence）` |

Retain the legitimate Stage 5 manifest title/version/stage/root metadata, the S-114..123 ID-range append, and S-114..123 entries subject to §5 corrections. The S-050 Yanacek pointer, if useful, must be new metadata or a new RQ5/source reference; it cannot be inserted into the accepted title.

### 6.2 `review-queue.yaml`: exact pre-RQ5 repair

Retain the Stage 5 title/version/stage and append RQ5-001..005. Restore the following historical text exactly:

1. `remediation_basis` → `Issue #3 CA decision D-B1..D-B3 / R1..R4；Issue #6 CA adjudication R-1..R-11；统计以 source-manifest.yaml 为单一事实源`.
2. Preservation comment → `# RQ2 段为 Stage 2 adjudication 保留原样；Stage 3 仅追加 RQ3 回流项，未修改已有内容`.
3. RQ2-013 / CH-S-01 `note` → `可信候选（官方文档存在），本轮 bounded cycle 未采集；留作 Stage 3+ 单进程形态补源首选` (remove the Stage 5 annotation from the old record; record new coverage in RQ5/new metadata).
4. Stage 3 section marker → `# ============ Stage 3 backflow（追加段，不修改上方 Stage 2 adjudication）============`.
5. RQ3-001 `summary` → `coupling / change-locality 缺专门权威来源：当前 V-014 族仅锚 SAIP 谱系（S-001/S-005/S-023）；H5b/H7 的 Stage 4 检验依赖定向补源（Challenger B-1）。建议候选：Parnas 1975「Software Aspect of Strategic Defense Systems」或 Constantine/Yourdon 结构化设计原始文献，待 Stage 4 定向核验`.

No RQ2-001..RQ2-014 or RQ3-002..RQ3-006 item body otherwise differs from baseline.

### 6.3 `sources/index.md`: additional historical metadata rewrite

The Primary also rewrites two historical index texts not called out in its “history unchanged” claim. Retain `stage: 5` and append the S-114..123 row, but restore:

1. S-112..S-113 range description → `Stage 2 remediation 补源：S-112 Electron（Desktop 正向权威）、S-113 FreeRTOS（Embedded 官方）`.
2. Optional-field rule → `` `access_status` / `canonical_url` / `verification_note` / `evidence_marker` 为 D-B3 批准的可选字段，仅应用于受影响条目。``

This makes the repair deterministic: restore accepted-history text, append Stage 5 material, and do not blend later annotations into old adjudications.

## 7. RQ5-001..RQ5-005 blocker assessment

| RQ | Classification | Assessment / disposition |
|---|---|---|
| RQ5-001 blast-radius measurement | **Non-blocking operationalization gap; Stage 7 metrics backlog** | P-004 can enter reduction with graded, outcome-oriented wording; do not claim a canonical metric. |
| RQ5-002 guarantee-mechanical-checking | **Non-blocking operationalization gap** | P-013 enters reduction only with TAUTOLOGY_RISK and empirical discriminator. Automation quality does not block the semantic candidate. |
| RQ5-003 observability/privacy evidence | **Non-blocking trade-off gap; Stage 7/domain backlog** | Privacy/security is a real design constraint but not needed in P-007’s minimum causal statement. Remove unsupported strength rather than block Stage 6. |
| RQ5-004 naturally bounded load exemption | **Non-blocking scope/operationalization gap** | Phrase applicability positively (“where demand can exceed capacity”) instead of asserting an evidence-heavy universal exemption. D-12 remains NEEDS_EVIDENCE. |
| RQ5-005 SQL label vs actual semantics | **Stage 7 integration/domain-layer backlog** | Useful P-013/P-010 eval/domain note; no Stage 6 blocker. |

**No RQ5 item is a Stage 6 research blocker.** The blocking condition is repository integrity and bounded statement/source remediation, not missing broad research.

## 8. Consolidated GOOD CASE / false-positive set

These are first-class knowledge-boundary and eval inputs, not illustrative footnotes:

1. **P-001:** supervised OTP process tree is explicit ownership; GC exempts managed-heap reclamation only; a process-owned unbounded mailbox is a P-003 bound issue, not ownerlessness.
2. **P-002:** exploration with unknown variation axes; deliberate performance-path permeability; convention-based local change.
3. **P-003:** indefinite daemon/service/stream lifetime with bounded per-work resources; input-bounded offline batch; runtime-governed soft heap budget.
4. **P-004:** SQLite-style single-process economics; Arrakis hardware-backed device/network/disk protection. Do not infer generic isolation substitution.
5. **P-006:** globally coordinated monorepo changes can be broad yet healthy; change spread alone is a signal, not a principle violation.
6. **P-007:** seL4-proved functional properties reduce the corresponding evidence question only; operational phenomena outside assumptions still require runtime evidence.
7. **P-008:** single-owner Linux internal API may break compatibility; RFC 7568 security override and governed ecosystem migration are legitimate explicit breaks.
8. **P-009:** closed single-user/internal coarse trust can be economically correct; external/supply-chain boundaries remain.
9. **P-010:** CRDT multi-writer, append-only log authority and local-first authority distribution are valid when conflict/merge semantics are explicit.
10. **P-012:** gateway/mesh/system-path admission can satisfy the candidate without per-service shedding code; priority scheduling alone does not.
11. **P-013:** documented actor per-pair ordering, non-preemptive event-loop segments and concrete DB transaction semantics are model-provided guarantees and must not be flagged.

## 9. Stage 6 reduction input (not Stage 6 execution)

Stage 6 receives ten surviving candidates: seven NARROW (P-001/002/003/007/008/009/012), three SURVIVES (P-004/P-010/P-013), and P-006 DEMOTE. More precisely:

- **NARROW:** P-001, P-002, P-003, P-007, P-008, P-009, P-012 — use the minimum statements in §2.
- **SURVIVES:** P-004 (graded canonical mechanism, D-10 gap), P-010 (R4 statement confirmed), P-013 (`TAUTOLOGY_RISK`; retain empirical discriminator).
- **DEMOTE:** P-006 to P-002-associated property/review signal.
- **Boundary fixtures:** D-01/02/04/05/06/07/09 remain independent; D-03 demotes P-006; D-08 is contextual; D-11 is question/proof scoped; D-12 remains NEEDS_EVIDENCE; D-13 does not resurrect H7; D-14 confirms P-010.
- **Constitution input only, not a drafted Constitution:** when applicable, mandatory regulatory/safety/security constraints bound the trade space. Do not universalize it.
- **Eval input:** preserve §8 GOOD CASES as false-positive fixtures and pair them with the candidate violation cases.

The synthesis count above is **7 NARROW + 3 SURVIVES + 1 DEMOTE = 11 candidates**. No Stage 6 reduction, Constitution text, ontology, or canonical P-* mutation is performed here.

## 10. Bounded remediation and genuine new owner decisions

### Gate remediation required before Stage 6

1. Apply §6 immutable-history repair exactly; keep append-only Stage 5 material.
2. Correct Primary P-003, P-007, P-012, P-004, P-008, P-001 and P-013 synthesis/dossier wording to match §§1–4 without rerunning research.
3. Apply §5 source metadata/claim fixes, including removal/replacement of every dangling `RQ-A/RQ-B/RQ-C` reference.
4. Preserve the consolidated GOOD CASE set as an explicit Stage 6/eval input.

### Genuinely new owner decisions only

1. **S-123 corpus status:** accept `LEAD_ONLY` removal from canonical admission, or retain it with an explicit platform-tactic scope and no claim that it changes P-004. Recommendation: `LEAD_ONLY` because corrected claims do not change a disposition or D-test.
2. **SC-04 promotion:** authorize later Primary/CA admission of Linux `stable-api-nonsense` as the genuinely novel P-008 single-owner/internal-contract source. Recommendation: promote after exact provenance review; this Challenger report allocates no S-* ID.

Everything else is fixed by OD5-1..OD5-5, CA5-1..CA5-10, or deterministic restore/correction and is not a new owner decision.
