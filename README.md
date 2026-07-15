<div align="center">

# Agent Architect

**Architecture judgment for coding agents.**

*Most coding agents can write code.<br />
Few can defend an architecture decision.*

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-agent--architect-111827?style=flat-square)](https://github.com/vortezwohl/Agent-Architect/tree/main/skills/agent-architect)
[![MIT License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](https://github.com/vortezwohl/Agent-Architect/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/vortezwohl/Agent-Architect?style=flat-square&label=Stars)](https://github.com/vortezwohl/Agent-Architect/stargazers)

<br />

> <strong>Stop asking agents which pattern to use.</strong><br />
> Ask them to prove <strong>what must change independently</strong>.

[Install](#install) &middot; [What It Does](#what-it-does) &middot; [See It Think](#see-it-think) &middot; [Protocol](#the-decision-protocol)

</div>

---

## The problem

AI makes implementation cheap.

It also makes **bad architecture cheap to multiply**:

- An interface for one stable implementation.
- A factory for a constructor call.
- An event bus without delivery semantics.
- Inheritance where a function would do.
- "Future-proofing" with no proven future.

The result looks sophisticated in a PR and becomes expensive in production.

> ## No abstraction without a proven variation point.

**Agent Architect** gives coding agents a decision protocol for architecture, refactoring, design patterns, boundaries, lifecycles, and evolution.

It does not ask:

```text
Which pattern should I use?
```

It asks:

```text
What changes independently?
What stays stable?
What is the smallest design that isolates the proven change?
How will we verify that the new structure is worth its cost?
```

---

## What it does

<table>
<tr>
<th align="left">Instead of this</th>
<th align="left">Agent Architect requires this</th>
</tr>
<tr>
<td>"Use Factory because we may add providers later."</td>
<td>Name the real creation variation, affected callers, lifecycle, and why a constructor or injected function is insufficient.</td>
</tr>
<tr>
<td>"Add an event for asynchronous processing."</td>
<td>Define transaction boundary, delivery guarantee, ordering, retry, idempotency, and consistency model.</td>
</tr>
<tr>
<td>"Introduce an interface for clean architecture."</td>
<td>Identify the independent variation it isolates and the ongoing cost of maintaining it.</td>
</tr>
<tr>
<td>"Refactor complete."</td>
<td>State the exact normal, boundary, failure, integration, and operational validation actually performed.</td>
</tr>
</table>

### The output is auditable

For every non-trivial design or refactor, the agent produces:

```text
01. Design diagnosis
    Objective, non-goals, evidence, callers, stable core,
    variation points, smells, and constraints.

02. Alternatives
    The smallest direct design, candidate patterns,
    rejected neighbors, and added structural cost.

03. Decision
    Chosen design, including a justified decision to use no pattern.

04. Verification
    Tests, operational checks, remaining uncertainty, and risk.
```

---

## See it think

### Wrong: the common AI answer

> "This payment module may support Stripe, PayPal, and more providers later. Let's create an `IPaymentProvider`, `PaymentProviderFactory`, `PaymentProviderRegistry`, and `PaymentProviderEventBus`."

### Right: the Agent Architect answer

> **Observed evidence:** only Stripe exists; there is one caller; no provider selection exists in product requirements; no second integration is scheduled.
>
> **Smallest direct design:** keep the injected `StripeClient` dependency.
>
> **Decision:** reject Factory, Registry, and Event Bus. They isolate no proven variation and add ownership, registration, test, and failure-path cost.
>
> **Extraction trigger:** introduce a provider seam when a second provider must coexist behind the same business operation, with shared caller expectations and independently changing provider behavior.
>
> **Verification:** preserve current payment failure semantics and characterize the provider boundary before extraction.

That is not "less architecture."

That is **architecture with evidence**.

---

## The decision protocol

```text
Inspect reality
      |
      v
Name the proven change
      |
      +-- No proven independent variation?
      |     `-- Keep the direct design. Record the extraction trigger.
      |
      v
Compare the smallest direct solution
      |
      v
Evaluate candidate patterns by intent, lifecycle, and failure modes
      |
      v
Reject look-alike patterns
      |
      v
Check API direction, ownership, transactions, concurrency, and rollback
      |
      v
Verify behavior at the right boundary
      |
      v
Report evidence, decision, validation, and remaining risk
```

### Non-negotiable rules

- Do not start from **"Which pattern should I use?"**
- Do not turn uncertainty into speculative abstraction.
- Do not call an event an async design without delivery semantics.
- Do not use Singleton to avoid dependency injection.
- Do not use inheritance when composition, callbacks, or direct functions are clearer.
- Do not call an unverified refactor complete.
- Do not add a type, wrapper, event, global, or factory without naming the concrete change it isolates.

---

## Install

### Codex

```text
$skill-installer install https://github.com/vortezwohl/Agent-Architect/tree/main/skills/agent-architect
```

Restart Codex after installation.

### Other Agent Skills-compatible tools

Copy the `skills/agent-architect/` directory into the tool's supported skills location, then invoke the skill by its name:

```text
agent-architect
```

> [!IMPORTANT]
> Read a skill before installing it. A skill is executable agent guidance: inspect its instructions, bundled references, scripts, and trust boundary.

---

## Use it

Ask your coding agent:

```text
Use $agent-architect to design or refactor this software
with the smallest justified pattern set.
```

Useful prompts:

```text
Use $agent-architect to review this PR for speculative abstractions.

Use $agent-architect to decide whether this module needs Strategy,
a direct function, or no extraction.

Use $agent-architect to refactor this service while preserving behavior.

Use $agent-architect to compare Adapter, Decorator, and Proxy
for this integration boundary.

Use $agent-architect to design the migration and rollback plan
for replacing this subsystem.
```

---

## What it covers

<details>
<summary><b>Creational decisions</b></summary>

- Factory Method
- Abstract Factory
- Builder
- Prototype
- Singleton scope

</details>

<details>
<summary><b>Structural decisions</b></summary>

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

</details>

<details>
<summary><b>Behavioral decisions</b></summary>

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
<summary><b>Critical pattern boundaries</b></summary>

| Do not confuse | With |
| --- | --- |
| Decorator | Proxy or Adapter |
| Facade | Mediator |
| Factory Method | Abstract Factory, Builder, or Prototype |
| Strategy | State or Template Method |
| Observer | Chain of Responsibility or Command |
| Composite | Decorator |

Agent Architect chooses by **intent, collaborators, lifecycle, variation, and failure behavior** - never by a class diagram alone.

</details>

---

## What this skill is not

| Not this | But this |
| --- | --- |
| A design-pattern encyclopedia | A decision protocol for selecting, rejecting, or combining patterns |
| A ceremony generator | A guardrail against needless layers |
| "Clean architecture" by default | Explicit dependency-direction and lifecycle analysis |
| A promise that every problem needs a pattern | Permission to choose the direct design |
| A substitute for engineering ownership | A way to make agent-produced decisions inspectable |

---

## Repository structure

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

- `SKILL.md` - operating rules and required decision record
- `decision-protocol.md` - binding diagnostic, selection, refactoring, and review gates
- `gof-patterns.md` - intent, trade-offs, misuse cases, and verification guidance
- `source-article.md` - architecture principles and pattern context for the AI coding era

---

## The standard

A design is not complete because it has more layers.

A refactor is not complete because the code looks cleaner.

An architecture decision is complete only when it can answer:

```text
What evidence justified this structure?
Why is the direct alternative insufficient?
What changes independently?
What did we reject, and why?
How was behavior verified?
What risk remains?
```

> **Design for the next verified change - not for a pattern name.**

---

## Contributing

Contributions should improve **judgment**, not add ceremony.

Good contributions:

- Better evidence gates for real architecture decisions.
- Clearer pattern boundaries and rejection criteria.
- Reproducible examples of overengineering and minimal alternatives.
- Verification guidance for lifecycle, concurrency, transactions, migration, and rollback.
- Corrections that make agents less likely to over-abstract.

Before opening a change, ask:

```text
Does this improve a decision an agent can make?
Can the improvement be verified?
Does it add guidance without adding speculative process?
```

---

## License

MIT. See [LICENSE](LICENSE).

---

<div align="center">

### If your agent adds abstractions faster than it can justify them, install this skill.

<strong>Star it. Fork it. Use it in your next architecture review.</strong>

</div>
