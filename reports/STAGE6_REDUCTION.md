---
id: REPORT-STAGE6-KIMI
type: stage-report
stage: 6
author: kimi-k3 (Primary First-Principles Reducer)
branch: research/stage6-reduction
date: 2026-09-20
issue: 15
input_baseline: "Stage 5 sealed (research/stage5-falsification@c09d72a5 系谱)；D-01..D-14 final；GOOD CASE register"
---
# Stage 6 Reduction Report — First-Principles Reduction (Kimi)

产物：`01_CONSTITUTION.md`（5 AX + 11 MP）。本文件是完整归约记录。未修改 canonical P-*；未做 Stage 7；未补源。

## 1. AX inventory（为何是公理而非因果原则）

| ID | 内容 | 非因果理由 |
|---|---|---|
| AX-001 | Evaluation Relativity | 评价框架/价值排序；不产生「违反→具体失败机制」的因果链（H1 在 Stage 4 已被判 category error，此处为其正确归宿） |
| AX-002 | Product-Contract Protection | 行为规范/治理约束（不得静默削弱能力），非系统结构主张 |
| AX-003 | Contextual Non-Negotiables | D-08 CONTEXTUAL ONLY 限定形式：适用的监管/安全/安保/外部契约约束限定权衡空间；**不主张普适 safety floor** |
| AX-004 | Minimum Sufficient Complexity | 元目标（评价其他原则代价侧），非因果主张（H9 归处） |
| AX-005 | Context > Pattern | 反教条元纪律，非结构因果主张 |

## 2. MP inventory（11 条；≤20 上限未作目标）

MP-001 Explicit Ownership · MP-002 Change-Decision Boundaries · MP-003 Bounded Execution · MP-004 Failure Containment ∝ Responsibility · MP-005 Trust Minimization · MP-006 Obtainable Diagnostic Evidence · MP-007 Contract Preservation · MP-008 State Authority & Conflict Semantics · MP-009 Overload Admission · MP-010 Execution-Model-Honest Correctness · MP-011 Power Proportionality（父原则，derived）

## 3. P-* → AX/MP disposition map

| Stage 5 输入 | Disposition | 落点 |
|---|---|---|
| P-001 (NARROW) | → MP-001 | 收窄保留（managed-heap 豁免边界） |
| P-002 (NARROW) | → MP-002 | 变化轴事前可识别写入 statement |
| P-003 (NARROW) | → MP-003 | lifetime/per-work 区分保留 |
| P-004 (SURVIVES) | → MP-004 | 原 statement；入 MP-011 父原则下作子机制 |
| P-007 (NARROW) | → MP-006 | question-relative 形式；无标量替代律 |
| P-008 (NARROW) | → MP-007 | 消费方独立性分级 |
| P-009 (NARROW) | → MP-005 | 边界触发条件限定；入 MP-011 下 |
| P-010 (SURVIVES) | → MP-008 | R4 双维 statement 原样 |
| P-012 (NARROW) | → MP-009 | 准入位置架构决策；priority≠admission |
| P-013 (SURVIVES+TAUTOLOGY_RISK) | → MP-010 | 过 tautology gate（见 §7） |
| P-006 (DEMOTE) | → 非 MP | MP-002 的 measurable property/review signal；Stage 7 metrics 层候选；RQ3-001 未触发 |

## 4. P-006 demotion preservation

按 OD5-1/Issue #15：不建 MP；作为 change amplification 度量信号关联 MP-002；若 Stage 7 批准 metrics/properties 层则为其输入。未做任何 rescue 研究。

## 5. Merge / hierarchy / separation 决策（含机制理由）

| 问题 | 决策 | 机制理由 |
|---|---|---|
| P-004+P-009 上位原则 | **PARENT + distinct child mechanisms**（MP-011 ← MP-004/MP-005） | 共享真实因果内容：「权力超过职责 → 成本落在责任方之外」；但 D-05 已证两子机制独立可违反（低权限组件放大故障 vs 隔离好但权限宽），故父不吞子 |
| P-001+P-010 共享上位 | **KEEP SEPARATE** | 共同措辞（「归属/权威显式」）是语言共性：lifecycle ownership 的失败机制是清理责任悬空（泄漏/孤儿），state authority 的失败机制是冲突无定义解（write skew/分歧）——机制不同源。上位合并无解释增益，拒绝 |
| P-003+P-012 资源治理父原则 | **KEEP SEPARATE** | 候选父「容量有限→设计极限行为」接近同义反复（资源有限是事实非机制）；ex-ante 维度界限与超载时准入回答不同问题，D-04 已证独立失败。父无新增判别力，拒绝 |
| P-007 是否 MP | **MP（收窄后）** | 因果核成立（信号位置决定证据可重建性）；question-relative 限定使其非 property 陈述 |
| P-008 是否独立 | **MP（独立）** | 机制（成本转嫁至交互方）不为任何演进公理所蕴含；S-124 显示其为独立的消费方分级判断 |
| P-002 口号检验 | **MP** | 与「modularity is good」的区分是因果的：无变化轴时本原则主动主张**不**划分（GOOD CASE），口号无此判别力 |
| P-013 tautology gate | **过，MP**（见 §7） | — |

## 6. D-01..D-14 preservation

| D | Stage 5 结果 | Stage 6 去向 |
|---|---|---|
| D-01 P-001/P-002 | DISTINCT | MP-001↔MP-002 Distinctions 段保留案例对 |
| D-02 P-001/P-013 | DISTINCT | stale overwrite 归因规则保留于 MP-010 |
| D-03 P-002/P-006 | DEMOTE P-006 | §4 执行 |
| D-04 P-003/P-012 | DISTINCT | MP-003↔MP-009 分立 + 父原则拒绝理由（§5） |
| D-05 P-004/P-009 | DISTINCT | MP-011 父子结构，子机制不合并 |
| D-06 P-010/P-001 | DISTINCT | MP-008↔MP-001 分立（§5 拒绝上位） |
| D-07 P-001/P-003 | DISTINCT | 取消语义归 MP-001、资源界限归 MP-003 |
| D-08 safety floor | CONTEXTUAL ONLY | AX-003 限定表述（见 §8） |
| D-09 P-013/P-010 | DISTINCT | MP-010↔MP-008 分立 |
| D-10 blast radius 度量 | NEEDS_EVIDENCE | MP-004 标注 RQ5-001 |
| D-11 P-007 | NARROW/claim-scoped | MP-006 question-relative |
| D-12 P-012 | NEEDS_EVIDENCE | MP-009 标注（priority≠admission） |
| D-13 H7 | NOT RESURRECTED | 维持降级 |
| D-14 P-010 CRDT | FRAMEWORK HOLDS | MP-008 含 CRDT GOOD CASE |

## 7. P-013 tautology 决策

**过 gate，保留为 MP-010**。依据（Issue #15 判据）：reduced statement 保留了非平凡判别内容——①经验判别类「assumed ≠ model-provided guarantee」预测具体失败模式（stale overwrite、时序窗口、僵尸工作）；②GOOD CASE 边界（模型真正保证的 per-pair 顺序/non-preemptive segment/具体 DBMS 隔离语义不得误报）有 Erlang 官方划界先例（S-115）。若未来表述坍缩为「正确系统依赖真实保证」，届时降级为 review/Constitution rule（OD5-5 条件保留）。

## 8. D-08 wording（AX-003）

采用：「当存在适用的、不可协商的监管/安全/安保/外部契约约束时，它们限定架构权衡空间。」不主张与域/产品无关的普适 safety floor；seL4/RFC 7568 只证明特定域的强制要求存在（S-118/S-120），不作普适推论。

## 9. Evidence family per MP

| MP | 家族 | 独立性评估 |
|---|---|---|
| MP-001 | 结构化并发谱系 + OTP/Armstrong 族 + 事故/监管族 + Go 官方 | 强（4 族；S-084..086 按 CA4-10 计一族） |
| MP-002 | Parnas 理论 + SEI 教材 + Shopify 实证 | 中-强（理论族同谱系；实证独立） |
| MP-003 | 定理 + 双云厂商 + 规范 + 事故 + 运行时平台 | 很强 |
| MP-004 | 模式专著 + 云实践 + 事故 + 安全科学 + OSDI（维度限定） | 强 |
| MP-005 | 1975 理论 + 政府标准 + 厂商方法 + 社区标准 + 平台契约 | 很强 |
| MP-006 | SRE 两书 + Majors(B) + OTel + Cook + SEC | 强（厂商立场已标） |
| MP-007 | 规范级 + 论文 + 平台 + DB 谱系 + IETF + PSF + Linux | 很强 |
| MP-008 | DB 理论 + 日志谱系 + 分布式实践 + local-first + CRDT | 强 |
| MP-009 | SRE/AWS（同生态集中，已标） + 规范 + 事故 | 中（厂商集中弱点诚实保留） |
| MP-010 | 定理族 + 平台契约（单谱系） + 航天事故 | 强 |
| MP-011 | 派生父原则：无新增证据；合法性 = D-05 判别 + 子原则证据族 | derived-parent（已标） |

## 10. GOOD CASE preservation matrix

| GOOD CASE（Stage 5 register §3） | 保护落点 |
|---|---|
| OTP supervised daemon / GC 托管堆 | MP-001 Applies + GOOD CASE；MP-003 软预算 |
| 探索期无边界原型 | MP-002 Applies When + GOOD CASE |
| lifetime indefinite + per-work 有界 | MP-003 statement 本体 |
| SQLite 单进程 | MP-004 GOOD CASE（S-117） |
| Arrakis 维度限定保护 | MP-004 GOOD CASE（S-122） |
| 广泛健康协调变更 | MP-002 非原则注记（P-006 归宿） |
| seL4 静态证明 | MP-006 GOOD CASE（S-118） |
| RFC 7568 / PEP 404 / Linux 内部 API | MP-007 GOOD CASE（S-120/121/124） |
| 封闭粗粒度信任 | MP-005 GOOD CASE |
| CRDT/log/local-first | MP-008 GOOD CASE（S-119/107） |
| 网关/path 级准入 | MP-009 GOOD CASE |
| 模型提供的时序/顺序保证 | MP-010 GOOD CASE（S-115） |

全部 14 条 register 条目有 MP 落点，无丢失。

## 11. Cross-shape check（宽 MP）

- MP-001：后端/Desktop（Electron main 拥有生命周期）/Embedded（静态任务）/分布式 ✓
- MP-002：Monolith（S-109）/Desktop（S-112）/DB-heavy ✓
- MP-003：服务端/事件循环/RTOS/金融单进程/分布式 ✓（最强跨形态）
- MP-004：云/分布式/Desktop/嵌入式（弱化形态 scoped）✓
- MP-005：企业/Web/Desktop/Agent runtime/嵌入式（退化形态注记）✓
- MP-006：服务端/嵌入式（约束形态）/Agent runtime（vendor evidence 注记）✓
- MP-007：后端 API/DB schema/local-first；Desktop ABI 证据缺席（诚实标注，不外推）◐
- MP-008：DB-heavy/分布式/local-first/Mobile（vendor-scoped 注记）✓
- MP-009：云/服务端；嵌入式准入 D-12 NEEDS_EVIDENCE（scoped）◐
- MP-010：分布式/并发运行时/RTOS/后端 ✓（单进程理论锚薄，自认）

## 12. 每个 MP 明确不规定什么

- MP-001：不规定 GC 是否足够、不强制 supervision 模式、不规定所有权粒度；
- MP-002：不规定分层数、DDD/Clean/微服务任何具体结构、模块大小；
- MP-003：不规定具体 timeout 值、配额大小、队列实现；
- MP-004：不规定进程边界、cell 化、多副本任何具体隔离 tactic；
- MP-005：不规定零信任产品、RBAC、mTLS 任何具体机制；
- MP-006：不规定 OTel 或任何遥测栈、不主张 instrument everything；
- MP-007：不规定 expand-contract/semver 任何具体迁移 tactic；
- MP-008：不规定 event sourcing/CQRS/CRDT 任何具体 tactic；
- MP-009：不规定 load shedding/circuit breaker 实现与位置；
- MP-010：不规定锁/全序化/版本防护任何具体机制；
- MP-011：不新增评审动作——评审落地用 MP-004/MP-005。

## 13. 残余 RQ 约束（解释时必须在场）

RQ5-001（blast radius 度量→MP-004 operationalization）、RQ5-002（保证机械判定→MP-010）、RQ5-003（观测/隐私→MP-006 trade-off 证据弱）、RQ5-004（负载有界豁免→MP-009）、RQ5-005（隔离级别名义 vs 实际→MP-008/MP-010 Stage 7 backlog）；RQ3-002（Java StructuredTaskScope→MP-001 realization 缺口）、RQ3-004（WASI capability→MP-005 形态实例）、RQ2-006（USL 不得唯一支撑）、RQ2-009（微服务正方证据缺——任何 MP 不得被推导出风格结论）。全部 non-blocking。

## 14. Stage 7 handoff

- domains 层：嵌入式隔离弱化形态、RTOS 准入机制（D-12）、browser 主线程（RQ3-005）、agent runtime 信任边界（S-110 时效）；
- failure-patterns 层：从各 MP 的 Failure Patterns Explained 段派生（Stage 5 dossier 已有素材）；
- tactics 层：断路器/舱壁/backpressure 等（与 MP 的 tactic 分离纪律保持）；
- metrics 层（若批准）：P-006 change amplification、blast radius 度量（RQ5-001）；
- cases/eval：GOOD CASE register 直接作为 false-positive fixture；D-01..14 判别案例对作为 recall fixture；
- 词汇：MP 文本已遵守 lexical gate，Stage 7 继承。

## 15. Rejected prettier-but-lossy reductions

1. **「Everything needs an owner/authority」大合并**（P-001+P-010+甚至 P-009）：语言共性，机制不同源——拒绝（D-06 会丢失）；
2. **「Resource governance」父原则**（P-003+P-012）：父接近同义反复——拒绝（D-04 信息会稀释为措辞）；
3. **P-007 并入 MP-006 上位「legibility」原则**：会把「诊断表面放置」的结构因果内容稀释为属性陈述——拒绝，保留收窄 MP；
4. **P-008 并入 evolvability 公理**：丢失「消费方独立性分级」的判别力（S-124 GOOD CASE）——拒绝；
5. **把 MP 压到 8 条以内**：会迫使上述合并之一发生——拒绝数量美学；
6. **MP-011 升格为唯一权力原则并删除子原则**：D-05 独立失败信息丢失——拒绝，采用父子结构。

## 16. 真正需要 owner 决策的问题

**无新增。** MP-011 父原则为派生抽象（无新增证据、合法性来自 D-05），CA 可在 gate 中判撤而不影响子原则；metrics/properties 层与否（Stage 7）为已登记延后事项。
