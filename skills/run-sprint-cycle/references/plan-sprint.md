# Plan a Sprint

Read this workflow for readiness checking, `sprint.planning-requested`, or `sprint.planning-started`.

## Check readiness

Start Sprint Planning only when all conditions are visible:

- a human-confirmed Product Vision and current Product Goal exist;
- the Product Backlog is ordered by the Product Owner;
- at least one PBI satisfies the Definition of Ready;
- the Definition of Done exists;
- a Product Owner and at least one configured Developer are available as separate runtime agents with preserved identifiers; and
- no other Sprint is active.

If a condition is missing, activate the accountable agent to address it. Do not manufacture product direction or technical capacity as Scrum Master.

## Run Sprint Planning

1. Request the Product Owner and all configured Developers as separate agents through the runtime host with `sprint.planning-started`. Preserve their runtime identifiers and reuse an already active matching agent instead of replacing it.
2. Let the Product Owner explain why the next work is valuable and present the highest-ordered ready PBIs.
3. Let Developers forecast at least one PBI and as many additional PBIs as they collectively judge feasible.
4. Collaborate as the Scrum Team, with the human where available, to establish one Sprint Goal.
5. Let Developers create the technical plan and testing approach.
6. Create `sprint-NNNN-short-goal-slug/` only after the Sprint Goal is established. Freeze the directory name when the Sprint starts.
7. Store `developer-plan.md` in the Sprint directory. Store the Sprint Goal at `sprint-backlog/sprint-goal.md` beside `sprint-backlog/index.md` and the selected work artifacts. Use OKF frontmatter for concept artifacts and maintain `created` and `updated` dates.
8. Move each selected PBI artifact from `product-backlog/items/` into the Sprint's `sprint-backlog/`. Preserve its stable ID and frozen filename, update affected links and workflow fields, and never duplicate the authoritative artifact.
9. Remove selected PBIs from the available Product Backlog order and link them from the Sprint Backlog index.
10. Signal `sprint.started` when the Sprint Goal, selection, moved PBIs, and initial Developer Plan are inspectable.
