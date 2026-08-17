# Welcome to {{PRODUCT_NAME}}

This workspace contains Product Code, product knowledge, Scrum artifacts, and product-specific extensions for the Agile Agentic Framework.

This file is for you, the human. Agents read `AGENTS.md` instead; you do not need to.

## Start here

Start with the **Product Owner**. The base framework also provides a **Scrum Master**, **Programmer**, and **Tester**. Tell your agent runtime:

> Start the Product Owner for this product. Inspect the existing artifacts and Product Code first, then continue product discovery with me.

The Product Owner resumes from existing knowledge when possible. If Product Vision, Product Goal, or sufficient Product Backlog Items are missing, it asks a few open questions at a time. You provide the creative direction; the Product Owner helps clarify users, problems, value, desired outcomes, boundaries, assumptions, and evidence of success.

When the Product Goal and at least one ready PBI exist, continue with:

> Ask the Scrum Master to start the next event-driven Sprint.

The Scrum Master brings the Product Owner and configured Developers into Sprint Planning, observes the delivery loop without assigning technical work, and facilitates Sprint Review and Retrospective.

## Workspace

- `product-code/`: the product's source code and code-level documentation.
- `artefacts/`: OKF product knowledge, Scrum artifacts, and Increment Documentation.
- `.aafe/`: explicit product-specific additions and overrides to the base framework.
- `AGENTS.md`: operating instructions for agents working in this workspace.

Product Vision and the current Product Goal live in `artefacts/product-backlog/`, alongside the backlog index and available PBI files. Each Sprint gets a directory under `artefacts/sprints/`.

Additional agent roles and skills become available when they are added to the base framework or explicitly declared under `.aafe/`.
