---
id: CONSTITUTION
type: architecture-constitution
stage: 6
status: draft-proposed
author: kimi-k3 (Primary First-Principles Reducer)
branch: research/stage6-reduction
date: 2026-09-20
issue: 15
input: "Stage 5 sealed dispositions (10 survivors + P-006 demoted)；D-01..D-14 final"
---
# 01_CONSTITUTION — Architecture Constitution（Draft）

**Architecture exists to protect required system properties under real constraints.**

本文档分两层：**AX-*** = 评估公理/治理约束（非因果原则）；**MP-*** = 因果 Mother Principles（当前 12 条，含 1 条父原则；≤20 是上限不是目标）。完整推导与证据谱系见 `reports/STAGE6_REDUCTION.md`；术语以 `02_VOCABULARY.md` 为准（高风险词必须带 V-* 限定）。

## 使用契约

1. MP 是因果主张：可以被违反，违反产生可指认的失败机制。不可被违反的表述不是原则。
2. Context > Pattern：任何判断从 required properties 与 constraints 出发；风格/模式/工具不作为答案。
3. 每个 MP 的 Applies When 是其组成部分；超出 scope 的引用是误用。
4. GOOD CASE 边界（见各 MP 与 reduction §10）是原则的组成部分：命中 GOOD CASE 的系统不是违规。
5. 证据不足时输出 NEEDS_EVIDENCE / CONTESTED，不猜测。

## Evaluation Axioms（AX）

### AX-001 Evaluation Relativity
架构评估只能相对 required properties（V-004-C）与 real constraints（V-004-D）进行；脱离二者的架构评价无判别力。Derived from: H1（Stage 4 demoted）。

### AX-002 Product-Contract Protection
实现困难不得静默削弱 product contract；真实冲突必须显式暴露为 trade-off 或升级决策。Derived from: H1 / 任务书 §22。

### AX-003 Contextual Non-Negotiables
当存在适用的、不可协商的监管/安全/安保/外部契约约束时，它们限定架构权衡空间。**语境限定（D-08 CONTEXTUAL ONLY）：不主张与域/产品无关的普适 safety floor。** Derived from: Stage 5 D-08。

### AX-004 Minimum Sufficient Complexity
目标是能安全保护 required properties 的最小复杂度；「简单」与「复杂」本身都不是目标。Derived from: H9（demoted meta-objective）。

### AX-005 Context > Pattern（反教条）
不把任何架构风格/pattern/tactic 当作默认正确；「X 优于 Y」形式的主张默认 CONTEXT_DEPENDENT 直到给出机制与边界。Derived from: Stage 1 研究立场 + Stage 2/3 反教条纪律。

## Mother Principles（MP）

### MP-001 Explicit Ownership
- **Statement**: 运行时实体与可变状态的创建/修改/停止/清理必须有可回答的归属。
- **Mechanism**: 故障恢复与变更需要可定位的裁决者；归属悬空 → 泄漏/孤儿/陈旧覆盖。
- **Protects**: reliability, correctness, operability。
- **Applies When**: 存在并发执行、异步任务、可变状态或需清理资源。豁免仅限运行时托管的资源回收维度（managed-heap reclamation）；总量责任与写权裁决不豁免。
- **Derived from**: P-001（NARROW）。
- **Evidence**: S-084/085/086（结构化并发谱系）、S-114（OTP supervision——合规机制实例，非普适 runtime invariant）、S-091、S-062、S-116（GC 豁免边界）。
- **GOOD CASE**: supervised daemon 无限运行；GC 托管堆（runtime 软预算）。
- **Distinctions**: ≠ MP-008（状态裁决语义）；≠ MP-003（资源界限）。D-02/D-06/D-07。

### MP-002 Change-Decision Boundaries
- **Statement**: 模块应按「可事前识别的、可能变化的设计决策」划分，易变决策隐藏在稳定接口后；边界仅在两侧变化规则确实不同时保护属性。
- **Mechanism**: 变更成本≈受影响单元数×单元成本；信息隐藏把易变决策的爆炸半径限制在单模块内。
- **Protects**: evolvability, correctness。
- **Applies When**: 预期多次变更且变化轴可合理识别的系统；探索期未知变化轴时无边界合法。
- **Derived from**: P-002（NARROW）。
- **Evidence**: S-001（Parnas）、S-005、S-012、S-109（Shopify 实证）、S-112（platform-scoped）。
- **GOOD CASE**: 探索期原型无显式边界；性能轴上的刻意跨层调用。
- **Distinctions**: ≠ 「modularity is good」口号——变化轴不可识别时本原则不主张划分；change amplification 仅作其 review signal（P-006 降级后的归宿）。D-01/D-03。

### MP-003 Bounded Execution
- **Statement**: system/service/stream 的 lifetime 可以 indefinite；但相关时，per-work execution/wait/retention time、retry、queue、concurrency、memory、fan-out 等维度需要 effective bound 或 governed policy。
- **Mechanism**: L=λW——固定容量下超载转化为积压与级联超时；无界维度在负载/故障下以资源耗尽形式失效。
- **Protects**: reliability, latency, availability。
- **Applies When**: 共享资源、外部输入、异步工作、跨边界调用。隐含界（输入限定的批处理）与 runtime 软预算（GOMEMLIMIT 型）是合法形态。
- **Derived from**: P-003（NARROW）。
- **Evidence**: S-072/073（Little's Law）、S-048/050/052、S-090、S-059/061/062/065（事故）、S-088、S-113、S-116。
- **GOOD CASE**: lifetime indefinite 但 per-work 有界的 daemon/流；隐含界批处理；软预算托管堆。
- **Distinctions**: ≠ MP-009（超载时行为）；取消/清理语义归 MP-001。D-04/D-07。

### MP-004 Failure Containment ∝ Responsibility
- **Statement**: 子系统的故障权力应与职责相称；隔离边界（failure domain：结构分区）按可接受影响范围设计，把故障后的 blast radius（结果影响面）遏制在其内。
- **Mechanism**: 故障沿共享资源与依赖传播；隔离切割传播图；防御机制若自耦合则成为放大器。
- **Protects**: availability, reliability。
- **Applies When**: 共享瓶颈、多租户、故障成本高的路径。隔离单元粒度是替代保证机制（进程边界/硬件虚拟化等，维度特定）与成本模型的函数，不默认进程边界；单进程单用户形态豁免。
- **Derived from**: P-004（SURVIVES）。
- **Evidence**: S-047、S-050、S-061/063/060（事故）、S-053、S-117（SQLite 反例形态）、S-122（Arrakis，仅 I/O 保护维度）。
- **GOOD CASE**: SQLite 单进程；Arrakis 硬件下放（维度限定）。
- **Distinctions**: 与 MP-005 同父（MP-011）但机制独立（故障传播 vs 信任/权限）；blast radius ≠ failure domain（结构 vs 度量）。D-05。度量方法论 NEEDS_EVIDENCE（RQ5-001）。

### MP-005 Trust Minimization
- **Statement**: 在存在不可信输入、多权限级别、外部集成或 agent 动作执行权的边界上，信任与权限必须按职责最小化。
- **Mechanism**: 攻击者损害 ≤ 被攻破组件持有的权限；least privilege 上限化单点攻破损失。
- **Protects**: security, reliability。
- **Applies When**: 上述边界存在时；封闭单用户形态的进程内部不强制细分信任边界。
- **Derived from**: P-009（NARROW）。
- **Evidence**: S-092（1975 原始）、S-093、S-096、S-110（agent 形态，时效注意）、S-112（platform-scoped）。
- **GOOD CASE**: 同团队单部署单元的内部粗粒度权限。
- **Distinctions**: 与 MP-004 同父但独立可违反（D-05）；capability 形态实例 NEEDS_EVIDENCE（RQ3-004）。

### MP-006 Obtainable Diagnostic Evidence
- **Statement**: 对未被更强静态保证消解的 operational questions（实际被证明且假设成立的问题除外），区分与归因相关运行时状态所需的证据必须由设计使其可获得。
- **Mechanism**: 证据的可获得性由信号/状态在边界与执行路径上的放置决定；缺失的证据不可事后补推（运维闭环的上游）。
- **Protects**: operability, reliability。
- **Applies When**: 持续运行/故障响应系统；深度受形态与成本约束（不是 instrument everything）。
- **Derived from**: P-007（NARROW，question-relative）。
- **Evidence**: S-048/049（SRE）、S-055（厂商立场已标）、S-058、S-053、S-062、S-118（seL4：静态证明只消解被证明且假设成立的问题）。
- **GOOD CASE**: seL4 型静态证明系统（假设集内）；DO-178C 式极简观测嵌入式。
- **Distinctions**: 无「静态证明越多观测越少」的标量替代律；观测成本/隐私/安全为 trade-off。D-11。

### MP-007 Contract Preservation
- **Statement**: 存在 independent consumer 依赖的 contract（V-012-B）必须保持显式兼容方向（reader/writer 视角）与迁移路径；破兼容仅在更高优先级 security/correctness 要求或治理化协调迁移显式主导时合法。
- **Mechanism**: 契约是跨边界协作的唯一稳定点；破坏契约把变更成本强转嫁给所有交互方。
- **Protects**: compatibility, evolvability, correctness。
- **Applies When**: 独立演进节奏的多方交互；内部紧协调接口的稳定性政策可合法不同。
- **Derived from**: P-008（NARROW）。
- **Evidence**: S-044/045、S-039、S-042、S-037/038、S-120（RFC 7568）、S-121（PEP 404）、S-124（Linux 内部接口）。
- **GOOD CASE**: 治理化安全破除；治理化生态演进；Linux 内部 API 不稳定 + syscall 稳定。
- **Distinctions**: 不弱化为「兼容有时可破」；行为语义兼容的可机检性 NEEDS_EVIDENCE。

### MP-008 State Authority & Conflict Semantics
- **Statement**: 每类状态必须显式声明两个正交维度：write/state authority（V-003-D）与 conflict/consistency semantics（V-010 带义项后缀）；任一不清则并发/故障下状态结果不可判定。
- **Mechanism**: 无裁决规则 → 冲突无定义解（lost update / write skew）；副本与权威漂移；合并语义（若多写）必须显式。
- **Protects**: correctness, reliability。
- **Applies When**: 可变状态 +（并发写 或 多副本 或 缓存层）。single-writer 非必需（CRDT/显式合并语义合法）。
- **Derived from**: P-010（SURVIVES）。
- **Evidence**: S-023、S-034/036、S-040/046、S-038、S-107、S-119（CRDT）。
- **GOOD CASE**: CRDT/local-first；append-only 无冲突域；只读派生视图。
- **Distinctions**: ≠ MP-001（归属程序 vs 裁决语义）；≠ MP-010（时序保证）。D-06/D-09/D-14。

### MP-009 Overload Admission & Graceful Degradation
- **Statement**: 当需求/工作可超过可用容量时，请求路径（服务/网关/mesh 任一或组合层）必须有显式准入控制与降级策略。
- **Mechanism**: 无准入 → 到达率>服务率 → 积压失稳 → 重试放大 + 容量损失反馈环；恢复流量同样需要准入。
- **Protects**: availability, reliability。
- **Applies When**: 不可控负载的请求路径；负载天然有界系统豁免（NEEDS_EVIDENCE 级 scope 注记）；准入位置是架构决策但精确卸载需要本地信息。
- **Derived from**: P-012（NARROW）。
- **Evidence**: S-048/049、S-050、S-052、S-090、S-061/065（事故）。厂商谱系集中度已标。
- **GOOD CASE**: 网关/path 级承担准入的服务；负载天然有界工具。
- **Distinctions**: ≠ MP-003（D-04 独立失败）；priority scheduling ≠ admission control（D-12 NEEDS_EVIDENCE）。

### MP-010 Execution-Model-Honest Correctness
- **Statement**: 正确性不得依赖执行模型未实际提供的时序/顺序/中断/取消/时钟保证；正确性关键保证必须由实际 primitive/contract/coordination semantics 强制。判别类：assumed guarantee ≠ model-provided guarantee——真实系统反复犯此类失配，并在扰动下产生具体失败模式。
- **Mechanism**: 隐式依赖不存在的保证，在调度扰动/延迟/重排序/取消/时钟行为下失效（Lamport 偏序；FLP 限定形式）。
- **Protects**: correctness。
- **Applies When**: 并发、异步、分布式、取消传播存在的系统。
- **Derived from**: P-013（SURVIVES + TAUTOLOGY_RISK——过 tautology gate 的依据：保留了经验判别类与 GOOD CASE 边界；若未来被读成「正确系统依赖真实保证」则降级）。
- **Evidence**: S-025/030/031（定理族）、S-023、S-084..086、S-091、S-115（Erlang 官方划界先例）。
- **GOOD CASE**: 模型真正保证的 per-pair 消息顺序、non-preemptive segments、具体 DBMS 承诺的隔离语义——不得误报。
- **Distinctions**: ≠ MP-008（顺序保证 vs 状态裁决，D-09）；≠ MP-001（stale overwrite 归因规则，D-02）。

### MP-011 Power Proportionality（父原则）
- **Statement**: 组件影响他方的权力（故障权力、信任/权限）不应超过其职责所要求的范围。
- **Mechanism**: 超出职责的权力创造「成本落在责任方之外」的风险形态——故障权力经传播图放大（MP-004），信任权力经攻击面放大（MP-005）。
- **Protects**: availability, security（经子原则）。
- **Applies When**: 存在跨组件权力（共享资源、权限授予）的系统。
- **Derived from**: P-004 + P-009 的上位抽象（D-05：子机制独立可违反，分立保留）。
- **Evidence**: 派生（无新增证据；合法性来自 D-05 判别 + 子原则证据族）。状态：derived-parent。
- **GOOD CASE**: 同子原则。
- **Distinctions**: 父原则不替代子原则的机制与 scope；评审落地用子原则。

## 非原则登记（不升格）

- P-006 Change Locality → MP-002 的 measurable property / review signal（change amplification）；Stage 7 metrics 层候选（若该层获批）。
- H7 locality → 未复活（D-13）。
- idempotency → explicit delivery semantics 下的 mechanism/tactic/contract property（MF-1）。
- USE/SLO/hedged requests/circuit breaker/event sourcing/strangler 等 → tactic/metric 层（Stage 7）。

## 残余不确定性（解释约束）

RQ5-001..005（全部 non-blocking）、RQ3-002/004、RQ2-006（USL）、RQ2-009（微服务正方证据）——见 `review-queue.yaml`；引用相关 MP 时这些缺口在场。
