---
id: PLAN-STAGE1
type: research-plan
stage: 1
status: proposed
author: kimi
branch: eval/stage1-kimi
date: 2026-09-17
---

# Stage 1 — Research Plan：通用软件架构师能力蒸馏

本文件是 Stage 1 的唯一产物。它规划「如何研究」，不包含任何已收集的来源内容、不包含候选原则正文、不包含 System Prompt。Stage 2（Source Collection）在本计划经人工评审通过前不得启动。

---

## 0. 研究立场声明（先于一切规划）

本研究对被研究对象持有三条元立场，后续所有阶段受它们约束：

1. **Architecture 是保护机制，不是表达形式。** 研究问题永远是「这条原则/模式在保护什么系统属性、在什么约束下成立」，而不是「业界主流怎么做」。
2. **假设先行，证伪跟进。** 任务书 §4 的六个候选母原则在本计划中一律记为 Hypothesis（H1–H6），而非结论。Stage 4–6 的存在意义是尝试杀死它们。
3. **Context > Pattern。** 任何「X 优于 Y」形式的结论默认标记为 `CONTEXT_DEPENDENT`，直到能给出适用边界与反例。

---

## 1. Research Questions

按「母问题 → 子问题 → 可证伪形式」组织。RQ-0 是全部研究的锚点。

### RQ-0（母问题）：What makes an architecture good?

- RQ-0.1 「好架构」可否归约为一组 ≤20 条、跨技术栈的母原则？
  - 证伪形式：找到一个真实架构失败案例，它能造成重大损失，但无法被候选母原则集合中的任何一条解释 → 集合不完备。
  - 反向证伪：找到两条候选原则在所有测试案例上永远同真同假 → 应合并。
- RQ-0.2 是否存在不属于六候选的母原则？（开放搜索，不允许用六候选做过滤网。）
- RQ-0.3 「好」是相对 Required System Properties + Constraints 而言，还是存在与产品目标无关的绝对架构品质？
  - 预设立场：前者。此立场本身也须在 Stage 5 接受反例检验（例如：安全下限是否与产品意图无关？）。

### RQ-1：Architecture 究竟在保护什么？（边界定义）

- RQ-1.1 任务书 §5 候选集合 {Capability, Correctness, Quality Attributes, Constraints, Boundaries, Ownership, Execution, State, Resources, Failure, Trust, Change, Operability} 是否构成最小充分集？
- RQ-1.2 给出一个能在 §5 列出的 12 类系统形态（Desktop / Web FE / Mobile / Backend / Monolith / Distributed / DB-heavy / DevTool / Local AI Tool / Cloud / Embedded / AI Agent Runtime）上同时成立的 Architecture Definition。
  - 检验方式：任取一类形态，若定义在该形态上退化为空话或错误，则定义失败。

### RQ-2：系统模型的最小充分维度

- RQ-2.1 §6 的 12 个 System Model（Purpose/Boundary/Execution/Ownership/State/DataFlow/ControlFlow/Resource/Failure/Trust/Deployment/Evolution）中，哪些是所有系统必须的，哪些只在特定形态下 relevant？
- RQ-2.2 每个 System Model 的「最小可回答集」是什么？（Agent 在 context 受限时，每个模型最少需要回答哪几个问题即可支撑推理？）→ 此问题直接决定 Progressive Disclosure 的粒度。

### RQ-3：Failure 的先验结构

- RQ-3.1 §16 的 18 个 Failure Patterns 能否由少量「无界性 / 所有权缺失 / 隔离缺失 / 时序假设错误」类机制推导出来？若能，Failure Pattern 库应是推导结果而非独立罗列。
- RQ-3.2 「Local correctness, global wrongness」的形式化：哪些属性是局部的、哪些是涌现的，评审时如何用有限证据逼近全局判断？

### RQ-4：Trade-off 推理的可操作化

- RQ-4.1 ATAM / Quality Attribute Scenarios 的方法论中，哪些部分可被 Agent 在无人工工作坊的情况下可靠执行？哪些必须升级给人？
- RQ-4.2 「Minimum Necessary Architecture」如何判定「必要」？需要给出可检验的判定程序，而不是审美判断。
- RQ-4.3 Type 1 / Type 2 决策（可逆性）与「决策延迟」的量化或半量化处理方式。

### RQ-5：证据与置信度

- RQ-5.1 §21 的五级证据分类（CONFIRMED → PERSONAL PREFERENCE）是否充分？评审 Agent 在只有静态代码证据时，能合法得出的最高置信度是哪一级？
- RQ-5.2 不同事实类型的权威来源优先级（§2.5：current behavior / product intent / architecture intent / historical reason）能否推广为通用规则？

### RQ-6：产品契约保护

- RQ-6.1 「Implementation constraints must not silently redefine the product contract」如何操作化？即：Agent 如何区分「实现困难」与「根本性冲突」？（输出物为 §23 ARCH_CONFLICT 的触发判据。）

### RQ-7：Agent 消费性

- RQ-7.1 何种知识组织粒度（文件大小、frontmatter 字段、关系图密度）在真实 Agent context 预算下表现最好？此问题在 Stage 10 的 eval 中用「路由准确率 / 平均加载文件数」实测，而非 Stage 1 凭空决定。

---

## 2. Knowledge Domains

研究覆盖域 = 任务书 §7 的 18 域，不增不减。但对每个域预先登记三件事：**研究目标（该域要产出什么判断方法）、预期母原则挂钩、主要证伪方向**。摘要表（全文见各域研究笔记模板，Stage 2 起用）：

| # | 域 | 核心研究目标 | 预期挂钩假设 | 主要证伪方向 |
|---|---|---|---|---|
| 7.1 | Fundamentals（模块化/信息隐藏/耦合内聚） | 抽象的成本何时超过收益 | H2 边界、H5 可演进 | Parnas 信息隐藏在现代 IDE/微服务下的反例 |
| 7.2 | Quality Attributes | QAS/ATAM 的 Agent 可操作化 | 全部 | QAS 是否在小型系统上过度重 |
| 7.3 | Runtime/Execution | 「Where does this run」的系统化追问 | H3 有界执行 | 纯函数式/无运行时系统的适用性 |
| 7.4 | Concurrency | 区分并发正确性与并发性能 | H3 | 无共享状态架构是否免疫 |
| 7.5 | Performance | 排队效应与尾延迟的先验判断 | H3 | Little/Amdahl 的适用前提与误用 |
| 7.6 | Resource Budgets | Boundedness 思维的操作化清单 | H3 | 探索性/批处理系统是否需要全程有界 |
| 7.7 | Failure Model | 失败传播路径的推导方法 | H4 故障遏制 | fail-fast 在长尾依赖下的反效果 |
| 7.8 | Failure Isolation | 验证「子系统故障权力 ≤ 责任」候选原则 | H4 | 共享资源的经济性反驳 |
| 7.9 | Distributed Systems | 先判定「这是否真是分布式问题」 | H4/H3 | 单机系统误套 CAP 类推理的识别 |
| 7.10 | State/Data | State Ownership 与 Source of Truth 的判定程序 | H2 | 事件溯源/QRS 的复杂度代价 |
| 7.11 | API/Integration | 契约/版本/幂等/背压的最小检查集 | H2/H3 | 内部接口是否需要同等严格 |
| 7.12 | Lifecycle/Ownership | 孤儿资源与 stale work 的系统性追问 | H2（最高优先级域） | GC 语言中所有权问题是否真的消失 |
| 7.13 | Security | 架构级安全风险的识别边界（不替代审计） | 独立属性 Trust | least privilege 与可用性的张力 |
| 7.14 | Observability | 验证「不可观测即不可运维」 | H6 | 高观测成本场景（嵌入式/边缘） |
| 7.15 | Scalability | O(N²) 与全局串行点的先验识别 | H3 | 规模永远很小的系统是否无需考虑 |
| 7.16 | Evolvability | 渐进演进路径优于重写的判定 | H5 | 何时重写反而更便宜 |
| 7.17 | Decision Making | ADR/可逆性/选项价值的操作化 | 全部（元域） | ADR 在快速原型期的成本 |
| 7.18 | Communication | 「最小准确表达」的判定标准 | H6 | C4 等视图方法的重度问题 |

域间显式关系（如 7.4↔7.5↔7.7）在 `relationship-map.yaml`（Stage 7）中落地，Stage 1 只登记「预期存在强耦合」的域对：(7.3,7.4)、(7.4,7.5)、(7.5,7.15)、(7.7,7.8)、(7.10,7.9)、(7.6,7.5)。

---

## 3. Candidate Primary Sources

只列候选清单与选择理由，**不展开内容**。最终 manifest 在 Stage 2 构建。标记 = 预期 Tier（§8）。

### 3.1 架构基础与元理论

- Parnas, "On the Criteria to Be Used in Decomposing Systems into Modules" (1972) — A
- Brooks, *The Mythical Man-Month* + "No Silver Bullet"（essential/accidental complexity）— A
- Bass/Clements/Kazman, *Software Architecture in Practice*（QAS、ATAM、tactics 原始定义）— A
- SEI ATAM 原始技术报告 — A
- ISO/IEC 25010（质量属性模型）— A
- Shaw & Garlan, *Software Architecture: Perspectives on an Emerging Discipline* — A/B
- Fowler：架构相关 essays（作为 B 级综合视角，不作母原则唯一依据）— B
- Evans DDD（限界上下文部分）— B
- Robert C. Martin *Clean Architecture*（**预登记为教条风险来源**：研究其机制而非其结论）— B/CONTESTED 候选

### 3.2 系统与分布式

- Kleppmann, *Designing Data-Intensive Applications* — A（教材级综合）
- Lamport 原始论文（Time/Clocks; Paxos 作背景）— A
- Gilbert & Lynch, CAP 原论文 + Brewer 原始表述 + "CAP Twelve Years Later"（防误读）— A
- Abadi, PACELC — A
- Ongaro & Ousterhout, Raft 论文 — A
- Gray & Reuter 事务处理（隔离级别、ACID 原始语义）— A/B

### 3.3 可靠性工程

- Nygard, *Release It!*（failure patterns 的重要实证来源）— A/B
- Google SRE Book + SRE Workbook（官方公开版）— A
- AWS Well-Architected Framework / Azure Well-Architected — A（作为工业界检验集，不作理论源）

### 3.4 性能

- Gregg, *Systems Performance* 2nd — A
- Little's Law 原始表述 + 适用条件文献 — A
- Amdahl 原论文 — A
- Gunther, Universal Scalability Law（**预登记为 NEEDS_EVIDENCE 候选**：需验证来源可靠性后才使用）— B?

### 3.5 并发

- 结构化并发原始论述（njsmith "Notes on structured concurrency"、Kotlin/Swift/Java Loom 官方文档作机制例）— A/B
- Hoare CSP 原始材料； actor model（Hewitt/Agha）— A/B
- 主流 runtime 官方并发文档仅作机制示例，不作原则来源 — B/C

### 3.6 安全

- Saltzer & Schroeder, "The Protection of Information in Computer Systems" (1975) — A
- NIST SP 800 系列（相关部分）、OWASP ASVS/Top10（架构级部分）— A
- Microsoft Threat Modeling（STRIDE）— B

### 3.7 Agent 工程（消费方式研究）

- GitHub Spec Kit、Kiro Specs 官方资料 — A（官方）
- Anthropic 官方 long-running agent / harness 工程文章 — A
- OpenAI harness/agent 工程公开材料 — A/B
- **预登记偏见警告**：此类来源多为厂商材料，须按 §2.5 区分「工程实践」与「产品叙事」。

### 3.8 覆盖缺口预登记

以下来源类别 Stage 2 必须主动补充，否则覆盖不完整：

- Postmortem 语料（Cloudflare / GitHub / AWS 等公开事故报告）— C 级但为 Failure Pattern 的关键实证；
- Embedded/Edge 与 Local AI Tool 形态的架构资料（§5 的 12 类形态中资料最稀缺的两类）— 缺口已知；
- AI Agent Runtime 架构（长时运行、上下文管理、工具调用生命周期）— 新兴领域，预期大量 `CONTESTED`。

---

## 4. Source Acquisition Strategy

1. **先索引后阅读。** 每个候选来源先建 manifest 条目（§12 全字段），标记 `status: queued`，再按研究问题驱动精读。禁止「先读一堆再想用不用」。
2. **双源验证规则。** 拟升级为 Mother Principle 的每个主张，须 ≥2 个独立 Tier A/B 来源，或 1 个 Tier A + 生产实证（postmortem/成熟开源项目）。单源主张最高 `status: candidate`。
3. **冲突处理。** 权威来源冲突时不做取舍，登记 `CONTESTED` 进入 `review-queue.yaml`，记录双方主张、各自上下文假设、分歧点。Stage 5 专门处理。
4. **版本与漂移。** manifest 记录 `last_verified`；对活文档（Well-Architected、SRE workbook 在线版）记录访问日期与版本。
5. **版权纪律。** 只保存高密度概括 + 必要短引用 + 位置指针 + URL；不整段搬运。
6. **检索路径。** 官方出版物/出版社页面 → 作者站点 → 标准组织站点 → 高校/机构存档；搜索引擎仅用于定位，不用于佐证。
7. **工作量控制（Stage 2 的停止规则）。** 每个域达到「能支撑该域全部研究问题的最小来源集」即停；预期总量 60–120 个来源条目，深度精读集中在约 25–35 个核心来源。超过 150 个条目触发范围审查。

---

## 5. First-Principles Hypotheses to Test

登记对象 = §4 六候选 + §37 候选思想 + 本计划新增候选。全部为 Hypothesis，Stage 4–6 期间接受证伪。

| ID | 假设 | 核心主张（一句话） | 预定证伪实验 |
|---|---|---|---|
| H1 | Purpose Fitness | 架构好坏只能相对「被要求的系统属性 + 真实约束」判定 | 找「违背产品目标但结构优雅」与「实现产品目标但结构丑陋」的案例对 |
| H2 | Explicit Ownership（合并 Clear Boundaries & Ownership） | 一切运行时实体与状态必须有可回答的 owner，否则故障时无人负责 | GC/actor/函数式系统中所有权是否仍是一阶问题；所有权是否可与边界分离 |
| H3 | Bounded Execution | 无界（时间/空间/并发/重试/积压）是架构失败的最大单一来源 | 找故意无界但正确的系统（如探索性计算、REPL） |
| H4 | Failure Containment | 子系统的故障权力不应超过其责任所需（§7.8 候选） | 共享基础设施（DB/网络）的经济性反例；隔离成本超过收益的场景 |
| H5 | Evolvability | 变化成本是被架构保护的一阶属性 | 一次性/短命软件是否需要；可逆性框架是否完整覆盖 |
| H6 | Legibility & Operability | 不可观测/不可理解的系统不可可靠运维 | 高可靠但低可观测系统的反例（形式验证过的嵌入式？） |
| H7 | Reversibility（§37 新增候选） | 决策可逆性应决定决策流程与审慎度 | 不可逆决策是否真的存在绝对类别 |
| H8 | Locality（§37 新增候选） | 推理/变更/故障的成本随距离增长 | 与分布式透明性的冲突 |
| H9 | Compatibility（§37 新增候选） | 兼容性是架构保护的独立属性，还是 Evolvability 的子集 | 合并/拆分判定（RQ-0.1 的合并检验直接适用） |
| H10 | Controlled Complexity | 目标是最小充分复杂度，不是最小复杂度 | 「简单至上」的失败案例（过度简化导致正确性受损） |

合并/拆分判定程序（Stage 6 执行）：对每对假设，用 eval 场景库做判别测试——存在场景能区分两原则（一个被违反另一个没有）则保持分离，否则合并。目标终值 ≤20 条，期望 8–15 条。

---

## 6. Known Bias Risks

预登记研究者（本 Agent）自身的偏见风险，Stage 5/10 对照检查：

| ID | 偏见 | 风险表现 | 缓解 |
|---|---|---|---|
| B1 | 后端/分布式中心偏见 | 把分布式系统原则当通用原则 | RQ-0 检验强制覆盖 12 类形态；每原则须给出不适用形态 |
| B2 | 大厂实践偏见 | Google/AWS 方法论被当作普适律 | Tier 分级；大厂材料只作工业检验集 |
| B3 | 新书/新词偏见 | 近年热词（云原生/微服务/serverless）获得超额权重 | 所有原则须能映射回 1970s–90s 的基础文献或其证伪 |
| B4 | Checklist 化偏见 | 把研究退化成「最佳实践汇编」 | 质量门禁：每原则必须过 §15 模板全部字段，尤其 Counterexamples |
| B5 | 过度工程偏见（评审侧） | 对简单系统套用重型框架 | eval 中 GOOD CASE 占比 ≥30%，专测误报 |
| B6 | 确认偏误 | 只搜支持候选原则的证据 | Stage 5 强制反例配额：每个候选原则至少 2 个认真构造的反例尝试 |
| B7 | 语言/生态偏见 | 以英文文献与主流语言 runtime 为全部世界 | 主动补非英语来源与嵌入式/函数式生态 |
| B8 | Agent 厂商叙事偏见 | 把厂商 harness 材料当工程事实 | 见 §3.7 预登记警告 |

---

## 7. Proposed Knowledge Architecture

采用任务书 §13 目录结构，Stage 7 允许小幅调整，但以下设计决策 Stage 1 即锁定（它们决定后续所有产物的形态）：

1. **三层渐进披露。**
   - L0：`00_ROUTER.md`（目标 <150 行，只做路由，零正文知识）；
   - L1：domain `index.md` + `principles/index.md` + `failure-patterns/index.md`（每个 <100 行，高密度摘要 + 稳定 ID）；
   - L2：原子知识文件（单主题、YAML frontmatter + Markdown，目标 80–250 行）；
   - L3：`sources/` 证据文件（仅在争议/高风险/低置信/用户要求时读取）。
2. **稳定 ID 方案。** `P-*` 原则、`FP-*` 失败模式、`T-*` 战术、`DP-*` 决策剧本、`S-*` 来源、`Q-*` 问题库条目、`EV-*` eval 场景。ID 一经分配不复用、不改语义；废止用 `status: deprecated` 标记而非删除。
3. **关系先行。** `relationship-map.yaml` 在 Stage 7 与知识文件同步构建，遵循 §18 的 Principle→protects→FailurePattern→detects_by→Tactic→tradeoff→Source 图式。索引文件由关系图生成而非手工维护（降低漂移）。
4. **知识与战术严格分层。** Principle / Failure Pattern / Tactic 三类文件用 `type` 字段强制区分；战术文件必须显式声明 `applies_when` / `costs` / `fails_when`。
5. **状态机。** 知识条目状态：`draft → candidate → stable → deprecated`；升级为 stable 的门槛写死在 §10 规则（双源 + 反例尝试 + eval 覆盖）。
6. **不确定性是一等公民。** `UNKNOWN / CONTESTED / CONTEXT_DEPENDENT / NEEDS_EVIDENCE` 作为 frontmatter 合法值，不得用流畅文笔掩盖。
7. **反 monolith。** 单文件 >400 行触发拆分审查；`00_ROUTER.md` 与任何 index 禁止包含正文知识。

---

## 8. Evaluation Strategy

Stage 1 只确定 eval 的设计骨架与成功标准，场景正文在 Stage 7–10 构建。

### 8.1 场景库构成（§30 的 25 类为下限）

- 每类至少 1 个场景，目标 30–40 个；
- 栈/形态配额：至少覆盖 {Web FE, Backend, Mobile/Desktop, Distributed, DB-heavy, AI Agent Runtime} 各 ≥3 个；
- **GOOD CASE 配额 ≥30%**（表面危险但合理的设计），专测误报与教条化（B5）；
- 每场景配 `expected-findings/`：必须命中（recall 项）/ 可选命中 / 不得报告（precision 项）三级标注。

### 8.2 评测维度与打分

采用 §31 的 A–J 十维，每维 0–2 分（0 缺失 / 1 部分 / 2 合格），另设三条一票否决：

- 把 Personal Preference 报告为 Blocker；
- 编造证据或来源；
- 静默削弱 Product Contract（RQ-6）。

### 8.3 对抗轮次（§33）

- R1 明显失败 → 测 Recall，目标 recall ≥90% 于「必须命中」；
- R2 隐蔽/跨组件失败 → 测机制推理，目标 ≥70% 且 mechanism 描述得分 ≥1.5；
- R3 GOOD CASE → 测 Precision，目标误报率 ≤15%，且不得出现教条式判决（检测到 async/cache/microservice 关键词自动报错 = 直接失败）。

### 8.4 AI 消费性实测

在 Stage 10 用受控 Agent 运行实测 Progressive Disclosure 效率：记录每个场景下 Agent 读取的文件数与 token 量，目标中位数 ≤8 个文件完成评审；超标则回炉 Knowledge Architecture（Stage 7 修复），而不是改 prompt。

### 8.5 修复优先级纪律

eval 暴露问题时按 §33 顺序修复：Knowledge → Principles → Question Bank → Reasoning Model → Prompt。每轮 eval 结果落盘 `eval/results/`，含 Missed / FalsePositives / OverDesign / WrongAssumptions 四类明细。

---

## 9. Estimated Distillation Stages

沿用任务书 §40 的 Stage 1–13，补充每阶段的**出口判据（Gate）**与预估关键风险：

| Stage | 产物 | Gate（进入下一阶段的条件） |
|---|---|---|
| 1 | 本计划 | 人工评审通过 |
| 2 | `source-manifest.yaml` + `sources/` | 每域最小来源集齐；双源规则可执行；缺口已登记 |
| 3 | `02_VOCABULARY.md` | 域间术语冲突全部显式登记；无静默双义 |
| 4 | candidate principles（`status: candidate`） | 每条过 §15 模板；每条挂 ≥1 来源 |
| 5 | 反例与冲突报告 | 每候选原则 ≥2 个认真反例尝试；冲突全部 `CONTESTED` 登记 |
| 6 | Mother Principles 集合 | ≤20 条；合并/拆分判定记录完整；每条 ≥2 独立来源或降级 |
| 7 | domains/ + failure-patterns/ + tactics/ + relationship-map.yaml | 18 Failure Pattern 全覆盖且可追溯到原则；索引可由关系图生成 |
| 8 | decision-playbooks/ + question-bank/ | §20 问题清单全归档到 Q-ID；playbook 通过走查 |
| 9 | Agent v0.1（system prompt + modes） | prompt 只含 §38 允许的九类内容；无知识正文 |
| 10 | eval 结果（R1–R3） | 达到 §8.3 目标或进入修复循环 |
| 11 | 修复记录 | 修复发生在正确层级；无 prompt 打补丁式修复 |
| 12 | Agent v1.0 | 重跑 eval 达标；GOOD CASE 误报率达标 |
| 13 | DISTILLATION_REPORT + PRINCIPLE_COVERAGE + OPEN_QUESTIONS | §42 十四问全部有明确回答（允许回答为 UNKNOWN） |

---

## 10. Questions That Genuinely Require Human Decision

以下问题超出 Agent 决策权限或影响任务边界，提交评审：

- **Q-H1（范围）**：§5 的 12 类系统形态中，是否允许对 Embedded/Edge 与 Local AI Tool 两类接受较低的研究深度（公开高质量来源稀缺，强行覆盖可能引入低 Tier 来源）？还是宁可标记 `NEEDS_EVIDENCE` 也保持同等严格？
- **Q-H2（来源边界）**：是否允许引用需要付费的书籍正文（如 *Systems Performance*、*DDIA*）？当前策略是使用其公开章节、作者公开演讲/论文与官方摘要，可能降低证据颗粒度。
- **Q-H3（评测执行方式）**：Stage 10 的 25+ 场景评测，是由本 Agent 自评（成本低、有自欺风险）、由另一个 Agent 交叉评（成本高、更可信）、还是混合？Issue #1 的 bake-off 结果表明存在 challenger/reviewer 的可能性——建议至少 R2/R3 轮由非作者 Agent 执行或复核。
- **Q-H4（终态语言）**：最终知识库与 System Prompt 的语言——中英双语、纯中文、还是纯英文（面向跨模型复用时英文更通用，但本项目语境为中文）？默认建议：知识正文中文，稳定 ID/枚举/frontmatter 键英文。
- **Q-H5（Knowledge Architecture 微调授权）**：§13 目录结构允许「小幅调整」的边界——Agent 是否可在 Stage 7 自主增删一级目录（如新增 `mechanisms/` 层），还是任何一级目录变更都需人工批准？

---

## 11. Scope Discipline 声明

本计划不包含：任何来源正文摘要、任何候选原则的正式表述、任何 System Prompt 草稿、任何 eval 场景正文。这些分属 Stage 2/4/9/7–10。Stage 1 到此为止。
