---
title: "STAGE 1 — Research Plan"
project: architecture-expert
version: 1.0
date: 2026-09-17
status: AWAITING_REVIEW
next_stage: 2 (Source Collection) — blocked until this plan is approved
---

# STAGE 1 — RESEARCH PLAN

> 目标回顾：不是写一条大 Prompt，而是构建可被任意高级 Agent 以 Progressive Disclosure 方式消费的架构知识系统，并从该系统蒸馏出 General-Purpose Software Architecture Expert。
> 本文档是全部后续阶段的控制计划。Stage 1 到此为止，不开始收集来源。

---

## 1. Research Questions

分五组。每个问题标注预期产物与验证方式。RQ 编号将贯穿后续所有阶段（coverage 矩阵、review-queue 均引用）。

### RQ-A 定义组（Architecture 是什么、保护什么）

| ID | 问题 | 预期产物 | 验证方式 |
|----|------|----------|----------|
| RQ-A1 | 能否给出一个严格的 Architecture Definition，同时覆盖任务书 §3 的 12 类系统（桌面 / 前端 / 移动 / 后端 / 单体 / 分布式 / 数据密集 / 开发工具 / 本地 AI 工具 / 云平台 / 嵌入式边缘 / Agent Runtime）？ | `02_VOCABULARY.md` 中的 Architecture 词条 + 判别式（"这属于架构问题吗"决策规则） | 对 12 类系统逐一做正反例测试：定义必须能解释为什么每类的典型架构关切不同 |
| RQ-A2 | Architecture 究竟在保护什么（Capability / Correctness / Quality Attributes / Constraints / Boundaries / State / Trust / Change…）？保护对象清单是否有限且不重叠？ | Constitution 的 `protects` 维度词表 | 与 ISO 42010 的 concern 概念、25010 的 quality characteristics 做归并对照 |
| RQ-A3 | 架构描述（AD）的最小充分表达形式是什么——哪些信息用人/AI 都可消费的极简格式承载（views / C4 / EARS / QA scenario / ADR）？ | domains/decision-making 与 5.18 的结论 | 用真实 ADR 与 C4 图做读写双向测试 |

### RQ-B 母原则组（What makes an architecture good）

| ID | 问题 | 预期产物 | 验证方式 |
|----|------|----------|----------|
| RQ-B1 | 六个候选母原则各自的解释力边界在哪里？哪些应合并（Boundaries 与 Ownership 是否同一条）？哪些应拆分（Evolvability 是否是 Reversibility + Change Locality + Compatibility 的合成）？ | 12–16 条母原则（01_CONSTITUTION.md），每条含适用/不适用条件 | 见 §5 假设矩阵；每条候选至少完成一轮 PHASE D 证伪搜索 |
| RQ-B2 | 候选"Bounded Execution"能否作为统一母原则，同时解释 unbounded queue / retry / fan-out / memory / scan / concurrency 六类失败？还是需要拆成 Resource Boundedness 与 Time Boundedness？ | 母原则 + 推导出的检查规则 | 在 failure-patterns 草稿上做覆盖测试：≥90% 的 unbounded 类 FP 能被该原则推导 |
| RQ-B3 | 候选"A subsystem should not have more failure power than its responsibility requires"是否成立、是否有跨栈反例（单进程桌面软件接受全进程崩溃）？ | 母原则 Failure Containment 的定稿或降级（降为 heuristic） | 跨栈反例搜索：桌面 / 嵌入式 / 工具类软件中"低隔离但成功"的系统 |
| RQ-B4 | 哪些流行"最佳实践"实际是 context-dependent tactic（微服务、async、cache、DDD、Clean Architecture、K8s、事件驱动）？各自的适用条件如何精确表述？ | tactics/ 条目的 Applies When / Does Not Apply When | Round 3 对抗评测（表面危险实际合理的设计）直接检验 |

### RQ-C 推理组（资深架构师如何思考）

| ID | 问题 | 预期产物 | 验证方式 |
|----|------|----------|----------|
| RQ-C1 | 任务书 §4 的 12 个 System Model 是否完备且按需可裁剪？典型的推理顺序是什么（是否总是先 Purpose→Boundary→Execution→State→Failure）？ | agent/ 推理工作流（Reasoning Workflow 章节） | 用 3 个不同栈的陌生系统做纸上演练：记录哪些模型被跳过、哪些顺序被调换 |
| RQ-C2 | 高价值架构问题的最小集合是什么？§18 的 33 个候选问题能否归并为 ~60 问的分层 question bank（按模型分组、按模式触发）？ | question-bank/（按 12 模型分组） | 每个问题标注"激活条件"——哪个模型建到哪一步时该问 |
| RQ-C3 | 资深架构师如何决定"停止深挖、开始下结论"？证据充分性的判定规则是什么？ | Evidence Discipline（CONFIRMED / HIGH-CONFIDENCE RISK / HYPOTHESIS / …）的操作化判据 | 在 eval 场景中测量：agent 是否在证据不足时仍下强结论（维度 I） |

### RQ-D 知识工程组（知识库怎么建）

| ID | 问题 | 预期产物 | 验证方式 |
|----|------|----------|----------|
| RQ-D1 | Progressive Disclosure 的最优层级与粒度：router 多短、index 多细、单文件多大，才能让典型任务的总加载量 < 8K tokens？ | 00_ROUTER.md + 各 index 的字数预算（见 §7） | 用 5 种典型任务（PR review / 性能审查 / 方案设计 / ADR 审查 / 事故分析）模拟加载路径并计 token |
| RQ-D2 | relationship-map.yaml 的关系谓词最小集合是什么？（protects / detects / mitigates / trades-off / derives-from / conflicts-with / supersedes） | relationship-map.yaml schema | 导航完整性测试：从任意 FP 出发能沿关系链走到 principle 和 source |
| RQ-D3 | 知识正文语言（中文 vs 英文）与引用保真如何平衡？来源多为英文，Agent 输出要求中文。 | 全库语言规范（待人工决策 Q2） | 抽样 3 个 principle 文件做双语对照评审 |

### RQ-E 评测组（如何证明蒸馏成功）

| ID | 问题 | 预期产物 | 验证方式 |
|----|------|----------|----------|
| RQ-E1 | 30 个场景（25 缺陷 + 5 良构）能否同时测出 recall、precision、教条化三个失败模式？expected findings 如何做到客观（不以知识库作者视角循环论证）？ | eval/scenarios/ + expected-findings/ | 2–3 个场景改编自公开 postmortem（held-out：其答案不预先写入知识库） |
| RQ-E2 | over-engineering 与 product-contract 侵蚀如何量化评分？ | eval/rubric.md 的维度 G/H 刻度 | Round 3 评测的 5 个良构场景 + 种子场景回归 |

---

## 2. Knowledge Domains — Research Clusters

任务书 §5 的 18 个域不改动本体，但研究阶段归并为 11 个簇（cluster）组织检索与蒸馏，避免同轮重复检索同一来源。簇内共享来源、跨簇共享词汇。

| Cluster | 覆盖（§5 编号） | 核心问题 | 优先级 |
|---------|-----------------|----------|--------|
| C1 结构与边界 | 5.1, 5.8(部分) | information hiding 到底保护什么；依赖方向的因果机制；何时不该加 abstraction | P0 |
| C2 运行时与并发 | 5.3, 5.4 | work 在哪执行、谁调度、谁能阻塞谁；concurrency correctness 与 performance 的分离 | P0 |
| C3 资源与性能 | 5.5, 5.6, 5.15 | critical path / bottleneck 定位方法论；boundedness 作为设计纪律；复杂度的增长函数 | P0 |
| C4 失败与隔离 | 5.7, 5.8, 5.9 | 失败传播机制；blast radius 控制；分布式结论的适用边界 | P0 |
| C5 状态与数据 | 5.10 | state ownership / source of truth / 生命周期；schema 演进 | P0 |
| C6 生命周期与所有权 | 5.12 | orphan / stale work / crash-restart 语义；ownership 转移 | **P0（最高）** |
| C7 集成 | 5.11 | contract / versioning / idempotency / ordering / backpressure 的统一框架 | P1 |
| C8 安全 | 5.13 | trust boundary 定位法；架构级（非实现级）安全风险识别 | P1 |
| C9 可观测 | 5.14 | "不可观测 ⟹ 不可可靠运维"的验证；观测的最小充分集 | P1 |
| C10 演进与决策 | 5.16, 5.17, 5.18 | 可逆性；渐进迁移模式；ADR 质量；trade-off 显式化 | P1 |
| C11 Agent 工程 | §7 末组（Spec Kit / Kiro / Anthropic / OpenAI） | 长时任务 agent 的 harness 约束（budget / cancellation / context 切换）如何反哺通用架构原则 | P1 |

C6 标最高优先级的理由：种子 PR prompt 的九个维度里 A/C/D/E 全部落在 lifecycle/ownership/boundedness 上；这是种子案例已验证的高杠杆区。

---

## 3. Candidate Primary Sources

Stage 1 只列候选与优先级；正式 `source-manifest.yaml` 与 `sources/S-*.md` 在 Stage 2 建立。优先级定义：
- **P0**：直接支撑母原则提取
- **P1**：支撑 domain 深化与反例
- **P2**：eval 案例与 held-out 素材

### Tier A — 标准 / 经典论文 / 官方方法论（摘选核心，Stage 2 全量入 manifest）

| 来源 | 年份 | 覆盖 cluster | 优先级 | 备注 |
|------|------|--------------|--------|------|
| ISO/IEC/IEEE 42010:2022 (Ed.2) | 2022 | C1 | P0 | 已验证当前版；architecture vs AD 区分是 A2 的概念基座 |
| ISO/IEC 25010 (quality model) | 2011/2023 | C3,C4 | P0 | 2023 修订状态 Stage 2 核实后入 review-queue |
| Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules" | 1972 | C1 | P0 | information hiding 原文 |
| Brooks, *Mythical Man-Month* + "No Silver Bullet" | 1975/1986 | C1,C10 | P0 | 概念完整性；essential/accidental complexity |
| Bass / Clements / Kazman, *Software Architecture in Practice* + SEI ATAM | 2012/2021 | C1,C3,C10 | P0 | QA scenario / drivers / trade-off 方法学 |
| Gilbert & Lynch, "Brewer's Conjecture…" | 2002 | C4 | P0 | CAP 形式化 |
| Brewer, "CAP Twelve Years Later" | 2012 | C4 | P0 | 作者自我修正——CAP 的适用边界 |
| Lamport, "Time, Clocks…" / "Paxos Made Simple" | 1978/2001 | C4 | P1 | |
| Ongaro & Ousterhout, "In Search of an Understandable Consensus Algorithm" (Raft) | 2014 | C4 | P1 | |
| Fischer / Lynch / Paterson (FLP) | 1985 | C4 | P1 | |
| Dean & Barroso, "The Tail at Scale" | 2013 | C3 | P0 | 尾延迟；queueing 效应 |
| Little, "A Proof for the Queueing Formula L=λW" | 1961 | C3 | P0 | |
| Amdahl, AFIPS 论文 | 1967 | C3 | P0 | |
| Hoare, "Communicating Sequential Processes" | 1978 | C2 | P0 | |
| DeCandia et al, Dynamo (SOSP) | 2007 | C4,C5 | P1 | 部分失败工程化的原始案例 |
| Kleppmann, *Designing Data-Intensive Applications* | 2017 | C4,C5,C7 | P0 | 2nd ed 状态 Stage 2 核实 |
| Nygard, *Release It!* 2e | 2018 | C4,C6 | P0 | circuit breaker / bulkhead 原始出处 |
| Google SRE Book + Workbook | 2016/2018 | C4,C9 | P0 | 官方免费全文 |
| AWS Builder's Library | 持续更新 | C4,C6,C7 | P0 | backoff/jitter/bulkhead/cell-based 官方权威 |
| AWS / Azure / GCP Well-Architected | 持续更新 | C3,C4,C10 | P1 | 三家对照取交集（共识部分证据更强） |
| Saltzer & Schroeder, "The Protection of Information in Computer Systems" | 1975 | C8 | P0 | least privilege / fail-safe defaults / economy of mechanism |
| NIST SP 800-160 v1 + OWASP ASVS | 当前版 | C8 | P1 | |
| Gregg, *Systems Performance* 2e | 2020 | C3 | P1 | |
| Node.js 官方 Event Loop 文档 / SQLite / PostgreSQL(MVCC) 架构文档 | 当前版 | C2,C5 | P1 | 单机/嵌入式侧的官方机制文档，对冲分布式偏差 |

### Tier B — 公认研究者与工程组织长期著作

| 来源 | 年份 | 覆盖 | 优先级 | 备注 |
|------|------|------|--------|------|
| Fowler, *PoEAA* + bliki 精选（Microservices / MonolithFirst / CQRS / EventSourcing / StranglerFig / TechnicalDebt / PresentationDomainDataLayering） | 2002–2015 | C1,C5,C7,C10 | P0 | bliki 全部一手，martinfowler.com |
| Evans, *DDD* | 2003 | C1 | P1 | bounded context / ubiquitous language |
| Martin, *Clean Architecture* | 2017 | C1 | P1 | **刻意降权读取**：只取依赖倒置机制论证，不作规范依据 |
| Richards & Ford, *Fundamentals of Software Architecture*；Ford 等, *The Hard Parts* | 2020/2021 | C10 | P1 | trade-off 案例集 |
| Hohpe & Woolf, *Enterprise Integration Patterns* | 2003 | C7 | P0 | 集成语义（idempotency/ordering/correlation）原始框架 |
| Newman, *Building Microservices* 2e | 2021 | C4,C7 | P1 | |
| Abadi, PACELC（作者博客） | 2012 | C4 | P1 | 一手研究者材料 |
| Kleppmann, "Please stop calling databases CP or AP" | 2015 | C4 | P1 | 去教条化关键证据 |
| Gunther, Universal Scalability Law（论文与著作） | 1993–2007 | C3 | P1 | 证据充分才保留为理论条目，否则标 CONTESTED |
| Shostack, *Threat Modeling* | 2014 | C8 | P1 | |
| Smith, "Notes on structured concurrency"（trio）+ JEP 453 + Kotlin coroutines guide | 2018– | C2,C6 | P0 | cancellation / ownership 的一手现代来源 |
| GitHub Spec Kit（github/spec-kit） | 当前 | C11 | P0 | 已验证；constitution→spec→plan→tasks 流程 |
| Kiro 官方文档（kiro.dev/docs） | 当前 | C11,A3 | P0 | 已验证；EARS 格式官方出处 |
| Anthropic, "Building Effective Agents" + context engineering 等工程文章 | 2024– | C11,C6 | P0 | 已验证 URL |
| OpenAI, "A Practical Guide to Building Agents" | 2025 | C11 | P0 | 已验证 PDF |

### Tier C — 高价值案例 / Postmortem（主要服务 eval 与 held-out）

| 案例 | 年份 | 服务对象 | 优先级 |
|------|------|----------|--------|
| AWS S3 大规模故障官方复盘（重试放大） | 2017 | FP-RETRY 类 held-out | P2 |
| GitHub 24h 降级复盘（维护编排失败） | 2018 | FP-ORCHESTRATION held-out | P2 |
| Cloudflare 正则回溯事故（runtime 失败隔离） | 2019 | C2/C4 案例 | P2 |
| Knight Capital（部署/复用旧代码/flag） | 2012 | C10 案例；SEC 报告为证 | P2 |
| Facebook BGP 级联断网复盘 | 2021 | C4 案例 | P2 |
| CrowdStrike 根因报告（内容更新无门禁） | 2024 | C10/C8 案例 | P2 |

纪律：Tier D（一般博客、二次解释）仅用于理解辅助，不进入 manifest 证据链；SEO 农场与 AI 聚合内容一律排除。

---

## 4. Source Acquisition Strategy

1. **获取顺序按优先级**：P0 全量 → P1 按 cluster 检索需要逐个补入 → P2 在 Stage 10（评测设计）前完成。
2. **访问路径**：官方免费在线优先（sre.google、AWS Builder's Library、martinfowler.com、kiro.dev、github/spec-kit、anthropic.com/engineering、cdn.openai.com、ISO OBP 预览、arXiv/作者主页论文）。付费书籍只做高密度概括 + 章节定位，不复制大段文本。
3. **manifest schema（Stage 2 落地）**：
   ```yaml
   - source_id: S-001
     title: ...
     author_or_organization: ...
     year: ...
     url: ...
     source_type: standard | paper | book | official-doc | postmortem | engineering-blog
     authority_tier: A | B | C
     topics: [boundaries, information-hiding]
     clusters: [C1]
     last_verified: YYYY-MM-DD
     status: active | needs-review | superseded
     notes: 高密度概括 + 关键位置（页/节/段）
   ```
4. **验证纪律**：每个来源记录访问日期；两个权威来源冲突时**双双收录**并标 CONTESTED，不裁决。
5. **停止条件（沿用任务书 §42）**：找不到 primary source / 权威真实冲突 / 理论与实践明显冲突 / 高度依赖技术栈 / 仅个人观点支撑 → 标 UNKNOWN / CONTESTED / CONTEXT_DEPENDENT / NEEDS_EVIDENCE，不为完整性补全。

---

## 5. First-Principles Hypotheses to Test

母原则最终数量目标 **12–16 条**（任务书允许 8–20；取中偏收敛）。候选假设的证伪设计：

### 原有六候选

| ID | 假设 | 证伪/重构问题 | 预判（待证据） |
|----|------|----------------|----------------|
| H1 | Purpose Fitness | 探索型系统目的漂移是常态；"目的"能否操作化为"required properties + drivers"？与 H9 是否合并为 Contract Preservation？ | 保留，但重述为可操作形式 |
| H2 | Clear Boundaries & Ownership | boundary（静态依赖）与 ownership（动态责任）机制不同——Parnas 讲依赖方向，lifecycle 讲资源责任。反例：SQLite amalgamation / Linux monolith 高耦合但成功 | **拆分为两条候选**：H2a Explicit Boundaries（信息隐藏/依赖方向）、H2b Explicit Ownership（谁创建/停止/清理） |
| H3 | Bounded & Predictable Execution | 批处理/离线可接受无界运行 → 真正的轴是"交互关键路径 vs 可延迟工作"还是"资源类别"？ | 保留；boundedness 作为统一失败机制做覆盖测试（RQ-B2） |
| H4 | Failure Containment（failure power ≤ responsibility） | 跨栈反例：单进程桌面软件、CLI 工具接受整体崩溃；成本分级是否让该原则降为 graded heuristic？ | 保留但预计带分级适用条件 |
| H5 | Evolvability | 是否只是 Reversibility + Change Locality + Compatibility 的合成词？合成原则应拆开 | **拆分检验**：H5a Reversibility、H5b Change Locality、H9 Compatibility；Evolvability 可能不再是独立母原则 |
| H6 | Legibility & Operability | 反例搜索：不可观测但自愈良好的极简系统？可观测但运维灾难的系统？ | 保留"可判定性"内核：无法区分正常/异常 ⟹ 无法可靠运维 |

### 新增候选（研究阶段引入，同样待证伪）

| ID | 假设 | 来源线索 |
|----|------|----------|
| H7 | Reversibility（单向/双向决策分级，one-way vs two-way doors） | Type 1/2 decisions；ADR 实践 |
| H8 | Locality（change / data / failure 三个 locality 是否同一原则的三种投影） | Parnas 变更局部性；性能文献数据局部性；bulkhead 故障局部性 |
| H9 | Contract Preservation（实现约束不得静默重定义产品契约） | 任务书 §20 候选；API/schema 兼容文献 |
| H10 | Controlled Complexity（minimum complexity required to safely protect required properties；essential vs accidental；coordination cost） | Brooks；Nygard；任务书 §34 |
| H11 | Least Trust（trust boundary 显式化 + 最小权限 + fail-safe defaults） | Saltzer & Schroeder |
| H12 | Single Source of Truth per State（每个状态恰好一个权威 owner；是否并入 H2b 待定） | DDIA；CQRS 文献的反面教训 |

### 证伪流程（每条假设必过）

Extract → Normalize → Compare → **Falsify（强制：至少一个反例搜索记录）** → Reduce → Operationalize。任何原则若只有单一来源族（如同一位作者的著作）支撑，不得进入 Constitution，只能停在 domains 层的 heuristic。

---

## 6. Known Bias Risks

| ID | 偏差 | 缓解措施 |
|----|------|----------|
| B1 | Clean Architecture / DDD 传播声量大，易被当成默认正确 | 显式降权读取；其主张必须另找独立来源族支持才能升级 |
| B2 | Postmortem 幸存者偏差（只有大厂大事故被记录） | 案例仅作 FP 佐证与 held-out，不作为原则唯一证据 |
| B3 | **分布式/云原生偏差**：现代架构文献以服务端为主，桌面/嵌入式/本地工具欠代表 | 刻意配比：Node.js/SQLite/Electron 官方文档、structured concurrency、桌面软件所有权案例进 P0/P1 |
| B4 | 新鲜度 vs 经典性的锚点冲突 | 以"是否仍解释当前系统行为"为准，不以年代为准（Little 1961 与 2025 的 agent harness 并列） |
| B5 | 确认偏差：研究者倾向证明候选假设 | PHASE D 强制证伪 + Round 3 专门测教条化 |
| B6 | 种子 prompt 的 Electron/FS 痕迹泛化为隐含假设 | PR_REVIEW_MODE 重写时先做栈无关化，Electron 作为 annex 而非主干 |
| B7 | eval 循环论证：出题人=知识作者 | 2–3 个场景取自公开 postmortem，答案不写入知识库（held-out） |
| B8 | "把知识塞进 prompt"的引力 | 制度约束：System Prompt 不得复制知识正文，只含导航契约；评审时逐段检查 |
| B9 | 英文生态中心 | 术语表保留多来源原始用语映射；中文源默认不入证据链（除非人工决策 Q8 指定） |

---

## 7. Proposed Knowledge Architecture

目录骨架沿用任务书 §11，以下是落地约束与微调建议：

1. **规模预算（硬约束）**
   - `00_ROUTER.md` ≤ 80 行（含路由表）：只答"有什么 / 去哪读"，零知识正文。
   - `01_CONSTITUTION.md` ≤ 150 行：12–16 条母原则，每条 ≤ 8 行（一句话原则 + 一句 Why + protects + 关联）。
   - `02_VOCABULARY.md` ≤ 200 行：术语 → 统一词 → 多来源原始用词映射。
   - domains 每域：`index.md` ≤ 60 行 + 2–5 个正文文件，单文件目标 ≤ 200 行。
   - failure-patterns 15–25 个 FP；tactics 15–20 个 T；decision-playbooks 6–10 个 DP；question-bank 按模型分组共 60–100 问。
   - 单条知识文件 YAML frontmatter 沿用任务书 §12 示例，增补 `version` 与 `superseded_by` 两字段。
2. **relationship-map 谓词枚举（RQ-D2）**：`protects` / `violated-by` / `detected-by` / `mitigated-by` / `trades-off-with` / `derives-from` / `conflicts-with` / `supersedes`。只允许闭集，保证可导航性。
3. **Progressive Disclosure 路径契约**：
   `00_ROUTER → (按需) 01_CONSTITUTION → domains/<x>/index → 相关 P-* → 相关 FP-* → DP-*（存在选择时）→ S-*（仅争议/高风险/用户要求时）`。典型任务目标加载量 < 8K tokens（RQ-D1 验证）。
4. **domains 结构微调（待决策 Q5）**：AI Agent Runtime 不新增独立域，并入 `runtime/`，理由：agent harness 的 budget/cancellation/context-switch 问题在机制层与 runtime/lifecycle 同构；但在 question-bank 单设 agent 触发组。
5. **principles/ 与 tactics/ 强制分离**（任务书 §15）：入库时逐条检查——回答"这是机制还是手段"，手段一律进 tactics/。

---

## 8. Evaluation Strategy

1. **场景集**：30 个 = 任务书 §28 的 25 个缺陷场景 + 5 个 GOOD ARCHITECTURE 反例场景（抑制假阳性：正确使用的 async/cache/queue/worker/共享库/microservice 等）。材料形态为"小型 repo/spec/diff/ADR"三种粒度，控制单场景成本。
2. **评分维度**：A–J 十维（任务书 §29），每维 0/1/2 三档；关键阈值建议：
   - B（Issue Detection Recall）≥ 0.80（关键缺陷）
   - C（Precision）≥ 0.67（报告问题至少 2/3 真实）
   - G（Scope Discipline）：单场景 over-design 计数 ≤ 1
   - H（Product Preservation）：静默削减产品能力 = 0 容忍
3. **三轮对抗**（任务书 §31）：R1 明显失败测 recall → R2 隐蔽跨组件失败测 execution reasoning → R3 表面危险实际合理测 false positive。每轮记录 Missed / FP / Over-design / Wrong-assumption 四清单。
4. **Held-out 盲测**：2–3 个场景改编自 Tier C postmortem，expected findings 来自事故报告本身，知识库不预含该案例答案。
5. **回归纪律**：Stage 11 修复后全量重跑 30 场景，输出 delta 报告；修复必须优先落在知识文件（principles/FP/question-bank），System Prompt 只允许改导航与契约——每次修复在 review-queue.yaml 留痕。
6. **执行预算（待决策 Q3）**：30 场景 × 3 轮 + 重跑 ≈ 120–150 次 agent 调用；需指定跑批模型。

---

## 9. Estimated Distillation Stages

| Stage | 产物 | 验收 gate |
|-------|------|-----------|
| 1 研究计划（本文档） | 本文档 | 用户审核通过 |
| 2 来源收集 | source-manifest.yaml + sources/S-*.md | ≥ 25 个 Tier A/B 来源入册，每个含 notes 与 last_verified |
| 3 词汇归一 | 02_VOCABULARY.md | ≥ 15 组跨来源术语冲突完成映射 |
| 4 原则提取 | 候选原则 20–30 条 | 每条有 ≥ 1 个独立来源族 + evidence_class 标注 |
| 5 证伪评审 | 反例记录 | 每条候选 ≥ 1 次证伪搜索记录（结果可为"未找到反例"） |
| 6 一阶归并 | Constitution 草案 | 母原则 ≤ 20 条（目标 12–16） |
| 7 知识架构 | domains/ + failure-patterns/ + tactics/ | 规模预算达标；关系闭集校验通过 |
| 8 推理模型 | decision-playbooks/ + question-bank/ | 每模式有触发条件与停止条件 |
| 9 Agent v0.1 | ARCHITECTURE_EXPERT_SYSTEM_PROMPT.md 草案 | Prompt 无知识正文复制（抽查通过） |
| 10 评测 | eval/ 全套 + 首轮结果 | 30 场景跑完，recall/precision 记录入库 |
| 11 修复 | 知识 diff + review-queue | 修复落在知识文件的占比 ≥ 70% |
| 12 Agent v1.0 | 最终 prompt + 11 个 MODE 文件 | 三轮对抗达标（§8 阈值） |
| 13 蒸馏报告 | reports/ 四件套 | DISTILLATION_REPORT 完整回答 §40 的 14 问 |

依赖关系：2→3→4→5→6 严格串行；7 可与 4–6 部分并行；8 依赖 6+7；10 依赖 9；11↔10 迭代；12→13。

---

## 10. Questions Requiring Human Decision

以下问题有真实的决策权归属，Agent 不代答：

| ID | 问题 | 我的建议（仅供参考） |
|----|------|----------------------|
| Q1 | 知识库根目录位置与最终消费方式（本地目录 / git 仓库 / 打包给哪些 agent 用） | 当前 workspace 下 `architecture-expert/`，git 化管理 |
| Q2 | 知识正文语言：英文（引用保真、来源同语）还是中文（消费端一致） | 正文英文关键术语 + 中文行文混合：术语/原则 statement 英文，解释中文；与 seed prompt 的输出规范一致 |
| Q3 | Stage 10 评测的跑批模型与预算（120–150 次调用跑在哪个 provider） | 用当前可用 provider 中的强推理模型跑正式轮，弱模型只做冒烟 |
| Q4 | 母原则数量偏好：8–12（极简）还是 12–16（完整） | 12–16，允许评测后收缩 |
| Q5 | Agent Runtime 是否单列一等知识域 | 并入 runtime/ + question-bank 单设触发组（见 §7.4） |
| Q6 | PR_REVIEW_MODE 泛化后，Electron/FS 专项是否保留为 stack annex | 保留为 annex，主干栈无关 |
| Q7 | review-queue.yaml 的人工复核角色由谁承担 | 森几本人；Agent 只登记不裁决 |
| Q8 | 是否纳入中文权威来源 | 默认不纳入（Tier 纪律）；如需指定请给出名单 |

---

## 附：本计划自检

- [x] 十项要求全部覆盖（研究问题 / 知识域 / 来源 / 获取策略 / 假设 / 偏差 / 知识架构 / 评测 / 阶段 / 人工决策）
- [x] 未开始任何来源收集（Stage 2 行为）
- [x] 未预写任何原则结论（全部标注"待证据/预判"）
- [x] 与任务书 §1–§44 无冲突；微调点（domains 归并、agent runtime 并域）已列为待决策项
