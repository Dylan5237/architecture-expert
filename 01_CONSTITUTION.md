---
id: CONSTITUTION
type: architecture-constitution
stage: 6
status: draft-remediated
author: kimi-k3 (Primary First-Principles Reducer)
branch: research/stage6-reduction
date: 2026-09-20
issue: 15
remediation_basis: "Issue #15 CA adjudication R6-1..R6-10；challenge/stage6-reduction@2d451b3 (accepted Pass B)"
---
# 01_CONSTITUTION — Architecture Constitution（Draft）

**Architecture exists to protect required system properties under real constraints.**

本文档分两层：**AX-*** = 评估公理/治理约束（非因果原则，当前 4 条）；**MP-*** = 因果 Mother Principles（**promoted 共 10 条**；MP-011 已 RETIRED/NOT PROMOTED，见 `reports/STAGE6_REDUCTION.md` tombstone；≤20 是上限不是目标）。术语以 `02_VOCABULARY.md` 为准（高风险词必须带 V-* 限定）。

## 使用契约

1. MP 是因果主张：可以被违反，违反产生可指认的失败机制。不可被违反的表述不是原则。
2. **Context > Pattern**：任何判断从 required properties 与 constraints 出发；「X 优于 Y」形式的主张默认 CONTEXT_DEPENDENT 直到给出机制与边界；风格/模式/工具不作为答案。
3. 每个 MP 的 Applies When 是其组成部分；超出 scope 的引用是误用。
4. GOOD CASE 边界是原则的组成部分：命中 GOOD CASE 的系统不是违规。
5. 证据不足时输出 NEEDS_EVIDENCE / CONTESTED，不猜测。
6. 词汇纪律：failure domain ≠ blast radius（结构分区 vs 结果影响面）；write/state authority 用 V-003-D 义；consistency 必须带 V-010 义项后缀；backpressure ≠ load shedding ≠ admission control ≠ degradation（V-008 族）；flow control ≠ backpressure；service/component/container 承载架构语义时必须带语境限定（V-002 族）。
7. 本 Constitution 不强制：进程边界、single writer、任何遥测栈、service-local 准入/卸载、universal backward compatibility。

## Evaluation Axioms（AX，4 条）

### AX-001 Evaluation Relativity
架构评估只能相对 required properties（V-004-C）与 real constraints（V-004-D）进行；脱离二者的架构评价无判别力。Derived from: H1（Stage 4 demoted）。

### AX-002 Product-Contract Protection
实现困难不得静默削弱 product contract；真实冲突必须显式暴露为 trade-off 或升级决策。Derived from: H1 / 任务书 §22。

### AX-003 Contextual Non-Negotiables
当存在适用的、不可协商的监管/安全/安保/外部契约约束时，它们限定架构权衡空间。**语境限定（D-08 CONTEXTUAL ONLY）：不主张与域/产品无关的普适 safety floor。** Derived from: Stage 5 D-08。

### AX-004 Minimum Sufficient Complexity
目标是能安全保护 required properties 的最小复杂度；「简单」与「复杂」本身都不是目标。Derived from: H9（demoted meta-objective）。

（AX-005 已移入使用契约第 2 条；ID 不复用。）

## Mother Principles（promoted 10 条）

### MP-001 Explicit Ownership
- **Statement**: 运行时实体与可变状态的创建/修改/停止/清理必须有可回答的归属。
- **Mechanism**: 故障恢复与变更需要可定位的裁决者；归属悬空 → 泄漏/孤儿/陈旧覆盖。
- **Protects**: reliability, correctness, operability。
- **Applies When**: 存在并发执行、异步任务、可变状态或需清理资源。豁免仅限运行时托管的资源回收维度（managed-heap reclamation）；总量责任与写权裁决不豁免。
- **Derived from**: P-001（NARROW）。
- **Evidence status**: THEORETICAL + EMPIRICAL + CONTEXT_DEPENDENT；scope: 并发/异步/可变状态系统的归属义务，GC 证据仅限回收维度；concentration/gaps: 结构化并发 S-084..086 为同一概念谱系（CA4-10），OTP（S-114）为 scoped realization，RQ3-002（Java realization）open；Sources: S-084, S-085, S-086, S-114, S-091, S-062, S-116。
- **GOOD CASE**: supervised daemon 无限运行（S-114）；GC 托管堆 + runtime 软预算（S-116）。
- **Distinctions**: ≠ MP-008（状态裁决语义，D-06）；≠ MP-003（资源界限，D-07）；≠ MP-010（stale overwrite 归因规则，D-02）。

### MP-002 Change-Decision Boundaries
- **Statement**: 模块应按「可事前识别的、可能变化的设计决策」划分，易变决策隐藏在稳定接口后；边界仅在两侧变化规则确实不同时保护属性。
- **Mechanism**: 把可事前识别的易变决策隐藏在稳定边界后，可以减少该决策变化时必须同步修改的依赖单元；实际成本仍取决于修改性质、验证、协调与发布条件。
- **Protects**: evolvability, correctness。
- **Applies When**: 预期多次变更且变化轴可合理识别的系统；探索期未知变化轴时无边界合法。
- **Derived from**: P-002（NARROW）。
- **Evidence status**: THEORETICAL + EMPIRICAL；scope: 可识别变化轴存在的系统结构；concentration/gaps: Parnas 谱系（S-001/S-005 同族），S-109 为独立实证形态，S-112 platform-scoped；模块化大样本实证缺（RQ2 系谱注意）；Sources: S-001, S-005, S-012, S-109, S-112。
- **GOOD CASE**: 探索期原型无显式边界；性能轴上的刻意跨层调用。
- **Distinctions**: ≠「modularity is good」口号（变化轴不可识别时本原则主动不主张划分）；change amplification 仅为其 review signal（P-006 归宿，非原则）。D-01/D-03。

### MP-003 Bounded Execution
- **Statement**: system/service（运行时角色义，V-002-C 限定）/stream 的 lifetime 可以 indefinite；但相关时，per-work execution/wait/retention time、retry、queue、concurrency、memory、fan-out 等维度需要 effective bound 或 governed policy。
- **Mechanism**: L=λW——固定容量下超载转化为积压与级联超时；无界维度在负载/故障下以资源耗尽形式失效。
- **Protects**: reliability, latency, availability。
- **Applies When**: 共享资源、外部输入、异步工作、跨边界调用。隐含界（输入限定的批处理）与 runtime 软预算（GOMEMLIMIT 型）是合法形态。
- **Derived from**: P-003（NARROW）。
- **Evidence status**: THEORETICAL + EMPIRICAL + NORMATIVE；scope: Little's Law 支撑排队关系而非每个列举维度的全部主张；事故/平台契约均为维度特定证据；concentration/gaps: 容量设定方法论缺（Stage 5 residual）；Sources: S-072, S-073, S-048, S-050, S-052, S-090, S-059, S-061, S-062, S-065, S-088, S-113, S-116。
- **GOOD CASE**: lifetime indefinite 但 per-work 有界的 daemon/流；隐含界批处理；软预算托管堆。
- **Distinctions**: ≠ MP-009（超载时行为，D-04，peer）；取消/清理语义归 MP-001（D-07）。

### MP-004 Failure Containment by Scoped Propagation Boundaries
- **Statement**: 子系统的故障权力应与职责相称；隔离边界（failure domain：结构分区）按可接受影响范围设计，把故障后的 blast radius（结果影响面）遏制在其内。
- **Mechanism**: 故障沿共享资源与依赖传播；隔离切割传播图；防御机制若自耦合则成为放大器。
- **Protects**: availability, reliability。
- **Applies When**: 共享瓶颈、多租户、故障成本高的路径。隔离单元粒度是替代保证机制（进程边界/硬件虚拟化等，维度特定）与成本模型的函数，不默认进程边界；单进程单用户形态豁免。
- **Derived from**: P-004（SURVIVES）。
- **Evidence status**: EMPIRICAL + HEURISTIC + CONTEXT_DEPENDENT；scope: 共享资源/多租户形态的传播遏制；Arrakis 仅约束 I/O 保护维度（S-122）；concentration/gaps: 度量方法论 open（RQ5-001）；Sources: S-047, S-050, S-061, S-063, S-060, S-053, S-117, S-122。
- **GOOD CASE**: SQLite 单进程（S-117）；Arrakis 硬件下放（维度限定，S-122）。
- **Distinctions**: 与 MP-005 为 peer（D-05：故障传播 vs 信任/权限，机制独立）；blast radius ≠ failure domain。

### MP-005 Trust Minimization
- **Statement**: 在存在不可信输入、多权限级别、外部集成或 agent 动作执行权的边界上，信任与权限必须按职责最小化。
- **Mechanism**: 减少授予的 privilege/trust 会减少组件被攻破后攻击者可直接执行的动作集合，并限制 blast potential 的一个维度；这不构成总损害的硬上界。
- **Protects**: security, reliability。
- **Applies When**: 上述边界存在时；封闭单用户形态的进程内部不强制细分信任边界；不 universalize zero trust。
- **Derived from**: P-009（NARROW）。
- **Evidence status**: NORMATIVE + THEORETICAL + CONTEXT_DEPENDENT；scope: least-privilege 证据支持「直接可用动作集合缩小」，非总损害定理；平台示例保持 scoped；concentration/gaps: agent 形态时效（S-110 新近），capability 实例 open（RQ3-004）；Sources: S-092, S-093, S-096, S-110, S-112。
- **GOOD CASE**: 同团队单部署单元的内部粗粒度权限。
- **Distinctions**: 与 MP-004 为 peer（D-05）；capability（V-016-C）为机制非原则。

### MP-006 Obtainable Diagnostic Evidence
- **Statement**: 对未被更强静态保证消解的 operational questions（实际被证明且假设成立的问题除外），区分与归因相关运行时状态所需的证据必须由设计使其可获得。
- **Mechanism**: 证据的可获得性由信号/状态在边界与执行路径上的放置与保留决定；若区分相关运行时状态所需的信息既未被捕获，也无法由其他保留证据推导，则无法可靠完成后续归因。
- **Protects**: operability, reliability。
- **Applies When**: 持续运行/故障响应系统；深度受形态与成本约束（不是 instrument everything）。
- **Derived from**: P-007（NARROW，question-relative）。
- **Evidence status**: EMPIRICAL + NORMATIVE + CONTEXT_DEPENDENT；scope: 证据放置主张是 question-relative；厂商 observability 材料（S-055）非普适；seL4 只消解被证明且假设成立的问题（S-118）；concentration/gaps: 观测/隐私 trade-off 证据弱（RQ5-003）；Sources: S-048, S-049, S-055, S-058, S-053, S-062, S-118。
- **GOOD CASE**: seL4 型静态证明系统（假设集内）；DO-178C 式极简观测嵌入式。
- **Distinctions**: 无「静态证明越多观测越少」标量律；观测成本/隐私/安全为 trade-off。D-11。

### MP-007 Contract Preservation
- **Statement**: 存在 independent consumer 依赖的 contract（V-012-B）必须保持显式兼容方向（reader/writer 视角，V-013-A/B）与迁移路径；破兼容仅在更高优先级 security/correctness 要求或治理化协调迁移显式主导时合法。
- **Mechanism**: 契约是跨边界协作的稳定点；破坏契约把变更成本强转嫁给所有交互方。
- **Protects**: compatibility, evolvability, correctness。
- **Applies When**: 独立演进节奏的多方交互；内部紧协调接口的稳定性政策可合法不同（S-124）。
- **Derived from**: P-008（NARROW）。
- **Evidence status**: NORMATIVE + EMPIRICAL + CONTEXT_DEPENDENT；scope: 契约稳定性依赖独立消费方/治理存在；Linux 内部 API 是边界案例非普遍许可；concentration/gaps: 行为语义兼容可机检性 open；Sources: S-044, S-045, S-039, S-042, S-037, S-038, S-120, S-121, S-124。
- **GOOD CASE**: 治理化安全破除（S-120）；治理化生态演进（S-121）；Linux 内部不稳定 + syscall 稳定（S-124）。
- **Distinctions**: 不弱化为「兼容有时可破」；不强制 universal backward compatibility。

### MP-008 State Authority & Conflict Semantics
- **Statement**: 每类状态必须显式声明两个正交维度：write/state authority（V-003-D）与 conflict/consistency semantics（V-010 带义项后缀）；任一不清则并发/故障下状态结果不可判定。
- **Mechanism**: 无裁决规则 → 冲突无定义解（lost update / write skew）；副本与权威漂移；多写形态的合并语义必须显式。
- **Protects**: correctness, reliability。
- **Applies When**: 可变状态 +（并发写 或 多副本 或 缓存层）。single-writer 非必需（CRDT/显式合并语义合法）。
- **Derived from**: P-010（SURVIVES）。
- **Evidence status**: THEORETICAL + NORMATIVE + EMPIRICAL；scope: consistency 义项必须带后缀（V-010）；CRDT/local-first 证据支持显式多写合并语义（S-119/S-107）；concentration/gaps: cache 漂移量表述 open；RQ5-005（隔离名义 vs 实际）Stage 7 backlog；Sources: S-023, S-034, S-036, S-040, S-046, S-038, S-107, S-119。
- **GOOD CASE**: CRDT/local-first；append-only 无冲突域；只读派生视图。
- **Distinctions**: ≠ MP-001（D-06）；≠ MP-010（D-09）。D-14 FRAMEWORK HOLDS。

### MP-009 Governed Overload Boundary
- **Statement**: 当工作需求可能超过可用容量时，相关请求/工作路径必须在无控制的队列或资源增长之前遇到有效、受治理的容量边界。
- **Mechanism**: 无边界 → 到达率>服务率 → 积压失稳 → 重试放大 + 容量损失反馈环；恢复流量同样需要边界。
- **Protects**: availability, reliability。
- **Applies When**: 需求/工作可超过可用容量的路径；负载天然有界系统豁免（NEEDS_EVIDENCE 级 scope 注记，RQ5-004）。
- **机制区分（tactic-neutral）**: admission control = 决定工作是否进入/继续；rejection / load shedding = 拒绝或移除工作；backpressure = 将容量压力向上游传播；degradation = 在压力下主动降低功能/质量/成本。这些是相关机制/tactic，不是 alias，也不是所有系统都必须同时采用；选择与放置位置（服务/网关/mesh）取决于系统形态。**不要求 service-local 实现**。
- **Derived from**: P-012（NARROW）。
- **Evidence status**: EMPIRICAL + CONTEXT_DEPENDENT + NEEDS_EVIDENCE；scope: 厂商/SRE 谱系集中；网关/path 级控制合法；concentration/gaps: D-12（嵌入式准入）与负载有界豁免 open；Sources: S-048, S-049, S-050, S-052, S-090, S-061, S-065。
- **GOOD CASE**: 网关/path 级承担准入的服务；负载天然有界工具。
- **Distinctions**: ≠ MP-003（D-04，peer）；priority scheduling ≠ admission control（D-12 NEEDS_EVIDENCE）。

### MP-010 Execution-Model-Honest Correctness
- **Statement**: 正确性不得依赖执行模型未实际提供的时序/顺序/中断/取消/时钟保证；正确性关键保证必须由实际 primitive/contract/coordination semantics 强制。判别类：assumed guarantee ≠ model-provided guarantee——真实系统反复犯此类失配，并在扰动下产生具体失败模式。
- **Mechanism**: 隐式依赖不存在的保证，在调度扰动/延迟/重排序/取消/时钟行为下失效（Lamport 偏序；FLP 限定形式）。
- **Protects**: correctness。
- **Applies When**: 并发、异步、分布式、取消传播存在的系统。
- **Derived from**: P-013（SURVIVES + TAUTOLOGY_RISK——过 gate 依据：保留经验判别类与 GOOD CASE 边界；若未来被读成「正确系统依赖真实保证」则降级为 review/Constitution rule）。
- **Evidence status**: THEORETICAL + NORMATIVE + EMPIRICAL；scope: 形式结果为定理范围限定；平台保证为模型特定（S-115）；concentration/gaps: 保证机械判定 open（RQ5-002）；Sources: S-025, S-030, S-031, S-023, S-084, S-085, S-086, S-091, S-115。
- **GOOD CASE**: 模型真正保证的 per-pair 消息顺序、non-preemptive segments、具体 DBMS 承诺的隔离语义——不得误报。
- **Distinctions**: ≠ MP-008（D-09）；≠ MP-001（D-02 归因规则）。

（MP-011 RETIRED / NOT PROMOTED——category/abstraction error；tombstone 见 `reports/STAGE6_REDUCTION.md` §2；ID 永久保留不复用。MP-004 与 MP-005 为 peer，Stage 7 仅接收 `MP-004 RELATED_TO MP-005` 导航假设。）

## 非原则登记（不升格）

- P-006 Change Locality → MP-002 的 measurable property / review signal（change amplification）；Stage 7 metrics 层候选（若获批）。
- H7 locality → 未复活（D-13）。
- idempotency → explicit delivery semantics 下的 mechanism/tactic/contract property（MF-1）。
- USE/SLO/hedged requests/circuit breaker/event sourcing/strangler 等 → tactic/metric 层（Stage 7）。

## 残余不确定性（解释约束）

RQ5-001..005（全部 non-blocking）、RQ3-002/004、RQ2-006（USL）、RQ2-009（微服务正方证据）——见 `review-queue.yaml`；引用相关 MP 时这些缺口在场。
