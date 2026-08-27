# Participate in Sprint Planning

Read this workflow on `planning.pbi.presented` or when directly participating in Sprint Planning.

1. For each Product Owner-proposed PBI, first ask only questions needed to understand product intent. Let the Product Owner decide and record product clarification; do not silently choose ambiguous behavior.
2. Let the Tester first contribute business-facing test cases and representative examples. Let the Programmer then contribute implementation approach, automated acceptance-test coverage, engineering tests, dependencies, risks, and sequence. Let the Tester review that plan for testability and add material gaps.
3. Do not execute Product Code, automated acceptance tests, UI tests, or exploratory tests while this Planning sequence is still in progress.
4. Help Developers collectively forecast which planned PBIs they can complete without treating the forecast as an externally assigned commitment.
5. Let the Product Owner propose the value-focused selection and a Sprint Goal. Collaborate with the Product Owner, Scrum Master, other Developers, and participating human to agree the final Sprint Goal; the Scrum Master only facilitates.
6. Keep estimates, implementation approach, sequencing, integration strategy, testing approach, and technical risk decisions with Developers.
7. After agreement, create `developer-plan.md` in the Sprint directory and the Sprint Backlog below `sprint-backlog/`; keep the agreed Sprint Goal at `sprint-backlog/sprint-goal.md`.
8. Move selected PBI artifacts from `product-backlog/items/` into the Sprint's `sprint-backlog/`, preserving their IDs and frozen filenames and updating affected links.
9. Make the plan sufficient to begin while expecting it to evolve as more is learned.
