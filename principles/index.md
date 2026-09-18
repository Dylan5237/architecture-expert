---
id: IDX-PRINCIPLES
title: principles/ index
stage: 4
status: candidate-set-remediated
updated: 2026-09-18
remediation_basis: "Issue #9 CA adjudication R1..R8 (OD4-1..4, CA4-1..11)"
---
# principles/ 索引（Stage 4 候选集，remediation 后）

**11 个候选原则**（P-005/P-011 已移除，**ID 保留空号不重排**）。候选 ≠ Mother Principle；Stage 5 证伪后才可能升格。提取依据与 H1..H11 disposition 见 `../reports/STAGE4_EXTRACTION.md`。

| ID | 候选 | 对应假设 | 状态 |
|---|---|---|---|
| P-001 | Explicit Ownership | H2b retain | CANDIDATE |
| P-002 | Change-Decision Boundaries | H2a retain（收窄） | CANDIDATE |
| P-003 | Bounded Execution | H3 retain | CANDIDATE |
| P-004 | Failure Containment ∝ Responsibility | H4 retain+narrow | CANDIDATE（R5 措辞修正后） |
| ~~P-005~~ | ~~Reversibility-Proportional Deliberation~~ | H5a **DEMOTE → Decision Playbook / decision heuristic**（OD4-2；Stage 8 输入保留于 extraction report） | REMOVED |
| P-006 | Change Locality | H5b retain | **NEEDS_EVIDENCE / OVERLAP_UNRESOLVED**（Stage 5 D-03 判别后定去留） |
| P-007 | Designed Diagnostic Surfaces | H6 retain + R6 因果重述 | CANDIDATE（附 Stage 5 条件测试 D-11：找不到结构判别案例则降为 required property） |
| P-008 | Contract Preservation | H8 retain（重命名） | CANDIDATE（R3 修正后；expand-contract 不作证据） |
| P-009 | Trust Minimization | H10 retain | CANDIDATE |
| P-010 | Authoritative State | H11 narrow | CANDIDATE（R4 双维修正后；D-14 CRDT 收窄留 Stage 5） |
| ~~P-011~~ | ~~Purpose Fitness~~ | H1 **DEMOTE → Constitution / evaluation frame**（OD4-1；Constitution 输入保留于 extraction report） | REMOVED |
| P-012 | Overload Admission & Graceful Degradation | 证据新增 | CANDIDATE |
| P-013 | Execution-Model-Honest Correctness | 证据新增 | CANDIDATE（R7 重述后；附 Stage 5 条件测试 D-02/D-09） |

已降级/未成为候选（rationale 见 extraction report §3）：
- H7 Locality → demote 为 Stage 5 待检验假设（V-014-C 多机制混合倾向，无单一机制；D-13 复活检验）；
- H9 Controlled Complexity → demote 为 Constitution/meta-objective（元目标非因果主张）；
- MF-1 idempotency → non-principle（explicit delivery semantics 下的 mechanism/tactic/contract property）；
- Tail-at-scale hedging、USE method、SLO 等 → tactic/metric 层，不进 P-*。

词汇 gate：所有 P-* 文件遵守 Stage 3 lexical gate（高风险词带 V-* 引用）。
