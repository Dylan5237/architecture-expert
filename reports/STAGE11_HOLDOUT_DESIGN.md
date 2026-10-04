# Stage 11A Holdout Design and Freeze

日期：2026-10-04（Asia/Shanghai）

状态：**FROZEN / DESIGN ONLY**。12 个全新案例及比较门槛随本次 Git 提交冻结；未实现 Agent v0.2，未执行任何 holdout 或其他被测模型调用。

本报告为设计者/评分者材料，不属于 runner payload，修复执行者不得读取。

## 1. 来源与授权

- 分支：`eval/stage11-holdout-design`，专用独立 worktree。
- 起点及 Chief Architect adjudication：`1621916b4f0bef8c5ceb7f43b30ca473416dea03`。
- 任务：`b62a10e7cb364cfa27105a5b935caa9639b55bf4:tasks/stage11/CODEX_STAGE11_HOLDOUT_DESIGN.md`，从更新后的 `origin/main` 直接读取；未合并 main。
- Agent v0.1 SUT：`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`。
- Stage 10 evidence：`d6ac48c16f7285f53fbc7af6e5aae4f64f83123b`。
- Stage 10 scorer：`c32adbdac7f4a74077d2ec3235e8feb76aadc0ce`。
- 冻结 rubric：`ff157eb1947860345a305fb29452b51e09dd3a2b:eval/stage10/design/rubric.md`。

已读仓库 AGENTS.md、TASK.md 和 TASK 引用的 Issue #24。该 issue 已 CLOSED 且属于 Stage 9；本轮按当前用户明确授权和指定 Stage 11 任务执行。原有 Stage 10 材料只用于识别排除场景与既定语义，未改动。

## 2. 交付结构

新增且仅新增 16 个文件：

- `eval/stage11/holdout/design/manifest.yaml`：输入 provenance、case list、payload SHA256、pass criteria、blindness/isolation。
- `eval/stage11/holdout/design/public/H11-001.md` .. `H11-012.md`：12 个 runner-facing 案例。
- `eval/stage11/holdout/design/private/oracle.yaml`：12 个私有预期条目。
- `eval/stage11/holdout/design/private/coverage.yaml`：互斥主类别与正交覆盖标签。
- `reports/STAGE11_HOLDOUT_DESIGN.md`：本报告。

PUBLIC 使用同类字段的普通 YAML 文本：id、neutral title、task_object、requested_mode、user_request、project_evidence、constraints、notes_for_runner。没有额外预期答案正文。每条私有 oracle 均包含任务要求的 route、alternate、overlays、properties、mechanisms、refs、find/non-find、dispositions、terminals、minimum correction、uncertainty、authority、HF triggers、ambiguity 和 scoring notes。

rubric 未复制，直接引用冻结 SHA 与文件 SHA256。保留 D1..D10、HF-01..12、typed terminal、route/DP、GOOD CASE、authority/evidence 语义；未新增评分维度、严重度 taxonomy 或 anchor。每案 HF 条件是将既定定义应用到可能输出的例子，未列出的 HF 仍适用。不存在预测成绩或预置被测输出。

## 3. 十二案覆盖

以下内容只供设计/评分，禁止提供给被测版本或修复执行者。

| Case | 主类别 | Preferred mode / DP | Shape | GOOD 标签 | 显式不确定性 | Authority stress |
|---|---|---|---|---|---|---|
| H11-001 | H-EVIDENCE | ARCH_DESIGN / DP-001 | batch/ML platform | — | 是 | — |
| H11-002 | H-EVIDENCE | INCIDENT_ANALYSIS / DP-005 | edge/IoT | — | 是 | — |
| H11-003 | H-EVIDENCE | CHANGE_REVIEW / DP-003 | desktop/local | — | 是 | — |
| H11-004 | H-EVIDENCE | INCIDENT_ANALYSIS / DP-005 | data pipeline | — | 是 | — |
| H11-005 | H-TERMINAL | ADR_REVIEW / DP-004 | backend | — | — | 是 |
| H11-006 | H-TERMINAL | CHANGE_REVIEW / DP-003 | embedded | partial | 是 | 是 |
| H11-007 | H-GUARANTEE | ARCH_REVIEW / DP-002 | mobile/backend | partial | — | 是 |
| H11-008 | H-GUARANTEE | CHANGE_REVIEW / DP-003 | developer tooling | — | 是 | 是 |
| H11-009 | H-GOODCASE | ARCH_REVIEW / DP-002 | desktop/local | strict | — | — |
| H11-010 | H-GOODCASE | ARCH_REVIEW / DP-002 | public API/integration | strict | — | — |
| H11-011 | H-ROUTING | CHANGE_REVIEW / DP-003 | distributed workflow | strict | 对象歧义 | 是 |
| H11-012 | H-CROSS | CHANGE_REVIEW / DP-003 | public API/integration | — | — | 是 |

主类别恰为 H-EVIDENCE=4、H-TERMINAL=2、H-GUARANTEE=2、H-GOODCASE=2、H-ROUTING=1、H-CROSS=1。标签允许交叉，不把交叉标签另算案例。

Preferred mode/DP：ARCH_DESIGN/DP-001=1；ARCH_REVIEW/DP-002=3；CHANGE_REVIEW/DP-003=5；ADR_REVIEW/DP-004=1；INCIDENT_ANALYSIS/DP-005=2。H11-011 明确允许 ADR_REVIEW/DP-004 alternate，须提供真实对象依据，不能执行两条 primary procedure。其终态按 route 判断：DP-003 无缺陷 delta review 为 NO_DEFECT；合格 DP-004 decision acceptance 允许 NO_DECISION_CHANGING_WORK，也保留有 global stop 依据的 NO_DEFECT 及有合理 decision-level accept-with-conditions 依据的 MIN_SAFE_FIX_IDENTIFIED。不能脱离 route/条件只使用预期集合的并集。

系统形态 10 种：backend、batch/ML platform、data pipeline、desktop/local、developer tooling、distributed workflow、edge/IoT、embedded、mobile/backend、public API/integration。形态来自实际执行/部署/交互边界，不按行业名增加计数。

GOOD/non-alarm=5：006/007 partial、009/010/011 strict。strict 组三案的指定合规组件进入 pass criterion 5；partial 组件仍受 D5/HF-02 保护，但不在 strict 指标中临时改组。006 的 board check 已由题内测试证明有效，不因此证明整个 interrupted-boot qualification 合格。

显式不确定性=6：001/002/003/004/006/008。对象/route ambiguity 另有 011，因此 coverage ambiguity 总数为 7。authority stress=6：005/006/007/008/011/012；该标签用于指定压力面，不替代逐案 D7 适用性判断。

## 4. 判别点与难度

- H-EVIDENCE 分别测试利用率不足以投影未测 workload 的容量、多源时间语义不能拼接因果、未提供 helper 不等于不存在、可复现契约缺陷与生产 lineage 未知并存。覆盖 design、incident 和 change-review；004 仍要求有界肯定 finding。
- H-TERMINAL 的 005 是两个已合规选项的真实 owner preference；006 的局部 board check 可用，但不证明整项安装资格，终态须留在 NEEDS_EVIDENCE。
- H-GUARANTEE 区分新链接授权与已发 bearer 链接、compiler identity 与独立 SDK/plugin 输入关系；最小修正必须证明覆盖或采用已授权的保守 fallback。
- H-GOODCASE 的 009 依赖已给出的同步不可重入执行片段，010 依赖不可变内容与 view revision 绑定。名称或一般平台偏见不能替代 qualifier。
- H-ROUTING 同时给出已接受 decision 与未合并 rollout delta，两种 primary 对象确实可辩护。组件协调及安全治理不能按变更广度误报。
- H-CROSS 的 012 将 accepted review/全格式 capability、异步完成顺序与独立 adapter/recipient contract 结合；已存在 parent owner，缺口是 publication order，而不是孤儿任务。

012 的充分修复条件是全部 included components 已审、验证绑定实际对外 bytes/版本、不能再暴露未审内容。不可变 snapshot 是可接受实现之一；满足同一 complete-review gate 的安全更新也可接受，不新增“所有 artifact 永不改变”的产品属性。

每案包含代码/配置/测试或明确 intent 足以建立有界判断，以及至少一个无效但诱人的推断。没有为评分答案补外部领域事实，不依赖算法、协议冷知识或 exact wording。没有为追求 unknown 而抹掉已有决定性证据，也不把局部动作等同整个决策完成。

## 5. 新颖性自审

完整对照 32 个 Stage 10 PUBLIC。按被审对象、决定性事实关系、已知/未知边界、受保护契约及局部纠正/停止点判断，不用 MP/FP 重叠当重复，也不用换行业名当新颖性证据。

新案未复制 Stage 10 的标题、数字常量、场景证据或特定答案链。PUBLIC 中的新增项目数值为 17 个 pilot collections、61% pilot GPU busy 和 147 个 dark frames；都来自本轮新合成项目证据，未继承旧案参数。编号、版本标签和冻结门槛是控制数据，不是场景事实。

案例中的 CODE/TEST/RUNTIME 是合成项目包给定的证据，不代表真实业务系统，也不表示本轮执行了这些测试。设计期的实际验证仅检查文档、引用、覆盖、隔离规则与 Git 完整性。

重点边界：002 有多源时间语义和不能比较的 capture/upload/deployment 关系；004 有明确单位转换 fixture，但生产 profile/build lineage 未给出；011 有 signer epoch 的 reader/writer、参与者 admission、ack/drain/rollback 关系及两个真实 review 对象。它们不是笼统遥测缺失或只改变停机许可的旧案改写。

独立审查使用主 Agent 调用所指定的 `gpt-6-astra/high` 配置，读取全部 32 个旧 PUBLIC 和本轮确切新文件，主 Agent 负责修正与最终核验。子 Agent 没有独立读取后端身份的接口；这里记录委派参数，不声称独立证明服务端模型身份。审查 scratch 留在仓库外，不供 runner/repair executor 阅读。

冻结前落实四项局部修正：011 的 route-conditioned terminal 与 implied status quo；012 去除强制不可变实现；006 增加已证实局部 guard 的 D5/partial 标签；manifest 将运行前输出合同登记与运行后实际 raw 固定分开。案例主配额、PUBLIC 场景及数值门槛未因此更改。

## 6. PUBLIC leakage 审查

PUBLIC 仅含正常任务对象、项目证据和约束。检查内容包括：

- 无 MP/FP/T/GC/Q/RQ/AX/HF/DP 等知识/评分标识、H 类别或其他 oracle ID；H11 case id 是必需的公开 identity。
- 无私有 oracle/coverage 引用、must_find/scoring fields、评分数字、typed terminal 提示或候选机制注册名。
- user assertion 可以提出错误指控；已给代码/配置/测试可以直接暴露具体行为。这些是问题证据，不是加入的预期 verdict。
- constraints 限定实际能力、环境或 scope；不把缺省 epistemic guard 或标准答案写入 runner instruction。

词法扫描与人工语义审查同时执行；仅有 regex 命中数不能证明无泄漏。未把设计报告或 manifest 作为普通 PUBLIC payload。

## 7. 冻结 Stage 11 pass criteria

在同一 sealed 12 案上运行 v0.1 与 v0.2，并在两个 canonical run 固定后解封评分。v0.1 的比较基线来自本 holdout，不使用 Stage 10 的 42.19% 或 80.67% 充当基线。以下条件须全部满足：

1. v0.2 的 D3 percentage 比 holdout v0.1 提高至少 **20 percentage points**。
2. HF-03 数量相对 v0.1 至少减少 **50%**；整数判断为 `2*N03(v0.2) <= N03(v0.1)`。
3. 相比 v0.1，v0.2 不得新增 HF-02、HF-05、HF-06、HF-07、HF-09。
4. v0.2 primary-route acceptance 不低于 v0.1。
5. strict GOOD CASE material false-positive count 不高于 v0.1。
6. overall applicable-point percentage 不低于 v0.1。
7. v0.2 没有任何案例揭示 unavailable holdout/private-eval knowledge；任一 HF-11 均使此项失败。

任务原文例外原样保留：若 v0.1 HF-03=0，则 v0.2 HF-03 也必须为 0，D3 的 +20pp 条件仍适用。仅当 **v0.1 HF-03=0 且 D3>=90%** 时，D3 改为最多回退 **2pp**。没有其他 ceiling exception；若实际基线使 +20pp 不可达，也不得在看到结果后放宽门槛。

计算与审计约定：

- D3 对 12 案永不 N/A，满分 24；使用精确点数/分数比较，显示 rounding 不影响 gate。
- HF count 以 distinct `(case_id, code)` 登记；同案同码多条证据不人为增加计数。所有触发条件仍按完整冻结 HF 定义审查。
- “无新增”按 protected code 的 case/code 集合比较：v0.2 集合必须为 v0.1 子集。把缺陷移到新案例而保住总数仍不通过。
- primary acceptance 允许冻结 alternate 且要求对象依据；overlay 质量仍在 D1 单独评分。
- strict GOOD CASE 固定为 009/010/011 的指定组件。标签及分母不得在看过输出后改动。
- overall 使用 earned/applicable max，N/A 按冻结 rubric；HF 仅 cap 受影响维度，不自动整案归零。
- incomplete、受污染或提前解封的 run 不构成可比较 gate 结果。保留证据并停止；本设计不授权补跑或替换 Attempt。

## 8. Blindness / isolation 与冻结身份

修复执行者不得读取本分支、任何 holdout PUBLIC/private、manifest 或本报告。设计者/审查者已经接触私有预期，不得以这段上下文承担后续 v0.2 repair。两个 runner 仅能访问各自冻结候选 SUT 与当前 PUBLIC case；不得访问 oracle、coverage、rubric、完整 manifest、报告或 designer scratch。

controller 可以从 manifest 生成只有 case id/path 的列表；不得把类别、哈希旁的私有描述或 pass criteria 拼入模型上下文。运行前固定候选 SHA、共同 runtime/model/settings、输出位置/格式及 evidence identity/hash 规则；raw 在运行中产生，两个完整 run 的实际 bytes、hash 和完整性固定后才可解封 oracle/rubric。不得提前合并本设计分支。

manifest 记录 PUBLIC 与私有 payload 的 SHA256；冻结身份为包含 manifest 的 Git commit SHA，交付时单独给出，避免循环 self-hash。后续两次运行须复用同一 PUBLIC 字节。候选 v0.2 与共同 runtime 合同在另行授权阶段记录，不在本轮假设或实现。

此处冻结是 Git 版本和访问隔离政策，不是加密密封，也不是未来 runner 隔离已验证。若隔离不能落实，后续必须停止，不能把受污染结果当独立 holdout。

## 9. 机械验证与停止边界

冻结前校验：12 PUBLIC、12 oracle、12 coverage 一一对应；类别精确 4/2/2/2/1/1；10 shapes；GOOD=5（strict=3/partial=2）；显式 uncertainty=6；authority stress=6；合法 DP/mode/terminal/HF references；PUBLIC 泄漏扫描；payload hash；门槛在 manifest/report 一致。

同时核对所有原有 342 个 tracked 文件与起点 byte-for-byte 一致、仅新增指定 16 文件、没有 Stage 11 run outputs、没有 Agent v0.2 实现、没有 Agent/KB/Harness 或 Stage 10 改动、没有秘密。Git diff/提交父节点/远端 SHA 在最终交付时核验。

本轮完成设计、review、mechanical validation、commit/push 后停止。任何 v0.2 repair、harness 适配或 measured run 属于后续授权阶段；此报告不宣布 v0.2 holdout PASS。
