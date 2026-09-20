---
id: IDX-QUESTION-BANK
type: question-bank
stage: 8
status: CANONICAL
issue: 21
---
# question-bank/

Conditional, mechanism-oriented questions. Not interview trivia. Not framework preference. Not a mandatory list.

**How to use:** a playbook activates **sections**. Ask a question only when its **Activate** matches. Stop when an answer cannot change the decision. Playbooks must reference IDs here; do not copy question text into DP files.

Section IDs (`Q-INT`, `Q-EVD`, …) are the units DPs name. Item IDs (`Q-001`…) are stable.

---

## Q-INT Intent / Product Contract

### Q-001 What property must remain true if this task succeeds?
Activate: always at start. Routes: AX-001; V-004-C.

### Q-002 What product capability would be dropped if we take the convenient implementation path?
Activate: design, change, or ADR; whenever cost/difficulty is offered as justification. Routes: AX-002.

### Q-003 Who is the independent consumer of this behavior, if any?
Activate: API/event/storage shape, migration, “internal only” claims. Routes: `integration/` MP-007 GC-011.

---

## Q-EVD Evidence / Current Baseline

### Q-004 What is currently true in code/config/tests/runtime, as opposed to what is asserted?
Activate: any project-specific claim about current behavior. Precedence: CODE/CONFIG/TEST/RUNTIME > GENERIC_KNOWLEDGE > USER_ASSERTION.

### Q-005 What was intended (product or ADR), and does it disagree with current behavior?
Activate: when both intent and current system exist. If they disagree → `KNOWLEDGE_DRIFT`.

### Q-006 What single observation would distinguish the remaining candidate mechanisms?
Activate: two or more FPs/mechanisms still fit. Prefer this over a BLOCKER. Routes: MP-006 T-014.

### Q-007 Which claims are USER_ASSERTION still in `HYPOTHESIS`?
Activate: incident notes, review interviews, “everyone knows”. Do not promote to CONFIRMED without origin upgrade.

---

## Q-PRP Required Properties / Constraints

### Q-008 Which constraints are real (capacity, latency, regulation, team, deploy shape) versus preferred?
Activate: after Q-001. Routes: V-004-D; AX-003 only if a named non-negotiable applies (D-08: not a universal safety floor).

### Q-009 What is explicitly out of scope for this pass?
Activate: always once properties are named. Prevents DP-005 from becoming a full-system tour.

### Q-010 If two properties conflict, is that fundamental or inconvenience?
Activate: when a proposed structure cannot keep both. Routes: `ARCH_CONFLICT` fields; AX-002.

---

## Q-OWN Boundaries / Ownership

### Q-011 Who owns create, mutate, cancel, and cleanup for each runtime entity and each mutable state?
Activate: concurrency, async, tasks, resources needing cleanup. Routes: `lifecycle/` MP-001 FP-001 T-001 T-002 GC-001 GC-002.

### Q-012 Is indefinite lifetime being confused with missing ownership or missing per-work bounds?
Activate: daemons/streams called “unbounded”. Routes: GC-001 GC-004; D-07 (cancel vs bounds).

### Q-013 For a stale/late completion, is the gap missing cleanup ownership or an assumed execution-model guarantee?
Activate: stale async, double apply, cancelled work that still mutates. Routes: D-02; FP-001 **and** FP-012; do not invent a third FP. GC-016.

### Q-014 Is “authority” here lifecycle ownership, write/state authority, authorization, or authority tier?
Activate: the word authority/owner without qualifier. Routes: V-003-D; D-06 MP-001 ≠ MP-008.

---

## Q-XCN Execution / Concurrency

### Q-015 Which ordering, cancellation, clock, or isolation behavior is assumed, and which does the execution model actually provide?
Activate: async, actors, event loops, DBMS isolation *names*, “it shouldn’t race”. Routes: `concurrency/` MP-010 FP-012 GC-016. ANSI isolation names are not GC-016 (RQ5-005).

### Q-016 What happens if a dependency never returns, returns twice, or returns after cancel?
Activate: remote calls, workers, retries, cancellation tokens. Routes: T-002 T-003; D-07 vs MP-003 bounds.

### Q-017 Is the unit of concurrency a model-provided primitive or an application timing hope?
Activate: thread/timer/sleep protocols, “soon”, “usually ordered”. Routes: FP-012; GC-016.

---

## Q-STA State / Authority / Conflict

### Q-018 Who may write, and what is the conflict/merge rule when two writes exist?
Activate: shared mutable state, multi-writer, sync. Routes: `state-data/` MP-008 FP-009 T-013 GC-013 GC-014. D-14: not a single-writer principle.

### Q-019 Which V-010 sense of “consistency” is meant?
Activate: any unqualified “consistency”. Refuse to diagnose until suffixed.

### Q-020 Is an append-only log or derived read model being flagged as “no conflict rule”?
Activate: event logs, CQRS-style read models. Routes: GC-014. Do not require a writer lock for a defined append/derive semantics.

---

## Q-FLW Data / Control Flow

### Q-021 Which data flows are in-band with control, and which can arrive late, duplicate, or reordered?
Activate: messaging, async APIs, dual writes. Routes: Q-XCN and Q-STA as needed; T-015 if duplicates must not double-apply.

### Q-022 Where does a request/work item exit the system, and who still holds a continuation?
Activate: callbacks, sagas, workflow engines, human tasks. Routes: MP-001 T-002.

---

## Q-RES Resources / Per-Work Bounds

### Q-023 Which per-work dimensions (time, wait, retry count, queue, concurrency, memory, fan-out) can grow without an effective bound or governed policy?
Activate: shared resources, external input, async work, cross-boundary calls. Routes: `resources/` MP-003 FP-003 T-003 T-004 T-005 GC-002 GC-004.

### Q-024 Is lifetime being treated as a per-work bound?
Activate: “it runs forever so it is unbounded”. Routes: GC-004; MP-003 statement: lifetime may be indefinite.

### Q-025 Is this a missing *bound* (MP-003) or missing *overload policy* (MP-009)?
Activate: saturation, timeouts, retries. Routes: D-04; do not merge `resources/` and `overload/`.

---

## Q-OVL Overload Path

### Q-026 Where is the governed decision to admit, continue, refuse, or reduce work under saturation?
Activate: overload, brownout, retry storm, “just scale”. Routes: `overload/` MP-009 FP-010 T-006 T-008 T-009 GC-015.

### Q-027 Which of admission, backpressure, shedding, degradation, and flow control is actually present? Do not alias them.
Activate: any overload control claim. Routes: T-006 T-007 T-008 T-009; V-008; flow control ≠ backpressure.

### Q-028 Is retry the bound, the amplifier, or both?
Activate: retries on timeouts/errors. Routes: FP-011 T-005; DISTINCT_FROM T-015 (retry ≠ idempotency).

### Q-029 Is missing *service-local* shedding being flagged when a path-level/gateway bound already exists?
Activate: “service has no load-shedding code”. Routes: GC-015.

---

## Q-FAL Failure / Propagation / Recovery

### Q-030 What is the failure domain (structural partition) versus the blast radius (outcome)?
Activate: isolation, cascade, “radius” talk. Routes: `reliability/` MP-004; RQ5-001 stays a gap — do not invent a universal metric.

### Q-031 Along which shared resources can this fault propagate, and is a coupled defense amplifying it?
Activate: cascade, retry-on-isolate, shared thread/connection/disk. Routes: FP-004 FP-005 T-010 GC-005 GC-006.

### Q-032 Is process isolation being required where the cost model does not justify it, or a dimension-specific mechanism already contains the fault?
Activate: “must be a process/container”. Routes: GC-005 GC-006; Constitution non-prescription of process boundaries.

### Q-033 Is trust minimization being substituted for failure containment, or the reverse?
Activate: “isolate it” vs “least privilege”. Routes: D-05; MP-004 RELATED_TO MP-005 is navigation, not parent.

---

## Q-TRS Trust / Security

### Q-034 Which trust boundaries are actually present (untrusted input, cross-privilege, external integration, agent action)?
Activate: authz, multi-tenant, tools/agents, supply chain. Routes: `security/` MP-005 FP-006 T-011 GC-012.

### Q-035 Is fine-grained internal zero-trust being required in a genuinely closed/coarse-trust context?
Activate: single-user/same-team deploy with no relevant untrusted boundary. Routes: GC-012; supply-chain/external boundaries remain in scope when present.

### Q-036 What can an agent/tool actually do, and is that privilege excess at a real boundary?
Activate: LLM tools, automation, workflow bots. Routes: FP-006 T-011; RQ2-008 / RQ3-004 remain gaps — do not fill by invention.

---

## Q-OBS Observability / Diagnostic Evidence

### Q-037 Which runtime states must be distinguishable to attribute this failure or to operate this path, and is that evidence captured or derivable?
Activate: attribution, SLO debate, “we cannot tell”. Routes: `observability/` MP-006 FP-007 T-014.

### Q-038 Is a missing telemetry product being treated as FP-007?
Activate: “no OTel / no dashboard”. FP-007 is distinguishing evidence for a *question that matters*, not a stack mandate.

### Q-039 Does a proof or assumption-set already discharge this question, and which questions remain outside that scope?
Activate: formal verification, DO-178-class, “we proved it”. Routes: GC-008; D-11.

---

## Q-INTG Integration / Compatibility

### Q-040 Who are the independent consumers, and in which compatibility direction must this change move?
Activate: API/event/schema/storage change. Routes: `integration/` MP-007 FP-008 T-012.

### Q-041 Is this break governed by an explicit higher-priority security/correctness requirement or coordinated migration, rather than an ungoverned contract break?
Activate: any compatibility break. Routes: GC-009 GC-010.

### Q-042 Is internal interface churn being treated as an independent-consumer violation?
Activate: tightly coordinated internals vs stable external contract. Routes: GC-011.

---

## Q-EVL Evolution / Change

### Q-043 Is there an identifiable variation axis, or is this still exploration?
Activate: module-split debates, “we need boundaries”. Routes: `evolution/` MP-002 FP-002 GC-003.

### Q-044 Is change spread being treated as a principle violation rather than a review signal?
Activate: large diffs, coordinated migrations. Routes: P-006; GC-007; D-03. Not an FP.

### Q-045 Do the two sides of this boundary actually have different change rules?
Activate: proposed module/service split. Routes: MP-002; D-01 vs ownership (MP-001).

---

## Q-ALT Alternatives / Minimum Correction

### Q-046 What is the smallest boundary, owner, bound, contract, or evidence change that breaks the named mechanism?
Activate: after a mechanism is identified (review/change/incident). Minimum-correction rule.

### Q-047 Which rejected alternatives still protect the required properties?
Activate: design and ADR; also when a rewrite is proposed. Routes: AX-004.

### Q-048 What would invalidate the chosen alternative?
Activate: ADR/design close. If nothing could invalidate it, it is dogma, not a decision.

### Q-049 Is a wider redesign required because the local fix cannot protect the property, or only because a rewrite is preferred?
Activate: any rewrite/platform proposal. Prefer local fix unless it fails Q-046.

---

## Q-VAL Validation / Proof

### Q-050 What evidence would confirm the property is protected after this design/change/fix?
Activate: before calling a proposal done. May be TEST, RUNTIME, or a proof with explicit assumptions (GC-008).

### Q-051 Is an isolation/consistency *name* being used as if it were a provided guarantee?
Activate: “serializable”, “linearizable”, “exactly once” without model evidence. Routes: MP-010; RQ5-005; T-015 for duplicate-effect, not as a delivery-semantics MP.

---

## Q-UNK Unknowns / Escalation

### Q-052 What is unknown, and is it decision-changing?
Activate: before continuing analysis. If not decision-changing, stop (stop rule 6).

### Q-053 Who has authority to pick among remaining viable alternatives or to drop a required capability?
Activate: multiple viable options, or AX-002 conflict. Escalation list in `decision-playbooks/index.md`.

### Q-054 Is this `NEEDS_EVIDENCE` with a named next observation, or an invitation to keep speculating?
Activate: temptation to BLOCKER without evidence+mechanism+failure mode+impact.

### Q-055 Does this require an `ARCH_CONFLICT` record rather than a silent shrink of the product contract?
Activate: “we can’t do that requirement”. Fill all ARCH_CONFLICT fields; inconvenience alone is invalid.
