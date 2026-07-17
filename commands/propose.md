---
description: Seal an approved design into a plan
argument-hint: [plan-name]
disable-model-invocation: true
---

Run the `architect-propose` skill.

Requirements:
- This is stage 2 only.
- Convert the already approved design bundle into one sealed `.architect/<plan-name>/` package.
- Do not redesign the solution.
- Do not continue into `architect-build`.

Plan-name handling:
- If `$1` is present, use it as the plan name.
- If `$1` is missing and there is exactly one obvious approved design bundle, propose a concise kebab-case `plan-name` and continue after user confirmation.
- If `$1` is missing and the target plan is ambiguous, ask the user for `[plan-name]`.
