# Coordinate delivery

Read this workflow for an active Sprint on `sprint.started`, `sprint-backlog.changed`, `developer.question`, or `sprint.impediment`.

1. Signal `developer.work-available`; let Developers pull and coordinate their own work.
2. Observe Sprint Backlog state, questions, test results, bugs, fixes, retests, Increment Documentation, and Product Owner assessments.
3. Keep completed PBI and Bug artifacts in the Sprint Backlog as history. Change their workflow state instead of deleting them.
4. Put every open Sprint bug above non-bug work. Let a Programmer fix it and a Tester independently retest it before normal Sprint work resumes.
5. Route product-intent questions to the Product Owner and keep technical decisions with Developers.
6. Allow explicit Sprint Backlog adaptation. Developers may add technical work; scope changes involving PBIs require collaboration with the Product Owner and must protect the Sprint Goal.
7. When scope is removed or the Sprint ends with unfinished work, move each unfinished PBI, Bug, or other work artifact back to `product-backlog/items/`, preserve its ID and history, and record the return and rationale in the Sprint Backlog index. Let the Product Owner order returned work.
8. If work stalls, expose the impediment and coordinate a decision. Never spin indefinitely or mark blocked work Done.
