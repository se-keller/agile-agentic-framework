---
type: Framework Documentation
title: Framework Guide
description: A human-oriented guide to starting and operating a product with AAF.
status: draft
created: "2026-08-26"
updated: "2026-08-28"
generated: { by: "codex/gpt-5.6", at: "2026-08-28T08:57:39+02:00" }
framework: agile-agentic-framework
---

# Framework Guide

## What AAF provides

AAF is a small, runtime-neutral set of agent roles, role skills, Scrum lifecycle rules, workspace templates, and evaluations. It does not contain a model runtime or a product implementation.

You provide an agent runtime capable of starting real, resumable agents. AAF supplies the contracts that tell those agents what they are accountable for, what they may change, and how they collaborate.

## Start a product

From the framework repository, run the [bootstrap script](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/bootstrap-product-development/scripts/bootstrap.py):

```bash
python3 skills/bootstrap-product-development/scripts/bootstrap.py "My Product" --parent ../
```

The new workspace contains:

- `README.md` for people;
- `AGENTS.md` for the runtime host and agents;
- `product-code/` for implementation;
- `artefacts/` for OKF product knowledge and Scrum results; and
- `.aafe/` for explicit product-specific framework extensions.

At the first product interaction of each runtime session, choose among the modes the runtime can actually provide:

- `host` for host-presented, attributable role results;
- `transparent-proxy` for visibly attributed role dialogue transported by the host; or
- `direct-handoff` when the runtime supports a real transfer of the same visible conversation.

Then ask the runtime to start the Product Owner:

> Start the Product Owner for this product. Inspect the existing artifacts and Product Code first, then continue product discovery with me.

The runtime host starts a real Product Owner agent and applies the selected mode. Later answers return to that same agent instance. Unsupported modes are not offered or silently substituted. For a new Product Vision, the Product Owner briefly explains the simple and extended Product Vision Board, lets you choose, and guides you through one field at a time. English field names remain visible with translations when you work in another language. The completed board records what is confirmed, assumed, or still needs validation; it then guides the next concrete Product Goal.

## Typical interaction

```mermaid
sequenceDiagram
    actor Human
    participant Host as Runtime host
    participant PO as Product Owner agent
    participant SM as Scrum Master agent
    participant P as Programmer agent
    participant T as Tester agent

    Human->>Host: Select supported interaction mode
    Human->>Host: Start product discovery
    Host->>PO: Activate with workspace and role contract
    PO->>Host: User-facing board variants and focused questions
    Host->>Human: Present according to selected mode
    Human->>Host: Confirm board, then Product Goal
    Host->>PO: Resume the same Product Owner agent
    PO-->>Host: product-direction.ready
    Host->>Host: Load Sprint Planning router
    Host->>SM: Activate for Planning facilitation
    Host->>PO: Resume to present one PBI
    Host->>P: Ask understanding questions, then plan implementation
    Host->>T: Ask questions, plan business tests, review plan
    PO->>Host: Propose selection and Sprint Goal
    SM->>Host: Facilitation result; no lifecycle transition
    Host->>P: Implement first PBI and run automated tests
    P->>Host: implementation.testable
    Host->>T: Route testable implementation
    T-->>Host: Test evidence or test.finding
    Host->>P: Route finding to the same Developer agent
    Host->>PO: Route passing Increment for product inspection
    Host->>Host: Verify transition evidence
    Host->>Human: Present state and product feedback request
```

The arrows show responsibility and one possible host-mediated message flow. Transparent proxy changes presentation, and a capable runtime may replace those presentation arrows with a direct handoff. In every mode, the host owns only interaction and lifecycle mechanics. Each handoff activates or resumes the needed role. The Scrum Master is invoked for facilitation rather than acting as the dispatcher; Developers pull and coordinate work themselves.

## What to inspect during a run

- Product direction and available work under `artefacts/product-backlog/`.
- The active Sprint Goal and selected items under `artefacts/sprints/<sprint>/sprint-backlog/`.
- The evolving `developer-plan.md`.
- Product Code and tests under `product-code/`.
- Increment evidence under `artefacts/increment-documentation/`.
- Agent identifiers and lifecycle events in the runtime trace.

The filesystem is deliberately inspectable. It allows a human or resumed agent to understand current state without depending on hidden conversation memory.

## Extend one product without forking AAF

Put product-specific agents, skills, rules, or deliberate overrides under `.aafe/` and declare them in `.aafe/aafe.yaml`. An undeclared same-name collision is an error.

Change the base repository only for a runtime-neutral defect or reusable improvement. Product Code and product knowledge never belong in the framework repository.

## Common failure modes

| Symptom | Meaning | Response |
|---|---|---|
| The host answers as the Product Owner | A role was simulated instead of activated | Stop and require a real role agent |
| Direct handoff is offered without runtime support | Capability negotiation was bypassed | Offer only host or transparent proxy and ask the human to choose |
| Two roles ask the human at once | Conversational ownership was lost | Keep one active role and queue the other question |
| A later answer reaches a new agent | Agent identity was not preserved | Route through the stored runtime identifier |
| Scrum Master runs lifecycle routing | Facilitation and runtime mechanics were merged | Return transitions to the host and keep Scrum Master on demand |
| Scrum Master assigns coding tasks | Developer self-management was crossed | Return planning and work selection to Developers |
| Tester starts product tests during Planning | A sequencing boundary was skipped | Finish PBI-wise Planning and wait for `implementation.testable` |
| Scrum Master proposes the Sprint Goal | Product accountability was crossed | Let the Product Owner propose; let Developers co-create and agree it |
| Tester edits production source | Independent test boundary was crossed | Restore the source and route the finding to a Programmer |
| Open Bug is called a limitation | Done evidence is being bypassed | Keep delivery active until fix and independent retest |
| Product-specific change edits AAF | Framework and product layers were mixed | Move the change into the product's `.aafe/` layer |

## Where the truth lives

This guide helps people. Normative behavior lives in [`AGENTS.md`](https://github.com/se-keller/agile-agentic-framework/blob/main/AGENTS.md), [agent manifests](https://github.com/se-keller/agile-agentic-framework/tree/main/agents/), and [skills](https://github.com/se-keller/agile-agentic-framework/tree/main/skills/). If this guide conflicts with those files, the normative contracts win and this documentation must be corrected.
