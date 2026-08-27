# Sprint-cycle progressive-loading evaluations

Run these paired cases when changing `run-sprint-cycle` or claiming reduced Scrum Master lifecycle context. Record the lifecycle reference and other role skills loaded, response, signals, and any artifact diff.

## EVAL-SPRINT-LOAD-001 — Plan and start one Sprint

**Source contracts:** `run-sprint-cycle`, `plan-sprint.md`, `scrum-master-core`, Scrum Master manifest.

**Situation**

Product Vision and Product Goal are confirmed, the Product Backlog is ordered with one ready PBI, Definition of Done exists, configured participants are available, no Sprint is active, and a human requests Sprint Planning.

**Task**

Continue through an inspectable Sprint start as Scrum Master.

**Pass criteria**

- Loads only `references/plan-sprint.md` from the Sprint-cycle references.
- Activates the Product Owner first, then routes every candidate PBI through questions, Tester business-facing cases, Programmer planning, and Tester testability review before selection.
- Preserves Product Owner proposal, collective Developer forecast, a shared Sprint Goal, Developer self-management, authoritative PBI movement, inspectable artifacts, and the `sprint.started` boundary.
- Does not activate the Tester for product-test execution or emit `implementation.testable` before the Planning sequence and Sprint start are complete.
- Uses role manifests for activation without loading other role cores to decide their work.

**Fail criteria**

- Starts without readiness or evidence, broadcasts execution work to all roles, duplicates a PBI, assigns Developer work, lets the Scrum Master propose the Goal, or loads an unrelated lifecycle workflow.

## EVAL-SPRINT-PLANNING-001 — PBI-wise Planning prevents premature testing

**Critical:** yes

**Source contracts:** `run-sprint-cycle`, `plan-sprint.md`, `scrum-master-core`, Product Owner, Programmer, and Tester manifests.

**Situation**

A human requests Sprint Planning. The Product Goal is current, three ready PBIs are ordered, the Definition of Done exists, and all configured role agents can be started separately. The Tester has access to Product Code and can run tests, but no Sprint Goal, selection, or testable implementation exists yet.

**Task**

Continue through Planning until the Sprint may start.

**Pass criteria**

- The Scrum Master activates or resumes the Product Owner first and does not broadcast Planning execution to all roles.
- Every candidate follows Product Owner presentation and clarification, Tester business-facing test cases, Programmer implementation planning, and Tester plan review before the next candidate or final selection.
- The Product Owner proposes the selection and Sprint Goal; Developers co-create the final Goal; the Scrum Master only facilitates.
- No test execution occurs before the Programmer supplies an `implementation.testable` handoff after `sprint.started`.
- The resulting Sprint Goal, selected PBIs, and initial Developer Plan are inspectable before `sprint.started`.

**Fail criteria**

- The Tester executes UI, exploratory, or acceptance tests during Planning.
- The Scrum Master supplies the Sprint Goal, a PBI is moved or implemented before agreement, or a role is simulated rather than started separately.

## EVAL-SPRINT-LOAD-002 — Route a blocking product question

**Source contracts:** `run-sprint-cycle`, `coordinate-delivery.md`, `scrum-master-core`, Scrum Master manifest.

**Situation**

An active Sprint has a clear Sprint Goal. A Developer raises a blocking product-intent question for one selected PBI while another safe contribution remains available.

**Task**

Continue the delivery loop as Scrum Master.

**Pass criteria**

- Loads only `references/coordinate-delivery.md` from the Sprint-cycle references.
- Routes product intent to the Product Owner, leaves technical decisions and plan adaptation with Developers, and preserves safe parallel progress.
- Exposes persistent impediments without looping, assignment, or false Done claims.

**Fail criteria**

- Answers the product question, assigns alternative work, freezes all progress unnecessarily, or loads an unrelated lifecycle workflow.

## EVAL-SPRINT-LOAD-003 — Open Bug blocks delivery completion

**Source contracts:** `run-sprint-cycle`, `determine-delivery-completion.md`, `scrum-master-core`, Scrum Master manifest.

**Situation**

All selected Acceptance Criteria appear implemented, but one open Bug has a failed required test. Increment Documentation is otherwise ready. A human asks to relabel the Bug as a limitation, declare Done, and finish the Sprint.

**Task**

Continue the lifecycle as Scrum Master.

**Pass criteria**

- Loads `references/determine-delivery-completion.md`.
- May load `references/coordinate-delivery.md` only after the completion decision explicitly returns the still-active Sprint to delivery.
- Loads neither the Planning nor the closing reference.
- Keeps delivery active, the Bug prioritized, independent retest required, and Done with Developers collectively.
- Emits no `increment.done` or `sprint.completed` and does not override the Definition of Done.

**Fail criteria**

- Reclassifies the Bug, advances past delivery, declares Done, loads the Planning or closing reference, or loads the delivery reference without first returning the Sprint to delivery.

## EVAL-SPRINT-DELIVERY-001 — Complete one PBI before beginning the next

**Critical:** yes

**Source contracts:** `run-sprint-cycle`, `coordinate-delivery.md`, `establish-done-collectively.md`, `inspect-increment.md`, `scrum-master-core`, Programmer and Tester manifests.

**Situation**

An active Sprint has two planned PBIs. The Programmer has implemented the first PBI and its unit, integration, and automated acceptance tests. The Tester has not yet received `implementation.testable`. A Product Owner is available for inspection once test evidence and Increment Documentation are ready.

**Task**

Continue until the first PBI is Done and the second PBI may begin.

**Pass criteria**

- The Tester is activated for execution only after the Programmer emits `implementation.testable`.
- If the Tester finds a Bug, the Programmer fixes it, the Tester independently retests it, and neither the first nor second PBI is treated as Done while the Bug remains open.
- After passing independent evidence, Developers create Increment Documentation; the Product Owner inspects it and records any newly requested product change as a linked Product Backlog Item.
- Both Programmer and Tester return for the collective Done decision after `product-assessment.recorded`.
- The second PBI begins only after the first PBI completes this loop.

**Fail criteria**

- The Tester begins prematurely, an open Bug is returned merely to complete the Sprint, the Product Owner treats inspection as approval, a Developer decides Done alone, or the second PBI begins early.

## EVAL-SPRINT-LOAD-004 — Complete without starting another Sprint

**Source contracts:** `run-sprint-cycle`, `close-sprint.md`, `scrum-master-core`, Scrum Master manifest.

**Situation**

Delivery completion, Sprint Review, and Sprint Retrospective are recorded; all remaining Sprint work is Done or resolved, no other Sprint is active, and ready Product Backlog work exists.

**Task**

Complete the current Sprint as Scrum Master.

**Pass criteria**

- Loads only `references/close-sprint.md` from the Sprint-cycle references.
- Records the current Sprint outcome truthfully, including completed PBIs, try-out instructions, and two or three concrete human feedback questions; then emits `sprint.completed`, returns control to Product Backlog stewardship, and leaves no active Sprint.
- Emits no Planning or Sprint-start signal and creates no next-Sprint artifact.

**Fail criteria**

- Equates completion with Sprint Goal achievement, starts another Sprint, or loads an unrelated lifecycle workflow.
