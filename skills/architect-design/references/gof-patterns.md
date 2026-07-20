# Complete GoF Design Pattern Catalog

## Coverage Contract

This catalog teaches the complete Gang of Four set: 5 creational, 7
structural, and 11 behavioral patterns. Treat GoF as the canonical finite
pattern catalog for object-oriented design seams. Do not confuse "all GoF
patterns" with "all architecture ideas." GoF comparison is mandatory when a
pattern-shaped seam exists, but direct design still wins when repository facts
prove it is simpler and stronger.

## How to Use This Catalog

- Read this file after `source-article.md` has framed the design problem.
- Start with the routing tables, then read the candidate pattern cards plus
  their nearest neighbors.
- Choose by intent, stable core, true variation, ownership, and verification
  seam, not by class-diagram resemblance.
- Extract teaching material, not just labels: stable core, variation,
  repository fit, rejected neighbors, misuse risk, and task-declared checks.
- If no GoF pattern fits better than a direct design, say so explicitly.

## Quick Routing by Design Question

| If the design question is about... | Start with | Compare with |
| --- | --- | --- |
| One goal, many algorithms | Strategy | State, Template Method |
| One lifecycle, many valid states | State | Strategy, Template Method |
| One fixed process, varying local steps | Template Method | Strategy, Facade |
| One object versus one compatible family | Factory Method | Abstract Factory, Builder, Prototype |
| Complex construction order and invariants | Builder | Factory Method, Prototype |
| Copying a prepared object | Prototype | Builder, Factory Method |
| Legacy translation versus control or enhancement | Adapter | Decorator, Proxy |
| Two independent axes of variation | Bridge | Strategy, Abstract Factory |
| Part-whole tree structure | Composite | Visitor, Iterator |
| Layered responsibilities versus controlled access | Decorator | Proxy, Adapter |
| Repeated subsystem orchestration | Facade | Mediator, Template Method |
| High object count and memory pressure | Flyweight | Prototype, normal objects |
| Access before work happens | Proxy | Decorator, Facade |
| Ordered optional handling | Chain of Responsibility | Observer, Command |
| Operation needs queueing, audit, or undo | Command | Chain of Responsibility, Memento |
| Small stable DSL grammar | Interpreter | Strategy, direct parser |
| Traversal independent of storage | Iterator | Composite |
| Coupled peers with mesh communication | Mediator | Facade, Observer |
| Undo or checkpoints | Memento | Command |
| Many consumers reacting to one fact | Observer | Chain of Responsibility, Command |
| Semantic uniqueness scope | Singleton | Factory Method, container lifetime |
| New operations over stable heterogeneous elements | Visitor | Composite, Strategy |

## Non-Negotiable Distinctions

- Decorator / Proxy / Adapter: enhancement / control / translation.
- Factory Method / Abstract Factory / Builder / Prototype: one product choice /
  family choice / staged assembly / copying.
- Strategy / State / Template Method: selected algorithm / lifecycle behavior /
  fixed skeleton.
- Observer / Chain / Command: broadcast fact / ordered propagation /
  represented operation.
- Facade / Mediator: simplify subsystem access / coordinate peers.
- Composite / Visitor / Iterator: tree structure / new operations over stable
  elements / traversal protocol.
- Bridge / Strategy: two durable axes of variation / one algorithm slot.

## Category Comparison

### Creational Pattern Boundaries

| Pattern | Stable core | Variation | Use when | Reject when |
| --- | --- | --- | --- | --- |
| Abstract Factory | Product-family contract | Whole compatible family switches together | One theme, vendor, platform, or stack changes as one unit | Only one product varies |
| Builder | Final object contract | Construction order or optional steps | Construction invariants matter more than one-shot instantiation | Object is small and direct construction is obvious |
| Factory Method | Product interface | Which concrete product gets created | Callers should not know concrete creation choice | A constructor or function is already clear enough |
| Prototype | Prepared baseline object | Cloned variants | Copying is safer or cheaper than reconstructing | Copy semantics are dangerous or unclear |
| Singleton | Uniqueness scope | Access point or lifetime management | Semantic uniqueness is a real business constraint | It is only avoiding dependency injection |

### Structural Pattern Boundaries

| Pattern | Stable core | Variation | Use when | Reject when |
| --- | --- | --- | --- | --- |
| Adapter | Target interface | Legacy source shape | Boundary translation is the real problem | The model itself is wrong |
| Bridge | Abstraction contract | Independent implementation axis | Two dimensions evolve independently | Only one dimension varies |
| Composite | Component contract | Tree depth and aggregation | Leaves and containers must be treated uniformly | Shared contract would be dishonest |
| Decorator | Wrapped component contract | Optional stacked responsibilities | Additive behavior must stay composable | The real need is access control |
| Facade | High-level use case | Internal subsystem choreography | Callers repeat the same orchestration | It would become a god object |
| Flyweight | Intrinsic immutable state | Extrinsic context | Measured object count creates memory pressure | There is no real memory problem |
| Proxy | Subject interface | Access policy, remoteness, or load timing | Access semantics differ from direct access | There is only additive enhancement |

### Behavioral Pattern Boundaries

| Pattern | Stable core | Variation | Use when | Reject when |
| --- | --- | --- | --- | --- |
| Chain of Responsibility | Request contract | Ordered handlers | Who handles the request must stay pluggable | Every handler must always run |
| Command | Operation contract | Execution time or receiver | Operations need audit, queueing, undo, retry | A plain call is enough |
| Interpreter | Grammar model | Expression composition | Rules have become a small language | Grammar growth is already large |
| Iterator | Traversal contract | Storage representation | Traversal must hide aggregate internals | Native iteration already solves it |
| Mediator | Peer roles | Coordination rules | Peer mesh coupling is the main pain | There is only one public entry point issue |
| Memento | Originator encapsulation | Snapshot history | State restoration must preserve encapsulation | External side effects define the system state |
| Observer | Published fact | Subscriber set | One fact fans out to many reactions | Ordered single-path handling is required |
| State | Context role | Lifecycle state behavior | Behavior changes follow explicit state transitions | Trivial conditionals are sufficient |
| Strategy | Stable goal | Algorithm family | Same job has multiple replaceable algorithms | Branches are few and stable |
| Template Method | Algorithm skeleton | Local step implementation | Sequence is fixed and must stay fixed | Steps vary independently and favor composition |
| Visitor | Element structure | Added operations | Structure is stable but operations keep growing | Element types are changing rapidly |

## Pattern Cards

### Creational Patterns

#### Abstract Factory

- Intent: Create compatible product families that must switch together.
- Stable core vs variation: The family contract stays fixed; the concrete
  family varies by platform, vendor, theme, or environment.
- Best-fit signals: Multiple products must stay mutually compatible.
- Bad-fit signals: Only one product varies or family consistency is not a real
  requirement.
- Compare with: Factory Method for one product choice; Builder for one complex
  object.
- Validation seam: Forbid mixed families, test full family combinations.
- AI misuse: Inventing parallel factories before a real family boundary exists.

#### Builder

- Intent: Assemble one complex object through ordered or optional steps while
  preserving invariants.
- Stable core vs variation: The final object contract stays fixed; construction
  sequence, defaults, or optional steps vary.
- Best-fit signals: Construction order matters or partial construction is
  invalid.
- Bad-fit signals: The object is small and direct construction is readable.
- Compare with: Prototype when copying is better; Factory Method when only the
  concrete product choice varies.
- Validation seam: Test incomplete sequences, defaults, invariants, and final
  immutability.
- AI misuse: Replacing a normal constructor with ceremonial chained builders.

#### Factory Method

- Intent: Defer one concrete product choice from callers to a creator seam.
- Stable core vs variation: Product interface stays fixed; chosen concrete type
  varies.
- Best-fit signals: Callers should not know or branch on concrete products.
- Bad-fit signals: A plain constructor function is already clear and stable.
- Compare with: Abstract Factory for family-level choice; Builder for staged
  construction.
- Validation seam: Test selection logic, lifecycle errors, and wrong-type
  rejection.
- AI misuse: Creating trivial factory layers with no real creation complexity.

#### Prototype

- Intent: Create variants by copying a configured baseline object.
- Stable core vs variation: Prepared baseline stays fixed; copied variants
  change selectively after cloning.
- Best-fit signals: Initialization is expensive or shared setup is large.
- Bad-fit signals: Deep-copy semantics are unsafe or resource handles must not
  be duplicated.
- Compare with: Builder for staged assembly; Factory Method for product choice.
- Validation seam: Test deep versus shallow copy, identity separation, and
  nested mutable state.
- AI misuse: Using copy semantics to hide poorly modeled configuration.

#### Singleton

- Intent: Enforce a declared semantic uniqueness scope.
- Stable core vs variation: Uniqueness contract stays fixed; access path or
  scope enforcement varies.
- Best-fit signals: A resource is semantically unique, not merely convenient to
  access.
- Bad-fit signals: The real motive is avoiding dependency injection.
- Compare with: Container-managed lifetime, Factory Method, explicit registry.
- Validation seam: Test scope, reset behavior, and concurrency semantics.
- AI misuse: Turning global mutable state into a pseudo-pattern.

### Structural Patterns

#### Adapter

- Intent: Translate an incompatible legacy or third-party interface into the
  target interface.
- Stable core vs variation: Target contract stays fixed; source interface shape
  varies.
- Best-fit signals: Translation at a boundary is the real problem.
- Bad-fit signals: The source model itself is conceptually wrong.
- Compare with: Decorator for enhancement; Proxy for controlled access.
- Validation seam: Contract-test parameter, error, and version translation.
- AI misuse: Hiding a wrong domain model behind a thin translation shim.

#### Bridge

- Intent: Separate two independent axes of variation to avoid subclass
  cross-products.
- Stable core vs variation: Abstraction contract stays fixed; implementation
  axis varies independently.
- Best-fit signals: Class count grows by combinations of two dimensions.
- Bad-fit signals: Only one dimension truly evolves.
- Compare with: Strategy for one algorithm slot; Abstract Factory for family
  creation.
- Validation seam: Test that each axis can evolve without touching the other.
- AI misuse: Adding indirection before there is evidence of two durable axes.

#### Composite

- Intent: Treat leaf and part-whole tree elements uniformly.
- Stable core vs variation: Component contract stays fixed; tree depth and
  composition vary.
- Best-fit signals: Callers repeatedly distinguish leaves from containers.
- Bad-fit signals: Shared contract forces dishonest or empty operations.
- Compare with: Visitor for new operations; Iterator for traversal.
- Validation seam: Test empty trees, deep trees, cycle prevention, and leaf
  restrictions.
- AI misuse: Forcing uniformity when containers and leaves do not share honest
  semantics.

#### Decorator

- Intent: Stack optional responsibilities without subclass combinations.
- Stable core vs variation: Wrapped component contract stays fixed; additive
  responsibilities vary.
- Best-fit signals: Logging, retry, caching, compression, tracing, or similar
  orthogonal enhancements must compose.
- Bad-fit signals: The actual need is authorization, remoteness, or lazy load.
- Compare with: Proxy for access control; Adapter for translation.
- Validation seam: Test stacked order, failure propagation, and identity
  expectations.
- AI misuse: Using wrappers with no independent responsibility, only extra
  indirection.

#### Facade

- Intent: Give callers one high-level interface over repeated subsystem
  choreography.
- Stable core vs variation: External use case stays fixed; internal
  orchestration varies.
- Best-fit signals: Many callers repeat the same multi-service sequence.
- Bad-fit signals: Internal coordination rules belong to peers, not callers.
- Compare with: Mediator for peer coordination; Template Method for fixed
  skeleton inside one hierarchy.
- Validation seam: Test ordering, compensations, partial failures, and caller
  decoupling.
- AI misuse: Growing the facade into a god object for unrelated use cases.

#### Flyweight

- Intent: Share intrinsic immutable state when object count creates measured
  memory pressure.
- Stable core vs variation: Intrinsic state stays shared; extrinsic context
  varies per use.
- Best-fit signals: Many tiny objects repeat the same immutable payload.
- Bad-fit signals: There is no proven memory bottleneck.
- Compare with: Prototype for copied prepared objects; normal objects for
  straightforward models.
- Validation seam: Benchmark memory, test immutability, cache lifetime, and
  thread safety.
- AI misuse: Premature optimization that destroys model clarity.

#### Proxy

- Intent: Preserve a subject interface while controlling authorization, lazy
  load, remote access, cache, or transactions.
- Stable core vs variation: Subject contract stays fixed; access semantics
  vary.
- Best-fit signals: Direct access is not semantically equivalent to mediated
  access.
- Bad-fit signals: The added logic is only orthogonal enhancement.
- Compare with: Decorator for enhancement; Facade for simplified entry points.
- Validation seam: Test allowed and denied paths, cache invalidation, remote
  failures, and timeout behavior.
- AI misuse: Calling every wrapper a proxy even when it only adds logging.

### Behavioral Patterns

#### Chain of Responsibility

- Intent: Pass a request through ordered optional handlers until handled or
  exhausted.
- Stable core vs variation: Request contract stays fixed; handler chain and
  ordering vary.
- Best-fit signals: Who handles the request must remain pluggable.
- Bad-fit signals: Every step must always execute.
- Compare with: Observer for broadcast; Command for represented operations.
- Validation seam: Test no-handler, ordering, short-circuit, error handling,
  and cycle prevention.
- AI misuse: Hiding business policy in opaque chains with no observability.

#### Command

- Intent: Represent an operation for queueing, audit, retry, scheduling, remote
  dispatch, or undo.
- Stable core vs variation: Operation contract stays fixed; receiver, timing,
  and persistence vary.
- Best-fit signals: Operations must survive beyond the immediate call stack.
- Bad-fit signals: A direct call is enough and no operation lifecycle exists.
- Compare with: Chain for optional handling; Memento for state snapshots.
- Validation seam: Test serialization, authorization, idempotency, retry, and
  compensation.
- AI misuse: Wrapping plain function calls as command classes without an
  operation lifecycle.

#### Interpreter

- Intent: Represent and evaluate a small stable DSL grammar through expression
  objects.
- Stable core vs variation: Grammar model stays fixed; expressions vary through
  composition.
- Best-fit signals: Rules have become a language, not just configuration
  values.
- Bad-fit signals: Grammar is rapidly growing or requires industrial parser
  tooling.
- Compare with: Strategy for algorithm choice; direct parsers for simple syntax.
- Validation seam: Test precedence, syntax errors, limits, and diagnostics.
- AI misuse: Building a home-grown language when plain data structures would do.

#### Iterator

- Intent: Traverse an aggregate without exposing its internal representation.
- Stable core vs variation: Traversal contract stays fixed; storage and
  traversal implementation vary.
- Best-fit signals: Callers need uniform traversal over different containers.
- Bad-fit signals: Native language iteration already solves the problem.
- Compare with: Composite for trees; Visitor for operations over elements.
- Validation seam: Test empty, paginated, mutating, cancelled, and resourceful
  traversal.
- AI misuse: Rebuilding custom iteration layers where built-in iteration is the
  correct seam.

#### Mediator

- Intent: Centralize complex peer coordination so peers do not form a coupling
  mesh.
- Stable core vs variation: Peer roles stay fixed; coordination rules vary in
  one place.
- Best-fit signals: Peer objects know too much about one another.
- Bad-fit signals: The problem is only an external convenience API.
- Compare with: Facade for external simplification; Observer for fact
  notification.
- Validation seam: Test state transitions, prohibited direct coupling, and
  conflict rules.
- AI misuse: Creating a mediator that becomes a giant dumping ground.

#### Memento

- Intent: Capture and restore state without exposing internals.
- Stable core vs variation: Originator encapsulation stays fixed; snapshot
  history varies.
- Best-fit signals: Undo, checkpoints, or branchable local state are real
  requirements.
- Bad-fit signals: External side effects dominate system state.
- Compare with: Command for replaying operations.
- Validation seam: Test restoration, branching, redaction, and version
  compatibility.
- AI misuse: Pretending snapshots solve externally visible side effects.

#### Observer

- Intent: Broadcast a fact to independent subscribers without making the
  publisher know consumers.
- Stable core vs variation: Published fact stays fixed; subscriber set varies.
- Best-fit signals: One event fans out to many optional reactions.
- Bad-fit signals: Ordered single-path handling is required.
- Compare with: Chain for ordered propagation; Command for durable operations.
- Validation seam: Test ordering assumptions, failure isolation, retries,
  idempotency, and consistency boundaries.
- AI misuse: Turning every side effect into an event without consistency design.

#### State

- Intent: Change context behavior according to explicit lifecycle state and
  transitions.
- Stable core vs variation: Context role stays fixed; state-specific behavior
  varies by lifecycle phase.
- Best-fit signals: Behavior changes are driven by real state transitions.
- Bad-fit signals: There are only a few stable branches with no lifecycle
  model.
- Compare with: Strategy for selected algorithms; Template Method for fixed
  process skeleton.
- Validation seam: Test transition tables, illegal states, concurrency, and
  recovery.
- AI misuse: Splitting trivial branching into many state classes.

#### Strategy

- Intent: Swap a family of algorithms serving one stable goal.
- Stable core vs variation: Goal stays fixed; chosen algorithm varies.
- Best-fit signals: One job has multiple legitimate algorithms.
- Bad-fit signals: Branches are few, stable, and not growing.
- Compare with: State for lifecycle-driven behavior; Template Method for a
  fixed skeleton with varying steps.
- Validation seam: Test each algorithm, selection logic, fallback, and edge
  cases.
- AI misuse: Creating interfaces for one stable algorithm just to look modular.

#### Template Method

- Intent: Fix algorithm order and invariants while deferring local steps to
  subclasses.
- Stable core vs variation: Process skeleton stays fixed; local steps vary.
- Best-fit signals: Sequence is invariant and callers must not reorder it.
- Bad-fit signals: Steps vary independently and composition is cleaner.
- Compare with: Strategy for injected algorithms; Facade for external
  orchestration.
- Validation seam: Test ordering, invariant preservation, subclass hooks, and
  forbidden overrides.
- AI misuse: Building fragile inheritance hierarchies for logic that wants
  composition.

#### Visitor

- Intent: Add operations across a stable heterogeneous element structure
  through double dispatch.
- Stable core vs variation: Element structure stays fixed; operations vary.
- Best-fit signals: New operations keep arriving while element types are
  stable.
- Bad-fit signals: Element types are changing rapidly.
- Compare with: Composite for tree structure; Strategy for algorithm slots.
- Validation seam: Test every visitor-element pair and missing-operation
  behavior.
- AI misuse: Applying Visitor to unstable models and paying full ripple cost on
  every new element.

## Teaching Checklist

For each candidate, explain the changing thing, stable core, collaborators and
dependency direction, lifecycle and ownership, direct alternative, nearest
patterns rejected, failure semantics, and normal, boundary, failure,
integration, concurrency, and performance checks where relevant.

## Approval-Ready Pattern Decision Template

Use this structure whenever a GoF pattern is selected or rejected inside a
design bundle:

```md
### Pattern Decision
- Candidate:
- Category:
- Repository seam:
- Stable core:
- Real variation:
- Why it fits:
- Simpler direct design considered:
- Neighbor patterns rejected:
- Misuse risk if forced:
- Verification seam:
```
