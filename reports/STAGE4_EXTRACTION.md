---
id: REPORT-STAGE4-KIMI
type: stage-report
stage: 4
author: kimi-k3 (Primary Researcher / Principle Extractor)
branch: research/stage4-principles
date: 2026-09-18
remediated: 2026-09-18
remediation_basis: "Issue #9 CA adjudication R1..R8；challenge/stage4-principles@c56e34a5 (Pass B, accepted)"
issue: 9
evidence_baseline: "Stage 2 corpus (S-001..S-113) + Stage 3 sealed vocabulary (02_VOCABULARY.md v2)"
---
# Stage 4 Extraction Report — Principle Extraction (Kimi)（v2，含 remediation R1..R8）

边界声明：本轮只做 Extract → Normalize → Compare + 有界 remediation。未做 Stage 5 完整证伪；未写 01_CONSTITUTION.md；未创建 Decision Playbook；未创建 FP-*/T-*；未写 Agent Prompt；未新增来源；未重排 P-* ID。全部 P-* 遵守 Stage 3 lexical gate。

## 1. 候选清单（remediation 后，**11 个文件**）

| ID | 候选 | 来源假设 | 状态 | 证据家族独立性 |
|---|---|---|---|---|
| P-001 | Explicit Ownership | H2b | CANDIDATE | 强（纲领+平台实现链——按 CA4-10 计为一族——+航天事故+监管文件） |
| P-002 | Change-Decision Boundaries | H2a | CANDIDATE | 强（1972 理论+SEI+企业实证） |
| P-003 | Bounded Execution | H3 | CANDIDATE | 很强（定理+双云厂商+规范+四事故+双运行时） |
| P-004 | Failure Containment ∝ Responsibility | H4 | CANDIDATE（R5 修正） | 强（模式专著+云实践+三事故+安全科学） |
| P-006 | Change Locality | H5b | **NEEDS_EVIDENCE / OVERLAP_UNRESOLVED**（D-03） | 弱（单源 S-001） |
| P-007 | Designed Diagnostic Surfaces | H6 | CANDIDATE（R6 重述；附 D-11） | 强（双厂商谱系+标准+理论+监管实证） |
| P-008 | Contract Preservation | H8 | CANDIDATE（R3 修正） | 强（规范级+论文+平台+DB 谱系） |
| P-009 | Trust Minimization | H10 | CANDIDATE | 很强（1975 理论+政府标准+厂商方法+社区标准+平台契约） |
| P-010 | Authoritative State | H11 | CANDIDATE（R4 修正） | 强（DB 理论+日志谱系+分布式实践+local-first） |
| P-012 | Overload Admission & Graceful Degradation | 证据新增 | CANDIDATE | 强但厂商集中（SRE/AWS 谱系+规范+事故；D-12） |
| P-013 | Execution-Model-Honest Correctness | 证据新增 | CANDIDATE（R7 重述；附 D-02/D-09） | 强（分布式理论+平台契约+事故）；单进程理论锚较薄 |

已移除（category error，CA 裁定）：
- **P-011 Purpose Fitness**（R1）：H1 是评估公理/价值排序，非结构因果主张 → DEMOTE → Constitution / evaluation frame；
- **P-005 Reversibility-Proportional Deliberation**（R2）：H5a 主语是决策程序投入，非系统结构机制 → DEMOTE → Decision Playbook / decision heuristic。

候选总数：**11**（稳定 ID 不重排，P-005/P-011 空号保留）。

## 2. H1..H11 disposition 表（final）

| H | Disposition | 落点 |
|---|---|---|
| H1 Purpose Fitness | **DEMOTE → Constitution / evaluation frame**（OD4-1） | 见 §10 Constitution 输入 |
| H2a Explicit Boundaries | retain + narrow | P-002 |
| H2b Explicit Ownership | retain | P-001 |
| H3 Bounded Execution | retain | P-003 |
| H4 Failure Containment | retain + narrow（graded） | P-004 |
| H5a Reversibility | **DEMOTE → Decision Playbook / decision heuristic**（OD4-2） | 见 §10 Stage 8 输入 |
| H5b Change Locality | retain as NEEDS_EVIDENCE + OVERLAP_UNRESOLVED | P-006（D-03） |
| H6 Legibility/Operability | retain + R6 因果重述 | P-007 |
| H7 Locality | demote（不生成 P-*；V-014-C 骨架 + D-13 复活检验） | — |
| H8 Compatibility | retain + rename → Contract Preservation | P-008 |
| H9 Controlled Complexity | **DEMOTE → Constitution / meta-objective**（显式化，承 OD4-1 框架） | 见 §10 Constitution 输入 |
| H10 Trust Minimization | retain | P-009 |
| H11 Authoritative State | retain + narrow | P-010 |

## 3. Merge / Split / Narrow / Reject 推理

- **Split**：H2 → P-001/P-002；H5 → P-005(已移除)/P-006。
- **Narrow**：H4（graded 化）、H8（行为面+视角纪律）、H11（适用面限定 + R4 双维正交化）。
- **Reject/Demote**：H7（多机制混合，无单一因果链）；H9（元目标非因果主张 → Constitution/meta-objective）；H1（评估公理 → Constitution/evaluation frame）；H5a（决策程序 → Decision Playbook 输入）。
- **新增（证据驱动）**：P-012、P-013。
- **未升格**：USE method（metric/方法论）、SLO（metric）、hedged requests（tactic）、circuit breaker/bulkhead（tactic）、event sourcing/CQRS（tactic）、strangler/expand-contract（tactic，后者 NEEDS_EVIDENCE）、微服务等风格标签、「可用性很重要」（属性）。
- **MF-1 disposition（OD4-3）**：idempotency under at-least-once → **non-principle**：explicit delivery semantics 下的 mechanism/tactic/contract property；其因果内容由 P-010（冲突/裁决语义）与 P-013（时序保证诚实性）覆盖，残余为操作性质（effect-equivalence）。不设独立原则。

## 4. Evidence-family map（含 CA4-10 lineage 修正）

- 定理族：S-024/025/026/028/030/031/072/073/074/075；
- SEI/ISO 族：S-005/006/008/019；
- SRE/AWS 族：S-048/049/050/052（同生态集中度警告维持）；
- 事故实证族：S-059..065/091/062；
- 平台契约族：S-084..090/105/112/113（S-084+085+086 = **同一概念谱系 + 平台实现，计为一族加平台佐证**，不重复计为三个独立理论族）；
- 安全标准族：S-092/093/096/110；
- DB/集成谱系：S-032..046；
- Fowler/ThoughtWorks 族：S-010/011/014/018/020——**注记：均属同一 broad lineage（演进性/决策观话语圈），不同文件不构成独立证据家族**；P-005 移除后该族不再支撑任何 P-*，仅作为 Constitution/Playbook 输入的背景。

## 5. Candidate-to-vocabulary map（lexical gate 合规自查）

全部 P-* 检索高风险词并挂 V-*：consistency→V-010（P-010）；atomicity→V-011-E 消歧纪律（未裸用）；authority→V-003-D（P-010 双维表述）；isolation→V-005-E/V-011-C 分义；context→V-007-D/V-020-D 分义；compatibility 方向→V-013-A/B（P-008）；container/component/service→V-002；stateless→V-021-H（P-001）；locality→V-014-C+N-8（P-006）；resilience/fault tolerance→V-005-C/D 无排序断言。**未发现裸用。**

## 6. 独立支撑不足的候选

- P-006（NEEDS_EVIDENCE + OVERLAP_UNRESOLVED，D-03）；
- P-012（厂商谱系集中，D-12 非服务端实证）；
- P-013（单进程理论锚薄，自认）；
- P-007（R6 重述后附 D-11 条件：结构判别案例失败则降 required property）。

## 7. BACKFLOW_TRIGGER 清单（按 CA adjudication 更新）

- **Stage 4 无 promotion-critical evidence backflow**（CA 裁定）。
- RQ3-001：**不触发**——P-006 的独立候选资格须先过 Stage 5 D-03，不为救 P-006 采证；
- RQ3-002/003/004：不触发；
- RQ3-005：可选的 Stage 5 跨形态补强，非 Stage 4 blocker；
- RQ3-006：**不触发**——正确修正是删除 P-008 中 expand-contract 的肯定性使用（R3 已完成），而非补证保它。

## 8. 留给 Stage 5 的重叠判别清单 → 已由预注册判别集取代（见 §9）

## 9. Stage 5 预注册判别集（D-01..D-14，承 accepted Pass B，本轮不执行）

| ID | 判别内容 | 失败后果 |
|---|---|---|
| D-01 | P-001 vs P-002 案例对 | 合并 |
| D-02 | P-001 vs P-013：stale overwrite 归因 | 归属规则重划 |
| D-03 | P-002 vs P-006：可度量子 vs 划分依据 | P-006 降 property |
| D-04 | P-003 vs P-012：有界无策略 vs 有策略无界 | 合并 |
| D-05 | P-004 vs P-009：故障权力≠信任权力案例对 | 按 OD4-4 保持分立 |
| D-06 | P-010 vs P-001：裁决语义 vs 归属程序 | 分立维持 |
| D-07 | P-001 vs P-003（CF-1）：取消语义 vs 资源界限（owned-but-unbounded vs bounded-but-unowned） | 语义归 P-001、界限归 P-003 |
| D-08 | safety floor 存在性与范围（原 P-011 弹性检验的 Constitution 化转型） | Constitution 公理加限定 |
| D-09 | P-013 vs P-010：顺序保证 vs 状态裁决 | 分立维持 |
| D-10 | P-004 blast radius 度量可操作性 | 降 heuristic |
| D-11 | P-007 反例搜索 + 结构判别 | 降 required property |
| D-12 | P-012 非服务端实证 | 形态 scoped |
| D-13 | H7 复活检验：locality 是否存在单一机制 | 维持降级 |
| D-14 | P-010 CRDT 收窄：「多写无裁决但显式合并语义」边界 | 收窄 statement |

## 10. 降级内容的未来落点（非本轮创建文件）

**Constitution / evaluation frame 输入（H1、H9；Stage 6 使用，D-08 待定）：**
- 架构评估相对 required properties（V-004-C，项目词）+ real constraints（V-004-D）；
- implementation difficulty 不得静默削弱 product contract——真实冲突显式暴露为 trade-off；
- safety/security floor 的存在与范围留 Stage 6 D-08；
- H9：目标是最小充分复杂度（minimum complexity required to safely protect required system properties）——作为元目标约束各原则的代价侧，不作独立原则。

**Decision Playbook 输入（H5a；Stage 8 使用）：**
- deliberation / alternatives / rationale effort 应随 irreversibility 与 error cost 增长；
- 明确声明：这是 decision-process heuristic，不是系统结构原则。

## 11. 真正需要 owner 决策的问题

**无新增。** 两项 Pass B 登记的非阻塞延后事项维持延后：metrics/properties ontology 层（Stage 7 视需要）；safety floor 表述（Stage 6 D-08）。
