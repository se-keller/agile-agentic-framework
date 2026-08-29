# Plan a Sprint

Read this workflow for readiness checking, `sprint.planning-requested`, or `sprint.planning-started`.

## Check readiness

Start Sprint Planning only when all conditions are visible:

- a human-confirmed Product Vision and current Product Goal exist;
- the Product Backlog is ordered by the Product Owner;
- at least one PBI satisfies the Definition of Ready;
- the Definition of Done exists;
- a Product Owner, at least one configured Developer, and the configured Scrum Master are available as separate resumable runtime agents; and
- no other Sprint is active.

If a condition is missing, route it to the accountable agent. Do not manufacture product direction, facilitation, or technical capacity in the host.

## Run Sprint Planning

Activate participants just in time. Activate the Scrum Master for Planning facilitation, but keep lifecycle state inspection, routing, and transitions in the host. Do not activate the Programmer and Tester together merely because Planning began, and do not emit `sprint.started`, `developer.work-available`, or `implementation.testable` until every selected PBI has completed the Planning sequence and the Sprint Backlog is agreed.

1. Resume the Product Owner with `sprint.planning-started` and activate or resume the configured Scrum Master to facilitate the event. Preserve both runtime identifiers. The Scrum Master does not request participants or own lifecycle transitions.
2. Let the Product Owner inspect whether the current Product Goal was achieved. If it was, collaborate with the human on the next Product Goal before selecting work. Let the Product Owner order all available PBIs, including returned Bugs, against the Product Vision and current Product Goal. If too little ready work exists, let the Product Owner create or refine PBIs with the human as needed.
3. For each PBI the Product Owner proposes for this Sprint, run this sequence before considering the next PBI:
   1. The Product Owner presents the PBI's problem, value, outcome, Acceptance Criteria, and constraints (`planning.pbi.presented`).
   2. Activate the Programmer and Tester, as separate agents, only for understanding questions. They send product-intent questions as `planning.pbi.clarification-requested`; the Product Owner decides and records clarified or newly learned product information in the PBI (`planning.pbi.clarified`).
   3. The Tester records business-facing test cases and representative examples in the pending Developer Plan (`planning.pbi.quality-planned`). This is planning only: no Product Code, automated acceptance test, UI, exploratory, or execution test may be run yet.
   4. The Programmer records the proposed implementation approach, automated acceptance-test coverage, engineering tests, dependencies, risks, and sequence in the pending Developer Plan (`planning.pbi.implementation-planned`).
   5. The Tester reviews that implementation plan for testability, asks the Programmer any necessary questions, and adds material quality risks or gaps (`planning.pbi.plan-reviewed`).
4. Repeat the PBI sequence for every candidate. Planning evidence may remain a pending plan while candidates are discussed; do not move a PBI or begin delivery until the resulting Sprint Backlog is agreed.
5. The Product Owner proposes the value-focused Sprint selection and a Sprint Goal. Programmers and Testers collectively forecast feasibility, confirm that the plan and quality evidence are sufficient, and request changes where needed. The Scrum Team, with the human where available, agrees the final Sprint Goal and Sprint Backlog. The Scrum Master facilitates this agreement when needed but never supplies the Goal's product content.
6. Have the Developers create `sprint-NNNN-short-goal-slug/` only after the Sprint Goal and selection are established. Freeze the directory name when the Sprint starts.
7. Have the Developers materialize the agreed pending plan as `developer-plan.md` in the Sprint directory and store the agreed Sprint Goal at `sprint-backlog/sprint-goal.md` beside `sprint-backlog/index.md` and the selected work artifacts. They use OKF frontmatter for concept artifacts and maintain `created` and `updated` dates.
8. Have the Developers move each selected PBI artifact from `product-backlog/items/` into the Sprint's `sprint-backlog/`. They preserve its stable ID and frozen filename, update affected links and workflow fields, and never duplicate the authoritative artifact.
9. Have the Product Owner remove selected PBIs from the available Product Backlog order and the Developers link them from the Sprint Backlog index.
10. Signal `sprint.started` only when the Sprint Goal, selection, moved PBIs, and complete initial Developer Plan are inspectable. Then let the Programmer pull the first PBI; do not send the Tester an execution request before the Programmer signals `implementation.testable`.
