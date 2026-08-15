# Repository instructions

Read [README.md](README.md) before changing the framework.

This repository defines a small, runtime-neutral Scrum-oriented agent framework. Keep it simple: add infrastructure only when a concrete need exists.

## Structure

- Define each agent manifest at `agents/<agent-name>/agent.yaml`.
- Put every skill below `skills/<skill-name>/`, including mandatory core skills.
- Reference mandatory skills through `core_skills` in the agent manifest.
- Do not organize the skill catalog by agent role; more than one role may use a skill.

## Knowledge artifacts

Use the shared [`okf` skill](skills/okf/SKILL.md) whenever an agent creates or changes product knowledge or result artifacts in Markdown. This includes Product Vision, Product Goal, Product Backlog Items, Sprint Goal, product decisions, and Increment Documentation.

Framework control files such as `AGENTS.md` and `SKILL.md` follow their own contracts and are not part of an OKF knowledge bundle.

## Product Owner boundary

The Product Owner may read and run Product Code for Increment inspection but must never modify Product Code or prescribe technical solutions.

## Product-specific extensions

Treat the base framework as read-only when using it for a product. Put additions and deliberate overrides in the product workspace's `.aafe/` directory and declare them explicitly in `.aafe/aafe.yaml`. Never infer an override from a same-name file.

## Framework development versus product development

During a framework test, classify every change before editing:

- Fix a runtime-neutral defect or reusable improvement in this base framework repository.
- Put product-specific agent, skill, rule, template, format, or process changes in the product repository's `.aafe/` layer.
- Put Product Code and product knowledge in the product repository, never in this framework repository.

Switch repositories explicitly and validate the affected layer independently. The base framework is read-only for ordinary product use, but remains writable when the human is deliberately developing or testing the framework itself.
