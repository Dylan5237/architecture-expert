# STAGE3_RECONCILIATION — Challenger Pass B（Vocabulary Reconciliation）

- **角色**: Independent Challenger Pass B — Codex harness（仓库操作/Git 完整性/持久化验证）+ GLM 5.3（术语 collision 分析与 reconciliation 判断）
- **分支**: `challenge/stage3-codex-glm`，base = `e6d67b3384a83608245cb7b937d291929d2852bb`（已接受的 Pass A 干净基线；不含 WorkBuddy 空 Pass B 提交 `626920e`）
- **审计对象**: Kimi Primary 固定 SHA `research/stage3-vocabulary@3f386db58a5f6679b7188daa4af89ccd35fae36f`（`02_VOCABULARY.md`：V-001..V-021 族 + N-1..N-10；`reports/STAGE3_HANDOFF.md`）
- **输入**: Pass A `STAGE3_COLLISION_AUDIT.md`（base 内）、Issue #6 Chief Architect 全部 checkpoint（OD-1..OD-5、10 条 Primary-review findings、Pass A 假设挑战清单、编排切换决议）
- **纪律**: 未修改 Kimi vocabulary；未重做广泛研究（仅回读 accepted corpus 中 S-011、S-042 两个源文件原文用于对账验证）；未进入 Stage 4；未创建竞争性词汇表
- **日期**: 2026-09-18

---

## 0. 方法与判定标尺

1. 逐条执行 Pass A 预注册的 V3-01..V3-24，对固定 SHA 的 `02_VOCABULARY.md` 全文对账。判定四值：**PASS**（检查满足）/ **PARTIAL**（核心保护在场但预注册要素缺失）/ **FAIL**（检查要求的保护不在场）/ **CHECK_INVALID**（检查本身的预注册假设被证伪，检查作废并修正）。
2. 21 条 Pass A collision 逐条对账：已解决 / 部分解决 / 未解决 / 假设修正。
3. 显式评估 CA 释放的 10 条 Primary findings（F-CA-1..10）：ADDRESSED / PARTIALLY ADDRESSED / CONFIRMED（缺口实在，需修）/ REJECTED。
4. 反向审查 Pass A 自身的 alias 假设（RA-1..6）——CA 指令：挑战者也要被挑战。
5. 每个未决项归入四层：**SOURCE_NORMALIZED**（corpus 归一主体）/ **PROJECT_DEFINED**（项目约定，保留+标注）/ **PROJECT_META**（元语言，OD-1 隔离）/ **Stage 4 hypothesis/principle leakage**（不词汇层硬修，走拆分或回填）。
6. 证据核对声明：本报告所有「在场/缺席」判定均对 `3f386db` 的 `02_VOCABULARY.md` 全文检索复核（structured concurrency、stateless、SSOT、system of record、failure domain、nursery、CoroutineScope、task group、S-081、S-087、S-105、S-109、RQ2-004、atomic consistency 等关键词逐一验证）；S-011/S-042 回读原文用于 F-CA-8 / F-CA-4 裁定。

---

## 1. V3-01..V3-24 判定总表

| Check | 内容 | 判定 | 证据落点 |
|---|---|---|---|
| V3-01 | consistency 裸词条禁令 + RQ2-004 链接 | **PARTIAL** | V-010 专族 + 强制后缀限定在场；RQ2-004 显式链接缺失（全文零出现） |
| V3-02 | atomicity 双义拆分 + 危险 alias | **PARTIAL** | CAP atomic 语义经 V-010-A（S-024）覆盖；无 atomicity(transaction) 义项、V-011-B 无 `atomic consistency` 危险 alias 警告（零出现） |
| V3-03 | isolation 三义消歧 | **PASS** | V-011-C + N-5（事务/故障/进程三义，do-not-conflate 到 V-005-E） |
| V3-04 | authority 四域不合并 | **PASS** | V-003-D（状态）/ V-016-D（安全 authn/authz）/ V-018-A（元语言 authority tier）/ V-003-A（运行时所有权）四处分立，无合并词条 |
| V3-05 | observability 三义项 + vendor 注记 | **PASS** | V-015-A/B/C 分立；Majors 厂商立场批评保留；telemetry 非 synonym |
| V3-06 | C4 container 双义警告 | **PARTIAL** | V-002-B component 侧三语境在场；container（C4 绘图抽象 vs 部署单元）双义警告缺席 |
| V3-07 | stateless REST/LLM 双义 | **FAIL** | 全文无 stateless/无状态词条（S-039 REST 约束义与 S-103 LLM 调用义均无落点） |
| V3-08 | workflow 双义分立 + vendor 标注 | **PARTIAL** | V-020-B Anthropic 语义 + BPM 排斥在场；业务流程义（S-037/S-038 补偿语义）无落点 |
| V3-09 | context 三义不合并 | **PASS** | V-020-D（工程）/ V-002-E bounded context（DDD）/ V-007-D（execution）三处分立 |
| V3-10 | schema compatibility 方向定义 | **PASS** | V-013-A「新代码读旧数据」/ V-013-B「旧版本容忍新数据」——「谁读谁」句式在场 |
| V3-11 | resilience 三源义项 | **PASS** | V-005-C/D/E 分立；SRE SLO 语义留在 V-005-B 未并入 resilience；排序断言问题另见 F-CA-3/R-2 |
| V3-12 | performance 三分立 | **PARTIAL** | V-006-D scalability 独立、V-006-E 强制落具体量在场；S-087「不是更快而是更可扩展」未被 V-006-D 引用（S-087 仅现于 V-007-A）；25010 特性名（performance efficiency）分立未显式 |
| V3-13 | REST 双语义声明 | **PASS** | N-7 裁决（CONTESTED）+ V-012-E 交叉引用；形式为裁决行而非独立词条，可接受 |
| V3-14 | structured concurrency 四平台 alias | **FAIL** | 全文无 structured-concurrency 词条；nursery/CoroutineScope/task group 平台标签零出现；机制证据仅以 status 附注散在 V-003-A/V-008-C，无统一导航 |
| V3-15 | backpressure 全链路 + 反例 + 对照 | **PARTIAL** | V-008-E request(n) + 隐式无界缓冲警告、V-021-E fallback 放大警告在场；S-090「任一环节 unbounded buffer 即破功」限定未入定义句、S-081 actor mailbox 反例缺席、V-008-E↔F 方向对照（传导 vs 主动卸载）缺席 |
| V3-16 | source of truth 别名统一 | **PARTIAL** | V-009-B 三语境在场；SSOT/system of record/authoritative state 变体未登记（零出现）、S-105（Android SSOT owner 语义）未被引用——目标经 RA-1 修正后从「同义合并」降为「变体登记」 |
| V3-17 | retry storm/amplification 合并双源 | **PASS** | V-008-D 单词条双源（S-048 + S-052）+ 链式表述 |
| V3-18 | deadline/timeout 对照；cancellation 双语义 | **PASS** | V-008-A/B 分立且互相 do-not-conflate（单次 vs 跨跳传播预算）；V-008-C 传播 + 协作式双机制在场；RPC vs scope 取消的显式二分由 F-CA-4/R-10 处理（预注册检查未要求该粒度） |
| V3-19 | failure domain/blast radius alias | **CHECK_INVALID** | 见 RA-2：Pass A 假设两者为 alias 被证伪；Kimi「属性（V-005-E）+ 度量（V-021-A）」结构更精确，接受 |
| V3-20 | progressive disclosure ↔ just-in-time context | **PASS** | V-020-E 明示 just-in-time context 为运行时实例 + S-099 + 项目词与厂商词汇合标注 |
| V3-21 | modular monolith 边界声明 | **PARTIAL** | V-019-B 形态定义在场（Shopify 实证）；S-109「部署单元≠组织/领域边界」显式反混用声明缺席 |
| V3-22 | vendor 词条 scope 注记（通则） | **PASS** | 使用契约第 4 条全局声明 + V-020-A/F、V-008-B、V-021-D、V-015-B、V-005-C 逐条落地 |
| V3-23 | tactic/pattern/mechanism/principle 操作定义 | **PASS** | V-017 全族（A..E）项目操作定义 + 任务书锚定 |
| V3-24 | 状态保留无人工升稳 | **PASS** | CONTESTED×2（V-019-C 含 RQ2-009 缺口在场、N-7）保留；NEEDS_EVIDENCE 保留（V-006-D/S-079、V-016-C、V-021-D）；V-010 强制 CONTEXT_QUALIFIED；未发现 Stage 2 争议被静默升稳 |

**统计**: PASS 13 · PARTIAL 8 · FAIL 2 · CHECK_INVALID 1。

### 1.1 FAIL 详述

**V3-14 · structured concurrency 词条缺席（对应 COL-U-01，P0）**

- 事实：`02_VOCABULARY.md` 全文无 structured concurrency 主词条；nursery（S-084）、CoroutineScope（S-085）、task group（S-086）平台标签零出现。「结构化并发」仅作为 V-003-A 与 V-008-C 的 status 附注出现（「结构化并发来源 S-084..086 为其提供机制证据」），机制本身没有词条。
- 风险：H2b（Explicit Ownership）/Lifecycle 域的核心证据组失去统一检索锚点；RQ-A/RQ-C 跨平台比较类问题会把 Kotlin CoroutineScope 与 Swift TaskGroup 当两种机制分别推理。这是 Pass A 定级的 P0 under-normalization；OD-2 已给出裁决政策（canonical term + 平台 realization，非盲目 alias），但 Kimi 在盲写条件下无从知晓。
- 处置：→ **R-1**。

**V3-07 · stateless 词条缺席（对应 COL-O-07，P2）**

- 事实：全文无 stateless/无状态词条。REST 约束义（S-039：会话状态放客户端）与 LLM 调用义（S-103：无状态函数，上下文随调用重传）两义均无落点。
- 风险：有界（P2）——无词条即无静默多义，但 Stage 4 引用 S-099/S-103 与 S-039 时词汇表无法提供消歧护栏；REST 处方（会话外移）误用到 LLM 上下文管理（需要 context engineering）的路径未被阻断。
- 处置：→ **R-9**（可选补充词条，一行成本）。

### 1.2 CHECK_INVALID 详述

**V3-19 · failure domain ≡ blast radius（Pass A 假设证伪）**

Pass A 提议两标签互为 alias 合并词条。CA checkpoint 反证：failure domain 是分区结构（静态划分），blast radius 是受影响面度量（动态结果），不是同义词。Kimi 的结构（V-005-E failure isolation 为属性、V-021-A blast radius 为其度量、S-063 在 V-021-A 引用）在语义上严格优于 Pass A 提议。**检查作废，Kimi 处理接受，无行动。**

---

## 2. Pass A 21 条 collision 对账矩阵

| Pass A ID | 内容 | 对账结果 | 处置 |
|---|---|---|---|
| COL-O-01 (P0) | consistency 三义 | **已解决**（V-010 专族 + N-1 强制后缀） | R-5a：补 RQ2-004 显式链接 |
| COL-O-02 (P0) | atomicity 双义 | **部分解决**（V-010-A 内嵌 atomic/linearizable 说明） | R-5b：V-011-B 加 `atomic consistency` 危险 alias 警告 |
| COL-O-03 (P1) | isolation 三义 | **已解决**（V-011-C + N-5） | — |
| COL-O-04 (P0) | authority 四域 | **已解决**（V-003-D / V-009-B / V-016-D / V-018-A / V-003-A 分域） | — |
| COL-O-05 (P1) | observability 三义 | **已解决**（V-015 + N-6） | — |
| COL-O-06 (P2) | container 双义 | **部分解决**（component 侧三语境在场） | R-3 合并处理（C4 语境行补 container 双义） |
| COL-O-07 (P2) | stateless 双义 | **未解决** | R-9 |
| COL-O-08 (P1) | workflow 双义 | **部分解决**（Anthropic 义 + BPM 排斥在场） | R-7b：V-020-B 补业务流程义一行（S-037/S-038） |
| COL-O-09 (P1) | context 三义 | **已解决** | — |
| COL-O-10 (P1) | compat 方向镜像 | **已解决**（V-013-A/B 方向句式 + 「不同生态表述相反」警告） | R-4：状态 STABLE→CONTEXT_QUALIFIED（F-CA-5） |
| COL-O-11 (P2) | resilience 三源 | **已解决**（V-005 家族分立） | R-2：处理「强于」排序断言（F-CA-3） |
| COL-O-12 (P2) | performance 三分 | **部分解决** | R-9b：V-006-D 补引 S-087 |
| COL-O-13 (P1) | REST 双义 | **已解决**（N-7 CONTESTED + V-012-E） | — |
| COL-U-01 (P0) | structured concurrency 别名 | **未解决** | **R-1**（旗舰项，按 OD-2 政策） |
| COL-U-02 (P0) | backpressure 边界 | **部分解决**（request(n) / fallback 警告 / load shedding 分立在场） | R-6：补全链路限定 + S-081 反例 + E↔F 方向对照 |
| COL-U-03 (P1) | SoT 别名族 | **假设修正 + 部分解决** | RA-1；R-8：变体登记（非同义）+ 补 S-105 |
| COL-U-04 (P2) | retry storm/amplification | **已解决**（V-008-D） | — |
| COL-U-05 (P1) | deadline/timeout/cancellation | **已解决**（V-008-A/B/C） | RA-5：Pass A 刚性二分框架修正；R-10：timeout 绝对化断言（F-CA-4 后半） |
| COL-U-06 (P2) | failure domain/blast radius | **假设修正**（Kimi 结构更优） | RA-2；无行动 |
| COL-U-07 (P1) | progressive disclosure 别名 | **已解决**（V-020-E） | — |
| COL-U-08 (P2) | monolith 边界词 | **部分解决** | R-7a：V-019-B 补「部署单元≠领域边界」声明（S-109） |

**统计**: 已解决 11 · 部分解决 7（含 COL-U-03 同时计假设修正）· 未解决 2 · 假设修正 2（其一兼部分解决）。

---

## 3. CA 10 条 Primary findings 评估

| # | CA finding | 评估 | 依据 | 处置 |
|---|---|---|---|---|
| F-CA-1 | V-002-B component 过归一（「可独立替换/部署」对 C4 component 不成立） | **CONFIRMED** | V-002-B working definition 首句「可独立替换/部署的单元」与 C4 语境行并存——C4 component 是 container 内代码级分组，不可独立部署（可部署的是 container）；定义句把 UML/SAIP 运行时义当作了全局义 | R-3：拆语境（replaceable-unit 义 vs C4 in-container 义） |
| F-CA-2 | V-002-C service 普遍化（独立部署+网络契约 ≈ 微服务前置） | **CONFIRMED（轻）** | 定义单源 S-023；已排 microservice 与 daemon/OS service，但「service=必然网络契约」的框架义仍在——internal service / 进程内 service 层未被语境覆盖 | R-3 合并处理（补一行语境） |
| F-CA-3 | V-005「fault tolerance 强于 resilience」全序断言无源 | **CONFIRMED** | V-005-C do-not-conflate「（容忍特定故障继续无中断运行，更强）」+ V-005-D「强于 resilience」——比较级排序被写进 STABLE 词条定义，但 corpus 无任何来源支撑该全序（两者按故障模型部分正交：指定故障不中断 vs 扰动下降级+恢复） | R-2：改为故障模型相对表述，或标注 PROJECT_DEFINED（→ OD-B） |
| F-CA-4 | V-008 timeout/deadline/cancellation 三个问题 | **PARTIALLY ADDRESSED** | deadline 半已修：V-008-B CONTEXT_QUALIFIED +「通用概念 STABLE；具体传播语义是平台 normative」正是 CA 要的形态。timeout 半未修：V-008-A「没有 timeout 的操作是时间维度上的无界」绝对化仍在——若 deadline/配额/上游取消等其他界在场，该断言过强。cancellation：V-008-C 传播+协作式机制在场，但 RPC 取消传播（S-042 语境）与结构化 scope 取消（S-084..086 语境）两种语义未显式二分，且 S-042 不在 V-008-C source 栏 | R-10：V-008-A 加「除非存在其他时间界」限定；V-008-C 补双语义一行 |
| F-CA-5 | V-013 兼容方向应 CONTEXT_QUALIFIED | **PARTIALLY ADDRESSED** | 方向句式 + 「不同生态表述相反的历史版本存在，引用须核对方向」警告在场，但 V-013-A/B 状态仍为 STABLE，且未强制 reader/producer 视角标注 | R-4：状态翻转 + 视角强制（一词+一行成本） |
| F-CA-6 | V-014-C locality 应作 Stage 4 假设 | **ADDRESSED** | V-014-C status 行自带假设标记（「是多种机制的共同倾向而非单一机制；Stage 4 需拆分检验」）+ N-8 禁止与 Herlihy-Wing 专用义互借——与 OD-5 一致的规范处理 | 无行动（B-1 关联项，机制拆分留 Stage 4） |
| F-CA-7 | V-019-D EDA 应 NEEDS_EVIDENCE | **PARTIALLY ADDRESSED** | V-019-D CONTEXT_QUALIFIED、定义极薄（无收益主张）、do-not-conflate event sourcing 在场。薄定义+无过度主张下 CONTEXT_QUALIFIED 可辩护；但 CA 的点是 corpus 内 EDA 权威（S-040/S-041 为 Event Sourcing/CQRS 证据）不足以支撑风格级词条 | → OD-C（owner/CA 裁量） |
| F-CA-8 | V-013-C / V-021-F expand-contract 支撑核验 | **CONFIRMED（缺口实在）** | 回读 S-011 原文验证：该源只覆盖 Strangler Fig（含 2024 细化子模式：事件拦截/资产分流/CQS），**无 expand-contract 表述**。V-021-F 把两个 tactic 家族写在同一词条并整体引 S-011 + Fowler 2004 出处，expand-contract 半缺乏直接支撑；V-013-C（migration 词条连带引 S-011）同病 | R-11：按 CA 指令 split-or-downgrade——expand-contract 半标 NEEDS_EVIDENCE 或拆出（可选锚 S-044 方向语义为相邻支撑）；B-6/OD-E 联动 |
| F-CA-9 | 项目定义词需 Origin 标记 | **PARTIALLY ADDRESSED** | 行内标注在场（V-004-C「项目内造词」/ V-007-D「工作词条」/ V-017「项目元定义」/ V-021-C），但无统一 `Origin:` 字段，机器不可判别 | → OD-D（本轮加 or Stage 4 工具化） |
| F-CA-10 | V-001-B architecture/design 约定需标注 | **ADDRESSED** | V-001-B 明示「该区分是工作约定而非来源规定」+ ATAM 连续性注记 | 无行动 |

---

## 4. Pass A 假设反向审查（挑战者被挑战）

- **RA-1（COL-U-03）**: Pass A 提议 SoT/SSOT/authoritative state/system of record 四标签互为 alias 合并——**证伪**。CA 指出非精确同义（S-105 的 SSOT 织入 owner 语义，平台表述）。修正后目标：V-009-B 作族枢纽 + 变体登记（各配差异注记），「合并词条」提议撤回。
- **RA-2（COL-U-06）**: failure domain ≡ blast radius alias——**证伪**（结构 vs 度量，见 V3-19）。Kimi 结构接受。
- **RA-3（COL-U-02 部分）**: flow control 作为 backpressure 的 alias——**撤回**。flow control 外延更宽（含 TCP 流控等非 Reactive Streams 机制）；Kimi 的「TCP 流控：同族但层不同」是正确精度。Pass A 原提议降级为 related-term 注记（不进 alias 表）。
- **RA-4（COL-U-01 部分）**: Virtual Threads 作为 structured concurrency 第四平台 alias——**证伪**（OD-2 裁决：JEP 444 虚拟线程 ≠ 结构化并发；Java 对应物是 StructuredTaskScope，corpus 未收录 → NEEDS_EVIDENCE，B-2）。R-1 按此修正执行。
- **RA-5（COL-U-05 部分）**: Pass A 的 deadline（绝对、传播）/ timeout（相对、局部）刚性二分——**修正**。corpus 中传播语义只有 S-042（gRPC）单一支撑，Kimi 的「通用概念稳定 + 传播语义平台 normative」拆分更忠实于证据密度；反向地，Kimi 的「无 timeout 即无界」也需要 R-10 的对称修正。
- **RA-6**: Pass A 的 P0/P1/P2 是挑战者风险导航分级，不是 Kimi 状态分类学——不要求 Primary 采纳，仅用于 remediation 排序。

---

## 5. 处置层分类

**层 0 — SOURCE_NORMALIZED（corpus 归一主体，无需动作）**

以下词条满足「source IDs 在场 + 定义句可回放到 S-ID 原文」的归一基准：V-001-A/C/D、V-002-A/D/E、V-003-A/B/C、V-004-A/B/D、V-005 全族、V-006 全族、V-007-A/B/C、V-008-A/B/D/E/F、V-009 全族、V-010、V-011 全族、V-012 全族、V-013-A/B/D/E、V-014-A/B/D、V-015 全族、V-016-A/B/D、V-019 全族、V-020-A/B/D/F、V-021-A/B/D/E。V-002-B/C 与 V-013-C 属于此层但带 F-CA-1/2/8 指出的局部过归一，由 R-3/R-11 微修。

**层 1 — lexical fix（Stage 3 词汇层微修，安全）= 最小 remediation 集 R-1..R-11，见第 8 节**

**层 2 — PROJECT_DEFINED（项目约定，保留+标注即可）**

V-001-B（architecture/design 工作约定，已标注）、V-004-C（required property）、V-007-D（execution context）、V-017 全族（tactic/pattern/mechanism/principle/heuristic）、V-020-C/E（harness、progressive disclosure）、V-021-C（unboundedness）。均有行内「项目定义/工作词条」标注 + 任务书锚定。统一 `Origin:` 字段属 schema 增强 → OD-D。

**层 3 — PROJECT_META（OD-1 已批隔离，已执行）**

V-018 全族独立成族（authority tier / evidence class / normative / empirical / theoretical），与领域词隔离，含 Issue #3 claim-relative 修正。OD-1 的「或 per-entry Origin: PROJECT_META」路径未走（统一字段缺失 → OD-D）。

**层 4 — Stage 4 假设/泄漏与证据回填（不词汇层硬修）**

- V-014-C locality：假设标记 + 禁止互借已规范——机制拆分留给 Stage 4，权威源走 B-1。
- V-021-C unboundedness、V-019-C microservices：假设/缺口标记规范。
- V-005「强于」：唯一的词汇层过度断言（Normative claim 无源），必须在 Stage 3 内修（R-2），不可延期。
- V-021-F expand-contract：词汇层缺源支撑（R-11 处理），完整 tactic 家族的一手出处核验走 B-6。

---

## 6. OD-1..OD-5 合规核对

| OD | 裁决 | Primary 现状 | 处置 |
|---|---|---|---|
| OD-1 元语言隔离 | APPROVED | V-018 独立成族已执行；per-entry Origin 字段未走 | 隔离达标；字段统一化 → OD-D |
| OD-2 structured concurrency 命名 | CANONICAL + PLATFORM REALIZATIONS | 未执行（盲写条件，无从知晓） | R-1 按裁决政策执行 |
| OD-3 中文别名选择性 | SELECTIVE | 词汇表基本未收中文口语标签（灰度未并入 canary），风险低；Alias vs Related 区分以 do-not-conflate 形式散在场 | 无强制动作；后续修订遵循「canary ≠ 灰度发布泛称」 |
| OD-4 Stage 4 qualified-term gate | APPROVED | 不适用于 Primary 产物，适用于 Stage 4 | 本报告第 8 节登记为 gate 条件 |
| OD-5 family 14 骨架 | KEEP SKELETON | V-014-C 骨架 + 假设标记保留，未重开采集 | 合规；H5b/H7 依赖走 B-1 定向回填 |

---

## 7. Targeted evidence backflow（Stage 3 边界外定向补源，不做词汇硬修）

| # | 缺口 | 关联 | 状态 |
|---|---|---|---|
| B-1 | family 14（coupling / change locality）权威源 | H5b/H7；F-CA-6；OD-5 已裁决骨架保留 | 登记待 Stage 4 定向补源 |
| B-2 | Java StructuredTaskScope 官方文档 | R-1 的平台 realization 行；补源后可从 NEEDS_EVIDENCE 升稳 | 新登记 |
| B-3 | microservices 正方一手论证 | RQ2-009 / N-9 | 已登记（承 Stage 2） |
| B-4 | WASI / component model capability 源 | RQ2-013 CH-S-07；V-016-C | 已登记（handoff 自报） |
| B-5 | WHATWG / web.dev UI 主线程形态 | CH-S-12；V-021-D | 已登记（handoff 自报） |
| B-6 | expand-contract 一手出处核验 | F-CA-8 / R-11 / OD-E；若 owner 选择保留完整 tactic 家族而非降级 | 新登记 |

---

## 8. Gate 建议

### **PASS_WITH_REMEDIATION**

理由：

1. **P0 语义场安全**。最高危的 consistency/atomicity/authority 场（Pass A 两个 P0 over-normalization）在 Kimi 词汇表中均已被强制 context qualification 或分域处理，无静默多义——这是 HOLD 的排除条件。
2. **纪律合规**。V3-22/23/24 全 PASS：vendor scoping、元术语定义、状态诚实性（CONTESTED/NEEDS_EVIDENCE 保留、无人工升稳）全部在场；handoff 自报缺口与实际一致。
3. **两个 FAIL 均为「缺席」而非「污染」**。V3-14（structured concurrency 词条缺席）与 V3-07（stateless 缺席）是遗漏——修复是加法不是改错，且 OD-2 已给 R-1 的执行政策。
4. **PARTIAL 8 项与新增 R-10/R-11 全部是一行至三行级微修**（R-4 是一词），无结构返工。
5. **Stage 4 开工前置**：R-1、R-2 必须先落盘（前者是 H2b 证据组导航锚点，后者防止无源排序断言被原则文本继承）；R-4、R-10、R-11 同为一行级，建议同批落盘；R-3..R-8 可 Stage 4 早期由 Primary 修订，但须在首个 P-* 文件引用相应词条前完成；R-9 可选。

### OD-4 落地为 Stage 4 gate 条件

Stage 4 任何 `P-*` 文件引用 P0 高危词——consistency、atomicity、authority、isolation、context、compatibility direction、container/component（相关处）——必须使用 qualified 义项或显式引用对应 V-* 条目/义项；违反即 gate fail。

### 最小 remediation 集（按优先级）

- **R-1（P0）**: 新增 structured-concurrency 词条，按 OD-2：canonical term + 平台 realization（nursery S-084 / CoroutineScope S-085 / task group S-086），Virtual Threads 显式排除，StructuredTaskScope 标 NEEDS_EVIDENCE（B-2）。
- **R-2（P1）**: V-005-C/D「强于/更强」全序断言改写为故障模型相对表述，或保留排序但标注 PROJECT_DEFINED（OD-B 二选一）。
- **R-10（P1）**: V-008-A「没有 timeout 的操作是时间维度上的无界」加「除非存在 deadline/配额/上游取消等其他时间界」限定；V-008-C 补 RPC 传播取消 vs 结构化 scope 取消的双语义一行（S-042 vs S-084..086）。
- **R-11（P1）**: V-021-F / V-013-C 的 expand-contract 半按 CA 指令 split-or-downgrade：标 NEEDS_EVIDENCE 或拆出独立行（可锚 S-044 方向语义为相邻支撑）；完整出处走 B-6。
- **R-4（P2）**: V-013-A/B 状态 STABLE→CONTEXT_QUALIFIED + 强制 reader/producer 视角标注。
- **R-3（P2）**: V-002-B/C 语境拆分（C4 component 非独立部署；service 补非网络语境行）。
- **R-5（P2）**: V-010-A 补 RQ2-004 链接；V-011-B 补 `atomic consistency` 危险 alias 警告。
- **R-6（P2）**: V-008-E 补 S-090「全链路成立」限定 + S-081 actor mailbox 反例；V-008-E↔F 方向对照（传导 vs 主动卸载）。
- **R-7（P2）**: V-019-B 补「部署单元≠组织/领域边界」（S-109）；V-020-B 补业务流程义一行（S-037/S-038）。
- **R-8（P2）**: V-009-B 登记变体族（SSOT / system of record / authoritative state，非同义 + 差异注记）+ 引 S-105（owner 语义标 vendor-scoped）。
- **R-9（P3，可选）**: stateless 微词条（REST S-039 vs LLM 调用 S-103）；V-006-D 补引 S-087。

---

## 9. 真正需要 owner 决策的问题

- **OD-A**: R-1/R-2（建议连同 R-4/R-10/R-11，皆一行级）未落盘前，Stage 4 是否允许开工？挑战者建议：不允许——R-1 是证据导航锚点，R-2/R-10/R-11 防止无源断言与缺源 tactic 表述被原则文本直接继承。
- **OD-B**: R-2 修法二选一：改写为故障模型相对表述（挑战者推荐，更贴 corpus），或保留排序但标注 PROJECT_DEFINED 项目约定。
- **OD-C**: V-019-D EDA 状态：接受 Kimi 的 CONTEXT_QUALIFIED，还是按 F-CA-7 翻转为 NEEDS_EVIDENCE？
- **OD-D**: 统一 `Origin: PROJECT_DEFINED | SOURCE_NORMALIZED | PROJECT_META` 字段（F-CA-9）：本修订轮加（约 7 处行内改字段），还是 Stage 4 工具化时统一处理？
- **OD-E**: expand-contract 处置：降级 NEEDS_EVIDENCE（挑战者建议，最贴 CA「split or downgrade」指令），还是触发 B-6 定向回填一手源后保留完整 tactic 家族？

---

## 10. 挑战者元声明

- Pass B 在 Pass A 盲写基线（e6d67b3）之上执行；Kimi 词汇表仅在 CA 接受 Pass A 之后读取（3f386db 固定 SHA 快照）。
- 本轮为 Codex harness + GLM 5.3 编排重建：工作区中存在 WorkBuddy 未持久化的 Pass B 草稿（其空 blob 提交 626920e 已被 CA supersede）。本报告未照单采信该草稿——全部事实判定对固定 SHA 独立复核，修正其 F-CA-4（原评 ADDRESSED，实为 deadline 半修）与 F-CA-8（原评「确认在场」，实为 S-011 回读证伪 expand-contract 支撑）两处评估，并新增 OD 合规核对与 SOURCE_NORMALIZED 层。
- 全部判定可回放：词条 V-* 编号 + S-ID + 本报告章节号。
- 本报告未修改 Primary 任何产物；未创建竞争性词汇表；未进入 Stage 4；未重开 Source Collection。
- Pass A 的 4 项 alias 假设被证伪并公开撤回（RA-1..RA-4）——对账是双向的。
