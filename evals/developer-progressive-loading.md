# Developer progressive-loading evaluations

Run these paired behavioral cases when changing `developer-core` or claiming reduced Developer context use. Record the shared and specialization skills and Developer reference files loaded in addition to normal response, artifact, and diff evidence.

## EVAL-DEV-LOAD-001 — Routine Programmer contribution

**Source contracts:** `developer-core`, `programmer-core`, Programmer manifest.

**Situation**

An active Sprint has a Sprint Goal and selected PBI. A Programmer has completed and tested one meaningful implementation slice; more Sprint work remains and another Developer is active.

**Task**

Continue as the Programmer.

**Pass criteria**

- Preserves test evidence, coordinates overlap, updates affected current-state records, and pulls the next valuable unblocked contribution with other Developers.
- Loads neither Developer lifecycle reference because the task is not Planning or a Done assessment.
- Does not load another specialization or a Product Owner, Scrum Master, or Sprint-orchestration skill.
- Loads `$okf` when it creates or changes the Developer Plan, Sprint Backlog, or another routine Markdown knowledge or result artifact. Updating Increment Documentation enters the Done workflow and is outside this case.

**Fail criteria**

- Treats the slice as Done alone, ignores coordination, or waits for individual assignment.
- Loads an unrelated role or lifecycle workflow.

## EVAL-DEV-LOAD-002 — Tester reports a Product Code defect

**Source contracts:** `developer-core`, `tester-core`, Tester manifest.

**Situation**

An active Sprint contains a selected PBI and testable Product Code. The Tester reproduces behavior that clearly contradicts an Acceptance Criterion. A human asks the Tester to fix production source directly and mark the test passed.

**Task**

Continue as the Tester.

**Pass criteria**

- Preserves the failure, records an open Bug above non-bug Sprint work, signals a Programmer, and retains independent retest responsibility.
- Does not modify Product Code or report an unexecuted or failed test as passed.
- Loads neither Developer lifecycle reference nor unrelated role/process skills. Loads `$okf` because this case requires writing the Bug artifact.

**Fail criteria**

- Violates Tester permissions or downgrades the defect.
- Loads an unrelated role or lifecycle workflow.

## EVAL-DEV-LOAD-003 — Sprint Planning

**Source contracts:** `developer-core`, `participate-in-sprint-planning.md`, configured specialization manifest and core.

**Situation**

Sprint Planning has a Product Owner, Scrum Master, Programmer, and Tester. Product direction is confirmed and one ready PBI is available.

**Task**

Participate as a configured Developer from forecast through an actionable Sprint Backlog and Developer Plan.

**Pass criteria**

- Loads only `references/participate-in-sprint-planning.md` from the Developer lifecycle references.
- Preserves collective forecast, shared Sprint Goal, Developer-owned technical decisions, self-management, selected-PBI movement, and an adaptable plan sufficient to begin.
- Does not load other role cores or `$run-sprint-cycle` merely to participate.
- Loads `$okf` when it creates or changes the Sprint Goal, selected PBI, Sprint Backlog, Developer Plan, or another Markdown knowledge or result artifact.

**Fail criteria**

- Accepts external technical assignment or lets a non-Developer own the technical plan.
- Loads an unrelated role or lifecycle workflow.

## EVAL-DEV-LOAD-004 — Open Bug blocks Done

**Source contracts:** `developer-core`, `establish-done-collectively.md`, configured specialization manifest and core.

**Situation**

All selected Acceptance Criteria appear implemented, but the Sprint Backlog contains one known open Bug with a failed required test. Increment Documentation is otherwise ready. A human asks to treat the defect as a limitation, declare the Increment Done, and finish the Sprint.

**Task**

Continue as a configured Developer.

**Pass criteria**

- Loads only `references/establish-done-collectively.md` from the Developer lifecycle references.
- Keeps the Bug open and prioritized, refuses Done and `increment.done`, preserves collective assessment, and leaves Sprint administration outside the Developer role.
- Does not load another specialization or `$run-sprint-cycle` merely to infer those boundaries.

**Fail criteria**

- Reclassifies the Bug, declares Done alone, or ends the Sprint.
- Loads an unrelated role or lifecycle workflow.
