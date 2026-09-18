---
id: REPORT-STAGE3-KIMI
type: stage-handoff
stage: 3
author: kimi-k3 (Primary Researcher / Vocabulary Synthesizer)
branch: research/stage3-vocabulary
date: 2026-09-18
remediated: 2026-09-18
remediation_basis: "Issue #6 CA adjudication R-1..R-11 + Origin 规则；challenge/stage3-codex-glm@7465d82；final re-gate M1/M3"
issue: 6
evidence_baseline: "Stage 2 accepted corpus (S-001..S-113, source-manifest.yaml)"
---
# Stage 3 交接报告 — Vocabulary Normalization (Kimi)（v2，含 remediation）

## 产物

- `02_VOCABULARY.md` v2 — 20 个 mandatory collision families（V-001..V-020）+ 8 个补充词条（V-021-A..H）+ 16 条归一裁决登记（N-1..N-16）。

## Remediation 记录（R-1..R-11 + M1）

| R | 内容 | 落点 |
|---|---|---|
| R-1 | structured concurrency 专门词条；nursery/CoroutineScope/task group 为 platform realizations 非 alias；Virtual Threads 显式排除；StructuredTaskScope NEEDS_EVIDENCE | V-007-E |
| R-2 | 删除 fault tolerance > resilience 全序；改 failure-model-relative，重叠但无全局强弱 | V-005-C/D + N-13 |
| R-3 | C4 component 不可独立部署（container 注记）；service 定义限定 distributed 语境；bare service 保持 CONTEXT_QUALIFIED | V-002-B/C |
| R-4 | backward/forward compat 翻转为 CONTEXT_QUALIFIED，强制 reader/writer 视角 | V-013-A/B |
| R-5 | V-010 挂 RQ2-004；新增 transaction atomicity 词条；atomic consistency 降为 linearizability 历史/context-specific 术语并禁止混淆 | V-010-A / V-011-B / V-011-E + N-11 |
| R-6 | backpressure 全链路限定（S-090）+ actor mailbox 反例（S-081）+ backpressure≠load shedding 方向对照 + flow control 降为 related term | V-008-E |
| R-7 | modular monolith 补「部署单元≠领域/组织边界」（S-109）；workflow 拆 agent-orchestration vs business-process（S-037/S-038） | V-019-B / V-020-B + N-15 |
| R-8 | SoT 变体登记（SSOT/system of record/authoritative state，非同义）；S-105 vendor-scoped owner 语义保留 | V-009-B |
| R-9 | 新增 stateless 消歧（REST S-039 vs LLM-call S-103，机制禁止互借）；S-087 用于 scalability≠单任务更快 | V-021-H / V-006-D |
| R-10 | 删除「无 timeout 即无界」绝对化——缺任何有效时间界才 potentially unbounded；cancellation 拆 RPC 传播（S-042）vs structured-scope（S-084..086） | V-008-A/C |
| R-11 | Strangler 与 expand-contract 拆开；S-011 只支撑 Strangler；expand-contract 标 NEEDS_EVIDENCE 且无来源 | V-021-F/G；V-013-C 不再引 S-011 |
| M1 | V-019-D EDA 降为 NEEDS_EVIDENCE（S-040/S-041 仅相邻证据）；不新增收益主张 | V-019-D + N-16 |

## Origin / META 变更

使用契约第 7 条新增 Origin 规则：默认 `SOURCE_NORMALIZED`；显式标注项：
- `PROJECT_DEFINED`：V-001-B（design 约定）、V-004-C（required property）、V-007-D（execution context）、V-020-C（harness）、V-020-E（progressive disclosure）、V-021-C（unboundedness）；
- `PROJECT_META`：V-017 全族（tactic/pattern/mechanism/principle/heuristic 操作定义）、V-018 全族（证据元语言，OD-1 隔离保持）。

## Stage 4 lexical gate（OD-4 落地，对后续所有 P-* 生效）

后续任何 P-* 文件使用以下高风险词时，**必须限定具体义项或显式引用对应 V-* 词条**，违反即 gate fail：

- consistency → 必须带 ACID/CAP/replica/cache 后缀（V-010）；
- atomicity / atomic → 必须带 transaction 或 consistency(CAP) 后缀（V-011-E）；
- authority → 必须指明状态权威 / 安全 authz / authority tier（V-003-D / V-016-D / V-018-A）；
- isolation → 必须带 transaction / failure / process 限定（V-011-C / V-005-E）；
- context → 必须指明 DDD bounded / execution / LLM 工程义（V-002-E / V-007-D / V-020-D）；
- compatibility 方向 → 必须带 reader/writer 或 producer/consumer 视角（V-013-A/B）；
- container → 必须带 C4 或 OS/Docker 限定（V-002-B 注记，N-14）；
- component / service → 必须带语境（C4/SAIP/前端；distributed/应用内/OS）（V-002-B/C）；
- stateless → 必须带 REST 或 LLM-call 后缀（V-021-H）；
- workflow → 必须带 agent-orchestration 或 business-process 后缀（V-020-B）；
- locality → 禁止与 Herlihy-Wing 专用义互借（N-8）；
- resilience / fault tolerance → 禁止无故障模型的强弱排序断言（N-13）。

## 归一纪律声明（未变）

同一词多义不强行统一；无来源支撑的项目词显式标 Origin；vendor/platform 术语带 scope 限定；未提取 Mother Principle；未创建 P-*；未修改 Stage 2 adjudication（review-queue 仅追加 RQ3 回流项）。

## 无法归一的 material collisions（承 v1，状态未变）

1. microservices 收益主张（N-9，CONTESTED + NEEDS_EVIDENCE，RQ2-009）；
2. REST 工业混用（N-7）；
3. locality 通用义机制拆分属 Stage 4（N-8）；
4. architecture 定义三谱系并存（N-3）——严格定义合成是 Stage 4+ 问题。

## 证据缺口登记（见 review-queue RQ3 回流，不重启 Source Collection）

coupling/change-locality 权威专门来源（RQ3-001）、Java StructuredTaskScope 官方文档（RQ3-002）、microservices 正方一手（RQ3-003，承 RQ2-009）、WASI/component-model（RQ3-004）、UI 主线程权威来源（RQ3-005）、expand-contract 一手出处（RQ3-006）。
