# Product workspace instructions

This is the self-contained entry point for AI agents working in this product workspace. Do not read `README.md` for operating instructions; it is the human entry point.

Use the configured Agile Agentic Framework as the base and apply only additions and explicit overrides declared in `.aafe/aafe.yaml`.

## Multi-agent execution

The primary agent is the runtime host, not a Scrum role.

- At the first product interaction of each runtime session, apply `$manage-role-interaction`. Inspect actual runtime capabilities, offer only supported `host`, `transparent-proxy`, and `direct-handoff` modes, and let the human choose unless they already selected one.
- Start each configured role when it is needed with the runtime's real subagent or delegation mechanism.
- Give the new agent this `AGENTS.md`, its manifest, and its declared core skills; do not load those role skills into the host to perform the work.
- Keep the returned agent identifier and route later human replies and lifecycle events back to that same agent.
- Keep at most one user-facing role active at a time. Apply the selected interaction mode without changing role permissions, lifecycle boundaries, or artifact ownership.
- Use a different agent for independent testing than for implementation.
- If a required agent cannot be started or resumed, stop the affected transition and report it. Never simulate the missing role in the host.

The host owns mechanical conversation routing and Sprint lifecycle transitions. Apply `$run-sprint-cycle` when Planning or an active Sprint needs coordination, but never load a role core or make a product, facilitation, implementation, test, or Done decision.

## Entry point

Start a separate Product Owner agent unless the human explicitly selects another available agent. Let it own product dialogue through the selected interaction mode and return later human answers to the same agent. The Product Owner must inspect existing `artefacts/` and relevant `product-code/` context before asking questions. Resume established product direction instead of restarting discovery.

When product direction and at least one ready PBI exist, let the host run the event-driven lifecycle through `$run-sprint-cycle`. Activate configured participants just in time: first the Product Owner, then the Programmer and Tester for each PBI planning handoff, then the Programmer for implementation, the Tester only after a testable handoff, and the Product Owner for Increment inspection. Activate the same Scrum Master agent only when facilitation, an impediment, a Scrum deviation, Sprint Review support, or Retrospective improvement needs its independent judgment. The Scrum Master never owns the lifecycle mechanism or assigns Developer work.

## Boundaries

- Use the framework's `okf` skill for product knowledge and result artifacts under `artefacts/`.
- Preserve each artifact's `created` date and update its `updated` date in `YYYY-MM-DD` format whenever its content or metadata changes.
- Keep Product Code under `product-code/`; never place it under `artefacts/` or `artefacts/increment-documentation/`.
- Allow only agents with Product Code write permission to modify `product-code/`.
- Put product-specific framework changes under `.aafe/`; do not modify the base framework.
- Treat same-name agent or skill collisions as errors unless `.aafe/aafe.yaml` explicitly declares an override.
- Keep `.aafe` skill folders minimal. Do not create `agents/` or `agents/openai.yaml` unless a concrete runtime integration explicitly requires that metadata.
- Make additional roles and skills available only through the base framework or explicit `.aafe` declarations. Product-specific stakeholder agents reuse `stakeholder-core` and provide product input through the Product Owner.
- Keep Product Vision and the current Product Goal under `artefacts/product-backlog/` with its index and available PBI items.
- During Planning, move selected PBI files from `artefacts/product-backlog/items/` into the Sprint's `sprint-backlog/`. Keep Done PBIs and resolved Bugs there; return unfinished work to the Product Backlog and preserve a return link in the Sprint Backlog index.
- Store the agreed Sprint Goal inside the Sprint Backlog as `sprint-backlog/sprint-goal.md`.
