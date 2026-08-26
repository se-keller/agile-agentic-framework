---
type: Framework Documentation
title: Glossary
description: Definitions of the central Scrum, agentic, runtime, and repository terms used by AAF.
status: draft
created: "2026-08-26"
updated: "2026-08-26"
generated: { by: "process:framework-documentation", at: "2026-08-26T14:57:16+02:00" }
framework: agile-agentic-framework
---

# Glossary

| Term | Meaning in AAF |
|---|---|
| Accountable agent | A separate runtime instance responsible for decisions within one declared role boundary. |
| Agent manifest | Runtime-neutral YAML declaring identity, core skills, permissions, subscriptions, and priority. |
| Core skill | Mandatory behavioral contract for a role or Developer specialization. |
| Detailed workflow | A reference loaded only for a matching lifecycle event or task. |
| Runtime host | The primary context that activates agents, stores their identifiers, and transports messages without acting as a Scrum role. |
| Agent identifier | Runtime-returned identity used to resume the same agent context. |
| Role simulation | Producing multiple role-labeled answers in one context without real agent activation; prohibited by AAF. |
| Product workspace | Separate repository containing one product's code, OKF artifacts, and `.aafe` extensions. |
| `.aafe` | Explicit product-local additions and overrides to the base framework. |
| OKF | Open Knowledge Format; indexed Markdown concepts with metadata, provenance, and human-readable links. |
| Product Code | Executable implementation and related technical files under `product-code/`. |
| Product artifact | Product knowledge or result evidence under `artefacts/`, not executable Product Code. |
| PBI | Product Backlog Item with stable identity, intended outcome, and observable Acceptance Criteria. |
| Developer | Scrum accountability shared by Programmer and Tester specializations. |
| Independent test | Test result produced by a Tester agent distinct from the Programmer whose implementation is evaluated. |
| Done | Collective Developer conclusion that the complete Definition of Done is satisfied by evidence. |
| Product assessment | Product Owner inspection and feedback; neither acceptance nor the Done decision. |
| Lifecycle event | Named transition signal such as `sprint.started`, `test.finding`, or `increment.done`. |
| Event-driven Sprint | AAF adaptation that advances through explicit evidence-backed events rather than a calendar timebox. |
| Commit gate | Cheap deterministic checks plus directly affected candidate behavioral cases. |
| Integration gate | Focused end-to-end trace for a changed shared boundary or lifecycle. |
| Release gate | Complete critical evaluation suite with fresh contexts and independent review. |
| Normative source | `AGENTS.md`, manifest, or skill that defines required behavior. Documentation is non-normative. |
