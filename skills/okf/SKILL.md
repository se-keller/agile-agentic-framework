---
name: okf
description: Create, update, inspect, and validate human- and agent-readable Markdown knowledge bundles using Open Knowledge Format v0.2. Use whenever an agent writes or changes product knowledge or result artifacts such as Product Vision, Product Goal, Product Backlog Items, Sprint Goal, product decisions, or Increment Documentation.
---

# Open Knowledge Format

Use OKF for product knowledge and result artifacts. Do not apply it to framework control files such as `AGENTS.md`, `SKILL.md`, or `agent.yaml`.

The profile below is sufficient for every artifact this framework produces. Work from it directly. Read [the bundled OKF v0.2 specification](references/SPEC.md) only when this profile does not cover the case: an `Attested Computation` concept, `sources` and per-claim attribution, `stale_after`, exchanging a bundle with an external producer, or an unfamiliar key found in an existing document.

## Profile for Scrum artifacts

### Frontmatter

Every concept document carries frontmatter delimited by `---`. `type` is the only key OKF requires; the rest of this profile is what this framework expects.

| Key | Use |
|---|---|
| `type` | Required, non-empty. See the vocabulary below. |
| `title` | Recommended human-readable name. |
| `description` | Recommended one-line summary. Index entries reuse it. |
| `status` | `draft`, `stable`, or `deprecated`. Absent means `stable`. OKF lifecycle only. |
| `created` | `YYYY-MM-DD`. Set once, never change. |
| `updated` | `YYYY-MM-DD`. Set to the current date on every content or metadata change. |
| `generated` | `{ by: <actor>, at: <ISO-8601> }`. How the current content was produced. |
| `verified` | A list of `{ by: <actor>, at: <ISO-8601> }`. Who confirmed the content. |
| `tags` | Optional list of short strings. |

`created` and `updated` go together: supplying one without the other is a validation error. Preserve unknown keys you find in an existing document rather than dropping them.

Actors follow one of three forms: `human:<id>` for a person, `process:<id>` for an automated process, and `<producer>/<version>` for an agent or tool. Trust classification keys off the `human:` prefix, so use it for anything a human authored or confirmed.

Record `verified` by a `human:` actor only after the human confirms the current content. Remove that entry after a meaningful content change and ask for confirmation again.

### Type vocabulary

`Product Vision`, `Product Goal`, `Product Backlog Item`, `Bug`, `Sprint Goal`, `Developer Plan`, `Increment Documentation`, `Sprint Review`, `Retrospective`, `Definition of Ready`, `Definition of Done`, `Decision`.

Values are not registered centrally. Add a descriptive type when an artifact genuinely does not fit, and tolerate unknown types in documents you read.

### Keep lifecycle state separate from workflow state

`status` describes the document; a domain workflow field describes the work. They answer different questions and must not be merged:

```yaml
status: stable          # the document is ready to be consumed
backlog_state: selected # the PBI is in a Sprint Backlog
```

A Bug uses `bug_state: open` or `bug_state: resolved`. Never express a bug's workflow state through `status`.

### Files and links

`index.md` and `log.md` are reserved at every level and are not concept documents. `index.md` carries no frontmatter, with one exception: the bundle-root `index.md` may declare `okf_version: "0.2"`. Every other `.md` file needs frontmatter with a `type`.

Link between concepts with ordinary Markdown links. Prefer the bundle-relative form beginning with `/`, which survives moving a document within its subdirectory. A link to a document that does not exist yet is tolerated, not an error.

Keep bodies concise and structured — headings, lists, tables, fenced code — so both a human and an agent can consume them without tooling.

### Template

```markdown
---
type: Product Backlog Item
title: Reset a forgotten password
description: A returning user regains access without contacting support.
status: draft
backlog_state: available
created: "2026-08-17"
updated: "2026-08-17"
generated: { by: product-owner/aaf, at: "2026-08-17T09:00:00Z" }
---

# Problem

...

# Acceptance Criteria

- ...
```

A work artifact's stable ID lives in its filename (`pbi-0001-short-slug.md`, `bug-0001-short-slug.md`). Freeze the filename once the artifact is created, and never reuse an ID.

## Validate

Install the validator dependency once:

```bash
python -m pip install -r scripts/requirements.txt
```

Run it once per commit, not once per edited artifact:

```bash
python scripts/validate_okf.py <bundle-root>
```

Treat successful validation as structural evidence only. It does not prove that the knowledge is strategically correct or sufficiently complete for a Sprint.
