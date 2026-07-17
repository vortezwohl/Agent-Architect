---
name: architect-design
description: "Manual-only skill. Use only when the user explicitly invokes the architect-design skill to produce an architecture decision bundle before any plan package exists. Do not auto-trigger from a generic feature, refactor, integration, or implementation request."
---

# Architect Design

Use this skill only as a manually selected architecture decision stage. Its job
is to teach and constrain one design decision bundle, not to plan tasks, modify
files, or invoke sibling skills automatically.

## Manual Invocation Only

- Run this skill only when the user explicitly asks for `architect-design`.
- Do not auto-switch into `architect-propose` or `architect-build`.
- If the next step needs planning or implementation, stop and tell the user
  which skill to invoke manually.

## Core Outcome

Produce an approved, bounded design bundle that another agent can inspect
without guessing:

- resolve compatibility intent before repository inspection;
- study the required references before naming a concept or pattern;
- inspect only the repository evidence needed for the current decision;
- compare the direct design with the best adjacent alternatives;
- define explicit `D-xxx` design units with boundaries, counterexamples,
  anti-patterns, and design rules;
- obtain explicit user approval for the displayed design bundle.

## Strict Boundary

- Design is read-only. Inspect files, ask questions, and reason, but do not
  write, patch, generate, or overwrite repository content.
- Do not create a plan package or implementation task.
- Do not convert an unapproved assumption into a design unit.
- Do not let silence count as approval.
- Do not continue while compatibility intent, design detail, or approval
  coverage remains unresolved.
- Do not use a pattern because its shape looks familiar.

## Working Sequence

1. Classify the request only far enough to decide whether architecture design
   is needed. Do not inspect the repository yet.
2. Read `references/decision-protocol.md` and apply Gate 0 before repository
   inspection when contracts, state, configuration, integrations, or extension
   points may change.
3. Read `references/source-article.md` before the first design decision.
4. Read the relevant entries in `references/gof-patterns.md` before choosing,
   rejecting, or comparing a GoF pattern. Read neighboring candidates together
   when confusion is plausible.
5. Inspect repository evidence only after the compatibility boundary is known:
   callers, tests, ownership, dependencies, lifecycle, state, failures,
   transactions, concurrency, framework constraints, and operational risk.
6. Define the compatibility boundary, evolution horizon, real variation,
   stable core, collaborators, lifecycle, and likely failure mode from
   evidence, not imagination.
7. Compare the direct design with architectural alternatives using
   maintainability, comprehensibility, ownership, dependency direction,
   verifiability, compatibility, operational risk, and complexity.
8. Split the approved solution into independently understandable `D-xxx`
   design units. One unit owns one architectural decision.
9. For every design unit, record a recognized engineering concept or pattern,
   canonical name, category, reliable reference, counterexamples,
   anti-patterns, design boundaries, and design-level `MUST DO` / `MUST NOT
   DO` rules.
10. Present the complete design bundle and obtain explicit user approval for
    the displayed `D-xxx` identifiers.

## Teaching Standard

Before asking for approval, explain for every non-trivial decision:

- what concrete problem the chosen concept solves here;
- what remains stable and what changes independently;
- which simpler direct design was considered and why it was accepted or
  rejected;
- which adjacent pattern or abstraction was rejected and why;
- which misuse, counterexample, or operational failure would make the concept a
  poor fit;
- which validation boundary Build must later preserve.

Do not cite the references mechanically. Convert them into reasoning that the
next agent can reapply.

## Design Unit Contract

Every design unit must contain the following fixed English fields. Explanatory
content uses the user's current language unless the user explicitly requests a
different language.

```md
# Design: D-001-<slug>

## Concept
- CanonicalName:
- Category:
- Reference:

## Intent
## StableCoreAndVariation
## Rationale
## Alternatives
## DesignBoundaries
## Counterexamples
## AntiPatterns
## Rules
### MUST DO
### MUST NOT DO
```

Rules must constrain implementation details, not merely desired outcomes.

## Completion Standard

Finish only when the user can inspect the approved design bundle, understand
why each concept beat its alternatives, and decide whether to stop or manually
invoke the architect-propose skill.
