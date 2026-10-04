# Stage 10 Phase D Defect Diagnosis

日期：2026-10-04（Asia/Shanghai）

状态：**SCORED_PENDING_ADJUDICATION**。32 案已评分，434/538（80.67%），16 项 HF 涉及 16 案；22 案需裁定。

## 1. 诊断边界与证据

- canonical evidence：`d6ac48c16f7285f53fbc7af6e5aae4f64f83123b`
- suite-design：`ff157eb1947860345a305fb29452b51e09dd3a2b`
- frozen SUT：`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- runtime freeze：`7db2639044d3a8f0b8706d70161513238ed29670`
- run_id：`phasec-20260930T101227Z-7db26390`
- 实例：Agent v0.1 / company compute gateway / `glm-5.3` / 冻结 Stage 10 Harness。

下列严重度表示后续修复优先级；逐案 finding disposition、HF taxonomy、分值仍以 `eval/stage10/scoring/case-scores.yaml` 为准。文中的最小修复均为待验证建议，本轮未实施，也未运行任何 E10、synthetic 或模型请求。

证据来自对应 PUBLIC、canonical raw 和冻结 oracle/rubric。`raw E10-xxx:Lm-Ln` 指 `eval/stage10/run/raw/E10-xxx.md` 的原始行号。冻结 SUT 的 system prompt、AUTO、DP-002、DP-004 仅用于判断已有规则与输出的落差，不替代 raw 中缺失的内容。

现有 system prompt 已要求项目事实的 origin/claim_state、产品 authority、六柱 BLOCKER、最小修正与 typed terminal；AUTO 已要求单一 DP 和显式 overlay。因而观察到的违反不能直接证明规则缺失，更不能据此认定 KB 或模型供应商是根因。没有通过修复实验隔离任何层的因果责任。

## 2. 优先级一：EVIDENCE_DISCIPLINE

**受影响案例**：HF-03 的 E10-005、006、007、009、011、012、019、022、028、029、030、031；HF-10 的 E10-018、021。另有 D3=1 的 004、008、010、014、015、016、017、018、020、021、024、027、032，属于证据状态或推断边界缺口，不能一律扩大成 HF。

**证据**：

| 例 | 可见输出与输入的落差 | 定位 |
|---|---|---|
| 011 | 同一输出将 PUBLIC 的三次 attempt 推成最多四个 request/×4 | raw L12；PUBLIC 的 retry count |
| 012 | 一次观测的两小时故障窗口被扩写成每日两小时 | raw L77 |
| 022 | 将未给出的短事务、数据量及容量余量写成当前方案依据 | raw L23 |
| 028 | duplicate rate UNKNOWN 被解释成项目没有 instrumentation | raw L12、L61 |
| 029 | 聚合的 lag/disk spike 被补成 lag 先于 94% disk 的时间顺序 | raw L9 |
| 030 | 没有同步 downstream dependent 被扩大成没有同步 incoming work dispatch | raw L14 |
| 031 | 人工 on-call rollback 被补成已有按 checkout SLO 触发的自动回滚 | raw L46 |
| 018 | 共享 schema 被确定地推成 pricing 决策仍然共享，实际表触碰与变更 ripple 未给出 | raw L31 |
| 021 | 1% head sampling 与 0.4% error 被直接推成不能捕获错误，缺少请求基数及 sampler 机制 | raw L43 |

其余 HF-03 的逐字证据和冻结 basis 见 case-scores；例如 005 的未使用 deprecation history 被扩成从未有 version contract，007 无大小证据即断言可放入 128KB，019 无计量即断言 DM 成本 trivial。

**可能机制**：在机制方向基本正确时，补写默认运行条件、数量、时间先后或已有能力，以支撑完整的叙述；把“未知值”“缺失材料”“未来建议”投射成当前项目事实。主结论保留 UNKNOWN，也未必约束后续局部句子的确定性。

**严重度与分布**：HIGH；具有系统性。D3 为 27/64，25/32 案低于 2；12 项 HF-03 和 2 项 HF-10 出现在多个 DP。这个分布足以说明重复的输出行为，不能隔离 prompt adherence、上下文消费与模型推断各自的贡献。

**最小可能修复**：在现有 origin/claim_state 要求中增加一次简短的 load-bearing claim 核对：数字/时间/基数有对应来源；“已有”“没有”“从不”等项目事实有明确证据；推断与未来方案保留条件状态。对采样、容量及因果判断，先写缺失的基数、单位或辨别观测，避免把知识中的一般规律当成已测项目数据。无需新增完整知识库或增加泛化长篇回答。

**过拟合风险**：低至中。以通用事实类型和证据状态约束实现较稳健；禁止把案例 ID、三次 retry、128KB 等答案常量写进 Agent。

**置信度**：输出缺陷 HIGH；上述根因及修复有效性 MEDIUM，HF 结论仍待裁定。

## 3. 优先级二：OUTPUT_CONTRACT

**受影响案例**：全局 terminal 错误的 E10-010、013、018；finding 与终态边界不一致的 004、012、021、022、024、028。010/018 的解释边界同时属于第 9 节。

**证据**：

- 010 的 raw L40-L63 指向 ADR 补证据及 owner 决定，实际全局终态为 `MIN_SAFE_FIX_IDENTIFIED`；冻结允许集合为 `OWNER_TRADE_OFF` 或 `NEEDS_EVIDENCE`。
- 018 的 raw L43-L48 同样以 decision rework 收敛为 `MIN_SAFE_FIX_IDENTIFIED`，仍有 pricing ripple 的决定性缺证据及 viable alternatives。
- 013 已否定 consultant 的 blanket BLOCKER，却在 raw L40-L51 重新引入没有本案依据的认证要求查询，将应有的 `NO_DEFECT` 改为 `NEEDS_EVIDENCE` 并继续工作。
- 004 的 raw L72-L73 将未定义的一致性契约直接当成已发生的实质 P1 削弱。checkout 权威校验是否保护产品保证仍未知。HF-01 针对缺少支持的 material-impact 柱，未按措辞或单纯文档缺失触发。
- 012/021 的全局 `NEEDS_EVIDENCE` 正确；局部 BLOCKER 与证据保留、低置信度仍不完全相容。028 的 raw L29-L31 允许限缩合并，末尾又将 delta 标为 BLOCKER，部分修复边界不稳定。

**可能机制**：把“存在一个局部可做动作”当成已经完成决策；finding、severity、terminal 各自生成后未统一核对。对 NO_DEFECT 的停止点，又可能从通用谨慎规则引入额外证据门槛。

**严重度与分布**：HIGH；跨 ADR、review、incident 的重复行为。全局终态 29/32 正确，与 D9 的 51/64、局部 disposition 完整性是不同指标。

**最小可能修复**：在既有 typed terminal 输出前核对当前决策是否仍由 owner 取舍或决定性证据阻塞；补写 ADR 不自动解除这些停止条件。将 finding disposition 与全局终态分别验证。确认合规或 refutation 后，只有当前 case 存在新的 load-bearing 要求才继续索证。BLOCKER 六柱需有实质支撑，不能仅填满字段。

**过拟合风险**：中。通用停止条件与 authority 状态可复用；针对三案硬编码 terminal，或看见错误输出后放宽冻结 terminal 集合，会严重过拟合。

**置信度**：实际 terminal 不匹配 HIGH；协议生成的根因 MEDIUM；004 严重度及 ADR 解释边界 MEDIUM，已标记裁定。

## 4. 优先级三：REASONING_PLAYBOOK

**受影响案例**：D6=1 的 E10-001、007、011、015、016、019、027、028、031、032；相关机制边界还见 008、020、022、024。此列表是诊断归类，不改变冻结 coverage 分组。

**证据**：

| 例 | 最小修正的缺口 | 定位 |
|---|---|---|
| 001 | 接受 bounded-interval 落盘并仍保证强杀 never lost edits；未定义持久确认边界 | raw L35，HF-05，D7=0 |
| 007 | 未测 payload 大小便宣称新 packet 可落入 128KB；修复容量保证不闭合 | raw L24 |
| 011 | retry 请求数量计算错误，削弱 bounded retry 对成本/尾延迟的分析 | raw L12 |
| 015 | `(order, payment_intent)` 唯一键及 per-intent 保证不必然实现每 order 一次 charge | raw L17-L20 |
| 016 | 各阶段“切回旧代码/toggle”未覆盖已删除列或旧写入的兼容恢复 | raw 的 migration/rollback 方案 |
| 019 | DM 成本被称 trivial，未建立保留窗口、计量及成本上限 | raw L26 |
| 027 | 切 SELECT-only 路径后，旧共享 RW credential 的撤销/轮换完成条件未明 | raw L16-L19、L44 |
| 028 | optional key 不能单独覆盖 unkeyed mobile；业务字段时间窗尚未证明等同真实提交意图 | raw L23-L27 |
| 031 | pool floor 用 concurrency×hold time，单位及容量关系不成立；queue governance 仍偏弱 | raw L11-L17、L46-L47 |
| 032 | root-cause repair 被推为 follow-up，quarantine/mark 对失败信号和回归门禁的含义未说明 | raw L27-L33 |

008 的 clock-skew/merge 推断、020 的 replica 拓扑、022 的 brief maintenance 与 node-loss outage 边界，也体现“正确修复方向”与“已证明后置条件”之间的差距。032 未明确说明丢弃测试，故不凭 quarantine 一词新增 HF-05。

**可能机制**：最小修正以组件、动作或 API 名称闭合，遗漏 accepted property 的前提、边界、数值单位或 rollout 阶段。已有的 generic min-correction 规则不足以保证每个具体方案都写出产品后置条件。

**严重度与分布**：HIGH；系统性边界问题，001 已触发产品能力削弱 HF-05。D6 48/58，说明多数方向正确，缺陷集中在“为什么该局部动作足够”。

**最小可能修复**：为最小修正增加一个简短的 property-preservation check：被保证对象、确认/ack 时点、key 基数、窗口语义、容量单位、回滚阶段及质量 gate。只检查当前方案所需项；无法建立充分性时指出具体 discriminator 或 owner 决策，不默认请求整体重构。

**过拟合风险**：中。通用前提/后置条件校验可复用；固定选择 SQLite、某种 key 或某种 CI 隔离方案会过拟合。015/028 必须保留对项目真实 cardinality/intent 的取证，不能由 scorer 补事实。

**置信度**：可见方案缺口 HIGH；具体语义争议与层级归因 MEDIUM，015/027/028/032 已标记裁定。

## 5. AGENT_PROMPT / MODE_ROUTING

**受影响案例**：E10-002、006、008、010、011、015、016、022、028、031、032，即 11 个 D1=1 案例。

**证据**：primary DP/mode 32/32 可接受，但 raw route declaration 未完全反映必要 overlays。例如 015 的 raw L1 没有 integration，028 的 raw L1 仅 state/data，031 的 raw L1-L13 缺 overload/policy，032 的 raw L3 将 resources/evolution 写成 resources/overload。006 的资源形式不能替代 ownership，008/022 的“none”也没有完整反映分析对象。

**可能机制**：正文分析和 route line 是两个投影；用载体/资源词替代实际机制家族，或把正文使用的第二 domain 当作已显式声明的 overlay。routing/tool metadata 不能补答复中的缺项。

**严重度与分布**：MEDIUM；系统性声明缺口。完整 D1=2 为 21/32；没有据此认定 11 案选择了错误主 DP，也没有触发 HF-06。

**最小可能修复**：保持单一 primary，在输出时将已经实际启用的机制家族核对到 route line，并简述 basis；不扩展为所有 domain 巡检。现有 AUTO 合同已有此要求，建议是一次短一致性检查。

**过拟合风险**：低至中。应按真实机制生成 overlays，不按“payment”“SQLite”等关键词固定映射，更不能写入 E10 routing 答案表。

**置信度**：缺失声明 HIGH；生成机制 MEDIUM。

## 6. KNOWLEDGE_RETRIEVAL / ROUTER

**受影响案例**：本轮没有独立定位到该层的缺陷案例；第 5 节的 route line 错误不能直接当成检索路由故障。

**证据与可能机制**：raw 中存在知识标识和 playbook 引用，但引用不证明所有决定性知识已消费；错误断言也不证明缺少检索。评分不使用 hidden reasoning、tool metadata 去补正文，且本轮无 retrieval 消融或复跑，因而未建立该层的因果证据。

**严重度与分布**：UNDETERMINED；不能判定系统性或孤立性。

**最小可能修复**：无已定位、可直接建议的 router 改动。未来若另行授权，应先验证实际加载的必要知识与输出使用情况，再决定是否做局部检索修复。

**过拟合风险**：高。仅凭案例失败追加硬编码检索规则，容易把正文事实纪律问题伪装成知识覆盖问题。

**置信度**：归因 LOW；当前证据不足这一限制 HIGH。

## 7. KNOWLEDGE_CONTENT / RELATIONSHIP MAP

**受影响案例**：没有独立确认某条冻结 KB 或 relationship map 错误导致这些输出。

**证据与可能机制**：多数输出正确识别 property、局部机制、GC 与可接受 primary route；错误集中在给定证据之外的项目事实和修复保证。已读 system prompt/DP 对 authority、stop condition 与 origin/state 有对应要求，但这不构成全 KB 内容正确的审计。

**严重度与分布**：UNDETERMINED；不能从 32 案答复独立区分内容缺陷、关系选择缺陷或规则未被执行。

**最小可能修复**：无已定位的内容修复。后续若发现具体知识规则与真实机制冲突，按单条规则及关系边界修复；目前不建议批量扩写 KB 或重做 relationship map。

**过拟合风险**：高。将 oracle 的具体项目事实抄成 KB 规则，会污染后续盲测并弱化通用机制约束。

**置信度**：内容归因 LOW；不作无证据 KB 归因的判断 HIGH。

## 8. MODEL_BEHAVIOR / UNCERTAIN

**受影响案例**：第 2–5 节已经指出可见行为及更具体的合同/机制问题；没有剩余案例能独立定位为 provider 或模型专属故障。

**证据与可能机制**：本次只有 Agent v0.1 在 `glm-5.3` 与冻结 Harness 下的一次 complete run。没有跨模型对照或重复采样，不能分离实例行为、Agent 规则执行、上下文消费及模型本身的贡献。不能因答错就归咎模型，也不能把技术运行 COMPLETE 当成质量 PASS。

**严重度与分布**：UNDETERMINED；通用模型能力、模型间优劣和长期稳定性均未评估。

**最小可能修复**：没有证据支持更换模型、增加 fallback 或修改 measured 配置。本轮只保留上述无法隔离的归因限制。

**过拟合风险**：高。依据一个固定小套题换模型或追分，可能改变评估对象而掩盖 Agent 的具体合同问题。

**置信度**：模型专属归因 LOW；适用范围限制 HIGH。

## 9. EVAL_CASE / ORACLE_AMBIGUITY

**受影响案例与边界**：

| 案例 | 需裁定的解释边界 |
|---|---|
| 004 | 文档/一致性缺失的实质 P1 影响，在 checkout 权威校验未知时是否足以支撑 MUST_FIX；当前按 HF-01 记录 |
| 010、018 | generic DP-004 允许部分 decision rework 使用 MIN_SAFE_FIX；本案仍有 owner/decisive-evidence 停止条件，冻结 oracle 集合更具体；当前终态按 FAIL |
| 015 | payment_intent 与 order 的基数关系是否使所提 key 保住 accepted 每 order 保证 |
| 020 | 所提 replica 方案实际是否独立于 shared lock/相关资源边界 |
| 022 | brief maintenance 容忍不能自动覆盖未定时长的 node-loss outage |
| 024 | ADR_REVIEW/DP-004 是冻结允许的 alternate，已计路由正确；fixed-capacity 冲突被条件化与 owner freeze 的处理仍有语义争议 |
| 027 | raw L16-L19、L44、L51 的 “the migration ticket” 特指模板迁移依赖，不能直接扩大为豁免全部审批；执行依赖边界仍不清 |
| 028 | 局部 UI 修复允许合并与 delta BLOCKER 的边界、optional key/时间窗的充分性 |
| 032 | quarantine/mark 的失败保留、回归 gate 与已知 order dependency 修复时序 |

**证据与可能机制**：部分 PUBLIC 未指定实现基数、复制拓扑、流程票据或 CI gate 的具体语义；通用 playbook 与 case-specific 停止条件也可能被混读。真正的材料缺口与 Agent 自行增加假设必须区分。所有 HF 强制裁定，并不等于所有 HF 案例的 oracle 存在歧义。

**严重度与分布**：MEDIUM；属于裁定边界，不能据此宣布整套 oracle 有系统性缺陷。当前 22 个 adjudication_required 保持，包括全部 HF、024 alternate 及上述实质解释争议。

**最小可能修复**：当前由人工在冻结规则与原字节证据上裁定，保留理由。若未来设计需要补充 cardinality、gate、authority stop 的明确说明，须形成新的 design freeze；不能在本轮看过分数后重解释或放宽 oracle。

**过拟合风险**：高。用 observed answer 反向改 expected outcome/HF 阈值会破坏盲评；当前没有实施这种变更。

**置信度**：存在解释边界 MEDIUM；当前 expected 集合及 HF taxonomy 未修改 HIGH。

## 10. 校准记录、优点与后续最小范围

统一复核将 004/005/031 的 D5 改为 N/A：不存在本维度要求的实际合规非报警组件，列出 GC 检查本身不获分。027 初评的 HF-03 因模板迁移上下文不足以支撑“既成项目事实”触发而撤销，D3=1、继续裁定。校准是应用既定规则，未更改 oracle、HF 定义或 measured evidence。

三个已体现的能力是：对象到 primary DP 的路由（32/32 含合法 alternate）；accepted property 理解（D2 61/64）；冻结 strict GOOD CASE 的指定非报警组件识别（8/8，material false positive=0）。这些优点与 HF 并存，不能抵消它们。

后续最小修复顺序建议为事实/证据状态核对、terminal/stop 一致性、修复后置条件，最后补 route declaration 一致性。任何后续验证都应先单独授权和冻结新的实现，并以新材料检验一般机制；不能修改本次 raw 或重新运行案例来替换成绩。本轮到评分提交停止。
