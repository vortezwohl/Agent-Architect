---
description: Approve one design bundle for a change
argument-hint: [change request]
disable-model-invocation: true
---

Run the `architect-design` skill for this request: $ARGUMENTS

Requirements:
- This is stage 1 only.
- Read the repository before making design decisions.
- Produce one approved design bundle containing one or more `D-xxx` subdesigns.
- Ask the user to define the compatibility boundary before finalizing the bundle.
- Do not continue into `architect-propose` or `architect-build`.

If no change request was provided, ask the user what consequential change should be designed.
