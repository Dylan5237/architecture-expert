---
id: PLAN-STAGE1-CANONICAL
type: research-plan
stage: 1
status: canonical-proposed
owner: chatgpt-chief-architect
date: 2026-09-17
source_submissions:
  - kimi: eval/stage1-kimi@35bc534a36cb7da7eadf47a1b0f9e9634f747725
  - workbuddy-original: eval/stage1-workbuddy@d529d6c537741941c13c1217b8b56f3a424221f2
issue: 1
---

# Stage 1 — Canonical Research Plan

## 0. Purpose and provenance

This is the canonical Stage 1 plan for the Architecture Expert distillation project.

It synthesizes:

- Kimi Stage 1 independent submission;
- WorkBuddy Stage 1 independent submission;
- Chief Architect review and bake-off decisions recorded in Issue #1;
- the original mission in `prompts/KIMI_ARCHITECTURE_DISTILLATION_TASK.md`.

The two agent submissions remain preserved on their evaluation branches as evidence. They are not themselves canonical project state.

Stage 1 defines **how we will research, falsify, structure, evaluate and distill architecture knowledge**. It does not contain a source corpus, final mother principles, or a final system prompt.

Stage 2 may begin only after this plan is accepted into `main`.

---

## 1. Research posture

The project is governed by five meta-rules.

### 1.1 Architecture is a protection mechanism, not an aesthetic form

Research asks:

- what system property is being protected;
- under which constraints;
- through which mechanism;
- against which failure mode;
- at what cost.

Patterns, frameworks and technologies are not principles by default.

### 1.2 Hypotheses must be falsifiable

Candidate principles are hypotheses until they survive:

- source triangulation;
- counterexample search;
- cross-system-shape testing;
- adversarial evaluation;
- independent challenge.

The goal is not to prove the original six candidate principles correct.

### 1.3 Context > Pattern

Any statement of the form `X is better than Y` is presumed `CONTEXT_DEPENDENT` until applicability, mechanism, trade-offs and counterexamples are explicit.

### 1.4 Evidence strength and confidence must remain separate from prose fluency

Use explicit epistemic states:

- `CONFIRMED`
- `HIGH-CONFIDENCE_RISK`
- `HYPOTHESIS`
- `NON-BLOCKING_IMPROVEMENT`
- `PERSONAL_PREFERENCE`
- `UNKNOWN`
- `CONTESTED`
- `CONTEXT_DEPENDENT`
- `NEEDS_EVIDENCE`

A weak claim may remain useful, but it must not be promoted by confident wording.

### 1.5 Implementation inconvenience must not silently redefine product intent

`Implementation constraints must not silently redefine the product contract.`

When required properties genuinely conflict with physical, cost, legal, security, compatibility or organizational constraints, the Architecture Expert must expose an explicit trade-off or `ARCH_CONFLICT` rather than quietly deleting capability.

---

## 2. Research questions

`RQ-0` is the mother question. The grouped RQs below are traceability anchors, not a closed list.

### RQ-0 — What makes an architecture good?

- Can architecture quality be reduced to a compact set of cross-stack mother principles?
- Which candidate principles are independent, which are projections of the same deeper mechanism, and which are merely heuristics?
- Are there architecture qualities that are non-negotiable independently of stated product intent, such as safety/security floors in some contexts?
- Can the resulting principles discriminate between good and bad architecture rather than explain every outcome post hoc?

A principle set fails if important real failures cannot be explained **or** if the principles are so elastic that almost any outcome can be rationalized after the fact.

### RQ-A — Definition and protected properties

1. What is a software architecture problem, and what is not?
2. Can one architecture definition remain meaningful across Desktop, Web Frontend, Mobile, Backend, Monolith, Distributed Systems, DB-heavy systems, Developer Tools, Local AI Tools, Cloud Platforms, Embedded/Edge systems and AI Agent Runtime?
3. What does architecture protect: capability, correctness, security, latency, availability, compatibility, operability, evolvability, cost, or other properties?
4. How do architecture concerns relate to quality attributes, system constraints and product contracts?
5. What is the minimum sufficient architecture description for human and AI reasoning?

### RQ-B — Mother principles and mechanisms

1. Are Boundaries and Ownership one principle or distinct mechanisms?
2. Can Bounded Execution explain queues, retries, scans, fan-out, concurrency, retained state and resource exhaustion under one deeper rule?
3. Does `A subsystem should not have more failure power than its responsibility requires` survive low-cost/single-process counterexamples, or is it a graded heuristic?
4. Is Evolvability a mother principle, or a composite of Reversibility, Change Locality and Compatibility?
5. Is Locality one principle with change/data/failure projections, or several unrelated mechanisms?
6. Is Controlled Complexity a principle, a meta-objective, or a consequence of other principles?
7. Is explicit trust/security a separate mother principle or a protected property handled by other structural principles?
8. What, if anything, is missing from the current candidate set?

### RQ-C — Architecture reasoning

1. What is the smallest useful set of system models for architecture reasoning?
2. Which models are always relevant and which are conditional?
3. What reasoning order works across system shapes without becoming a rigid checklist?
4. How should the expert decide when evidence is sufficient to conclude versus when to ask for more evidence?
5. How should it distinguish static code evidence, runtime evidence, product intent, architecture intent and historical rationale?
6. How should it choose among multiple viable designs without substituting personal taste for architecture reasoning?
7. How should it identify the minimum necessary correction instead of defaulting to rewrite or generalized frameworks?

### RQ-D — Knowledge engineering and agent consumption

1. What routing/index structure yields the minimum sufficient context for each task?
2. What knowledge unit granularity best balances retrieval precision, reasoning completeness and token cost?
3. What relationship predicates are actually useful for navigation and reasoning?
4. Which knowledge belongs in Principles, Failure Patterns, Tactics, Decision Playbooks, Question Bank and Sources?
5. How should knowledge status, freshness, contradiction and supersession be represented?
6. Which corpus organization performs best under real agent consumption tests rather than document aesthetics?

### RQ-E — Evaluation and proof of distillation quality

1. How do we distinguish genuine mechanism reasoning from keyword/checklist matching?
2. How do we measure false positives and over-engineering, not only defect recall?
3. How do we evaluate architecture **design and trade-off selection**, not only architecture review?
4. How do we blind the evaluated agent from expected findings?
5. How do we avoid circular evaluation where the knowledge author also defines all answers?
6. What evidence is sufficient to promote a candidate principle to stable status?

---

## 3. Knowledge domain coverage

The 18 domains from the mission are **mandatory minimum coverage, not a closed ontology**. Research may add, split or merge domains if evidence reveals a better decomposition. Top-level ontology changes must be explicit and reviewed before becoming canonical.

Minimum coverage:

1. Software Architecture Fundamentals
2. Architecture Quality Attributes
3. Runtime / Execution Architecture
4. Concurrency
5. Performance Engineering
6. Runtime / Resource Budgets
7. Failure Model
8. Failure Isolation
9. Distributed Systems
10. State / Storage / Data Architecture
11. API / Integration Architecture
12. Lifecycle / Ownership
13. Security Architecture
14. Observability / Operability
15. Scalability
16. Evolvability
17. Architecture Decision Making
18. Architecture Communication

For research execution, these may be grouped into overlapping clusters to reduce duplicate source work:

- Structure / Boundaries
- Runtime / Concurrency
- Resources / Performance / Scalability
- Failure / Isolation / Distributed Failure
- State / Data
- Lifecycle / Ownership
- Integration / Contracts
- Security / Trust
- Observability / Operability
- Evolution / Decisions / Communication
- Agent Runtime / Harness as a cross-cutting system shape

`Lifecycle / Ownership` is a high-priority research area because ownership ambiguity, cancellation, stale work, resource cleanup and failure domains recur across runtime, concurrency and reliability problems. This priority is empirical, not a declaration that it must become a mother principle.

Agent Runtime is not yet a permanent first-level domain. It is a mandatory cross-cutting system shape used to test whether general principles survive newer long-running AI workloads.

---

## 4. Candidate source map

Stage 1 records candidate families only. Stage 2 establishes exact provenance, versions, URLs and evidence notes.

### 4.1 Architecture fundamentals / quality attributes

Priority candidates include:

- David Parnas — information hiding / modular decomposition
- Fred Brooks — essential vs accidental complexity, conceptual integrity
- Bass / Clements / Kazman — Software Architecture in Practice
- SEI — ATAM and quality-attribute methods
- ISO/IEC/IEEE 42010 — architecture description and concerns
- ISO/IEC 25010 — product/system quality model
- Shaw & Garlan
- Martin Fowler — selected architecture and evolution essays
- Eric Evans — bounded contexts where relevant
- Robert C. Martin — treated as an opinionated source, never normative by default

### 4.2 Systems / distributed / state

- Martin Kleppmann / DDIA
- Leslie Lamport
- Gilbert & Lynch CAP formalization
- Brewer CAP retrospective
- Abadi PACELC
- Raft
- FLP where relevant
- transaction / isolation / MVCC primary literature and official DB documentation

### 4.3 Reliability / failure / operations

- Michael Nygard / Release It!
- Google SRE Book / Workbook
- AWS Builder's Library
- AWS / Azure / GCP Well-Architected as industrial practice sets, not universal theory
- production postmortems from mature engineering organizations

### 4.4 Performance / concurrency

- Brendan Gregg / Systems Performance
- Little's Law primary/authoritative material
- Amdahl's Law primary material
- Dean & Barroso / Tail at Scale
- CSP / actor model primary literature
- structured concurrency sources and official runtime/language documentation
- Universal Scalability Law only if source quality and applicability survive review

### 4.5 Security / trust

- Saltzer & Schroeder
- NIST architecture-relevant publications
- OWASP architecture-relevant material
- threat modeling sources where useful

### 4.6 Agent engineering / consumption

- GitHub Spec Kit
- Kiro official documentation
- Anthropic official agent/harness/context-engineering material
- OpenAI official agent/harness engineering material

Vendor agent material is treated as engineering evidence with explicit vendor-bias risk, not universal architecture truth.

### 4.7 Case / held-out evidence

Public incident reports are important for failure mechanisms and evaluation, but they must not become the sole source for mother principles.

Candidate held-out families include:

- retry amplification / dependency failure incidents;
- deployment and migration incidents;
- regex/runtime blocking incidents;
- BGP/network control-plane incidents;
- update/rollout validation incidents;
- storage or consistency incidents.

Exact cases used for blind evaluation must not be embedded into the tested knowledge path in a way that leaks expected answers.

---

## 5. Source acquisition and evidence discipline

### 5.1 Authority order

Prefer:

1. standards, RFCs, primary papers, official documentation, original authors;
2. authoritative books and long-lived engineering organizations;
3. mature engineering case studies and postmortems;
4. secondary explanatory material only when needed for understanding.

SEO farms, AI aggregation and low-provenance summaries do not support core claims.

Language is **not** an authority criterion. Chinese sources may enter the evidence chain if they meet the same provenance and quality bar.

### 5.2 Promotion rule

A Mother Principle candidate should normally require either:

- at least two independent high-quality source families; or
- one strong primary/theoretical source plus strong independent empirical evidence.

Single-source claims remain `candidate`, `heuristic`, `CONTESTED` or `CONTEXT_DEPENDENT` as appropriate.

### 5.3 Contradictions

Do not force consensus.

When authoritative sources disagree:

- record both;
- identify hidden assumptions and context differences;
- mark `CONTESTED` where unresolved;
- send the item to `review-queue.yaml`;
- let Stage 5 falsification and later eval determine whether the disagreement can be reduced.

### 5.4 Copyright / paid books

Paid books may be used if legitimately accessible to the researcher. Store:

- provenance;
- chapter/page/location pointers where possible;
- paraphrased claims;
- short necessary quotations only.

If the executing agent cannot access the book text, it must not imply otherwise.

### 5.5 Breadth and stopping

Source-count ranges are guardrails, not success metrics.

The stopping rule is evidence sufficiency per research question and domain, not document volume. Where strong evidence is scarce, use `NEEDS_EVIDENCE` instead of lowering standards.

---

## 6. Candidate first-principles hypotheses

The following are research hypotheses, not conclusions.

### H1 — Purpose / Required-Property Fitness

Architecture quality is relative to required system properties and real constraints, subject to any justified non-negotiable floors such as safety/security in applicable contexts.

### H2a — Explicit Boundaries

Boundaries and dependency direction reduce the propagation of change, reasoning burden or failure only when they correspond to meaningful responsibilities and interfaces.

### H2b — Explicit Ownership

Runtime entities and mutable state require sufficiently explicit ownership, lifecycle and mutation authority to avoid orphaning, stale work and ambiguous responsibility.

### H3 — Bounded & Predictable Execution

Important work should have credible bounds or controlled degradation across time, space, concurrency, queues, retries, fan-out and retained state, according to the criticality of the path.

### H4 — Failure Containment

Failure power and blast radius should not exceed what the subsystem's responsibility and economics justify.

### H5a — Reversibility

Decision reversibility should influence the amount of analysis, migration planning and commitment required.

### H5b — Change Locality

Good structure tends to localize likely changes and prevent change amplification.

### H6 — Legibility / Operability / Verifiability

A system that cannot reveal enough of its behavior to distinguish normal from abnormal cannot be operated or validated reliably at the required level.

### H7 — Locality

Reasoning, data movement, failure propagation and change cost often increase with distance across boundaries; whether these are one principle or multiple projections must be tested.

### H8 — Compatibility / Contract Preservation

Compatibility and product-contract preservation may be first-class architectural properties rather than merely subsets of evolvability.

### H9 — Controlled Complexity

The objective is the minimum complexity necessary to safely protect required system properties, not minimum complexity in the abstract.

### H10 — Trust Minimization

Trust boundaries and privilege should be no broader than required by responsibility and system constraints.

### H11 — Authoritative State / Source of Truth

State should have clear authority and consistency semantics; whether this is independent from ownership remains an open question.

Additional hypotheses may be introduced by evidence. None of the above has protected status.

---

## 7. Falsification and reduction protocol

Each candidate principle passes through:

`Extract -> Normalize -> Compare -> Falsify -> Reduce -> Operationalize`

For each candidate:

- identify at least one serious counterexample search;
- test at least two substantially different system shapes where relevant;
- record failure cases it explains;
- record cases it must **not** classify as violations;
- distinguish mechanism from tactic;
- identify trade-offs and applicability boundaries;
- link evidence classes and source IDs;
- preregister expected discriminators before adversarial evaluation where practical.

A principle should remain separate from another only if there are credible cases where one is violated and the other is not, or where they protect materially different properties through different mechanisms.

Independent challenge is required for ambiguous principle-to-case mappings to reduce post-hoc elasticity.

The final Constitution has a hard guardrail of `<=20` mother principles. There is **no target number to hit**. Compression is driven by explanatory power, discrimination and eval performance, not aesthetics.

---

## 8. Knowledge architecture

### 8.1 Stable invariants

The following are accepted architecture invariants for the knowledge system:

- GitHub repository is the durable source of truth;
- stable IDs for durable knowledge entities;
- explicit provenance;
- uncertainty and contradiction are first-class states;
- Principles, Failure Patterns and Tactics are distinct types;
- System Prompt must not duplicate the knowledge corpus;
- Progressive Disclosure is required;
- accepted knowledge is versioned, superseded or deprecated rather than silently rewritten;
- relationship navigation must be machine-readable enough for agents/tools to follow.

### 8.2 Parameters that remain hypotheses

The following must **not** be treated as fixed truths before consumption testing:

- exact number of disclosure layers;
- router/index line limits;
- file-size thresholds;
- exact directory decomposition;
- exact relationship predicate set;
- exact token/file count targets;
- exact number of Failure Patterns / Tactics / Questions.

These may begin with sensible operational guardrails, then be changed based on measured agent consumption quality.

### 8.3 Initial shape

The mission's repository layout remains the default starting hypothesis:

- `00_ROUTER.md`
- `01_CONSTITUTION.md`
- `02_VOCABULARY.md`
- `source-manifest.yaml`
- `relationship-map.yaml`
- `review-queue.yaml`
- `principles/`
- `domains/`
- `failure-patterns/`
- `tactics/`
- `decision-playbooks/`
- `question-bank/`
- `cases/`
- `sources/`
- `agent/`
- `eval/`
- `reports/`

Top-level ontology changes after Stage 2 must be proposed explicitly with migration impact and approved by the Chief Architect before becoming canonical.

---

## 9. Evaluation strategy

Evaluation must test both **review** and **design** capability.

### 9.1 Scenario families

The corpus should include at least the 25 failure classes in the mission, plus enough good cases to measure precision.

Target mix should cover:

- defect/review scenarios;
- architecture design with multiple viable alternatives;
- trade-off selection;
- evolution/migration decisions;
- incident architecture analysis;
- ambiguous evidence / insufficient evidence cases;
- good architecture cases containing superficially suspicious patterns.

GOOD CASES should be materially represented; 30% is a useful initial guardrail, not a permanent target.

### 9.2 Anti-pattern-matching probes

Include:

- inverted-pattern scenarios: looks dangerous, mechanism is safe;
- novel recombination scenarios: familiar pattern name is misleading, mechanism reveals the issue;
- cross-component failures where local code looks correct;
- cases where the right answer is `NEEDS_EVIDENCE` rather than a verdict.

### 9.3 Blindness

The agent under test must not have access to its scenario's expected findings.

R2/R3 and a sample of R1 must be executed or independently adjudicated by a non-author agent.

Every run records at least:

- model/provider;
- prompt/system revision;
- knowledge repository SHA;
- scenario version;
- judge identity;
- task mode.

### 9.4 Metrics

Track at least:

- issue-detection recall;
- precision / false positives;
- mechanism quality;
- evidence quality;
- trade-off quality;
- scope discipline;
- product preservation;
- uncertainty handling;
- minimum-correction quality;
- architecture-design quality;
- consumption cost / context efficiency.

Any initial numeric thresholds are provisional until baseline runs establish realistic distributions. Fabricated evidence and silent product-contract reduction remain hard failures.

### 9.5 Repair discipline

When eval fails, repair in this order:

`Knowledge -> Principles -> Question Bank -> Reasoning Model -> Prompt`

Do not paper over a knowledge or reasoning defect by continuously enlarging the system prompt.

---

## 10. Research orchestration model

This project adapts governance ideas from `agent-project-ops` without copying implementation-phase mechanics.

The research-native loop is:

`Question / Hypothesis -> Dispatch independent research -> Evidence capture -> Contradiction / gap analysis -> Synthesis proposal -> Adversarial challenge -> Architect gate -> Promote / revise / keep contested`

### Roles

**Kimi Research Mode / K3 cluster — Primary Researcher**

Primary responsibilities:

- broad source discovery;
- source triangulation;
- literature mapping;
- initial evidence extraction;
- candidate synthesis.

**WorkBuddy Research Mode / GLM 5.3 — Independent Challenger**

Primary responsibilities:

- challenge source coverage and authority;
- search for counterexamples;
- identify hidden assumptions and contradictions;
- independently test candidate synthesis;
- review ambiguous claims.

**Cursor — Repository Engineering Worker**

Use when the work becomes deterministic enough for:

- schema/index generation;
- relationship-map tooling;
- consistency checks;
- eval harness / scripts;
- batch repository transformations.

Cursor does not own research truth or principle promotion.

**ChatGPT Chief Architect — Disposer / Synthesizer / Gatekeeper**

Responsibilities:

- task decomposition and dispatch;
- compare actual repository artifacts;
- adjudicate evidence conflicts;
- decide promotion state;
- synthesize canonical plans, principles and agent core;
- maintain research scope discipline;
- escalate only genuine human-owner decisions.

**Human Owner**

Needed for:

- product/scope trade-offs;
- external commitments;
- material budget decisions when required;
- irreversible ontology/product decisions;
- disputes that cannot be resolved by evidence.

Chat is not project state. All durable outcomes must land in GitHub.

---

## 11. Distillation stages and gates

### Stage 1 — Research Plan

Output: this file.

Gate: accepted canonical plan in `main`.

### Stage 2 — Source Collection

Outputs:

- `source-manifest.yaml`
- `sources/S-*.md`
- source-gap / conflict entries in `review-queue.yaml`

Gate:

- minimum credible source coverage for every mandatory domain/cluster;
- source provenance present;
- known weak/contested areas explicit;
- no pressure to reach arbitrary source counts.

### Stage 3 — Vocabulary Normalization

Output: `02_VOCABULARY.md`.

Gate: material cross-source term collisions are explicit and no important term silently carries multiple incompatible meanings.

### Stage 4 — Principle Extraction

Output: candidate `P-*` files.

Gate: each candidate has mechanism, protects, applicability, trade-offs, counterexample plan and source links.

### Stage 5 — Contradiction / Counterexample Review

Outputs: falsification notes + contested queue.

Gate: every candidate has serious counterexample work; independent challenger has reviewed high-impact candidates.

### Stage 6 — First-Principles Reduction

Outputs: Constitution draft + reduction record.

Gate: `<=20` principles, with merge/split rationale and evidence status; no unsupported universalization.

### Stage 7 — Knowledge Architecture

Outputs: domains, failure patterns, tactics, relationship map and indexes.

Gate: traceability and navigation work; ontology remains agent-consumable.

A small consumption smoke test may be inserted before Stage 8 if it can cheaply reveal structural problems.

### Stage 8 — Reasoning Model

Outputs: decision playbooks and question bank.

Gate: modes have triggers, stopping conditions, evidence expectations and escalation rules.

### Stage 9 — Agent v0.1

Outputs: core system prompt + mode files.

Gate: prompt contains role/constitution/workflow/navigation/evidence/decision/escalation/output behavior, not duplicated corpus knowledge.

### Stage 10 — Evaluation

Outputs: blinded eval runs, metadata and results.

Gate: review + design + good-case coverage complete enough to diagnose recall, precision, over-engineering and reasoning quality.

### Stage 11 — Repair

Outputs: knowledge/reasoning repairs with before/after evidence.

Gate: defects are repaired at the correct layer rather than prompt-patched.

### Stage 12 — Agent v1.0

Output: release candidate Architecture Expert.

Gate: adversarial eval satisfies agreed quality bar with no hard-failure violations.

### Stage 13 — Distillation Report

Outputs:

- `reports/SOURCE_MAP.md`
- `reports/DISTILLATION_REPORT.md`
- `reports/PRINCIPLE_COVERAGE.md`
- `reports/OPEN_QUESTIONS.md`

Gate: final claims, unresolved issues and evidence lineage are explicit.

---

## 12. Resolved Stage 1 decisions

These decisions are canonical unless later evidence justifies reopening them.

1. **Sparse domains:** do not lower evidence standards for Embedded/Edge, Local AI Tool or other underrepresented shapes. Use `NEEDS_EVIDENCE` where necessary.
2. **Paid books:** allowed when legitimately accessible; store provenance and paraphrase, not substantial copyrighted text.
3. **Evaluation:** mixed, blinded, with independent challenge. R2/R3 require non-author participation; self-eval is never sufficient for promotion.
4. **Language:** explanatory prose may be Chinese; stable IDs, enums, frontmatter keys and precision-sensitive architecture terms may remain English. Do not duplicate the corpus bilingually by default.
5. **Top-level ontology:** agents may propose changes, but ontology-level changes require explicit architecture review before canonical adoption.
6. **Knowledge host:** this GitHub repository remains the durable source of truth and primary consumption form.
7. **Mother-principle count:** `<=20` is a guardrail, not a target. Final number is evidence/eval-driven.
8. **Agent Runtime:** mandatory cross-cutting coverage, not automatically a permanent first-level domain.
9. **Stack annexes:** stack-specific material such as Electron/FS may exist as annex/domain examples, never as the universal core.
10. **Review queue:** Chief Architect handles routine adjudication; human owner is engaged for genuine authority/scope/irreversibility decisions.
11. **Source language:** authority is determined by provenance and quality, not English vs Chinese.
12. **Knowledge parameters:** file/token/line/count limits are operational hypotheses and guardrails until consumption tests validate them.

---

## 13. Stage 2 entry contract

Once this plan is merged, Stage 2 begins with the following orchestration:

### Primary track — Kimi K3

Build the initial source map and manifest across the mandatory domain coverage. Focus on authoritative sources, provenance, domain gaps and claims that directly answer the registered RQs.

### Challenger track — WorkBuddy GLM 5.3

Independently review:

- missing source families;
- authority misclassification;
- overrepresentation of backend/distributed/cloud material;
- weak or circular evidence;
- candidate counterevidence;
- version/freshness problems.

WorkBuddy should not merely rewrite Kimi's notes. It should generate independent challenge artifacts.

### Chief Architect gate

The Chief Architect compares repository evidence, resolves source-status disagreements where possible, and keeps unresolved matters explicitly contested.

### Stage 2 stop condition

Stage 2 stops when the mandatory coverage is sufficiently evidenced to support vocabulary normalization and principle extraction—not when a predetermined document count is reached.

No agent proceeds to Stage 3 without the Stage 2 gate.
