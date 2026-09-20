---
id: REPORT-STAGE6-KIMI
type: stage-report
stage: 6
author: kimi-k3 (Primary First-Principles Reducer)
branch: research/stage6-reduction
date: 2026-09-20
issue: 15
remediation_basis: "Issue #15 CA adjudication R6-1..R6-10；challenge/stage6-reduction@2d451b3 (accepted Pass B)"
input_baseline: "Stage 5 sealed；D-01..D-14 final；GOOD CASE register"
---
# Stage 6 Reduction Report（final，含 R6-1..R6-10 remediation）

产物：`01_CONSTITUTION.md`（4 AX + 10 promoted MP）。未修改 P-*、Stage 5 artifacts、sources、queue。

## 1. AX inventory（4 条，均非因果公理/约束）

- AX-001 Evaluation Relativity（评价框架，无因果链）；
- AX-002 Product-Contract Protection（治理约束，非结构主张）；
- AX-003 Contextual Non-Negotiables（D-08 CONTEXTUAL ONLY）；
- AX-004 Minimum Sufficient Complexity（代价侧元目标）。
- ~~AX-005 Context > Pattern~~ → **MOVE_TO_USAGE_RULE**（使用契约第 2 条保留该指令一次；ID 不复用）。

## 2. MP inventory（promoted 10 条）

MP-001 Explicit Ownership · MP-002 Change-Decision Boundaries · MP-003 Bounded Execution · MP-004 Failure Containment by Scoped Propagation Boundaries · MP-005 Trust Minimization · MP-006 Obtainable Diagnostic Evidence · MP-007 Contract Preservation · MP-008 State Authority & Conflict Semantics · MP-009 Governed Overload Boundary · MP-010 Execution-Model-Honest Correctness

**Tombstone**：`MP-011 Power Proportionality — RETIRED / NOT PROMOTED at Stage 6 reconciliation; category/abstraction error; no independent causal mechanism or evidence; ID reserved and MUST NOT be reused.`

Retiring MP-011 loses：**no unique mechanism**（其 mechanism 仅复述 MP-004/005 已有内容）、**no D-test**（D-05 作为 peer 关系反而更强）、**no GOOD CASE**（其条目只回指子原则）、**no source lineage**（无新增证据）。

## 3. P-* → AX/MP disposition map（final）

P-001→MP-001 · P-002→MP-002 · P-003→MP-003 · P-004→MP-004 · P-007→MP-006 · P-008→MP-007 · P-009→MP-005 · P-010→MP-008 · P-012→MP-009 · P-013→MP-010（过 tautology gate，带条件） · P-006→非 MP（MP-002 关联 property/review signal）

## 4. P-006 demotion preservation

不建 MP；作为 change amplification 度量信号关联 MP-002；Stage 7 metrics/property 候选（若该层获批）；RQ3-001 未触发。

## 5. Merge / hierarchy / separation 决策（final）

| 问题 | 决策 | 机制理由 |
|---|---|---|
| P-004+P-009 上位原则 | **RETIRE 父原则（MP-011），二者保持 peer** | 复核后认定：候选父只复述子原则机制，无独立因果内容/证据——counted parent 是无支撑的压缩（Pass B V6-24 FAIL）。D-05 以 peer distinction 保留 |
| P-001+P-010 上位 | **KEEP SEPARATE** | 语言共性；清理责任悬空 vs 冲突无定义解，机制不同源 |
| P-003+P-012 上位 | **KEEP SEPARATE（peer）** | 候选父「容量有限」接近同义反复；D-04 独立失败保留 |
| P-007 | **MP（question-relative 收窄）** | 因果核成立（证据放置决定可重建性），条件性保留 |
| P-008 | **MP 独立** | 消费方独立性分级的判别力（S-124） |
| P-002 口号检验 | **MP** | 无变化轴时主动主张不划分，与口号有因果区分 |
| P-013 tautology gate | **过，MP-010** | 见 §7 |

## 6. D-01..D-14 preservation（remediation 后复核）

全部保留：D-01 DISTINCT（MP-001/002）；D-02 DISTINCT（MP-001/010）；D-03 DEMOTE（P-006）；D-04 PEER（MP-003/009）；D-05 PEER（MP-004/005，MP-011 移除后 peer 关系更强）；D-06 DISTINCT（MP-008/001）；D-07 DISTINCT（MP-001/003）；D-08 CONTEXTUAL ONLY（AX-003）；D-09 DISTINCT（MP-010/008）；D-10 NEEDS_EVIDENCE（RQ5-001）；D-11 question-relative（MP-006）；D-12 NEEDS_EVIDENCE（MP-009）；D-13 NOT RESURRECTED；D-14 FRAMEWORK HOLDS（MP-008 GOOD CASE）。

## 7. P-013 tautology 决策

**过 gate，MP-010**。判别内容保留：assumed ≠ model-provided 判别类 + 扰动下具体失败模式预测 + GOOD CASE 边界（S-115 划界先例）。坍缩触发器保留：若未来表述退化为「正确系统依赖真实保证」，届时降级为 review/Constitution rule。

## 8. D-08 wording

AX-003：「当存在适用的、不可协商的监管/安全/安保/外部契约约束时，它们限定架构权衡空间。」不主张普适 safety floor。

## 9. Evidence family per MP（claim-relative status 格式，已写入 Constitution 各 MP）

格式：`Evidence status: <V-018 classes>; scope: <claim/shape>; concentration/gaps: <lineage/RQ>; Sources: <IDs>`。不以来源数量推强度；authority tier 不复制为 claim confidence；sibling 间不互借证据（MP-009 不继承 MP-003 的理论支撑；MP-005 不继承 MP-004 的遏制证据）。逐 MP 内容见 01_CONSTITUTION.md 各条 Evidence status 行（按 reconciliation §10.2 执行）。

## 10. GOOD CASE preservation matrix（MP-011 移除后复核：无丢失）

| Stage 5 GOOD CASE | 最终非违规落点 |
|---|---|
| OTP supervised daemon | MP-001（supervision 满足；indefinite lifetime 不违规） |
| Managed-heap GC reclamation | MP-001（仅回收维度豁免；语义 ownership 不豁免） |
| 探索期未知变化轴 | MP-002 不主张投机边界 |
| lifetime indefinite + per-work 有界 | MP-003 statement 本体（service 按运行时角色义读取） |
| SQLite 单进程经济 | MP-004 不要求进程边界/分布式遏制 |
| Arrakis 维度特定保护 | MP-004 只计入实际约束的维度 |
| 广泛但健康的协调变更 | P-006 非原则；协调一致的广泛变更不违规 |
| seL4 proof-scope | MP-006 只消解被证明且假设成立的问题 |
| 治理化安全破除 / 生态迁移 / Linux 内部 API | MP-007 三个 GOOD CASE（S-120/121/124） |
| 封闭/粗粒度信任 | MP-005 在无相关边界时不要求细分 |
| CRDT/local-first 多写 | MP-008 允许多写+显式合并语义 |
| Append-only log / 只读派生视图 | MP-008 视显式 append/派生语义为已定义冲突/权威模型 |
| 网关/path 级超载控制 | MP-009 要求路径上有受治理边界，不要求 service-local 代码 |
| 模型提供的时序/顺序保证 | MP-010 GOOD CASE（actor 顺序/non-preemptive/DBMS 语义） |

MP-011 未贡献任何独有 GOOD CASE；移除零损失。

## 11. Cross-shape check（claim/scope 表述，不用裸 checkmark）

- MP-001：后端/Desktop/Embedded/分布式（S-112 platform-scoped）；
- MP-002：Monolith（S-109 实证）/Desktop（S-112 scoped）；
- MP-003：服务端/事件循环/RTOS/金融单进程/分布式（维度特定证据）；
- MP-004：云/分布式/Desktop；嵌入式弱化形态 scoped；
- MP-005：企业/Web/Desktop/Agent runtime（S-110 新近性注记）；嵌入式退化形态注记；
- MP-006：服务端/嵌入式（约束形态）/Agent runtime（vendor evidence 注记）；
- MP-007：后端 API/DB schema/local-first；Desktop ABI 证据缺席（诚实标注）；
- MP-008：DB-heavy/分布式/local-first/Mobile（S-105 vendor-scoped）；
- MP-009：云/服务端；嵌入式准入 D-12 NEEDS_EVIDENCE；
- MP-010：分布式/并发运行时/RTOS/后端；单进程理论锚薄（自认）。

## 12. 每个 MP 明确不规定什么

- MP-001：不强制 supervision 模式、不规定所有权粒度、不评判 GC 选择；
- MP-002：不规定分层数/DDD/Clean/微服务/模块大小；
- MP-003：不规定具体 timeout/配额/队列实现；
- MP-004：**不强制进程边界**、cell 化、多副本任何具体隔离 tactic；
- MP-005：不 universalize zero trust、不规定 RBAC/mTLS；
- MP-006：**不规定任何遥测栈**、不主张 instrument everything；
- MP-007：**不强制 universal backward compatibility**、不规定 expand-contract/semver；
- MP-008：**不强制 single writer**、不规定 event sourcing/CQRS/CRDT；
- MP-009：**不强制 service-local admission/shedding**；
- MP-010：不规定锁/全序化/版本防护任何具体机制。

## 13. 残余 RQ 约束

RQ5-001（→MP-004 operationalization/metrics backlog）、RQ5-002（→MP-010 operationalization）、RQ5-003（→MP-006 trade-off 证据弱）、RQ5-004（→MP-009 scope）、RQ5-005（→MP-008/010 Stage 7 backlog）、RQ3-002（→MP-001 realization 缺口）、RQ3-004（→MP-005 capability 实例）、RQ2-006（USL 不得唯一支撑）、RQ2-009（微服务正方证据缺）。全部 non-blocking。

## 14. Stage 7 handoff（仅记录，不实施）

- 关系/导航：`MP-004 RELATED_TO MP-005`（via constrained cross-component impact/power；导航假设，非父语义、非证据继承；**本轮不创建 relationship-map / relation edge**）；
- cases/eval：§10 GOOD CASES → false-positive fixtures；D-01..D-14 → discriminator/recall fixtures；
- tactics：admission control / backpressure / load shedding-rejection / degradation 作为关联 MP-009 的**不同** tactic（非 alias）；
- metrics/properties：P-006 change amplification 与 RQ5-001 blast-radius 度量留在 MP 集外；
- domain 层：D-12（嵌入式容量行为）、RQ5-003（观测/隐私成本）、RQ5-005（名义 vs 实际保证缺口）保持 scoped gaps；
- lexical validation：Stage 7 构建关系与示例时继续强制 V-002/V-003/V-008/V-010 限定。
- **不创建**：relationship-map、domains、failure-patterns、tactics、metrics ontology、eval 文件。

## 15. Rejected prettier-but-lossy reductions

1. 「Everything needs an owner/authority」大合并——拒绝（D-06 丢失）；
2. 「Resource governance」父原则——拒绝（近同义反复，D-04 稀释）；
3. MP-011 式 counted 父原则（Power Proportionality）——复核后 RETIRE：无独立机制/证据/GOOD CASE/lineage，纯语言压缩；
4. P-007 并入上位 legibility 原则——拒绝（稀释结构因果内容）；
5. P-008 并入 evolvability 公理——拒绝（丢失消费方分级判别力）；
6. 压 MP 数量至 8 条以内——拒绝数量美学。

## 16. 真正需要 owner 决策的问题

**无新增。** MP-011 退休为 CA 已裁决事项的执行；metrics/properties 层留 Stage 7 已登记事项。
