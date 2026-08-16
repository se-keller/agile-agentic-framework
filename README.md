# Agile Agentic Framework

This repository defines runtime-neutral agent roles and a shared skill catalog for an agentic Scrum system.

## Structure

- `agents/`: one runtime-neutral manifest per agent.
- `skills/agent-core-skills/`: mandatory role contracts and role specializations.
- `skills/`: process, cross-role, and other optional skills such as bootstrap, Sprint cycle, and OKF.

A skill needs only `skills/<skill-name>/SKILL.md`. Add scripts, references, or assets only when they are used. Runtime-specific UI metadata such as `agents/openai.yaml` is intentionally omitted unless a concrete integration requires it.

The Product Owner is defined by `agents/product-owner/agent.yaml`. Programmer and Tester agents combine the shared Scrum Developer contract in `skills/agent-core-skills/developer-core/` with their specialization in `skills/agent-core-skills/programmer-core/` or `skills/agent-core-skills/tester-core/`. The Scrum Master combines `skills/agent-core-skills/scrum-master-core/` with `skills/run-sprint-cycle/` to orchestrate the configured agents without assigning their work. Product-specific stakeholder agents can reuse `skills/agent-core-skills/stakeholder-core/` while remaining outside the Scrum Team. All agents can discover shared capabilities such as `skills/okf/`.

## Start a product workspace

Use the bootstrap skill to create a separate, Git-ready workspace for one product:

```bash
python3 skills/bootstrap-product-development/scripts/bootstrap.py "My Product" --parent ../
```

This creates `product-development-my-product/` with a human and agent entry point, a `product-code/` area, initial OKF artifacts, a Product Backlog, Sprint and Increment Documentation areas, and a `.aafe/` extension layer. Keep product knowledge and product-specific framework changes there; do not modify this base framework for one product's needs.

Product Vision and the current Product Goal live under `artefacts/product-backlog/` with its index. PBI files begin under `artefacts/product-backlog/items/`. Sprint Planning stores the Sprint Goal at `sprint-backlog/sprint-goal.md` and moves selected PBI files beside it. Done PBIs and resolved Bugs remain there as the completed Sprint record; unfinished work is moved back to the Product Backlog for Product Owner ordering.

## Test and improve the framework

Framework development and product development may alternate during a trial, but changes remain separated:

- Reusable framework defects and improvements belong in this repository.
- Product-specific framework extensions and overrides belong under the product repository's `.aafe/` directory.
- Product knowledge and Product Code belong only in the product repository.

Validate and version each repository independently so a product experiment cannot silently change the base framework.

## Validation

Install the validator's single dependency and validate an OKF knowledge bundle:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r skills/okf/scripts/requirements.txt
.venv/bin/python skills/okf/scripts/validate_okf.py path/to/bundle
```

Read [AGENTS.md](AGENTS.md) for repository-level instructions used by AI agents.

## License

This project is licensed under the [BSD 2-Clause License](LICENSE). You may use,
modify, and distribute it, including for commercial purposes, provided that the
copyright notice and license terms are retained as required by the license.
