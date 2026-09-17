---
id: IDX-SOURCES
title: sources/ index
stage: 2
updated: 2026-09-17
---
# sources/ 索引

按 ID 区间导航；完整 provenance 见 `../source-manifest.yaml`。

| 区间 | 主题簇 |
|---|---|
| S-001..S-022 | 架构基础 / 质量属性 / 决策方法 / 架构沟通 / 演进性 |
| S-023..S-046 | 分布式系统 / 状态与数据 / 集成与契约 |
| S-047..S-069 | 可靠性 / 故障模型 / 可观测性 / 事故实证（postmortem） |
| S-070..S-091 | 性能工程 / 并发 / 资源有界 / 运行时执行模型 |
| S-092..S-111 | 安全与信任 / Agent 工程消费 / 欠代表形态（embedded/desktop/local-first/monolith） |

使用规则：
- postmortem（S-059..S-065, S-091）只作实证证据，不作 Mother Principle 唯一支撑。
- 厂商 Agent 工程材料（S-098..S-103, S-111）为 vendor evidence，引用须标注。
- 标记 NEEDS_EVIDENCE / needs-reverify 的条目见 `../review-queue.yaml`。
