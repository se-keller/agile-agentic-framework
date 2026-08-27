# Plan testing

Read this workflow on `planning.pbi.clarified` or when directly planning quality work.

1. Inspect the proposed PBI, Acceptance Criteria, Definition of Done, known risks, and Product Owner clarification. Do not inspect Product Code or execute tests merely because Planning began.
2. Define business-facing test cases and representative examples with the Product Owner. Let the Product Owner clarify users, intended behavior, business rules, and expected outcomes.
3. Make each business-facing case traceable to one or more Acceptance Criteria and add it to the pending Developer Plan before the Programmer plans implementation.
4. After `planning.pbi.implementation-planned`, review the proposed implementation and automated-test coverage for testability. Ask the Programmer questions and add testing activities, environments, dependencies, and material risks to the pending plan.
5. Keep automation mechanics with Developers; the Programmer implements and executes automated acceptance tests. Reserve independent UI and exploratory execution for a meaningful `implementation.testable` handoff, without waiting for all Sprint PBIs to finish.
