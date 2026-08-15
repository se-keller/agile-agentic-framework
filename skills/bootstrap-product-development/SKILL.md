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
6. Show the generated `README.md` as the human entry point and use the generated `AGENTS.md` as the agent entry point.
7. Validate the generated `artefacts/` bundle with the shared `$okf` skill.
8. Start or hand off to the Product Owner. Let it inspect existing artifacts and Product Code before it continues discovery with open questions.

## Preserve boundaries

- Keep the base framework unchanged for product-specific needs.
- Put product-specific agents and skills under `.aafe/agents/` and `.aafe/skills/`.
- Declare additions and overrides explicitly in `.aafe/aafe.yaml`.
- Treat an undeclared same-name collision as an error, not an implicit override.
- Keep Product Code under `product-code/`, outside the OKF `artefacts/` bundle.
- Store Increment Documentation under `artefacts/increment-documentation/`; never place Product Code there.
- Keep stable PBI identifiers even when their filename slug changes. Freeze a PBI filename when it enters a Sprint Backlog.
- Create Sprint directories only after Sprint Planning has established a Sprint Goal. Freeze their directory names when the Sprint begins.
