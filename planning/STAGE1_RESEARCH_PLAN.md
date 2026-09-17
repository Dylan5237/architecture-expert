---
id: PLAN-S1-WB-001
type: research-plan
project: architecture-expert
author: WorkBuddy (GLM 5.3)
branch: eval/stage1-workbuddy
version: 1.0
date: 2026-09-17
status: AWAITING_REVIEW
scope: Stage 1 - Research Plan only (per AGENTS.md initial gate, TASK.md, task prompt 40/46, Issue #1)
next: Stage 2 blocked until this plan is accepted by Chief Architect / human owner
---

# STAGE 1 — RESEARCH PLAN（WorkBuddy submission）

> 使命回顾（task §45）：得到一个能"理解目标 → 获取最小必要知识 → 建立系统模型 → 找出约束 → 回源证据 → 推导运行机制 → 建立 Failure Model → 找到风险 → 分析 Trade-off → 设计最小方案 → 定义验证 → 明确未知 → 在真正需要决策权时升级"的通用架构专家，而非"懂架构名词的 AI"。本计划只回答"怎么研究、怎么蒸馏、怎么证明"，不产出知识本体。

## 0. 输入基线与范围声明

- 已完整阅读：`AGENTS.md`、`TASK.md`、`prompts/KIMI_ARCHITECTURE_DISTILLATION_TASK.md`（§1–§46）、Issue #1 正文及全部 3 条评论（含 Chief Architect 对 Kimi 计划的初审意见与 Q-H1–Q-H5 裁决）。
- 已采纳的既定裁决（本轮不再重复提问）：
  - Q-H1 证据标准不降级（Embedded/Local AI 证据不足就标 NEEDS_EVIDENCE）；
  - Q-H2 付费书合规使用边界（合法可及、不存大段原文、记录缺口）；
  - Q-H3 混合评测 + 独立挑战（R2/R3 非作者执行或裁决）；
  - Q-H4 语言规范（中文行文 + 英文稳定 ID/枚举/frontmatter key/关键术语）；
  - Q-H5 一级本体变更需架构变更备忘 + Chief Architect 审批。
- 范围纪律：本文件是 Stage 1 的全部正式产物。未创建 source manifest、未收集来源、未撰写原则正文、未生成 System Prompt 或任何 corpus（对应 Issue #1 比较准则 9：Scope discipline）。

## 1. Research Questions

### RQ-0 锚问题

**架构质量能否归约为少量（≤20，目标更少）跨栈、机制可解释的母原则，使大多数架构失败模式（FP）与 tactic 选择规则可由它们推导？**

- RQ-0.1 "推导"的操作定义：原则 P 解释 FP-F，当且仅当 P 能陈述"违反 P ⟹ 以什么**机制链**产生 F 描述的失败"（机制因果，非相关性、非类比、非"best practice"）。
- RQ-0.2 防弹性化：原则不得宽泛到事后能解释一切。对策见 §5 判别式预注册协议（Issue #1 评论 3 修正点 3）。
- RQ-0.3 跨栈检验：每条母原则须在 ≥3 类系统（task §5 的 12 类中抽取，至少 1 类为非服务端：桌面/嵌入式/开发工具/本地 AI 工具/Agent Runtime）给出机制级成立说明或明确的分级适用条件。
- RQ-0 证伪路径：若 Stage 5–6 发现高频 FP 簇无法由任何候选原则机制化解释，或解释需堆砌例外条件，则 RQ-0 部分失败 → 输出"原则层 + 领域启发式层"的分层结论，而不是硬凑宪章。

### RQ-A 定义与边界组（Architecture 是什么、保护什么）

| ID | 问题（可证伪形式） | 预期产物 | 验证方式 |
|----|------|------|------|
| RQ-A1 | 覆盖 task §5 全部 12 类系统的严格 Architecture Definition 是否存在？判别式"这是不是架构问题"能否形式化？ | `02_VOCABULARY.md` Architecture 词条 + 判别规则 | 12 类系统各做 1 正例 / 1 反例判别测试；边界用例：算法/数据结构选择何时升级为架构决策（当其定义边界或状态契约时） |
| RQ-A2 | §5 的 13 项候选保护对象（Capability…Operability）能否归并为不重叠的最小集？ | Constitution 的 `protects` 维度词表 | 与 ISO 42010 concerns、ISO 25010 characteristics 做映射归并，输出不可归并残差清单 |
| RQ-A3 | 最小充分架构描述形式是什么（views / C4 / EARS / QA scenario / ADR 的最小组合）？ | domains/decision-making 与 domains/communication 的结论 | 双向测试：真实 ADR+C4 让陌生 agent 重建系统行为；反向从系统生成描述再由另一 agent 复原 |

### RQ-B 母原则组（What makes an architecture good）

| ID | 问题 | 预期产物 | 验证方式 |
|----|------|------|------|
| RQ-B1 | task §4 六候选 + §37 补充候选（详表见本计划 §5）中，哪些应保留 / 合并 / 拆分 / 降级？ | 12–16 条带适用边界的候选原则 → Stage 6 宪章草案 | 每条完成 §5 六相证伪流程；机制/属性配对检测（RQ-B5） |
| RQ-B2 | Boundedness 能否作为统一机制解释 unbounded queue / retry / fan-out / scan / memory / concurrency 六类失败？ | 母原则 + 可推导的检查规则 | 覆盖测试：≥90% 的 unbounded 类 FP 可由该原则机制化推导（Stage 7 用 failure-patterns 草稿实测） |
| RQ-B3 | "failure power ≤ responsibility" 是否跨栈成立？单进程桌面/CLI 接受整体崩溃是否构成真实反例？ | 原则定稿（带分级适用条件）或降级为 heuristic | 跨栈反例程序：桌面/嵌入式/工具类中"低隔离但成功"的系统清单 + 成本收益解释 |
| RQ-B4 | 哪些流行"最佳实践"实为 context-dependent tactic（microservice / async / cache / DDD / Clean Architecture / K8s / 事件驱动）？适用/不适用条件如何精确表述？ | tactics/ 条目的 Applies When / Does Not Apply When | Round 3 对抗评测（表面危险实际合理的设计）直接检验误报率 |
| RQ-B5 | 机制与属性是否被误当两条原则（如"显式边界"(机制) 与"变更局部性"(属性)）？ | Reduction 阶段合并规则 | 每条候选标注 mechanism / property / decision-process 三类，层内合并候选显式评估 |

### RQ-C 推理组（资深架构师如何思考）

| ID | 问题 | 预期产物 | 验证方式 |
|----|------|------|------|
| RQ-C1 | task §6 的 12 个 System Model 是否完备、可按任务类型裁剪？真实推理是固定顺序，还是证据驱动的机会主义 + 完备性清单兜底？ | agent/ 推理工作流（STEP 序列 + 触发条件 + 裁剪规则） | 3 个不同栈陌生系统纸上演练，记录实际调用的模型子集与顺序 |
| RQ-C2 | 高价值架构问题最小集是什么？§20 的 33 问归并后按模型分组、按建模进度触发的 question bank 长什么样？ | question-bank/（每问带激活条件） | 每问标注"建到哪一步该问"；与 FP 检测问题交叉引用 |
| RQ-C3 | "停止深挖、开始下结论"的判定规则是什么？§21 五级证据分类的操作判据？ | Evidence Discipline 操作判据 | eval 维度 I 实测：agent 是否在证据不足时仍下强结论；伪造证据 = 单场景自动不合格 |

### RQ-D 知识工程组（知识库怎么建才能被 AI 消费）

| ID | 问题 | 预期产物 | 验证方式 |
|----|------|------|------|
| RQ-D1 | Progressive disclosure 的最优层级/粒度：router 多短、index 多细、单文件多大？典型任务总加载量能否 < 8K tokens？ | 00_ROUTER.md + 各 index + 参数基线（全部标 `status: hypothesis`） | 消费测试（§7.4）：5 种任务原型模拟加载路径，计 token 与路由命中率；Stage 7.5 冒烟 + Stage 10 全量 |
| RQ-D2 | relationship-map 谓词最小闭集是什么？ | 谓词枚举 + schema | 导航完整性测试：任一 FP 可达 ≥1 principle 与 ≥1 source；闭集外关系一律拒绝入库 |
| RQ-D3 | Q-H4 双语边界的执行细节：术语翻译损害精度时如何回退英文？ | 全库语言规范 | 抽样 3 个 principle 文件双语对照评审 |

### RQ-E 评测效度组（如何证明蒸馏成功）

| ID | 问题 | 预期产物 | 验证方式 |
|----|------|------|------|
| RQ-E1 | 场景集能否同时测 recall / precision / 教条化三种失败模式，并区分"真推理"与"清单匹配"？ | eval/ 全套（§8 四部分组合） | inverted-pattern 场景（似险实安必须 PASS）+ novel-recombination 场景（表面模式与机制错位，只有机制推理能发现） |
| RQ-E2 | expected findings 如何客观化（不以知识作者视角循环论证）？ | expected-findings/ + 预注册协议 | 2–3 个 held-out 场景改编自公开 postmortem，答案来自事故报告本身且不写入知识库 |
| RQ-E3 | over-engineering 与 product-contract 侵蚀如何量化评分？ | rubric 维度 G/H 刻度 | Round 3 良构场景 + 种子场景回归；静默削减产品能力 = 0 容忍 |

## 2. Knowledge Domains — 覆盖矩阵与检索簇

规则（吸收 Issue #1 评论 3 修正点 1 + Q-H5）：task §7 的 18 个知识域是**强制最低覆盖，不是封闭本体**。研究期按"检索簇"（cluster）组织——同簇共享来源族、避免重复检索；最终知识库本体在 Stage 6–7 由证据形状决定，一级目录变更走架构变更备忘 + Chief Architect 审批。

| 簇 | 覆盖（§7 编号） | 检索主线（来源族） | 优先级 |
|----|------|------|------|
| W1 结构·边界·演进 | 7.1, 7.16 | Parnas / Brooks / Fowler 谱系（Evans、R.C. Martin 降权） | P0 |
| W2 质量属性·决策·沟通 | 7.2, 7.17, 7.18 | SEI（Bass/Clements/Kazman、ATAM）/ ADR 实践 / ISO 42010 | P0 |
| W3 运行时·并发·生命周期 | 7.3, 7.4, 7.12 | OS 文献 / CSP / structured concurrency / 各 runtime 官方文档 | **P0（最高，§7.12）** |
| W4 性能·资源·扩展 | 7.5, 7.6, 7.15 | queueing theory（Little/Amdahl）/ Gregg / The Tail at Scale | P0 |
| W5 失败·隔离·可靠性·分布式 | 7.7, 7.8, 7.9 | Nygard / Google SRE / CAP 谱系 / Raft / AWS Builder's Library | P0 |
| W6 状态·数据·集成 | 7.10, 7.11 | Kleppmann / 数据库官方文档 / EIP / Newman | P0 |
| W7 安全 | 7.13 | Saltzer & Schroeder / NIST / OWASP | P1 |
| W8 可观测·运维 | 7.14 | SRE Book + Workbook / 可观测性文献 | P1 |
| W9 Agent 工程反哺 | §9 末组 | GitHub Spec Kit / Kiro / Anthropic 工程文章 / OpenAI agents guide | P1 |

Issue #1 比较准则 4 列的 16 个领域全部落位：fundamentals→W1；runtime/execution、concurrency→W3；performance、resources、scalability→W4；reliability、distributed→W5；state/data、integration→W6；lifecycle→W3；security→W7；observability→W8；evolution→W1；decision-making、communication→W2。

## 3. Candidate Primary Sources

纪律：Stage 1 只登记候选与用途；URL / 版次 / 存取核实与 `last_verified` 记录在 Stage 2 获取时完成——**本表不包含任何"已验证"声明**（诚实边界）。优先级定义：P0 支撑母原则提取；P1 支撑域深化与反例；P2 服务评测与 held-out。

### Tier A — 标准 / 经典论文 / 官方方法论

| 来源 | 年份 | 簇 | 优先级 | 用途 |
|------|------|-----|--------|------|
| ISO/IEC/IEEE 42010 (Ed.2) | 2022 | W2 | P0 | 架构 vs 架构描述的概念基座（RQ-A1/A2） |
| ISO/IEC 25010 | 2011/2023 | W2,W4 | P0 | 质量特性对照（RQ-A2）；2023 修订状态 Stage 2 核实 |
| Parnas, "On the Criteria…" | 1972 | W1 | P0 | information hiding 原文（H-02/H-06） |
| Brooks, *MMM* + "No Silver Bullet" | 1975/1986 | W1 | P0 | 概念完整性；本质 vs 偶然复杂度（H-11） |
| Bass/Clements/Kazman + SEI ATAM | 2012/2021 | W2 | P0 | QA scenario / drivers / trade-off 方法学（RQ-A3） |
| Gilbert & Lynch 2002 + Brewer "CAP Twelve Years Later" 2012 | — | W5 | P0 | CAP 形式化 + 作者自我修正（去教条关键证据） |
| Dean & Barroso, "The Tail at Scale" | 2013 | W4 | P0 | 尾延迟 / queueing 效应 |
| Little 1961；Amdahl 1967 | — | W4 | P0 | 定量基座 |
| Hoare, CSP | 1978 | W3 | P0 | 并发推理基座 |
| Lamport（时钟/Paxos）；Raft 论文；FLP | 1978–2014 | W5 | P1 | 分布式机制（预期留在域层，见 §5 降级预判） |
| Saltzer & Schroeder | 1975 | W7 | P0 | least privilege / fail-safe defaults（H-09） |
| Nygard, *Release It!* 2e | 2018 | W5 | P0 | circuit breaker / bulkhead 原始出处 |
| Google SRE Book + Workbook | 2016/2018 | W5,W8 | P0 | 官方免费全文 |
| AWS Builder's Library | 持续 | W5,W6 | P0 | backoff/jitter/bulkhead/cell-based 官方权威 |
| AWS / Azure / GCP Well-Architected | 持续 | W2 | P1 | 三家交集 = 共识部分证据更强 |
| Node.js event loop / SQLite / PostgreSQL(MVCC) 官方文档 | 当前 | W3,W6 | P1 | 对冲分布式偏差（B-01）的非服务端机制文档 |
| NIST SP 800-160 v1 + OWASP ASVS | 当前 | W7 | P1 | |

### Tier B — 公认研究者与工程组织长期著作

| 来源 | 年份 | 簇 | 优先级 | 用途 |
|------|------|-----|--------|------|
| Fowler, *PoEAA* + bliki 精选（Microservices / MonolithFirst / CQRS / EventSourcing / StranglerFig / TechnicalDebt） | 2002–2015 | W1,W6 | P0 | 一手 bliki 免费 |
| Evans, *DDD* | 2003 | W1 | P1 | bounded context；需独立来源族支持才升级 |
| R.C. Martin, *Clean Architecture* | 2017 | W1 | P1 | **降权读取**：只取依赖倒置机制论证，不作规范依据 |
| Kleppmann, *DDIA* | 2017 | W5,W6 | P0 | 2e 状态 Stage 2 核实 |
| Kleppmann, "Please stop calling databases CP or AP" | 2015 | W5 | P1 | 去教条化关键证据 |
| Hohpe & Woolf, *EIP* | 2003 | W6 | P0 | 集成语义（idempotency/ordering）原始框架 |
| Newman, *Building Microservices* 2e | 2021 | W6 | P1 | |
| Richards & Ford, *Fundamentals* + *Hard Parts* | 2020/2021 | W2 | P1 | trade-off 案例集 |
| Gregg, *Systems Performance* 2e | 2020 | W4 | P1 | |
| Abadi, PACELC（作者博客） | 2012 | W5 | P1 | 一手研究者材料 |
| Gunther, USL | 1993–2007 | W4 | P1 | 证据充分才保留为理论条目，否则 CONTESTED |
| N. Smith "Notes on structured concurrency"（trio）+ JEP 453 + Kotlin coroutines guide | 2018– | W3 | P0 | cancellation / ownership 的现代一手来源 |
| Shostack, *Threat Modeling* | 2014 | W7 | P1 | |
| GitHub Spec Kit；Kiro 官方文档；Anthropic "Building Effective Agents" 等工程文章；OpenAI "A Practical Guide to Building Agents" | 2024– | W9 | P0 | agent harness 约束反哺通用原则 |

### Tier C — 高价值案例 / Postmortem（服务评测与 held-out）

| 案例 | 年份 | 服务对象 | 优先级 |
|------|------|----------|--------|
| AWS S3 大规模故障官方复盘（重试放大） | 2017 | FP-RETRY 类 held-out 候选 | P2 |
| GitHub 24h 降级复盘（维护编排失败） | 2018 | 编排类 held-out 候选 | P2 |
| Cloudflare 正则回溯事故 | 2019 | runtime 失败隔离案例 | P2 |
| Knight Capital（SEC 报告为证） | 2012 | 部署/复用旧代码案例 | P2 |
| Facebook BGP 级联断网 | 2021 | 级联失败案例 | P2 |
| CrowdStrike 根因报告 | 2024 | 更新门禁缺失案例 | P2 |

Tier D（一般博客、二次解释）仅理解辅助，不入 manifest 证据链；SEO 农场与 AI 聚合内容排除（§8 纪律）。

## 4. Source Acquisition Strategy

1. **获取顺序**：P0 全量 → P1 按簇检索需要逐个补入 → P2 在 Stage 10（评测设计）前到位。
2. **访问路径**：官方免费在线优先（sre.google / AWS Builder's Library / martinfowler.com / kiro.dev / github/spec-kit / anthropic.com/engineering / OpenAI CDN / ISO OBP 预览 / arXiv 与作者主页）。付费书按 Q-H2：合法可及才用；不存大段受版权保护原文，只存 provenance + 章节/页码定位 + 高密度概括 + 必要短引；不可及就记录缺口，不假装读过。
3. **manifest schema**（Stage 2 落地，字段 = task §12）：`source_id / title / author_or_organization / publication / year / url / source_type / authority_tier / topics / clusters / last_verified / status / notes`。
4. **晋升规则**（落实 §8 交叉验证要求）：母原则须 ≥2 个**独立来源族**支持（作者与组织谱系独立——SEI 与 Google SRE 算两族；同一作者的著作+博客算一族）。单族支撑的观点停留在 domains 层 heuristic，不得进入 Constitution。
5. **冲突规则**：权威来源真实冲突 → 双双收录 + `CONTESTED` + 入 review-queue，不静默裁决（fail closed，§44）。
6. **停止条件**：全文沿用 §44（找不到 primary source / 权威真实冲突 / 理论与实践明显冲突 / 高度栈相关 / 仅个人观点 → 标 UNKNOWN / CONTESTED / CONTEXT_DEPENDENT / NEEDS_EVIDENCE，不为完整性补全）。
7. **数量观**（吸收评论 3 修正点 6）：一切数量区间是运营护栏，不是成功标准。验收用信息密度（每条原则解释的 FP 数、每次正确决策的 token 成本、路由命中率）与决策质量，不用文件数 / 来源数。

## 5. First-Principles Hypotheses to Test

收敛目标 **8–14 条**（task 允许 8–20，取少不取多）。每条候选必过六相流程（§10）：Extract → Normalize → Compare → **Falsify（强制反例搜索留痕，结果可为"未找到反例"）** → Reduce → Operationalize。RQ-B5 合并规则：候选先标注 mechanism / property / decision-process 三类，只有同类才谈合并。

| ID | 假设（statement 雏形） | 类型 | 来源线索 | 关键检验 |
|----|------|------|------|------|
| H-01 | Purpose Fitness：架构决策须可追溯到须保护的 required properties + drivers | property | SEI drivers | 与 H-12 分离测试：是否存在保住全部显式契约却偏离目的的设计（探索型产品反例） |
| H-02 | Explicit Boundaries：依赖方向与信息隐藏边界显式化，沿变更方向与知识方向切分 | mechanism | Parnas | 反例搜索：Linux 单体高内聚成功？→ 边界粒度分级；与 H-06 的关系见 RQ-B5 |
| H-03 | Explicit Ownership：每个运行时实体恰有一个生命周期 owner（或显式转移协议） | mechanism | §7.12 / structured concurrency | orphans / stale work 是否全部可归因于 owner 缺失；与 H-08 的关系 |
| H-04 | Bounded Execution：一切资源消耗维度显式有界；交互关键路径不被可延迟工作阻塞 | mechanism | §7.6 / Builder's Library | RQ-B2 覆盖测试；批处理反例 → "界"的维度轴修正 |
| H-05 | Failure Containment：子系统的 failure power ≤ 其 responsibility | property | Nygard | RQ-B3 跨栈反例程序；预判带分级适用条件 |
| H-06 | Change Locality：变更成本与变更理由成比例 | property | Parnas | 可能是 H-02 的 protects 表述 → Reduce 阶段合并评估 |
| H-07 | Reversibility：按可逆性给决策分级，优先保留可逆性 | decision | Type 1/2 doors、ADR | 是否独立于结构原则的决策层原则 |
| H-08 | Single Source of Truth per State：每个状态恰有一个权威 owner | mechanism | DDIA / CQRS 反面教训 | 可能并入 H-03 作为状态特化 |
| H-09 | Least Trust：trust boundary 显式 + 最小权限 + fail-safe defaults | mechanism | Saltzer & Schroeder | 跨栈检验：本地单用户工具的信任模型退化形态 |
| H-10 | Legibility：正常/异常必须可区分，否则不可可靠运维 | property | §7.14 | 弱化形式检验：不可观测但行为确定性的嵌入式固件是否构成反例 |
| H-11 | Controlled Complexity：以保护 required properties 所需的最小复杂度为限 | meta | Brooks / §36 | 预判：更像宪章序言与验收判据，而非并列编号原则——Reduce 阶段定夺 |
| H-12 | Contract Preservation：实现约束不得静默重定义产品契约 | property | §22 | eval 维度 H 直接检验；与 H-01 的分离度 |

**预期不进入宪章的候选**（降级过滤器示例，证明 Reduce 机制在工作）：CAP / PACELC（仅分布式上下文 → 域知识）；async 优于 sync、cache、microservice、K8s（tactic，§17）；"所有模块必须解耦"（教条，§35）。

### 判别式预注册协议（防事后弹性化，RQ-0.2）

Stage 6 结束时冻结 `eval/preregistration.yaml`：每条存活原则登记 —— ≥2 个**应命中**的真实案例 + ≥2 个近似但**不得命中**的案例（含良构案例）+ 其解释的 FP 清单。评测后任何映射调整必须走 review-queue 留痕说明理由，不得静默重调；歧义映射交独立挑战者裁决（Q-H3）。

## 6. Known Bias Risks

| ID | 偏差 | 缓解 |
|----|------|------|
| B-01 | 分布式/云原生偏差：现代文献以服务端为主，桌面/嵌入式/开发工具欠代表 | 每个 P0 簇强制配比非服务端来源（Node.js / SQLite / 桌面案例 / 嵌入式）；RQ-0.3 跨栈检验 |
| B-02 | Clean Architecture / DDD 传播声量大，易被当成默认正确 | 降权读取 + 独立来源族晋升规则（§4.4） |
| B-03 | Postmortem 幸存者偏差（只有大厂大事故被记录） | 案例只作 FP 佐证与 held-out，不作原则唯一证据 |
| B-04 | 新鲜度 vs 经典性的锚点冲突 | 以"是否仍解释当前系统行为"为准，不以年代为准（Little 1961 与 2025 agent harness 并列） |
| B-05 | 确认偏差：研究者倾向证明候选假设 | 强制证伪相 + Round 3 教条化专项 + 独立挑战者 |
| B-06 | eval 循环论证（出题人 = 知识作者 = 判官） | 盲测隔离 + held-out + 判官/作者分离（§8.2） |
| B-07 | "把知识塞进 prompt"的引力 | System Prompt 契约 = 只含导航与规则；Stage 9 逐段审计 |
| B-08 | 把语言多样性当来源质量（评论 3 修正点 7） | 多样性目标定义为生态/系统形态多样；语言不是质量轴 |
| B-09 | 种子 prompt 的 Electron/FS 痕迹泛化为隐含假设 | PR_REVIEW_MODE 栈无关化重写；种子降级为 cases/ 素材 |
| B-10 | 冗长胜出的评审偏差 | 密度指标验收（§4.7）；评审看机制与可追溯性，不看篇幅（Issue #1 明示） |

## 7. Proposed Knowledge Architecture

采纳 task §13 目录树为**初始假设**，并把所有设计参数分成两类（吸收评论 3 修正点 2）：

### 7.1 不变量（现在锁定）

- 稳定 ID：`P-* / FP-* / T-* / DP-* / S-*`，frontmatter 含 `version` 与 `superseded_by`；
- YAML frontmatter + 单一主题原子文件 + 显式关联（§14）；
- 原则 / tactic 强制分离（§17：入库逐条问"这是机制还是手段"，手段一律进 tactics/）；
- 谓词闭集（RQ-D2）：`protects / violated-by / detected-by / mitigated-by / trades-off-with / derives-from / conflicts-with / supersedes`；闭集外关系拒绝入库；
- 语言规范（Q-H4）：中文行文 + 英文 ID / 枚举 / frontmatter key / 关键术语；
- 新鲜度：`review-queue.yaml` 记录 contested / 待人工复核 / 来源漂移 / eval 暴露缺口；
- 晋升阶梯：`candidate → contested/context-dependent → stable`（降级同样显式留痕）；晋升依据 = 来源质量 + 对抗评测结果，不是合并行为本身。

### 7.2 可调参数（`status: hypothesis`，消费测试前不定型）

单文件行数、目录拆分粒度、router 行数、index 深度、FP/T/DP 数量目标（§16 的 15–25 FP 等区间视为护栏）。初始护栏值沿用 §13–§16 建议值，Stage 7.5 / 10 消费测试后校准。

### 7.3 Progressive Disclosure 路径契约

`00_ROUTER → (按需) 01_CONSTITUTION → domains/<x>/index → 相关 P-* → 相关 FP-* → DP-*（存在真实选择时）→ S-*（争议 / 高风险 / 低置信 / 用户要求时）`。典型任务目标加载量 < 8K tokens——这是 RQ-D1 的**验证目标值，不是承诺值**。

### 7.4 消费测试设计（RQ-D1 的验证器）

5 种任务原型（PR review / 性能审查 / 方案设计 / ADR 审查 / 事故分析）× 模拟加载路径 → 记录 token 总量、路由命中率（该读没读 / 不该读读了）、决策质量代理分。Stage 7.5 冒烟（早发现参数错误）+ Stage 10 全量。

## 8. Evaluation Strategy

### 8.1 场景组合（四部分；扩展 §30/§33 以覆盖评论 3 修正点 4）

| 部分 | 构成 | 测什么 |
|------|------|--------|
| A 缺陷场景 ×25 | §30 枚举的 25 类失败（UI/event-loop 阻塞、unbounded queue、retry storm、orphan、stale async、全量扫描、热点、池耗尽、锁竞争、N+1、HOL、thundering herd、缓存不一致/踩踏、schema 迁移、兼容破坏、部分失败、重复/乱序、泄漏、noisy neighbor、超时预算错配、fan-out、隐藏 SPOF、过度设计） | recall + 机制质量 |
| B 良构反例 ≥5 | 正确使用的 async/worker、带失效与预算的 cache、带背压与 DLQ 的队列、真单写者的共享库、沿真实 ownership 缝的微服务拆分 | precision / 教条化（false positive 控制） |
| C 设计/权衡场景 ≥5 | 多可行解的 greenfield / 迁移 / 选型（示例：桌面索引器执行模型、strangler vs 原地迁移、长任务取消传播、一致性级别选择、100x 输入容量规划） | 约束识别、备选比较、可逆性处理、复杂度经济、unknowns 与验证计划——不只找缺陷 |
| D 事故分析 ≥3 | 给症状 → 排序失败假设 → 提出判别性证据请求 | 反向推理 + 证据纪律 |

C/D 部分改编自公开事件；held-out 2–3 个从 Tier C 选（S3 2017 / GitHub 2018 / Cloudflare 2019 / Knight 2012 / Facebook 2021 / CrowdStrike 2024），其答案不写入知识库（RQ-E2）。

### 8.2 盲测与判官（吸收评论 3 修正点 5 + Q-H3）

- 被测 agent 只见场景材料；expected-findings 物理隔离，由判官持有；
- R2 / R3 全部 + R1 抽样由非作者 agent 执行或独立裁决；分歧由 Chief Architect 裁决；自评只作廉价初筛，永不作为晋升唯一证据；
- 每次 run 记录元数据：模型、prompt 版本、知识库 git SHA、场景版本、判官身份。

### 8.3 三轮对抗（§33）

R1 明显失败测 recall → R2 隐蔽跨组件失败测 execution reasoning → R3 表面危险实际合理测误报。每轮记录 Missed / FP / Over-design / Wrong-assumption 四清单。反清单探针：inverted-pattern（似险实安，必须 PASS）+ novel-recombination（表面模式与机制错位，只有机制推理能发现）——直接区分真推理与模式匹配（Issue #1 准则 5）。

### 8.4 指标与阈值提案（数值待 Q-3 签署）

A–J 十维（§31）。提案：B（recall，关键缺陷）≥ 0.80；C（precision）≥ 0.67；G（scope）单场景 over-design ≤ 1；H（product）静默削减产品能力 = 0 容忍；机制引用率（findings 须命名机制链，仅模式名不算）≥ 80%；伪造证据 = 单场景自动不合格。

### 8.5 修复纪律（§33 顺序）

Knowledge → Principles → Question Bank → Reasoning Model → Prompt。System Prompt 只允许改导航与契约；每次修复在 review-queue 留痕 + before/after eval delta；修复落知识层占比 ≥ 70% 才算修对层。

## 9. Estimated Distillation Stages

| # | 阶段 | 产物 | Gate（谁验收） |
|---|------|------|------|
| 1 | 研究计划（本文件） | planning/STAGE1_RESEARCH_PLAN.md | Chief Architect + human owner（当前） |
| 2 | 来源收集 | source-manifest.yaml + sources/S-*.md（≥25 个 Tier A/B，含 notes + last_verified） | CA 抽查 provenance |
| 3 | 词汇归一 | 02_VOCABULARY.md（≥15 组跨来源术语冲突映射） | 术语一致性检查 |
| 4 | 原则提取 | 候选 20–30 条（evidence_class + source_ids） | 晋升规则合规检查 |
| 5 | 证伪评审 | 每条 ≥1 次反例搜索记录 | 独立挑战者 |
| 6 | 一阶归并 | 宪章草案（≤16 条）+ preregistration.yaml 冻结 | CA |
| 7 | 知识架构 | domains/ + failure-patterns/ + tactics/ + relationship-map.yaml | 谓词闭集 + 导航完整性 |
| 7.5 | 消费冒烟测试 | 参数基线报告 | 密度指标 |
| 8 | 推理模型 | decision-playbooks/ + question-bank/ | 每模式有触发与停止条件 |
| 9 | Agent v0.1 | ARCHITECTURE_EXPERT_SYSTEM_PROMPT.md 草案 | 无知识正文复制（逐段审计） |
| 10 | 评测 | eval/ 全套 + 首轮结果 + 消费全量测试 | 阈值（Q-3） |
| 11 | 修复 | 知识 diff + review-queue | 修复落知识层占比 ≥ 70% |
| 12 | Agent v1.0 | 最终 prompt + 11 个 MODE 文件 | 三轮对抗达标 |
| 13 | 蒸馏报告 | reports/ 四件套（含 §42 十四问） | human owner |

依赖：2→3→4→5→6 严格串行；7 可与 4–6 部分并行；8 依赖 6+7；10 依赖 9；11↔10 迭代；12→13。研究原生控制环（Issue #1 评论 2）贯穿 4–6：假设 → 独立取证 → 矛盾/缺口分析 → 综合提案 → 对抗挑战 → gate → 晋升/修订/保持争议。

## 10. Questions Requiring Human Decision

已裁决不重开：Q-H1–Q-H5（Issue #1 评论 3）。本轮真正开放：

| ID | 问题 | 我的建议 |
|----|------|------|
| Q-1 | Stage 10 评测执行预算与模型/判官分配（约 120–150 次 agent 调用跑在哪些 provider；判官用谁） | 强推理模型跑正式轮，弱模型只冒烟；判官与被测异模型 |
| Q-2 | 知识库最终宿主与消费形态（留本仓库 / 打包为 skill / 供哪些 agent 消费）——影响 router 路径假设（文件工具读取 vs 检索） | 留仓库；router 以文件读取为第一消费形态设计 |
| Q-3 | §8.4 阈值最终签署（recall / precision / 机制引用率等出口线） | 按 §8.4 提案值起步，Stage 10 后校准一次 |
| Q-4 | review-queue 人工复核的常设角色确认 | 默认 human owner；可授权 CA 代行 |

## 附：自检

- [x] task §46 十项产出齐备（研究问题 / 知识域 / 候选来源 / 获取策略 / 假设 / 偏差 / 知识架构 / 评测 / 阶段 / 人工决策）
- [x] Stage 1 纪律：未开始来源收集、未预写原则结论（全部标注待证）、未生成 prompt 或 corpus（Issue #1 准则 9）
- [x] Issue #1 评论 3 七项修正点原生吸收：开放本体（§2）/ 参数假设化（§7）/ 预注册（§5）/ 评测扩展（§8.1 C+D）/ 盲测（§8.2）/ 数量护栏观（§4.7）/ 多样性定义（§6 B-08）
- [x] 与 task §1–§46 无冲突；对 §13/§16 数值区间的处理已声明为护栏而非目标
