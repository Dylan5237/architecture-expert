---
id: REPORT-STAGE5-KIMI
type: stage-report
stage: 5
author: kimi-k3 (Primary Falsification Researcher)
branch: research/stage5-falsification
date: 2026-09-20
issue: 12
baseline: 05cfea4981c77d9a13520762e2e37244d4079bce
remediation_basis: "Issue #12 CA adjudication R5-1..R5-8 + M5-1..M5-5；challenge/stage5-falsification@d9d6996 (accepted Pass B)"
---
# Stage 5 Falsification Report — 综合（final, 含 remediation）

边界：只做证伪与 disposition 输出；未改 canonical principles/P-*.md；未写 Constitution；未做 Stage 6 reduction。原子 dossier 见 `reports/stage5/P-*.md`（11 份）。immutable-history 已按 baseline `05cfea49` 恢复（S-001..S-113 manifest 记录与 RQ2/RQ3 队列历史原文恢复；Stage 5 追加段 append-only）。

## 1. 11 候选 disposition 矩阵（final）

| 候选 | Final Disposition | 关键收窄点 |
|---|---|---|
| P-001 Explicit Ownership | **NARROW** | GC 豁免仅限 managed-heap reclamation；supervision 是合规机制非普适 invariant；邮箱归接收进程拥有，容量无界归 P-003 |
| P-002 Change-Decision Boundaries | **NARROW** | 事前识别变化轴为适用前提；探索期未知变化轴为 GOOD CASE |
| P-003 Bounded Execution | **NARROW** | lifetime 可 indefinite；per-work execution/wait/retention/retry/queue/concurrency/memory/fan-out 仍需有效界或治理策略 |
| P-004 Failure Containment | **SURVIVES** | graded/outcome-oriented 保留；替代保证机制证据维度特定化（Arrakis 仅 I/O 保护维度）；eBPF 不作 admitted 证据 |
| P-006 Change Locality | **DEMOTE** | 降为 P-002 关联 measurable property / review signal；不触发 RQ3-001 |
| P-007 Designed Diagnostic Surfaces | **NARROW** | question-relative：未被静态证明消解的 operational questions 需可获得证据；隐私/安全为 trade-off（无标量替代律） |
| P-008 Contract Preservation | **NARROW** | 按消费方独立性分级；更高优先级要求（RFC 7568）或治理化迁移（PEP 404/Linux 内部接口）可显式破兼容 |
| P-009 Trust Minimization | **NARROW** | 强制点限定在不可信输入/跨权限/外部集成/agent 动作边界 |
| P-010 Authoritative State | **SURVIVES** | R4 双维 statement 原样存活；CRDT 为确认/GOOD CASE |
| P-012 Overload Admission | **NARROW** | 准入位置是架构决策；负载天然有界豁免（NEEDS_EVIDENCE 级）；priority scheduling ≠ admission control |
| P-013 Execution-Model-Honest Correctness | **SURVIVES + TAUTOLOGY_RISK** | 保留 assumed≠provided 经验判别类与 GOOD CASE 保护；Stage 6 若坍缩为同义反复则届时降级 |

## 2. D-01..D-14 最终结果（accepted Pass B，未静默升级）

| D | 结果 |
|---|---|
| D-01 P-001 vs P-002 | DISTINCT |
| D-02 P-001 vs P-013 | DISTINCT |
| D-03 P-002 vs P-006 | P-006 NOT INDEPENDENT AS CAUSAL PRINCIPLE → DEMOTE |
| D-04 P-003 vs P-012 | DISTINCT |
| D-05 P-004 vs P-009 | DISTINCT（「权力≤职责」深层同构记为 Stage 6 Constitution 级抽象候选） |
| D-06 P-010 vs P-001 | DISTINCT |
| D-07 P-001 vs P-003 | DISTINCT（取消语义归 P-001、资源界限归 P-003） |
| D-08 safety floor | CONTEXTUAL ONLY（「non-negotiable regulatory/safety/security constraints, when applicable, bound the trade space」——不得主张普适 safety floor） |
| D-09 P-013 vs P-010 | DISTINCT |
| D-10 P-004 度量可操作性 | NEEDS_EVIDENCE（RQ5-001） |
| D-11 P-007 结构判别 | NARROW / claim-scoped |
| D-12 P-012 非服务端形态 | NEEDS_EVIDENCE（priority scheduling ≠ admission control；RQ5-004） |
| D-13 H7 复活检验 | NOT RESURRECTED |
| D-14 P-010 CRDT | FRAMEWORK HOLDS |

## 3. GOOD CASE / false-positive register（first-class eval fixture 输入）

以下每条为「表面可疑但架构合法」的判别边界，供未来 Agent eval 的 false-positive fixture 使用（格式：形态 → 不得报 → 依据/限定）：

1. **OTP supervised daemon 无限运行**（S-114/S-115）→ 不得报生命周期/ownership 缺失；supervision 是合规 ownership 机制，但不得当普适 invariant 引用。
2. **GC 托管堆 + runtime 软预算**（S-116 GOMEMLIMIT）→ 不得报无界内存；GC 只豁免 managed-heap 回收维度的 ownership。
3. **探索期/未知变化轴的无边界原型**（P-002）→ 不得报缺模块化；变化轴未知时无边界合法。
4. **lifetime indefinite 但 per-work 有界的流处理/daemon**（P-003）→ 不得报「无限运行」；界按 per-work 资源维度判定。
5. **SQLite 单进程嵌入式顶级可靠性**（S-117）→ 不得以「无隔离/无分布式机制」报错；仅 testing 页支持范围。
6. **Arrakis 硬件下放的 I/O 保护**（S-122，维度限定）→ 不得报「缺进程边界隔离」；但不得外推为硬件替代所有故障遏制。
7. **广泛但健康的协调变更**（统一升级/全局迁移）→ 不得以变更范围大报结构差（P-006 误报面；P-006 已非原则）。
8. **seL4 型静态证明系统**（S-118，显式假设集内）→ 不得按服务端遥测标准报观测缺失；假设集外的 operational questions 不在豁免内。
9. **RFC 7568 型治理化安全破除 / PEP 404 型治理化生态演进**（S-120/S-121）→ 不得报契约破坏；更高优先级要求或治理化迁移显式主导。
10. **Linux 内核内部接口不稳定 + syscall 稳定**（S-124）→ 不得报内部接口不兼容；消费方独立性分级合法；不得泛化为内部 API 应不稳定。
11. **封闭/粗粒度信任的单用户本地形态**（P-009）→ 不得报缺细粒度内部权限（supply chain 边界除外）。
12. **CRDT / log / local-first 形态**（S-119/S-107）→ 不得报「无中心权威」；显式合并语义是合法形态。
13. **网关/mesh/path 级准入的服务**（P-012）→ 不得报服务内无降级代码；准入位置是架构决策。
14. **模型真正保证的运行时语义**（actor per-pair 顺序、non-preemptive segments、具体 DBMS 承诺的隔离语义，S-115 先例）→ 不得报隐式时序假设；assumed≠provided 判据仅抓「依赖实现巧合」。

## 4. 证据家族与跨形态弱点

- SRE/AWS 谱系集中度（P-012）维持，规范族（S-090）可对冲；
- 单进程/嵌入式经 S-114..118/122 增强；Desktop/browser 形态仍薄（不阻塞）；
- S-119 HAL 访问受限如实记录（bot-blocked + canonical identity + DOI）；
- S-123（eBPF verifier）**已移除为 LEAD_ONLY**（OD5-6），ID 不复用；不作 admitted disposition-changing 证据；
- SC-08（Sandi Metz）REJECT_UNVERIFIED（OD5-3）；SC-05 LEAD_ONLY，不逆转 Stage 2 Raymond Chen adjudication。

## 5. 新增证据（final admitted Stage 5 sources）

**S-114, S-115, S-116, S-117, S-118, S-119, S-120, S-121, S-122, S-124**（共 10 条；全部 claim-scoped 修正完成，无 related_rq 字段，manifest 已登记）。

## 6. RQ5 分类（不关闭、不改写）

| ID | 分类 | Stage 6 blocker? |
|---|---|---|
| RQ5-001 blast radius 度量方法论 | non-blocking operationalization / Stage 7 metrics backlog | 否 |
| RQ5-002 保证机械判定 | non-blocking operationalization | 否 |
| RQ5-003 观测/隐私权威源弱 | non-blocking trade-off / Stage 7 domain backlog | 否 |
| RQ5-004 负载天然有界豁免无源 | non-blocking scope/operationalization | 否 |
| RQ5-005 SQL 隔离名义 vs 实际 | Stage 7 integration/domain backlog | 否 |

**没有任何 RQ5 是 Stage 6 research blocker。**

## 7. Stage 6 reduction 输入（计数已修正）

**Stage 6 接收 10 个 surviving candidates：**

- 7 NARROW：P-001, P-002, P-003, P-007, P-008, P-009, P-012；
- 2 SURVIVES：P-004, P-010（Stage 4 修正版 statement 原样）；
- 1 SURVIVES + TAUTOLOGY_RISK：P-013（不混入 NARROW 计数；reduction 时若坍缩为同义反复则届时降级）；
- 1 DEMOTE：P-006——**不进入 principle reduction**，其度量思想并入 P-002 operationalization 或 Stage 7 metrics 层。

Constitution 级抽象候选：「权力（故障/信任）与责任相称」（D-05）；「purpose-fitness 评估框架 + CONTEXTUAL ONLY 的 regulatory/safety/security 约束限定」（D-08）；「最小充分复杂度」元目标。GOOD CASE register（§3）直接作为 eval false-positive fixture 输入。重叠风险已清：D-01/02/04/05/06/07/09 全部 DISTINCT。

## 8. 真正需要 owner 决策的问题

**无新增。** P-006 降级后的 metric/property 归宿层（Stage 7）、D-08 限定表述（Stage 6）均为已登记的延后 CA 事项。
