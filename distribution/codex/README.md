# Architecture Expert Codex Skill

在其他项目的 Codex 中调用 Architecture Expert，进行架构设计/评审、代码或 PR 的架构评审、ADR 评审和事故分析。只需一个用户级 Skill 和一个已配置的本地知识根，不需要 MCP、服务或额外运行平台。

## Beta 与来源

本分发使用冻结 v0.1 基线 `96d9ae333ffc5a8076d635b86634b5151ec0bbc5` 的原有知识文件与行为合同，分发分支为 `release/architecture-expert-v0.1-beta`。`SKILL.md` 负责定位和加载，不能替代完整的 `agent/system-prompt-v0.1.md` 或所选 mode/DP；不复制整个知识库。

这是供人工审阅的可用 Beta，不是无缺陷或已认证的正式质量发布。后续 Stage 10/11 发现过重要的证据纪律与产品契约弱点；Stage 11 最终裁决 v0.2 未通过，同一组 12 个案例中 v0.1 为 184/212（86.79%），v0.2 为 176/212（83.02%）。这些测量使用 `glm-5.3`，不能当作用户 Codex 模型的能力保证。分发采用 v0.1，保留原 prompt 的历史 `UNEVALUATED` frontmatter，不改写历史来源。

分发范围与以上测量说明的来源为[指定任务书](https://github.com/Dylan5237/architecture-expert/blob/fbe99705daa2658b39776087b3ea5a752a5b8a86/tasks/release/CODEX_FIRST_USABLE_V01_BETA.md)。运行 Skill 时不加载这些评测或管理材料。

## Windows 用户安装

先准备一个持续保留的本地 checkout/worktree，检出本分发分支，并确认 canonical Agent/KB 保持上述 v0.1 基线。不要使用随后会删除或切换到其他知识版本的临时目录。知识由 `Dylan5237/architecture-expert` 维护，必需依赖包括全文 v0.1 prompt、原模式与 DP、Router、Constitution 及任务按需使用的原知识页；缺失时停止并报告。

[OpenAI 本地 Skill 文档](https://learn.chatgpt.com/docs/build-skills)规定用户位置为 `~/.agents/skills`，适用于所有项目；应结合本机新会话实际发现结果验证。下面的 PowerShell 在这个位置只安装 `architecture-expert`，将一个知识根路径持久化到用户环境。把示例路径换成自己的 checkout/worktree，命令不包含个人路径或凭证：

```powershell
$kbRoot = (Resolve-Path -LiteralPath 'D:\path\architecture-expert-v01-beta').Path
$skillSource = Join-Path $kbRoot 'distribution\codex\architecture-expert'
$skillParent = Join-Path $env:USERPROFILE '.agents\skills'
$skillTarget = Join-Path $skillParent 'architecture-expert'
$configuredRoot = [Environment]::GetEnvironmentVariable('ARCHITECTURE_EXPERT_KB_ROOT', 'User')

if (Test-Path -LiteralPath $skillTarget) {
    throw 'architecture-expert 已存在；先核对现有安装，不覆盖'
}
if ($configuredRoot -and $configuredRoot -ne $kbRoot) {
    throw '已有不同的知识根配置；先核对，不自动替换'
}
foreach ($relative in @(
    'distribution\codex\architecture-expert\SKILL.md',
    'agent\system-prompt-v0.1.md',
    'agent\modes\AUTO.md',
    '00_ROUTER.md', '01_CONSTITUTION.md',
    'decision-playbooks\index.md', 'question-bank\index.md'
)) {
    if (-not (Test-Path -LiteralPath (Join-Path $kbRoot $relative) -PathType Leaf)) {
        throw "缺少必需文件：$relative"
    }
}
New-Item -ItemType Directory -Path $skillParent -Force | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillTarget -Recurse -ErrorAction Stop
[Environment]::SetEnvironmentVariable('ARCHITECTURE_EXPERT_KB_ROOT', $kbRoot, 'User')
$env:ARCHITECTURE_EXPERT_KB_ROOT = $kbRoot

Get-Item -LiteralPath (Join-Path $skillTarget 'SKILL.md')
[Environment]::GetEnvironmentVariable('ARCHITECTURE_EXPERT_KB_ROOT', 'User')
$sourceHash = (Get-FileHash -LiteralPath (Join-Path $skillSource 'SKILL.md') -Algorithm SHA256).Hash
$installedHash = (Get-FileHash -LiteralPath (Join-Path $skillTarget 'SKILL.md') -Algorithm SHA256).Hash
if ($sourceHash -ne $installedHash) { throw '安装文件与分发文件不一致' }
```

此方法复制 Skill 入口，知识仍直接读取已配置的原仓库。安装后若修改入口，需要明确更新这份安装副本；不能宣称副本会自动同步。不要改动原 Agent/KB。知识根迁移时先核对目标版本，再明确更新用户变量；进程变量若仍指向旧根，更新它或重启宿主，Skill 会报告冲突。

若磁盘安装或用户配置失败，状态是 `PACKAGED_NOT_INSTALLED`；保留具体错误，完成对应的复制/用户变量步骤并读回后才能继续，不能仅因分发文件存在就声称安装成功。

## 从其他项目调用

安装后在另一个项目开启新的 Codex 会话，通过 Skill 选择器选择 `architecture-expert`，或使用明确调用：

```text
$architecture-expert 请评审当前项目的现有任务处理路径，依据已接受的需求和代码判断资源界限与故障机制，给出最小修正或 NO_DEFECT。
```

可明确指定 `ARCH_DESIGN`、`ARCH_REVIEW`、`CHANGE_REVIEW`、`ADR_REVIEW` 或 `INCIDENT_ANALYSIS`；未指定时按对象 AUTO 路由。单次 CLI 调用也可在项目目录执行：

```powershell
codex exec -C 'D:\path\another-project' '$architecture-expert 请评审这个项目的当前结构，只读取项目证据和必要知识，不修改文件。'
```

如果 CLI 在加载 Skill 前报告账户不支持配置中的模型，先用 `codex debug models` 核对本机实际目录，再为这一条 `codex exec` 添加 `-m` 指定目录中可用的模型，并使用它支持的思考强度。单次参数不改全局默认；模型启动失败不证明 Skill 已被调用，也不属于架构质量结果。

Codex 检测到新 Skill 后即可使用；选择器未出现时重启 Codex。[调用与发现方式见官方文档](https://learn.chatgpt.com/docs/build-skills)。UI 选择器是否可见需在用户 UI 中确认，CLI 实测不能冒充 UI 截图验证。

## 一次使用验证与边界

在知识仓库之外，以一个小型非保密架构问题或用户批准的真实项目任务明确调用一次。核对实际文件读取轨迹，确认全文 v0.1 prompt、相应 mode、Router、Constitution、一个 DP 和相关知识页确实被读取；不能只看助手自述。

结果应有一个主要 mode/DP、项目证据的 origin/state、具体机制、相关 GOOD CASE 限定条件、最小修正或 NO_DEFECT、相关不确定性与 typed terminal。`BETA_USABLE` 表示个人安装及这次明确调用成功；不表示评分通过、覆盖所有模式、其他宿主模型验证或正式发布。无法调用且缺少必要能力时报告 `BLOCKED`。

使用记录与私人安装路径留在本地工作区之外。不得向公共仓库提交用户/公司代码、网关地址/密钥或项目原始输出；本分发只跟踪 `distribution/codex/architecture-expert/SKILL.md` 与本 README。分析本身不授权修改待分析项目、知识库或外部系统。
