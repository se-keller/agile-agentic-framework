# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The Agile Agentic Framework (AAF) is a runtime-neutral definition of a Scrum-oriented multi-agent system. It contains no application code — only agent manifests (YAML), skills (Markdown contracts), and two Python support scripts. There is no build, no test suite, and no package manifest.

Behavior is specified in prose, not implemented in code. A change to a `SKILL.md` is a behavioral change; review it with the same care as code.

## Commands

Bootstrap a product workspace (creates `product-development-<slug>/` next to this repo):

```bash
python3 skills/bootstrap-product-development/scripts/bootstrap.py "My Product" --parent ../
# --no-git suppresses `git init`; the script also skips it when --parent is already inside a worktree
```

Validate an OKF knowledge bundle (the only dependency in the repo is PyYAML):

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r skills/okf/scripts/requirements.txt
.venv/bin/python skills/okf/scripts/validate_okf.py path/to/artefacts
```

The validator exits 1 on errors, 0 on warnings only. Broken local links are warnings; missing/invalid `type`, malformed frontmatter, and inconsistent `created`/`updated` dates are errors.

## Architecture

### Three layers, strictly separated

1. **Base framework** (this repository) — runtime-neutral, reusable agents and skills. Read-only during ordinary product use; writable only when deliberately developing or testing the framework.
2. **`.aafe/` extension layer** (inside a product workspace) — product-specific agents, skills, rules, and overrides. Every addition or override must be declared in `.aafe/aafe.yaml`; an undeclared same-name collision is an error, never an implicit override.
3. **Product workspace** — Product Code under `product-code/`, product knowledge under `artefacts/`.

Classify every change into one of these layers before editing. This is the most common source of mistakes in this repository.

### Agents

`agents/<name>/agent.yaml` (`api_version: aaf.dev/v1alpha1`, `kind: Agent`) declares an agent through four things: `core_skills` (relative paths to mandatory skill folders), `skill_catalogs`, a `permissions` tree, and event `subscriptions` plus a `task_priority` ordering.

The permissions tree is the authority on capability. A skill never expands permissions — when a skill and a manifest disagree, the manifest wins, and the most restrictive applicable rule applies. Key asymmetries:

- `product-owner`: reads and executes Product Code, never writes it.
- `tester`: writes `test_code`, never `product_code`.
- `programmer`: writes both.
- `scrum-master`: no Product Code access at all, and `assign_developer_work: false`.

Agents coordinate by event names (`sprint.started`, `developer.question`, `test.finding`, `increment.done`, …) matched between one agent's `subscriptions` and the signals other agents emit in their skills. There is no dispatcher in this repository; the runtime supplies it.

### Skills

- `skills/agent-core-skills/<name>/` — mandatory role contracts, referenced from `core_skills`.
- `skills/<name>/` — process, cross-role, and optional skills (`okf`, `run-sprint-cycle`, `bootstrap-product-development`).

Do not organize the catalog by role; more than one role may use a skill. Each skill folder is `SKILL.md` plus only the resources it actually uses. Do not add `agents/` or `agents/openai.yaml` inside a skill unless a concrete runtime integration requires it.

Skill composition is explicit: Programmer and Tester each combine `developer-core` (the shared Scrum Developer contract) with their specialization; the Scrum Master combines `scrum-master-core` with the `run-sprint-cycle` process skill. `SKILL.md` files reference each other as `$skill-name`.

Every `SKILL.md` needs YAML frontmatter with `name` and a `description` written so an agent can decide from the description alone whether the skill applies.

### OKF

Product knowledge and result artifacts are Open Knowledge Format v0.2 bundles — Markdown with YAML frontmatter, `type` the only required key, `index.md` and `log.md` reserved.

`skills/okf/SKILL.md` carries a self-contained profile covering every artifact this framework produces. Work from that profile. The full spec at `skills/okf/references/SPEC.md` is roughly 9,000 tokens and is reserved for cases the profile does not cover (Attested Computations, `sources`, `stale_after`, external bundle exchange) — do not load it routinely.

Two OKF conventions this framework adds on top of the spec: every product artifact carries `created` and `updated` (`YYYY-MM-DD`, `created` preserved, `updated` bumped on every change), and OKF lifecycle state stays separate from domain workflow state (`status: stable` and `backlog_state: selected` answer different questions; a bug's state is `bug_state`, never `status`).

Framework control files (`AGENTS.md`, `SKILL.md`, `agent.yaml`) are **not** OKF and must not be given OKF frontmatter.

### Workspace skeleton

`skills/bootstrap-product-development/assets/product-development-skeleton/` is the template the bootstrap script copies. Files there use `{{PRODUCT_NAME}}`, `{{PRODUCT_SLUG}}`, `{{GENERATED_AT}}`, `{{GENERATED_DATE}}` tokens — an unknown `{{TOKEN}}` makes the script fail, so add new tokens to the substitution map in `bootstrap.py` when introducing one.

## Conventions that are easy to get wrong

- **PBIs move, they are never copied.** A selected PBI's authoritative file moves from `artefacts/product-backlog/items/` into the Sprint's `sprint-backlog/` at Planning, keeping its stable ID and frozen filename. At Sprint completion, Done PBIs and resolved Bugs stay in the Sprint Backlog as the historical record; unfinished work moves back to `product-backlog/items/`. File location is the inspectable state.
- **IDs are never reused**, and historical evidence is never rewritten — add corrections or linked follow-ups instead.
- **Sprints end on completion conditions, not a timebox.** This is a documented, deliberate deviation from the 2020 Scrum Guide; keep it flagged as an adaptation wherever it appears.
- **Done is a collective Developer decision.** The Product Owner's Increment assessment is input, never approval; the Scrum Master only verifies that evidence exists. Sprint Review is not an acceptance or release gate.
- **Zero Bug Policy**: an open bug outranks all non-bug Sprint Backlog work and blocks Done. It may not be reclassified as a limitation.
- Add infrastructure only when a concrete need exists. The repository is deliberately small.
