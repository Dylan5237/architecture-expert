---
id: IDX-PRINCIPLES
title: principles/ index
stage: 4
status: candidate-set
updated: 2026-09-18
---
# principles/ 索引（Stage 4 候选集）

13 个候选原则（CANDIDATE / CONTESTED / NEEDS_EVIDENCE）。**候选 ≠ Mother Principle**；Stage 5 证伪后才可能升格。提取依据与 H1..H11 disposition 见 `../reports/STAGE4_EXTRACTION.md`。

| ID | 候选 | 对应假设 | 状态 |
|---|---|---|---|
| P-001 | Explicit Ownership | H2b retain | CANDIDATE |
| P-002 | Change-Decision Boundaries | H2a retain（收窄） | CANDIDATE |
| P-003 | Bounded Execution | H3 retain | CANDIDATE |
| P-004 | Failure Containment ∝ Responsibility | H4 retain+narrow | CANDIDATE |
| P-005 | Reversibility-Proportional Deliberation | H5a narrow | CANDIDATE |
| P-006 | Change Locality | H5b retain | NEEDS_EVIDENCE（RQ3-001） |
| P-007 | Legibility for Operability | H6 retain | CANDIDATE |
| P-008 | Contract Preservation | H8 retain（重命名） | CANDIDATE |
| P-009 | Trust Minimization | H10 retain | CANDIDATE |
| P-010 | Authoritative State | H11 narrow | CANDIDATE |
| P-011 | Purpose Fitness | H1 retain（meta-principle 候选） | CANDIDATE |
| P-012 | Overload Admission & Graceful Degradation | 证据新增 | CANDIDATE |
| P-013 | Explicit Time & Ordering Assumptions | 证据新增 | CANDIDATE |

已降级/未成为候选（rationale 见 extraction report §3）：
- H7 Locality → demote 为 Stage 5 待检验假设（V-014-C 多机制混合倾向，无单一机制）；
- H9 Controlled Complexity → demote 为 meta-objective（元目标非因果主张）；
- Tail-at-scale hedging、USE method、SLO 等 → tactic/metric 层，不进 P-*。

词汇 gate：所有 P-* 文件遵守 Stage 3 lexical gate（高风险词带 V-* 引用）。
