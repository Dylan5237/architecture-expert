# Stage 11D — Paired Defect Delta

**Current holdout gate: FAIL; scoring complete, Chief Architect adjudication pending.**

固定双版本的整体分数为184/212→176/212（−8分，−200/53 pp）；D3为16/24→15/24（−1分，−25/6 pp）；HF03 distinct case/code为4→4，relative reduction=0%。没有新protected HF case/code pair，primary route12→12、strict GOOD CASE material FP0→0、global terminal12/12→12/12；这些稳定项不能替代C1/C2/C6的失败。

## Evidence and comparison scope

评分对象仅是`113ac1a4a6ffafeb4af0724c5a7efa2c14ffb21a`中24个canonical final-answer raw。v0.1 SUT=`96d9ae333ffc5a8076d635b86634b5151ec0bbc5`；v0.2 SUT=`c12b67c7410878960c45a9934ded6ae52ae6c42f`。oracle/coverage/manifest直接来自`69cab5ab750c350ce719a0d37e7680bbc96bdf21`，rubric直接来自`ff157eb1947860345a305fb29452b51e09dd3a2b`。先核验两run固定并通过Gate0再解封；规则、分组和门槛没有调整。

下文`v0.x/H11-xxx:L`均指`eval/stage11/holdout/run/v0.x/raw/H11-xxx.md`在上述evidence commit的one-based canonical行。逐维 rationale、exact quotes/HF受影响维度、初评分锁定矩阵与最终统一记录在`eval/stage11/holdout/scoring/paired-case-scores.yaml`；算术、七门禁和子组在`reports/STAGE11_PAIRED_SCORECARD.md`。没有使用Stage10分数作为v0.1 holdout baseline，也没有运行Stage10 regression。

## Measured improvements

| Observation | Fixed evidence | Score effect and limit |
|---|---|---|
| H001避免选样方向的项目事实扩写 | v0.1/001:26把hand-selected断言为systematically avoids pathological sizes；v0.2/001:18,24,36保持pilot与production sizing证据边界 | HF03在001被移除，D3 0→2；设备批准两版都维持NEEDS_EVIDENCE。没有证据证明容量能力增长 |
| H011不再断言未给出的完整diff范围 | v0.1/011:18称No diff hunk exists outside epoch variation axis；v0.2/011:18-27只据供应的delta/config/test判断 | HF03在011被移除，D3 0→2；NO_DEFECT和单一DP003都稳定，v0.2 evolution overlay漏标使D1 2→1 |
| H002更完整地分开capture/upload/clock问题 | v0.2/002:16-24明确session count、upload bucket与capture-time/clock comparability | D4 1→2、D1 1→2；这两分不抵销其新增无证据的历史销毁/采证排除 |
| H012继续保护all-component publication，少一个carry-over | 两版/012的join、reviewed-output assembly和pending/fail保持supported formats；v0.2/012:18-25,67-82 | D6两版均2，minimum correction没有由verbosity获得额外分；D10 1→2。actual served-byte binding按机制等价认可，而不是强制特定snapshot/hash词汇 |

HF03移除的case为001、011，新增的case为005、009，共有的case为002、004。因此“修好两案”与“HF03减少50%”并非同一结果；distinct pairs净变化为0。

## Measured regressions and shared defects

| Observation | Fixed evidence and mechanism | Dimensions / registration |
|---|---|---|
| H002将missing provenance扩成destroyed history，继而排除证据 | v0.2/002:22、38、50、88把firmware replaced before export改写为controller history destroyed/Not collectible；PUBLIC没有销毁事实 | HF03[D3,D8]；D8 2→0，D6 2→1。两版capture-boundary BLOCKER都缺支持性证据，HF01[D9]共有，不能因六个字段齐全认定六柱成立 |
| H005把恢复能力升级为决策可逆 | v0.2/005:11 “both reversible (recovery procedures tested for each)”；recovery tests没有证明撤销决定/反向迁移 | 新HF03[D3]，D3 2→0；不是protected code，所以不触发C3。如何理解reversible需裁决 |
| H009把已给enforcement evidence升级成排他项目事实 | v0.2/009:59 “currently enforced only by tests + runtime contract”；输入没有排除既有runtime guards | 新HF03[D3]，D3 2→0；L50把已否证race仍标NEEDS_EVIDENCE，使D9 2→1，但全局NO_DEFECT正确，没有material strict GC false positive |
| H007局部代理方案缺既有signed URL覆盖闭环 | v0.2/007:41-45只讲API/front、未来不发storage URLs；未明确撤销已发URL或强制关闭原直达storage绕行；v0.1/007:42,46明确use-time storage check或atomic/total invalidation | D6/D7/D9 2→1。未因方案细节不足自动注册HF05；若authorizing front明确强制覆盖原endpoint，可能恢复分数，需裁决 |
| H008错误把assertion verification作为drift对象 | v0.2/008:16-20的competing record A是USER_ASSERTION，不是接受的project-truth surface | D3/D9 2→1；SDK fixture、plugin unknown与safe no-hit仍正确。不把分级/写作分歧变为HF |
| H004两版以安全拒绝代替已知输入的完整转换 | v0.1/004:13,37与v0.2/004:35-41,76都是returned unit+non-metre refusal；已知yard测试要求转换为metre | 两版同注册HF05[D6,D7]；shared material weakening，C3仍PASS。若仅认temporary containment，两版须同撤销HF，但D6仍不得满分；完整fix与containment需裁决 |
| H004两版将retained packet缺字段扩写为未采集 | v0.1/004:42；v0.2/004:43,99。外部keyed ledger并未被输入排除 | 共有HF03[D3]；scope of absence需裁决。两版正确分开producer defect与unknown vendor attribution，未据此注册HF10 |

D6为20/22→18/22，下降来自002和007各−1；D7为22/24→21/24，仅007−1；D8为12/12→10/12，仅002−2。H004的相同guarantee缺陷始终对两版用同一标准，不能当v0.2新缺陷或用更流畅的解释掩盖。

## Terminal choice and non-alarm preservation

本holdout里global terminal没有净改善或退化：两版均12/12。001/002/003/006需要证据；004/007/008/012已有局部minimum-fix主对象；005停止于OWNER_TRADE_OFF；009/010/011停止于NO_DEFECT。H011两版都选择CHANGE_REVIEW/DP003，只适用NO_DEFECT；允许ADR/DP004的terminal alternatives没有被用于放宽本次评分。

D9为20/24→17/24，差别来自finding dispositions、drift与纠正保证边界，不能宣称terminal guard改善，也不能把global terminal正确当作finding axis正确。H002一个全局NEEDS_EVIDENCE并不使同答unsupported BLOCKER合法；H009一个NEEDS_EVIDENCE finding不自动使整案发生HF08。

严格designated GOOD CASE 009/010/011两版material FP均0；006和007的correct partial guard也都被保留。009的enforcement事实扩写与GOOD CASE误报是不同问题。010对immutable source、digest verification、view binding的非误报保护稳定；没有测到framework prescription、inconvenience ARCH_CONFLICT或private leakage的新缺陷。

## Generalizable weaknesses supported by this run

1. **缺失的作用域仍会被扩大。** 从“这个packet/record没有字段”跳到“系统从未captured”“history destroyed”“only tests enforce”。通用证据守卫存在并不证明它在具体claim上有效；load-bearing claim必须回到输入提供的时间/路径/范围。
2. **局部安全floor容易被当作完整产品保证。** H004 refusal守住不错误发布，但未完成已知输入转换；H007新增代理路径没有说明已有可用bearer URL怎样被约束。完整修复需要说明所有仍被支持的路径如何满足同一个accepted property。
3. **全局终局与局部finding轴仍有混用。** H002 unsupported BLOCKER、H008 USER_ASSERTION drift、H009 refuted accusation的NEEDS_EVIDENCE都未改变global terminal，却降低D9。
4. **Primary routing稳定，overlay契约持续不完整。** 两版primary12/12、D1同14/24，问题主要是explicit overlay缺漏/误标；没有依据要求新的routing procedure或扩展ontology。

## Smallest possible next repair, conditional on adjudication

已经测到C1/C2/C6失败，因此可向owner提出一个小范围修复候选，但本任务不实施、不宣布新版本，也不创建新benchmark：

- 对证据守卫增加最后输出检查：每个否定事实和exclusive/historical claim必须指向同scope的project evidence；如果只有packet/record缺失，改为该scope的UNKNOWN和named next observation。不要从replacement推destruction、从recovery推reversibility、从给定tests推only enforcement。该候选针对005/009的新HF03与002/004持续的absence扩写。
- 若004/007的guarantee裁决成立，只补一条existing-path closure检查：枚举仍有效的已发capability/已知accepted input路径；分别说明转换、use-time拒绝或强制失效的真实机制及保留能力。不能以refusal/新proxy名字自称完整fix，也不需要换框架或平台。
- 不提出新的terminal rewrite：global terminal已12/12；只有在裁决确认finding/drift误触发后，才针对这些轴补最小一致性检查。Primary路线也未测到退化，不以此授权routing重构。

这些候选只来自本次可定位的失败，不是对Agent/KB的新修改授权。Chief Architect可以接受、拒绝或收窄它们；后续修复/验证属于单独任务。

## Disputes, delivery and limits

需要裁决001/002/004/005/007/009/011：所有注册HF、004双版containment边界、007旧URL/front完整性，以及009 owner abstraction与only enforcement的事实范围。建议分层spot-check006/010/012。root按机制等价未注册006 pre-programming digest HF03；同一个已给check不能证明后续flash完整性，不等于断言项目没有额外readback。012只组装reviewed outputs并消除late raw replacement已按实际served identity的机制等价计D6=2；额外cross-adapter验证是抽查限制。

规则、oracle/rubric、七门禁、category与strict grouping保持冻结。裁决若改变分数或HF，应重算exact fractions，不能先把FAIL提升为release approval。当前仅三个授权新文件；29 canonical evidence及Agent/KB/Harness字节不变，没有模型执行、修复、merge/deploy/release。本地普通commit完成后，push依用户Git约定另待明确确认；remote SHA未匹配前不能报告已推送。

12个固定案例、每版一次run不足以给出跨模型、跨系统或统计显著性结论。当前报告提供的是可复算的holdout scoring与争议清单，架构师裁决、完整Stage11接受和Agent release approval仍未完成。
