---
id: STAGE4-RECONCILIATION
type: challenger-reconciliation
stage: 4
pass: B
challenger: Codex harness (repository, git, read-back) + GLM 5.3 (semantic boundary analysis)
primary_sha: 958dfcd8ce165546e2dc097de0038311f2ee2226
pass_a_sha: 01b5189a532c1eaa8820324c363f51f6ac798707
baseline: d6a7808611742dda6e2e6f9fa0154b12ae67b4a3
issue: 9
date: 2026-09-18
status: challenger-pass-b
---

# Stage 4 Challenger Pass B — Reconciliation

## 0. 固定输入与方法

- Primary：`research/stage4-principles@958dfcd8`（P-001..P-013、principles/index.md、reports/STAGE4_EXTRACTION.md）；
- Pass A：`challenge/stage4-principles@01b5189a`（V4-01..V4-24 预注册检查、CF-1..CF-5、MF-1..MF-3）；
- Issue #9 Chief Architect checkpoint：OD4-1..OD4-4、CA4-1..CA4-11 已读取并逐项对账；
- 本报告执行 V4-01..V4-24、CF/MF 对账、CA4 评估、候选分类、边界矩阵、RQ3 重判；
- 不修改 Primary P-*；不执行 Stage 5 反例战役；不起草 Constitution。

总体判定先行：**PASS_WITH_REMEDIATION**。Primary 的候选集质量高（机制/边界/证伪计划纪律良好、词汇 gate 合规、lineage 大体诚实），但存在 2 个已由 CA 裁定的 category error（P-011、P-005）、1 处 NEEDS_EVIDENCE 证据违规使用（P-008 expand-contract）、2 处 mechanism 措辞修正（P-010、P-004）、2 个 statement 重述条件（P-007、P-013）。全部 remediation 是有界的措辞/移除级操作，无需结构性返工。

## 1. V4-01..V4-24 逐项执行

| ID | 判定 | 证据与理由 | 最小修正 |
|---|---|---|---|
| V4-01 | **PASS** | extraction §2 对 H1..H11 全部 13 个假设给出 disposition + 机制理由；H7/H9 未静默丢弃 | 无 |
| V4-02 | **PARTIAL** | H7 降级有落点（Stage 5 假设 + V-014-C 骨架）；H9 降级为 meta-objective 但未点名 Constitution 层，且声称内容「由各候选 Trade-offs 段承载」与 OD4-1 的 Constitution 去向不一致 | H9 disposition 改为 `DEMOTE -> Constitution/meta-objective`（R8） |
| V4-03 | **PARTIAL** | CF-2（→§8.6 P-002↔P-006）、CF-3（→§8.4 P-004↔P-009）、CF-4（H7 降级后消解为 P-002 自身机制）、CF-5（H9 降级）实质处理；**CF-1（P-001↔P-003 共享 scope-ownership→lifetime-bound 机制）完全缺席**于 §8 重叠清单 | 登记 P-001 vs P-003 为新重叠（D-07）；extraction §8 补一行（R8） |
| V4-04 | **PARTIAL** | P-001/P-002 split 有判别案例对（伪分层 vs 单模块多任务）；P-004/P-009 有计划中的判别方向；但 P-005/P-006 split 仅给「决策程序 vs 空间属性」的范畴区分，未给判别案例对 | P-005 移除后 P-005/P-006 split 问题消解；P-002↔P-006 判别已在两文件中登记，保留 |
| V4-05 | **PARTIAL** | MF-2→P-013 显式承接；MF-3→P-003+P-012 显式承接；**MF-1（idempotency family）无显式 disposition**——仅在 P-010/P-013 中作为机制（V-021-B）隐式使用 | 按 OD4-3 在 extraction 补一行：idempotency 记录为 explicit delivery semantics 下的 mechanism/tactic/contract property，不设独立原则（R8） |
| V4-06 | **PARTIAL** | P-001 证据段正确把 S-084..086 归并为「博客→官方采纳链」单族；P-012 厂商集中诚实标注；但 **P-005 把 Fowler 谱系与 ThoughtWorks 演进架构计为两族**（Pass A §5 已裁定同轨道） | P-005 移除后此问题基本消解；extraction §4 家族图对 Fowler/ThoughtWorks 加同轨注记（R8） |
| V4-07 | **PARTIAL** | P-006 单源已诚实 NEEDS_EVIDENCE；P-003/P-009/P-010 族数充足；P-005 以 heuristic 为主的族维持宽 CANDIDATE（移除后消解）；P-011 宽 scope 但自标可证伪性弱（移除后消解） | 移除 P-005/P-011 后其余候选满足「≥2 独立族或明确 scoped」 |
| V4-08 | **PASS** | 全部 13 个 P-* 有 Cross-System-Shape Check；extraction §4 标注 SRE/AWS 同生态集中度警告；P-008 标注 ABI/Desktop 证据缺席；RQ2-014 的偏差数字未重述但偏差被承认 | 无 |
| V4-09 | **PASS** | 独立扫描 13 个文件：consistency→V-010（P-010 带义项后缀）、atomicity 未裸用、authority 带「状态」+V-003-D、compatibility 方向带 V-013-A/B 视角、stateless 带 V-021-H、backpressure 带 V-008-E、context 在 extraction §5 按 V-007-D/V-020-D 处理（OS context-switch 义稳定，风险低）；与 §5 自查一致，未发现裸用 | 无 |
| V4-10 | **PARTIAL** | P-004 frontmatter 与 Distinguish 段正确区分 blast radius（V-021-A 度量）与 failure domain（V-005-E 结构）；但 Mechanism 中「受影响面 ≤ 设计的 failure domain」把结构分组当标量阈值使用（CA4-7 确认） | R5：改为「使故障影响被遏制在预期 failure domain 所界定的 blast radius 内」，两概念保持区分 |
| V4-11 | **PASS** | 全部产物无 virtual threads / structured concurrency alias | 无 |
| V4-12 | **PASS** | P-010 把 source of truth（V-009-B）与状态 authority（V-003-D）作为两个具名维度并列引用，未自动等价；system of record 未使用。CA4-4 指出的是另一问题（一致性强度≠权威强度），见 R4 | 无 |
| V4-13 | **PASS** | P-012 的 Distinguish 段给出 V-008-E/F 方向对照；无 flow control = backpressure 断言 | 无 |
| V4-14 | **PASS** | P-003 statement 以「可说明上限或受控降级」主导，V-021-C 在 frontmatter 与机制中承担组织抽象，failure patterns 段以其统一解释 queue/retry/fan-out/blocking 家族；tactic（V-017-B）显式分离 | 无 |
| V4-15 | **PASS** | H7 整体降级；P-006 引用 V-014-C/V-014-D 且注明 N-8 禁止 Herlihy-Wing 互借；V-014-C 保留为 Stage 5 骨架 | 无 |
| V4-16 | **PASS** | 13/13 有 Falsification Plan，多数含 ≥2 攻击方向；relevant 候选有 cross-shape 攻击面 | 无 |
| V4-17 | **PASS** | 13/13 有 Distinguish From；extraction §3「未升格」清单把 USE/SLO/hedged/circuit breaker/ES/CQRS/strangler 等压回 tactic/metric 层 | 无 |
| V4-18 | **PASS** | extraction §7 BACKFLOW_TRIGGER 表诚实：BT-1 触发、BT-2..4/6 给出不触发理由、BT-5 弱触发；无静默填坑 | 无 |
| V4-19 | **PARTIAL** | 无凑数候选；但 P-011/P-005 违反 principle-vs-not 过滤器（CA4-1/2 已裁定 category error），P-006/P-007/P-013 附条件 | R1/R2 移除；R6/R7 条件重述 |
| V4-20 | **PASS** | 13/13 frontmatter vocabulary_refs 非空且与正文引用一致 | 无 |
| V4-21 | **CHECK_INVALID** | 该检查按字面要求 Primary「采纳或逐条拒绝 Pass A scope-down 清单」——但 Pass A 是盲审，Primary 结构上不可能看到该清单；字面检查无效。实质核验：H4-graded ✓、H7-降级 ✓、H8-条件化 ✓、H6-按运维等级 scoped ✓、H10-形态限定 ✓、H1 floors 留 Stage 5 ✓、H5a 未按 process rule 降级 ✗（已被 OD4-2 裁定） | 逐项对账由本报告 §2/§8 完成；H5a/H1 处置按 OD4-1/2 修正（R1/R2） |
| V4-22 | **FAIL** | P-008 Mechanism：「数据迁移路径（expand/contract 家族）使破坏性变更以并存期完成而非切换瞬间完成」——肯定性因果使用；而 V-021-G 为 NEEDS_EVIDENCE、无一手出处、RQ3-006 open（CA4-3 确认）。同文件 Distinguish/Open Questions 的对冲不能抵消 Mechanism 段的肯定性使用 | R3：删除该句或改写为显式假设（「破坏性变更若需并存期过渡，须显式设计迁移路径；expand-contract 为候选 tactic，V-021-G NEEDS_EVIDENCE/RQ3-006 未回流，不得作因果支撑」） |
| V4-23 | **PASS** | 13/13 具备 Statement/Mechanism/Protects/Applies When/Does Not Necessarily Apply/Failure Patterns/Trade-offs/Distinguish/Evidence/Cross-Shape/Counterexample Plan/Open Questions 六要素齐全 | 无 |
| V4-24 | **PASS** | 全部为 falsification plan（未执行战役）；无 01_CONSTITUTION.md、无 FP-*/T-* 文件、无 ≤20 压缩、无 Agent prompt | 无 |

统计：PASS 14 / PARTIAL 8 / FAIL 1 / CHECK_INVALID 1。

## 2. CF-1..CF-5 对账（vs 实际 13 候选）

| CF | Pass A 假设 | Primary 实际处理 | Pass B 判定 |
|---|---|---|---|
| CF-1 | H2b+H3 部分共享「scope ownership → bounded lifetime」 | P-001/P-003 分立且 §8 重叠清单**未含**此对 | **未对账**——新重叠登记 D-07：结构化取消语义（S-084..086）同时是 ownership 机制与 execution bound 机制；Stage 5 需「owned-but-unbounded vs bounded-but-unowned」判别 |
| CF-2 | H5b ⊂ H7 | H7 整体降级（V-014-C 多机制混合）；P-006 以 NEEDS_EVIDENCE 存活并登记 P-002↔P-006 判别 | **部分对账**——H7 降级后坍缩问题转化为 CA4-9 的 P-006 归属问题；Pass B 判定 P-006 倾向 measurable property of P-002（见 §5） |
| CF-3 | H4+H10 共族分立 | P-004/P-009 分立，双方 Distinguish 登记共构与判别方向 | **对账一致**，与 OD4-4 裁定吻合；D-05 预注册 |
| CF-4 | H2a 是 H7 的管理手段 | H7 降级后 CF-4 消解为 P-002 自身的 Parnas 机制 | **对账完成**（消解） |
| CF-5 | H9 ⊂ H1 双 meta-objective | H9 降级为 meta-objective；H1 保留为 P-011「meta-principle 候选」 | **半对账**——CA4-1/OD4-1 裁定 P-011 亦须移出；CF-5 由 R1/R2 完成闭环 |

## 3. MF-1..MF-3（按 OD4-3 裁定执行）

**MF-1 idempotency under at-least-once**：Pass B 检验「是否缺失更深因果原则」——重复投递下的正确性要求，其因果内容可被 P-010（状态裁决/冲突语义含重复处理，V-021-B 在 P-010/P-013 中作为机制正确使用）与 P-013（重复/时序假设显式化）共同覆盖，残余部分是操作性质地（effect-equivalence）。**结论：同意 OD4-3，记为 non-principle（mechanism/tactic/contract property under explicit delivery semantics）**。缺陷仅为 extraction 缺一行显式 disposition（R8）。

**MF-2 scheduling/priority as correctness**：由 P-013 承接。类别检验（CA4-6）：现 statement「必须显式声明时间与时序假设」是 review/documentation 纪律；但其可分离的因果核心存在——「正确性不得依赖执行模型未提供的时序/顺序保证，隐式依赖在调度扰动/延迟/漂移下产生潜在失效」（S-025/030/031 + S-091 机制背书）。**结论：不整体降级；要求 statement 重述（R7），「声明」降为 operationalization，结构主张升为 statement**。单进程理论锚薄（自认）维持 Stage 5 检验。

**MF-3 capacity/queueing protection**：由 P-003（ex-ante 维度界限）+ P-012（超载行为设计）承接。CA4-8 判别检验（§6 D-04）显示二者可独立失败，无损失覆盖，无需第三原则。**结论：同意 OD4-3，不新增**。

## 4. CA4-1..CA4-11 逐项评估

| CA | Pass B 评估 | 结论/修正 |
|---|---|---|
| CA4-1 P-011 category error | 同意。P-011 是评估公理非因果结构主张；其自认「可证伪性弱」「弹性检验」恰是 principle 过滤器的 broad-aspiration 违规；保护 capability 的机制是「评估锚点」而非结构因果链 | 移出 P-*（R1）；H1 disposition 改 DEMOTE -> Constitution/evaluation frame；product-contract 规则保留为 Constitution 输入 |
| CA4-2 P-005 category error | 同意。主语是「决策值得多少论证/记录」，机制主体在决策流程；cross-shape 段的形态差异（硬件不可逆等）只改变不可逆性输入，不改变其 process 性质 | 移出 P-*（R2）；规则保留为 extraction 中 Stage 8 Decision Playbook 输入 |
| CA4-3 P-008 expand-contract 泄漏 | 确认（V4-22 FAIL）。Mechanism 的肯定性使用与 V-021-G NEEDS_EVIDENCE 冲突 | R3 措辞修正；P-008 因果支撑改为仅 S-044/S-045/S-039/S-042/S-037/S-038 |
| CA4-4 P-010 混淆一致性强度与权威 | 确认。「复制一致性光谱的选择即权威强度的选择」被 corpus 反例驳倒：单写权威+最终一致副本（弱一致+单权威）与多写 CRDT+显式合并语义（强合并语义+多写）均真实存在，两维正交 | R4：Mechanism 改为双维显式（write authority × conflict/consistency semantics），删除等式句 |
| CA4-5 P-007 property 风险 | 部分确认。现行 statement 主体仍是 necessary-property（「不能区分→不能运维」）；但存在可背书的因果重述：「诊断表面是结构分配的——观测点/状态的架构位置决定何者可区分、可归因」（S-055 宽事件的位置论证、S-053 运维理解作为防御层、S-048 SLI 依赖结构先行） | R6：条件重述为 designed diagnostic surfaces 因果主张；若 Stage 5 找不到结构侧判别案例则降级为 required property |
| CA4-6 P-013 reasoning rule 风险 | 部分确认。见 §3 MF-2：因果核心可分离且源背书充分 | R7：statement 重述为结构主张，「声明」降为 operationalization |
| CA4-7 P-004 词汇精度 | 确认（V4-10 PARTIAL）。frontmatter/Distinguish 合规，Mechanism 句把 failure domain 用作标量阈值 | R5 措辞修正 |
| CA4-8 P-003/P-012 判别 | 判别案例可构造（D-04）：①全链有界（容量/队列/重试）但无准入分级——过载时等概率丢弃关键流量（P-012 violated, P-003 满足）；②有准入/降级策略但内部重试维度无界——策略被重试放大击穿（P-003 violated, P-012 满足）。二者可独立失败 | 保持分立；D-04 预注册；不合并 |
| CA4-9 P-006/P-002 与 RQ3-001 | Pass B 判定：P-006 的第二句（「变化传播范围是可观察信号」）是 metric/property 主张，第一句（「好结构使变化集中」）是 P-002 机制的直接后果——独立因果内容单薄（单源 S-001）。倾向 demote 为 P-002 的 measurable property；是否保留 NEEDS_EVIDENCE 候选资格留 Stage 5 D-03 判别 | RQ3-001 在 Stage 4 **不构成 promotion-critical**（见 §7） |
| CA4-10 family 计量 | P-001 正确归并 S-084..086 为单族；P-012/P-013 集中度诚实；P-005 的 Fowler/ThoughtWorks 双族计数是唯一膨胀（移除后消解） | R8 家族图加同轨注记 |
| CA4-11 角色元数据 | 确认。Pass A frontmatter 误标 WorkBuddy | 已修正：challenger: Codex harness + GLM 5.3（本 commit 内完成，challenger 自有产物的元数据修正，不触碰 Primary） |

## 5. 候选分类总表（P-001..P-013）

| ID | 分类 | 附注 |
|---|---|---|
| P-001 Explicit Ownership | **VALID_CAUSAL_CANDIDATE** | 新增 D-07（vs P-003）重叠登记；RQ3-002 保持 NEEDS_EVIDENCE 不触发 |
| P-002 Change-Decision Boundaries | **VALID_CAUSAL_CANDIDATE** | 主攻击面（模块化大样本实证缺）已自认，留 Stage 5 |
| P-003 Bounded Execution | **VALID_CAUSAL_CANDIDATE** | 跨形态最强；Little's Law 平均值限制自认（S-077 尾部维度留 Stage 5） |
| P-004 Failure Containment | **VALID_CAUSAL_CANDIDATE** | + R5 措辞修正；graded 定位正确；度量可操作性留 Stage 5（D-10） |
| P-005 Reversibility Deliberation | **CATEGORY_ERROR** | OD4-2/CA4-2：移出 P-*，保留为 Stage 8 playbook 输入 |
| P-006 Change Locality | **OVERLAP_UNRESOLVED**（附 NEEDS_EVIDENCE） | 倾向 P-002 的 measurable property；D-03 判别后定去留 |
| P-007 Legibility for Operability | **VALID_CAUSAL_CANDIDATE**（附条件） | R6 因果重述为 designed diagnostic surfaces；否则降 property |
| P-008 Contract Preservation | **VALID_CAUSAL_CANDIDATE** | + R3 expand-contract 修正（V4-22 FAIL 的补救） |
| P-009 Trust Minimization | **VALID_CAUSAL_CANDIDATE** | lineage 最强；agent 形态新近性已自标 |
| P-010 Authoritative State | **VALID_CAUSAL_CANDIDATE** | + R4 双维修正；CRDT 收窄边界留 Stage 5（D-14） |
| P-011 Purpose Fitness | **CATEGORY_ERROR** | OD4-1/CA4-1：移出 P-*，去向 Constitution/evaluation frame |
| P-012 Overload Admission | **VALID_CAUSAL_CANDIDATE** | 厂商集中已诚实标注；非服务端实证薄自认（D-12） |
| P-013 Time & Ordering Assumptions | **VALID_CAUSAL_CANDIDATE** + **OVERLAP_UNRESOLVED** | R7 statement 重述；D-02（vs P-001）/D-09（vs P-010）判别 |

## 6. 候选边界矩阵（Stage 5 预注册）

| 对 | 判别案例 a（X 违反 / Y 满足） | 判别案例 b（X 满足 / Y 违反） | 无法判别时 |
|---|---|---|---|
| P-001 vs P-002 | 边界清晰但运行时实体无归属（有界无主 worker 池） | 单模块内任务/状态归属严格但无变化决策边界 | 合并（CA4-9 框架） |
| P-001 vs P-013 | 归属明确但时序假设隐式（重排序下 stale overwrite） | 时序假设全部显式（全序化）但清理归属悬空（孤儿定时器） | stale overwrite 归 P-013，孤儿/泄漏归 P-001 |
| P-002 vs P-006 | 约定俗成内聚代码库：变更局部但无显式边界 | 显式分层边界但变更跨切 feature（P-006 亦违反——需第三态：边界错误轴） | P-006 降为 P-002 的 property/metric |
| P-003 vs P-012 | 全链有界但无准入分级（关键流量等概率被弃） | 有准入降级但重试维度无界（策略被放大击穿） | 合并 |
| P-004 vs P-009 | 低权限组件经共享资源放大故障（信任小、故障权力大） | 故障域隔离良好但权限过宽（横向移动面大） | 按 OD4-4 保持分立，登记共族 |
| P-010 vs P-001 | 权威声明清晰但实体无主（泄漏+权威并存） | 归属清晰但一致性义项未声明（缓存漂移） | 保留分立（裁决语义 vs 归属程序） |
| P-001 vs P-003（新，CF-1） | 有 deadline 的 fire-and-forget：有界无主 | 严格 scope-owned 但 scope 内计算无界：有主无界 | 拆分取消语义归 P-001、资源界限归 P-003 |
| P-013 vs P-010（新） | 全序化序列的重复投递（时序已显式、重复未裁决） | 权威+幂等键齐备但时钟漂移破坏顺序假设 | 保留分立 |

## 7. RQ3-001..006 重判（cleanup 后 promotion-critical 性）

| RQ3 | cleanup 后判定 | 理由 |
|---|---|---|
| RQ3-001 coupling/change-locality | **不推荐 Stage 4 定向回流** | P-006 倾向降为 property；P-002 站在 S-001/S-005/S-109 上不以该源为 promotion 前提。若 owner 决定保留 P-006 候选资格，可在 Stage 5 前以 D-03 结果为条件再议（低优先） |
| RQ3-002 Java StructuredTaskScope | 不触发 | P-001 未主张 Java realization；NEEDS_EVIDENCE 已标 |
| RQ3-003 microservices 正方 | 不触发 | 无任何 P-* 引用微服务收益主张；P-002 反而以 S-109 模块化单体为证 |
| RQ3-004 WASI/capability | 不触发 | P-009 以 S-092/093/096 成立；capability 仅单一形态实例缺口 |
| RQ3-005 UI 主线程权威源 | 弱触发，留 Stage 5 | P-003 核心不依赖 UI 形态（借 S-088 事件循环同构已标注）；跨形态测试前的可选补强 |
| RQ3-006 expand-contract | **cleanup 后不触发** | 正确补救是删除肯定性使用（R3）而非补证；P-008 站在 S-044/S-045 上；缺口留待 Stage 7 tactic 层处理 |

**定向回流总结论：Stage 4 gate 无 promotion-critical 回流项。** RQ3-005 为可选（Stage 5 前），RQ3-001 为条件性（取决于 P-006 去留的 owner 决定）。

## 8. Gate 建议 + 最小 remediation 集

### Gate：**PASS_WITH_REMEDIATION**

依据：V4 统计 14 PASS / 8 PARTIAL / 1 FAIL / 1 CHECK_INVALID；唯一 FAIL（V4-22）是有界措辞修正；两个 category error 已由 CA 预先裁定且有明确落点；候选集的机制纪律、词汇合规、证据诚实度、反例计划完备性整体达标。

### 最小 remediation（全部为 Primary 侧有界操作，由 Chief Architect 授权 Primary 执行）

| # | 对象 | 操作 |
|---|---|---|
| R1 | P-011 | 从 principles/ 移除；H1 disposition 改 `DEMOTE -> Constitution/evaluation frame`；product-contract 规则保留为 Constitution 输入（OD4-1） |
| R2 | P-005 | 从 principles/ 移除；H5a disposition 改 `DEMOTE -> Decision Playbook`；规则文本保留于 extraction 作 Stage 8 输入（OD4-2） |
| R3 | P-008 Mechanism | 删除/假设化 expand-contract 因果句（CA4-3，V4-22） |
| R4 | P-010 Mechanism | 「一致性光谱选择即权威强度选择」改为 write authority × conflict/consistency semantics 双维表述（CA4-4） |
| R5 | P-004 Mechanism | 「受影响面 ≤ 设计的 failure domain」改为保持两概念区分的遏制表述（CA4-7） |
| R6 | P-007 Statement | 重述为 designed diagnostic surfaces 因果主张（CA4-5；条件性保留） |
| R7 | P-013 Statement | 「必须显式声明」降为 operationalization，statement 升为「正确性不得依赖执行模型未提供的时序/顺序保证」（CA4-6） |
| R8 | extraction report | 四处补写：H9 → Constitution/meta-objective 显式化；MF-1 idempotency non-principle 一行；P-001↔P-003 重叠一行；Fowler/ThoughtWorks 同轨注记 |
| R9 | （已完成）Pass A 报告元数据 | challenger 角色修正为 Codex harness + GLM 5.3（CA4-11，本 commit） |

### 候选移除/降级汇总

- 移除：P-011（→Constitution/evaluation frame）、P-005（→Decision Playbook 输入）；
- 条件保留：P-007（因果重述，否则降 required property）、P-013（statement 重述）；
- 倾向降级待判别：P-006（→P-002 的 measurable property/metric，D-03 后定）；
- 修正后保留：P-004/P-008/P-010（mechanism/statement 措辞级）；
- 无条件保留：P-001/P-002/P-003/P-009/P-012。

## 9. Stage 5 预注册判别集

| ID | 判别内容 | 失败后果 |
|---|---|---|
| D-01 | P-001 vs P-002 案例对（§6） | 合并 |
| D-02 | P-001 vs P-013：stale overwrite 归因 | 归属规则重划 |
| D-03 | P-002 vs P-006：可度量子 vs 划分依据 | P-006 降 property |
| D-04 | P-003 vs P-012：有界无策略 vs 有策略无界 | 合并 |
| D-05 | P-004 vs P-009：故障权力≠信任权力案例对 | 按 OD4-4 保持分立 |
| D-06 | P-010 vs P-001：裁决语义 vs 归属程序 | 分立维持 |
| D-07 | P-001 vs P-003（CF-1 新增）：取消语义 vs 资源界限 | 语义归 P-001、界限归 P-003 |
| D-08 | safety floor 存在性与范围（原 P-011 弹性检验的 Constitution 化转型） | Constitution 公理加限定 |
| D-09 | P-013 vs P-010：顺序保证 vs 状态裁决 | 分立维持 |
| D-10 | P-004 blast radius 度量可操作性 | 降 heuristic |
| D-11 | P-007 反例搜索：低可观测高可靠系统（形式验证嵌入）+ 因果重述判别 | 降 required property |
| D-12 | P-012 非服务端实证（desktop 离线队列/embedded 调度准入） | 形态 scoped |
| D-13 | H7 复活检验：locality 是否存在单一机制（通信成本超线性等） | 维持降级 |
| D-14 | P-010 CRDT 收窄：「多写无裁决但显式合并语义」边界 | 收窄 statement |

## 10. Genuine owner decisions（新增）

Stage 4 gate 层面**无阻塞性新增 owner 决策**——两个 category error 与回流政策均已由 OD4-1..4 裁定，本报告仅执行。两项非阻塞延后决策供登记：

1. **可度量子属性的归宿层**：P-006 若按建议降为 measurable property/metric，Stage 7 知识架构需要一个 metrics/properties 层收纳此类「结构质量的可观察信号」——这是 ontology 级扩展，按 plan §8.3/§12.5 需 CA 显式评审、owner 认可 irreversible 变更（延后至 Stage 7 前）；
2. **safety floor 的 Constitution 表达**：D-08 的结果将决定 Constitution 评估公理是否携带非协商底线限定及其范围（延后至 Stage 6）。

## 11. 元声明

- 本报告对账对象为固定 SHA（Primary 958dfcd8 / Pass A 01b5189），对账过程不修改任何 Primary P-* 文件；
- 唯一触碰的 Pass A 产物是 challenger 字段的角色元数据修正（CA4-11 明确要求，属 challenger 自有产物）；
- 未执行 Stage 5 反例战役（全部为预注册判别计划）；未起草 Constitution；未创建 FP-*/T-*；
- V4-21 标记 CHECK_INVALID 的理由：该检查的字面对象（Primary 逐条回应 Pass A 清单）在盲审结构下不可能成立，实质核验已在本报告 §2/§8 内完成；
- 本报告判定为 challenger 立场，最终 gate 与 remediation 授权归 Chief Architect。
