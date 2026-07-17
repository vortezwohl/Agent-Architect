---
description: Execute a sealed plan in order
argument-hint: [plan-name]
disable-model-invocation: true
---

Run the `architect-build` skill.

Requirements:
- This is stage 3 only.
- Execute the sealed plan package in order.
- Restore the required package context before acting if necessary.
- Keep execution state and logs strictly factual.
- Do not reopen design or propose a new plan mid-build.

Plan-name handling:
- If `$1` is present, use it as the plan name.
- If `$1` is missing and there is exactly one obvious sealed plan package, use it.
- If `$1` is missing and multiple sealed plans are plausible, ask the user for `[plan-name]`.
