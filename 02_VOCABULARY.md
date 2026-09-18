---
id: VOCABULARY
type: vocabulary
stage: 3
status: proposed-v2
author: kimi-k3 (Primary Researcher / Vocabulary Synthesizer)
branch: research/stage3-vocabulary
date: 2026-09-18
remediated: 2026-09-18
remediation_basis: "Issue #6 CA adjudication R-1..R-11 + Origin 规则；challenge/stage3-codex-glm@7465d82"
issue: 6
evidence_baseline: "Stage 2 accepted corpus (source-manifest.yaml, S-001..S-113)"
---
# 02_VOCABULARY — 架构词汇归一（v2，含 remediation）

## 使用契约（先于所有词条）

1. 本词汇表从 Stage 2 accepted corpus 的证据归一而来，不从泛化记忆定义术语。每个词条挂 source IDs。
2. **同一词在不同权威来源含义不同时，不强行统一**——用 `Context-specific meanings` 做 context qualification。禁止静默多义。
3. Status 取值：`STABLE` / `CONTEXT_QUALIFIED`（同一词有多个合法但不同的含义，使用时必须带限定）/ `CONTESTED` / `NEEDS_EVIDENCE`。
4. Vendor/platform 术语只在自身 scope 内是 normative；跨栈使用必须重新论证。
5. 本表不是百科全书：只收录会实质影响架构推理、导航、评测或后续原则提取的术语。
6. Stage 3 不提取 Mother Principles；`Working definition` 是词汇级工作定义，不是原则表述。
7. **Origin 规则**（每个词条的词义来源必须可判别）：
   - 默认 `Origin: SOURCE_NORMALIZED`——定义可回放到所挂 source IDs，不逐条标注；
   - `Origin: PROJECT_DEFINED`——项目工作定义/约定，来源无此词条，显式标注；
   - `Origin: PROJECT_META`——本项目证据/知识管理的元语言，显式标注。

## 导航

| 族 | 主题 |
|---|---|
| V-001 | architecture / design / structure / decision |
| V-002 | module / component / service / subsystem / boundary |
| V-003 | responsibility / ownership / lifecycle / authority |
| V-004 | quality attribute / NFR / required property / constraint |
| V-005 | availability / reliability / resilience / fault tolerance / failure isolation |
| V-006 | latency / throughput / utilization / saturation / scalability / performance |
| V-007 | concurrency / parallelism / async / scheduling / structured concurrency |
| V-008 | timeout / deadline / cancellation / retry / backoff / backpressure / load shedding |
| V-009 | state / source of truth / authority / consistency |
| V-010 | consistency 的多义性（CAP vs ACID vs 口语） |
| V-011 | serializability / linearizability / isolation / durability / atomicity |
| V-012 | API / interface / contract / protocol / compatibility |
| V-013 | backward/forward compat / migration / reversibility / evolvability |
| V-014 | coupling / cohesion / locality / change locality |
| V-015 | observability / monitoring / telemetry / operability |
| V-016 | trust boundary / privilege / capability / authn / authz |
| V-017 | tactic / pattern / mechanism / principle / heuristic（项目元术语） |
| V-018 | authority tier / evidence class / normative / empirical / theoretical（证据元语言） |
| V-019 | monolith / modular monolith / microservices / event-driven / local-first |
| V-020 | agent / workflow / harness / tool / context / progressive disclosure |
| V-021 | 补充词条（blast radius / idempotency / unboundedness / event loop / fallback / strangler / expand-contract / stateless） |

---

## V-001 族：architecture / design / structure / decision

### V-001-A architecture
- Working definition: 系统推理所需的结构集合——软件元素、元素间关系、两者属性（SAIP 定义）；等价地，{elements, form, rationale}（Perry & Wolf）。
- Aliases / accepted synonyms: 体系结构（中文标准译法）。
- Do not conflate with: design（见下）、UML 图、技术选型清单、目录结构。
- Context-specific meanings:
  - SAIP/SEI 语境：结构 + 质量属性承载 + 商业资产（ABC 环）。
  - ISO 42010 语境：实体在其环境中的基础概念/属性 + 实现与演化的治理原则。
  - Fowler/Johnson 语境：「重要的、难以改变的决策」——重要性由变更成本度量（该定义有自知明的循环性）。
- Status: CONTEXT_QUALIFIED（三个权威定义强调不同侧面，可互补使用，但引用时必须指明谱系）
- Source IDs: S-005, S-007, S-009, S-010, S-020

### V-001-B design（相对 architecture）
- Origin: PROJECT_DEFINED
- Working definition: 本项目内约定——design 指不改变系统级结构/边界/所有权关系的决策；architecture 指改变这些的决策。该区分是工作约定而非来源规定。
- Do not conflate with: architecture（同上）；visual design。
- Status: CONTEXT_QUALIFIED（边界本身在来源间模糊；ATAM 视角下二者连续而非二元）
- Source IDs: S-005, S-006

### V-001-C structure
- Working definition: 元素 + 关系 + 属性的静态描述；是 architecture 的可观察部分，不含 rationale。
- Do not conflate with: 文件目录结构（目录结构本身不是架构证据）。
- Status: STABLE
- Source IDs: S-005, S-004

### V-001-D (architecture) decision
- Working definition: 针对一组 forces 做出的、影响系统结构/属性的一次选择；rationale 与被否决的替代方案是其一等组成部分。
- Aliases: ADR 记录的对象。
- Do not conflate with: ADR 文档格式本身（格式是载体，决策是内容）。
- Status: STABLE
- Source IDs: S-021, S-014, S-009

---

## V-002 族：module / component / service / subsystem / boundary

### V-002-A module
- Working definition: 按「可能变化的设计决策」划分的、隐藏内部实现并暴露稳定接口的代码级单元（Parnas 语义）。
- Do not conflate with: component（见下）、service（见下）、package（构建粒度）。
- Status: STABLE（Parnas 语义）；注意「模块化」收益缺乏大样本实证
- Source IDs: S-001

### V-002-B component
- Working definition: 可替换的单元（可替换性是唯一跨语境成立的核）。**是否可独立部署取决于语境，不是 component 的固有属性。**
- Context-specific meanings:
  - C4 语境：container 内的代码级分组——**不可独立部署**（C4 中可部署的单位是 container，不是 component）。
  - SAIP/UML 语境：运行时元素，可独立替换/部署。
  - 前端框架语境（React 等）：UI 组件——纯平台术语，无部署语义。
- Do not conflate with: container（C4 中 container 是可运行/可部署的抽象层；Docker 语境 container 是 OS 级隔离部署单元——两个「container」也不同义，引用时必须带 C4 或 OS 限定）。
- Status: CONTEXT_QUALIFIED
- Source IDs: S-016, S-005

### V-002-C service
- Working definition（限定语境）: **在 distributed / service-architecture 语境下**：独立部署、经网络契约通信的运行时单元。
- Context-specific meanings:
  - 分布式/服务架构语境：如上（单源 S-023，注意该定义带有服务架构的前设）。
  - 单进程/应用内部语境：「service 层」「internal service」是代码组织称谓，不含网络/独立部署语义。
  - OS 平台语境：daemon/OS service——纯平台术语。
- Do not conflate with: microservice（V-019-C，风格标签不是尺寸描述）。
- Status: CONTEXT_QUALIFIED（bare service 一词不带限定时不允许作架构断言）
- Source IDs: S-023

### V-002-D subsystem
- Working definition: 系统内具有内聚职责的部分；粒度约定俗成，无跨来源统一定义。
- Status: CONTEXT_QUALIFIED（使用时必须自带粒度说明）
- Source IDs: S-005

### V-002-E boundary
- Working definition: 两侧变化/故障/信任/所有权规则不同的分界线。
- Context-specific meanings: 模块边界（Parnas 信息隐藏面）；进程/服务边界（运行时隔离面）；bounded context（DDD 模型一致性边界）；trust boundary（STRIDE 威胁建模的安全语义边界）。**四类边界机制不同，禁止混用「划清边界」一语带过。**
- Status: CONTEXT_QUALIFIED（本项目最高危多义词之一）
- Source IDs: S-001, S-012, S-096, S-112

---

## V-003 族：responsibility / ownership / lifecycle / authority

### V-003-A ownership（运行时所有权）
- Working definition: 对某运行时实体（进程/线程/worker/timer/queue/socket/任务）或某份可变状态，谁创建、谁可修改、谁停止、谁清理的可回答性。
- Do not conflate with: 代码所有权的组织含义（CODEOWNERS）；数据管辖权。
- Status: STABLE（结构化并发来源 S-084..086 提供机制证据；另见 V-007-E）
- Source IDs: S-084, S-085, S-086, S-091

### V-003-B lifecycle
- Working definition: 实体从创建到销毁的状态机，含崩溃/重启/孤儿化路径。
- Do not conflate with: SDLC（流程术语）。
- Status: STABLE
- Source IDs: S-062, S-091

### V-003-C responsibility
- Working definition: 一个单元「被允许且被要求做什么」的职责范围；是划分 ownership 与 boundary 的依据，不等于它们。
- Status: STABLE
- Source IDs: S-001, S-005

### V-003-D authority（状态权威）
- Working definition: 对某状态「谁的可写副本是裁决者」的规定；与 source of truth（V-009-B）同族，authority 强调写权归属。
- Do not conflate with: authorization（安全术语，V-016-E）；authority tier（元语言，V-018-A）。
- Status: CONTEXT_QUALIFIED（中英混用时极易与安全 authority 混淆，使用须带「状态」限定）
- Source IDs: S-023, S-046

---

## V-004 族：quality attribute / NFR / required property / constraint

### V-004-A quality attribute (QA)
- Working definition: 系统的可度量质量特性；必须用 stimulus-response 场景六元组精确化，拒绝模糊形容词。
- Aliases: NFR（见下）、质量属性。
- Do not conflate with: feature；形容词式需求（「高性能」「高可用」不是 QA 表述）。
- Status: STABLE（SEI/SAIP 语义）；与 ISO 25010 特性树的映射是 Stage 4+ 任务
- Source IDs: S-005, S-006, S-008

### V-004-B NFR (non-functional requirement)
- Working definition: 工业口语中 ≈ QA；注意「non-functional」措辞被批评为误导（QA 影响功能是否可用）。
- Status: CONTEXT_QUALIFIED（口语可用，正式推理用 QA + 场景）
- Source IDs: S-005, S-008

### V-004-C required property
- Origin: PROJECT_DEFINED
- Working definition: 本项目工作术语——产品契约要求系统必须保护的属性（capability/correctness/latency/security…）；是 QA 与 product intent 的交集。
- Status: CONTEXT_QUALIFIED（项目内造词，用于 ARCH_CONFLICT 判定；外部来源无此词条）
- Source IDs: （项目定义；锚 S-005 QA + 任务书 §22）

### V-004-D constraint
- Working definition: 不可由架构师选择的前提（法规/平台/成本/兼容承诺）。
- Do not conflate with: requirement（可选中权衡）；preference。
- Status: STABLE
- Source IDs: S-006, S-022

---

## V-005 族：availability / reliability / resilience / fault tolerance / failure isolation

### V-005-A availability
- Working definition: 系统处于可服务状态的时间/请求比例（可度量：uptime、成功请求率）。
- Do not conflate with: reliability（见下）。
- Status: STABLE
- Source IDs: S-048, S-023

### V-005-B reliability
- Working definition: 在给定条件与时间内持续正确执行功能的能力（含正确性维度，不只 uptime）。
- Context-specific meanings: ISO 25010:2023 中 reliability 为独立特性族；SRE 语境用 SLI/SLO 操作化。
- Status: CONTEXT_QUALIFIED（ISO 与 SRE 操作化路径不同但都合法）
- Source IDs: S-008, S-048, S-049

### V-005-C resilience
- Working definition: 扰动/故障下维持可接受服务并恢复的能力（强调降级与恢复行为，而非免故障）。
- Do not conflate with: fault tolerance（见下）。**注意：corpus 无来源支撑 resilience 与 fault tolerance 之间存在全局强弱排序；二者是 failure-model-relative 的不同能力描述，有重叠但不构成全序。**
- Status: STABLE；Reactive Manifesto 语境有特定用法
- Source IDs: S-057, S-047, S-048

### V-005-D fault tolerance
- Working definition: 针对指定故障模型（failures 的类型与数量假设）继续服务不中断的能力（如副本接管）；能力的强弱完全相对于所声明的故障模型。
- Do not conflate with: resilience（扰动下降级+恢复）。二者重叠（都关乎故障下行为），但不存在「fault tolerance 全局强于 resilience」的排序——是否更强取决于故障模型与服务水平定义。
- Status: STABLE
- Source IDs: S-023

### V-005-E failure isolation / blast radius / containment
- Working definition: 限制故障传播范围的结构属性；blast radius 是其度量（受影响面）。failure domain 是静态分区结构，blast radius 是动态结果度量，二者不是同义词。
- Aliases: fault containment。bulkhead 是 tactic 不是属性。
- Status: STABLE
- Source IDs: S-047, S-050, S-061

---

## V-006 族：latency / throughput / utilization / saturation / scalability / performance

### V-006-A latency
- Working definition: 单个操作的完成时间；必须以分布（p50/p95/p99）表述，平均值掩盖排队效应。
- Status: STABLE
- Source IDs: S-070, S-077

### V-006-B throughput
- Working definition: 单位时间完成工作量；与 latency 经排队效应耦合，不可独立优化（L=λW）。
- Status: STABLE
- Source IDs: S-072, S-073

### V-006-C utilization / saturation
- Working definition: utilization = 资源忙的时间比例；saturation = 资源排队/超载程度（队列长度、调度延迟）。USE method 三要素之二（第三为 errors）。
- Do not conflate with: 100% utilization ≠ 饱和；饱和可在低利用率下由突发造成。
- Status: STABLE
- Source IDs: S-070, S-071

### V-006-D scalability
- Working definition: 负载增长时维持所需属性的能力；必须说明 scaling 维度（请求/用户/数据/租户）与成本曲线。**Scalability 改进不等于单任务更快**——虚拟线程的目标「不是更快而是更可扩展」是其最清晰的官方表述（S-087）。
- Do not conflate with: 「能加机器」（Gustafson 修正）；并发度提升（V-007-A）；单操作延迟改善。
- Status: STABLE
- Source IDs: S-074, S-075, S-076, S-087, S-079（NEEDS_EVIDENCE）

### V-006-E performance
- Working definition: latency/throughput/resource-efficiency 的总称；单独说「性能好/差」不构成架构陈述。
- Context-specific meanings: ISO 25010:2023 中特性名为 performance efficiency（独立特性族，与本族词条映射属 Stage 4+ 任务）。
- Status: CONTEXT_QUALIFIED（泛称，推理时必须落到 A–D 的具体量）
- Source IDs: S-070, S-008

---

## V-007 族：concurrency / parallelism / asynchronous / scheduling / structured concurrency

### V-007-A concurrency
- Working definition: 多个任务的执行区间可重叠的结构属性（单核也可成立）。
- Do not conflate with: parallelism（同时物理执行，需多核/多机）。
- Status: STABLE
- Source IDs: S-080, S-081, S-087

### V-007-B asynchronous execution
- Working definition: 发起方不等待完成即可继续的执行方式；是机制选择，不隐含性能或可靠性优劣。
- Do not conflate with: 「async 天然更好」（本项目明令禁止的教条）；消息驱动架构风格。
- Status: STABLE
- Source IDs: S-088, S-089

### V-007-C scheduling
- Working definition: 谁决定何时何地执行哪段工作（OS 调度器、事件循环、executor、RTOS 调度器）。
- Context-specific meanings: 协作式（事件循环/coroutine 挂起点让出）vs 抢占式（RTOS/OS 线程）——取消与阻塞语义完全不同。
- Status: CONTEXT_QUALIFIED
- Source IDs: S-086, S-089, S-113, S-091

### V-007-D execution context / runtime unit（工作词条）
- Origin: PROJECT_DEFINED
- Working definition: 执行的最小可归属单位（process/thread/task/coroutine/actor）；RQ-C 推理的基本粒子。
- Status: CONTEXT_QUALIFIED（项目工作词条；各 runtime 术语不同，引用时映射到具体机制）
- Source IDs: S-080..S-091

### V-007-E structured concurrency
- Working definition: 一种并发组织原则与运行时机制族：**子任务不得比父作用域活得更久**；作用域（nursery/scope）退出前所有子任务必须完成或被取消并 await；应由运行时强制而非程序员自律。
- Platform realizations / related constructs（不是机械 alias——各平台语义细节不同，引用时按平台）：
  - nursery（Trio/Smith 论述，S-084）；
  - Kotlin CoroutineScope / structured scope semantics（S-085）；
  - Swift task group / async-let（S-086）。
- Do not conflate with:
  - **Java Virtual Threads（S-087）不是 structured concurrency 的同义词**——JEP 444 解决的是轻量线程可扩展性；Java 生态对应的结构化并发机制是 StructuredTaskScope（JEP 453+ 预览系列），corpus 未收录其官方文档 → NEEDS_EVIDENCE（review-queue RQ3-002）。
  - 全局后台 worker / fire-and-forget 守护任务：需显式脱离 scope，不能用 structured concurrency 一刀切。
- Status: STABLE（原则层，S-084 纲领 + S-085/S-086 官方采纳背书）；Java 侧 NEEDS_EVIDENCE
- Source IDs: S-084, S-085, S-086

---

## V-008 族：timeout / deadline / cancellation / retry / backoff / backpressure / load shedding

### V-008-A timeout
- Working definition: 单次操作的最长等待。缺少 timeout 不必然等于无界——**只有当缺少任何有效时间界（timeout、deadline、配额、上游取消等）时，操作才 potentially unbounded**。
- Do not conflate with: deadline（跨多跳端到端剩余预算，见下）。
- Status: STABLE
- Source IDs: S-050, S-047, S-042

### V-008-B deadline
- Working definition: 跨调用链传播的端到端时间预算（gRPC deadline propagation 为其平台 normative 实例）。
- Status: CONTEXT_QUALIFIED（通用概念 STABLE；具体传播语义是平台 normative）
- Source IDs: S-042

### V-008-C cancellation
- Working definition: 中止进行中工作的信号及其传播。两种语义必须区分：
  - **RPC/dependency cancellation propagation**：跨进程调用链的取消/截止时间传播（S-042 gRPC 语境，平台 normative）；
  - **structured-scope cancellation**：进程内结构化作用域的协作式取消——scope 取消则子任务全部取消，代码在挂起点响应（S-084..086 语境）。
- Do not conflate with: timeout（触发源之一）；kill（强制终止，无清理机会）。
- Status: STABLE（双语义分立后）
- Source IDs: S-084, S-085, S-086, S-042

### V-008-D retry / backoff
- Working definition: retry = 失败后重发；backoff = 重试间隔策略（指数+抖动）；无限重试 = 无界性；叠加重试 = retry amplification → retry storm。
- Status: STABLE；retry storm 有官方反模式定义（S-052）
- Source IDs: S-050, S-052, S-048

### V-008-E backpressure
- Working definition: 下游向上游显式传递处理能力的流量控制机制（Reactive Streams request(n) 为规范级实例）。**backpressure 只在全链路各环节都实现时才成立——任一环节 unbounded buffer 即破功**（S-090）。
- Do not conflate with:
  - load shedding（V-008-F）：backpressure 是能力信号向**上游传导**，load shedding 是入口**主动拒绝/卸载**——方向相反，机制不同，可互补；
  - flow control：related term 而非精确 alias——flow control 外延更宽（含 TCP 流控等非显式能力信号机制）；
  - 「队列满了再说」：隐式、无界缓冲等价物。
- Counterexample（机制缺席的形态）: actor 模型不天然提供 backpressure——mailbox 可无限增长（S-081）；引入 actor 形态时必须另行回答有界性问题。
- Status: STABLE
- Source IDs: S-090, S-057, S-081

### V-008-F load shedding / overload handling
- Working definition: 过载时按优先级/临界度主动拒绝或降级工作（SRE Ch.21；client-side throttling、criticality 分级）。
- Do not conflate with: backpressure（见 V-008-E 方向对照）；被动崩溃；fail-fast。
- Status: STABLE
- Source IDs: S-048, S-050

---

## V-009 族：state / source of truth / authority / consistency

### V-009-A state
- Working definition: 影响未来行为的已存信息；架构上必须回答：在哪、谁拥有、谁可写、生命周期、一致性要求。
- Do not conflate with: data（流转中的信息）；cache（派生、可丢弃的 state 副本）。
- Status: STABLE
- Source IDs: S-023

### V-009-B source of truth
- Working definition: 某类信息的权威版本所在；其他副本的合法性由其与该权威的关系定义。
- Related variants（**不是 exact synonyms**，各有差异注记）：
  - SSOT (single source of truth)：平台文档常用表述；Android 官方语境中 SSOT 织入 owner 语义（数据持有方即修改入口）——vendor-scoped（S-105），不得外推为通用定义；
  - system of record：企业数据管理谱系的相近概念（corpus 未收录专门来源，作 related term 登记）；
  - authoritative state：V-003-D 的状态权威表述，强调写权归属。
- Context-specific meanings: event sourcing 语境（事件日志为 SoT，状态为回放投影）；local-first 语境（主副本在用户设备）；Kafka/Log 语境（append-only log 为集成层 SoT）。
- Status: CONTEXT_QUALIFIED
- Source IDs: S-040, S-046, S-107, S-105

### V-009-C consistency（族内多义，另见 V-010）
- 见 V-010（专族处理，本项目最高危术语冲突之一）。
- Source IDs: S-026, S-024, S-034

---

## V-010 族：consistency 多义性（强制 context qualification）

### V-010-A consistency（必须带限定使用）
- Working definition: **不存在无语境的 consistency 定义。** 使用时必须后缀：
  - `consistency (ACID)`：事务把数据库从一个满足 invariant 的状态带到另一个（应用级不变量，C 属于应用）。
  - `consistency (CAP)`：Gilbert & Lynch 形式化中的 atomic/linearizable 单对象语义。
  - `consistency (replica)`：多副本读到的值的一致程度（strong/eventual 光谱）。
  - `consistency (cache)`：缓存与 SoT 的漂移程度。
- Do not conflate with: 以上四种互不相同；ACID 的 C 与 CAP 的 C 混用是教科书级错误（关联 review-queue RQ2-004）。
- Status: CONTEXT_QUALIFIED（强制）
- Source IDs: S-026, S-027, S-024, S-033, S-034
- Review linkage: RQ2-004

---

## V-011 族：serializability / linearizability / isolation / durability / atomicity

### V-011-A serializability
- Working definition: 并发事务的执行等价于某个串行顺序（多对象、多操作的 transactional 语义）。
- Do not conflate with: linearizability（单对象实时序）；ANSI SERIALIZABLE 隔离级别名（Berenson 证明其与真可串行化不等价）。
- Status: STABLE；引用 ANSI 级别名时必须带 Berenson 限定
- Source IDs: S-034, S-033, S-023

### V-011-B linearizability
- Working definition: 单对象操作在调用与响应之间某点生效（实时序约束）；可组合（locality——注意此为 Herlihy-Wing 专用义，与 V-014-C 禁止互借）。
- Dangerous alias warning: 历史文献中 linearizability 曾被称为 `atomic consistency` / `atomic`（CAP 原文即用 atomic 语义）。**该称呼是 linearizability 的 context-specific 历史术语，禁止与 transaction atomicity（V-011-E）混淆。**
- Status: STABLE
- Source IDs: S-024, S-023, S-026

### V-011-C isolation (transaction)
- Working definition: 事务间互不可见性的级别光谱（read committed → snapshot isolation → serializable）；snapshot isolation 允许 write skew。
- Do not conflate with: failure isolation（V-005-E，故障维度）；进程隔离。
- Status: STABLE；但「isolation」单独出现必须带事务限定
- Source IDs: S-034, S-035, S-036

### V-011-D durability
- Working definition: 已提交结果在故障后仍存活（写入持久介质/足够副本）。
- Status: STABLE
- Source IDs: S-032, S-033

### V-011-E atomicity（强制消歧）
- Working definition: **不存在无语境的 atomicity。**
  - `atomicity (transaction)`：事务的全有或全无性——要么全部生效要么全部不生效（Gray 事务概念，S-032/S-033）。
  - `atomic (consistency)`：linearizability 的历史/context-specific 称呼（V-011-B；CAP 原文语义）。
- Do not conflate with: 两种语义互不蕴含——事务原子性不保证实时序，线性一致不保证多操作全有或全无。
- Status: CONTEXT_QUALIFIED（强制）
- Source IDs: S-032, S-033, S-024, S-026

---

## V-012 族：API / interface / contract / protocol / compatibility

### V-012-A interface
- Working definition: 跨边界调用的表面（签名/消息/事件形状）。
- Status: STABLE
- Source IDs: S-001

### V-012-B contract
- Working definition: interface + 行为语义 + 非功能承诺（时序、错误模型、幂等、顺序、兼容规则）的总和；schema 只是 contract 的一部分。
- Status: CONTEXT_QUALIFIED（工业口语常把 schema 当 contract，推理时必须包含语义部分）
- Source IDs: S-039, S-042, S-044

### V-012-C protocol
- Working definition: 消息交换的规则（格式、顺序、状态机）；HTTP/2、gRPC、Reactive Streams 均为协议层实例。
- Do not conflate with: API（协议上的一次暴露面）。
- Status: STABLE
- Source IDs: S-042, S-090

### V-012-D compatibility
- Working definition: 变更后既有交互方仍可工作的性质；方向分类见 V-013-A/B。
- Status: STABLE
- Source IDs: S-044, S-045

### V-012-E API
- Working definition: 可编程调用的 contract 暴露面。
- Do not conflate with: REST（Fielding 语义 vs 口语「RESTful」，见 N-7）。
- Status: STABLE
- Source IDs: S-039, S-042

---

## V-013 族：backward/forward compat / migration / reversibility / evolvability

### V-013-A backward compatible
- Working definition: **reader/writer（或 producer/consumer）视角下的方向属性**：新 reader 能读旧 writer 产生的数据 / 新版本接受旧版本调用（schema registry normative：新代码读旧数据）。**使用该词必须显式标注谁读谁（reader/writer 或 producer/consumer 视角）。**
- Status: CONTEXT_QUALIFIED（方向定义以 S-044 为准；不同生态存在方向表述相反的历史用法，引用须核对视角）
- Source IDs: S-044, S-045

### V-013-B forward compatible
- Working definition: 旧 reader 能容忍新 writer 产生的数据/调用（unknown fields 转发等）。同样必须带 reader/writer 视角。
- Status: CONTEXT_QUALIFIED
- Source IDs: S-044, S-045

### V-013-C migration
- Working definition: 系统/数据/接口从旧形态到新形态的受控过渡。渐进迁移的 tactic 家族见 V-021-F/G（注意：Strangler 与 expand-contract 是不同 tactic，证据支撑不同）。
- Status: STABLE
- Source IDs: S-044

### V-013-D reversibility
- Working definition: 决策可被撤销/改变的代价高低（Type 1/2 决策语义）；影响该投入的论证深度与承诺时机。
- Status: CONTEXT_QUALIFIED（Fowler「难改变的决策」与可逆性框架相关但不同源）
- Source IDs: S-010, S-018

### V-013-E evolvability
- Working definition: 系统低成本适应未来变化的能力；fitness function 是其可执行守护形式。
- Do not conflate with: 「多用可扩展接口」（把未来猜测预埋为复杂度是反模式）。
- Status: STABLE
- Source IDs: S-018, S-010

---

## V-014 族：coupling / cohesion / locality / change locality

### V-014-A coupling
- Working definition: 单元间相互依赖的程度与种类（数据/控制/时序/部署/组织）。
- Do not conflate with: 「有依赖」——耦合的架构问题是变化/故障沿依赖传播，不是依赖存在本身。
- Status: STABLE（注意：coupling/change-locality 的专门权威来源未收录，review-queue RQ3-001；当前锚定 SAIP 谱系）
- Source IDs: S-005, S-023

### V-014-B cohesion
- Working definition: 单元内部件为同一职责服务的程度。
- Status: STABLE
- Source IDs: S-005

### V-014-C locality（推理/变更/数据/故障的距离成本）
- Working definition: 推理成本、变更成本、数据移动成本、故障传播随「距离」（跨模块/进程/机器/组织边界数）增长的一般倾向。
- Status: CONTEXT_QUALIFIED（是多种机制的共同倾向而非单一机制；Stage 4 需拆分检验——Stage 4 hypothesis，词汇层只作骨架）
- Source IDs: S-001, S-024（locality 在 Herlihy-Wing 有完全不同的专用含义=可组合性，禁止混淆）

### V-014-D change amplification
- Working definition: 一次概念变更迫使多处代码/配置/部署变更的现象；change locality 的反面度量。
- Status: STABLE（权威专门来源同 RQ3-001）
- Source IDs: S-001, S-005

---

## V-015 族：observability / monitoring / telemetry / operability

### V-015-A monitoring
- Working definition: 对已知故障模式的预设检查与告警（已知未知）。
- Status: STABLE
- Source IDs: S-048

### V-015-B observability
- Working definition: 从外部输出推断内部状态任意问题的能力（未知未知）；高基数/宽事件为其工程形态。
- Do not conflate with: monitoring（子集）；「装了 OTel」（工具不等于能力）。
- Status: CONTEXT_QUALIFIED（Majors 定义带厂商立场批评；SRE 语境不强调此区分——两谱系都合法）
- Source IDs: S-055, S-048, S-058

### V-015-C telemetry
- Working definition: traces/metrics/logs 信号的产生与传输（OTel 三信号）。
- Status: STABLE
- Source IDs: S-058

### V-015-D operability
- Working definition: 系统被安全运维的难易（部署、回滚、扩容、诊断、恢复）。
- Status: STABLE
- Source IDs: S-047, S-049

---

## V-016 族：trust boundary / privilege / capability / authn / authz

### V-016-A trust boundary
- Working definition: 两侧信任级别不同的分界线；威胁建模（STRIDE/DFD）的核心原语。
- Do not conflate with: 网络边界（零信任明确否定网络位置=信任）；V-002-E 的其他边界类型。
- Status: STABLE
- Source IDs: S-096, S-093

### V-016-B privilege / least privilege
- Working definition: 执行任务所需的权限；least privilege = 只持有必需的最小集（Saltzer & Schroeder 原始八原则之一）。
- Status: STABLE
- Source IDs: S-092

### V-016-C capability（安全语义）
- Working definition: 不可伪造的、将权限与对象指定合一的令牌式授权单元；capability-based security。
- Do not conflate with: 业务能力（business capability）。
- Status: NEEDS_EVIDENCE（原则层锚 S-092；WASI/component-model 公开实例未收录——review-queue RQ3-004）
- Source IDs: S-092

### V-016-D authentication / authorization
- Working definition: authn = 是谁；authz = 能做什么。
- Status: STABLE
- Source IDs: S-093, S-095

---

## V-017 族：tactic / pattern / mechanism / principle / heuristic（项目元术语）

（全族 Origin: PROJECT_META——本项目知识工程的操作定义，不要求外部来源有相同词条；其中 tactic/pattern 与 SAIP/PLoP 谱系兼容。）

### V-017-A principle
- Origin: PROJECT_META
- Working definition: 跨场景的因果主张：某结构在 mechanism 上保护某属性；有适用边界与反例。
- Do not conflate with: best practice（无机制论证的惯例）、law（只有 Little's Law 等有形式证明的才可称 law）。
- Status: STABLE
- Source IDs: 任务书 §15/§17；锚 S-005（tactics 体系）

### V-017-B tactic
- Origin: PROJECT_META
- Working definition: 实现某质量属性响应的具体设计决策（SAIP 语义：QA tactic）；circuit breaker、cache、worker 都是 tactic 不是 principle。
- Status: STABLE
- Source IDs: S-005, S-047

### V-017-C pattern
- Origin: PROJECT_META
- Working definition: 带语境的可复用解决方案形式；pattern 不是合规性标签。
- Status: STABLE
- Source IDs: S-004

### V-017-D mechanism
- Origin: PROJECT_META
- Working definition: 因果链条的可指认环节（谁阻塞谁、谁放大故障）；「因为 best practice」不构成 mechanism。
- Status: STABLE
- Source IDs: 任务书 §15

### V-017-E heuristic
- Origin: PROJECT_META
- Working definition: 经验法则；有效的 heuristic 不是普适定律（本项目证据纪律的核心句）。
- Status: STABLE
- Source IDs: 任务书 §11

---

## V-018 族：authority tier / evidence class / normative / empirical / theoretical（证据元语言）

（全族 Origin: PROJECT_META——本项目证据管理的元语言，与领域词隔离（OD-1）。）

### V-018-A authority tier
- Origin: PROJECT_META
- Working definition: 来源出处的权威分级（A/B/C）；是**来源属性**。
- Status: STABLE
- Source IDs: 任务书 §8；source-manifest.yaml

### V-018-B evidence class
- Origin: PROJECT_META
- Working definition: 证据性质分级（normative/empirical/theoretical/heuristic/contested/context_dependent）；是**主张属性**（claim-relative，CA 决议修正：同一来源对不同主张可属不同 class）。
- Do not conflate with: authority tier（来源权威 ≠ 主张证据性质；厂商文档对自身平台契约是 normative，对通用架构主张不是）。
- Status: STABLE
- Source IDs: Issue #3 CA decision；manifest

### V-018-C normative
- Origin: PROJECT_META
- Working definition: 定义某事物应当如何的规范性内容（标准、官方契约）。Scope 限定是其合法性的组成部分。
- Status: STABLE
- Source IDs: 同上

### V-018-D empirical
- Origin: PROJECT_META
- Working definition: 来自观察/生产实践的证据（postmortem、SRE 实践、测量研究）。
- Status: STABLE
- Source IDs: 同上

### V-018-E theoretical
- Origin: PROJECT_META
- Working definition: 来自形式化定义/证明/模型的证据（CAP、FLP、Little's Law、linearizability）。
- Status: STABLE
- Source IDs: 同上

---

## V-019 族：架构风格标签（全部 CONTEXT_DEPENDENT）

### V-019-A monolith
- Working definition: 单部署单元的应用形态。
- Status: CONTEXT_QUALIFIED（中性描述词；「单体=落后」为被 corpus 否证的教条）
- Source IDs: S-108, S-109

### V-019-B modular monolith
- Working definition: 单体内强制模块边界（组件化+公开 API+依赖方向强制）的形态（Shopify 实证）。**部署单元 ≠ 领域/组织边界**（S-109）：模块化是代码与职责的划分，不以拆分部署单元为前提。
- Status: CONTEXT_QUALIFIED
- Source IDs: S-109

### V-019-C microservices
- Working definition: 细粒度独立部署服务族形态；**corpus 目前只有反方一手论证，正方一手论证缺失（RQ2-009，NEEDS_EVIDENCE）**——引用微服务收益主张时此缺口必须在场。
- Status: CONTESTED
- Source IDs: S-108, S-109（反方）；RQ2-009

### V-019-D event-driven / EDA
- Working definition: 以事件为首要集成机制的形态。
- Do not conflate with: event sourcing（持久化策略，S-040）——二者常搭配但独立。
- Status: CONTEXT_QUALIFIED
- Source IDs: S-040, S-041

### V-019-E local-first
- Working definition: 数据主副本在用户设备、云端仅同步的形态（Ink & Switch 七属性）。
- Status: STABLE（术语原始出处明确）
- Source IDs: S-107

---

## V-020 族：agent / workflow / harness / tool / context / progressive disclosure

### V-020-A agent
- Working definition: LLM 动态指挥自身流程与工具使用的系统（Anthropic 定义）；与 workflow（预定义代码路径编排）区分。
- Status: CONTEXT_QUALIFIED（厂商工程语义，S-098；vendor evidence 纪律适用）
- Source IDs: S-098, S-102

### V-020-B workflow
- Working definition: 两个语境必须区分：
  - `workflow (agent-orchestration)`：预定义代码路径编排 LLM 调用的系统（Anthropic 语义，S-098）。
  - `workflow (business-process)`：跨实体长事务的业务流程状态跟踪——Helland 的 activities、Saga 的补偿事务链（S-037/S-038）。
- Do not conflate with: 两种语境互不提供机制；BPM 口语另属。
- Status: CONTEXT_QUALIFIED
- Source IDs: S-098, S-037, S-038

### V-020-C harness
- Origin: PROJECT_DEFINED
- Working definition: 包裹模型的执行环境：工具装配、上下文组织、停止条件、证据验证与执行闭环。
- Status: CONTEXT_QUALIFIED（任务书 §2.4 工作定义；厂商材料中用法不一）
- Source IDs: 任务书；S-102, S-103

### V-020-D context（工程语义）
- Working definition: 模型可见 token 集合的策展对象；「context rot」指 token 增长导致性能下降。
- Do not conflate with: bounded context（DDD）；execution context（V-007-D）；「上下文」口语。
- Status: CONTEXT_QUALIFIED
- Source IDs: S-099

### V-020-E progressive disclosure
- Origin: PROJECT_DEFINED
- Working definition: 按需逐层加载知识（router → index → 原子文件 → 证据），目标是 minimum sufficient context；just-in-time context 为其运行时实例（S-099）。
- Status: CONTEXT_QUALIFIED（项目方法论词 + 厂商术语汇合）
- Source IDs: 任务书 §2.3；S-099

### V-020-F guardrail
- Working definition: 输入/输出/工具各阶段的验证执行点（OpenAI SDK 语义）；harness 层信任边界机制。
- Status: CONTEXT_QUALIFIED（平台 normative；通用化需论证）
- Source IDs: S-102, S-110

---

## V-021 补充词条（最小集之外、实质影响推理）

### V-021-A blast radius
- Working definition: 单一故障/变更/操作可影响的最大范围；failure isolation（V-005-E）的度量（与 failure domain 的区分见 V-005-E）。
- Status: STABLE
- Source IDs: S-050, S-061, S-063

### V-021-B idempotency
- Working definition: 同一操作重复执行的效果等价于执行一次；at-least-once 交付下接收方正确性的前提。
- Status: STABLE
- Source IDs: S-038, S-043

### V-021-C unboundedness（无界性，工作词条）
- Origin: PROJECT_DEFINED
- Working definition: 时间/空间/并发/重试/积压/扇出任一维度缺少可说明上限的状态；corpus 中多数 failure pattern 的共同机制特征。
- Status: CONTEXT_QUALIFIED（项目工作词条；Stage 4 需检验其解释力）
- Source IDs: S-048, S-050, S-052, S-059, S-088, S-090

### V-021-D event loop / main thread 约束
- Working definition: 单线程事件分发模型下「每个回调工作量必须小」的运行时契约。
- Status: CONTEXT_QUALIFIED（Node 文档对其运行时 normative；UI 主线程形态同构但来源未收录——review-queue RQ3-005）
- Source IDs: S-088, S-089

### V-021-E fallback
- Working definition: 主路径失败时的替代路径；AWS 警告 fallback 自身可放大故障（失败时两条路径同时承压）。
- Status: STABLE
- Source IDs: S-050

### V-021-F strangler (fig)
- Working definition: 渐进迁移 tactic：在旧系统边缘逐步生长新系统直至旧系统被移除；反对大爆炸重写。原始出处 Fowler 2004（不是 Greg Young——RQ2-007）。
- Status: STABLE
- Source IDs: S-011

### V-021-G expand-contract
- Working definition: 渐进迁移 tactic：接口/schema 先扩展（新旧并存）再收缩（移除旧）的变更路径。
- Status: NEEDS_EVIDENCE（corpus 内无一手出处；S-011 只覆盖 Strangler，不得再被引用于本词条；S-044 兼容性方向语义仅为相邻支撑。一手出处核验见 review-queue RQ3-006）
- Source IDs: （无——待补）

### V-021-H stateless（强制消歧）
- Working definition: **不存在无语境的 stateless。**
  - `stateless (REST)`：请求自包含、会话状态不留服务端（Fielding 约束之一，S-039）——是「会话状态外移」的架构处方。
  - `stateless (LLM-call)`：模型调用是无状态函数，输出质量几乎由输入质量决定，上下文随调用重传（S-103）——是「context engineering 优先」的论据。
- Do not conflate with: 两义禁止互借机制——REST 处方不能用于 LLM 上下文管理（后者恰恰需要显式策展与重传上下文）。
- Status: CONTEXT_QUALIFIED（强制）
- Source IDs: S-039, S-103

---

## 归一裁决登记（跨来源冲突的显式处理）

| # | 冲突 | 裁决 | 状态 |
|---|---|---|---|
| N-1 | consistency 四义（ACID/CAP/replica/cache） | 强制后缀限定（V-010）+ RQ2-004 链接 | CONTEXT_QUALIFIED |
| N-2 | serializability vs linearizability vs ANSI 级别名 | V-011-A/B 分开；ANSI 名引用带 Berenson 限定 | STABLE+限定 |
| N-3 | architecture 三谱系定义（SAIP/42010/Fowler-Johnson） | 并存，引用指明谱系 | CONTEXT_QUALIFIED |
| N-4 | boundary 四类（模块/进程/模型/信任） | 使用时必须指明类型 | CONTEXT_QUALIFIED |
| N-5 | isolation 事务义 vs 故障义 vs 进程义 | 单独出现必须带限定 | CONTEXT_QUALIFIED |
| N-6 | observability 两谱系（SRE vs Majors） | 并存；厂商立场已标 | CONTEXT_QUALIFIED |
| N-7 | REST Fielding 语义 vs 工业口语 | 引用 REST 必须注明语义 | CONTESTED（事实层无争议，工业实践层持续混用） |
| N-8 | locality 通用倾向 vs Herlihy-Wing 专用义（可组合性） | 禁止互借 | CONTEXT_QUALIFIED |
| N-9 | microservices 收益主张 | 正方一手证据缺失，引用时缺口必须在场 | CONTESTED / NEEDS_EVIDENCE (RQ2-009) |
| N-10 | 「quality in use」与产品质量模型（ISO 25010:2023 拆分 25019） | 本项目只锚定产品质量模型 | STABLE（scope 裁决） |
| N-11 | atomicity 双义（transaction vs CAP atomic consistency） | 强制后缀（V-011-E）；atomic consistency 仅作 linearizability 历史术语 | CONTEXT_QUALIFIED |
| N-12 | stateless 双义（REST vs LLM-call） | 强制后缀（V-021-H）；机制禁止互借 | CONTEXT_QUALIFIED |
| N-13 | resilience vs fault tolerance 排序 | 无全序；failure-model-relative（V-005-C/D） | STABLE（无源排序断言已移除） |
| N-14 | container 双义（C4 可部署抽象 vs Docker OS 隔离单元） | 引用必须带 C4 或 OS 限定（V-002-B 注记） | CONTEXT_QUALIFIED |
| N-15 | workflow 双义（agent-orchestration vs business-process） | 强制后缀（V-020-B） | CONTEXT_QUALIFIED |
