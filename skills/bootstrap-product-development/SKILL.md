---
name: bootstrap-product-development
description: Create a minimal, standalone product-development workspace for the Agile Agentic Framework. Use when starting development of a new product, bootstrapping its initial Scrum-oriented OKF artifacts, preparing its Git repository, or creating its product-specific `.aafe` extension and override layer.
---

# Bootstrap Product Development

Create one workspace per product. Do not create a separate product merely for a technical module; use another workspace only when it has an independently managed product boundary, Product Goal, Product Backlog, and stakeholder context.

## Bootstrap

1. Ask for the product's human-readable name and the parent directory when either is unknown.
2. Preview the resulting directory name: `product-development-<product-slug>`.
3. Run:

   ```bash
   python3 scripts/bootstrap.py "<Product Name>" --parent "<parent-directory>"
   ```

4. Never overwrite an existing target. Resolve the collision with the user.
5. If the parent is not already inside a Git worktree, let the script initialize a Git repository. Use `--no-git` only when the user explicitly does not want this.
6. Show the generated `README.md` as the human entry point and use the generated `AGENTS.md` as the single, self-contained agent entry point. Do not load `README.md` as agent operating input.
7. Validate the generated `artefacts/` bundle with the shared `$okf` skill.
8. Apply `$manage-role-interaction`, inspect the runtime's actual conversation capabilities, and let the human select a supported interaction mode for the session unless they already selected one.
9. Using the runtime's real subagent or delegation mechanism, start a separate Product Owner agent. Give it the workspace `AGENTS.md`, the Product Owner manifest and its declared core skills, and let it inspect existing artifacts and Product Code before continuing discovery with open questions.
10. Preserve the returned Product Owner agent identifier and route the human dialogue according to the selected interaction mode. If a separate agent cannot be started or resumed, stop after bootstrap instead of acting as the Product Owner.

## Preserve boundaries

- Keep generated `README.md` human-facing and `AGENTS.md` agent-facing. Duplicate information when both audiences need it; never make an agent depend on `README.md`.
- Keep the base framework unchanged for product-specific needs.
- Put product-specific agents and skills under `.aafe/agents/` and `.aafe/skills/`.
- Keep each product-specific skill folder minimal: `SKILL.md` plus only required resources. Omit `agents/` and `agents/openai.yaml` unless a concrete runtime integration requires them.
- Declare additions and overrides explicitly in `.aafe/aafe.yaml`.
- Treat an undeclared same-name collision as an error, not an implicit override.
- Keep Product Code under `product-code/`, outside the OKF `artefacts/` bundle.
- Store Increment Documentation under `artefacts/increment-documentation/`; never place Product Code there.
- Store Product Vision at `artefacts/product-backlog/product-vision.md` and the current Product Goal at `artefacts/product-backlog/current-product-goal.md`.
- Keep stable PBI identifiers even when their filename slug changes. Freeze a PBI filename and move the authoritative artifact from `product-backlog/items/` into the selected Sprint's `sprint-backlog/` during Planning.
- Keep Done PBIs and resolved Bugs in the completed Sprint Backlog. Move unfinished work back to `product-backlog/items/` for Product Owner ordering and preserve its return in the Sprint Backlog index.
- Store each agreed Sprint Goal inside its Sprint Backlog as `sprint-backlog/sprint-goal.md`.
- Create Sprint directories only after Sprint Planning has established a Sprint Goal. Freeze their directory names when the Sprint begins.
