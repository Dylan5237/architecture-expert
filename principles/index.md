---
id: IDX-PRINCIPLES
title: principles/ index
stage: 7
status: CANONICAL-INDEX
updated: 2026-09-20
---
# principles/ 索引

本目录同时存放 **Stage 7 规范 Mother Principles** 与 **Stage 4 历史候选**。两类不可混读。

## Canonical Mother Principles（MP-001..MP-010）

权威语义在 `01_CONSTITUTION.md`。下列原子页只作导航与 operationalization 链接，不得改写因果主张。

| ID | Title | Domain | Status |
|---|---|---|---|
| [MP-001](MP-001.md) | Explicit Ownership | lifecycle | CANONICAL |
| [MP-002](MP-002.md) | Change-Decision Boundaries | evolution | CANONICAL |
| [MP-003](MP-003.md) | Bounded Execution | resources | CANONICAL |
| [MP-004](MP-004.md) | Failure Containment by Scoped Propagation Boundaries | reliability | CANONICAL |
| [MP-005](MP-005.md) | Trust Minimization | security | CANONICAL |
| [MP-006](MP-006.md) | Obtainable Diagnostic Evidence | observability | CANONICAL |
| [MP-007](MP-007.md) | Contract Preservation | integration | CANONICAL |
| [MP-008](MP-008.md) | State Authority & Conflict Semantics | state-data | CANONICAL |
| [MP-009](MP-009.md) | Governed Overload Boundary | overload | CANONICAL |
| [MP-010](MP-010.md) | Execution-Model-Honest Correctness | concurrency | CANONICAL |

Promoted count is 10. Evaluation axioms AX-001..AX-004 live in the Constitution, not in this folder.

## Retired / reserved IDs

| ID | Disposition | Do not |
|---|---|---|
| AX-005 | usage-rule only; ID reserved | reuse as AX or MP |
| **MP-011** | RETIRED / NOT PROMOTED (Stage 6); tombstone in `reports/STAGE6_REDUCTION.md` §2 | reuse, revive as parent of MP-004/MP-005, or convert to AX |
| P-005 | Stage 4 REMOVED (decision heuristic / Stage 8 input) | reactivate as principle |
| P-011 | Stage 4 REMOVED (evaluation frame → AX lineage) | reactivate as principle |

MP-004 and MP-005 are **peers**. Stage 7 records `MP-004 RELATED_TO MP-005` only as a non-parent navigation edge.

## Non-principle review-signal / property lineage

| ID | Title | Home | Not |
|---|---|---|---|
| [P-006](P-006.md) | Change Locality / change amplification (V-014-D) | MP-002 review signal; `domains/evolution/`; GC-007 | Mother Principle, Failure Pattern, Tactic, or H7 locality revival |
| RQ5-001 | blast-radius measurement methodology | MP-004 `HAS_GAP`; D-10 NEEDS_EVIDENCE | MP, FP, or admitted universal metric |

No `review-signals/RS-*` type is instantiated. See Stage 7 report §15.

## Historical Stage 4 candidates（P-*，immutable）

以下文件是 Stage 4 候选制品，**不得改写或删除**。Stage 5/6 去留以 Constitution 与 Stage 5/6 报告为准，不以本表旧状态覆盖。

| ID | 候选 | Stage 6 disposition | 历史文件 |
|---|---|---|---|
| P-001 | Explicit Ownership | → MP-001 | [P-001.md](P-001.md) |
| P-002 | Change-Decision Boundaries | → MP-002 | [P-002.md](P-002.md) |
| P-003 | Bounded Execution | → MP-003 | [P-003.md](P-003.md) |
| P-004 | Failure Containment | → MP-004 | [P-004.md](P-004.md) |
| ~~P-005~~ | Reversibility-Proportional Deliberation | REMOVED (Stage 4) | — |
| P-006 | Change Locality | **非 MP**（review signal / property） | [P-006.md](P-006.md) |
| P-007 | Designed Diagnostic Surfaces | → MP-006 | [P-007.md](P-007.md) |
| P-008 | Contract Preservation | → MP-007 | [P-008.md](P-008.md) |
| P-009 | Trust Minimization | → MP-005 | [P-009.md](P-009.md) |
| P-010 | Authoritative State | → MP-008 | [P-010.md](P-010.md) |
| ~~P-011~~ | Purpose Fitness | REMOVED (Stage 4; AX frame) | — |
| P-012 | Overload Admission & Graceful Degradation | → MP-009 | [P-012.md](P-012.md) |
| P-013 | Execution-Model-Honest Correctness | → MP-010 | [P-013.md](P-013.md) |

H7 Locality remains demoted (D-13). MF-1 idempotency remains a tactic/contract property (`T-015`), not a principle.
