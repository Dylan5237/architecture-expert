---
id: REPORT-STAGE2-KIMI
type: stage-handoff
stage: 2
author: kimi-k3 (Primary Researcher)
branch: research/stage2-kimi
date: 2026-09-17
remediated: 2026-09-18
remediation_basis: "Issue #3 CA decision D-B1..D-B3 / R1..R4"
issue: 3
---
# Stage 2 交接报告 — Primary Researcher (Kimi)（含 remediation v2）

## 产物清单

- `source-manifest.yaml` — 113 个来源条目（S-001..S-113），含 provenance / tier / verification / 可选 access_status/canonical_url/verification_note/evidence_marker
- `sources/index.md` + `sources/S-*.md` — 113 份高密度来源笔记
- `review-queue.yaml` — 14 项，含 CH-S-01..12 逐条 disposition 表（RQ2-013）

## 统计（以 source-manifest.yaml 为单一事实源重算，2026-09-18）

- 来源总数：**113**（S-001..S-113；sources/ 目录另含 index.md，共 114 文件）
- Tier：**A 77 / B 33 / C 3**（S-069 由 B 降为 C；新增 S-112/S-113 为 B）
- verification：**direct-open 50 / search-cross-verified 50 / offline-publication 12 / needs-reverify 1**（仅 S-069）
- access_status 受影响条目：moved 3（S-032/060/105/106 中 4 条：S-032、S-060、S-105、S-106）/ bot-blocked 2（S-027、S-053）/ unresolved 1（S-069）/ offline-only 1（S-079）
- postmortem 8 篇 + 聚合索引 2 个 + historical-background 1 个（S-069）

## 覆盖矩阵（18 个强制域；remediation 后）

| # | 域 | 主要来源 | 状态 |
|---|---|---|---|
| 7.1 | Fundamentals | S-001/002/003/004/005/007/012/013 | covered |
| 7.2 | Quality Attributes | S-005/008/006 | covered |
| 7.3 | Runtime/Execution | S-087/088/089/080/081/112/113 | covered |
| 7.4 | Concurrency | S-080..S-086/090/091 | covered |
| 7.5 | Performance | S-070..S-078 | covered |
| 7.6 | Resource Budgets | S-050/052/090/088/113 | covered（间接为主，见 G4） |
| 7.7 | Failure Model | S-047/048/049/053/059..065 | covered |
| 7.8 | Failure Isolation | S-047/050/056/069(背景) | covered |
| 7.9 | Distributed Systems | S-023..S-031/077 | covered |
| 7.10 | State/Data | S-032..S-037/040/041/046 | covered |
| 7.11 | API/Integration | S-039/042/043/044/045/038 | covered |
| 7.12 | Lifecycle/Ownership | S-084/085/086/062/091 | covered（跨域分散，见 G4） |
| 7.13 | Security | S-092..S-096/110 | covered |
| 7.14 | Observability | S-048/049/055/058 | covered |
| 7.15 | Scalability | S-074..S-079/023 | covered（USL 标 NEEDS_EVIDENCE） |
| 7.16 | Evolvability | S-010/011/018/020/044/045 | covered |
| 7.17 | Decision Making | S-006/014/015/021/009 | covered |
| 7.18 | Communication | S-016/017/022/009 | covered |

形态覆盖（RQ-A 12 形态）：Backend/Distributed/DB-heavy 强；Mobile S-105、Desktop **S-112（新增正向权威）**、Embedded **S-104+S-113（双锚点）**、Local-first S-107、Monolith S-108/109；Apple 负结果 S-106（仅覆盖观察）。browser/runtime 与 single-process 专用来源：本轮不收录，disposition 见 RQ2-013（CH-S-12 rejected this cycle；CH-S-01/02 needs_evidence）。

## Remediation 记录（R1–R4）

- R1：S-078 DOI 修正为 10.1145/3232559；S-032 换原文 PDF 直链；S-060/S-105 canonical 更新；S-106 重选在世 URL 并收回超出页面支持的表述；S-069 有界考古后降级 historical-background（D-B2）。
- R2：全部统计从 manifest 重算（原 handoff 的 111/78/30/3、38/9 等口径已更正）；RQ2-001 refs 与 manifest 对齐。
- R3：CH-S-01..12 disposition 表落盘（RQ2-013）；Desktop 补 S-112、Embedded 补 S-113。
- R4：S-079 结构化 `evidence_marker: NEEDS_EVIDENCE`，RQ2-006 关联保持。

## Material gaps / conflicts（详见 review-queue.yaml）

G1 Embedded 已缓解（S-104+S-113），AUTOSAR/ISO 26262 仍 NEEDS_EVIDENCE；G2 Desktop 已缓解（S-112），Apple 侧负结果保留；G3 微服务正方论证不对称（RQ2-009）；G4 Boundedness/Lifecycle 无专著级锚点；冲突登记 RQ2-004/005/006/007/011；vendor-bias RQ2-008；持续风险 RQ2-014（例证基率/DDIA 2e/postmortem 幸存者偏差）。

## Stage 2 自评 vs 验收标准

- 每域有可信证据或显式缺口：满足。
- provenance 可脱离聊天重放：满足。
- 主要主张不单靠单一弱来源族：满足（USL/S-069 已结构化降级）。
- 矛盾保留：满足。
- 形态多样性：Desktop/Embedded 从 0/1 提升至 1/2 锚点；browser/single-process 有显式 disposition。
- 未夹带 Stage 3 工作：满足。
