# Stage 11D — Paired Holdout Scorecard

**SCORING: SCORED_AWAITING_ARCHITECT_ADJUDICATION**
**Gate 0: PASS**
**STAGE11_HOLDOUT_GATE: FAIL**

当前统一初评分为 v0.1 **184/212 = 46/53 = 86.79245283%**，v0.2 **176/212 = 44/53 = 83.01886792%**，差值 **−8 分 / −200/53 个百分点 = −3.77358491 pp**。七项预注册门禁中 C1、C2、C6 FAIL，C3、C4、C5、C7 PASS。所有注册 HF 及标记的关键解释等待 Chief Architect 裁决；此结果不是 Agent v0.2 release approval，也不是 Stage 11 PASS。

## Provenance and fixed run scope

| Identity | Frozen value |
|---|---|
| branch | `eval/stage11-paired-scoring` |
| starting_head | `113ac1a4a6ffafeb4af0724c5a7efa2c14ffb21a` |
| task_source | `9f9e5df88ea31931581915bb7f35d42d9020dcce:tasks/stage11/CODEX_STAGE11_PAIRED_SCORING.md` |
| task_sha256 | `4774e5fbe2bbc1df1dfc77ca270cb2990c564f58f77f7db5fa69b43adbc15b8f` |
| design_sha | `69cab5ab750c350ce719a0d37e7680bbc96bdf21` |
| rubric_ref | `ff157eb1947860345a305fb29452b51e09dd3a2b:eval/stage10/design/rubric.md` |
| evidence_sha | `113ac1a4a6ffafeb4af0724c5a7efa2c14ffb21a` |
| v0_1_sut | `96d9ae333ffc5a8076d635b86634b5151ec0bbc5` |
| v0_2_sut | `c12b67c7410878960c45a9934ded6ae52ae6c42f` |
| adapter_sha | `c3fe4596961cf3abf30296aac169ef73c71034cd` |

- 专用 worktree：`D:\_projects\TempFiles\MartinFowler\architecture-expert-wt-stage11-paired-scoring-20261008`；开始时 clean，分支/HEAD 精确匹配。远端 main 独立读回为任务来源 SHA。
- AGENTS.md 已读取。TASK.md 仍指 Stage 9；明确授权的 Stage 11D task 与 Issue #30 最新授权评论共同确定当前范围：https://github.com/Dylan5237/architecture-expert/issues/30#issuecomment-6055080595。控制 issue 检索含历史 Stage 10 概要，但没有读取 Stage 10 raw/scorecard 或将其分数用作 holdout baseline。
- Gate 0 完成后才从 frozen design/rubric commit 解封。12 PUBLIC、oracle、coverage 的 payload hashes 和 rubric SHA256 均按 frozen manifest 校验。
- 双版本 COMPLETE，各 12 个非空 raw；29 canonical run 文件、24 raw hashes、12 跨版同一 PUBLIC hashes 全部一致。两版各 206 snapshot hashes 对应指定 SUT 的 Git archive；活动 prompt 分别 `57b8f181429d316f88cf84edcc52b13d0a97eb89df7b0b0ecf5d7d0f0c032367`、`775a9d1c0e918d031a48ee6ed3de6c58caefe610aec49a8f1e15b2c63c9dc698`。
- 同一 company-gateway `glm-5.3`，temperature=0、max_tokens=32000、tool ceiling=24，transport/harness 相同。97/97 observed model rounds 匹配；无 integrity HOLD。现有 3 次不存在的 SUT GOOD CASE 文件读取均被拒绝，没有 private-path allow。
- `core.autocrlf=true`：working files 有正常 CRLF checkout 转换；canonical LF blob 与 metadata raw SHA256 一致，29 clean-filter blob 身份全部匹配冻结提交。未重写 evidence 文件。
- 两个子评分者分别只读一版 raw、先锁定 per-case scores；root 随后复核冻结触发和机制等价边界，再计算跨版汇总。YAML 的 `independent_lock_audit` 保留初评分矩阵，仅供追溯，不计入最终24条record汇总。
- 没有 H11/provider/model rerun、Agent/KB/Harness 修改、规则调整、design merge、deploy/release。评分仅依据 final answer raw；工具元数据/隐藏推理不作为答案内容。

## D1..D10 and overall

| Dimension | v0.1 earned/max | v0.1 % | v0.2 earned/max | v0.2 % | Δ earned |
|---|---:|---:|---:|---:|---:|
| D1 | 14/24 | 58.33% | 14/24 | 58.33% | +0 |
| D2 | 24/24 | 100.00% | 24/24 | 100.00% | +0 |
| D3 | 16/24 | 66.67% | 15/24 | 62.50% | -1 |
| D4 | 23/24 | 95.83% | 24/24 | 100.00% | +1 |
| D5 | 10/10 | 100.00% | 10/10 | 100.00% | +0 |
| D6 | 20/22 | 90.91% | 18/22 | 81.82% | -2 |
| D7 | 22/24 | 91.67% | 21/24 | 87.50% | -1 |
| D8 | 12/12 | 100.00% | 10/12 | 83.33% | -2 |
| D9 | 20/24 | 83.33% | 17/24 | 70.83% | -3 |
| D10 | 23/24 | 95.83% | 23/24 | 95.83% | +0 |
| Overall | 184/212 | 86.79% | 176/212 | 83.02% | −8 |

D1、D2、D3、D4、D7、D9、D10 每版 max=24；D5 max=10；D6 max=22；D8 max=12，总 max=212。百分比只用于展示；所有门禁比较用 exact fractions。Overall 是 sum earned / sum applicable max，不是各案百分比的平均。

N/A 两版完全一致：D5 仅 H11-006/007 的 partial non-alarm 和 H11-009/010/011 的 strict GOOD CASE 适用；D6 仅纯 ADR/authority H11-005 为 N/A；D8 仅 H11-001/002/003/004/006/008 适用。D7 依据每案 accepted property/authority 表面全12案适用，coverage 的 product-contract tag 不决定 N/A。D4 每案都有所要求的机制判断。

## Per-case paired deltas

| Case | v0.1 earned/max | v0.2 earned/max | Δ points | Main measured change |
|---|---:|---:|---:|---|
| H11-001 | 14/18 | 17/18 | +3 | 移除偏向异常样本的无依据断言，设备决定仍evidence-gated |
| H11-002 | 12/18 | 11/18 | -1 | 时间机制更完整；虚构历史销毁并排除采证，unsupported BLOCKER持续 |
| H11-003 | 17/18 | 17/18 | +0 | 稳定区分helper未知与不存在；保留cache许可 |
| H11-004 | 11/18 | 11/18 | +0 | 两版相同guard/已知yard转换缺口，HF05统一处理 |
| H11-005 | 13/14 | 10/14 | -3 | 把recovery tests上升为可逆事实；增加治理风险分级 |
| H11-006 | 19/20 | 18/20 | -1 | 全qualification保持NEEDS_EVIDENCE；v0.2新增标注的carry-over |
| H11-007 | 17/18 | 14/18 | -3 | v0.2缺具体旧URL强制失效/关闭绕行保证 |
| H11-008 | 17/18 | 15/18 | -2 | safe no-hit稳定；v0.2错误以USER_ASSERTION触发drift |
| H11-009 | 17/18 | 14/18 | -3 | 无实质GC误报；v0.2虚构only enforcement并混用finding轴 |
| H11-010 | 17/18 | 17/18 | +0 | 稳定拒绝immutable cache/async误报 |
| H11-011 | 16/18 | 17/18 | +1 | v0.2未断言未给完整diff的绝对范围，仍只选DP003 |
| H11-012 | 14/16 | 15/16 | +1 | join全部reviews+只用reviewed outputs机制等价保护served identity；v0.2少一个carry-over |

逐维理由、raw path/SHA256、one-based canonical 行范围、HF 精确引文、terminal、route/overlay 分离和裁决标记均在 `eval/stage11/holdout/scoring/paired-case-scores.yaml`。

## Frozen subgroup reconciliation

| Exclusive frozen category | Cases | v0.1 earned/max | v0.2 earned/max | Δ points |
|---|---|---:|---:|---:|
| H-EVIDENCE | 001, 002, 003, 004 | 54/72 | 56/72 | +2 |
| H-TERMINAL | 005, 006 | 32/34 | 28/34 | -4 |
| H-GUARANTEE | 007, 008 | 34/36 | 29/36 | -5 |
| H-GOODCASE | 009, 010 | 34/36 | 31/36 | -3 |
| H-ROUTING | 011 | 16/18 | 17/18 | +1 |
| H-CROSS | 012 | 14/16 | 15/16 | +1 |
| Sum | 12 | 184/212 | 176/212 | −8 |

类别保持 frozen coverage：4 evidence、2 terminal、2 guarantee、2 goodcase、1 routing、1 cross；10 shapes。严格 GOOD CASE 为固定3案009/010/011，不因输出重分组；partial 006/007不混入C5。

## Seven preregistered criteria

| Criterion | Exact arithmetic and affected scope | Result |
|---|---|---|
| C1 D3 +≥20 pp | v0.1=16/24=2/3；v0.2=15/24=5/8；差=−1/24=−25/6 pp < 1/5=20 pp。baseline HF03=4，故“HF03=0 AND D3≥90%”例外不适用。D3改善001/011、退化005/009，各±2；008退化1，净−1。 | **FAIL** |
| C2 HF03减少≥50% | distinct(case,HF03)：4→4；2×4=8 > 4；relative reduction=(4−4)/4=0%。 | **FAIL** |
| C3 无新protected HF pair | HF02/05/06/07/09逐code set(v0.2)⊆set(v0.1)；HF05两版同为{004}，其它空；new pairs=∅。 | **PASS** |
| C4 accepted primary routes不减少 | 12 EXACT→12 EXACT；12≥12；允许alternate未使用。D1仍单独反映overlay质量。 | **PASS** |
| C5 strict GOOD CASE误报不增加 | 固定009/010/011的designated component material FP：0→0；0≤0。 | **PASS** |
| C6 Overall不退化 | 176/212=44/53 < 184/212=46/53；cross products 176×212=37312 < 184×212=39008。 | **FAIL** |
| C7 v0.2 private-eval泄漏为0 | v0.2 HF11 set=∅，count=0。PUBLIC case ID和合法SUT知识ID不当leakage。 | **PASS** |

默认D3所需整数增量至少5/24（20.8333 pp）；本baseline尚有8分余量，不存在无法达到门槛的ceiling问题。没有调整阈值或增设例外。所有七项必须PASS；三项FAIL决定当前 `STAGE11_HOLDOUT_GATE: FAIL`。

## HF registry and protected comparison

| Code | v0.1 count / case set | v0.2 count / case set | New protected pairs |
|---|---|---|---|
| HF-01 | 1 / 002 | 1 / 002 | — |
| HF-02 | 0 / ∅ | 0 / ∅ | ∅ |
| HF-03 | 4 / 001, 002, 004, 011 | 4 / 002, 004, 005, 009 | — |
| HF-04 | 0 / ∅ | 0 / ∅ | — |
| HF-05 | 1 / 004 | 1 / 004 | ∅ |
| HF-06 | 0 / ∅ | 0 / ∅ | ∅ |
| HF-07 | 0 / ∅ | 0 / ∅ | ∅ |
| HF-08 | 0 / ∅ | 0 / ∅ | — |
| HF-09 | 0 / ∅ | 0 / ∅ | ∅ |
| HF-10 | 0 / ∅ | 0 / ∅ | — |
| HF-11 | 0 / ∅ | 0 / ∅ | — |
| HF-12 | 0 / ∅ | 0 / ∅ | — |

每版6个distinct case/code pairs、4个HF-affected cases。HF03的多条支持引文不重复计数；同案不同code分别计数。HF caps仅影响所列维度：HF03主要D3，v0.2 H002额外D8；HF01只D9；H004 HF05只D6/D7。没有自动整案归零。H004 material contract weakening两版同为1案，不能将共享缺陷说成v0.2新增protected pair。

## Routing, global terminals and GOOD CASE

Primary acceptance 两版12/12 EXACT；没有 ALLOWED_ALTERNATE 或 FAIL。overlay完整标注两版均2/12，但完整者不同：v0.1 004/011，v0.2 002/004；D1均14/24。正文触及某dimension不等于route line已准确标overlay；missing overlay不等于HF06。

| Global terminal | Expected cases | v0.1 correct | v0.2 correct |
|---|---|---:|---:|
| NEEDS_EVIDENCE | 001,002,003,006 | 4/4 | 4/4 |
| MIN_SAFE_FIX_IDENTIFIED | 004,007,008,012 | 4/4 | 4/4 |
| OWNER_TRADE_OFF | 005 | 1/1 | 1/1 |
| NO_DEFECT | 009,010,011 | 3/3 | 3/3 |
| Total | 12 | 12/12 | 12/12 |

H011两版都选CHANGE_REVIEW/DP003，所以只接受NO_DEFECT；没有用允许ADR/DP004的terminal union放宽其判断。global terminal正确不意味着finding dispositions、修复保证或D9全部正确：H002 unsupported BLOCKER、H005治理风险、H008 drift、H009 evidence disposition均单独计分。

| Strict designated GOOD CASE | v0.1 material FP | v0.2 material FP | Component protected |
|---|---:|---:|---|
| H11-009 | 0 | 0 | provided non-reentrant sole-loop transaction |
| H11-010 | 0 | 0 | immutable authoritative manifests + verified derived tiles/view binding |
| H11-011 | 0 | 0 | coherent governed security-epoch migration |

006 board guard和007新issuance guard两版均获正确partial credit；不能因为whole qualification/whole removal仍未完成而把partial guard计为GC false positive。

## Adjudication handoff

必裁决案例：**001、002、004、005、007、009、011**。所有注册HF待Chief Architect确认；007的旧链接方案边界会影响protected HF及整体分数，009也含“owner抽象”与“only enforcement”两个不同解释。没有material strict GOOD CASE误报。

| Case/version | Specific disputed registration or threshold-relevant boundary |
|---|---|
| 001 v0.1 | hand-selected是否可断言systematically avoids pathological sizes；HF03登记D3=0。 |
| 002 both | export缺字段是否足以断言capture全局未留存并注册BLOCKER；HF01/HF03受影响范围。v0.2另有controller history destroyed及不可采集断言。 |
| 004 both | 缺retained linkage能否推出never captured；HF03。完整fix拒绝已知yard与temporary containment的界线；HF05必须双版同判。 |
| 005 v0.2 | tested recovery procedures能否证明decision reversible；HF03。 |
| 007 v0.2 | authorizing front是否已足够表达强制覆盖旧storage endpoint；目前D6/D7/D9各1，未自动HF05。long TTL按零grace相对用语未认具体配置事实。 |
| 009 both | v0.1 sole-loop owner抽象最终未认HF03；v0.2 only tests/runtime enforcement最终认HF03。需按事实断言范围而非修辞一致性裁决。 |
| 011 v0.1 | 未给完整diff能否确认No diff hunk outside epoch axis；HF03。 |

建议少量分层抽查：006（whole qualification uncertainty/partial guard）、010（strict immutable GC）、012（cross-format completion与reviewed-byte binding的机制等价）。006和012的初评分分歧已由root统一解释，没有残留“拟取消/给1”作为当前结论；它们属于抽查记录。

裁决若改变注册/受影响维度，必须从24条final records重新机械计算七门禁。此会话没有代替Chief Architect处理争议，也没有用可能的裁决结果预先改阈值。

## Mechanical validation and delivery limits

- 24条final records、12 common IDs、合法D1..D10/0/1/2/N/A；same applicability；HF01..12代码、affected dims=0全部通过。
- 全部raw paths/hashes、每dimension/route/terminal/HF/uncertainty pointer范围、精确HF引文和route-conditioned terminal匹配通过；29 canonical run files再次读回一致。
- 逐维、逐案、exclusive category、HF distinct-pair、terminal与strict subgroup总数、七门禁exact fraction相互对账；两个独立机械核算一致。初评分口算值未作为结果。
- 唯一新增路径：`eval/stage11/holdout/scoring/paired-case-scores.yaml`、`reports/STAGE11_PAIRED_SCORECARD.md`、`reports/STAGE11_PAIRED_DEFECT_DELTA.md`。保护现有tracked artifacts。
- 无private oracle/rubric整段复制、secret或hidden reasoning；只保留所需触发/证据指针。源design/private未放进candidate snapshot。
- 交付边界：三文件本地普通commit；本次push须按用户Git约定取得明确确认，并在推送后读回remote SHA。提交身份沿用仓库配置，commit footer含Codex署名。报告自身不嵌入它所在提交的循环自SHA；scoring SHA以最终handoff为准。
- 固定12-case/one run per candidate，不能解释为统计显著性、所有架构能力覆盖、Stage10 regression执行、release/business acceptance。当前只完成holdout scoring，Agent不变。
