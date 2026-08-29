# Close a Sprint

Read this workflow for Sprint Review, Sprint Retrospective, cancellation, or Sprint completion.

## Run Sprint Review

1. Activate the Product Owner, Developers, human, and configured stakeholder agents. Activate or resume the Scrum Master when the Review needs facilitation; do not use it as the lifecycle controller.
2. Let Developers demonstrate usable Increments using the Increment Documentation and explain how the human can try the changes.
3. State the Sprint Goal, whether it was achieved, and which PBIs were completed. Inspect outcomes, Product Goal progress, environment changes, feedback, and next opportunities together.
4. Ask the human two or three concrete feedback questions relevant to the delivered outcome. Let the Product Owner create and reorder follow-up PBIs from the answers. Stakeholders provide feedback but do not make product decisions.
5. Have a participating accountable role record material review results, completed PBIs, try-out instructions, and the feedback questions and answers in `sprint-review.md` within the Sprint directory.
6. Never use the Sprint Review as a Done, release, or acceptance gate.

## Run Sprint Retrospective

1. Activate the Scrum Team after the Sprint Review and resume the same Scrum Master agent to facilitate improvement.
2. Let every participating agent state briefly what worked well and propose changes to quality, flow, tools, interactions, role boundaries, agent behavior, skills, rules, templates, formats, or process.
3. Ask the human whether a different outcome or process change is wanted, then select a small number of concrete improvements with a clear expected effect.
4. Store the result under `artefacts/retrospectives/` and link it to the Sprint.
5. Apply product-specific framework improvements only through a human-reviewed Pull Request against `.aafe/`.
6. Put Product Code or product-scope improvements in the appropriate backlog rather than `.aafe/`.

## Complete the Sprint

1. Have a permitted participating role update the Sprint index with completion or cancellation state and links to Sprint Goal, Developer Plan, Sprint Backlog, Increment Documentation, Sprint Review, and Retrospective.
2. Verify that every work artifact remaining in the Sprint Backlog is Done or resolved and every unfinished artifact has returned to the Product Backlog with an inspectable rationale.
3. Record whether the Sprint Goal was achieved. A completed Sprint may reveal that more Product Backlog work is needed; never rewrite that outcome as success.
4. As the host, signal `sprint.completed` only after Review and Retrospective records exist.
5. Return control to Product Backlog stewardship before planning another Sprint.
