---
name: run-sprint-cycle
description: Run one inspectable, event-driven Sprint through Sprint Planning, iterative development and testing, Sprint Review, Sprint Retrospective, and completion. Use when a Product Goal and ready Product Backlog exist, when coordinating configured Product Owner, Developer, and stakeholder agents, when resuming an active Sprint, or when deciding whether Sprint work is complete. This framework adaptation ends a Sprint by explicit completion conditions rather than a calendar timebox.
---

# Run Sprint Cycle

Apply this process skill with `$scrum-master-core`. Treat the event-driven duration as an explicit framework adaptation: the official Scrum Guide defines fixed-length Sprints, while this workflow initially uses completion events to support autonomous agent execution.

## Keep lifecycle state explicit

Advance only one inspectable state at a time:

1. Start Planning only after an explicit request and visible readiness, with no active Sprint.
2. Start one Sprint only after its Goal, selection, moved PBI files, indexes, and initial Developer Plan are inspectable.
3. Keep the Sprint active while Developers deliver, test, adapt, and resolve impediments.
4. Treat delivery as complete only after the required Done and artifact evidence exists and unfinished work has returned to the Product Backlog.
5. Run Sprint Review, then Sprint Retrospective.
6. Complete or cancel the current Sprint, return control to Product Backlog stewardship, and stop. Never start another Sprint merely because ready work exists.

Inspect indexes, status metadata, lifecycle signals, and directly referenced artifacts before loading full bodies. Use `$okf` only when creating or changing knowledge or result artifacts.

Use the Scrum Master manifest, `$scrum-master-core`, and this process skill. Read another role's manifest to activate it, but do not load that role's core skill to decide or perform its work. Let configured agents apply their own contracts and report their results.

Load only the detailed workflow matching the current event:

- `product-direction.ready`, `sprint.planning-requested`, readiness checking, or `sprint.planning-started`: [plan a Sprint](references/plan-sprint.md).
- `sprint.started`, `sprint-backlog.changed`, `developer.question`, or `sprint.impediment`: [coordinate delivery](references/coordinate-delivery.md).
- `increment.done`, `product-assessment.recorded`, or an explicit delivery-completion decision: [determine delivery completion](references/determine-delivery-completion.md).
- `sprint.review-ready`, Sprint Review, `retrospective.ready`, Sprint Retrospective, cancellation, or Sprint completion: [close a Sprint](references/close-sprint.md).

Do not load multiple references in advance. Load the next one only when a real lifecycle transition occurs.

## Preserve lifecycle boundaries

- Never assign Developer work, order the Product Backlog, choose product value, make technical decisions, or determine Done.
- An open Bug or failed required test blocks delivery completion; never relabel it as a limitation to advance the lifecycle.
- Keep Done or resolved work in the completed Sprint Backlog. Return unfinished work to the Product Backlog with identity, evidence, link, and rationale intact.
- Only the Product Owner may determine that the Sprint Goal is obsolete; facilitate but never initiate cancellation on its behalf.
- Never use Sprint Review as a Done, release, or acceptance gate.
- Never rewrite Sprint completion as Sprint Goal achievement.
- After `sprint.completed`, emit no Planning or Sprint-start signal without a separate request.
