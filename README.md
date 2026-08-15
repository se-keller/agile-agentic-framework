# Agile Agentic Framework

This repository defines runtime-neutral agent roles and a shared skill catalog for an agentic Scrum system.

## Structure

- `agents/`: one runtime-neutral manifest per agent.
- `skills/`: all skills, including mandatory agent core skills and cross-role capabilities.

The Product Owner is defined by `agents/product-owner/agent.yaml`. Programmer and Tester agents combine the shared Scrum Developer contract in `skills/developer-core/` with their specialization in `skills/programmer-core/` or `skills/tester-core/`. The Scrum Master combines `skills/scrum-master-core/` with `skills/run-sprint-cycle/` to orchestrate the configured agents without assigning their work. Product-specific stakeholder agents can reuse `skills/stakeholder-core/` while remaining outside the Scrum Team. All agents can discover shared capabilities such as `skills/okf/`.

## Start a product workspace

Use the bootstrap skill to create a separate, Git-ready workspace for one product:

```bash
python3 skills/bootstrap-product-development/scripts/bootstrap.py "My Product" --parent ../
```

This creates `product-development-my-product/` with a human and agent entry point, a `product-code/` area, initial OKF artifacts, a Product Backlog, Sprint and Increment Documentation areas, and a `.aafe/` extension layer. Keep product knowledge and product-specific framework changes there; do not modify this base framework for one product's needs.

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
