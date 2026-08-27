---
type: Framework Documentation
title: Architecture
description: The layers, components, dependencies, and runtime interaction model of AAF.
status: draft
created: "2026-08-26"
updated: "2026-08-27"
generated: { by: "codex/gpt-5.6", at: "2026-08-27T00:00:00+02:00" }
framework: agile-agentic-framework
---

# Architecture

## Architectural overview

AAF separates three concerns that are often mixed in agent systems:

1. **Runtime:** starts, resumes, isolates, and routes real agents.
2. **Framework:** defines reusable roles, permissions, skills, lifecycle rules, and evaluations.
3. **Product workspace:** contains one product's code, knowledge, Sprint state, and explicit extensions.

```mermaid
flowchart TB
    subgraph Runtime["Agent runtime"]
        H["Primary host"]
        I["Agent identity and routing"]
        X["Isolated role agents"]
        H --> I --> X
    end

    subgraph Framework["Base AAF repository"]
        M["Agent manifests"]
        S["Core and process skills"]
        B["Bootstrap assets"]
        E["Evaluations"]
    end

    subgraph Product["Product workspace"]
        W["Workspace AGENTS.md"]
        K["OKF artefacts"]
        C["Product Code"]
        P[".aafe extensions"]
    end

    H --> W
    X --> M
    X --> S
    B --> Product
    P -. "explicit add or override" .-> M
    P -. "explicit add or override" .-> S
    X --> K
    X --> C
    E -. "tests behavior" .-> Runtime
    E -. "tests contracts" .-> Framework
```

## The primary host is transport, not a role

The primary agent context coordinates the runtime mechanism. It starts the required role agent, stores the returned identifier, and routes later human replies and lifecycle messages to the same instance.

The host must not load a role's core skills and perform that role itself. This prevents one conversational context from producing apparently independent product, technical, testing, and process decisions.

## Manifests and skills have different jobs

An [agent manifest](https://github.com/se-keller/agile-agentic-framework/tree/main/agents/) declares stable configuration:

- identity and display name;
- mandatory core skills;
- permissions;
- subscribed lifecycle events; and
- task priority.

A [core skill](https://github.com/se-keller/agile-agentic-framework/tree/main/skills/agent-core-skills/) defines behavioral accountability and operating boundaries. Process skills such as [run-sprint-cycle](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/run-sprint-cycle/SKILL.md) coordinate work across roles without absorbing their decisions.

```mermaid
flowchart LR
    E["Lifecycle event"] --> M["Agent manifest"]
    M --> R["Separate role instance"]
    R --> C["Mandatory core skill"]
    C --> Q{"Specific workflow needed?"}
    Q -- "No" --> O["Act with compact core"]
    Q -- "Yes" --> F["Load one matching reference"]
    F --> O
```

## Roles and authority

| Role | Owns | Must not own |
|---|---|---|
| Product Owner | Product direction, Product Goal, Product Backlog content and order, value | Product Code, technical solution, Done decision |
| Scrum Master | Process, transparency, lifecycle facilitation, impediment visibility | Product priority, task assignment, technical plan, Done decision |
| Programmer | Product Code, implementation, technical decisions, engineering tests | Product value and independent Tester result |
| Tester | Independent test design and evidence, test assets, Bug reporting and retest | Production source changes, unilateral Done decision |
| Stakeholder | Declared perspective, observations, needs, feedback | Product decisions, artifact mutation, technical direction |

Programmer and Tester are specializations of the same Scrum Developer accountability. They share [`developer-core`](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/agent-core-skills/developer-core/SKILL.md) and add specialization-specific contracts.

## Two inspectable planes

AAF uses a control plane and a knowledge/work plane:

- The **control plane** consists of manifests, skills, permissions, runtime identities, events, and lifecycle rules.
- The **knowledge/work plane** consists of OKF artifacts, Product Code, tests, Sprint Backlogs, plans, and evidence.

The control plane determines who may act and when. The knowledge/work plane records what is known and what changed. The documentation bundle sits outside both planes and describes them for people.

Lifecycle events are handoffs, not broadcasts. In Sprint Planning, the Product Owner presents and clarifies one PBI; the Tester contributes business-facing cases; the Programmer plans implementation; and the Tester reviews testability. During delivery, the Programmer hands a testable slice to the Tester, then passing evidence to the Product Owner for inspection. This sequencing preserves independent perspectives without allowing premature execution.

## Runtime neutrality

AAF names required capabilities—real agent activation, resumable identifiers, message routing, permissions, and inspectable files—without prescribing a vendor API. A conforming runtime maps those concepts to its own native mechanism.

This neutrality has a limit: if a runtime cannot create or resume a required separate agent, AAF stops that transition. It does not fall back to role simulation.

## Dependency direction

```mermaid
flowchart LR
    D["Human documentation"] -. "references" .-> F["Normative framework"]
    P["Product .aafe layer"] --> F
    R["Runtime"] --> F
    F --> W["Generated product workspace"]
    W --> A["Product agents and artefacts"]

    A -. "must not depend on" .-> D
    F -. "must not depend on" .-> D
```

The dashed lines toward documentation are explanatory only. Removing `docs/` must not change agent behavior.
