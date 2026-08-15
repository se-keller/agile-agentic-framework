---
name: okf
description: Create, update, inspect, and validate human- and agent-readable Markdown knowledge bundles using Open Knowledge Format v0.2. Use whenever an agent writes or changes product knowledge or result artifacts such as Product Vision, Product Goal, Product Backlog Items, Sprint Goal, product decisions, or Increment Documentation.
---

# Open Knowledge Format

Use OKF for product knowledge and result artifacts. Do not apply it to framework control files such as `AGENTS.md`, `SKILL.md`, or `agent.yaml`.

## Work with OKF

1. Read [the bundled OKF v0.2 specification](references/SPEC.md) completely before creating or changing an OKF bundle.
2. Follow its required frontmatter, reserved filename, linking, provenance, trust, lifecycle, and actor conventions.
3. Keep the Markdown body concise, structured, and understandable without special tooling.
4. Preserve unknown types and frontmatter keys when updating existing documents.
5. Give every product artifact that has YAML frontmatter a `created` and `updated` date in `YYYY-MM-DD` format. Preserve `created`; set `updated` to the current date whenever its content or metadata changes.
6. Use ordinary Markdown links for relationships between concepts.
7. Record human verification only after the human confirms the current content. Remove outdated verification after a meaningful content change.
8. Keep OKF lifecycle state separate from domain workflow state. For example, `status: stable` and `backlog_state: selected` answer different questions.
9. Validate the bundle before committing it.

## Validate

Install the validator dependency once:

```bash
python -m pip install -r scripts/requirements.txt
```

Run:

```bash
python scripts/validate_okf.py <bundle-root>
```

Treat successful validation as structural evidence only. It does not prove that the knowledge is strategically correct or sufficiently complete for a Sprint.
