---
id: REPORT-STAGE4-KIMI
type: stage-report
stage: 4
author: kimi-k3 (Primary Researcher / Principle Extractor)
branch: research/stage4-principles
date: 2026-09-18
issue: 9
evidence_baseline: "Stage 2 corpus (S-001..S-113) + Stage 3 sealed vocabulary (02_VOCABULARY.md v2)"
---
# Stage 4 Extraction Report — Principle Extraction (Kimi)

边界声明：本轮只做 Extract → Normalize → Compare。未做 Stage 5 完整证伪（每个候选只有 falsification plan）；未写 01_CONSTITUTION.md；未压缩至 ≤20；未创建 FP-*/T-*；未写 Agent Prompt。全部 P-* 遵守 Stage 3 lexical gate。

## 1. 候选清单

| ID | 候选 | 来源假设 | 状态 | 证据家族独立性 |
|---|---|---|---|---|
| P-001 | Explicit Ownership | H2b | CANDIDATE | 强（纲领+双平台契约+航天事故+监管文件） |
| P-002 | Change-Decision Boundaries | H2a | CANDIDATE | 强（1972 理论+SEI+企业实证） |
| P-003 | Bounded Execution | H3 | CANDIDATE | 很强（定理+双云厂商+规范+四事故+双运行时） |
| P-004 | Failure Containment ∝ Responsibility | H4 | CANDIDATE | 强（模式专著+云实践+三事故+安全科学） |
| P-005 | Reversibility-Proportional Deliberation | H5a | CANDIDATE | 中（全 heuristic 族——升级弱点） |
| P-006 | Change Locality | H5b | **NEEDS_EVIDENCE**（RQ3-001） | 弱（单源 S-001） |
| P-007 | Legibility for Operability | H6 | CANDIDATE | 强（双厂商谱系+标准+理论+监管实证） |
| P-008 | Contract Preservation | H8 | CANDIDATE | 强（规范级+论文+平台+DB 谱系） |
| P-009 | Trust Minimization | H10 | CANDIDATE | 很强（1975 理论+政府标准+厂商方法+社区标准+平台契约） |
| P-010 | Authoritative State | H11 | CANDIDATE | 强（DB 理论+日志谱系+分布式实践+local-first） |
| P-011 | Purpose Fitness | H1 | CANDIDATE（meta-principle 候选） | 强（SEI+ISO+Brooks），但可证伪性弱——Stage 5 重点 |
| P-012 | Overload Admission & Graceful Degradation | 证据新增 | CANDIDATE | 强但厂商集中（SRE/AWS 谱系 + 规范 + 事故） |
| P-013 | Explicit Time & Ordering Assumptions | 证据新增 | CANDIDATE | 强（分布式理论+平台契约+事故）；单进程理论锚较薄 |

候选总数：**13**（无凑数目标；证据不支持的已降级而未生成 P-* 垃圾文件）。

## 2. H1..H11 disposition 表

| H | Disposition | 落点 | 理由 |
|---|---|---|---|
| H1 Purpose Fitness | **retain**（作 meta-principle 候选） | P-011 | 其余原则的评价框架；Stage 5 检验其可证伪性 |
| H2a Explicit Boundaries | **retain + narrow** | P-002 | 收窄为「按变化决策划分」的 Parnas 机制；无变化依据的边界不保护属性 |
| H2b Explicit Ownership | **retain** | P-001 | 证据最跨形态 |
| H3 Bounded & Predictable Execution | **retain** | P-003 | 「无 timeout 即无界」的绝对化已按 R-10 修正为「缺任何有效时间界」 |
| H4 Failure Containment | **retain + narrow** | P-004 | 「故障权力≤职责」明确为 graded，非绝对律；隔离成本可超收益的形态限定 |
| H5a Reversibility | **narrow** | P-005 | 从「可逆性原则」收窄为「不可逆性分配论证深度」的决策程序主张 |
| H5b Change Locality | **retain as NEEDS_EVIDENCE** | P-006 | 单源；升级依赖 RQ3-001 补源 |
| H6 Legibility/Operability | **retain** | P-007 | SRE/Majors 两谱系并存已按 N-6 处理 |
| H7 Locality | **demote**（不生成 P-*） | — | V-014-C：多机制共同倾向而非单一机制；且与 Herlihy-Wing 专用义冲突（N-8）。作为 Stage 5 待检验假设保留于 V-014-C 骨架 |
| H8 Compatibility | **retain + rename** | P-008 | 重命名为 Contract Preservation，显式包含「不得静默破坏」的行为面与方向视角纪律 |
| H9 Controlled Complexity | **demote to meta-objective**（不生成 P-*） | — | 「最小充分复杂度」是评价目标而非因果主张：它不说什么结构在什么机制下保护什么属性，而是其他原则的代价侧约束。若强行作原则会违反 principle 过滤器（broad aspiration）。其内容已由各候选的 Trade-offs 段承载 |
| H10 Trust Minimization | **retain** | P-009 | — |
| H11 Authoritative State | **retain + narrow** | P-010 | 限定「可变状态+并发/多副本/缓存」适用面；CRDT 收窄边界待 Stage 5 |

## 3. Merge / Split / Narrow / Reject 推理

- **Split**：H2 拆 P-001/P-002（ownership 与 boundary 判别案例对存在：有边界无所有权的伪分层、有所有权无边界的单模块多任务）；H5 拆 P-005/P-006（决策程序 vs 结构空间属性）。
- **Narrow**：H4（graded 化）、H5a（程序化）、H8（行为面+视角纪律）、H11（适用面限定）。
- **Reject/Demote**：H7（多机制混合，无单一因果链——弹性解释风险）、H9（元目标非因果主张）。
- **新增（证据驱动）**：P-012（SRE/AWS/规范/事故四族共同指向的超载准入主张，H1..H11 未覆盖——原假设集的真实盲区）；P-013（Lamport/FLP/DLS + 结构化并发 + Pathfinder 共同指向的时序假设显式化，原假设集只有隐含覆盖）。
- **未升格**（防伪装原则的清单项）：USE method（metric/方法论）、SLO（metric）、hedged requests（tactic）、circuit breaker/bulkhead（tactic）、event sourcing/CQRS（tactic）、strangler/expand-contract（tactic，后者 NEEDS_EVIDENCE）、REST/CQRS/microservices（风格标签，V-019 族）、「可用性很重要」（属性）。

## 4. Evidence-family map（独立性判断）

- 定理族：S-024/025/026/028/030/031/072/073/074/075（P-003/P-010/P-013）
- SEI/ISO 族：S-005/006/008/019（P-002/P-011）
- SRE/AWS 族：S-048/049/050/052（P-003/P-004/P-007/P-012）——**同生态集中度警告**（RQ2-008 纪律）
- 事故实证族：S-059..065/091/062（P-003/P-004/P-007/P-012/P-001/P-013）
- 平台契约族：S-084..090/105/112/113（P-001/P-003/P-009/P-013；platform-normative 纪律）
- 安全标准族：S-092/093/096/110（P-009）
- DB/集成谱系：S-032..046（P-008/P-010）
- Fowler/ThoughtWorks 族：S-010/011/014/018/020（P-005）——heuristic 集中

独立性风险：P-005 全 heuristic；P-012 厂商集中；P-006 单源。其余候选 ≥3 独立族。

## 5. Candidate-to-vocabulary map（lexical gate 合规自查）

全部 P-* 检索高风险词并挂 V-*：consistency→V-010（P-010）；atomicity→V-011-E（P-010 未裸用）；authority→V-003-D（P-010）；isolation→V-005-E/V-011-C 分义（P-004/P-010）；context→V-007-D/V-020-D 分义（P-001/P-013）；compatibility 方向→V-013-A/B（P-008）；container/component/service→V-002（P-002 等处）；stateless→V-021-H（P-001）；workflow→未裸用；locality→V-014-C + N-8 禁止互借（P-006）；resilience/fault tolerance→V-005-C/D 无排序断言（P-004/P-007/P-012）。**未发现裸用。**

## 6. 独立支撑不足的候选

- P-006（NEEDS_EVIDENCE，单源 + RQ3-001）；
- P-005（全 heuristic 族，无受控实证——升 stable 前需实证补强或接受 heuristic 定位）；
- P-012（厂商谱系集中，需非厂商实证）；
- P-011（可证伪性弱点——Stage 5 的弹性检验）。

## 7. BACKFLOW_TRIGGER 清单

| Trigger | 缺口 | 影响 |
|---|---|---|
| BT-1 → RQ3-001 | coupling/change-locality 权威源 | P-006 的 scope 与升级直接依赖；**触发** |
| BT-2 → RQ3-002 | Java StructuredTaskScope | P-001 的 Java realization 完整性；不阻塞候选存在（标 NEEDS_EVIDENCE 即可），不触发 |
| BT-3 → RQ3-003 | microservices 正方一手 | 本轮无 P-* 引用微服务收益主张（V-019-C 缺口在场即合规）；不触发 |
| BT-4 → RQ3-004 | WASI/capability | P-009 的 capability 形态支撑；候选以 S-092/093/096 成立，不触发 |
| BT-5 → RQ3-005 | UI 主线程权威源 | P-003 的 UI 形态例证（当前借 Node 事件循环同构）；Stage 5 跨形态测试前建议补；**弱触发** |
| BT-6 → RQ3-006 | expand-contract 一手出处 | P-008 不以 expand-contract 为唯一机制（S-044/045 已支撑兼容面）；不触发 |

## 8. 留给 Stage 5 的重叠判别清单

1. P-003 ↔ P-012：有界执行 vs 超载准入——判别案例对已写入两文件 Distinguish From；
2. P-001 ↔ P-002：ownership vs boundary；
3. P-001 ↔ P-013：stale overwrite 的归因归属（所有权不明 × 时序隐式）；
4. P-004 ↔ P-009：故障权力≤职责 vs 信任权力≤职责——深层同构「权力与责任相称」，若判别失败应合并为更深层原则；
5. P-008 ↔ evolvability 属性（V-013-E）：机制主张 vs 属性的边界；
6. P-002 ↔ P-006：划分依据 vs 度量属性；
7. P-011 的弹性检验（是否能合理化一切）；
8. H7 复活检验：若 Stage 5 找到 locality 的单一机制（如「通信成本超线性」），可重新升格。

## 9. 真正需要 owner 决策的问题

**无新增。** 所有证据依赖均已按 NEEDS_EVIDENCE/BACKFLOW_TRIGGER 登记，属 Chief Architect 的定向补源授权范围（非 owner 级）。H9 降级为 meta-objective、H7 降级为假设，是本项目内的证据裁决，可由 CA 复核推翻，不构成 owner 决策。
