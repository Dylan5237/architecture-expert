# STAGE3_RECONCILIATION — Independent Challenger Pass B (Vocabulary Reconciliation)

- **角色**: WorkBuddy (Independent Challenger, Research Mode / GLM 5.3)
- **分支**: `challenge/stage3-vocabulary`（基于 Pass A 干净基线 `e6d67b3`）
- **审计对象**: Kimi `research/stage3-vocabulary@3f386db58a5f6679b7188daa4af89ccd35fae36f`（`02_VOCABULARY.md` 672 行 / V-001..V-021 + N-1..N-10；`reports/STAGE3_HANDOFF.md`）
- **输入**: Pass A `STAGE3_COLLISION_AUDIT.md`（e6d67b3）、Issue #6 CA checkpoint（comment 5725432016，含 OD-1..OD-5 + 10 Primary findings + Pass A 假设挑战清单）
- **纪律**: 未修改 Kimi 词汇表；未进入 Stage 4；判定只用 corpus 证据（S-ID + 词条原文）+ CA 已裁决的 owner decision
- **日期**: 2026-09-18

---

## 0. 方法

1. 逐条执行 Pass A 预注册的 V3-01..V3-24，对 Kimi 固定 SHA 的 `02_VOCABULARY.md` 机器化对账。判定四值：**PASS**（检查满足）/ **PARTIAL**（核心保护在场但预注册要素缺失）/ **FAIL**（检查要求的保护不在场）/ **CHECK_INVALID**（检查本身的预注册假设被证伪，检查作废并修正）。
2. 21 条 Pass A collision 逐条对账：已解决 / 部分解决 / 未解决 / 假设修正。
3. 显式评估 CA checkpoint 的 10 条 Primary findings（F-CA-1..10）。
4. 反向审查 Pass A 自身的 alias 假设（RA-1..6）——CA 指令：挑战者也要被挑战。
5. 每个未决项归类到四个处置层：**lexical fix**（Stage 3 内词汇层微修）/ **PROJECT_DEFINED**（保留+标注）/ **PROJECT_META**（OD-1 隔离）/ **Stage 4 泄漏或回填**（不词汇层硬修）。

---

## 1. V3-01..V3-24 判定总表

| Check | 内容 | 判定 | 证据落点 |
|---|---|---|---|
| V3-01 | consistency 裸词条禁令 + RQ2-004 链接 | **PARTIAL** | V-010 专族 + 强制后缀 ✓；RQ2-004 显式链接缺失 |
| V3-02 | atomicity 双义拆分 + 危险 alias | **PARTIAL** | V-010-A/V-011-B 分立 ✓；无 atomicity(transaction) 义项、V-011-B 无 `atomic consistency` 危险 alias 警告 |
| V3-03 | isolation 三义消歧 | **PASS** | V-011-C + N-5（事务/故障/进程三义，do-not-conflate 到 V-005-E） |
| V3-04 | authority 四域不合并 | **PASS** | V-003-D(状态)/V-016-D(安全)/V-018-A(元语言)/V-003-A(运行时所有权) 四处分立，无合并词条 |
| V3-05 | observability 三义项 + vendor 注记 | **PASS** | V-015-A/B/C 分立；Majors 厂商立场批评保留；telemetry 非 synonym |
| V3-06 | C4 container 双义警告 | **PARTIAL** | V-002-B component 侧三语境 ✓；container(C4 绘图抽象 vs 部署单元) 双义警告缺席 |
| V3-07 | stateless REST/LLM 双义 | **FAIL** | 全表无 `stateless`/`无状态` 词条（S-039/S-103 两义均无家） |
| V3-08 | workflow 双义分立 + vendor 标注 | **PARTIAL** | V-020-B Anthropic 语义 + BPM 排斥 ✓、V-020-A vendor 标注 ✓；业务流程义（S-037/S-038 补偿语义）无落点 |
| V3-09 | context 三义不合并 | **PASS** | V-020-D(工程)/V-002-E bounded context(DDD)/V-007-D(execution) 三处分立 |
| V3-10 | schema compatibility 方向定义 | **PASS** | V-013-A「新代码读旧数据」/ V-013-B「旧版本容忍新数据」——"谁读谁"句式在场 |
| V3-11 | resilience 三源义项 | **PASS** | V-005-C/D/E 分立；SRE SLO 语义留在 V-005-B 未并入 resilience；但见 F-CA-3（"强于"排序问题） |
| V3-12 | performance 三分立 | **PARTIAL** | V-006-D scalability 独立 ✓、V-006-E 强制落到具体量 ✓；S-087「不是更快而是更可扩展」未被 V-006-D 引用；25010 特性名分立未显式 |
| V3-13 | REST 双语义声明 | **PASS** | N-7 裁决（CONTESTED）+ V-012-E 交叉引用；形式为裁决行而非独立词条，可接受 |
| V3-14 | structured concurrency 四平台 alias | **FAIL** | 全表无 `structured-concurrency` 词条；nursery/CoroutineScope/task group 零出现；机制证据散在 V-003-A/V-008-C 的 source 栏，无统一导航 |
| V3-15 | backpressure 全链路 + 反例 + 对照 | **PARTIAL** | V-008-E request(n) + 隐式无界缓冲警告 ✓、V-021-E fallback 放大警告 ✓；S-090「全链路成立」显式限定、S-081 actor mailbox 反例、E↔F 方向对照（传导 vs 卸载）缺席 |
| V3-16 | source of truth 别名统一 | **PARTIAL** | V-009-B 三语境 ✓；SSOT/system of record/authoritative state 变体未登记、S-105（Android SSOT owner 语义）全文未引用——另见 RA-1（假设修正后目标从"同义合并"降为"变体登记"） |
| V3-17 | retry storm/amplification 合并双源 | **PASS** | V-008-D 单词条双源（S-048 amplification + S-052 storm）+ 链式表述 |
| V3-18 | deadline/timeout 对照；cancellation 双语义 | **PASS** | V-008-A/B 分立且互相 do-not-conflate（单次 vs 跨跳传播预算）；V-008-C 传播+协作式双机制在场 |
| V3-19 | failure domain/blast radius alias | **CHECK_INVALID** | 见 RA-2：Pass A 假设两者为 alias 是错的；Kimi 的「属性(V-005-E) + 度量(V-021-A)」结构更精确，接受 |
| V3-20 | progressive disclosure ↔ just-in-time context | **PASS** | V-020-E 明示「just-in-time context 为其运行时实例」+ S-099 + 项目词与厂商词汇合标注 |
| V3-21 | modular monolith 边界声明 | **PARTIAL** | V-019-B 形态定义 ✓（Shopify 实证）；S-109「部署单元≠组织/领域边界」显式反混用声明缺席 |
| V3-22 | vendor 词条 scope 注记（通则） | **PASS** | 使用契约第 4 条全局声明 + V-020-A/F、V-008-B、V-021-D、V-015-B、V-005-C 逐条落地 |
| V3-23 | tactic/pattern/mechanism/principle 操作定义 | **PASS** | V-017 全族（A..E）项目操作定义 + 任务书锚定 |
| V3-24 | 状态保留无人工升稳 | **PASS** | CONTESTED×2（V-019-C 含 RQ2-009 缺口在场、N-7）保留；NEEDS_EVIDENCE 保留（V-006-D/S-079、V-016-C、V-021-D）；V-010 强制 CONTEXT_QUALIFIED；未发现 Stage 2 争议被静默升稳 |

**统计**: PASS 13 · PARTIAL 8 · FAIL 2 · CHECK_INVALID 1。

### 1.1 FAIL 详述

**V3-14 · structured concurrency 词条缺席（对应 Pass A COL-U-01，P0）**

- 事实：`02_VOCABULARY.md` 全文无 structured concurrency 主词条；nursery（S-084）、CoroutineScope（S-085）、task group（S-086）四个平台标签零出现。「结构化并发」仅作为 V-003-A 与 V-008-C 的 status 附注出现（"结构化并发来源 S-084..086 为其提供机制证据"），机制本身没有词条。
- 风险：H2b（Explicit Ownership）/Lifecycle 域的核心证据组失去统一检索锚点；RQ-A/RQ-C 跨平台比较类问题会把 Kotlin CoroutineScope 与 Swift TaskGroup 当两种机制分别推理。这是 Pass A 定级的 P0 under-normalization，且 OD-2 已给出裁决政策（canonical term + 平台 realization，非盲目 alias），但 Kimi 在盲写条件下无从知晓。
- 处置：→ **R-1**（最小 remediation 集第 1 项）。

**V3-07 · stateless 词条缺席（对应 Pass A COL-O-07，P2）**

- 事实：全文无 stateless/无状态词条。REST 约束义（S-039：会话状态放客户端）与 LLM 调用义（S-103：无状态函数，上下文随调用重传）两义均无落点。
- 风险：有界（P2）——无词条即无静默多义，但 Stage 4 引用 S-099/S-103 与 S-039 时词汇表无法提供消歧护栏；REST 处方（会话外移）误用到 LLM 上下文管理（需要 context engineering）的路径未被阻断。
- 处置：→ **R-9**（可选补充词条，一行成本）。

### 1.2 CHECK_INVALID 详述

**V3-19 · failure domain ≡ blast radius（Pass A 假设证伪）**

Pass A 提议两标签互为 alias 合并词条。CA checkpoint 反证：failure domain 是**分区结构**（静态划分），blast radius 是**受影响面度量**（动态结果），不是同义词。Kimi 的结构（V-005-E failure isolation 为属性、V-021-A blast radius 为其度量、S-063 在 V-021-A 引用）在语义上严格优于 Pass A 提议。**检查作废，Kimi 处理接受，无行动。**

---

## 2. Pass A 21 条 collision 对账矩阵

| Pass A ID | 内容 | 对账结果 | 处置 |
|---|---|---|---|
| COL-O-01 (P0) | consistency 三义 | **已解决**（V-010 专族 + N-1 强制后缀） | R-5a：补 RQ2-004 显式链接 |
| COL-O-02 (P0) | atomicity 双义 | **部分解决**（V-010-A 内嵌 atomic/linearizable 说明） | R-5b：V-011-B 加 `atomic consistency` 危险 alias 警告 |
| COL-O-03 (P1) | isolation 三义 | **已解决**（V-011-C + N-5） | — |
| COL-O-04 (P0) | authority 四域 | **已解决**（V-003-D / V-009-B / V-016-D / V-018-A / V-003-A 分域） | — |
| COL-O-05 (P1) | observability 三义 | **已解决**（V-015 + N-6） | — |
| COL-O-06 (P2) | container 双义 | **部分解决**（component 侧✓） | R-3 合并处理（C4 语境行补 container 双义） |
| COL-O-07 (P2) | stateless 双义 | **未解决** | R-9 |
| COL-O-08 (P1) | workflow 双义 | **部分解决**（Anthropic 义✓ + BPM 排斥✓） | R-7b：V-020-B 补业务流程义一行（S-037/S-038） |
| COL-O-09 (P1) | context 三义 | **已解决** | — |
| COL-O-10 (P1) | compat 方向镜像 | **已解决**（V-013-A/B 方向句式 + 「不同生态表述相反」警告） | R-4：状态 STABLE→CONTEXT_QUALIFIED（F-CA-5） |
| COL-O-11 (P2) | resilience 三源 | **已解决**（V-005 家族分立） | R-2：处理「强于」排序断言（F-CA-3） |
| COL-O-12 (P2) | performance 三分 | **部分解决** | R-9b：V-006-D 补引 S-087 |
| COL-O-13 (P1) | REST 双义 | **已解决**（N-7 CONTESTED + V-012-E） | — |
| COL-U-01 (P0) | structured concurrency 别名 | **未解决** | **R-1**（旗舰项，按 OD-2 政策） |
| COL-U-02 (P0) | backpressure 边界 | **部分解决**（request(n)✓ / fallback 警告✓ / load shedding 分立✓） | R-6：补全链路限定 + S-081 反例 + E↔F 方向对照 |
| COL-U-03 (P1) | SoT 别名族 | **假设修正 + 部分解决** | RA-1；R-8：变体登记（非同义）+ 补 S-105 |
| COL-U-04 (P2) | retry storm/amplification | **已解决**（V-008-D） | — |
| COL-U-05 (P1) | deadline/timeout/cancellation | **已解决**（V-008-A/B/C；CA-4 的平台限定已内建） | RA-5：Pass A 刚性二分框架修正 |
| COL-U-06 (P2) | failure domain/blast radius | **假设修正**（Kimi 结构更优） | RA-2；无行动 |
| COL-U-07 (P1) | progressive disclosure 别名 | **已解决**（V-020-E） | — |
| COL-U-08 (P2) | monolith 边界词 | **部分解决** | R-7a：V-019-B 补「部署单元≠领域边界」声明（S-109） |

**统计**: 已解决 11 · 部分解决 7 · 未解决 2 · 假设修正 2（其一同时算部分解决）。

---

## 3. CA 10 条 Primary findings 评估

| # | CA finding | 评估 | 依据 | 处置 |
|---|---|---|---|---|
| F-CA-1 | V-002-B component 过归一（「可独立替换/部署」对 C4 component 不成立） | **CONFIRMED** | V-002-B working definition 首句「可独立替换/部署的单元」与 C4 语境行并存——C4 component 是 container 内代码级分组，**不可**独立部署（可部署的是 container）；定义句把 UML/SAIP 运行时义当作了全局义 | R-3：拆语境（replaceable-unit 义 vs C4 in-container 义） |
| F-CA-2 | V-002-C service 普遍化（独立部署+网络契约 ≈ 微服务前置） | **CONFIRMED（轻）** | 定义单源 S-023；已排 microservice 与 daemon/OS service，但「service=必然网络契约」的框架义仍在——internal service / 进程内 service 层未被语境覆盖 | R-3 合并处理（补一行语境） |
| F-CA-3 | V-005「fault tolerance 强于 resilience」全序断言无源 | **CONFIRMED** | V-005-C do-not-conflate「（容忍特定故障继续无中断运行，更强）」+ V-005-D「强于 resilience」——比较级排序被写进 STABLE 词条的 working definition，但 corpus 无任何来源支撑该全序（两者按故障模型部分正交：指定故障不中断 vs 扰动下降级+恢复） | R-2：改为故障模型相对表述，或标注为项目约定（→ OD-B） |
| F-CA-4 | V-008-B deadline gRPC 特定性 | **ADDRESSED** | Kimi 已标 CONTEXT_QUALIFIED 并拆分「通用概念 STABLE；具体传播语义是平台 normative」——正是 CA 要的形态 | 无行动 |
| F-CA-5 | V-013 兼容方向应 CONTEXT_QUALIFIED | **PARTIALLY ADDRESSED** | 方向句式✓ + 「不同生态表述相反的历史版本存在，引用须核对方向」警告✓，但状态仍为 STABLE | R-4：状态翻转（一词成本） |
| F-CA-6 | V-014-C locality 应作 Stage 4 假设 | **ADDRESSED** | V-014-C「Stage 4 需拆分检验」+ N-8 禁止与 Herlihy-Wing 专用义互借——假设泄漏的规范处理范例 | 无行动（进入 backflow 清单 B-1 的关联项） |
| F-CA-7 | V-019-D EDA 应 NEEDS_EVIDENCE | **PARTIALLY ADDRESSED** | V-019-D CONTEXT_QUALIFIED、定义极薄（无收益主张）、do-not-conflate event sourcing✓。薄定义+无过度主张下 CONTEXT_QUALIFIED 可辩护；但 CA 的点是 corpus 内 EDA 权威不足以支撑风格级词条 | → OD-C（owner/CA 裁量） |
| F-CA-8 | V-013-C/V-021-F expand-contract 有 S-011 支撑 | **ADDRESSED（确认在场）** | V-021-F 引 S-011 + Fowler 2004 出处修正（非 Greg Young，RQ2-007） | 无行动 |
| F-CA-9 | 项目定义词需 Origin 标记 | **PARTIALLY ADDRESSED** | 行内标注在场（V-004-C「项目内造词」/V-007-D「工作词条」/V-017「项目元定义」/V-021-C），但无统一 `Origin:` 字段 | → OD-D（现在改 or Stage 4 工具化） |
| F-CA-10 | V-001-B architecture/design 约定需标注 | **ADDRESSED** | V-001-B 明示「该区分是工作约定而非来源规定」+ ATAM 连续性注记 | 无行动 |

---

## 4. Pass A 假设反向审查（挑战者被挑战）

- **RA-1（COL-U-03）**: Pass A 提议 SoT/SSOT/authoritative state/system of record 四标签**互为 alias** 合并——**证伪**。CA 指出非精确同义（S-105 的 SSOT 织入 owner 语义，平台表述）。修正后目标：V-009-B 作族枢纽 + 变体登记（各配差异注记），Pass A 的「合并词条」提议撤回。
- **RA-2（COL-U-06）**: failure domain ≡ blast radius alias——**证伪**（结构 vs 度量，见 V3-19）。Kimi 结构接受。
- **RA-3（COL-U-02 部分）**: flow control 作为 backpressure 的 alias——**撤回**。Kimi 未做此 alias，且 V-008-E 的「TCP 流控：同族但层不同」是正确精度。Pass A 原提议降级为 related-term 注记（不进 alias 表）。
- **RA-4（COL-U-01 部分）**: Virtual Threads 作为 structured concurrency 第四平台 alias——**证伪**（OD-2：JEP 444 虚拟线程 ≠ 结构化并发；Java 的对应物是 StructuredTaskScope，corpus 未收录 → NEEDS_EVIDENCE）。R-1 按此修正执行。
- **RA-5（COL-U-05 部分）**: Pass A 的 deadline（绝对、传播）/ timeout（相对、局部）刚性二分——**修正**。corpus 中传播语义只有 S-042（gRPC）单一支撑，Kimi 的「通用概念稳定 + 传播语义平台 normative」拆分更忠实于证据密度。
- **RA-6**: Pass A 的 P0/P1/P2 是挑战者风险导航分级，不是 Kimi 状态分类学——不要求 Primary 采纳，仅用于 remediation 排序。

---

## 5. 处置层分类（lexical / PROJECT_DEFINED / PROJECT_META / Stage 4 泄漏）

**层 1 — lexical fix（Stage 3 词汇层微修，安全，共 9 项 = 最小 remediation 集）**

R-1 structured-concurrency 新词条（OD-2 政策：canonical + 平台 realization + virtual threads 排除 + StructuredTaskScope NEEDS_EVIDENCE）
R-2 V-005-C/D「强于」全序断言改写（或标注项目约定）
R-3 V-002-B/C 语境拆分（C4 component 非独立部署；service 补非网络语境行）
R-4 V-013-A/B 状态 STABLE→CONTEXT_QUALIFIED
R-5 V-010-A 补 RQ2-004 链接；V-011-B 补 `atomic consistency` 危险 alias
R-6 V-008-E 补「全链路成立」限定（S-090）+ S-081 actor mailbox 反例；V-008-E↔F 方向对照（传导 vs 主动卸载）
R-7 V-019-B 补「部署单元≠组织/领域边界」（S-109）；V-020-B 补业务流程义一行（S-037/S-038）
R-8 V-009-B 登记变体族（SSOT/system of record/authoritative state，非同义+差异注记）+ 引 S-105（owner 语义标 vendor-scoped）
R-9（可选）`stateless` 微词条（REST S-039 vs LLM 调用 S-103）；V-006-D 补引 S-087

**层 2 — PROJECT_DEFINED（保留，标注即可，无需动作）**
V-001-B（architecture/design 约定）、V-004-C（required property）、V-007-D（execution context）、V-017 全族、V-020-C/E、V-021-C（unboundedness）。均有行内「项目定义/工作词条」标注 + 任务书锚定。统一 `Origin:` 字段属 schema 增强 → OD-D。

**层 3 — PROJECT_META（OD-1 已批隔离，已执行）**
V-018 全族独立成族（authority tier / evidence class / normative / empirical / theoretical），与领域词隔离 ✓，含 Issue #3 claim-relative 修正 ✓。

**层 4 — Stage 4 假设/泄漏与证据回填（不词汇层硬修）**
- V-014-C locality：规范处理 ✓（假设标记 + 禁止互借）——机制拆分留给 Stage 4。
- V-005「强于」：唯一的**词汇层过度断言**（Normative claim 无源），必须 Stage 3 内修（R-2），不属于可延期项。
- V-021-C unboundedness、V-019-C microservices：假设/缺口标记规范 ✓。

---

## 6. Targeted evidence backflow（Stage 4 边界外补源，不做词汇硬修）

| # | 缺口 | 关联 | 状态 |
|---|---|---|---|
| B-1 | family 14（coupling / change locality）权威源 | H5b/H7；F-4；OD-5 已裁决骨架保留 | 登记待 Stage 4 定向补源 |
| B-2 | Java StructuredTaskScope 官方文档 | R-1 的 alias 行完成后可从 NEEDS_EVIDENCE 升稳 | 新登记 |
| B-3 | microservices 正方一手论证 | RQ2-009 / N-9 | 已登记（承 Stage 2） |
| B-4 | WASI / component model capability 源 | RQ2-013 CH-S-07；V-016-C | 已登记（handoff 自报） |
| B-5 | WHATWG / web.dev UI 主线程形态 | CH-S-12；V-021-D | 已登记（handoff 自报） |

---

## 7. Gate 建议

### **PASS_WITH_REMEDIATION**

理由：
1. **P0 语义场安全**。最高危的 consistency/atomicity/authority 场（Pass A 两个 P0 over-normalization）在 Kimi 词汇表中均已被强制 context qualification 或分域处理，无静默多义——这是 HOLD 的排除条件。
2. **纪律合规**。V3-22/23/24 全 PASS：vendor scoping、元术语定义、状态诚实性（CONTESTED/NEEDS_EVIDENCE 保留、无人工升稳）全部在场；handoff 自报缺口与实际一致。
3. **两个 FAIL 均为「缺席」而非「污染」**。V3-14（structured concurrency 词条缺席）与 V3-07（stateless 缺席）是遗漏——修复是加法不是改错，且 OD-2 已给 R-1 的执行政策。
4. **PARTIAL 8 项全部是一行至三行级微修**（R-4 是一词），无结构返工。
5. Stage 4 开工前置条件：R-1、R-2 完成（前者是 H2b 证据组导航锚点，后者防止无源排序断言被原则文本继承）；R-3..R-9 可与 Stage 4 并行由 Primary 修订，但建议在 Stage 4 首个 P-* 文件引用相应词条前落盘。OD-4（qualified-term gate）已批，随 Stage 4 开工生效。

### 最小 remediation 集
R-1（P0，必须先于 Stage 4）· R-2（P1，必须先于 Stage 4）· R-3..R-8（P2，Stage 4 早期落盘）· R-9（P3，可选）。

### 真正需要 owner 决策的问题
- **OD-A**: R-1/R-2 未完成前，Stage 4 是否允许开工？（挑战者建议：不允许——两者分别是证据导航锚点与无源断言，会被原则文本直接继承。）
- **OD-B**: R-2 的修法二选一：改写为故障模型相对表述（挑战者推荐，更贴 corpus），或保留排序但标注 PROJECT_DEFINED 项目约定。
- **OD-C**: V-019-D EDA 状态：接受 Kimi 的 CONTEXT_QUALIFIED，还是按 F-CA-7 翻转为 NEEDS_EVIDENCE？
- **OD-D**: 统一 `Origin: PROJECT_DEFINED` 字段（F-CA-9）：本修订轮加（约 7 处行内改字段），还是 Stage 4 工具化时统一处理？

---

## 8. 挑战者元声明

- Pass B 在 Pass A 盲写基线（e6d67b3）之上执行；Kimi 词汇表仅在 CA 接受 Pass A 之后读取（3f386db 固定 SHA 快照）。
- 全部判定可回放：词条 V-* 编号 + S-ID + 本报告章节号。
- 本报告未修改 Primary 任何产物；未创建竞争性词汇表；未进入 Stage 4。
- 本人 Pass A 的 4 项 alias 假设被证伪并公开撤回（RA-1..RA-4）——对账是双向的。
