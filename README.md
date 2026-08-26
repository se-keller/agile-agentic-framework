# Agile Agentic Framework

This README is the entry point for people who use or develop the framework. AI agents use `AGENTS.md` as their self-contained repository entry point and load relevant skills as needed; they do not need this README as operating input.

This repository defines runtime-neutral agent roles and a shared skill catalog for an agentic Scrum system.

For an illustrated guide to framework use, architecture, agentic principles, lifecycle, extensions, evaluations, and design rationale, start with the [OKF documentation bundle](docs/index.md). The documentation is for people and is not operating input for agents.

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

Behavioral changes to agent manifests, skills, and agent instructions are checked with the lightweight, runtime-neutral evaluations under [`evals/`](evals/README.md). Evaluation cases stay separate from the productive instructions they test. Change authors provide the relevant evidence, critical behavior is reviewed independently when practical, and the human maintainer remains responsible for the merge decision. Resource savings count as improvements only when the candidate continues to pass the same quality criteria as the unchanged baseline.

## Validation

Install the validator's single dependency and validate an OKF knowledge bundle:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r skills/okf/scripts/requirements.txt
.venv/bin/python skills/okf/scripts/validate_okf.py path/to/bundle
```

AI-agent operating instructions are maintained separately in [AGENTS.md](AGENTS.md). People may inspect that file when reviewing or developing agent behavior, but it is not required for ordinary framework use.

## License

This project is licensed under the [MIT License](LICENSE). You may use,
modify, and distribute it, including for commercial purposes, provided that the
copyright notice and license terms are retained as required by the license.
