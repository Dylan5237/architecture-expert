---
id: STAGE4-PRINCIPLE-BOUNDARY-AUDIT
type: challenger-audit
stage: 4
pass: A (blind independent)
challenger: WorkBuddy / GLM 5.3 (semantic boundary analysis) + Codex harness (repository, git, read-back)
baseline: d6a7808611742dda6e2e6f9fa0154b12ae67b4a3
issue: 9
date: 2026-09-18
scope: Stage 1 H1..H11 + sealed Stage 2 corpus + canonical Stage 3 vocabulary
status: challenger-pass-a
---

# Stage 4 Challenger Pass A — Principle Boundary Audit（盲审）

## 0. 方法与盲审声明

本报告是 Stage 4 Principle Extraction 的 Independent Challenger Pass A，在 Kimi Primary 产出任何 Stage 4 内容之前完成。

盲审声明：

- 未读取 `research/stage4-principles` 分支上 Kimi 的任何 Stage 4 输出（refs 已 fetch，但未 show/log/diff 其内容）；
- 本报告不创建竞争性 P-* principle set，不预设 H1..H11 的最终去留；
- 不执行 Stage 5 反例战役；需要反例才能裁决的边界，登记为 Stage 5 preregistered discriminators；
- 不修改 canonical evidence（Stage 2 corpus）与 vocabulary（Stage 3）；
- 审计对象是 Stage 1 plan §6 的 H1..H11 假设与 baseline SHA 上密封的 corpus。

读取范围：`planning/STAGE1_RESEARCH_PLAN.md`（§2 RQ、§6 H 定义、§7 falsification 协议）、`02_VOCABULARY.md`（canonical）、`source-manifest.yaml`、`review-queue.yaml`（RQ2/RQ3 全部条目）、`sources/` 下 54 个源文件（S-001..113 抽样覆盖全部 11 个 cluster）、GitHub Issue #9 全文。

审计视角：每个 H 按「是 causal structural principle，还是 property / tactic / heuristic / meta-objective / process rule」判定；每个判定给出机制理由与证据锚点，不凭措辞强度。

## 1. H1..H11 逐项边界审计

### H1 — Purpose / Required-Property Fitness

**判定：META_OBJECTIVE / evaluation frame，不是 causal principle。**

H1 说的是「架构质量相对于所需属性与约束来评判」——这是所有其他原则的评判框架（ATAM 效用树 S-006、ISO 25010 S-008 是其操作化实例），自身不陈述任何「结构 X 在约束 Y 下保护属性 Z」的因果机制。它无法被结构反例证伪，只能被评估方法反例证伪，属于不同层面。

风险：若进入 P-* 集，会变成万能解释项（任何结论都可归因于「fitness 不同」），违反 plan §7 的歧视力要求。

处置建议：放入 Constitution 层作为评判公理，不占 principle 名额。safety/security 非 negotiable floor 子句保留其限定（"in applicable contexts"），不得扩为普适地板。

### H2a — Explicit Boundaries

**判定：机制候选成立，但自带坍缩风险（→ CF-4）。**

H2a 的可证伪核心是「boundary 只有对应 meaningful responsibility 才减少 change/failure/reasoning 传播」——前提子句（Parnas S-001：按变化方向隐藏）是机制，后半是边界质量的判据。风险在于退化为「划清边界」tactic：V-002-E 已裁定 boundary 至少有 module / process-service / bounded-context / trust 四类，机制不同，禁止以「划清边界」一语带过。

Stage 5 必须用反例区分：responsibility 错位的 boundary（变化仍跨界面传播）与无 boundary 但变化天然局部（单一职责小系统）的双向反例。

### H2b — Explicit Ownership

**判定：机制候选成立；与 H3 部分共享深层机制（→ CF-1）。**

结构化并发语料（S-084 Smith、S-085 Kotlin、S-086 Swift）给出的机制是：显式 scope ownership 把运行时实体的 lifetime 纳入结构化范围，从而消除 orphaning 与 stale work。V-003-A/B 已锚定 ownership/lifecycle 语义。

边界风险：与 H11 的独立性待验（ownership 是「谁管实体」，authority 是「谁的可写副本裁决」——V-003-D）；与 H3 的共享机制是「ownership scope 给 execution lifetime 一个结构上界」。RQ3-002 已登记：若主张 Java 平台特化（如 thread-per-task realization），证据不足，须回流。

### H3 — Bounded & Predictable Execution

**判定：机制候选成立，但最高 tactic 清单化风险。**

H3 覆盖 time / space / concurrency / queues / retries / fan-out / retained state 七个维度，corpus 对每个维度都有成熟 tactic（timeout V-008-A、deadline V-008-B、backpressure V-008-E、load shedding V-008-F、constant work S-050）。若 P-H3 写成这些 tactic 的清单，它就是 checklist 不是 principle。

成原则的唯一路径：锚定 V-021-C unboundedness 抽象（PROJECT_DEFINED，Stage 4 必须检验其解释力）——「关键路径上的工作不得在任一维度处于不可说明的无界状态，bounds 按 criticality 分级」。该表述有反例 discrimination（有界但错误分级 / 无界但非关键路径），且被 corpus 多数 failure pattern（retry storm S-052、queue 积压、fan-out 放大 S-077）共同需要。

### H4 — Failure Containment

**判定：graded heuristic / economics rule，不是普适定律（scope down）。**

「failure power ≤ responsibility 所需」在 RQ-B3 已被 plan 自己标注单进程/低成本反例风险：一个 shell 脚本误删主目录，failure power 远超其「responsibility」，但加 failure domain 隔离在经济上不合理。S-050 cell-based、S-048 SRE、S-063 Meta BGP 事故都支持该启发式在 multi-tenant / 高代价 / 物理共享形态下强成立。

词汇红线（Issue #6 已裁决）：blast radius（V-021-A，动态结果度量）≠ failure domain（V-005-E，静态分区结构），Stage 4 任何 P-* 不得把二者作 alias。

### H5a — Reversibility

**判定：process rule / decision heuristic，不是结构原则。**

Type 1/2 决策框架（V-013-D，S-010/S-018）约束的是「何时承诺、投入多少分析」的决策流程，不是系统结构本身的因果律。它影响架构行为（可逆决策少做过度设计），但其机制主体在决策过程层。

证据风险：V-021-G expand-contract 目前 NEEDS_EVIDENCE（corpus 无一手出处），RQ3-006 未回流前不得用它支撑 H5a/H8 的任何主张。

### H5b — Change Locality

**判定：大概率是 H7 的投影（→ CF-2），独立原则地位存疑。**

change amplification（V-014-D，S-001/S-005）是「变更成本随距离增长」在 change 维度的实例。若 H7（locality 总族）成立，H5b 应作为其投影并入，避免同一 distance-cost 机制计双份。独立存活的唯一理由：change 维度有独立机制（信息隐藏预测变化方向），S-001 恰好提供了该独立性证据——但这需要 Stage 5 用「data locality 好而 change locality 差」与反向的真实结构反例裁决，不能在 Stage 4 预先裁定。

### H6 — Legibility / Operability / Verifiability

**判定：property，需重述为因果结构主张才可成原则。**

「不可揭示行为的系统无法在所需级别运维/验证」是属性陈述（可观测性 S-055、arc42 S-022 支持）。成原则的重述方向：「结构决定可观测表面的分布——横切关注点的结构放置决定能否按组件归因异常」。注意 S-055 的 Honeycomb 厂商立场已在 corpus 标注；scope 应按运维要求等级限定（plan RQ-A5 的 minimum sufficient description 同族）。

### H7 — Locality

**判定：family hypothesis 成立，但是倾向非定律（scope down），且词汇骨架未决。**

V-014-C 自认 CONTEXT_QUALIFIED「多种机制的共同倾向而非单一机制；Stage 4 需拆分检验」。N-8 禁止与 Herlihy-Wing locality（= 可组合性）互借。RQ3-001 已登记 coupling/change-locality 缺专门权威来源，当前锚 SAIP 谱系（S-005）。

Stage 4 不得把「distance cost 上升」写成 universal monotone law；正确形态是分投影检验：reasoning / data movement / failure propagation / change cost 四投影，各自的机制与反例不同（S-077 tail at scale 是 data/fan-out 维度的量化证据；S-001 是 change 维度）。

### H8 — Compatibility / Contract Preservation

**判定：条件性原则候选——scope 限于有外部消费者/兼容承诺的系统。**

Schema registry（S-044）、Protobuf（S-045）提供工业 normative 机制。词汇红线：V-013-A/B 强制 reader/writer（producer/consumer）视角标注，backward/forward 裸用即 gate violation。在封闭单租户、同仓同部署形态下，兼容性可被部署顺序替代，原则不适用——scope 子句必须显式。

### H9 — Controlled Complexity

**判定：META_OBJECTIVE，且是他者的后果。**

「最小必要复杂度以保护所需属性」是优化目标陈述。economy of mechanism（S-092 Saltzer-Schroeder）是其投影之一；H2a/H3/H4 良好应用的自然后果亦然。复杂度本身在 02_VOCABULARY 无词条（无操作化定义），美学主张风险最高——「简单」不可度量时，该候选最易退化为品味判断。处置：并入 Constitution 的价值排序，不作为独立 P-*；若保留，必须先给复杂度的可判定操作化。

### H10 — Trust Minimization

**判定：机制候选成立；与 H4 共族不同保护属性（→ CF-3）。**

least privilege / complete mediation（S-092）、zero trust（S-093 NIST）提供机制与标准级证据。与 H4 共享深层机制「power-responsibility alignment」，但保护属性不同：H4 保护 availability（故障传播），H10 保护 confidentiality/integrity（越权路径）。plan §7 规则：保护 materially different properties 可作为分立理由，但共族关系必须登记，Stage 5 需给出「一者违反另一者不违反」的结构反例对。

形态边界：S-093 自认以企业 IT 为预设，单进程/本地形态几乎无语料——wide scope 前必须补形态证据。

### H11 — Authoritative State / Source of Truth

**判定：需机制化，否则是词汇/属性。**

「state 应有清晰 authority 与 consistency 语义」若不停留在此抽象层，必须落到机制主张：single writable authority + derived-copy discipline（S-023 DDIA 综述、S-024/S-026 CAP 系、Kafka/DB 语料支撑）。与 H2b 的独立性是 plan 自己登记的 open question：ownership 管实体，authority 管状态裁决权——概念可分，机制上常共生（谁拥有实体常决定谁是权威），Stage 5 反例裁决。

词汇红线（Issue #6 三连）：source of truth / system of record / authoritative state 不自动等价；consistency（V-010）必须带 ACID/CAP/client-visible 限定；atomicity（V-011-E）必须区分 transaction 与 linearizability 历史义；authority（V-003-D）必须带「状态」限定防与 authorization 混淆。

## 2. 坍缩 / 共族图谱

| # | 坍缩假设 | 深层机制 | 判定 | 裁决层 |
|---|---|---|---|---|
| CF-1 | H2b + H3 部分合并 | 显式 scope ownership 给 execution lifetime 一个结构上界（S-084..086） | 部分共享，非全并：H3 的 space/queue/retry 维度不依赖 H2b | Stage 4 可登记，Stage 5 反例定边界 |
| CF-2 | H5b ⊂ H7 | change locality 是 distance-cost 的 change 投影 | 大概率并入；S-001 信息隐藏提供唯一独立性证据 | Stage 5：需「一投影好另一投影差」的双向反例 |
| CF-3 | H4 + H10 共族 | power-responsibility alignment | 共族但保护属性不同（availability vs confidentiality/integrity），暂分立 | Stage 5：一者违反另一者不违反的反例对 |
| CF-4 | H2a 服务于 H7 | boundary 是引入/管理 distance cost 的机制 | H2a 是 H7 的管理手段，非同一原则 | Stage 4 登记从属关系即可 |
| CF-5 | H9 ⊂ H1 | 二者均为 meta-objective | 成立：H9 并入 Constitution 层价值排序 | Stage 4 可直接处置 |

## 3. Principle-vs-not 降级分析

| H | 分类 | 降级目标层 | 理由 |
|---|---|---|---|
| H1 | meta-objective / evaluation frame | Constitution 评判公理 | 无因果结构主张，不可结构证伪 |
| H9 | meta-objective + consequence | Constitution 价值排序（或先操作化复杂度再议） | economy of mechanism 是投影；复杂度无词条无操作化 |
| H5a | process rule / decision heuristic | Decision Playbook（Type 1/2 决策） | 机制主体在决策流程不在系统结构 |
| H6 | property | 重述为「结构决定可观测表面分布」后才可入 P-* | 现表述是属性非因果律 |
| H3 | tactic 清单化风险 | 必须锚 V-021-C unboundedness 抽象 | 清单无歧视力；抽象有反例 discrimination |
| H11 | 需机制化 | single writable authority + derived-copy discipline | 停留词汇层则非原则 |
| H8 | 条件性候选 | scope 限于有外部消费者/兼容承诺系统 | 封闭形态可被部署顺序替代 |
| H2a/H2b/H4/H5b/H7/H10 | family 候选 | 各自带 Stage 5 判别义务 | 机制成立但独立性/普适性未证 |

## 4. 缺失 principle family 候选

H1..H11 未覆盖、corpus 却有证据的家族：

1. **MF-1 idempotency under at-least-once**：V-021-B（S-037/038/043）——分布式交付语义下接收方正确性的前提，机制独立（重复执行等价性），不属于 H3 的 bound 问题也不属于 H11 的 authority 问题。
2. **MF-2 scheduling / priority as correctness**：S-091 Mars Pathfinder 优先级反转（正确性被调度策略破坏）、S-113 FreeRTOS 确定性调度——实时/嵌入形态下 scheduling 是正确性维度，H 列表完全缺席。
3. **MF-3 capacity / queueing 保护**：S-050 constant work、S-072 Little's Law（L=λW 的稳定性前提）——部分可归 H3，但「容量作为一等设计约束」有独立机制（利用率-延迟非线性）。

处置：登记为 evidence-derived 候选，是否进入提取由 Primary 决定，本报告不代为创建 P-*。

## 5. Lineage 非独立性表

| 表面多源组 | 实际 lineage | 宽 scope 计数资格 |
|---|---|---|
| S-084 Smith + S-085 Kotlin + S-086 Swift | Smith 自认承 Sústrik 2016；Kotlin/Swift 是对 Smith 框架的平台采纳 | 1 个独立源族 + 2 个平台背书，不是 3 族 |
| S-057 Reactive Manifesto + S-090 Reactive Streams | 同社区（Reactive SIG / JDK Flow 规范化） | 1 族 |
| S-047 Nygard + S-048 Google SRE + S-050 AWS | 三个真正独立工业 lineage，但全部大规模 web/backend | 3 族但单一形态 |
| S-023 DDIA | 二次综述，引 S-024/S-026 | 不计额外独立证据 |
| S-010/S-011 Fowler + S-018 Ford/Parsons/Kua | ThoughtWorks 轨道（evolvability 族） | 单 shop 偏斜，宽 scope 不足 |

## 6. Backend / distributed / cloud bias 与 cross-shape

偏差分布：H3 证据重 Node/Reactive/gRPC/AWS；H4 重 AWS cell/SRE；H11 重分布式 DB/Kafka/Android。RQ2-014 已记录 backend/distributed 例证占 55-60%。

Cross-shape 锚点（宽 scope 前必须引用的形态）：S-112 Electron（desktop）、S-113 FreeRTOS（embedded）、S-107 local-first（本地优先）、S-098..103（agent runtime）。Issue #9 规则：两个独立源族方可宽 scope；单形态族必须 shape-scoped（如 H10 的 zero trust 限定企业 IT 形态，见 S-093 自认预设）。

## 7. Lexical gate 风险图（Stage 3 → Stage 4 强制）

| 风险点 | 违规形态 | 词条锚 | 级别 |
|---|---|---|---|
| consistency 裸用 | 「系统应保持一致」无限定 | V-010：必须 ACID/CAP/client-visible 后缀 | P0 |
| atomicity 裸用 | transaction 与 linearizability 历史义混用 | V-011-E 强制消歧 | P0 |
| authority 裸用 | 状态权威与 authorization/security authority 混淆 | V-003-D 须带「状态」限定 | P1 |
| blast radius ↔ failure domain alias | 「缩小 failure domain 即缩小 blast radius」 | V-005-E/V-021-A + Issue #6 裁决 | P0 |
| backpressure 裸用 / flow control 等价 | 「flow control 提供了 backpressure」 | V-008-E + Issue #6：不自动相等；全链路才成立 | P0 |
| stateless 裸用 | REST 处方与 LLM-call 语义混用 | V-021-H 强制消歧 | P1 |
| backward/forward compatible 无视角 | 不标 reader/writer（producer/consumer） | V-013-A/B | P1 |
| structured concurrency ↔ virtual threads alias | 「虚拟线程即结构化并发」 | Issue #6 裁决：不是 alias | P0 |
| SoT/SoR/authoritative state 自动等价 | 三词互替不证 | Issue #6 裁决 | P0 |
| unboundedness 未检验直接用 | 把 V-021-C 当已证概念 | PROJECT_DEFINED，Stage 4 须检验解释力 | P1 |
| locality 借 Herlihy-Wing 义 | 可组合性混入距离成本义 | N-8 禁止互借 | P1 |
| resilience / fault tolerance 排序 | 「FT 强于 resilience」 | V-005-C/D + N-13：无全序 | P1 |
| complexity 无操作化 | 「保持简单」作为原则语言 | 02_VOCABULARY 无词条 | P1（美学主张风险） |

## 8. Scope-down 清单

| H | 原 broad 形态 | 收窄后形态 |
|---|---|---|
| H4 | failure power ≤ responsibility（普适） | multi-tenant/高代价/物理共享形态下的 graded economics heuristic；单进程低成本显式豁免 |
| H7 | distance cost 单调上升（定律） | 分投影（reasoning/data/failure/change）的倾向 + 各自反例域 |
| H8 | 兼容性一等属性（普适） | 有外部消费者/兼容承诺的系统；封闭同部署形态豁免 |
| H6 | 不可观测即不可运维（普适） | 按运维要求等级限定；「所需级别」进前提 |
| H5a | 可逆性影响决策（普适） | Type 1/2 决策语境的 process rule |
| H1 floors | safety/security 非协商地板 | 仅 "in applicable contexts"（保留原文限定） |
| H10 | 零信任普适 | 企业 IT/多租户形态优先；单进程/本地 NEEDS_EVIDENCE |

## 9. BACKFLOW_TRIGGER 候选（对应 review-queue RQ3）

| RQ3 | 触发条件 | 涉及 H |
|---|---|---|
| RQ3-001 | coupling/change-locality 专门权威来源未补，H5b/H7 却被 promotion | H5b, H7 |
| RQ3-002 | H2b 主张 Java/平台特化 realization 而无平台一手证据 | H2b |
| RQ3-003 | 任何「风格/范式收益」（reactive、微服务）进入原则语言 | H3 及全部 |
| RQ3-004 | H10 需要 capability/零信任平台实例支撑宽 scope | H10 |
| RQ3-005 | H3 主张 browser/UI 形态而证据全在 server 端 | H3 |
| RQ3-006 | expand-contract（V-021-G NEEDS_EVIDENCE）被用作 H5a/H8 证据 | H5a, H8 |

## 10. Genuine owner decisions

1. **H1 与 H9 的层归属**：二者并入 Constitution 层（评判公理 + 价值排序）还是保留 principle 候选——影响最终 P-* 数量与 Constitution 结构，属架构治理决定。
2. **H5a 的降级处置**：接受降为 Decision Playbook（process rule），还是坚持其结构侧面并要求 Stage 5 反例——决定 playbook 层的输入。
3. **是否接受 evidence-derived 新候选**：MF-1（幂等）、MF-2（调度正确性）、MF-3（容量保护）超出原 H 列表；plan 允许新增（"Additional hypotheses may be introduced by evidence"），但提取资源分配是 owner 决定。
4. **H4+H10 共族登记**：接受「共族分立、Stage 5 反例定界」的处理，还是提前合并——影响 Stage 5 反例设计预算。

## 11. Preregistered checks（Pass B 对 Kimi fixed-SHA 产物的对账清单）

| ID | 检查 | 判定 |
|---|---|---|
| V4-01 | H1..H11 每项有显式 disposition（保留/合并/降级/拆分）+ 机制理由 | PASS/FAIL |
| V4-02 | 降级项标注目标层（Constitution/Playbook/Tactic/Property），未静默丢弃 | PASS/FAIL |
| V4-03 | CF-1..CF-5 每项被采纳（带证据）或拒绝（带理由） | PASS/FAIL |
| V4-04 | 合并/拆分对满足 plan §7：credible cases 一者违反另一者不违反，或保护属性实质不同 | PASS/FAIL |
| V4-05 | MF-1..MF-3 被显式接受为新候选或拒绝，无静默缺口 | PASS/FAIL |
| V4-06 | lineage 非独立性诚实呈报：Smith/Kotlin/Swift 不计 3 族；ThoughtWorks 轨道标注 | PASS/FAIL |
| V4-07 | 宽 scope 仅在 ≥2 独立源族时授予；单族/单形态 shape-scoped | PASS/FAIL |
| V4-08 | backend/distributed/cloud 偏差被量化或承认；cross-shape 表（desktop/embedded/local-first/agent）在场 | PASS/FAIL |
| V4-09 | §7 全部 P0/P1 词汇带限定与 V-ref；consistency/atomicity/authority/backward-compatible/stateless 裸用即 FAIL | PASS/FAIL |
| V4-10 | blast radius 未 alias failure domain（Issue #6） | PASS/FAIL |
| V4-11 | 无 structured concurrency ↔ virtual threads alias（Issue #6） | PASS/FAIL |
| V4-12 | SoT/SoR/authoritative state 未自动等价（Issue #6） | PASS/FAIL |
| V4-13 | flow control 未自动等价 backpressure（Issue #6） | PASS/FAIL |
| V4-14 | H3 锚定 unboundedness 抽象（V-021-C）并检验其解释力，非 timeout/retry tactic 清单 | PASS/FAIL |
| V4-15 | H7 未借 Herlihy-Wing locality（N-8）；V-014-C 骨架被拆分检验或标记未决 | PASS/FAIL |
| V4-16 | 每候选有 counterexample plan（≥1 serious search，relevant 时 ≥2 shapes，plan §7） | PASS/FAIL |
| V4-17 | 每候选 mechanism 与 tactic 分离，pattern/framework 名未作为原则 | PASS/FAIL |
| V4-18 | RQ3-001..006 未被静默填充；backflow 政策被遵守 | PASS/FAIL |
| V4-19 | 无 junk P-*（凑数候选）；每个 P-* 对应真实机制假设 | PASS/FAIL |
| V4-20 | 每候选 vocabulary_refs 填充至 02_VOCABULARY 词条 | PASS/FAIL |
| V4-21 | §8 scope-down 清单被采纳或逐条给出拒绝理由 | PASS/FAIL |
| V4-22 | expand-contract（V-021-G NEEDS_EVIDENCE）未在 RQ3-006 回流前被用作证据 | PASS/FAIL |
| V4-23 | 每候选含 protects / mechanism / scope / trade-offs / evidence / counterexample plan 六要素（Issue #9） | PASS/FAIL |
| V4-24 | 无 Stage 5 走私：反例战役未提前执行，判别项登记为 Stage 5 任务 | PASS/FAIL |

## 12. 元声明

- 本报告为盲审 Pass A：未读 Kimi Stage 4 输出，未创建竞争 P-* set，未执行 Stage 5 反例，未修改 canonical evidence/vocabulary。
- 所有判定是 challenger 立场的边界分析，非 promotion 决定；最终去留由 Primary 提取 + Pass B 对账（V4-01..V4-24）+ Chief Architect gate 裁定。
- 本报告自身不引用任何 research/stage4-principles 分支内容；引证仅来自 baseline d6a7808 上的 canonical 文件与已 seal 的 sources/。
