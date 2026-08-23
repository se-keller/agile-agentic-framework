---
name: okf
description: Create, update, inspect, and validate human- and agent-readable Markdown knowledge bundles using Open Knowledge Format v0.2. Use whenever an agent writes or changes product knowledge or result artifacts such as Product Vision, Product Goal, Product Backlog Items, Sprint Goal, product decisions, or Increment Documentation.
---

# Open Knowledge Format

Use OKF for product knowledge and result artifacts. Do not apply it to framework control files such as `AGENTS.md`, `SKILL.md`, or `agent.yaml`.

This profile is complete and authoritative for every product and result artifact the base framework produces. Do not load reference files to create, update, inspect, or validate those artifacts. The profile fully covers concept frontmatter, `generated`, `verified`, lifecycle and workflow state, framework dates, actors, reserved files, indexes, logs, links, and unknown keys. Preserve unknown keys without interpreting them.

## Create and update concepts

- Write each concept as a UTF-8 Markdown file with YAML frontmatter delimited by `---` and a structured, human-readable body.
- Require a non-empty `type`. Prefer a clear `title` and one-sentence `description`. Tolerate unknown types and preserve unknown frontmatter keys when updating a document.
- Use the framework's existing descriptive types, including `Product Vision`, `Product Goal`, `Product Backlog Item`, `Bug`, `Sprint Goal`, `Developer Plan`, `Increment Documentation`, `Sprint Review`, `Retrospective`, `Definition of Ready`, `Definition of Done`, and `Decision`. Add another descriptive type only when the artifact genuinely does not fit.
- Give every framework product artifact `created` and `updated` together in `YYYY-MM-DD` format. Set `created` once. Set `updated` to the current date on every content or metadata change.
- Record how the current content was produced as `generated: { by: <actor>, at: <ISO-8601> }` when provenance is available. Update it after a meaningful content change.
- Keep the body concise and prefer headings, lists, tables, and fenced code over unstructured prose.

## Apply trust and lifecycle fields

- Identify actors as `<producer>/<version>` for an agent or tool, `human:<id>` for a person, and `process:<id>` for automation. Use the `human:` prefix for human-authored or human-confirmed content.
- Record verification as one mapping or a list of `{ by: <actor>, at: <ISO-8601> }` entries. Add human verification only after the human confirms the current content. Remove verification made stale by a meaningful change; verification may also be refreshed without regenerating content.
- Use OKF `status` only for document lifecycle: `draft`, `stable`, or `deprecated`; absence means `stable`.
- Keep domain workflow state in a separate field. For example, use `backlog_state` for a PBI and `bug_state: open` or `bug_state: resolved` for a Bug. Never encode those states through OKF `status`.

## Organize and link the bundle

- Treat every `.md` file except `index.md` and `log.md` as a concept requiring frontmatter and `type`.
- Keep reserved `index.md` and `log.md` files free of concept frontmatter. Only the bundle-root `index.md` may declare `okf_version: "0.2"` in frontmatter.
- Use `index.md` for concise directory listings and progressive disclosure. When present, keep its links, order, and descriptions consistent with the current concepts.
- Use `log.md`, when present, as newest-first prose grouped under `YYYY-MM-DD` headings.
- Express relationships with ordinary Markdown links. Use bundle-relative links beginning with `/` when they remain correct across expected file moves; relative links are also valid. Preserve link context in prose.
- Do not treat a missing link target as malformed OKF, but keep framework links current when artifacts move.

## Use advanced OKF features only on explicit request

Only when the task explicitly requires `sources` or per-claim attribution, `stale_after`, an `Attested Computation`, or external bundle exchange or migration, consult the relevant sections of [the bundled OKF v0.2 specification](references/SPEC.md). Never load the full specification by default.

## Validate

Install the validator dependency once:

```bash
python -m pip install -r scripts/requirements.txt
```

Run:

```bash
python scripts/validate_okf.py <bundle-root>
```

Validate the affected bundle before committing. Treat success as structural evidence only; it does not prove that the knowledge is strategically correct, complete, or ready for a Sprint.
