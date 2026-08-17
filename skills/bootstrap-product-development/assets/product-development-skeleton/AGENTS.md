# Product workspace instructions

This is the single entry point for agents working in this workspace. It is self-contained; do not read `README.md`, which addresses humans and repeats this content.

Use the configured Agile Agentic Framework as the base and apply only additions and explicit overrides declared in `.aafe/aafe.yaml`.

## Entry point

Start with the Product Owner unless the human explicitly selects another available agent. The Product Owner must inspect existing `artefacts/` and relevant `product-code/` context before asking questions. Resume established product direction instead of restarting discovery.

When product direction and at least one ready PBI exist, hand lifecycle control to the Scrum Master. Let it activate configured participants and run the event-driven Sprint without assigning Developer work.

Product-specific stakeholder agents reuse `stakeholder-core` and give all product input through the Product Owner.

## Boundaries

- Use the framework's `okf` skill for product knowledge and result artifacts under `artefacts/`. Its profile is sufficient for every artifact this workspace produces; consult the OKF specification only for a case the profile does not cover.
- Preserve each artifact's `created` date and update its `updated` date in `YYYY-MM-DD` format whenever its content or metadata changes.
- Keep Product Code under `product-code/`; never place it under `artefacts/` or `artefacts/increment-documentation/`.
- Allow only agents with Product Code write permission to modify `product-code/`.
- Put product-specific framework changes under `.aafe/`; do not modify the base framework.
- Treat same-name agent or skill collisions as errors unless `.aafe/aafe.yaml` explicitly declares an override.
- Keep `.aafe` skill folders minimal: `SKILL.md` plus only resources the skill actually uses. Do not create `agents/` or `agents/openai.yaml` unless a concrete runtime integration explicitly requires that metadata.

## Work artifact locations

- Keep Product Vision and the current Product Goal under `artefacts/product-backlog/` with its index and available PBI items.
- During Planning, move selected PBI files from `artefacts/product-backlog/items/` into the Sprint's `sprint-backlog/`. Preserve the stable ID and frozen filename; never leave a duplicate behind.
- Store the agreed Sprint Goal inside the Sprint Backlog as `sprint-backlog/sprint-goal.md`.
- Keep Done PBIs and resolved Bugs in the completed Sprint Backlog as the Sprint record. Return unfinished work to `artefacts/product-backlog/items/` for Product Owner ordering and preserve a return link in the Sprint Backlog index.
