---
okf_version: "0.2"
created: "2026-08-26"
updated: "2026-08-28"
---

# Agile Agentic Framework Documentation

This OKF bundle explains how to use, understand, maintain, and learn from the Agile Agentic Framework (AAF).

The documentation is **descriptive and non-normative**. Agents operate from the repository's `AGENTS.md`, manifests, and skills. No runtime, role, or product workspace may depend on this bundle to behave correctly.

## Choose a reading path

### Use the framework

1. [Framework guide](framework-guide.md)
2. [Sprint lifecycle](sprint-lifecycle.md)
3. [Repository and extension model](repository-and-extension-model.md)

### Understand and maintain the framework

1. [Architecture](architecture.md)
2. [Agentic principles](agentic-principles.md)
3. [Design decisions](design-decisions.md)
4. [Evaluation strategy](evaluation-strategy.md)

### Learn how to build an agent framework

1. [Building an agent framework](building-an-agent-framework.md)
2. [Architecture](architecture.md)
3. [Design decisions](design-decisions.md)
4. [Glossary](glossary.md)

## Documentation map

| Document | Primary framework sources |
|---|---|
| [Framework guide](framework-guide.md) | [`README.md`](https://github.com/se-keller/agile-agentic-framework/blob/main/README.md), [bootstrap skill](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/bootstrap-product-development/SKILL.md), [workspace template](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/bootstrap-product-development/assets/product-development-skeleton/AGENTS.md) |
| [Architecture](architecture.md) | [`AGENTS.md`](https://github.com/se-keller/agile-agentic-framework/blob/main/AGENTS.md), [interaction skill](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/manage-role-interaction/SKILL.md), [agent manifests](https://github.com/se-keller/agile-agentic-framework/tree/main/agents/), [skill catalog](https://github.com/se-keller/agile-agentic-framework/tree/main/skills/) |
| [Agentic principles](agentic-principles.md) | [role cores](https://github.com/se-keller/agile-agentic-framework/tree/main/skills/agent-core-skills/), [Sprint-cycle skill](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/run-sprint-cycle/SKILL.md) |
| [Sprint lifecycle](sprint-lifecycle.md) | [Sprint-cycle skill](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/run-sprint-cycle/SKILL.md), [Scrum Master core](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/agent-core-skills/scrum-master-core/SKILL.md), [Product Vision Board skill](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/product-vision-board/SKILL.md), and their workflow references |
| [Repository and extension model](repository-and-extension-model.md) | [`AGENTS.md`](https://github.com/se-keller/agile-agentic-framework/blob/main/AGENTS.md), [bootstrap skeleton](https://github.com/se-keller/agile-agentic-framework/tree/main/skills/bootstrap-product-development/assets/product-development-skeleton/) |
| [Evaluation strategy](evaluation-strategy.md) | [evaluation guide](https://github.com/se-keller/agile-agentic-framework/blob/main/evals/README.md), [critical cases](https://github.com/se-keller/agile-agentic-framework/blob/main/evals/critical-behavior.md), [commit checks](https://github.com/se-keller/agile-agentic-framework/blob/main/evals/run_deterministic_checks.py) |
| [Design decisions](design-decisions.md) | Current contracts, Git history, and [evaluation reports](https://github.com/se-keller/agile-agentic-framework/tree/main/evals/reports/) |
| [Building an agent framework](building-an-agent-framework.md) | Synthesis of the architecture and current contracts |

## Trust and maintenance

- Every concept is initially a draft until the human maintainer verifies it.
- Reconstructed rationale is labeled explicitly in the design-decision catalog.
- A semantic framework change must review the affected documents in this map.
- The commit gate validates this bundle's OKF structure and local links.
- Structural validation cannot prove that an explanation is semantically current; human review remains necessary.
