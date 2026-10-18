---
name: solid-design
description: Apply Robert C. Martin's SOLID principles across programming paradigms. Required by Programmer core for new responsibilities, changed module boundaries, extensions of strongly coupled modules, and independent structure reviews. Use for concrete design pressures, never to impose classes or mechanical splitting.
---

# SOLID design

Use SOLID to make a concrete change safer to understand, extend, and test. Apply the principles to the smallest useful software entity: a module, function, data type, schema, endpoint, command, or protocol. The original papers use object-oriented terms; do not infer that a solution needs classes, inheritance, or language-level interfaces.

## Work from the likely change

Identify the requested behavior, the users or business function asking for it, the observable contract, and the dependencies that the change would touch. Preserve established conventions and choose the smallest design that addresses the actual change. Do not introduce an abstraction, layer, or indirection solely to demonstrate a principle.

Apply the relevant principles as decision tests:

- **Single Responsibility Principle (SRP):** Group behavior that changes for the same reason and is accountable to the same actor; separate behavior that changes for different reasons. A responsibility is not a method count or a rule that every function must be isolated.
- **Open-Closed Principle (OCP):** Where a likely variation is known, arrange the affected entity so behavior can be extended without repeatedly modifying dependable, already-working code. Close only against changes worth anticipating; no design can be closed against every future change.
- **Liskov Substitution Principle (LSP):** When one implementation, variant, or representation is presented in place of another, it must preserve the observable expectations on which its consumer relies. Check inputs, outputs, errors, invariants, ordering, and side effects—not just type compatibility. This check applies to any substitutable contract, whether or not inheritance exists.
- **Interface Segregation Principle (ISP):** Give each consumer the smallest cohesive capability surface it needs. In languages without declared interfaces, apply this to function parameters, returned data, message schemas, endpoints, commands, or imported modules. Do not create a unique surface for every consumer when consumers have the same cohesive need.
- **Dependency Inversion Principle (DIP):** Keep high-level policy from being coupled to volatile implementation details by depending on a stable contract at the relevant boundary. A contract may be a behavior, function signature, data schema, protocol, or language-level interface. Retain a direct dependency when the concrete detail is stable and an abstraction would add no useful boundary.

## Scope refactoring to the current change

The smallest coherent change includes behavior-preserving refactoring needed to keep the affected responsibilities cohesive, dependencies controlled, and behavior testable in isolation. Do not repeatedly append independent concerns to an overloaded module merely because that produces the smallest diff. Keep public contracts and existing behavior stable while making the separation; add characterization or focused regression coverage where needed, then verify the requested behavior separately.

A long file is a review signal, not proof of a design defect. Product-specific file/function sizes, complexity measures, and coupling thresholds may draw attention to a boundary; keep their tools, values, rationale, and exceptions in the product repository. Examine responsibilities and change reasons before deciding to split. Do not mechanically split cohesive code, create layers or abstractions for hypothetical reuse, or refactor unrelated modules to satisfy a metric. Functions, components, and modules can provide sufficient boundaries without classes.

## Independent structure review

Review the actual affected diff and relevant consumers in proportion to the change. A tiny local change may need only a short recorded conclusion; a new responsibility or coupled extension needs inspection of the affected boundaries. Review:

- **Cohesion:** whether each affected entity groups behavior with the same responsibility and reason to change.
- **Coupling:** whether dependencies are necessary, explicit, and directed toward stable contracts at volatile boundaries.
- **Interfaces:** whether consumers receive cohesive capabilities and established observable contracts remain intact.
- **Isolated testability:** whether the affected policy can be exercised without unrelated infrastructure, with appropriate seams and focused evidence.

Record the independent reviewer or capability, reviewed source state or diff, scope, findings, and disposition in the existing plan or handoff evidence; an author's self-review does not supply independence. Remain within the reviewer's permissions: a Tester may inspect source and contribute test evidence, but cannot modify production source. Source inspection before handoff is not independent acceptance-test execution, which still waits for the normal testable/fix-ready handoff.

Fix structural problems required for safe delivery in the current change. A non-blocking structural concern may be deferred only with its exact location and problem, a concrete technical reason and current impact/risk, and an observable trigger for reassessment recorded in the existing plan or linked follow-up work. “Later,” delivery pressure, or file length alone is insufficient. Do not defer known Bugs, failing required checks, or unmet Definition of Done criteria as design debt. If a finding remains unresolved without a justified disposition, withhold the handoff. Relevant structural changes invalidate that part of the review; retain unaffected evidence.

## Make and review changes

For a design or review decision, state the specific pressure that justifies a boundary: a distinct actor or change reason, a likely variation, a consumer contract, or a volatile detail. Prefer evidence from the code and its tests over speculative future flexibility. Verify the resulting observable behavior and the consumers that could be affected; update focused tests when a contract changes.

Do not turn SOLID into a checklist that overrides a product requirement, a simpler design, language idioms, performance constraints, or an established public contract. Explain meaningful trade-offs and leave unrelated code untouched.

## Source discipline

Base interpretations only on Robert C. Martin's original material below. The 1996 papers are linked from Martin's own article collection; the later SRP article clarifies what he means by a reason for change.

- [The original SOLID articles: SRP, OCP, LSP, ISP, and DIP](https://sites.google.com/site/unclebobconsultingllc/uncle-bob-consulting-llc/articles) — Robert C. Martin, 1996.
- [The Single Responsibility Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) — Robert C. Martin, 2014 clarification of SRP.
