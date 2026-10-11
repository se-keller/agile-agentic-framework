# Participate in Sprint Planning

Read this workflow on `planning.pbi.presented` or when directly participating in Sprint Planning.

1. For each Product Owner-proposed PBI, first ask only questions needed to understand product intent. Let the Product Owner decide and record product clarification; do not silently choose ambiguous behavior.
2. Let the Tester first contribute business-facing test cases and representative examples. Let the Programmer then contribute implementation approach, automated acceptance-test coverage, engineering tests, dependencies, risks, and sequence. Let the Tester review that plan for testability and add material gaps.
3. Make a brief delivery-shape check using the shared [Product Backlog Item Splitting skill](../../../product-backlog-item-splitting/SKILL.md). Raise an alternative split only when it would materially avoid coordination, loops, technical risk, or implementation overhead, or improve a vertical Increment. Explain the technical evidence and product-outcome trade-off; do not split into technical-layer tasks, order the alternatives, or silently rewrite the PBI. Route a material proposal to the Product Owner, who decides whether to change the PBI before selection.
4. Do not execute Product Code, automated acceptance tests, UI tests, or exploratory tests while this Planning sequence is still in progress.
5. Help Developers collectively forecast which planned PBIs they can complete without treating the forecast as an externally assigned commitment.
6. Let the Product Owner propose the value-focused selection and a Sprint Goal. Collaborate with the Product Owner, Scrum Master, other Developers, and participating human to agree the final Sprint Goal; the Scrum Master only facilitates.
7. Keep estimates, implementation approach, sequencing, integration strategy, testing approach, and technical risk decisions with Developers.
8. After agreement, create `developer-plan.md` in the Sprint directory and the Sprint Backlog below `sprint-backlog/`; keep the agreed Sprint Goal at `sprint-backlog/sprint-goal.md`.
9. Move selected PBI artifacts from `product-backlog/items/` into the Sprint's `sprint-backlog/`, preserving their IDs and frozen filenames and updating affected links.
10. Make the plan sufficient to begin while expecting it to evolve as more is learned.
