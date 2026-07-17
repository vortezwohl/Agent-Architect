<div align="center">

<h1>
  <img src="../assets/architect-wordmark.svg" alt="Architect" width="520" />
</h1>

**快速写代码不难。难的是让代码库在接下来的上百次变更后依然站得住。**

*构建能够随着规模增长仍保持一致性的代码库，而不是落入巨型模块、预设性抽象或意外破坏性变更。*

[![Architect Workflow](https://img.shields.io/badge/Architect-design%20-%20propose%20-%20build-111827?style=flat-square)](https://github.com/vortezwohl/Agent-Architect/tree/main/skills/architect-design)
[![MIT License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](https://github.com/vortezwohl/Agent-Architect/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/vortezwohl/Agent-Architect?style=flat-square&label=Stars)](https://github.com/vortezwohl/Agent-Architect/stargazers)

<br />

**不让架构在偶然中形成。** &nbsp; **不靠臆测引入抽象。** &nbsp; **不凭假设维护兼容性。**

[Why](#为什么选择-architect) &middot; [Workflow](#工作流) &middot; [Outputs](#产物) &middot; [Example](#示例体验) &middot; [Install](#安装)

</div>

<h4 align="center">
  <p>
    <a href="https://github.com/vortezwohl/Agent-Architect/blob/main/README.md">English</a> |
    <a href="https://github.com/vortezwohl/Agent-Architect/blob/main/i18n/README_zh-hant.md">&#32321;&#39636;&#20013;&#25991;</a> |
    <b>&#31616;&#20307;&#20013;&#25991;</b> |
    <a href="https://github.com/vortezwohl/Agent-Architect/blob/main/i18n/README_ja-jp.md">&#26085;&#26412;&#35486;</a>
  </p>
</h4>

---

## 为什么选择 Architect

多数 coding agent 失败，并不是因为它们不会写代码。

而是因为它们会在写代码的同时，悄悄做出结构性决策。

一个听起来很普通的请求：

```text
增加第二个支付提供方。
重构这个服务。
让这个功能可扩展。
```

其实已经强迫你对所有权、边界、兼容性、失败行为、状态流、迁移方式和回滚方式做出决策。

当这些决策始终保持隐含状态时，代码库通常会滑向三种代价高昂的状态之一：

| Failure | What happens |
| --- | --- |
| **Architecture by neglect** | 功能被塞进最近的文件里。所有权开始模糊，规则开始复制，一两个模块不断吞掉一切。 |
| **Architecture by speculation** | 还没有真实变化点时，可能的未来就先被做成接口、工厂、注册表、事件层或继承层。 |
| **Compatibility by assumption** | 在未先把预期边界说清楚之前，已有行为就被默认保留，或者被默认破坏。 |

Architect 的存在，就是为了在代码库为这些决策付出代价之前，先把它们强制暴露出来。

---

## 工作流

Architect 是一个严格的**手动三阶段流程**：

```text
architect-design -> architect-propose -> architect-build
```

每个阶段都有独立职责，并且会拒绝自动去做下一个阶段的工作。

| Stage | Invoke when | Produces | Refuses to do |
| --- | --- | --- | --- |
| `architect-design` | 你需要为一次重要变更确定一个经过批准的架构方向。 | 一个经过批准的设计包，其中包含一个或多个 `D-xxx` 子设计。 | 计划编排、文件写入或实现。 |
| `architect-propose` | 设计包已经获批，必须转成可执行包。 | 一个封存好的 `.architect/<plan-name>/` 包，包含 `D-xxx`、`T-xxx`、状态文件和日志产物。 | 重新设计方案或编辑应用代码。 |
| `architect-build` | 封存包已经校验完毕，准备执行。 | 真实的实现推进、任务状态更新，以及基于事实的执行日志。 | 在构建中途重新打开设计，或临时发明新结构。 |

这就是核心的用户体验变化：agent 不再从请求直接跳到代码。它必须先把设计批准、计划封存和有边界的执行拆开。

---

## 产物

### 1. 已批准的设计包

`architect-design` 会为一个未来计划包产出一个已批准的设计包。

每个设计包都可以包含多个 `D-xxx` 子设计，并且明确给出意图、边界、反例、反模式，以及 `MUST DO` / `MUST NOT DO` 规则。

### 2. 封存的执行包

`architect-propose` 会把该已批准设计包转换为位于以下目录中的一个确定性执行包：

```text
.architect/<plan-name>/
```

该执行包包含：

```text
00-plan-manifest.md
01-context-and-contract.md
02-design-catalog.md
03-designs/D-xxx-<slug>.md
04-impact-and-boundaries.md
05-task-catalog.md
06-tasks/T-xxx-<slug>.md
07-verification-plan.md
08-execution-log.md
.state/execution-state.json
```

这不是一堆笔记，而是构建阶段的执行合同。

### 3. 受检查点控制的构建证据

`architect-build` 会按顺序执行封存的 `T-xxx` 任务，如实更新任务状态，追加基于事实的日志记录，并把实现严格限制在已批准边界内。

你得到的不只是代码。你得到的是代码，以及解释为什么要改代码、实际发生了什么的决策轨迹、状态轨迹和执行轨迹。

---

## 示例体验

```text
User:
在不破坏当前结账流程的前提下，增加第二个支付提供方。
```

```text
Stage 1: $architect-design
- 先读取仓库。
- 询问必须保持哪些兼容性。
- 把已被证明的变化点和稳定策略分离开。
- 产出已批准的 D-xxx 子设计。
```

```text
Stage 2: $architect-propose add-payment-provider
- 创建 .architect/add-payment-provider/
- 使用仓库脚本分配设计文档和任务文档。
- 封存并校验执行包。
```

```text
Stage 3: $architect-build add-payment-provider
- 加载封存包和当前执行状态。
- 按顺序执行记录在案的 T-xxx 任务。
- 用真实结果更新执行日志。
```

差异很直接：

- 普通 coding agent 会直接开始写代码，并把架构决策藏进 diff 里。
- Architect 会让这些决策变得显式、可批准、可序列化、可执行。

---

## 安装

### 插件

#### Codex

```text
codex plugin marketplace add vortezwohl/Agent-Architect
codex plugin install architect@architect
```

#### Claude Code

```text
/plugin marketplace add vortezwohl/Agent-Architect
/plugin install architect@architect
```

安装完成后请开启一个新会话，这样 agent 才能发现该插件。

### 独立技能

```text
npx skills add vortezwohl/Agent-Architect
```

或者把 `skills/` 复制到你的工具支持的 skills 目录中，然后手动调用各阶段：

```text
$architect-design
$architect-propose <plan-name>
$architect-build <plan-name>
```

> [!IMPORTANT]
> 安装前先阅读 skill。这些 skill 编码了执行规则、包合同和阶段边界。

---

## 正确使用方式

按顺序使用各阶段。

1. 只有在你需要一个经过批准的设计包时，才运行 `architect-design`。
2. 只有在该设计包已经获批后，才运行 `architect-propose`。
3. 只有在生成的执行包已经封存并校验后，才运行 `architect-build`。

不要从一个大型请求直接跳到 `architect-build`。这个仓库是围绕“已批准设计、封存计划和有边界执行的分离”而构建的。

---

## 仓库结构

```text
assets/
`-- architect-wordmark.svg

skills/
|-- architect-design/
|   |-- SKILL.md
|   |-- agents/openai.yaml
|   `-- references/
|       |-- decision-protocol.md
|       |-- gof-patterns.md
|       `-- source-article.md
|-- architect-propose/
|   |-- SKILL.md
|   |-- agents/openai.yaml
|   |-- scripts/
|   `-- templates/
`-- architect-build/
    |-- SKILL.md
    `-- agents/openai.yaml
```

公开产品名是 **Architect**。

三个可调用阶段分别是 `architect-design`、`architect-propose` 和 `architect-build`。

---

## 贡献

贡献应该强化这套工作流，而不是增加噪音。

好的贡献通常会改善以下某一项：

- 设计阶段的证据门禁；
- 兼容性边界的清晰度；
- 封存包的确定性；
- 构建阶段的执行纪律；
- 回滚、校验或日志记录的准确性。

如果一个改动增加了流程负担，却没有提升上述任一属性，那它大概率就是错误的改动。

---

## 许可证

MIT。参见 [LICENSE](../LICENSE)。
