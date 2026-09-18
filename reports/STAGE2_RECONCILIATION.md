# STAGE2_RECONCILIATION — Pass B Corpus Reconciliation

- **角色**: WorkBuddy (Independent Challenger, Research Mode / GLM 5.3)
- **分支**: `challenge/stage2-workbuddy`（Pass B 产物；本报告不修改 Kimi corpus）
- **审计对象（固定）**: `research/stage2-kimi@b85a826b4d678a38c0657678a1c1bbf2a5ab159b`
- **上游输入**: main@db5c6d6 canonical plan；Issue #3 CA checkpoint（2026-09-18）；Pass A 报告 `reports/STAGE2_CHALLENGE.md`@ac7b42a（预注册 C-01..C-08）
- **日期**: 2026-09-18
- **边界**: 未进入 Stage 3；未改写 corpus；本轮 delta 相对 Pass A 预注册，不改写挑战史。

---

## 0. 审计方法

1. `git fetch` + `git archive` 将固定 SHA corpus 落到只读工作副本（112 文件），全程不触碰 `research/stage2-kimi` 分支。
2. 全量读 `source-manifest.yaml`（111 条）、`review-queue.yaml`、`sources/index.md`、`reports/STAGE2_HANDOFF.md`；统计脚本核对 tier/verification/evidence_class/frontmatter 完备性。
3. 跨 5 个 research cluster + 全部欠代表形态抽样深读 28 个 S 文件（S-005/008/011/013/021/023/026/027/030/047/050/062/064/072/073/084/088/091/092/098/104/105/106/107/108/109 + S-106 复核）。
4. 13 条 needs-reverify URL 全部独立 fetch 终验（Node fetch + WebFetch 双栈），真 404/DOI 错误再做 WebSearch 定位正确目标。
5. 按 CA checkpoint 的方法论修正执行：authority tier 与 evidence class 分维审计，逐 claim 检查 scope 是否超出来源支持范围。

---

## 1. 预注册检查 C-01..C-08 重跑结果

| ID | 检查项 | 结果 | corpus evidence |
|---|---|---|---|
| C-01 | ISO 25010 引用必须 2023 版 | **RESOLVED** | S-008 标题/frontmatter 均为 `25010:2023`，核心主张含 "safety（2023 新增）"，9 特性清单与 2023 Ed.2 一致 |
| C-02 | DDIA 引用须含版次+状态 | **PARTIAL** | S-023 固定为 1e（2017）并声明未取得全文——满足"可复现"底线；但 Pass A 预注册背景里 2e Early Release 状态未在 corpus 任何位置登记（manifest 无 DDIA-2e 条目、review-queue 无漂移提醒）。Stage 4 若引用 2e 新增主题（cloud-native/AI 章）无落点 |
| C-03 | 欠代表形态 ≥1 条/形态 | **PARTIAL** | mobile-desktop 2 条（S-105/106）、embedded-edge 1 条（S-104）、local-first 1 条（S-107）、monolith 2 条（S-108/109）；**Desktop 正向权威 0 条**（仅 Apple 负结果 S-106）；browser/runtime 0 条；single-process 专用 0 条（S-107 兼跨） |
| C-04 | evidence class 不高于预设；厂商文档不越权 | **RESOLVED（按 CA 修正后的 claim-relative 标准）** | 全部 111 条 S 文件 evidence_class 与 manifest 一致且 claim-relative：S-105 Android 指南 `normative` 仅限"平台自身推荐架构"scope，争议栏显式标"平台厂商利益"；S-098 Anthropic 标 vendor evidence；S-088 Node.js `normative+empirical` 限运行时契约。未发现厂商文档冒充通用架构规范的条目 |
| C-05 | H3/H4 例证基率审计出数 | **RESOLVED** | 非分布式例证实际存在且被点出：S-062 Knight Capital（单进程死代码+部署，H3）、S-064 CrowdStrike（内核驱动内容更新，H3/H4）、S-091 Pathfinder（RTOS mutex，H3）、S-088 Node 事件循环（H3 运行时形态）。Pass A 担心的"零非分布式例证"不成立 |
| C-06 | CAP 无"三选二"；引用含 Brewer 2012 | **RESOLVED** | S-026 明示"仅适用于原子读/写寄存器语义"+ 争议栏显式反"三选二"；S-027 Brewer 2012 在册且与 S-026 配对；RQ2-004 预登记 Stage 3/4 引用限定 |
| C-07 | 微服务条目有 monolith-first 反方或标 CONTESTED | **PARTIAL** | S-108 DHH + S-109 Shopify 反方在册；但 Fowler «Microservices»（2014）与 «Monolith First»（2015）仍缺席——正方一侧缺一手权威，Kimi 自己在 RQ2-009 承认并建议 Stage 3 前补。不对称依旧存在，只是方向与 Pass A 预想的相反（**反方强、正方缺**） |
| C-08 | SQLite/LMDB 若收录走单进程定位 | **N/A→缺口** | 未收录（可接受，非强制），但 single-process 数据系统家族整体缺席与 C-03 的 browser/single-process 空洞同源 |

**小结**：8 项预注册中 4 项 RESOLVED、3 项 PARTIAL、1 项 N/A 转【RB-03】缺口。Pass A 预注册发挥了作用——C-01/C-04/C-05/C-06 四处在 corpus 里都能找到针对性处理。

---

## 2. Pass A 发现 CH-01..CH-05 裁决

| ID | Pass A 主张 | 裁决 | 依据 |
|---|---|---|---|
| CH-01 | ISO 25010 版本漂移风险（P1） | **RESOLVED** | corpus 直接采用 2023 Ed.2（见 C-01）。风险在落地前被消除 |
| CH-02 | DDIA 2e Early Release 引用纪律 | **PARTIALLY RESOLVED** | 1e 引用干净；2e 漂移未登记（见 C-02）。低危：Stage 4 未开始，可在 principle 提取前补 |
| CH-03 | 来源地图 ~72% backend/distributed/cloud，Embedded/Local-AI 0 条（P1） | **PARTIAL** | 实际 corpus 后端/分布式/云占比约 55–60%（Tier A 77 条中约 43 条），好于计划地图的预测；cluster-e 显式收录 embedded/desktop/local-first/monolith 且 CA D-1/D-2 决议已传导（S-104/105/106/107/108/109 全部在册）。但 Desktop 正向权威、browser/runtime、single-process 仍为 0（见【RB-03】）。计划级结构性偏差被部分修复，未根除 |
| CH-04 | 附录位降级传染效应 | **SUPERSEDED** | corpus 没有 annex 层级；CA D-2 已裁定 annex=scope-specific 而非优先级降级，议题被上游决策取代 |
| CH-05 | H3/H4 例证基率偏移（P2） | **PARTIAL→弱化** | 单进程/非云例证存在（见 C-05），但按形态计数仍 <10%：embedded 1、mobile 2、local-first 1、monolith 2、desktop 0。CA D-5 已给出终局标准（Mother Principle 必须跨实质不同形态测试并记录分布），Stage 4 执行时才见分晓。登记为持续风险 R-1 而非 Stage 2 缺陷 |

---

## 3. 抽样深读发现（28 样本，跨 cluster × 形态）

总体：S 文件质量高于 Pass A 预期——frontmatter 111/111 完整（evidence_class / authority_tier / verification / last_verified / related_rq 全部在位，脚本核验 0 缺失）；claim scope 普遍克制，"争议/误用"栏普遍存在且内容真实（非装饰）。

### RB-01 · 链接腐烂数据（URL reverify 终验）

- **severity: P1（数据完整性）｜status: NEW**
- **corpus evidence**: 13 条 needs-reverify 全部独立 fetch：
  - **真失效 2 条**：S-078 `doi.org/10.1145/3226569` → DOI Not Found（ACM 官方确认为 **10.1145/3232559**，Delimitrou & Kozyrakis CACM 61(8) 65-72）；S-032 `microsoft.com/en-us/research/publication/the-transaction-concept-virtues-and-limitations/` → 404（有效替代：`research.microsoft.com/~gray/papers/theTransactionConcept.pdf`，Tandem TR 81.3 原文，搜索结果直接返回论文全文）。
  - **迁移 1 条**：S-060 GitHub blog 旧路径 200 但重定向到 `/news-insights/company-news/oct21-post-incident-analysis/`（内容在，URL 应更新）。
  - **内容漂移 1 条**：S-106 Apple URL 200 但重定向到 `…/documentation/swiftui/model-data`——"State and data flow" 页已重组，S-106 描述的"事实上立场"文档已非该 URL 内容。
  - **网络栈假阴性 3 条**：S-068（codeascraft，WebFetch 双栈确认文章完整在世）、S-105（developer.android.com，搜索确认 canonical 已是 `/jetpack/arch`）、S-069（netflixtechblog 403 反爬，Medium 系常态）。S-069 本身 URL 只是域名首页而非 2012 Hystrix 文深链——**笔记自己也没给出精确 URL**，这条是真"未定位"。
  - **正常 200**：S-024（PDF 2.2MB）、S-027（405 = InfoQ 拒 GET 以外方法/爬虫，页面在）、S-053（403 MIT 反爬镜像，RQ2-001 已注明"非作者官方站"）、S-065、S-101、S-109。
- **mechanism/risk**: needs-reverify 是 corpus 里唯一"承认未终验"的通道，如果它半数以上是假阴性而真阳性（DOI 错误）混在里面没被区分，下游会把整组当作低置信度噪音，或反过来信任了错误 DOI。
- **required correction**: ①S-078 DOI 改 3232559；②S-032 换 research.microsoft.com 直链；③S-060/S-105 更新为重定向后 canonical；④S-106 重选在世 URL（model-data 或显式登记原 URL 已重组）；⑤S-069 需补精确文章 URL 或降级为"仅历史背景，URL 未定位"；⑥verification 字段建议增加 `bot-blocked-200-verified` 类区分（S-024 直接 PDF 200 可升级 direct-open）。
- **blocks Stage 2 gate**: 否（数据可修，见 remediation R1；但属最小修复集必含项）。

### RB-02 · 计数口径三处不一致

- **severity: P2（一致性）｜status: NEW**
- **corpus evidence**: handoff §统计称 "needs-reverify 9 条"；review-queue RQ2-001 列 12 条 refs；manifest 实际 `needs-reverify` **13 条**（S-024/027/032/053/060/065/068/069/078/101/105/106/109，脚本核验）。handoff 又称 "Tier A 78 / B 30 / C 3"，manifest 实为 **A 77 / B 32 / C 2**；"sources 111" vs 目录 112 文件（多出的是 index.md，口径可解释但 handoff 未说明）；handoff 称 direct-open 38，实为 46。
- **mechanism/risk**: AI consumption 阶段（RQ-D）若以 handoff 统计做路由假设，会系统性低估已验证来源比例、错估 reverify 工作量。多处小口径漂移是 provenance 纪律松动的早期信号。
- **required correction**: 以 manifest 为单一事实源重算 handoff 统计段；RQ2-001 refs 补齐 S-106（13 条）。
- **blocks**: 否。R2。

### RB-03 · 欠代表形态覆盖仍不均（Desktop/browser/single-process = 0）

- **severity: P2（覆盖）｜status: PARTIAL（承 CH-03）**
- **corpus evidence**: 12 系统形态（RQ-A.2）映射：Desktop 正向权威 0（唯一 desktop 相关是 Apple 负结果 + Electron 缺席——Pass A 提案 CH-S-03 未被收录，也未见"验证过但拒绝"的记录）；browser/Web Frontend 0（CA D-3 已裁定不设一级域、跨切面覆盖，但跨切面来源如 WHATWG/web.dev 一条未见）；single-process 专用 0（S-107 local-first 兼跨，SQLite/LMDB 家族 CH-S-01/02 未收录未见处置记录）；Embedded 1（S-104）；Mobile 2。Pass A 12 条提案（CH-S-01..12）在 corpus 与 review-queue 中**均无逐条处置痕迹**——CA D-1 明确 "CH-S-07..11 become mandatory candidate leads for Kimi to verify"，其中仅 WASI/MCP/FreeRTOS/Zephyr/ONNX/llama.cpp 相关（CH-S-07/08/10/11）完全未见，SQLite/LMDB（CH-S-01/02）、Electron（CH-S-03）、Old New Thing（CH-S-04）、iOS（CH-S-06）、Web 平台（CH-S-12，受 D-3 约束）也未见 verify/admit/reject 记录。
- **mechanism/risk**: 违反 D-1 "must not be left empty if credible sources can be found" 的执行闭环——不收录可以，但 mandatory leads 需要显式处置（收录/拒绝/NEEDS_EVIDENCE），否则 Challenger 的 lead 循环断裂，且 Desktop 形态在 Stage 4 跨形态测试（D-5）时无证据可用。
- **required correction**: 最小闭环 = review-queue 增设一条 disposition 表：CH-S-01..12 每条标 admitted / rejected(理由) / needs_evidence；Desktop 至少补 1 条正向权威（CH-S-03 Electron process model 是最低成本候选，CA Pass A 评论已确认其 normative-for-platform-contract 地位）；Embedded 可按 CA 建议补 FreeRTOS/Zephyr 官方设计材料（公开可验证）。
- **blocks**: 否（不阻塞 gate，因为 G1/G2 已如实标 NEEDS_EVIDENCE——Kimi 没有掩盖；但阻塞 Stage 4 跨形态原则测试的就绪度）。R3。

### RB-04 · S-021 等"学术谱系 A 级" Tier 校准

- **severity: P3（分级校准）｜status: CONFIRMED（handoff 自邀挑战点之三）**
- **corpus evidence**: S-021（Jansen & Bosch 2005，WICSA，theoretical）、S-007（Perry & Wolf 1992）等 Tier A：作为"架构=决策集合"概念的一手出处，A 级成立（原创论文、明确 scope、与 ADR/42010 三源印证被显式写出）。抽查未见为凑数而虚高的条目；真正可疑的 S-013 Clean Arch 已主动降 B 并写明"绝不直接接受其结论"。
- **mechanism/risk**: 无实质风险。按 CA 指令"不机械降级 claim scope 明确的原创文献"，维持原判。
- **required correction**: 无。
- **blocks**: 否。

### RB-05 · 数量 vs 信息增益（重复条目检查）

- **severity: P3｜status: RESOLVED（未发现实质问题）**
- **corpus evidence**: 逐对审查最可能重复的族：S-048/S-049（SRE book vs Workbook——内容分工：教科书 vs 实操手册，不重复）；S-072/S-073（Little 1961 定理 + Little 2011 作者自澄清——2011 条目核心价值恰是防超范围引用，与 C-06 同类防御性收录，合理）；S-074/075/076（Amdahl 原文 + Gustafson 修正 + Hill&Marty 多核重述——三篇是争论链不是复述）；S-026/027（定理 + 纠正，配对使用）；S-108/109（立场文 + 企业案例，证据类型不同）。唯一边缘：S-046 Kreps Log 与 S-043 Kafka docs 有主题重叠，但一个讲抽象、一个讲交付语义契约，可保留。
- **mechanism/risk**: 无。111 条无"凑数"痕迹，每条有独立 claim 空间。
- **required correction**: 无。
- **blocks**: 否。

### RB-06 · 厂商文档 normative 边界（用户令牌检查 ⑤）

- **severity: P3｜status: RESOLVED**
- **corpus evidence**: 这是本轮最重点的专项。逐条检查全部 official-doc/standard 34 条中 evidence_class 含 `normative` 的：S-088（Node 事件循环）、S-085/086/087（Kotlin/Swift/Java structured concurrency）、S-105（Android）、S-092 栏（S&S 理论+normative 双标）、S-058（OpenTelemetry spec）、S-090（Reactive Streams spec）等。模式一致：**normative 均指向该平台/规范自身契约**（"Node 回调必须小"、"Kotlin coroutine scope 结构"、"Android 推荐分层"），而通用架构推论处全部降档（S-105 争议栏"厂商利益+过度工程化批评"；S-098/099 vendor evidence 标注；RQ2-008 把 7 条 Agent 工程材料整体登记 CONTEXT_DEPENDENT）。S&S 的 normative 指其作为安全设计原则表述的权威性，同时保留 theoretical——不越权。
- **mechanism/risk**: 未发现需要纠正的越权条目。风险仅在 Stage 4：原则提取时若把 S-088 的"每个回调必须小"直接升格为跨栈原则而非"运行时契约形态的证据"，会复发——已由 CA claim-relative 框架覆盖，登记为持续注意项。
- **required correction**: 无（corpus 层面）；Stage 4 执行清单建议保留 scope 字段。
- **blocks**: 否。

### RB-07 · 付费/离线来源访问边界（RQ2-012 复核）

- **severity: P3｜status: RESOLVED**
- **corpus evidence**: RQ2-012 如实登记 12 条 offline-publication"未读全文"；抽查 S-005/S-023/S-047 的 notes 均有"基于目录/作者公开材料"免责说明。符合 CA paid-source 决议（不装读过的全文、不阻塞 Stage 3、principle 级引用时再升级 NEEDS_EVIDENCE）。
- **required correction**: 无。
- **blocks**: 否。

### RB-08 · USL 双重标记内部不一致

- **severity: P3（数据卫生）｜status: NEW**
- **corpus evidence**: S-079 manifest 的 verification 是 `offline-publication`，但 title 内嵌 "(NEEDS_EVIDENCE: 1993 CMG 原文不可公开验证)"、RQ2-006 标 marker NEEDS_EVIDENCE——同一来源在三个位置用了三种机制表达同一状态。与之对照 S-106 的负结果在 title/frontmatter/queue 三处一致用 NEEDS_EVIDENCE。
- **mechanism/risk**: AI 路由（RQ-D）按结构化字段过滤时，S-079 的警示藏在 title 字符串里，可能被当作普通 offline 书目引用。
- **required correction**: manifest 增加可选 `evidence_marker:` 字段（或统一入 notes 结构化格式），S-079 补标。
- **blocks**: 否。

---

## 4. Gate 建议

### 判定：**PASS_WITH_REMEDIATION**

理由：corpus 的证据纪律、claim scope 控制、矛盾保留（CAP/FLP/USL/strangler 归因/数字口径）、负结果登记均达标且优于 Pass A 预期；预注册检查 8 项无一项 FAIL；无需退回 HOLD。但存在两个数据级硬伤（错误 DOI、死链）与一个 D-1 执行闭环缺口（mandatory leads 无处置记录），应在 Stage 3 前以最小成本修复。

### 最小 remediation 清单（Stage 3 前完成，全部落在 research/stage2-kimi 新 commit）

| # | 项 | 对应 finding | 预估成本 |
|---|---|---|---|
| R1 | 修 2 个真失效 URL（S-078 DOI→3232559；S-032→research.microsoft.com 直链）+ 2 个 canonical 更新（S-060、S-105→/jetpack/arch）+ S-106 重选在世 URL + S-069 补精确文 URL 或降级 | RB-01 | 小时级 |
| R2 | handoff 统计段以 manifest 重算（13/46/41/11、A77/B32/C2）；RQ2-001 refs 补 S-106 | RB-02 | 分钟级 |
| R3 | review-queue 增 CH-S-01..12 逐条 disposition（admitted/rejected+理由/needs_evidence）；Desktop 至少补 1 条正向权威（建议 CH-S-03 Electron）；Embedded 补 FreeRTOS 或 Zephyr 官方设计材料 1 条（公开可验证） | RB-03 | 半天级（验证新来源） |
| R4 | S-079 结构化 marker（evidence_marker 字段或 notes 规范） | RB-08 | 分钟级 |

R1/R2/R4 完成即可开 Stage 3 准备工作；R3 建议与 Stage 3 初期并行，不互相阻塞。

### 持续风险登记（不阻塞，Stage 4 执行时核查）

- **R-1（承 CH-05）**: Mother Principle 提取时按 CA D-5 执行跨形态测试并记录分布——当前例证基率后端约 55-60%，Desktop/browser/single-process 无例证可用（依赖 R3 补齐）。
- **R-2（承 C-02）**: DDIA 2e Early Release 无登记位。Stage 4 引用 2e 主题前须先建条目（版次+快照日期），或显式声明 corpus 锚定 1e。
- **R-3**: postmortem 幸存者偏差（全部为头部厂商公开复盘）——handoff 自邀挑战点，维持登记，Stage 5 评测素材选取时对冲（danluu 索引 S-066 可作扩展入口）。

---

## 5. 真正需要 owner 决策的问题

1. **D-B1**: R3 的处置范围——Challenger leads（CH-S-01..12）的 disposition 与 Desktop/Embedded 补源，由 Kimi 在 remediation commit 一并完成，还是另开 mini-iteration 由 owner 指定人选？涉及对 Primary 的工作量追加授权。
2. **D-B2**: S-069（Netflix Hystrix 2012）是否值得继续考古精确 URL——其历史价值（断路器模式工业史）与考古成本不成比例时可整条降级为"仅历史背景，S-056 已覆盖模式本身"，是否接受该降级由 owner 定。
3. **D-B3**: verification 词表是否扩展（如 `bot-blocked` / `moved-canonical-updated`）以支撑 RB-01⑥ 的区分——词表变更属 schema 变更，按 Stage 1 决策"本体/结构变更需 owner 审批"。

---

## 6. 挑战者元声明

- 本轮全部 URL 终验与检索于 2026-09-18 (GMT+8) 完成，双栈（Node fetch + 独立 fetch 服务）交叉；bot 拦截类（403/405）均以内容检索二次确认后才判"内容在世"。
- 审计只读：corpus 经 `git archive` 快照提取，未 checkout、未触碰 `research/stage2-kimi` 引用。
- 28 样本覆盖率：cluster-a 8 / cluster-b 5 / cluster-c 4 / cluster-d 6 / cluster-e 5，另加 manifest/queue/handoff/index 四份结构性文件全读。
