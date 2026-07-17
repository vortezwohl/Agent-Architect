---
name: architect-propose
description: "Manual-only skill. Use only when the user explicitly invokes the architect-propose skill to turn an already approved design bundle into a sealed plan package under `.architect/`. Do not auto-trigger from a design or implementation request."
---

# Architect Propose

Use this skill only as a manually selected plan-packaging stage. Its job is to
convert an already approved design bundle into deterministic Markdown artifacts,
not to redesign, implement code, or invoke sibling skills automatically.

## Manual Invocation Only

- Run this skill only when the user explicitly asks for `architect-propose`.
- Do not auto-switch into `architect-build`.
- If planning finishes and the next step is implementation, stop and tell the
  user to invoke the architect-build skill manually.

## Strict Boundary

- Create or update only `.architect/<plan-name>/` after user authorization.
- Do not edit application code, tests, runtime configuration, or unrelated
  documentation.
- Do not invent a design unit, concept, boundary, anti-pattern, or rule.
- Do not create a task that cannot cite approved `D-xxx` design units and their
  concrete rules.
- Do not mark a package buildable while a placeholder, encoding error, unknown
  decision, incomplete boundary, or unresolved approval remains.

## Required Input

Before creating a package, require all of the following:

1. The complete approved design bundle with `D-xxx` identifiers.
2. Approval evidence that explicitly covers every referenced design unit.
3. Compatibility intent, objective, non-goals, affected surfaces, and risks.
4. A kebab-case plan name, provided by the user or safely derived from the
   approved design.
5. The user's document language, inferred from the current interaction unless
   the user explicitly requests another language.

## Deterministic Package Creation

Use repository-provided plan tooling rather than manually creating identifiers,
timestamps, directories, state records, or hashes. In this repository's native
Codex setup, the helper commands are:

```text
python scripts/make_plan.py --repo-root <root> --plan <name> --language <tag>
python scripts/plan_control.py add-design --repo-root <root> --plan <name> --slug <slug>
python scripts/plan_control.py add-task --repo-root <root> --plan <name> --slug <slug>
```

These commands generate metadata fields, IDs, filenames, timestamps, state
records, and content digests. Agent-authored prose fills only `{{AGENT:...}}`
areas in the user's document language. In another runtime, use an equivalent
repository wrapper if one exists, but preserve the same package contract. Do
not add or rename fields, headings, files, identifiers, or directories
manually.

## Package Contract

The package root is:

```text
.architect/<plan-name>/
```

It must contain these artifacts:

- `00-plan-manifest.md`
- `01-context-and-contract.md`
- `02-design-catalog.md`
- `03-designs/D-xxx-<slug>.md`
- `04-impact-and-boundaries.md`
- `05-task-catalog.md`
- `06-tasks/T-xxx-<slug>.md`
- `07-verification-plan.md`
- `08-execution-log.md`
- `.state/execution-state.json`
- `.state/checkpoints/`

Every `T-xxx` document must state exact paths, symbols, operations, approved
design references, approved rule references, task-specific `MUST DO`,
task-specific `MUST NOT DO`, atomic steps, scope recovery, local verification,
and a completion condition.

If a task needs a new pattern, dependency direction, state transition, error
contract, or file outside the approved boundary, stop and tell the user that
the work must return to the architect-design skill manually.

## Sealing and Validation

After all placeholders are filled, seal the package and validate it:

```text
python scripts/plan_control.py seal --repo-root <root> --plan <name>
python scripts/validate_plan.py --repo-root <root> --plan <name>
```

Do not auto-rewrite semantic prose after a validation failure. Stop, inspect
the reported evidence, correct the package from approved inputs, and validate
again.

## Completion Standard

Finish only after validation succeeds. Report the package path, actual
validation result, remaining risk, and whether the user may manually invoke
the architect-build skill for the selected plan next.
