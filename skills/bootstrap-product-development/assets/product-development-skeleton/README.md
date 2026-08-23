# Welcome to {{PRODUCT_NAME}}

This README is the entry point for people using or developing this product. AI agents use `AGENTS.md` as their self-contained workspace entry point and load relevant skills as needed; they do not need this README as operating input.

This workspace contains Product Code, product knowledge, Scrum artifacts, and product-specific extensions for the Agile Agentic Framework.

## Start here

Start with the **Product Owner**. The base framework also provides a **Scrum Master**, **Programmer**, and **Tester**. Tell your agent runtime:

> Start the Product Owner for this product. Inspect the existing artifacts and Product Code first, then continue product discovery with me.

The Product Owner will resume from existing knowledge when possible. If Product Vision, Product Goal, or sufficient Product Backlog Items are missing, it will ask a few open questions at a time. You provide the creative direction; the Product Owner helps clarify users, problems, value, desired outcomes, boundaries, assumptions, and evidence of success.

When the Product Goal and at least one ready PBI exist, continue with:

> Ask the Scrum Master to start the next event-driven Sprint.

The Scrum Master brings the Product Owner and configured Developers into Sprint Planning, observes the delivery loop without assigning technical work, and facilitates Sprint Review and Retrospective.

## Workspace

- `product-code/`: the product's source code and code-level documentation.
- `artefacts/`: OKF product knowledge, Scrum artifacts, and Increment Documentation.
- `.aafe/`: explicit product-specific additions and overrides to the base framework.
- `AGENTS.md`: the separate, self-contained operating entry point for AI agents.

Product Vision and the current Product Goal live in `artefacts/product-backlog/`. PBI files begin in `artefacts/product-backlog/items/`. Planning stores the Sprint Goal at `sprint-backlog/sprint-goal.md` and moves selected PBI files beside it. Done PBIs and resolved Bugs remain there; unfinished work returns to the Product Backlog for reordering.

Additional agent roles and skills become available when they are added to the base framework or explicitly declared under `.aafe/`. Product-specific stakeholder agents should reuse `stakeholder-core` and give all product input through the Product Owner.

A product-specific skill normally contains only `.aafe/skills/<skill-name>/SKILL.md`. Add resource folders only when used; omit `agents/` and `agents/openai.yaml` unless a concrete runtime integration requires them.
