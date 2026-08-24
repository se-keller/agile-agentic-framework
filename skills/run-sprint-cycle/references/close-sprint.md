# Close a Sprint

Read this workflow for Sprint Review, Sprint Retrospective, cancellation, or Sprint completion.

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
2. Verify that every work artifact remaining in the Sprint Backlog is Done or resolved and every unfinished artifact has returned to the Product Backlog with an inspectable rationale.
3. Record whether the Sprint Goal was achieved. A completed Sprint may reveal that more Product Backlog work is needed; never rewrite that outcome as success.
4. Signal `sprint.completed` only after Review and Retrospective records exist.
5. Return control to Product Backlog stewardship before planning another Sprint.
