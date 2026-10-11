---
name: solid-design
description: Apply Robert C. Martin's SOLID principles to maintainable software design across programming paradigms. Use when designing or reviewing boundaries, dependencies, contracts, and change impact; do not use merely to format code or impose object-oriented structure.
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

## Make and review changes

For a design or review decision, state the specific pressure that justifies a boundary: a distinct actor or change reason, a likely variation, a consumer contract, or a volatile detail. Prefer evidence from the code and its tests over speculative future flexibility. Verify the resulting observable behavior and the consumers that could be affected; update focused tests when a contract changes.

Do not turn SOLID into a checklist that overrides a product requirement, a simpler design, language idioms, performance constraints, or an established public contract. Explain meaningful trade-offs and leave unrelated code untouched.

## Source discipline

Base interpretations only on Robert C. Martin's original material below. The 1996 papers are linked from Martin's own article collection; the later SRP article clarifies what he means by a reason for change.

- [The original SOLID articles: SRP, OCP, LSP, ISP, and DIP](https://sites.google.com/site/unclebobconsultingllc/uncle-bob-consulting-llc/articles) — Robert C. Martin, 1996.
- [The Single Responsibility Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) — Robert C. Martin, 2014 clarification of SRP.
