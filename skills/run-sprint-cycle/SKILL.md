---
name: run-sprint-cycle
description: Run one inspectable, event-driven Sprint through Sprint Planning, iterative development and testing, Sprint Review, Sprint Retrospective, and completion. Use when a Product Goal and ready Product Backlog exist, when coordinating configured Product Owner, Developer, and stakeholder agents, when resuming an active Sprint, or when deciding whether Sprint work is complete. This framework adaptation ends a Sprint by explicit completion conditions rather than a calendar timebox.
---

# Run Sprint Cycle

Apply this process skill with `$scrum-master-core`. Treat the event-driven duration as an explicit framework adaptation: the official Scrum Guide defines fixed-length Sprints, while this workflow initially uses completion events to support autonomous agent execution.

## Check readiness

Start Sprint Planning only when all conditions are visible:

- a human-confirmed Product Vision and current Product Goal exist;
- the Product Backlog is ordered by the Product Owner;
- at least one PBI satisfies the Definition of Ready;
- the Definition of Done exists;
- a Product Owner and at least one configured Developer are available; and
- no other Sprint is active.

If a condition is missing, activate the accountable agent to address it. Do not manufacture product direction or technical capacity as Scrum Master.

## Run Sprint Planning

1. Activate the Product Owner and all configured Developers through `sprint.planning-started`.
2. Let the Product Owner explain why the next work is valuable and present the highest-ordered ready PBIs.
3. Let Developers forecast at least one PBI and as many additional PBIs as they collectively judge feasible.
4. Collaborate as the Scrum Team, with the human where available, to establish one Sprint Goal.
5. Let Developers create the technical plan and testing approach.
6. Create `sprint-NNNN-short-goal-slug/` only after the Sprint Goal is established. Freeze the directory name when the Sprint starts.
7. Store `sprint-goal.md`, `developer-plan.md`, and `sprint-backlog/index.md` in that directory. Use OKF frontmatter for concept artifacts and maintain `created` and `updated` dates.
8. Link selected PBIs from the Sprint Backlog without moving or duplicating their authoritative Product Backlog artifacts.
9. Signal `sprint.started` when the Sprint Goal, selection, and initial Developer Plan are inspectable.

## Run the delivery loop

1. Signal `developer.work-available`; let Developers pull and coordinate their own work.
2. Observe Sprint Backlog state, questions, test results, bugs, fixes, retests, Increment Documentation, and Product Owner assessments.
3. Keep completed and removed entries for history. Change their workflow state instead of deleting them.
4. Put every open Sprint bug above non-bug work. Let a Programmer fix it and a Tester independently retest it before normal Sprint work resumes.
5. Route product-intent questions to the Product Owner and keep technical decisions with Developers.
6. Allow explicit Sprint Backlog adaptation. Developers may add technical work; scope changes involving PBIs require collaboration with the Product Owner and must protect the Sprint Goal.
7. If work stalls, expose the impediment and coordinate a decision. Never spin indefinitely or mark blocked work Done.

## Determine delivery completion

Do not literally empty the Sprint Backlog. Delivery is complete only when:

- every active selected PBI meets the Definition of Done;
- every open Sprint bug is resolved and independently retested;
- all required tests pass without known regression;
- Increment Documentation and Product Owner assessments are recorded;
- no active Sprint Backlog work remains; and
- removed or returned work is explicitly recorded with its rationale and remains linked to the Product Backlog.

Developers determine Done collectively. The Scrum Master only verifies that the required state and evidence are present. The Sprint may continue with one or many PBIs, and explicit scope adaptation may change the active set.

If the Product Owner determines that the Sprint Goal has become obsolete, facilitate cancellation and preserve the Sprint record. Do not cancel a Sprint on behalf of the Product Owner.

## Run Sprint Review

1. Activate the Product Owner, Developers, human, and configured stakeholder agents.
2. Let Developers demonstrate usable Increments using the Increment Documentation.
3. Inspect outcomes, Product Goal progress, environment changes, feedback, and next opportunities together.
4. Let the Product Owner create and reorder follow-up PBIs. Stakeholders provide feedback but do not make product decisions.
5. Record material review results in `sprint-review.md` within the Sprint directory.
6. Never use the Sprint Review as a Done, release, or acceptance gate.

## Run Sprint Retrospective

1. Activate the Scrum Team after the Sprint Review.
2. Inspect evidence about quality, flow, tools, interactions, role boundaries, agent behavior, skills, rules, templates, formats, and process.
3. Select a small number of concrete improvements with a clear expected effect.
4. Store the result under `artefacts/retrospectives/` and link it to the Sprint.
5. Apply product-specific framework improvements only through a human-reviewed Pull Request against `.aafe/`.
6. Put Product Code or product-scope improvements in the appropriate backlog rather than `.aafe/`.

## Complete the Sprint

1. Update the Sprint index with completion or cancellation state and links to Sprint Goal, Developer Plan, Sprint Backlog, Increment Documentation, Sprint Review, and Retrospective.
2. Record whether the Sprint Goal was achieved. A completed Sprint may reveal that more Product Backlog work is needed; never rewrite that outcome as success.
3. Signal `sprint.completed` only after Review and Retrospective records exist.
4. Return control to Product Backlog stewardship before planning another Sprint.
