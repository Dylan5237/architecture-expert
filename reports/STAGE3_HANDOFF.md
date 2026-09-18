---
id: REPORT-STAGE3-KIMI
type: stage-handoff
stage: 3
author: kimi-k3 (Primary Researcher / Vocabulary Synthesizer)
branch: research/stage3-vocabulary
date: 2026-09-18
issue: 6
evidence_baseline: "Stage 2 accepted corpus (S-001..S-113, source-manifest.yaml)"
---
# Stage 3 交接报告 — Vocabulary Normalization (Kimi)

## 产物

- `02_VOCABULARY.md` — 20 个 mandatory collision families 全覆盖（V-001..V-020）+ 6 个补充词条（V-021）+ 10 条归一裁决登记（N-1..N-10）。

## 规模与纪律

- 词条约 70 个，按族组织；只收实质影响架构推理/导航/评测/原则提取的术语，未写成百科全书。
- 全部词条挂 Stage 2 source IDs；无来源支撑的项目工作词条（required property、harness、unboundedness 等）显式标注「项目定义」并锚定任务书章节。
- Status 分布：STABLE 多数；CONTEXT_QUALIFIED 集中于最高危多义词（boundary、consistency、isolation、architecture、scheduling、observability、各 agent 术语）；CONTESTED 2 处（microservices、REST 工业混用）；NEEDS_EVIDENCE 随 RQ2-009 等关联保留。
- Vendor/platform 术语均带 scope 限定（Node event loop、Android 推荐架构、OpenAI guardrail 等）。
- 未提取 Mother Principle，未创建 P-* 文件，未改证据内容。

## 归一方法

同一词多义时不强行统一：10 条归一裁决（N-1..N-10）全部采用「强制 context qualification」或「并存谱系」处理；无一条强行合并。高危族（V-010 consistency、V-002-E boundary、V-011 isolation）已给出使用级强制规则。

## 无法归一的 material collisions

1. **N-9 microservices 收益主张**（CONTESTED + NEEDS_EVIDENCE）：正方一手权威论证缺失（RQ2-009 承自 Stage 2），词汇层只能强制「引用收益主张时缺口在场」，无法给出归一定义。解法是补源（Stage 3 外）。
2. **N-7 REST 工业混用**：Fielding 语义清晰，但工业口语「RESTful」的混用是持续现实，词汇表只能要求注明语义，无法消除外部混用。
3. **V-014-C locality**：通用「距离成本」倾向与 Herlihy-Wing 专用义（可组合性）同名；只能禁止互借，通用义的机制拆分属 Stage 4 原则工作，不在词汇层解决。
4. **architecture 定义三谱系**（N-3）：SAIP/42010/Fowler-Johnson 各有权威，归一为单一定义会丢失信息；维持并存并要求引用指明谱系。这是否满足 RQ-A 对「严格 Architecture Definition」的要求，是 Stage 4+ 的合成问题，不是词汇层能裁决的。

## 证据缺口登记（不重启 Source Collection）

- V-016-C capability（安全语义）：WASI/component model 未收录（RQ2-013 CH-S-07 needs_evidence），词条暂只锚 S-092 原则层。
- V-021-D UI 主线程形态：WHATWG/web.dev 未收录（CH-S-12 rejected this cycle），同构形态暂无来源支撑。
- 以上两项不影响 Stage 3 gate（无重要术语静默多义），但建议列入 Stage 4 的按需定向补源清单。

## 给 Challenger (WorkBuddy Pass A/B) 的建议检查点

- 过归一风险：检查 N-1..N-10 是否存在被强行统一的不同概念（我的自评：无）。
- 欠归一风险：检查是否存在同一概念被拆成冗余标签（自评：authority/authz 分离是刻意的）。
- 高危遗漏：是否存在未覆盖、且会导致架构推理错误的术语冲突（重点看 distributed/state-data 与 agent-runtime 交叉带）。
