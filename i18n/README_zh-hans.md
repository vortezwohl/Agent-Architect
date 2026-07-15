<div align="center">

# Agent Architect

**面向编码智能体的架构护栏。**

*你的智能体已经在作出架构决策。<br />
不要让它悄无声息地作出这些决定。*

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-agent--architect-111827?style=flat-square)](https://github.com/vortezwohl/Agent-Architect/tree/main/skills/agent-architect)
[![MIT License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](https://github.com/vortezwohl/Agent-Architect/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/vortezwohl/Agent-Architect?style=flat-square&label=Stars)](https://github.com/vortezwohl/Agent-Architect/stargazers)

<br />

> <strong>不让架构偶然产生。</strong><br />
> <strong>不让抽象源于臆测。</strong>

[安装](#安装) &middot; [问题所在](#问题所在) &middot; [对比差异](#对比差异) &middot; [决策协议](#决策协议)

</div>

<h4 align="center">
  <p>
    <a href="https://github.com/vortezwohl/Agent-Architect/blob/main/README.md">English</a> |
    <a href="https://github.com/vortezwohl/Agent-Architect/blob/main/i18n/README_zh-hant.md">繁體中文</a> |
    <b>简体中文</b> |
    <a href="https://github.com/vortezwohl/Agent-Architect/blob/main/i18n/README_ja-jp.md">日本語</a>
  </p>
</h4>

---

## 问题所在

大多数用户并不会要求智能体作出架构决策。

他们要求它完成普通工作：

```text
新增一个用于下载发票的端点。
构建一个设置页面。
将此服务接入新的提供方。
重构这个模块。
让此功能具备可扩展性。
```

智能体写下第一行代码之前，就已经开始决定：

- 哪个模块拥有该行为与状态。
- 哪些依赖会跨越边界。
- 哪些失败路径会成为公开行为。
- 直接实现、抽象或框架扩展是否有充分理由。
- 这项改动将如何演进、迁移、回滚与验证。

这些都是架构决策。

没有明确协议时，智能体通常会以三种方式失败：

<table>
<tr>
<th align="left">失败方式</th>
<th align="left">会发生什么</th>
</tr>
<tr>
<td><strong>偶然架构</strong></td>
<td>智能体把功能直接写进最近的文件。还没有人为边界命名，依赖、状态和错误路径就已经扩散。</td>
</tr>
<tr>
<td><strong>臆测抽象</strong></td>
<td>智能体看见一个可能的未来，在真正的变化出现前就创建接口、工厂、注册表、事件或继承体系。</td>
</tr>
<tr>
<td><strong>断言式验证</strong></td>
<td>智能体没有证明行为、兼容性、失败处理或剩余风险，便宣称重构简洁或已完成。</td>
</tr>
</table>

**Agent Architect** 是非平凡编码请求与结构复杂度之间的护栏。

它促使智能体审视现实、选择理由最充分的最小设计，并在复杂度扩散前报告证据。

---

## 对比差异

### 使用 Agent Architect 前

```text
用户：“新增一个用于下载发票的端点。”

智能体：写一个处理器，直接访问持久化层并调用存储，
内联加入鉴权，再为“未来格式”创建 ExportFactory，
然后报告该端点已完成。
```

### 使用 Agent Architect 后

```text
用户：“新增一个用于下载发票的端点。”

智能体：
1. 检查现有发票归属、鉴权、存储、调用方、
   错误处理和测试。
2. 说明实际改动：为一个现有发票产物新增一个 HTTP 入口。
3. 对比直接调用应用服务与新增导出层。
4. 当只有一种格式和一条存储路径时，保留直接设计。
5. 记录提取触发条件：同一应用操作背后有多个独立变化的导出
   格式或存储提供方。
6. 验证鉴权、发票缺失、存储失败和既有发票流程。
```

结果并不是更少的工程工作。

而是**具有明确决策、更小影响范围和验证路径的工程工作**。

---

## 决策协议

```text
收到一项非平凡的编码请求
      |
      v
检查仓库和当前行为
      |
      v
说明已证实的改动、稳定核心、约束与失败路径
      |
      +-- 没有独立变化的证据？
      |     `-- 保留直接设计，并记录提取触发条件。
      |
      v
将最小直接方案与候选结构进行比较
      |
      v
拒绝不必要的接口、工厂、包装器、事件和继承
      |
      v
检查所有权、生命周期、API 方向、事务、并发、
回滚、可观测性和框架约定
      |
      v
实现一个最小且已验证的切片
      |
      v
报告证据、决策、已执行验证和剩余风险
```

### 不可妥协的规则

- 在说明哪些内容独立变化、哪些内容保持稳定之前，不要生成结构。
- 未说明它隔离的具体变化及增加的成本前，不要引入接口、工厂、包装器、事件、继承层级、全局对象或框架层。
- 不要把不确定性转化为臆测式抽象。
- 没有投递语义时，不要把事件称为异步设计。
- 不要用 Singleton 规避依赖注入。
- 当组合、回调或直接函数更清晰时，不要使用继承。
- 不要把未经验证的实现或重构称为完成。

---

## 智能体会产出什么

对于每项非平凡功能、集成、设计或重构，Agent Architect 都会生成可审计记录：

```text
01. 设计诊断
    目标、非目标、仓库证据、调用方、稳定核心、
    变化点、异味和约束。

02. 备选方案
    最小直接设计、候选结构、
    被拒绝的备选方案和持续性的结构成本。

03. 决策
    选定设计、公开 API 与依赖影响、
    迁移与回滚影响，或经过充分理由支持的不使用模式的决定。

04. 验证
    正常、边界、失败、集成和运行检查；
    实际执行的验证；以及剩余不确定性或风险。
```

---

## 何时使用

在**实现或审查任何非平凡改动之前**使用 Agent Architect，包括：

- 跨越模块、层或服务的新功能。
- 改变依赖、所有权、状态或生命周期的重构。
- 第三方集成和遗留系统适配。
- 异步、事件、事务、重试、缓存或鉴权工作。
- 要求让系统“整洁”“可扩展”“可伸缩”或“面向未来”的请求。
- 代码看似合理、但其结构决策是隐含的 PR 审查。

> [!TIP]
> 不要等用户提出架构问题。请将此技能加入处理功能工作和结构性改动的智能体工作流。

---

## 安装

### Codex

```text
$skill-installer install https://github.com/vortezwohl/Agent-Architect/tree/main/skills/agent-architect
```

安装后重启 Codex。

### 其他兼容 Agent Skills 的工具

将 `skills/agent-architect/` 复制到工具支持的技能目录，然后调用：

```text
agent-architect
```

> [!IMPORTANT]
> 安装技能前请先阅读。技能是可执行的智能体指导：请检查其说明、随附参考资料、脚本和信任边界。

---

## 使用方法

向你的编码智能体提出：

```text
在实现或审查这项非平凡改动之前使用 $agent-architect。
检查仓库，选择理由最充分的最小设计，
然后实现并验证它。
```

示例：

```text
在添加此支付提供方之前使用 $agent-architect。

使用 $agent-architect 审查此功能，寻找偶然架构
和臆测抽象。

在重构此服务边界之前使用 $agent-architect。
保持行为不变，并报告迁移和回滚影响。

使用 $agent-architect 确定此集成是否需要适配器、
直接依赖或框架扩展。
```

---

## 模式是工具，而非产品

Agent Architect 覆盖全部 23 种 GoF 模式，但它并不从模式目录开始。

它从证据开始：**什么会变化、谁拥有它、什么会失败，以及什么必须保持稳定。**

<details>
<summary><b>创建型决策</b></summary>

- Factory Method
- Abstract Factory
- Builder
- Prototype
- Singleton scope

</details>

<details>
<summary><b>结构型决策</b></summary>

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

</details>

<details>
<summary><b>行为型决策</b></summary>

- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor

</details>

<details>
<summary><b>关键模式边界</b></summary>

| 不要混淆 | 与 |
| --- | --- |
| Decorator | Proxy 或 Adapter |
| Facade | Mediator |
| Factory Method | Abstract Factory、Builder 或 Prototype |
| Strategy | State 或 Template Method |
| Observer | Chain of Responsibility 或 Command |
| Composite | Decorator |

模式应按**意图、协作者、生命周期、变化和失败行为**选择——绝不能只依据类图。

</details>

---

## 此技能不是什么

| 不是这个 | 而是这个 |
| --- | --- |
| 模式百科全书 | 面向编码智能体的架构决策协议 |
| 仪式生成器 | 防止偶然复杂度的护栏 |
| 默认采用“整洁架构” | 显式分析边界、依赖和生命周期 |
| 增加层级的理由 | 没有证据时保留直接设计的许可 |
| 工程所有权的替代品 | 让智能体产出结构可审计、可验证的方法 |

---

## 仓库结构

```text
skills/
`-- agent-architect/
    |-- SKILL.md
    |-- agents/
    |   `-- openai.yaml
    `-- references/
        |-- decision-protocol.md
        |-- gof-patterns.md
        `-- source-article.md
```

- `SKILL.md` - 运行规则和必需的设计记录
- `decision-protocol.md` - 具有约束力的诊断、选择、重构和审查关卡
- `gof-patterns.md` - 模式意图、权衡、误用场景和验证指南
- `source-article.md` - AI 编码时代的架构原则

---

## 标准

功能并不会因为能编译就算完成。

重构并不会因为代码看起来更整洁就算完成。

架构决策只有能回答下列问题时才算完成：

```text
什么证据证明此结构合理？
为什么直接替代方案不足？
什么会独立变化？
我们拒绝了什么，为什么？
行为如何得到验证？
还剩下什么风险？
```

> **为下一次经过验证的改动设计——而不是为某个模式名称设计。**

---

## 贡献

贡献应改进**判断力**，而不是增加仪式。

有价值的贡献包括：

- 面向真实功能与架构决策的证据关卡。
- 更清晰的模式边界和拒绝条件。
- 可复现的偶然架构与臆测抽象示例。
- 面向生命周期、并发、事务、迁移和回滚的验证指南。
- 能让智能体更不容易扩散结构复杂度的修正。

在发起改动前，请先问：

```text
这是否改进了智能体在代码扩散前可作出的决策？
这项改进能否验证？
它是否在不增加臆测流程的情况下提供指导？
```

---

## 许可证

MIT。请参阅 [LICENSE](../LICENSE)。

---

<div align="center">

### 不要让你的编码智能体悄无声息地设计你的系统。

<strong>点个 Star。Fork 它。在下一次非平凡改动前加入它。</strong>

</div>