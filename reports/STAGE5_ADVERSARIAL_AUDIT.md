---
id: STAGE5-ADVERSARIAL-AUDIT
title: "Stage 5 Independent Adversarial Falsification — Pass A (Blind)"
stage: 5
pass: A
role: challenger
challenger: "Codex harness + GLM 5.3"
branch: challenge/stage5-falsification
baseline: 05cfea4981c77d9a13520762e2e37244d4079bce
date: 2026-09-18
blind: true
status: COMPLETE
---

# Stage 5 Independent Adversarial Falsification — Pass A（盲审）

## 0. 方法与盲审声明

本报告是 Issue #12 指派的 Independent Adversarial Falsifier（Codex harness + GLM 5.3）的 **Blind Pass A** 产物。写作时未读取 `research/stage5-falsification` 上的任何 Kimi Stage 5 输出。攻击对象是 baseline `05cfea49` 上 sealed 的 11 个候选（P-001/002/003/004/006/007/008/009/010/012/013；P-005/P-011 已移除且未复活）。

方法：对每个候选执行 A–H 攻击模型（necessity / sufficiency / scope / mechanism / cost / independence / evidence / good-case），并完成 D-01..D-14 预注册判别。攻击优先寻找：成熟系统违反原则但仍然正确的 GOOD CASE、满足原则却仍失败的反例、适用范围更窄的证据、成本大于收益的场景、无法独立失败的对、同 lineage 误计多源、tautology/property/heuristic/process rule 证据、backend/cloud bias、非 distributed 形态反例。

纪律：不创建 S-* ID；不修改 source-manifest.yaml / sources/ / principles/；外部证据只记 SOURCE_CANDIDATE（§6）。「未找到反例」不作为证明；disposition 词汇用 SURVIVES / NARROW / DEMOTE / REJECT / MERGE_CANDIDATE / CONTESTED / NEEDS_EVIDENCE。

## 1. 十一候选攻击档案

### 1.1 P-001 Explicit Ownership

**A — necessity**：最强攻击是 Erlang/OTP let-it-crash：表面「不管理生命周期、崩溃即重启」像是无所有权，但 supervisor 树恰是显式 ownership 的运行时实例——每个 process 有 supervisor、链接语义与重启策略，归属由 runtime 强制。攻击失败，转为支持案例。GC 管内存可达性，不管任务/会话/业务实体的语义归属（timer、外部副作用、分布式请求上下文都不归 GC）——GC 语言中 ownership 失效（泄漏的 timer、孤儿 promise）依旧真实存在。
**B — sufficiency**：归属清晰但清理依赖纪律执行（owner 存在但不 poll）时仍会泄漏——候选主张的是「能回答归属问题」是必要条件而非充分条件，statement 本身未声称充分，不构成致命攻击。
**C — scope**：单线程一次性脚本已在豁免面内。注意「explicit」必须包含 runtime 强制/语义保证的所有权（OTP supervisor、structured scope），仅文档说明不算——否则候选退化为文档仪式。
**D — mechanism**：因果链（归属悬空→泄漏/孤儿/陈旧写）与 S-062/S-091 事故证据一致，未见 post-hoc。
**E — cost**：小系统 scope ceremony 的成本已在 Trade-offs 承认。
**F — overlap**：D-06/D-07/D-02/D-01 见 §2；与 P-002 的「有边界但无归属」「有归属但无边界」案例对存在，不合并。
**G — evidence**：S-084..086 是同一概念谱系的平台实现（Stage 4 已按单族计），加 S-091/S-062 事故与监管文件，无新增 lineage 问题。
**H — good case**：fire-and-forget + 全局 deadline（有界但无主）是合法形态吗？不——deadline 只保证终止，不保证语义清理（部分副作用已发生）；真正的 good case 是 runtime 隐式提供归属（actor 的 supervisor、JS 事件的 target 归属），这恰要求「explicit = 被执行模型实际提供」的澄清。

**Disposition：SURVIVES**（附澄清：explicit 包含 runtime/语义强制，文档声明不算）。

### 1.2 P-002 Change-Decision Boundaries

**A — necessity**：三个真实反压力：(i) 错误早期抽象——Sandi Metz 的 wrong abstraction 论点（duplication 比 wrong abstraction 便宜，SC-08），过早冻结错误决策轴；(ii) 横切关注点（logging/auth/tracing）结构上抵抗按决策模块化，历史上用 AOP 等机制补；(iii) 变化轴不可预测时错误边界比无边界更糟——statement 的 Does Not Necessarily Apply 已内置此豁免，边界条件是承重的而非装饰。
**B — sufficiency**：边界正确划分但组织协调失败（跨团队接口契约不遵守）仍演进失败——但那是 P-008 域的失败，不属于本候选保护属性的反例。
**C — scope**：适用面「多次变更 + 粒度值得 ceremony」已恰当收窄。
**D — mechanism**：Parnas KWIC 是示例性论证非受控实验（候选已标注）；变更成本公式的「协调成本」项缺乏形式化——机制方向成立但强度弱于表述。
**E — cost**：见 A(i)；间接层成本已在 Trade-offs。
**F — overlap**：D-03 见 §2——P-006 的独立因果内容单薄，倾向 P-006 降级为本候选的可度量结果。
**G — evidence**：S-001/S-005/S-012 存在教材谱系同源风险（SEI/Parnas 学术一轨）；S-109（Shopify 实证）与 S-112（平台契约）补足独立性。Google monorepo 大范围协调变更但高绩效（工具补偿 distance cost）——对本候选是边界确认（变化规则相同时无需人为分裂边界），对 P-006 是直接攻击。
**H — good case**：约定优于配置的系统（Rails）变更可达局部而无显式接口边界——这是 D-03 判别的第一臂，说明「局部性可由约定达成」，支持 P-006 与 P-002 分层的说法，但削弱「显式边界必要」的强读法；statement 用「应按决策划分」而非「必须有形式边界」，可容纳。

**Disposition：SURVIVES**（窄化确认：变化轴不可预测时的豁免必须保留在最终表述中）。

### 1.3 P-003 Bounded Execution

**A — necessity**：主事件循环/main loop 本身是无限循环、streaming 系统时间上无限运行、OS scheduler 永不退出——「无界时间」本身不是危害。关键澄清：候选的「时间有界」必须读作**每单位工作 / 每请求 / 每消息的资源维度有界**，不是程序总运行时。在此读法下 streaming（Kafka/Flink）时间无界但空间与速率有界（windowing/backpressure），恰支持维度化表述；候选 statement 列举的维度（内存/队列/重试/扇出）本就是 per-work 维度，「时间」一词需要 Stage 6 明确为 per-work latency/deadline。
**B — sufficiency**：全链有界但无准入分级时过载下关键流量等概率被弃（D-04 第一臂）——有界不保证「保对的流量」，这是 P-012 独立存在的证明，不是 P-003 失败。
**C — scope**：探索式计算豁免已内置。
**D — mechanism**：Little's Law 只约束均值稳态，尾延迟有界需独立论证（S-077 已在 corpus）；机制链整体成立。
**E — cost**：小流量内部工具的全套配额是过度工程——statement 用「可说明的上限或受控降级」，隐含界可以是粗的/隐含的（offline 批处理按输入有界），可容纳。
**F — overlap**：D-04/D-07 见 §2，与 P-012 分立成立。
**G — evidence**：corpus 中例证形态最多样的候选（定理+云厂商+规范+事故+平台），无 lineage 问题。
**H — good case**：UI 虚拟列表「无限滚动」实为有界化渲染（只渲染视口）；REPL 长会话是用户自担的探索豁免。两个 good case 都被现有豁免面覆盖。

**Disposition：SURVIVES**（附术语澄清：所有维度均为 per-unit-of-work 界，非程序总运行时；Stage 6 表述时必须显式）。

### 1.4 P-004 Failure Containment ∝ Responsibility

**A — necessity**：SQLite 单进程嵌入、无进程隔离，是成熟且正确的设计（SC-02）——graded 豁免（「故障权力≤职责」是 heuristic 面非绝对律）已内置并真实承重。共享 DB 的多组件设计有时是正确经济选择（豁免面已含）。
**B — sufficiency**：隔离边界存在但防御机制自耦合时（S-063：DNS 保护机制撤 BGP 反而放大故障）blast radius 超出设计 failure domain——候选把该形态列为反面机制证据而非反例，处理正确：隔离的「实现缺陷」不否定「按影响范围设计隔离」的主张。
**C — scope**：单用户单机、嵌入式弱隔离形态（S-113）已 scoped。
**D — mechanism**：R5 修正后 failure domain（静态结构分区）/ blast radius（动态结果影响面）分离清晰，未见再混淆。
**E — cost**：小团队 SaaS 过度 cell 化的容量冗余与运维单元数上升是真实成本反例——graded 表述是唯一正确回应。
**F — overlap**：D-05 见 §2，与 P-009 分立成立（信任权力小但故障权力大 vs 反之的案例对存在）。
**G — evidence**：S-050/S-048/S-052 等存在 AWS/SRE 生态集中，但 S-061/S-063/S-060 事故实证 + S-053 安全科学补足独立族。
**H — good case**：单进程桌面应用全部组件同生共死（无隔离）是合法设计（经济性豁免）；Chromium 反向证明桌面形态下进程隔离的价值（SC-09）——两个方向都在 graded 框架内。

**Disposition：SURVIVES**（scoped/graded 维持；D-10 的 blast radius 度量不可操作问题保留为 NEEDS_EVIDENCE，不阻塞候选本身，但阻塞其可测量性主张）。

### 1.5 P-006 Change Locality

**A — necessity**：Google monorepo + 大规模自动化工具（大规模变更文化）实现高性能演进——变更高度分散（跨数千目标）但工具补偿协调成本。这不是「违反原则仍正确」的直接反例（principle 说局部化是结构质量的信号，没说必须人为缩小变更面），但证明「变更集中度」单独不构成因果主张，工具/组织变量可以主导结果。
**B — sufficiency**：变更局部但系统仍演进失败（局部性是语法指标，不保证语义正确演进）——满足指标不保属性。
**C — scope**：变化方向可预测时才有意义的条件已内置，但该条件与 P-002 的适用条件几乎同构。
**D — mechanism（核心攻击）**：statement 第一句（好结构使高频变化局部化）是 P-002 信息隐藏机制的**后果**——按决策划分边界自然导致变更局部；第二句（传播范围是可观察信号）是 **metric/property** 陈述（change amplification 可从版本历史事后度量）。候选自身承认与 P-002「共享 Parnas 机制」。独立因果内容只剩「局部性本身有独立于边界划分的因果效力」，而 D-03 的约定式系统（Rails：无显式边界但变更局部）恰好说明局部性可由**约定**达成——这把 P-006 的独立空间压缩到「度量层」而非「因果层」。
**E — cost**：为局部化而局部化（变化轴判断错误时集中点选错）已承认。
**F — overlap**：D-03 见 §2。
**G — evidence**：单源 S-001（theoretical/heuristic），证据基线是 11 个候选中最弱的，RQ3-001 缺口明确。
**H — good case**：见 A。

**Disposition：DEMOTE（倾向性，留 Pass B 对账）**——P-006 应降级为 P-002 的 measurable property / evolution-health metric。不存在「禁止度量」的问题，但它不是独立因果原则。owner decision（Stage 4 已登记 metrics 层缺失）与此一致：Stage 7 需要 metrics/property 层来安放此类可观察信号。

### 1.6 P-007 Designed Diagnostic Surfaces

**A — necessity（关键攻击）**：seL4 形式验证微内核——功能正确性经机器证明，运行时可观测面极小，却是可靠性最高的系统类别之一（SC-01）。同类：确定性系统、纯函数核心 + 显式边界的小测试面。这是对「运行时必须有诊断表面」的直接反例。但注意候选 statement 已经是「架构性地放置区分正常/异常所需的状态与信号」——对 seL4，「区分正常/异常」的证据被**构建时验证**替代：证明本身是设计时内置的 diagnostic surface。攻击因此收窄为：候选的纯运行时读法必须修正为「证据必须设计时内置：运行时 telemetry 或构建时 verification 二者居一」。
**B — sufficiency**：信号存在但不可行动（S-062 的 97 条预警无人处置）仍失败——候选已把该形态纳入机制叙述（位置/信噪比设计失败），成立。
**C — scope**：嵌入式带宽/功耗约束（S-104）已 scoped；privacy/security 约束形态是未闭合的收窄面。
**D — mechanism**：因果核「信号位置是架构分配、缺失位置则证据不可事后重建」与 S-053（运维理解是防御层）一致；但「位置」与「运维结果」的因果链无受控证据——D-11 的结构侧判别（两个设计只在信号位置不同，运维结果可分）在对比案例中成立（宽事件 vs 聚合指标的归因能力差异），缺少受控/系统比较证据。
**E — cost**：instrument-everything 的成本已排除（不主张）；「最低诊断表面」的量化缺失是真实成本模糊面。
**F — overlap**：与 P-001/P-010 的信号归属维度可分，未见合并压力。
**G — evidence**：S-048/S-049/S-055/S-058 的 Google SRE + OTel 谱系集中——但 SRE 谱系与 OTel 标准的立场独立性有限（OTel 传承 Google Dapper/OpenCensus 一线，Stage 4 已计两族，此处维持「两族但同厂商起源风险标注」）；S-053/S-062 是真正独立族。
**H — good case**：seL4（见 A）；一次性脚本豁免已内置。

**Disposition：NARROW**——因果核保留但收窄为「诊断证据必须设计时内置（运行时 telemetry 或构建时 verification），且其位置是架构分配」；纯运行时表述不成立。D-11 判别：结构侧对比案例存在但缺受控证据 → 维持「条件性成立」，若 Pass B/Stage 6 找不到更强结构判别证据，按候选文件预注册的条件降为 required property。

### 1.7 P-008 Contract Preservation

**A — necessity（最强攻击，结果为 good case 确认）**：Linux kernel 内部 API/ABI 明确不保持稳定（stable-api-nonsense，SC-04）：紧协调的单组织系统里，保持内部接口兼容的成本（冻结演进、为兼容打补丁）高于让所有使用方随树一起改。这是「破坏兼容比保持兼容更正确」的成熟 canonical 案例。候选的豁免面（单一所有权内内部接口）恰好覆盖，说明豁免不是装饰而是承重结构——但也证明豁免边界的判定（何谓「独立演进节奏」）是候选真正的主战场。
**B — sufficiency**：schema 完全兼容但行为语义漂移（返回码含义变化、时序变化）仍破坏交互——候选已把 contract 定义为接口+行为语义+非功能承诺（V-012-B），且自认「行为语义兼容的实证较薄」：满足机检 schema 兼容不保证契约保持，可执行面确实窄于口号。
**C — scope**：原型期豁免已内置；desktop ABI 形态实证缺席（RQ2-013）——SC-05（Raymond Chen / Win32 兼容文化）是该缺口的直接候选证据：Win32 几十年 ABI 兼容是 desktop 形态下 contract preservation 的强支持。
**D — mechanism**：「破坏契约=成本转嫁」机制与 S-044 的机检兼容谓词一致；expand-contract 已按 R3 清除出因果链，无残留违规。
**E — cost**：并存期双栈维护已承认。
**F — overlap**：与 P-002（边界划分 vs 边界上的契约保持）可分：错误边界 + 完美契约保持仍演进失败，正确边界 + 契约随意也失败——两轴独立。
**G — evidence**：S-039/S-042/S-044/S-045 集中于 schema/API 层规范，行为语义层薄（已自认）；S-037/S-038 分布式谱系独立。
**H — good case**：安全修复强制破坏兼容（故意 break 是显式带成本决策的合法形态——statement 明确「破坏是显式决策而非副产品」，安全 break 属于此类）；Linux 内部 API（见 A）。

**Disposition：SURVIVES**（边界确认：单一所有权豁免承重；行为语义兼容不可机检是真实收窄面，保持 NEEDS_EVIDENCE 而非扩大口号）。

### 1.8 P-009 Trust Minimization

**A — necessity**：单用户桌面/嵌入式形态：VS Code 扩展生态历史上粗粒度信任（扩展获得全能力而非声明式最小权限）仍形成繁荣生态；Excel 宏历史宽松；裸机嵌入式无 MMU 时细粒度信任边界在硬件上不可执行——威胁模型粗/缺时 minimization ceremony 不付值。graded 豁免已覆盖大部分，但「supply chain 仍是不可信输入」的注释把豁免面收回一部分，处理诚实。
**B — sufficiency**：权限最小化但供应链投毒（依赖本身恶意）仍失败——最小权限限制损害上限但不消除；候选主张的是上限化不是消除，一致。
**C — scope（重要）**：不得把企业 zero-trust 证据 universalize（Issue #12 明确禁令）；least privilege 在微服务扩散后的运维爆炸（权限矩阵的组合复杂度、每服务凭证管理的认知成本）是机制自身成本反噬的真实形态——候选 Trade-offs 已列「过度细分权限的运维负担」，但没有证据量化该成本何时压倒收益。
**D — mechanism**：Saltzer-Schroeder 的「损害≤权限」是近乎定义性的上界论证（机制成立），但「经济性何时值得」是未决问题。
**E — cost**：见 C——这是本候选最大的真实攻击面。
**F — overlap**：D-05 见 §2，与 P-004 分立成立。
**G — evidence**：独立性最强的候选之一（1975 经典 + NIST + OWASP + 平台契约），无 lineage 问题；S-110 agentic 形态 2025-12 极新，稳定性 CONTESTED 已标。
**H — good case**：本地开发工具的宽信任（dev container 内 root）是合法效率选择——豁免面覆盖。

**Disposition：SURVIVES（scoped/graded）**——附两条保留：(i) 微服务权限爆炸的量化成本证据缺失（NEEDS_EVIDENCE）；(ii) agent 形态方法论成熟度不足（维持 Stage 4 标注）。

### 1.9 P-010 Authoritative State

**A — necessity（D-14 核心攻击）**：CRDT 多写副本 + 确定性合并语义——没有「单一权威写者」但系统正确且成熟（SC-06）。R4 修正后的双维框架（write authority / consistency semantics 正交但都显式声明）恰好容纳：CRDT 的维度 1 是「全体副本持有写权（显式声明的多写 authority 形态）」，维度 2 是「合并语义（CRDT 半格）显式定义」。Kafka append-only log：权威是 log 本身（写入顺序由 log 定序），派生投影可重建（豁免面）。攻击确认双维框架是必要的最小结构，未击穿。
**B — sufficiency**：权威与一致性语义都声明但实现有 bug（合并函数错误）仍失败——实现缺陷类，不构成原则反例。
**C — scope**：纯派生/只读豁免已内置；「可接受漂移量」表述缺失（已标 NEEDS_EVIDENCE）。
**D — mechanism**：R4 后「权威强度=一致性强度」等式已删除，正交性论证与 S-034/S-038 一致。
**E — cost**：event sourcing 回放成本、强裁决的延迟代价已列。
**F — overlap**：D-06/D-09 见 §2，与 P-001/P-013 分立成立。
**G — evidence**：S-040/S-046（Fowler 谱系）+ S-038（Helland）+ S-023/S-034（学术）——Stage 4 已处理 Fowler/ThoughtWorks 同轨问题（P-005 移除时），本轮无新增。
**H — good case**：local-first 的设备侧主副本 + 云端同步（S-107）：看似「无中心权威」，实际是权威随实体分布 + 合并语义显式（维度化框架内合法）。

**Disposition：SURVIVES**（R4 双维框架通过 D-14；CRDT/log/local-first 形态证明框架的容纳力而非否定它）。

### 1.10 P-012 Overload Admission & Graceful Degradation

**A — necessity**：负载天然有界的系统（内部工具、单用户应用）——豁免已内置。水平无状态扩展 + autoscaling + 客户端退避：S-050 明确主张服务端仍需配额（否则重试风暴击穿），不支持完全豁免。
**B — sufficiency**：有准入分级但分级错误（误杀高优先级流量、依赖图未建模导致保护非关键路径）仍失败——策略正确性是第二层失败，不否定「必须有策略」。
**C — scope（D-12 核心攻击）**：非服务端形态实证薄：Desktop 离线队列溢出、mobile 后台任务风暴是适用形态但 corpus 无实证；嵌入式 RTOS 的准入=静态优先级配置（S-113 弱形式成立）。诚实标注：跨形态成立是概念性判断，证据集中服务端。
**D — mechanism**：L=λW 失稳 + retry 放大 + 容量损失反馈环的因果链是 corpus 中最扎实的之一。
**E — cost**：降级路径是「第二套需维护的行为」已承认。
**F — overlap**：D-04 见 §2，与 P-003 分立成立。
**G — evidence（弱点）**：S-048/S-049/S-050/S-052/S-090 厂商/规范集中（SRE+AWS 同生态叙事），事故实证（S-061/S-065）独立补足——维持 Stage 4 的集中度标注。
**H — good case**：批处理系统按输入大小天然限流（隐式准入）——「显式准入」要求需要宽容读法：静态容量配置也算显式设计。

**Disposition：SURVIVES（scoped）**——非服务端形态证据缺口维持 NEEDS_EVIDENCE（D-12），不阻塞候选但限制 universal 表述。

### 1.11 P-013 Execution-Model-Honest Correctness

**A — necessity**：actor 串行邮箱、单线程事件循环非抢占、协程挂起点语义——时序保证「隐式」但由模型**实际提供**：候选要求的是保证由执行模型真实提供而非文档声明，actor 模型恰满足（保证来自模型语义）。攻击转为支持案例。
**B — sufficiency**：保证齐备但业务逻辑错误仍失败——平凡实现缺陷，不在攻击范围。
**C — tautology 攻击（核心）**：「正确性不得依赖不存在的保证」接近定义性真理——反例不可能存在（依赖不存在保证的系统按定义不正确）。候选的非平凡内容在于：(i) assumed-vs-provided 缺口是**真实复发性失效模式**（S-091 Pathfinder：时序窗口只在真实数据率暴露——「以为有保证」与「模型实际提供」的差距是事故的直接原因）；(ii) 该缺口在评审时不可自动判定（保证核验的机械化程度 NEEDS_EVIDENCE）。因此候选不是纯 tautology，但必须标注其「经验内容 = 缺口的现实发生率与不可判定性」，而非命题本身。
**D — mechanism**：Lamport 偏序 / FLP / DLS 的理论锚扎实；S-084..086 平台谱系按单族计（Stage 4 已处理）。
**E — cost**：保守串行化的吞吐代价已列。
**F — overlap**：D-02/D-09 见 §2，与 P-001/P-010 分立成立。
**G — evidence**：分布式理论 + 平台契约（单谱系）+ 航天事故——单进程理论锚薄（自认），无新增问题。
**H — good case**：协作式调度下「挂起点之间不被打断」的正确依赖（模型真实提供）——不是违规而是候选的正面实例。

**Disposition：SURVIVES**（附 tautology 标注：非平凡性依赖 assumed-vs-provided 缺口的经验现实性与不可判定性，Stage 6 表述时必须保留该经验内容，否则退化为正确性定义）。

## 2. D-01..D-14 判别结果

| D | 判别 | 结果 | 说明 |
|---|---|---|---|
| D-01 | P-001 vs P-002 | **DISTINCT** | 「有边界但任务/状态归属不明」（模块接口清晰，worker 池无 owner）vs「归属清晰但无边界」（单 owner 巨石，变更全穿透）案例对存在；两轴可独立失败。 |
| D-02 | P-001 vs P-013 | **DISTINCT** | 归属明确但时序保证缺失（owner 明确的 async 写，无版本防护 → stale overwrite 归 P-013）vs 时序保证齐备但清理归属悬空（取消语义完整，但 timer 无人认领 → 孤儿归 P-001）。 |
| D-03 | P-002 vs P-006 | **DISTINCT（但 P-006 因果内容不足以独立）** | 约定式系统（Rails）变更局部但无显式边界（局部性可由约定达成）；错误边界系统有边界但变更不局部。两臂都存在 → 判别成立、不合并；但第一臂同时证明局部性不是边界的专属产物，P-006 的独立因果主张被抽空 → DEMOTE 倾向的依据。 |
| D-04 | P-003 vs P-012 | **DISTINCT** | 全链有界但无准入分级（过载时关键流量等概率被弃）vs 有准入降级但重试维度无界（策略被放大击穿）。独立可失败，不合并。 |
| D-05 | P-004 vs P-009 | **DISTINCT** | 低权限组件经共享资源放大故障（信任小/故障权力大：无权限服务打挂共享 DB）vs 隔离良好但权限过宽（横向移动：故障域小/信任权力大）。案例对存在。 |
| D-06 | P-010 vs P-001 | **DISTINCT** | 权威清晰但实体无主（状态裁决明确，操作该状态的进程泄漏+权威并存）vs 归属清晰但一致性义项未声明（owner 明确，缓存副本漂移无定义）。 |
| D-07 | P-001 vs P-003 | **DISTINCT** | 有界无主（fire-and-forget + deadline：终止有界但语义清理无主）vs 有主无界（scope-owned 计算，scope 内无算力/时间界）。取消语义归 P-001，资源界限归 P-003。 |
| D-08 | safety floor 存在性/范围 | **CONFIRMED（contextual）** | seL4（SC-01）、DO-178C、IEC 61508 证明存在「适用语境内不可协商的安全地板」；不溢出为全局绝对律——Constitution 公理层须保留 in-applicable-contexts 限定。 |
| D-09 | P-013 vs P-010 | **DISTINCT（交集归 P-013）** | 全序化序列的重复投递（时序/交付语义问题归 P-013）vs 权威齐备但时钟漂移破坏顺序（交集：时钟保证属执行模型诚实性，归 P-013）。 |
| D-10 | P-004 blast-radius 可操作性 | **NEEDS_EVIDENCE** | blast radius 无规范化度量（用户数/请求比例/数据面/收入？）；「职责相称」的可判定性未解决。不阻塞候选存在性，阻塞其可测量主张。 |
| D-11 | P-007 结构可判别性 | **CONDITIONAL** | 结构侧对比案例存在（信号位置不同而其余相近的设计，归因能力可分：宽事件 vs 聚合指标）；缺受控/系统比较证据。若 Stage 6 无更强证据，按预注册条件降为 required property。 |
| D-12 | P-012 非 server 形态 | **NEEDS_EVIDENCE（倾向成立）** | RTOS 静态优先级=弱形式准入（成立）；desktop/mobile 离线队列、后台任务风暴概念适用但 corpus 无实证。 |
| D-13 | H7 locality 复活测试 | **NOT RESURRECTED** | 未发现「单一 locality 机制」（如通信成本超线性）的权威证据；变更局部性（P-006）与通信局部性是不同机制，后者 corpus 无锚。维持 H7 降级。 |
| D-14 | P-010 CRDT/多写边界 | **FRAMEWORK HOLDS** | CRDT=维度 1 多写 authority 形态 + 维度 2 显式合并语义；append-only log=log 自身为权威；local-first 主副本=权威随实体分布。双维框架容纳全部攻击形态，无需 single-writer。 |

## 3. GOOD CASE / false-positive register

| # | 系统/形态 | 关联候选 | 结论 |
|---|---|---|---|
| G-01 | Linux 内核内部 API 有意不兼容 | P-008 | 单一所有权豁免的 canonical 证明；豁免边界承重。 |
| G-02 | SQLite 单进程无隔离 | P-004 | graded 豁免真实；隔离成本可超保护价值。 |
| G-03 | seL4 极低运行时遥测 + 形式验证 | P-007 | 验证替代遥测：诊断证据设计时内置的构建时形态。 |
| G-04 | 主事件循环/流式系统时间无界 | P-003 | 界是 per-work 维度，非程序总运行时。 |
| G-05 | GC 管内存不管语义归属 | P-001 | 内存可达性 ≠ 任务/会话语义所有权。 |
| G-06 | Erlang/OTP let-it-crash + supervisor | P-001 | 看似无所有权，实为 runtime 强制的显式归属。 |
| G-07 | VS Code 扩展粗粒度信任 / Excel 宏历史 | P-009 | 威胁模型粗时 minimization 不付值。 |
| G-08 | Google monorepo 大范围协调变更 | P-006（攻击）/ P-002（边界确认） | 工具补偿协调成本；变更集中度单独不是因果主张。 |
| G-09 | CRDT 多写 + 合并语义 | P-010 | 双维框架内的合法显式形态。 |
| G-10 | append-only log（Kafka 类） | P-010 | log 自身为权威；投影可重建豁免。 |
| G-11 | actor 串行邮箱 / 事件循环非抢占 | P-013 | 保证由模型实际提供 = 候选正面实例。 |
| G-12 | 约定优于配置（Rails 类） | P-002/P-006 | 局部性可由约定达成；显式边界非唯一路径。 |

## 4. Lineage / evidence 攻击汇总

本轮无 Stage 4 未处理的**新增** lineage 问题。已登记并维持的集中度标注：P-012 的 SRE/AWS 生态叙事集中（事故实证独立补足）；P-007 的 Google SRE→OTel 谱系同源风险（S-053/S-062 安全科学/监管独立）；P-013 的 S-084..086 平台契约单族（理论+事故锚独立）；P-010 的 Fowler/ThoughtWorks 轨道（学术+Helland 独立）。P-002 的 S-001/S-005/S-012 教材谱系同源风险由 S-109/S-112 补足。source-family independence 未被高估到需要推翻任何 disposition 的程度，但 P-012 的 vendor 集中度是最接近「多源实为同叙事」的案例。

## 5. 跨形态缺口

- **Backend/cloud bias**：P-012（非服务端实证薄，D-12）、P-007（隐私/安全约束形态未闭合）最明显；P-008 的 desktop ABI 形态实证缺席（SC-05 是直接补源候选）。
- **嵌入式**：P-004（隔离弱化形态）、P-013（单进程理论锚薄）已有 scoped 处理，无新增反例。
- **Browser/frontend**：P-003 的事件循环证据（S-088）在 corpus 内，本轮无新增。
- **local-first / agent runtime**：P-009（S-110 极新）、P-010（S-107）已有形态证据，P-001 的 agent 任务归属是概念适用但无实证的形态。

## 6. SOURCE_CANDIDATE 记录

Challenger 未分配 S-* ID、未修改任何 canonical source 文件。全部条目为 Stage 5 攻击中实际使用的外部证据，供 Chief Architect 裁决是否晋升（预计对应 Kimi 侧 RQ5-* / S-114+ 决策）。

| # | title | author/org | URL | year | 攻击对象 | why it matters | 验证状态 |
|---|---|---|---|---|---|---|---|
| SC-01 | seL4 微内核（形式验证） | seL4 Foundation / Trustworthy Systems, UNSW | https://sel4.systems/ | 2009– | P-007 / D-11 / D-08 | 机器证明替代运行时遥测的高可靠系统：P-007 纯运行时表述的反例，诊断证据构建时内置的 canonical 案例 | HTTP 200（2026-09-18） |
| SC-02 | SQLite 架构文档（单进程、无隔离设计） | SQLite Consortium | https://www.sqlite.org/arch.html | 2009– | P-004 | 成熟系统在单进程形态下正确地放弃隔离：graded 豁免的实证锚 | HTTP 200（2026-09-18） |
| SC-03 | PostgreSQL WAL（Write-Ahead Logging）文档 | PostgreSQL Global Development Group | https://www.postgresql.org/docs/current/wal-intro.html | — | P-010 | append-only log 作为权威、派生状态可重建的 DB 形态实例（log-as-authority） | HTTP 200（2026-09-18） |
| SC-04 | stable-api-nonsense（Linux 内核内部 API 不保证兼容） | Linux Kernel Organization | https://www.kernel.org/doc/html/latest/process/stable-api-nonsense.html | 2017– | P-008 | 紧协调单组织系统破坏兼容比保持便宜：P-008 单一所有权豁免的 canonical good case | HTTP 200（2026-09-18） |
| SC-05 | The Old New Thing（Win32 ABI 兼容文化） | Raymond Chen / Microsoft | https://devblogs.microsoft.com/oldnewthing/ | 2003– | P-008 | desktop/ABI 形态下契约保持的长期实证（RQ2-013 缺口的直接候选） | HTTP 200（2026-09-18） |
| SC-06 | Conflict-free Replicated Data Types | Shapiro, Preguiça, Baquero, Zawirski（INRIA） | https://hal.inria.fr/inria-00555588/document | 2011 | D-14 / P-010 | 多写 + 显式合并语义的 canonical 理论来源：验证双维框架对 CRDT 的容纳 | HTTP 200（2026-09-18） |
| SC-07 | Erlang/OTP 进程与监督语义文档 | Erlang/OTP 社区 / Ericsson | https://www.erlang.org/docs | 1986– | P-001 | supervisor 树 = runtime 强制的显式 ownership：necessity 攻击转为支持案例的锚 | HTTP 200（2026-09-18） |
| SC-08 | The Wrong Abstraction | Sandi Metz | https://www.sandimetz.com/blog/2016/01/20/the-wrong-abstraction | 2016 | P-002 / D-03 | 错误抽象比重复更贵：过早边界冻结的成本反例，P-002 豁免面承重的锚 | **原 URL 404**（www 与裸域均 404，2026-09-18）；Wayback 存档验证因 archive.org 网络不可达未完成——内容主张广为转引，晋升前需 CA 找到可验证版本 |
| SC-09 | Chromium Site Isolation | Chromium 项目 / Google | https://www.chromium.org/Home/chromium-security/site-isolation/ | 2017– | P-004 | 桌面形态下进程隔离按职责分配故障域的现代实证（与 G-02 SQLite 构成两极对照） | HTTP 200（2026-09-18） |

## 7. Pass B 预注册对账检查（V5-01..V5-20）

Pass A 立场固定如下，Pass B 与 Kimi Primary 对账时逐项核：

| check | 内容 | Pass A 立场 |
|---|---|---|
| V5-01 | P-001 disposition | SURVIVES（澄清：explicit=runtime/语义强制） |
| V5-02 | P-002 disposition | SURVIVES（变化轴不可预测豁免承重） |
| V5-03 | P-003 disposition | SURVIVES（per-work 维度澄清必须进 Stage 6 表述） |
| V5-04 | P-004 disposition | SURVIVES scoped/graded；D-10 NEEDS_EVIDENCE |
| V5-05 | P-006 disposition | DEMOTE 倾向（P-002 的 measurable property/metric 层） |
| V5-06 | P-007 disposition | NARROW（构建时验证替代运行时遥测；D-11 条件性） |
| V5-07 | P-008 disposition | SURVIVES（单一所有权豁免承重；行为语义兼容收窄） |
| V5-08 | P-009 disposition | SURVIVES scoped/graded（微服务权限爆炸成本证据缺） |
| V5-09 | P-010 disposition | SURVIVES（R4 双维框架通过 D-14） |
| V5-10 | P-012 disposition | SURVIVES scoped（非服务端证据缺口维持） |
| V5-11 | P-013 disposition | SURVIVES（tautology 标注：经验内容=缺口现实发生率） |
| V5-12 | D-03 结果 | DISTINCT 但 P-006 独立因果内容不足 |
| V5-13 | D-07/D-04 独立失败对 | 均成立（P-001/P-003、P-003/P-012 不合并） |
| V5-14 | D-14 CRDT 处理 | 双维框架容纳，无需 single-writer |
| V5-15 | D-08 safety floor | contextual 成立（不溢出为绝对律） |
| V5-16 | D-10/D-11/D-12 证据状态 | 均维持 NEEDS_EVIDENCE / CONDITIONAL，不悄悄升级 |
| V5-17 | GOOD CASE register 覆盖度 | G-01..G-12 是否被 Primary 侧同覆盖（尤其 Linux API / SQLite / seL4 / monorepo 四个 canonical case） |
| V5-18 | SC-01..09 晋升必要性 | 只有影响 disposition/D-test 的才应晋升（预判 SC-04/SC-06/SC-08 影响最大；SC-08 需先解决 404） |
| V5-19 | lineage 集中度 | P-012 vendor 集中度是否被 Primary 低估 |
| V5-20 | 无 S-* 走私 | Challenger 未创建任何 S-* ID / canonical source 修改（fail-closed 项 6 核验） |

## 8. Genuine owner decisions

1. **P-006 去留**：Pass A 建议 DEMOTE 为 P-002 的度量层结果。若 Chief Architect 保留 P-006 为候选，需要指出独立因果内容或接受「单源 + 无独立机制」的现状；若降级，Stage 7 需要 metrics/property 层安放（与 Stage 4 已登记的 owner decision 合并处理）。
2. **P-007 降级条件**：D-11 只有条件性结构判别。接受「降为 required property」的触发条件现在就该固定（建议：Stage 6 开始前仍无受控证据即触发），避免事后移动球门。
3. **SC-08（Sandi Metz）晋升前置**：原 URL 404。若 Primary 侧也引用该论点，需要先找到可验证一手来源（存档或刊物版本），否则该攻击线降级为「广为转引但未验证」。
4. **SC 晋升范围**：9 个 SOURCE_CANDIDATE 中哪些进入 S-114+（建议仅限影响 disposition/D-test 的：SC-01/SC-04/SC-05/SC-06/SC-08 优先级最高），哪些留在报告引用层。
5. **P-013 的 Stage 6 表述边界**：保留 assumed-vs-provided 缺口的经验内容，还是接受更干净的 tautology 风险——这决定它进 Constitution 的措辞强度。

## 9. 元声明

- 本报告未读取 Kimi Stage 5 任何输出（盲审约束遵守）。
- 未创建 S-* ID；未修改 source-manifest.yaml / sources/ / principles/。
- 未进入 Stage 6：无 Constitution 草案、无 reduction、无 Stage 7 ontology。
- disposition 为 challenger 立场，最终裁决权在 Chief Architect；「未找到反例」未被当作证明使用。
