# STAGE3_COLLISION_AUDIT — Independent Challenger Pass A (Terminology Collision Audit)

- **角色**: WorkBuddy (Independent Challenger, Research Mode / GLM 5.3)
- **分支**: `challenge/stage3-vocabulary`
- **审计基线（accepted corpus）**: main @ `a6b28f1`（PR #4 + PR #5 合入后：manifest v2 共 113 源、review-queue v2、sources S-001..S-113）
- **独立性声明**: 本 Pass A 未读取、未等待、未参考 `research/stage3-vocabulary` 上 Kimi 的任何 Stage 3 产出；未写竞争性 `02_VOCABULARY.md`；不进入 Stage 4；不修改 Primary corpus。
- **日期**: 2026-09-18
- **输入**: AGENTS.md（v2）、TASK.md（Stage 3）、canonical plan、`source-manifest.yaml`、`review-queue.yaml`、`sources/S-001..S-113`、Issue #6。

---

## 0. 方法

1. 通读 accepted corpus 的结构性文件（manifest/queue/index），深读约 45 份 S 笔记（覆盖全部 5 cluster + 全部欠代表形态 + Issue #6 全部 20 个 mandatory families 的证据落点）。
2. 对每个 family 提问两个方向：
   - **Over-normalization**：不同机制被压进同一个词？（→ 检查该词在各来源笔记中的实际用法是否互斥）
   - **Under-normalization**：同一机制被不同来源的标签拆散？（→ 检查跨来源是否存在互译关系而 corpus 未登记）
3. 只用 corpus 内证据（S-ID + 笔记原文），不引入外部记忆定义；厂商词只按其平台契约范围采信（承 Stage 2 claim-relative 纪律）。
4. 每条高风险 collision 附预注册检查（V3-*），供 Pass B 对 Kimi 固定 Stage 3 SHA 机器化对账。
5. 风险分级：P0 = 直接导致架构推理错误（含义互斥且高频）；P1 = 特定推理路径上导致错误；P2 = 导航/检索退化为主。

---

## 1. Mandatory families 覆盖矩阵（Issue #6 全 20 组）

| # | Family | 主要证据源 | 风险 | 对应 finding |
|---|---|---|---|---|
| 1 | architecture / design / structure / decision | S-004, S-005, S-007, S-009, S-010, S-020, S-021 | P1 | COL-O-04/OD-1 备注 |
| 2 | module / component / service / subsystem / boundary | S-001, S-012, S-016, S-109, S-112 | **P0** | COL-O-07, COL-U-08 |
| 3 | responsibility / ownership / lifecycle / authority | S-062, S-084..087, S-112 | **P0** | COL-O-04 |
| 4 | quality attribute / NFR / constraint | S-005, S-006, S-008 | P2 | 覆盖观察（§5 F-1） |
| 5 | availability / reliability / resilience / fault tolerance / failure isolation | S-047, S-048, S-050, S-057 | P2 | COL-O-11 |
| 6 | latency / throughput / utilization / saturation / scalability | S-071, S-072, S-077, S-087 | P2 | 覆盖观察（§5 F-2） |
| 7 | concurrency / parallelism / async / scheduling | S-080, S-086..089 | P2 | 覆盖观察（§5 F-3） |
| 8 | timeout / deadline / cancellation / retry / backoff / backpressure / load shedding | S-042, S-047, S-050, S-052, S-057, S-090 | **P0** | COL-U-02, COL-U-05 |
| 9 | state / source of truth / authority / consistency | S-012, S-040, S-100, S-105 | **P0** | COL-O-04, COL-U-03 |
| 10 | CAP consistency vs ACID consistency | S-023, S-026, S-027, RQ2-004 | **P0** | COL-O-01 |
| 11 | serializability / linearizability / isolation / durability | S-024, S-026, S-034, S-035 | **P0** | COL-O-02, COL-O-03 |
| 12 | API / interface / contract / protocol / compatibility | S-039, S-042, S-044, S-045, S-090 | P1 | COL-O-10, COL-O-19(REST) |
| 13 | backward/forward compatibility / migration / reversibility / evolvability | S-010, S-011, S-018, S-044, S-045 | P1 | COL-O-10 |
| 14 | coupling / cohesion / locality / change locality | S-001, S-018（无单一边界权威源） | P2 | 覆盖观察（§5 F-4） |
| 15 | observability / monitoring / telemetry / operability | S-048, S-055, S-058 | P1 | COL-O-05 |
| 16 | trust boundary / privilege / capability / authn / authz | S-092, S-093, S-096, S-112 | P1 | COL-O-04(安全支) |
| 17 | tactic / pattern / mechanism / principle / heuristic | S-005, S-047, S-050, S-092 | P1 | 覆盖观察（§5 F-5） |
| 18 | authority tier / evidence class / normative / empirical / theoretical | manifest schema 本身 | P1 | COL-O-04(元语言支), §5 F-6 |
| 19 | monolith / modular monolith / microservices / event-driven / local-first | S-011, S-040, S-107, S-108, S-109 | P1 | COL-U-08 |
| 20 | Agent / workflow / harness / tool / context / progressive disclosure | S-098..S-103, S-111, S-099 | **P0** | COL-O-08, COL-O-09, COL-U-07 |

20/20 覆盖。其中 4 个 family 定为 P0（8/9/10/11 实为一个大一致性语义场 + 2/3 的边界与授权语义场），是 Stage 3 词汇表最容易出错的地方。

---

## 2. 高风险 collisions — Over-normalization（不同概念被合并成一个词）

### COL-O-01 · consistency（CAP-C vs ACID-C vs 一致性光谱）— **P0**

- **terms involved**: consistency（CAP 语境）/ consistency（ACID 语境）/ consistency（DDIA 光谱：read committed → serializable → linearizable）/ eventual consistency
- **source evidence**: S-026（"其 consistency 是 linearizable 原子语义，与数据库 ACID 的 C 不同"，RQ2-004 CONTESTED）；S-027（BASE 澄清）；S-023（一致性光谱把隔离级别与线性一致性放进同一连续谱叙述）；S-035（Adya 广义理论）。
- **incompatible meanings**: CAP 的 C = 单对象线性一致性（原子寄存器）；ACID 的 C = 事务保持的不变量（应用级约束）；S-023 的光谱横跨**事务隔离**（多操作）与**副本一致性**（单对象多副本）两个正交轴。同一个词在 corpus 内至少承载三种互斥语义。
- **why this matters**: "这个系统是 consistent 的"——Expert 若不区分轴，会把隔离级别结论误用到副本语义（或反之）；CAP 引用必须携带 RQ2-004 限定，Stage 4 原则提取若引用裸词 "consistency" 会直接继承歧义。
- **recommended normalization**: 不设单一 `consistency` 词条；拆为 `consistency(replication)`（linearizable/eventual…，引 S-024/S-026）与 `consistency(transaction-invariant)`（引 S-032/S-034），光谱叙述保留为两轴对照图而非一维谱。`CONTESTED` 状态继承 RQ2-004。
- **preregistered check**: **V3-01** — `02_VOCABULARY.md` 中不得存在无 context-qualifier 的裸 `consistency` 主词条；CAP 相关词条必须链接 RQ2-004 与 S-026/S-027。

### COL-O-02 · atomicity（事务原子性 vs 原子对象/线性一致性）— **P0**

- **terms involved**: atomicity（事务 all-or-nothing）/ atomic（object/register，文献中作 linearizable 同义词）/ atomic operation
- **source evidence**: S-032（事务原子性 = all-or-nothing，跨多操作）；S-026（CAP consistency = "原子读/写寄存器语义"）；S-024（linearizability 原始定义，Herlihy & Wing 论文语境中 atomicity 即指单对象线性语义）。
- **incompatible meanings**: DB 语义：多操作事务的不可分性（abort 则全回滚）；分布式文献语义：单对象操作的线性顺序性。二者失败模式、证明方式、机制（undo log vs quorum 读写出现在同一时刻）完全不同。
- **why this matters**: "atomic" 是 Expert 推理中最常见的形容词之一；把 "atomic register" 读成 "事务原子的寄存器" 会产生错误的心智模型，反之亦然。S-024 与 S-032 同时在场使该冲突在 corpus 内部就是活的。
- **recommended normalization**: 两个词条：`atomicity(transaction)`（S-032/S-037）与 `atomic-consistency(=linearizability)` 作为 `linearizability` 的 **alias 并标注危险**（S-024）。禁止互相 alias。
- **preregistered check**: **V3-02** — `atomicity` 词条若存在，必须含两义拆分与 "do not conflate" 声明；`linearizability` 词条的 alias 表须含 `atomic consistency` 且标 non-synonym-warning。

### COL-O-03 · isolation（隔离级别 vs 故障隔离 vs actor 隔离）— **P1**

- **terms involved**: isolation（DB isolation levels）/ failure isolation / blast radius isolation / actor isolation（Swift）
- **source evidence**: S-034（ANSI 隔离级别批判）；S-047/S-050（failure isolation：bulkhead、cell、shuffle sharding）；S-086（"actor 隔离 + Sendable 静态消除数据竞争"）。
- **incompatible meanings**: 并发控制语义（事务间可见性）/ 故障传播控制（故障域物理分区）/ 数据竞争静态隔离（编译器 enforced）。三者都是"隔离"，机制对象分别为：操作交错、故障传播路径、内存访问。
- **why this matters**: 三者在不同 cluster 中都是高频推理材料；Expert 建议某处"加强隔离"时，必须知道自己在谈哪一个轴，否则会推荐错误机制（如用舱壁模式解决 write skew）。
- **recommended normalization**: 三个独立词条，共享 "isolation (disambiguation)" 导航页；互相标注 do-not-conflate。
- **preregistered check**: **V3-03** — 词汇表中 `isolation` 必须出现为消歧条目或带三个 context-qualified 子义；不允许单一义项。

### COL-O-04 · authority（四种权威/授权语义场）— **P0**

- **terms involved**: authority（安全：访问权/控制权）/ authoritative state / source of truth / authority tier（本项目元语言）/ ownership（组织权威）
- **source evidence**: S-092（least privilege 语境的权限）；S-093（Policy Administrator 控制权）；S-105（"单一可信来源 SSOT"）；S-040（"事件日志为 source of truth"）；S-100（"规格是 source of truth"）；S-016 C4（container 所有权）；manifest 元语言 `authority_tier`。
- **incompatible meanings**: ①安全域：谁有权执行/访问（S-092/093）；②状态域：哪份拷贝是权威副本（S-105/S-040/H11）；③证据域：来源的权威等级（manifest schema）；④组织域：哪个团队/进程拥有生命周期（S-112 main 进程是 "应用生命周期所有者"；S-084 scope 拥有子任务）。同一英文词在 corpus 四个层面高频出现。
- **why this matters**: H2b（Explicit Ownership）与 H11（Authoritative State）是两条候选母原则——如果 "authority" 不消歧，Stage 4 提取时 Ownership 原则会被状态权威证据"污染"，或安全权威例证被误用于状态原则。这是直接影响母原则推导路径的词汇碰撞。
- **recommended normalization**: 四词条：`authority(security)`、`authoritative-state`（与 COL-U-03 合并处理）、`source-authority`（元语言，见 F-6 建议独立 meta 节）、`ownership(lifecycle)`。
- **preregistered check**: **V3-04** — 不得存在合并多义项的单一 `authority` 词条；H2b/H11 相关词条的 source 引用必须按上述四域归类。

### COL-O-05 · observability / monitoring / telemetry — **P1**

- **terms involved**: observability / monitoring / telemetry / operability
- **source evidence**: S-055（monitoring=已知未知 vs observability=未知未知；**且争议栏登记 "observability 定义营销化"批评**，作者为 Honeycomb CTO）；S-048（SRE 用 monitoring 覆盖症状 vs 原因 + 四大黄金信号——SRE 语境下 monitoring ≈ 广义可观测实践）；S-058（OpenTelemetry = telemetry 数据管道标准，traces/metrics/logs 传输层）。
- **incompatible meanings**: Honeycomb 窄义（高基数探索性查询能力）vs SRE 宽义（监控体系总称）vs OTel 纯管道义（数据采集传输，不含查询/推断语义）。vendor 立场已在 corpus 登记（S-055 争议栏）。
- **why this matters**: "提升可观测性"的处方在三种语义下完全不同（加埋点 vs 加告警 vs 加查询能力）；Expert 若把 OTel 部署等同于获得 observability，属于典型推理错误。
- **recommended normalization**: 一词条三 context-qualified 义项 + 三源并引；Honeycomb 义项标注 vendor-scoped、营销化争议保留 `CONTESTED`。
- **preregistered check**: **V3-05** — observability 词条必须含三义项区分与 S-055 vendor 立场注记；telemetry（S-058）不得作为 observability 的 synonym。

### COL-O-06 · container（C4 抽象层 vs 部署容器）— **P2**

- **terms involved**: Container（C4 第二层）/ container（OS/部署单元）/ Component（C4 第三层）
- **source evidence**: S-016（C4：System Context → Container → Component → Code；container 定义为"独立运行单元如 SPA、服务端 API、数据库"）；S-050（cell-based/cell 语境的部署容器）；S-109（Shopify 组件边界）。
- **incompatible meanings**: C4 Container 是**绘图抽象**（可以是进程、可以是数据库，与 Docker 无关）；部署 container 是 OS 级隔离单元。C4 文档明示 "container ≠ Docker container"，但日常混用极高发，且 C4 Component（代码级模块）与一般 component 用法再叠一层歧义。
- **why this matters**: Expert 读 C4 图说 "6 个 containers" 与运维说 "6 个 containers" 数的是不同对象；审计/沟通类问题（RQ-C/RQ-D 导航）会错位。
- **recommended normalization**: `container(C4)` 与 `container(deployment)` 两词条互标 do-not-conflate；`component` 词条注明 C4 层级特指 vs 泛指模块两种用法。
- **preregistered check**: **V3-06** — C4 相关词条必须显式登记此二义警告。

### COL-O-07 · stateless（REST 无状态 vs LLM 调用无状态 vs 计算无状态）— **P2**

- **terms involved**: stateless（REST 约束）/ stateless（LLM 函数语义）/ stateless compute
- **source evidence**: S-039（REST stateless 约束：请求间服务端不保留会话）；S-103（"LLM 是无状态函数，输出质量几乎由输入质量决定"）；S-107（local-first 把状态权威移到端侧）。
- **incompatible meanings**: REST 的 stateless 是**协议层约束**（会话状态放客户端）；LLM 的 stateless 是**调用语义**（上下文必须随每次调用重传）；二者推导出的架构动作完全不同（会话外移 vs 上下文工程/状态重建）。
- **why this matters**: Agent Runtime 形态与 Web 形态的推理都会高频使用该词；混用会把 REST 的处方（会话外移）错误应用到 LLM 上下文管理（需要的恰是 context engineering，S-099）。
- **recommended normalization**: 两义项分立，各引其源；`context engineering` 词条（COL-O-09）与之交叉引用。
- **preregistered check**: **V3-07** — stateless 词条须含 REST/LLM 两义项区分。

### COL-O-08 · workflow（Agent workflow vs 业务工作流/长事务）— **P1**

- **terms involved**: workflow（Anthropic 语义：预定义代码路径）/ workflow（业务流程/Sagas activities）/ workflow engine
- **source evidence**: S-098（"区分 workflows（预定义代码路径）与 agents（LLM 动态指挥自身流程）"——**厂商定义**）；S-037/S-038（Sagas、Helland activities：跨实体业务流程）。
- **incompatible meanings**: Agent 域的 workflow 特指"LLM 编排里有固定控制流的形态"（与 agent 相对）；业务域的 workflow 指跨服务长流程（补偿、at-least-once）。一个 "workflow engine" 在两个世界是 Kafka/Temporal vs LangGraph 完全不同的东西。
- **why this matters**: RQ-D（agent 消费）与 RQ-B（状态/事务）都会引用 workflow；不区分会把补偿语义（S-037）错误挂到 agent workflow 模式（S-098）上。且 S-098 定义本身是 vendor-scoped（RQ2-008），必须显式继承。
- **recommended normalization**: `workflow(agent-orchestration)`（vendor-scoped，引 S-098）与 `workflow(business-process)`（引 S-037/S-038）分立。
- **preregistered check**: **V3-08** — 两义项分立；S-098 引用处必须携带 vendor 标注。

### COL-O-09 · context（DDD bounded context vs LLM context window vs context engineering）— **P1**

- **terms involved**: context（DDD）/ context window / context engineering / execution context
- **source evidence**: S-012（Bounded Context：模型一致性边界）；S-099（context engineering：token 集合策展、context rot、just-in-time context）；S-098（ACI 工具语境）。
- **incompatible meanings**: DDD 的 context 是**领域模型边界**；LLM 的 context 是**有限 token 窗口**；context engineering 是管理后者的工程实践。三者规模、机制、失败模式（边界外的术语不一致 vs context rot）完全不同。
- **why this matters**: 本项目自身用 "context" 描述知识加载（RQ-D / progressive disclosure），三种语义在最终 Prompt 里会同时出现——Expert 若不区分，会把 DDD 的 Context Map 处方错误用于 token 管理（或反之）。
- **recommended normalization**: 三词条；`bounded-context` 独立主词条（DDD 域高频），`context-window`/`context-engineering` 归 agent 域，互相 do-not-conflate。
- **preregistered check**: **V3-09** — 三者不得合并为单词条或互为 synonym。

### COL-O-10 · backward / forward compatibility 方向约定 — **P1**

- **terms involved**: BACKWARD compatibility（Schema Registry 语义）/ FORWARD compatibility / colloquial "backward compatible"
- **source evidence**: S-044（Confluent：BACKWARD（默认）= **新 schema 能读旧数据**；FORWARD = 旧 schema 能读新数据；+ TRANSITIVE 变体）；S-045（Protobuf field number 保留规则）。
- **incompatible meanings**: Schema Registry 的 BACKWARD 以 **reader 为锚**（新读者兼容旧数据）；口语 "backward compatible change" 通常以 **change/producer 为锚**（老客户端不受新变更影响）——两套方向定义恰好互为镜像。Protobuf 语境下兼容性又按 wire-format 规则而非语义规则判定。
- **why this matters**: 方向搞反 = 升级顺序推荐错误（这是会直接造成生产事故级别的推理错误）。S-044 是 H8（兼容性）的工业机制锚点，Stage 4 必然引用。
- **recommended normalization**: `schema-compatibility(BACKWARD/FORWARD/FULL)` 词条内显式给出方向定义（"谁读谁"句式）+ 与口语用法的映射表（口语→registry 语义的翻译规则），标 `CONTEXT_QUALIFIED`。
- **preregistered check**: **V3-10** — schema compatibility 词条必须含 "新 X 读旧 Y" 式方向定义；不得只用 "向后兼容" 一词带过。

### COL-O-11 · resilience（Reactive 属性 vs SRE 可靠性 vs Release It 稳定性）— **P2**

- **terms involved**: resilient（Reactive Manifesto）/ reliability（SRE）/ stability（Release It）
- **source evidence**: S-057（resilient 为 Reactive 四属性之一，宣言非学术来源——corpus 自己注明）；S-048（SRE reliability = SLO 达成度）；S-047（stability = 抗干扰能力，circuit breaker 等模式的靶属性）。
- **incompatible meanings**: Reactive：故障下仍保持响应（含隔离/复制/监督语义）；SRE：量化可靠性目标；Release It：生产稳定性（防级联/防崩溃）。重叠但不等同——例如 cron 单体批处理谈 resilience 几乎无 Reactive 语义。
- **why this matters**: "这个设计不够 resilient" 在三种语义下指向不同处方（加监督树 vs 调 SLO vs 加隔板）。
- **recommended normalization**: 三义项词条（或 stability 独立 + resilience 双义项），各引其源；保持 S-057 的非学术来源警告。
- **preregistered check**: **V3-11** — resilience 词条须含三来源义项区分；不得把 SRE SLO 语义并入 resilience 单义。

### COL-O-12 · performance（25010 performance efficiency vs 性能工程 vs 吞吐）— **P2**

- **terms involved**: performance efficiency（25010）/ performance（工程语境）/ scalability
- **source evidence**: S-008（25010 特性名 performance efficiency——标准语义，限定在产品质量特性框架）；S-070/S-071（Gregg：性能工程 = 延迟+吞吐+资源系统观）；S-087（JEP 444 明确 "目标不是更快而是更可扩展"——性能与可扩展性的区分实例）。
- **incompatible meanings**: 25010 的特性是**产品度量维度**；Gregg 的是**工程学科**；scalability 是**负载维度行为**。日常 "performance" 常被吞吐独占。
- **why this matters**: QA 评估（ATAM/S-006）用 25010 语言，性能诊断用 Gregg 语言；不区分会让 Expert 在评估语境开药方（类别错误）。
- **recommended normalization**: `performance-efficiency(25010)` 与 `performance-engineering` 分立；`scalability` 独立词条（Amdahl 族 S-074..079 是其证据组）。
- **preregistered check**: **V3-12** — 三者分立或单词条多义项；S-087 的 "不是更快而是更可扩展" 区分须被保留引用。

### COL-O-13 · REST（Fielding 语义 vs 工业口语语义）— **P1**

- **terms involved**: REST（Fielding：超媒体约束集）/ RESTful（工业口语：HTTP+JSON API）
- **source evidence**: S-039（corpus 明示 "多数自称 RESTful 的 API 不符合 Fielding 定义（缺 hypermedia）——Fielding 本人多次公开抱怨。引用 REST 须注明是 Fielding 语义还是工业口语语义"）。
- **incompatible meanings**: Fielding REST = 六约束体系（uniform interface 含 HATEOAS）；工业 RESTful = 远弱化的"HTTP 动词 + JSON"。判定 "这个 API 是否符合 REST" 在两种语义下结论相反。
- **why this matters**: 集成审计类问题（RQ-C）高频触发；Stage 4 若提取 "契约兼容" 类原则会引用 REST 作为风格锚点，语义漂移会传导进原则文本。
- **recommended normalization**: `REST(Fielding)` 主词条 + `RESTful(colloquial)` 作为 **非 synonym** 的相关词登记。
- **preregistered check**: **V3-13** — REST 词条必须携带 Fielding vs 口语双语义声明（S-039 原文要求）。

---

## 3. 高风险 collisions — Under-normalization（同一概念被拆散成多个标签）

### COL-U-01 · structured concurrency 的四个平台别名 — **P0**

- **terms involved**: nursery（Smith）/ CoroutineScope（Kotlin）/ task group & async-let（Swift）/ structured task scope + Virtual Threads（Java）
- **source evidence**: S-084（nursery，术语最早出自 Sústrik 2016，corpus 已登记）；S-085（CoroutineScope）；S-086（task group）；S-087（JEP 444 虚拟线程语境）。
- **fragmentation evidence**: 同一机制（子任务生命周期嵌套于父作用域、取消与完成以 scope 为界）在 corpus 四个来源里是四个标签；无任何一处登记互译关系。S-084 的 notes 已提示"可借官方文档背书化"，但别名映射本身不存在。
- **why this matters**: H2b（Ownership）/Lifecycle 域的核心证据组；若词汇表不统一，Expert 会把 Kotlin CoroutineScope 与 Swift TaskGroup 当作两种机制分别推理，跨平台比较类问题（RQ-A/RQ-C）直接失真。
- **recommended normalization**: 单一 `structured-concurrency` 主词条，四个平台名全部进 alias 表（各配 S-ID），机制定义以 S-084 为骨、S-085..087 为平台实例；`GlobalScope 逃逸舱`（S-085 备注）作为显式例外登记。
- **preregistered check**: **V3-14** — structured concurrency 词条必须存在且 alias 表含 nursery/CoroutineScope/task group/structured task scope 四项。

### COL-U-02 · backpressure / flow control / load shedding 边界 — **P0**

- **terms involved**: back-pressure（Reactive glossary）/ backpressure（Reactive Streams request(n)）/ flow control / load shedding / graceful degradation / fallback
- **source evidence**: S-057（宣言级定义："跨异步边界的流量控制"）；S-090（规范级：request(n) 需求信号，**"任一环节 unbounded buffer 即破功"**）；S-048（SRE Ch.21 处理过载：load shedding/降级）；S-050（Brooker：fallback 放大故障的风险 + 重试配额）；S-081（actor mailbox 无天然 backpressure——H3 已知弱点）。
- **fragmentation + 边界混淆 evidence**: 同一机制（下游向上游传导容量约束）有 backpressure/flow control 两个标签且 corpus 未互译；同时 load shedding（上游**丢弃**而非传导）与 backpressure 是**相反方向**的控制策略，日常语言常互换；fallback（S-050 警告放大故障）又与 graceful degradation 相邻。
- **why this matters**: 这是 family 8 的核心，也是 H3（有界执行）的主要机制组。把 load shedding 当 backpressure 的同义词，会让 Expert 在"下游已过载"场景推荐错误处方（传导压力 vs 主动卸载）；S-050 的 fallback 警告若与 degradation 混淆会丢掉 "fallback 有放大风险"的关键限定。
- **recommended normalization**: `backpressure` 主词条（S-057 定义 + S-090 机制 + S-081 反例），`flow-control` 为 alias；`load-shedding`、`graceful-degradation`、`fallback` 为**相邻非同义**词条，显式给对照（控制方向/丢弃语义/故障放大风险）。
- **preregistered check**: **V3-15** — backpressure 词条必须含 S-090 的 "全链路成立" 限定与 S-081 反例；load shedding 必须出现在 do-not-conflate；fallback 词条必须含 S-050 放大风险警告。

### COL-U-03 · source of truth 别名族 — **P1**

- **terms involved**: source of truth / SSOT（Android）/ authoritative state / system of record / 事件日志为真相源（ES）
- **source evidence**: S-105（Android 用 "single source of truth (SSOT)"，含 owner 语义："SSOT 是数据的 owner，只有它能修改"）；S-040（Event Sourcing："事件日志为 source of truth"）；S-100（Spec Kit："规格是 source of truth"——agent 域复用）；canonical plan H11（authoritative state）。
- **fragmentation evidence**: 四标签一概念（唯一权威可变副本），且 S-105 版本还把 ownership（COL-O-04④）织入定义；agent 域（S-100）的复用把词带进新形态。
- **why this matters**: H11 是候选母原则；若 SSOT/authoritative state/SoT 在词汇表散落，Stage 4 原则提取时证据召回不完整，且 S-105 的 owner 语义会让 H11 与 H2b 边界糊掉。
- **recommended normalization**: `source-of-truth` 主词条 + SSOT/system of record/authoritative state 进 alias；"owner 语义"单独一句标注为 Android 文档的平台表述（vendor-scoped），不并入通用定义。
- **preregistered check**: **V3-16** — source of truth 词条必须统一四别名；H11 相关引用可全部路由到单词条。

### COL-U-04 · retry storm / retry amplification — **P2**

- **terms involved**: retry storm（Azure 反模式名）/ retry amplification（SRE Ch.21/22 用语）/ 重试风暴
- **source evidence**: S-052（"Retry storm 反模式权威定义：客户端重试叠加放大服务端故障"）；S-048（"级联故障机制：retry amplification、capacity 损失反馈环"）。
- **fragmentation evidence**: 同一机制（重试正向反馈放大）微软叫 storm、Google 叫 amplification，corpus 两源并存未互译。
- **why this matters**: Failure Pattern 库（后续 stage）的条目去重与检索都依赖该统一；量级不大但属于"零成本修复"。
- **recommended normalization**: `retry-amplification`（或 storm）择一为主，另一个进 alias，双源并引。
- **preregistered check**: **V3-17** — 词汇表存在合并词条且同时引用 S-048/S-052。

### COL-U-05 · deadline / timeout / cancellation 三件套 — **P1**

- **terms involved**: timeout（单次操作时限）/ deadline（端到端时限）/ cancellation（取消传播 vs scope 取消）/ backoff（重试间隔策略）
- **source evidence**: S-042（gRPC：**deadline 传播 + cancellation 联动**——端到端语义的工业实例）；S-047（Release It：timeout 作为稳定性模式）；S-050（backoff with jitter + token bucket 重试配额）；S-085（scope 取消：CoroutineScope 取消则子协程全取消）；S-086/087（task group 取消；虚拟线程 interrupt）。
- **fragmentation evidence**: 五个来源覆盖同一"时间与取消控制"机制空间，但按来源族自然分簇（RPC 簇、稳定性簇、运行时簇），corpus 无统一导航。特别是 **deadline（绝对、传播）与 timeout（相对、局部）** 的区分只存在于 S-042 的字里行间。
- **why this matters**: H3（有界执行）的时间维度证据组。Expert 在"该在哪层设超时"类问题上，若不区分 per-call timeout 与 propagated deadline，会推荐出重复计时或计时真空的设计；cancellation 的两种语义（RPC 传播取消 vs 结构化 scope 取消）机制不同但常被合并叙述。
- **recommended normalization**: 词条族 `deadline(end-to-end)`、`timeout(operation)`、`cancellation(propagation)`、`cancellation(scope)`、`retry-backoff`；deadline/timeout 词条内给对照句（"deadline 是绝对时刻且随调用链传播；timeout 是相对时长且各跳独立"——依 S-042）。
- **preregistered check**: **V3-18** — deadline 与 timeout 必须分立词条且含传播性对照；cancellation 双语义显式。

### COL-U-06 · failure domain / blast radius / 故障域 — **P2**

- **terms involved**: failure domain（S-063 BGP 事故语境）/ blast radius（S-050 shuffled sharding/cell）/ failure isolation（S-047）
- **source evidence**: S-047（failure isolation 章法）；S-050（"限制 blast radius"）；S-063（failure-model 簇）。
- **fragmentation evidence**: 一概念三标签（故障影响的空间界），AWS 语系偏 blast radius，Nygard 语系偏 failure isolation，corpus 未互译。
- **why this matters**: H4（故障遏制）的证据召回与 Failure Pattern 库导航。
- **recommended normalization**: `failure-domain(blast-radius)` 合并词条，两标签互为 alias。
- **preregistered check**: **V3-19** — 别名登记存在。

### COL-U-07 · progressive disclosure vs just-in-time context — **P1**

- **terms involved**: progressive disclosure（本项目知识架构术语）/ just-in-time context（Anthropic）/ lazy loading（通用工程）
- **source evidence**: S-099（"just-in-time context：agent 持轻量引用运行时加载，替代前置全量加载"，corpus 注明"直接支撑本项目 Progressive Disclosure 设计"）；S-103（context engineering 优先原则）。
- **fragmentation evidence**: 本项目自身核心术语与厂商术语同义异名；词汇表若不同步登记，RQ-D 检索会漏掉 agent 域证据。
- **why this matters**: 这是知识工程主轴词——最终 Prompt、路由层、加载策略全部围绕它；检索失联会让 agent 在最关键的自描述概念上丢失证据链。
- **recommended normalization**: `progressive-disclosure` 主词条（项目定义）+ just-in-time context 为 agent 域 alias（vendor-scoped，S-099）；lazy loading 作为跨域弱关联（不 alias，机制近似但语境不同）。
- **preregistered check**: **V3-20** — progressive disclosure 词条的 alias 表含 just-in-time context 且标注 S-099 来源。

### COL-U-08 · monolith 家族的边界词（modular monolith 的 module ≠ Parnas module）— **P2**

- **terms involved**: monolith / modular monolith（组件边界）/ module（Parnas 语义）/ service（部署单元）/ outposts（DHH Citadel）
- **source evidence**: S-108（Citadel："99% 业务在中心单体，特殊运行时需求抽出为 outposts"）；S-109（"模块边界（组件化 + 公开 API + 依赖方向强制）在单体内实现；**部署单元 ≠ 组织/领域边界**"）；S-001（Parnas：按变化决策分解 module）。
- **fragmentation evidence**: Shopify 的 "module/component" 是**单体内强制边界**，与 Parnas 的信息隐藏 module、与部署级 service 三个层次都用同一批词；S-109 的关键区分（部署单元≠领域边界）已存在但散在单源内。
- **why this matters**: family 19 风格辩论的推理准确性：把 "modular monolith 的组件" 等同 "微服务"（因都叫 component/service）是最常见的风格级错误；S-109 区分是反教条证据组的一部分。
- **recommended normalization**: `modular-monolith` 词条显式收编 S-109 区分；`module(parnas)`、`module(in-process boundary)`、`service(deployment-unit)` 三个词条互标 context 差异。
- **preregistered check**: **V3-21** — modular monolith 词条含 "部署单元≠领域边界" 声明；module 词条含 Parnas 语义限定。

---

## 4. 汇总统计

- 详细登记 collisions：**21**（Over-normalization 13：P0×3、P1×7、P2×3；Under-normalization 8：P0×2、P1×3、P2×3）
- P0（直接推理错误级）：consistency 场（COL-O-01/O-02）、authority 四义（COL-O-04）、structured concurrency 别名（COL-U-01）、backpressure 边界（COL-U-02）
- 与 canonical plan 母原则假设的交叉：H2b/H11 ↔ COL-O-04；H3 ↔ COL-U-02/U-05；H4 ↔ COL-U-06；H5a/H8 ↔ COL-O-10；H7 ↔ family 14（见 F-4）

---

## 5. 覆盖观察（非 collision，供词汇表处理时参考）

- **F-1（family 4）**: quality attribute（S-005 六元组场景语义）vs NFR（工业惯用语）vs 25010 characteristic（S-008）。corpus 用 QA 为纲；建议词汇表以 `quality-attribute` 为主词条、NFR 为 alias 并注明 25010 术语差异（interaction capability/flexibility/safety 与传统 -ility 清单不一一对应）。
- **F-2（family 6）**: utilization/saturation 有 USE 方法的精确定义（S-071），latency vs tail latency（S-077）语义不同（平均值 vs p99）；建议词条区分。
- **F-3（family 7）**: virtual threads "concurrent but not parallel"（S-087）与 event loop 单线程并发（S-088）是 concurrency/parallelism 区分的两个最佳 corpus 内例证；建议词条引用。
- **F-4（family 14）**: coupling/coherence/change locality 在 corpus 中无单一权威源（S-001/S-018 分散）——词汇表可先立骨架词条标 `NEEDS_EVIDENCE`，不建议 Stage 3 内开采集（Issue #6 禁令）。
- **F-5（family 17）**: tactic（S-005，QA 手段）vs pattern（S-047，问题-解法叙述）vs mechanism（S-050，因果链）vs principle（S-092，设计准则）——四词在后续知识单元类型（Stage 4 P-* 文件、Failure Patterns、Playbooks）中是**结构标签**，词汇表必须给出项目内操作定义，否则单元分类会漂移。
- **F-6（family 18）**: manifest 元语言（authority tier / evidence class / normative / empirical）本身是被审计对象的一部分；建议 `02_VOCABULARY.md` 把这组词放进显式 **meta 节**（或独立小节）与领域词隔离——否则 "normative" 的平台契约义（S-101 verification_note 已在用）与标准规范义（S-008）会在同一文件内打架。这是 owner 决策（OD-1）。
- **F-7**: 中文别名的地位（灰度=canary、舱壁=bulkhead、绞杀者=strangler）：Stage 1 语言决策是中文行文+英文术语；词汇表 alias 是否收中文等价词影响检索，属 owner 政策（OD-4）。

---

## 6. 预注册检查清单（供 Pass B 对 Kimi 固定 Stage 3 SHA 机器化对账）

V3-01 consistency 裸词条禁令 + RQ2-004 链接
V3-02 atomicity 双义拆分 + atomic-consistency 危险 alias
V3-03 isolation 三义消歧
V3-04 authority 四域不合并
V3-05 observability/monitoring/telemetry 三义项 + vendor 注记
V3-06 C4 container 双义警告
V3-07 stateless REST/LLM 双义
V3-08 workflow(agent)/workflow(business) 分立 + vendor 标注
V3-09 context 三义不合并
V3-10 schema compatibility 方向定义（"谁读谁"句式）
V3-11 resilience 三源义项
V3-12 performance-efficiency / performance-engineering / scalability 分立
V3-13 REST 双语义声明
V3-14 structured concurrency 四平台 alias 齐全
V3-15 backpressure 全链路限定 + S-081 反例 + load shedding do-not-conflate + fallback 放大警告
V3-16 source of truth 四别名统一
V3-17 retry storm/amplification 合并双源
V3-18 deadline/timeout 传播性对照；cancellation 双语义
V3-19 failure domain/blast radius alias
V3-20 progressive disclosure ↔ just-in-time context alias
V3-21 modular monolith 部署单元≠领域边界声明
V3-22（通则）每个 vendor-defined 词条携带 scope 注记（承 RQ2-008）
V3-23（通则）tactic/pattern/mechanism/principle 存在项目内操作定义（F-5）
V3-24（通则）所有 CONTEXT_QUALIFIED/CONTESTED 词条状态保留，无人工升稳（Issue #6 验收红线）

---

## 7. 真正需要 owner 决策的问题

- **OD-1（元语言隔离）**: manifest 元语言（authority tier/evidence class/normative…）是否在 `02_VOCABULARY.md` 内设独立 meta 节与领域词隔离？（F-6；影响 COL-O-04③ 的处理位置）
- **OD-2（structured convergence 命名政策）**: 平台别名统一为 `structured concurrency` 主词条 + alias 表是否可接受？还是要求平台词条各自独立（检索更精确但碎片化）？（COL-U-01）
- **OD-3（中文别名政策）**: 词汇表 alias 是否收录中文等价词（灰度/canary、舱壁/bulkhead）？（F-7；牵动 RQ-D 检索设计与中英混合行文规范）
- **OD-4（母原则联动护栏）**: P0 级 collision（consistency/atomicity/authority）是否在 Stage 4 开工前作为**原则文本用词规范**（P-* 文件引用这些词时必须标注义项）写入 gate 条件？（防 Stage 4 把词汇歧义继承进原则文本）
- **OD-5（boundary 词的骨架策略）**: family 14（coupling/change locality）无权威源却与 H5b/H7 直接相关——接受词汇表骨架词条 + NEEDS_EVIDENCE 进入 Stage 4，还是先补源再立词？（Issue #6 禁止 Stage 3 内重开采集，补源即越界，需 owner 定例外与否）

---

## 8. 挑战者元声明

- 本审计在 Kimi `02_VOCABULARY.md` 不存在于本人上下文的前提下完成（`research/stage3-vocabulary` 分支内容未读取）；所有结论仅基于 accepted Stage 2 corpus（main@a6b28f1）与 Issue #6 任务书。
- 每个 collision 的 corpus evidence 均可回放（S-ID + 笔记小节）；厂商定义全部按 platform-scoped 采信，未采信任何通用化主张。
- 本文件是审计报告不是词汇表——不含 V-* 词条本体，不与 Primary 产物竞争。
