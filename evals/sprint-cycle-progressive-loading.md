# Sprint-cycle progressive-loading evaluations

Run these cases when changing `run-sprint-cycle` or the host's lifecycle ownership. Record the lifecycle reference and role skills loaded, agent activations and preserved identifiers, response, signals, and any artifact diff. The host may inspect role manifests for activation but must not load role cores to decide or perform their work.

## EVAL-SPRINT-LOAD-001 — Plan and start one Sprint

**Source contracts:** `run-sprint-cycle`, `plan-sprint.md`, workspace host contract, configured role manifests.

**Situation**

Product Vision and Product Goal are confirmed, the Product Backlog is ordered with one ready PBI, Definition of Done exists, configured participants are available, no Sprint is active, and a human requests Sprint Planning.

**Task**

Continue through an inspectable Sprint start as the runtime host.

**Pass criteria**

- Loads only `references/plan-sprint.md` from the Sprint-cycle references and loads no role core.
- Resumes the Product Owner and activates the Scrum Master for facilitation, then routes every candidate PBI through questions, Tester business-facing cases, Programmer planning, and Tester testability review before selection.
- Keeps lifecycle checks and transitions with the host, facilitation with the Scrum Master, product proposal with the Product Owner, and forecast, plan, artifact materialization, and authoritative PBI movement with Developers.
- Preserves a shared Sprint Goal, Developer self-management, inspectable artifacts, stable role IDs, and the `sprint.started` boundary.
- Does not activate the Tester for product-test execution or emit `implementation.testable` before the Planning sequence and Sprint start are complete.

**Fail criteria**

- Starts without readiness or evidence, broadcasts execution work, duplicates a PBI, assigns Developer work, lets the host or Scrum Master propose the Goal, lets the Scrum Master run lifecycle transitions, or loads an unrelated lifecycle workflow or role core.

## EVAL-SPRINT-PLANNING-001 — PBI-wise Planning prevents premature testing

**Critical:** yes

**Source contracts:** `run-sprint-cycle`, `plan-sprint.md`, workspace host contract, Scrum Master, Product Owner, Programmer, and Tester manifests.

**Situation**

A human requests Sprint Planning. The Product Goal is current, three ready PBIs are ordered, the Definition of Done exists, and all configured role agents can be started separately. The Tester has access to Product Code and can run tests, but no Sprint Goal, selection, or testable implementation exists yet.

**Task**

Continue as the runtime host through Planning until the Sprint may start.

**Pass criteria**

- The host loads only the Planning reference, resumes the Product Owner, and activates or resumes the same Scrum Master for facilitation without giving it lifecycle control.
- Every candidate follows Product Owner presentation and clarification, Tester business-facing test cases, Programmer implementation planning, and Tester plan review before the next candidate or final selection.
- The Product Owner proposes the selection and Sprint Goal; Developers co-create the final Goal; the Scrum Master facilitates; the host only routes and verifies transition evidence.
- No test execution occurs before the Programmer supplies an `implementation.testable` handoff after `sprint.started`.
- The resulting Sprint Goal, selected PBIs, and initial Developer Plan are materialized by accountable roles and inspectable before the host emits `sprint.started`.

**Fail criteria**

- The Tester executes UI, exploratory, or acceptance tests during Planning.
- The host or Scrum Master supplies the Sprint Goal, the Scrum Master activates roles or emits transitions, a PBI is moved or implemented before agreement, or a role is simulated rather than started separately.

## EVAL-SPRINT-LOAD-002 — Route a blocking product question

**Source contracts:** `run-sprint-cycle`, `coordinate-delivery.md`, workspace host contract, Product Owner and Developer manifests.

**Situation**

An active Sprint has a clear Sprint Goal. A Developer raises a blocking product-intent question for one selected PBI while another safe contribution remains available.

**Task**

Continue the delivery loop as the runtime host.

**Pass criteria**

- Loads only `references/coordinate-delivery.md` from the Sprint-cycle references and loads no role core.
- Routes product intent to the preserved Product Owner agent, leaves technical decisions and plan adaptation with Developers, and preserves safe parallel progress.
- Activates the Scrum Master only if the situation becomes an actual impediment needing facilitation; ordinary message routing does not require it.
- Exposes persistent impediments without looping, assignment, or false Done claims.

**Fail criteria**

- Answers the product question, assigns alternative work, activates Scrum Master for routine transport, freezes all progress unnecessarily, or loads an unrelated lifecycle workflow or role core.

## EVAL-SPRINT-LOAD-003 — Open Bug blocks delivery completion

**Source contracts:** `run-sprint-cycle`, `determine-delivery-completion.md`, workspace host contract, Developer manifests.

**Situation**

All selected Acceptance Criteria appear implemented, but one open Bug has a failed required test. Increment Documentation is otherwise ready. A human asks to relabel the Bug as a limitation, declare Done, and finish the Sprint.

**Task**

Continue the lifecycle as the runtime host.

**Pass criteria**

- Loads `references/determine-delivery-completion.md` and no role core.
- May load `references/coordinate-delivery.md` only after the completion decision explicitly returns the still-active Sprint to delivery.
- Loads neither the Planning nor the closing reference.
- Keeps delivery active, the Bug prioritized, independent retest required, and Done with Developers collectively.
- Emits no `increment.done` or `sprint.completed` and does not treat mechanical evidence inspection as a Done or Scrum Master decision.

**Fail criteria**

- Reclassifies the Bug, advances past delivery, declares Done, loads the Planning or closing reference, loads a role core, or loads the delivery reference without first returning the Sprint to delivery.

## EVAL-SPRINT-DELIVERY-001 — Complete one PBI before beginning the next

**Critical:** yes

**Source contracts:** `run-sprint-cycle`, `coordinate-delivery.md`, `establish-done-collectively.md`, `inspect-increment.md`, workspace host contract, Programmer and Tester manifests.

**Situation**

An active Sprint has two planned PBIs. The Programmer has implemented the first PBI and its unit, integration, and automated acceptance tests. The Tester has not yet received `implementation.testable`. A Product Owner is available for inspection once test evidence and Increment Documentation are ready.

**Task**

Continue as the runtime host until the first PBI is Done and the second PBI may begin.

**Pass criteria**

- Loads only `references/coordinate-delivery.md` from the Sprint-cycle references and loads no role core.
- The Tester is activated for execution only after the Programmer emits `implementation.testable`.
- If the Tester finds a Bug, the Programmer fixes it, the Tester independently retests it, and neither the first nor second PBI is treated as Done while the Bug remains open.
- After passing independent evidence, Developers create Increment Documentation; the Product Owner inspects it and records any newly requested product change as a linked Product Backlog Item.
- Both Programmer and Tester return for the collective Done decision after `product-assessment.recorded`; the host only verifies the resulting transition evidence.
- The second PBI begins only after the first PBI completes this loop.

**Fail criteria**

- The Tester begins prematurely, an open Bug is returned merely to complete the Sprint, the Product Owner treats inspection as approval, the host or one Developer decides Done, the second PBI begins early, or the host loads a role core.

## EVAL-SPRINT-LOAD-004 — Complete without starting another Sprint

**Source contracts:** `run-sprint-cycle`, `close-sprint.md`, workspace host contract, Scrum Master manifest.

**Situation**

Delivery completion, Sprint Review, and Sprint Retrospective are recorded; all remaining Sprint work is Done or resolved, no other Sprint is active, and ready Product Backlog work exists.

**Task**

Complete the current Sprint as the runtime host.

**Pass criteria**

- Loads only `references/close-sprint.md` from the Sprint-cycle references and loads no role core.
- Verifies truthful current-Sprint records, including completed PBIs, try-out instructions, and human feedback; then emits `sprint.completed`, returns control to Product Backlog stewardship, and leaves no active Sprint.
- Resumes the same Scrum Master for Retrospective facilitation when that event has not already completed, but does not give it lifecycle control.
- Emits no Planning or Sprint-start signal and creates no next-Sprint artifact.

**Fail criteria**

- Equates completion with Sprint Goal achievement, starts another Sprint, lets the host create role-owned retrospective or product content, gives lifecycle control to the Scrum Master, or loads an unrelated lifecycle workflow or role core.
