---
id: REPORT-STAGE5-KIMI
type: stage-report
stage: 5
author: kimi-k3 (Primary Falsification Researcher)
branch: research/stage5-falsification
date: 2026-09-18
issue: 12
baseline: 05cfea4981c77d9a13520762e2e37244d4079bce
---
# Stage 5 Falsification Report — 综合（Kimi）

边界：只做证伪与 disposition 输出；未改 canonical principles/P-*.md；未写 Constitution；未做 Stage 6 reduction；未做 Stage 7 ontology。原子 dossier 见 `reports/stage5/P-*.md`（11 份）。

## 1. 11 候选 disposition 矩阵

| 候选 | Disposition | 关键收窄点 |
|---|---|---|
| P-001 Explicit Ownership | **SURVIVES + NARROW** | 豁免 GC 托管内存维度的释放归属；邮箱等运行时托管队列的总量责任仍在设计者 |
| P-002 Change-Decision Boundaries | **SURVIVES + NARROW** | 事前识别变化轴是隐含适用前提，写入 statement；探索期无边界合法 |
| P-003 Bounded Execution | **SURVIVES + NARROW** | 界指资源维度（时间/内存/并发/队列/重试/扇出），持续时间不是资源维度；输入隐含界豁免 |
| P-004 Failure Containment | **SURVIVES + NARROW** | 隔离粒度是替代保证机制（进程边界/硬件虚拟化/静态验证）与成本的函数，不默认进程边界 |
| P-006 Change Locality | **DEMOTE** | 独立因果内容检验失败（D-03）；降为 P-002 的 measurable property / review signal |
| P-007 Designed Diagnostic Surfaces | **SURVIVES + NARROW** | 诊断表面必要性随静态保证强度递减（seL4）；观测本身是攻击面/隐私面 |
| P-008 Contract Preservation | **SURVIVES + NARROW** | 例外形态显式化：安全负债（RFC 7568）与技术负债（PEP 404）驱动的治理化破兼容合法 |
| P-009 Trust Minimization | **SURVIVES + NARROW** | 强制点限定在不可信输入/跨权限/外部集成/agent 动作的边界；封闭单用户形态内部不强制细分 |
| P-010 Authoritative State | **SURVIVES + NARROW** | D-14 确认：双维框架容纳 CRDT（显式合并语义=维度 2）；single-writer 非必需 |
| P-012 Overload Admission | **SURVIVES + NARROW** | 准入位置是架构决策（请求路径任一/组合层）；负载天然有界系统豁免 |
| P-013 Execution-Model-Honest Correctness | **SURVIVES（不变）** | 「承诺的保证 vs 实现巧合」判据有 Erlang 官方先例；actor/SQL good cases 成立 |

无 REJECT、无 MERGE_CANDIDATE 执行（D-04/D-05 等判别均判分立）；CONTESTED 项见 §11。

## 2. D-01..D-14 结果

| D | 结果 | 摘要 |
|---|---|---|
| D-01 P-001 vs P-002 | **分立维持** | 有边界无所有权（伪分层）/ 有所有权无边界（单模块监督 worker）案例对成立 |
| D-02 P-001 vs P-013 | **分立维持** | stale overwrite 归因规则：缺时序保证归 P-013，缺清理归属归 P-001 |
| D-03 P-002 vs P-006 | **P-006 降 property**（P-006 独立因果内容检验失败） | 见 P-006 dossier |
| D-04 P-003 vs P-012 | **分立维持** | 有界无策略 / 有策略无界 案例对成立 |
| D-05 P-004 vs P-009 | **分立维持** | 信任小故障权力大 / 隔离好权限宽 案例对成立；「权力≤职责」深层同构记为 Stage 6 Constitution 级抽象候选 |
| D-06 P-010 vs P-001 | **分立维持** | 裁决语义 vs 归属程序 |
| D-07 P-001 vs P-003 | **分立维持** | owned-but-unbounded / bounded-but-unowned 案例对成立；取消语义归 P-001、资源界限归 P-003 |
| D-08 safety floor | **有条件成立** | 安全/合规底线在安全关键与受监管语境真实存在（S-118 seL4、S-120 RFC 7568、ISO 25010:2023 新增 safety——间接）；floor 存在但 scope 有限（安全关键/受监管）。Stage 6 Constitution 公理应携带限定形式 |
| D-09 P-013 vs P-010 | **分立维持** | 全序化序列重复投递 / 权威齐备但时钟漂移 案例对成立 |
| D-10 P-004 度量可操作性 | **部分成立 → NEEDS_EVIDENCE**（RQ5-001） | 代理度量实践中存在，无权威方法论来源；不阻塞升格，operationalization 标缺口 |
| D-11 P-007 结构判别 | **判别成立，候选收窄存活** | seL4（S-118）是真实豁免形态（静态证明闭合时）；不降 property |
| D-12 P-012 非服务端形态 | **成立为形态注释** | RTOS 准入=静态优先级配置（S-113）；Desktop 离线队列实证薄（自认） |
| D-13 H7 复活检验 | **维持降级** | 两轮外部研究未发现 locality 单一机制；H7 保持 demoted |
| D-14 P-010 CRDT | **收窄确认** | S-119：推翻 single-writer 必需性，强化显式语义维度 |

## 3–6. 分类汇总

- 不变存活：P-013；
- 收窄存活：P-001/002/003/004/007/008/009/010/012（收窄 statement 见各 dossier）；
- 合并建议：无（D-04/D-05/D-07 均判独立失败）；D-05 的「权力≤职责」深层同构留 Stage 6 决定是否抽象为 Constitution 条款；
- 降级：P-006 → P-002 的 measurable property/review signal；
- 拒绝：无。

## 7. 因果/机制检验失败的 statement

- P-006 原 statement（metric 主张无独立因果内容）——DEMOTE；
- 其余候选的机制段通过检验（P-004/P-010 的机制措辞问题已在 Stage 4 remediation R4/R5 修正，本轮复核无新问题）。

## 8. GOOD CASES / 误报保护（评测素材登记）

1. SQLite 单进程嵌入式顶级可靠性（S-117）——不得以「无隔离/无分布式机制」报错；
2. supervised daemon 无限运行（S-114/115）——不得报生命周期缺失；
3. GC 托管堆（有 runtime 上限管理，S-116）——不得报无界内存；
4. 依赖文档承诺的 actor per-pair 顺序 / DBMS 隔离语义（S-115 + PostgreSQL 文档 lead）——不得报隐式假设；
5. 隐含界的离线批处理——不得要求显式配额文档；
6. RFC 7568 / PEP 404 型治理化破兼容（S-120/121）——不得报契约破坏；
7. 网关/mesh 承担准入的服务——不得报服务内无降级代码；
8. 同团队单部署单元的内部粗粒度权限——不得报缺细粒度权限；
9. 探索期原型无显式边界——不得报缺模块化；
10. 全局协调一致的广泛变更（统一升级）——不得以变更范围大报结构差（P-006 误报面）。

## 9. 证据家族与跨形态弱点

- SRE/AWS 谱系集中度（P-012）维持；Stage 6 升格时可用规范族（S-090）对冲；
- Fowler/ThoughtWorks 同轨注记生效（该族不再支撑任何 P-*）；
- 单进程/嵌入式形态经 S-114..118/122/123 显著增强；Desktop/browser 形态仍薄（browser 无来源——CH-S-12 遗留，不阻塞）；
- 观测/隐私冲突只有 B 级来源（RQ5-003）。

## 10. 新增证据（S-114..S-123）

全部经 manifest 登记、sources/S-*.md 落盘、含 provenance/tier/verification，且每条注明改变的 attack/D-test：
- S-114 Armstrong thesis → P-001 攻击 1 反例转正面；
- S-115 Erlang Processes 官方 → P-013 判据先例 + P-001 邮箱缝隙；
- S-116 Go GC Guide → P-001 GC 豁免边界 + P-003 good case；
- S-117 SQLite testing → 单进程 GOOD CASE（P-004/D-12）；
- S-118 seL4 → P-007 D-11 收窄；
- S-119 CRDT → P-010 D-14 收窄确认；
- S-120 RFC 7568 / S-121 PEP 404 → P-008 例外条款（两独立族）；
- S-122 Arrakis / S-123 eBPF verifier → P-004 替代保证机制收窄。

Leads（未入 corpus，不改变 disposition）：Hermitage（Kleppmann）、Akka message delivery 文档、Dynamo SOSP 2007、Jepsen TigerBeetle 2025、Leucker & Schallhart 2009、Envoy adaptive concurrency（未终验）、Yanacek load shedding 文（S-050 家族内指针）、PostgreSQL transaction-iso 文档。

## 11. CONTESTED / 未决

- RQ5-001：blast radius 度量方法论（D-10）——NEEDS_EVIDENCE；
- RQ5-002：「执行模型是否提供保证」的机械判定方法（P-013）——NEEDS_EVIDENCE；
- RQ5-003：观测/隐私冲突缺权威来源——NEEDS_EVIDENCE；
- RQ5-004：负载天然有界豁免缺权威来源——NEEDS_EVIDENCE；
- RQ5-005：SQL 隔离级别名义 vs 实际语义（Hermitage lead）——Stage 7 integration/domain 层的提示，非阻塞。
- D-08 的结论为「floor 存在但 scope 有限」，供 Stage 6 Constitution 采用；若 CA 对 floor 范围有不同证据判断，属 CA 裁决。

## 12. Stage 6 reduction 输入

1. 原则集候选：P-001/002/003/004/007/008/009/010/012/013 的收窄 statement（各 dossier「Proposed Narrowed Statement」）；
2. P-006 不进入原则集；其度量思想并入 P-002 operationalization 或 Stage 7 metrics 层；
3. Stage 6 可考虑的 Constitution 级抽象：「权力（故障/信任）与责任相称」（P-004+P-009 深层同构，D-05 分立但上层抽象可行）；「purpose-fitness 评估框架 + 限定 safety floor」（D-08）；「最小充分复杂度」元目标（承 Stage 4）；
4. 重叠风险已清：D-01/02/04/05/06/07/09 全部判分立；
5. 形态 scoped 注释（嵌入式隔离弱化、RTOS 准入、Desktop 薄覆盖）随 Stage 7 domain 层承载。

## 13. 真正需要 owner 决策的问题

**无新增。** P-006 降级后的 metric/property 归宿层（Stage 7 ontology 扩展）为 CA 权限内的已登记延后事项；D-08 floor 表述为 Stage 6 事项。无不可逆/范围/授权级新问题。
