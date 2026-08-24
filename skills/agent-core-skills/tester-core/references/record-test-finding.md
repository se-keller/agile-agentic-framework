# Record a test finding

Read this workflow when observed behavior clearly contradicts an expectation.

1. Create a linked OKF Bug artifact inside the active Sprint Backlog, using a stable ID and a readable filename such as `bug-0001-short-slug.md`.
2. Record the related PBI and Acceptance Criterion, environment, preconditions, reproduction steps, expected behavior, actual behavior, evidence, impact, and discovery source.
3. Set a domain workflow field such as `bug_state: open`; do not misuse OKF `status` as the bug workflow state.
4. Add the Bug above every non-bug entry in the authoritative Sprint Backlog order.
5. Signal `test.finding` so a Programmer sees the work. Open Sprint Bugs always take priority over other Sprint Backlog work.
6. Continue other safe testing while the Bug is being fixed when possible.

If expected behavior is unclear, record the finding without falsely classifying it as a confirmed Bug and ask the Product Owner through `developer.question`. Either the Tester or Programmer may ask; state the product decision needed and its impact.
