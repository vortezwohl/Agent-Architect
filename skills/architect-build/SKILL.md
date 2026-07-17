---
name: architect-build
description: "Manual-only skill. Use only when the user explicitly invokes the architect-build skill to execute one sealed plan task at a time with strict boundary checks and factual verification. Do not auto-trigger from a generic implementation request."
---

# Architect Build

Use this skill only as a manually selected implementation stage. Its job is to
execute one sealed task exactly as written, record factual evidence, and
recover deterministically from scope breaches. It does not redesign the plan or
invoke sibling skills automatically.

## Manual Invocation Only

- Run this skill only when the user explicitly asks for `architect-build`.
- Do not auto-switch into `architect-design` or `architect-propose`.
- If the work must return to design or planning, stop and tell the user which
  skill to invoke manually.

## Strict Boundary

- Do not select a new architecture, pattern, concept, dependency direction, or
  lifecycle behavior.
- Do not edit task or design Markdown files after the plan is sealed.
- Do not modify a source path outside the active task's exact boundary.
- Do not continue after a scope breach, incomplete detail, design
  contradiction, missing approval, or failed recovery.
- Do not mark a task complete before scope validation and the task's actual
  verification evidence are recorded.

## Preflight

Before any source edit, confirm that the selected plan is sealed, the current
task is the active bounded task to execute, and the package state is valid for
continuation. Read the manifest, context, design catalog, impact boundaries,
task catalog, verification plan, the active task, and every `D-xxx` document
referenced by that task.

If task state is unfinished, interrupted, or ambiguous, do not continue from
partial implementation as if it were trusted state.

## Task Execution Loop

For exactly one pending task:

1. Announce its `T-xxx` ID, cited `D-xxx` units, allowed paths, symbols,
   operations, `MUST DO`, and `MUST NOT DO` rules.
2. Ensure any required task-state protection is established before editing.
3. Perform one declared atomic step. Do not add an unapproved helper, wrapper,
   pattern, file, state transition, or error behavior.
4. After every atomic edit, verify that the changed paths still stay inside the
   task's exact boundary.
5. Run the task's listed verification command and compare the actual result
   with its expected result.
6. Record actual evidence only after scope and verification pass.
7. Stop after the current task is completed unless the user explicitly asked to
   continue with the next task in the same manual `architect-build` run.

## Mandatory Scope-Breach Recovery

When scope checking reports any unexpected path, stop the task attempt
immediately. Do not manually repair the extra file and keep the same attempt
alive. Return the exact evidence for external recovery. Do not improvise a
partial recovery.

## Return Conditions

- Return to the architect-design skill manually when a task requires a concept
  or rule not covered by an approved `D-xxx` unit.
- Return to the architect-propose skill manually when the approved design
  remains valid but the sealed plan omitted a file, symbol, task, precondition,
  verification rule, or impact boundary.

Report the document, ID, code evidence, and smallest required correction. Do
not modify the sealed plan silently.

## Completion Standard

Finish only after the current task's scope check and verification pass, the
actual evidence is recorded, and the final report distinguishes completed
evidence from remaining risk.
