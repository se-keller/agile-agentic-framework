# Plan implementation

Read this on `planning.pbi.quality-planned`, for implementation planning, or for collaborative acceptance-test definition.

1. Inspect the proposed PBI, Acceptance Criteria, pending Developer Plan, Product Code, existing tests, constraints, and the Tester's business-facing cases. Do not wait for the Sprint Goal or selected Sprint Backlog when the PBI is being planned.
2. Collaborate with the other Developers on implementation sequence, integration, testing strategy, technical risks, and dependencies.
3. Make technical choices independently within product constraints. Keep the Product Owner focused on users, value, outcomes, and expected behavior.
4. Record material architecture decisions, migrations, dependencies, risks, and rollback considerations in the Developer Plan or a linked technical artifact.
5. Adapt the plan as implementation reveals new information.

## Define acceptance tests collaboratively

1. Translate the Tester's business-facing cases into automated acceptance-test scenarios jointly with the Tester and relevant Programmers before or during implementation.
2. Let the Product Owner clarify intended behavior, user value, business rules, and representative examples.
3. Let Developers own the technical test design, automation approach, fixtures, environments, and execution strategy.
4. Make every scenario traceable to one or more Acceptance Criteria.
5. Expose ambiguity or conflicting expectations through `developer.question` instead of silently choosing product behavior.
