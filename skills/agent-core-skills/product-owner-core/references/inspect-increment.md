# Inspect an Increment

Read this workflow on `increment.documentation-ready` or another explicit Increment inspection.

1. Load the referenced Increment Documentation.
2. Review the outcome, instructions, test evidence, change references, known limitations, referenced Product Backlog Items, and Sprint Goal.
3. Run the Increment locally when that improves inspection and is safe. For browser-visible WebApp behavior, load `$webapp-ui-testing` and inspect it through the runtime's built-in interactive browser when available.
4. Assess the Increment against the Product Backlog Item, Acceptance Criteria, Sprint Goal, Product Goal, and Product Vision, including value, usability, intended effect, and relevant limitations.
5. Keep three decisions distinct: whether work is Done, what product feedback emerges, and whether humans choose to release or demonstrate the Increment.
6. Never call an Increment approved or rejected by the Product Owner.
7. Record the assessment so Developers can determine whether the inspection criterion in the Definition of Done has been completed; never replace their Definition of Done decision with a Product Owner acceptance gate.
8. When a human wants a change before release or demonstration, preserve any already-Done Increment, record that exposure decision separately, and create linked follow-up work.
9. Create and order a linked Product Backlog Item for every newly requested product change, whether small or large. Do not turn Product Owner inspection into an extension of the completed PBI.
10. Record the Product Owner assessment in or alongside the Increment Documentation without rewriting Developers' evidence or historical facts, then signal `product-assessment.recorded` so both Developers can make their collective Definition of Done decision.
