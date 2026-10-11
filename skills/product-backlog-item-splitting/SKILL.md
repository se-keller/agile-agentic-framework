---
name: product-backlog-item-splitting
description: Split oversized Product Backlog Items into appropriately small, valuable, testable vertical slices. Use while creating or refining PBIs before Sprint selection; do not use to divide implementation tasks by technical layer.
---

# Product Backlog Item Splitting

Make PBI splitting the normal refinement practice. The Scrum Team collaborates to find useful slices: the Product Owner remains accountable for product intent, PBI content, and Product Backlog order; Developers contribute feasibility, risk, and testability knowledge without turning PBIs into technical tasks.

The Product Owner applies this skill when first writing or refining PBIs. During Planning, Developers make a brief delivery-shape check of each proposed slice. They should raise an alternative only when the proposed cut would create material avoidable coordination, feedback loops, technical risk, or implementation overhead, or when another vertical cut would improve the Increment. A Developer proposal explains the trade-off and preserves the same product outcome; it does not set priority, redefine value, or decide the Product Backlog. The Product Owner decides whether to adopt it and updates the PBI when the product knowledge changes.

Start with a PBI that describes a user-visible change in system behavior and its value. If it is a component, infrastructure task, or implementation step, combine it with the missing work until it represents an increment of value. Split into thin vertical slices that may span architectural layers as needed to deliver an observable outcome. Do not split by UI, database, API, or other technical layer.

## Assess the item and its slices

Use INVEST as a decision aid:

- **Independent:** can be ordered for value or risk rather than mainly technical dependency.
- **Negotiable:** leaves product and implementation details open for collaboration at the appropriate time.
- **Valuable:** delivers a visible user outcome; it need not be independently releasable.
- **Estimable:** Developers have enough shared understanding to estimate it.
- **Small:** near the top of the Product Backlog, prefer a size that would allow roughly 6–10 comparable PBIs in a Sprint, adjusted for the product's Sprint length, team, and capacity.
- **Testable:** has observable Acceptance Criteria or other concrete evidence of the changed behavior.

Favor several small, coherent PBIs over one large PBI when this creates earlier value, feedback, learning, or prioritization options. Do not split mechanically: keep a slice whole when further division would remove a meaningful user outcome or independence, make it untestable, or create coordination overhead that outweighs the benefit.

## Find a useful split

Locate the main complexity and the variations around it, then seek one complete slice through that complexity with fewer variations. Explore applicable patterns; try more than one when useful:

1. **Workflow steps:** deliver a simple end-to-end path first, then add middle steps, exceptions, or review stages. Do not automatically make each workflow step its own PBI.
2. **Operations:** separate distinct operations, such as create, read, update, or cancel.
3. **Business-rule variations:** isolate rules that change the same outcome.
4. **Data variations:** start with one representative data type, locale, region, entity, or range, then add others as evidence warrants.
5. **Data-entry methods:** begin with the simplest usable interaction, then add richer input methods.
6. **Major effort:** expose an initial representative choice or integration separately from later, cheaper variants; keep dependencies explicit.
7. **Simple/complex:** retain the smallest useful core and move variations and edge cases into follow-up PBIs.
8. **Defer performance or another non-functional concern:** first make the valuable behavior work, then improve the relevant quality attribute only when the initial slice remains honest about its limits and does not create unmanaged debt.
9. **Time-boxed spike:** use only after the other patterns cannot reduce material implementation uncertainty. State the questions to answer and stop when they are answered; use what is learned to create or refine valuable implementation PBIs.

Choose the split that makes lower-value work easiest to defer or discard and that produces more evenly sized, independently orderable slices. In complex work, create only the first one or two valuable learning slices instead of pretending the entire future scope is known.

For each resulting PBI, preserve or establish its user, desired behavior, value, Acceptance Criteria, material assumptions, and relationship to the original scope. Retire the oversized PBI or replace it without duplicating the same scope in the Product Backlog. Apply the product's Definition of Ready before Sprint selection.

## Source

This skill is based primarily on [The Humanizing Work Guide to Splitting User Stories](https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/), including its INVEST guidance, vertical-slice framing, splitting patterns, and evaluation heuristics.
