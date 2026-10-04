# Stage 10 Phase D Scorecard

日期：2026-10-04（Asia/Shanghai）

状态：**SCORED_PENDING_ADJUDICATION**；32 案评分完成，22 案需人工裁定。

总分：**434/538（80.67%）**。

## 1. 证据与适用范围

- canonical evidence SHA：`d6ac48c16f7285f53fbc7af6e5aae4f64f83123b`
- runtime freeze SHA：`7db2639044d3a8f0b8706d70161513238ed29670`
- suite-design SHA：`ff157eb1947860345a305fb29452b51e09dd3a2b`
- frozen SUT SHA：`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`
- run_id：`phasec-20260930T101227Z-7db26390`
- 实例：Agent v0.1 / company compute gateway / `glm-5.3` / temperature=0 / max_tokens=32000 / max_tool_rounds=24
- 本评分的适用范围限定为上述 Agent、模型及冻结 Harness 组合；跨 provider 或其他运行设置的表现未评估。
- 评分辅助：四组 `gpt-6-astra/high` 委派配置；主评分者统一复核 HF、适用维度及汇总。子 Agent 无独立后端身份读取接口，配置记录来自主 Agent 的 spawn 调用。
- 任务来源：`origin/main@a96ea6a7bcb677df3b234889f7cbc9719f26dbcf:tasks/stage10/CODEX_PHASE_D_SCORING.md`。

## 2. 完整性与评分规则

32/32 COMPLETE，32 个非空 raw，34 个规范 evidence 文件；SHA、唯一归属与重复检查均通过。原有 338 个 tracked 文件保持原字节，评分期无重跑、无模型/API调用、无外部研究。Windows 初次 checkout 的 CRLF 转换未用于评分；保留该 checkout 后以关闭转换的全新 worktree 获取 canonical 原字节。

oracle/rubric/coverage/manifest 仅直接读取冻结 Git blobs；未改变规则或证据。评分只使用 raw 的可见结论；tool/route metadata 不补齐正文。逐案记录、理由、证据行号、HF依据和受影响维度见 `eval/stage10/scoring/case-scores.yaml`。

使用 0/1/2 ordinal。51 个 N/A 不计分母；其余269个适用维度的满分为538。HF只将受影响维度置0，保留其他维度所得分，并单独登记。该分数不能掩盖16案的HF；没有据此宣布 Agent/Phase PASS。

D1/D2/D3/D9/D10永不N/A；本套32案均要求机制或决策机制推理，D4均适用。D6仅纯ADR/authority重做的010/018/024为N/A；D5须存在实际合规非报警组件，不能因列GC检查就获分；D7按实际authority surface，D8按实质缺证据或冲突判断。逐案N/A理由可审计。

统一复核校准：004/005/031的D5改为N/A；027的“the migration ticket”结合16–19/44/51行解释为模板迁移依赖，未达到明确既成事实HF-03阈值，D3=1并继续标记裁定。这些是应用既定规则的记录，未修改oracle/HF定义。

## 3. 维度与总分

| 维度 | 含义 | 得分/适用满分 | 百分比 | 适用案数 | N/A案数 |
|---|---|---:|---:|---:|---:|
| D1 | routing_correctness | 53/64 | 82.81% | 32 | 0 |
| D2 | property_understanding | 61/64 | 95.31% | 32 | 0 |
| D3 | evidence_discipline | 27/64 | 42.19% | 32 | 0 |
| D4 | mechanism_accuracy | 51/64 | 79.69% | 32 | 0 |
| D5 | goodcase_precision | 27/28 | 96.43% | 14 | 18 |
| D6 | min_correction | 48/58 | 82.76% | 29 | 3 |
| D7 | product_contract_authority | 47/52 | 90.38% | 26 | 6 |
| D8 | uncertainty_evidence | 11/16 | 68.75% | 8 | 24 |
| D9 | finding_terminal | 51/64 | 79.69% | 32 | 0 |
| D10 | scope_discipline | 58/64 | 90.62% | 32 | 0 |

总和：434/538 = 80.67%。采用适用点数之和，没有平均各案百分比或任意重新加权。

## 4. Hard-failure register

| HF code | 次数 | 案例 |
|---|---:|---|
| HF-01 | 1 | E10-004 |
| HF-02 | 0 | 无 |
| HF-03 | 12 | E10-005, E10-006, E10-007, E10-009, E10-011, E10-012, E10-019, E10-022, E10-028, E10-029, E10-030, E10-031 |
| HF-04 | 0 | 无 |
| HF-05 | 1 | E10-001 |
| HF-06 | 0 | 无 |
| HF-07 | 0 | 无 |
| HF-08 | 0 | 无 |
| HF-09 | 0 | 无 |
| HF-10 | 2 | E10-018, E10-021 |
| HF-11 | 0 | 无 |
| HF-12 | 0 | 无 |

HF总数16，涉及16/32案。每项的逐字证据、冻结basis、trigger与受影响维度均在case-scores；无HF-02/04/06/07/08/09/11/12记录。所有HF仍需人工裁定。

## 5. 逐案摘要

EXACT/ALT为primary route判定；D1另含overlay质量。数字为D1→D10，N表示N/A。

| Case | 主路由 | 逐维分值 | 总分 | 全局terminal | HF | 裁定 |
|---|---|---|---:|---|---|---|
| E10-001 | ARCH_REVIEW / DP-002 (EXACT) | 2/2/2/2/2/1/0/N/2/2 | 15/18 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-05 | 是 |
| E10-002 | ARCH_REVIEW / DP-002 (EXACT) | 1/2/2/2/2/2/2/N/2/1 | 16/18 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 否 |
| E10-003 | INCIDENT_ANALYSIS / DP-005 (EXACT) | 2/2/2/2/N/2/N/N/2/2 | 14/14 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 否 |
| E10-004 | ARCH_REVIEW / DP-002 (EXACT) | 2/2/1/2/N/2/2/2/0/2 | 15/18 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-01 | 是 |
| E10-005 | CHANGE_REVIEW / DP-003 (EXACT) | 2/2/0/2/N/2/2/N/2/1 | 13/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-03 | 是 |
| E10-006 | ARCH_REVIEW / DP-002 (EXACT) | 1/2/0/1/2/2/2/N/2/2 | 14/18 | NO_DEFECT (PASS) | HF-03 | 是 |
| E10-007 | INCIDENT_ANALYSIS / DP-005 (EXACT) | 2/2/0/1/N/1/2/N/2/2 | 12/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-03 | 是 |
| E10-008 | ARCH_DESIGN / DP-001 (EXACT) | 1/1/1/1/2/2/2/2/2/2 | 16/20 | NO_DECISION_CHANGING_WORK (PASS) | — | 否 |
| E10-009 | INCIDENT_ANALYSIS / DP-005 (EXACT) | 2/2/0/2/N/2/2/N/2/2 | 14/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-03 | 是 |
| E10-010 | ADR_REVIEW / DP-004 (EXACT) | 1/2/1/2/2/N/2/2/0/2 | 14/18 | MIN_SAFE_FIX_IDENTIFIED (FAIL) | — | 是 |
| E10-011 | CHANGE_REVIEW / DP-003 (EXACT) | 1/2/0/1/N/1/2/N/2/2 | 11/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-03 | 是 |
| E10-012 | INCIDENT_ANALYSIS / DP-005 (EXACT) | 2/2/0/2/2/2/N/2/1/1 | 14/18 | NEEDS_EVIDENCE (PASS) | HF-03 | 是 |
| E10-013 | ARCH_REVIEW / DP-002 (EXACT) | 2/2/2/2/2/2/2/N/0/0 | 14/18 | NEEDS_EVIDENCE (FAIL) | — | 否 |
| E10-014 | CHANGE_REVIEW / DP-003 (EXACT) | 2/2/1/2/N/2/2/N/2/2 | 15/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 否 |
| E10-015 | INCIDENT_ANALYSIS / DP-005 (EXACT) | 1/2/1/2/2/1/1/N/2/1 | 13/18 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 是 |
| E10-016 | CHANGE_REVIEW / DP-003 (EXACT) | 1/2/1/2/N/1/2/N/2/2 | 13/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 否 |
| E10-017 | CHANGE_REVIEW / DP-003 (EXACT) | 2/2/1/2/N/2/2/N/2/2 | 15/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 否 |
| E10-018 | ADR_REVIEW / DP-004 (EXACT) | 2/2/1/0/N/N/2/0/0/2 | 9/16 | MIN_SAFE_FIX_IDENTIFIED (FAIL) | HF-10 | 是 |
| E10-019 | INCIDENT_ANALYSIS / DP-005 (EXACT) | 2/2/0/2/N/1/2/N/2/2 | 13/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-03 | 是 |
| E10-020 | ARCH_REVIEW / DP-002 (EXACT) | 2/2/1/1/N/2/2/N/2/2 | 14/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 是 |
| E10-021 | INCIDENT_ANALYSIS / DP-005 (EXACT) | 2/2/1/0/N/2/N/0/1/2 | 10/16 | NEEDS_EVIDENCE (PASS) | HF-10 | 是 |
| E10-022 | ARCH_DESIGN / DP-001 (EXACT) | 1/1/0/1/2/2/1/N/1/2 | 11/18 | NO_DECISION_CHANGING_WORK (PASS) | HF-03 | 是 |
| E10-023 | ARCH_REVIEW / DP-002 (EXACT) | 2/2/2/2/N/2/2/N/2/2 | 16/16 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 否 |
| E10-024 | ADR_REVIEW / DP-004 (ALT) | 2/1/1/1/N/N/1/1/1/2 | 10/16 | ARCH_CONFLICT (PASS) | — | 是 |
| E10-025 | ARCH_REVIEW / DP-002 (EXACT) | 2/2/2/2/2/2/N/N/2/2 | 16/16 | NO_DEFECT (PASS) | — | 否 |
| E10-026 | ARCH_REVIEW / DP-002 (EXACT) | 2/2/2/2/2/2/2/N/2/2 | 18/18 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 否 |
| E10-027 | ARCH_REVIEW / DP-002 (EXACT) | 2/2/1/2/N/1/N/N/2/2 | 12/14 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 是 |
| E10-028 | CHANGE_REVIEW / DP-003 (EXACT) | 1/2/0/2/1/1/2/N/1/2 | 12/18 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-03 | 是 |
| E10-029 | ARCH_DESIGN / DP-001 (EXACT) | 2/2/0/2/2/2/2/N/2/2 | 16/18 | NO_DECISION_CHANGING_WORK (PASS) | HF-03 | 是 |
| E10-030 | CHANGE_REVIEW / DP-003 (EXACT) | 2/2/0/2/N/2/N/N/2/2 | 12/14 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-03 | 是 |
| E10-031 | CHANGE_REVIEW / DP-003 (EXACT) | 1/2/0/1/N/1/2/2/2/2 | 13/18 | MIN_SAFE_FIX_IDENTIFIED (PASS) | HF-03 | 是 |
| E10-032 | CHANGE_REVIEW / DP-003 (EXACT) | 1/2/1/1/2/1/2/N/2/2 | 14/18 | MIN_SAFE_FIX_IDENTIFIED (PASS) | — | 是 |

## 6. 路由、terminal与非报警

- 主路由接受准确率：32/32（100%）；31案与oracle primary一致，024采用明确允许且有对象依据的ADR_REVIEW/DP-004。非oracle primary的024按任务标记裁定。
- 完整D1=2：21/32（65.63%）；11案primary正确但overlay声明/选择不完整，D1=1。主路由100%不代表完整routing contract100%。
- 全局terminal准确率：29/32（90.63%）。010/018输出MIN_SAFE_FIX_IDENTIFIED，冻结期望OWNER_TRADE_OFF或NEEDS_EVIDENCE；013输出NEEDS_EVIDENCE，期望NO_DEFECT。不能用正文的保留或其他finding字段替换实际terminal。
- frozen strict GOOD CASE/non-alarm组件：8/8正确识别，material false positive=0，非报警precision=8/(8+0)=100%。026的增长风险是合法正向finding，不把它当合规merge组件的误报。该指标仅覆盖冻结8案的指定组件；这8案的全局terminal准确率为6/8，仍有3案其他类型HF。
- 028在strict8之外：客户端部分修复的合并边界含糊，D5=1并标记裁定；本报告未据此声称所有局部非报警边界均已解决。

## 7. Ambiguity与NEEDS_EVIDENCE

冻结严格歧义6案：010、012、018、021、024、031。uncertainty_result为3 PASS、2 FAIL（018/021局部false certainty）、1 AMBIGUOUS（024）；该组全局terminal4/6正确。

012/021都输出NEEDS_EVIDENCE，达到两案全局终态要求（2/2）；但012将一次窗口扩写成每日故障，021把1% sampler与0.4% error直接推成必然零捕获。保持主要根因未知不能消除这些局部无依据断言。031保留“相关、可能因果”的状态并提出pool利用率/acquire-wait观察；仍有虚构已有自动回滚的HF-03。024的替代DP合法，固定约束冲突被条件化的处理仍待裁定。

## 8. Product-contract authority

冻结product_contract_surface8案：6 PASS、2 AMBIGUOUS（015/024），primary与全局terminal均8/8匹配。D7全部适用案总分47/52（90.38%）。

范围更广的产品保证检查还发现001接受bounded-interval落盘并保证强杀永不丢编辑，记录HF-05；015的order/payment-intent基数、022的brief维护与node-loss outage边界未明确。不能从冻结surface组的通过率推断所有产品保证已受保护。多数ToS/PRD/跨团队约束被保留，局部修正的后置保证仍是弱点。

## 9. 冻结coverage分组

以下组的成员仅来自冻结coverage.yaml，不按观察结果重分组。组间可重叠，不能相加当全套总分。

| 冻结组 | 案数 | 得分/满分 | 百分比 | primary正确 | terminal正确 | HF案数 |
|---|---:|---:|---:|---:|---:|---:|
| AUTO-route challenge (strict) | 6 | 81/102 | 79.41% | 6/6 | 5/6 | 2 |
| GOOD CASE/non-alarm (strict) | 8 | 117/144 | 81.25% | 8/8 | 6/8 | 3 |
| ambiguity (strict) | 6 | 70/102 | 68.63% | 6/6 | 4/6 | 4 |
| cross-domain (strict) | 8 | 118/134 | 88.06% | 8/8 | 8/8 | 4 |
| primary-route ambiguous | 2 | 23/34 | 67.65% | 2/2 | 2/2 | 1 |
| product-contract surface | 8 | 102/134 | 76.12% | 8/8 | 8/8 | 4 |

严格AUTO challenge为6案；coverage另记录PUBLIC requested AUTO为19案，两个数量含义不同。跨域8案全局终态均正确，但4案出现HF-03，不能将机制方向正确当作事实纪律正确。

## 10. 按DP/mode汇总

采用coverage.mode（oracle preferred mode）分组；024虽然观察到允许的DP-004，仍留在冻结ARCH_REVIEW组，防止改变分组口径。031保留CHANGE_REVIEW。

| Mode / DP | 案数 | 得分/满分 | 百分比 | terminal正确 | HF案数 |
|---|---:|---:|---:|---:|---:|
| ADR_REVIEW / DP-004 | 2 | 23/34 | 67.65% | 0/2 | 1 |
| ARCH_DESIGN / DP-001 | 3 | 43/56 | 76.79% | 3/3 | 2 |
| ARCH_REVIEW / DP-002 | 11 | 160/186 | 86.02% | 10/11 | 3 |
| CHANGE_REVIEW / DP-003 | 9 | 118/148 | 79.73% | 9/9 | 5 |
| INCIDENT_ANALYSIS / DP-005 | 7 | 90/114 | 78.95% | 7/7 | 5 |

## 11. 裁定与限制

需裁定（22案）：E10-001, E10-004, E10-005, E10-006, E10-007, E10-009, E10-010, E10-011, E10-012, E10-015, E10-018, E10-019, E10-020, E10-021, E10-022, E10-024, E10-027, E10-028, E10-029, E10-030, E10-031, E10-032。

HF-01的004实质影响柱、027模板依赖/流程审批、015/028幂等意图与部分合并、032quarantine门禁语义是重点解释边界。分数是当前独立评分判断，尚无人类adjudication。裁定可能改变分值/HF；当前oracle/HF taxonomy和canonical evidence保持冻结。

机械校验覆盖32唯一score条目、raw/oracle/PUBLIC一一对应、合法分值及N/A、HF受影响维度归零、全部聚合算术、3个新文件写入白名单、原有338文件/34 evidence字节不变、secret scan、无private源全文复制、无重跑/外部研究；提交推送和remote SHA另在最终交付中核验。
