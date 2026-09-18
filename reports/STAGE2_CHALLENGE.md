# STAGE2_CHALLENGE — Independent Challenger Report

- **角色**: WorkBuddy (Independent Challenger, Research Mode / GLM 5.3)
- **分支**: `challenge/stage2-workbuddy`
- **基线**: main @ `db5c6d6` ("chore: enter Stage 2 source collection")
- **挑战对象**: `planning/STAGE1_RESEARCH_PLAN.md` (PLAN-STAGE1-CANONICAL, 经 PR #2 合入 main) §4 候选来源地图与 §5 研究问题映射
- **日期**: 2026-09-17
- **边界声明**: 本报告不修改 Primary Researcher (Kimi) 的 corpus（`research/stage2-kimi` 当前 == main，corpus 尚未推送，故本轮挑战对象为权威计划的来源地图与高影响来源抽样验证）。不进入 Stage 3。

---

## 0. 挑战方法（How this challenge was run）

按 Issue #3 Challenger 职责清单执行：

1. **抽样验证**：对权威计划 §4 中标注"高影响"的来源做独立版本/现状核查（不是复述，是重新查证发布状态、版本、可得性）。
2. **覆盖审计**：将 §4.1–§4.7 候选来源按"系统形态"（system shape）重新分类，量化 backend/distributed/cloud 与其他形态的权重失衡。
3. **遗漏扫描**：针对 Issue #3 点名的欠代表形态（Desktop/Mobile、Embedded/Edge、Local AI Tool、单进程、非云运行时）检索候选来源家族，附出处与挑战者 ID。
4. **预登记核查项**：为 Kimi corpus 落地后的正式对账预登记机器可检查的清单（§5）。
5. 全程不预设 corpus 内容——在 corpus 落地前，本报告的覆盖性发现针对的是**计划的来源地图**，而非 Kimi 的实际产出。

证据分级沿用权威计划 §7：NORMATIVE / THEORETICAL / EMPIRICAL / HEURISTIC / CONTESTED / CONTEXT_DEPENDENT / UNKNOWN / NEEDS_EVIDENCE。

---

## 1. 抽样验证结果（High-impact source verification）

对计划中高影响来源的独立核查结论：

| 计划引用 | 验证结论 | 状态 | 影响 |
|---|---|---|---|
| ISO/IEC 25010 | **版本漂移风险已发生**：25010:2011 已撤销，现行版本为 ISO/IEC 25010:2023（Ed.2，2023-11-15 发布）。"quality in use" 新增，safety 独立成特性，family 扩展至 25002:2024 / 25019:2023 | NEEDS_EVIDENCE→已证实 | **P1**。若 corpus 落地时引用 2011 版特性清单即为陈旧证据。预登记核查项 C-01 |
| Kleppmann, DDIA | **版本漂移风险**：第 2 版已确认（Kleppmann + Riccomini，O'Reilly Early Release，~600 页，融入 cloud-native 与 AI 内容）。正式版发布日期未定 | NEEDS_EVIDENCE | P2。引用时必须标注版次与"Early Release"状态。预登记 C-02 |
| Saltzer & Schroeder 1975 | 可得性确认：MIT 公开 PDF（web.mit.edu/saltzer/www/publications/rfc/csr-rfc-060.pdf，~96 页）。无版本问题（历史文献冻结） | 已证实 | 无。H10/H11 的理论锚点稳固 |
| Kiro spec-driven dev | 存在且活跃（kiro.dev/docs，EARS 记法）。属**厂商产品文档**而非同行评审文献 | CONTEXT_DEPENDENT | P2。作为 Agent Runtime 域 HEURISTIC 级证据可用，不可作 NORMATIVE |
| Electron process model | 官方文档确认（electronjs.org/docs)：main/renderer/utility 多进程模型 | 已证实 | 支持把 Electron 从"附录"提为 Desktop 域候选（见 §3.2） |
| WASI Preview 2 / Component Model | 官方（wasi.dev）确认：capability-based 安全、组件模型、embedded/edge/插件场景 | 已证实 | **强候选**，同时覆盖 Embedded/Edge 与 Local AI Tool 形态（见 §3.4） |

**挑战结论 CH-01（P1，版本漂移）**：权威计划引用 ISO/IEC 25010 未标注年份，而 2011→2023 版结构性变化（safety 独立、quality-in-use 新增）足以改变 NFR 域的特性映射。corpus 落地时必须按 2023 版核对，任何引用 2011 特性树的条目应记为陈旧证据并进 review queue。

**挑战结论 CH-02（P2，Early Release 引用纪律）**：DDIA 2e 处于 Early Release，章节集不稳定。引用需版次+日期戳，否则跨 Stage 不可复现。

---

## 2. 覆盖审计：系统形态权重失衡（Overrepresentation finding）

把 §4.1–§4.7 候选来源按主系统形态重新归类（同一来源只计主形态，交叉的计入次形态备注）：

| 形态 | 候选来源计数（§4） | 占比 | 对应计划章节 |
|---|---|---|---|
| Backend / 分布式 / 云 | ~26（Google SRE、AWS Builder's Library、DDIA、CAP、Raft、Paxos、Spanner、Dynamo、Kafka、microservices、Temple 的 systems、信号量/互斥论文走服务化解读…） | **~72%** | §4.1–§4.4 主体 |
| 数据/存储系统（偏服务端） | ~4（SQLite 已列但被归"附录"，LMDB 未列） | ~11% | §4.4 |
| 桌面/移动 | ~2（Electron、Node 事件循环——且都被标为"annex 附录"） | ~6% | §4.7 |
| 嵌入式/边缘 | ~0 | **0%** | 无 |
| Local AI Tool / 单进程运行时 | ~0（Agent Runtime 域的引用全部面向服务端 agent 框架） | **0%** | §4.6 |
| 前端/浏览器运行时 | ~0（Web 平台约束未入图） | 0% | 无 |

**挑战结论 CH-03（P1，结构性偏差，EMPIRICAL 对计划文本）**：候选来源地图存在显著 backend/distributed/cloud 过代表——嵌入性与边缘形态完全缺席，Local AI Tool 与单进程系统在 Agent Runtime 域被"跨切面域"决定（Stage 1 已决策）吸收后**没有任何具体来源兜底**。这与 Issue #3 的点名完全一致，也与权威计划自己声明的"18 域最低覆盖"中 Desktop/Mobile、Embedded 域（隐含在 D 列表）形成承诺-资源落差。

**挑战结论 CH-04（P2，'附录'降级的传染效应）**：Stage 1 决策把 Electron/Node 事件循环标为"stack annexes"是合理的主干纪律，但 §4 中 Desktop 形态**仅有**这两条且都在附录位。当欠代表形态的全部来源都处于附录位时，"sparse domains 不降低证据标准"的 Stage 1 决策会在执行时被读成"sparse domains 顺带也降低收录优先级"——建议 owner 明确：附录位不等于优先级降级（见 §6 D-2）。

**挑战结论 CH-05（P2，方法论偏差风险）**：§4 的分布偏斜会通过 H1–H11 的例证选择反向污染第一性原理本身——例如 H3（Bounded Execution）与 H4（Failure Containment）几乎全部例证来自进程外/跨机边界（容器、超时、断路器），而单进程形态的同类机制（协作式取消、structured concurrency、协程作用域、UI 主线程约束）零例证。这不是假设错误，是**例证基率偏移**，会在蒸馏阶段让原理获得隐性的"分布式味道"。标注：CONTEXT_DEPENDENT——修复方式是补例证而非改假设。

---

## 3. 遗漏来源家族（Proposed additions，附出处）

以下为建议 Primary track 增补的候选来源。**本报告仅提案，不写入 corpus**。每条附：形态覆盖、证据级别预设、出处。

### 3.1 单进程数据系统 / 嵌入式存储（Single-process, non-cloud）

- **CH-S-01 · SQLite architecture（hippyhippoblog / SQLite 官方文档 35% 磁盘讲解）** — 形态：单进程嵌入式数据库。架构价值：单文件 ACID、WAL、跨平台 ABI 稳定（25+ 年）。证据级预设 EMPIRICAL（描述已部署系统）。出处：sqlite.org/arch.html; hippyhack 博客系列。支撑 H2a/H8/H9（单进程内边界与兼容性）。
- **CH-S-02 · LMDB（Lightning Memory-Mapped Database）论文与设计文档** — 形态：单进程、零拷贝、B+树、copy-on-write MVCC。架构价值：非云事务与崩溃一致性的教科书反例集。证据级 EMPIRICAL。出处：symas.com/lmdb; Howard & Chu 2011 ("LMDB: A Memory-Mapped Database")。

### 3.2 桌面 / 桌面级进程模型（Desktop）

- **CH-S-03 · Electron 官方 process model 文档（升级：从附录提为 Desktop 域候选）** — main/renderer/utility 进程隔离、contextIsolation、IPC 最小面。价值：Desktop 形态下 H2a/H3/H10 的直接例证。证据级 NORMATIVE（厂商规范定义进程契约）。出处：electronjs.org/docs/latest/latest/process-model。交叉：CSP、preload 沙箱即 capability 模式。
- **CH-S-04 · Windows API 一致性 / Win32 应用兼容性工程（Raymond Chen, The Old New Thing）** — 形态：Desktop，25 年 ABI 兼容的极限案例。价值：H8（兼容性/契约保持）的最强非云例证之一。证据级 HEURISTIC（工程实践记录）。出处：devblogs.microsoft.com/oldnewthing/ 及《The Old New Thing》书。

### 3.3 移动（Mobile）

- **CH-S-05 · Android 架构文档（进程优先级/生命周期/权限模型）** — 形态：Mobile。价值：受限资源下的生命周期状态机、进程分级回收，是 H3/H4 在 OS 调度层的镜像。证据级 NORMATIVE（平台规范）。出处：developer.android.com/guide/components/…; process lifecycle 文档。
- **CH-S-06 · iOS App 生命周期与后台执行约束文档** — 同上，对照性收录（两平台对同一问题的不同裁决）。证据级 NORMATIVE。出处：developer.apple.com/documentation/…

### 3.4 嵌入式 / 边缘（Embedded / Edge）

- **CH-S-07 · WASI Preview 2 / Component Model（官方规范与 wasi.dev 文档）** — 形态：Embedded/Edge/插件。价值：capability-based 安全（与 Saltzer & Schroeder 直接呼应）、组件级边界、非云沙箱执行。证据级 NORMATIVE（规范）/ THEORETICAL（component model 形式化）。出处：wasi.dev; component-model proposal (GitHub)。**单条来源同时修复两处空白**。
- **CH-S-08 · FreeRTOS / Zephyr 设计文档（任务调度、内存确定性、静态分配策略）** — 形态：Embedded RTOS。价值：H3/H9 在硬资源约束下的形态（确定性、无动态分配选项）。证据级 EMPIRICAL/NORMATIVE 混合。出处：freertos.org; zephyrproject.org 文档。
- **CH-S-09 · MISRA C / IEC 61508 功能安全标准家族概览** — 形态：安全关键嵌入。价值：受限语言子集作为架构约束（H1/H4 的语言级实现）。证据级 NORMATIVE。注意：付费标准，按 Stage 1 决策采用"公开解读文献"策略。出处：misra.org.uk 公开材料。

### 3.5 Local AI Tool / 端侧推理（Local AI Tool）

- **CH-S-10 · ONNX Runtime / llama.cpp 架构文档** — 形态：本地推理运行时。价值：单进程内存层级管理（KV cache、mmap 权重、量化权衡）、非服务端部署形态。证据级 EMPIRICAL。出处：onnxruntime.ai; github.com/ggml-org/llama.cpp（README+discussions 的架构讨论）。
- **CH-S-11 · MCP (Model Context Protocol) 规范** — 形态：Local-first agent 工具调用。价值：Agent Runtime 域中**非云假设**的标准契约（本地 stdio 传输、能力协商）。证据级 NORMATIVE（规范）。出处：modelcontextprotocol.io。修复 Agent Runtime 域全部引用面向服务端框架的问题。

### 3.6 浏览器 / Web 运行时（计划未列，建议 owner 裁决）

- **CH-S-12 · Web 平台约束文档（WHATWG HTML Living Standard 选段 + web.dev 性能预算材料）** — 形态：浏览器运行时（全球部署面最大的单一运行时之一）。价值：主线程约束（H3 的 UI 级形态）、渐进增强（H8）、资源预算。证据级 NORMATIVE。出处：whatwg.org; web.dev。**是否纳入 Desktop 域还是独立，属 owner 决策（见 §6 D-3）**。

---

## 4. 反证与弱证据登记（Counter-evidence & weak-evidence ledger）

- **CH-W-01（CONTESTED 预登记）**：微服务 vs 单体的经验证据长期弱（多数为 HEURISTIC 级厂商内容）。若 corpus 将"每个服务单一职责/独立部署"作为 NORMATIVE 收录，应记 CONTESTED——存在同等量级的反方文献（monolith-first：如 Shopify Modular Monolith、Amazon Prime Video 2023 回迁案例报告）。出处：shopify.engineering; aws.amazon.com/blogs/…prime-video…。建议 corpus 落地后逐条核对。
- **CH-W-02（CONTEXT_DEPENDENT 预登记）**：CAP 定理的常见转述常超出定理本身（ Partition Tolerance 语义、网络切换场景）。若 corpus 出现"三选二"表述即为教科书式弱证据，应替换为 Gilbert & Lynch 2002 原文 + Brewer 2012 澄清 ("CAP twelve years later")。出处：IBM J. Res. Dev. 2012。
- **CH-W-03（HEURISTIC 上限）**：Google SRE / AWS Builder's Library 属高价值工程叙事，但为单一厂商经验（幸存者偏差 + 组织耦合）。建议证据级上限 HEURISTIC，禁止升格为 NORMATIVE，与 Stage 1 "来源语言/厂商不构成权威标准"决策一致。
- **CH-W-04（NEEDS_EVIDENCE 预登记）**：Kiro/EARS 作为 spec-driven 开发的代表性证据目前只有厂商文档，缺独立第三方采用报告。若 corpus 引用应标 NEEDS_EVIDENCE（采用效果），文档本身可作 NORMATIVE（记法定义）。

---

## 5. 预登记核查清单（Corpus 落地后对账，机器可检查）

Kimi 的 `research/stage2-kimi` 当前等于 main（corpus 未推送）。为 corpus 落地后的正式对账预登记以下检查项：

| ID | 检查项 | 关联 |
|---|---|---|
| C-01 | 所有 ISO/IEC 25010 引用必须为 2023 版；2011 特性树条目标陈旧 | CH-01 |
| C-02 | DDIA 引用必须含版次+状态（1e/2e-ER+日期） | CH-02 |
| C-03 | source-manifest.yaml 中 Desktop/Mobile/Embedded/Local-AI/single-process 形态来源 ≥1 条/形态；当前计划基线为 0/0/~2(附录)/0/0 | CH-03 |
| C-04 | 每条 S-*.md 的 evidence-class 不高于 §4 预设；厂商文档（SRE/AWS/Kiro）上限 HEURISTIC | CH-W-03/04 |
| C-05 | H3/H4/H5 例证基率审计：非分布式形态例证占比报告（不设硬门槛，但必须出数） | CH-05 |
| C-06 | CAP 相关条目无"三选二"表述；引用含 Brewer 2012 | CH-W-02 |
| C-07 | 微服务收益类条目存在 monolith-first 反方对照或标 CONTESTED | CH-W-01 |
| C-08 | SQLite/LMDB 若收录，须走单进程数据系统定位而非"云数据库的简化版"叙事 | CH-S-01/02 |

---

## 6. 真正需要 owner 决策的问题（Genuine owner decisions）

仅列无法由 Challenger/Primary 自行裁决的：

- **D-1（P1）**：Embedded/Edge 与 Local AI Tool 形态在 §4 候选地图为 0。是否将 §3.4/§3.5 的提案（CH-S-07…CH-S-11）纳入 Primary track 的正式收集范围？还是接受"sparse domain"记录并留待后续 Stage 补？**这直接决定 C-03 的门槛值。**
- **D-2（P2）**："附录位"（stack annexes）语义澄清：附录是否等价于收录优先级降级？建议否——附录只是"不入主干原理推导"，收录优先级应与域稀缺度正相关（稀缺形态优先）。
- **D-3（P2）**：Web/浏览器运行时（CH-S-12）是否入域？三选一：并入 Desktop 域 / 独立子域 / 暂不收录。涉及 18 域清单是否变动的 Stage 1 决策边界。
- **D-4（P2）**：DDIA 2e Early Release 的引用策略：允许引用 ER 版（标注+日期戳）还是冻结在 1e？ER 内容含 cloud-native/AI 章节恰是高价值部分。
- **D-5（P3）**：CH-05 的例证基率审计（C-05）是否设硬门槛（如"每条原理至少 1 条非分布式例证"）还是仅报告？硬门槛会强制收录，软报告可能被忽略。

---

## 7. 挑战者元声明

- 本轮挑战在 corpus 缺席条件下进行，§2 的权重统计基于权威计划文本，属**对计划的挑战**；corpus 落地后需按 §5 清单重跑覆盖对账，届时结论以 corpus 为准。
- 挑战不针对 Primary Researcher 的能力，针对的是**单一研究者路径的系统风险**（Issue #3 设立 Challenger 的初衷）。
- 全部网络验证于 2026-09-17 (GMT+8) 完成；URL 级出处已在各条目内注明，正式收录时 Primary 须复核可得性。
