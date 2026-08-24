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
- Preserves readiness, collective forecast, shared Sprint Goal, Developer self-management, authoritative PBI movement, inspectable artifacts, and the `sprint.started` boundary.
- Uses role manifests for activation without loading other role cores to decide their work.

**Fail criteria**

- Starts without readiness or evidence, duplicates a PBI, assigns Developer work, or loads an unrelated lifecycle workflow.

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

## EVAL-SPRINT-LOAD-004 — Complete without starting another Sprint

**Source contracts:** `run-sprint-cycle`, `close-sprint.md`, `scrum-master-core`, Scrum Master manifest.

**Situation**

Delivery completion, Sprint Review, and Sprint Retrospective are recorded; all remaining Sprint work is Done or resolved, no other Sprint is active, and ready Product Backlog work exists.

**Task**

Complete the current Sprint as Scrum Master.

**Pass criteria**

- Loads only `references/close-sprint.md` from the Sprint-cycle references.
- Records the current Sprint outcome truthfully, emits `sprint.completed`, returns control to Product Backlog stewardship, and leaves no active Sprint.
- Emits no Planning or Sprint-start signal and creates no next-Sprint artifact.

**Fail criteria**

- Equates completion with Sprint Goal achievement, starts another Sprint, or loads an unrelated lifecycle workflow.
