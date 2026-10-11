---
type: Framework Documentation
title: Glossary
description: Definitions of the central Scrum, agentic, runtime, and repository terms used by AAF.
status: draft
created: "2026-08-26"
updated: "2026-10-11"
generated: { by: "process:pbi-splitting-evaluierung-und-push", at: "2026-10-11T13:35:47.595424+00:00" }
framework: agile-agentic-framework
---

# Glossary

| Term | Meaning in AAF |
|---|---|
| Accountable agent | A separate runtime instance responsible for decisions within one declared role boundary. |
| Agent manifest | Runtime-neutral YAML declaring identity, core skills, permissions, subscriptions, and priority. |
| Core skill | Mandatory behavioral contract for a role or Developer specialization. |
| Detailed workflow | A reference loaded only for a matching lifecycle event or task. |
| Runtime host | The primary infrastructure context that negotiates interaction transport, activates agents, stores their identifiers, routes messages, and executes mechanical lifecycle transitions without acting as a Scrum role. |
| Agent identifier | Runtime-returned identity used to resume the same agent context. |
| Interaction mode | Session-scoped choice controlling whether the host presents role results, transparently proxies role dialogue, or performs a supported direct handoff. |
| Conversational owner | The one active role agent permitted to ask the human a blocking question and receive the next role-directed reply. |
| Transparent proxy | Host transport that visibly attributes and forwards a role's intended user-facing payload without material rewriting, then returns the human reply unchanged to the same role ID. |
| Direct handoff | Native runtime transfer of the same visible conversation to a role agent and later back to the host; a label, proxy, or separate task is not equivalent. |
| Role simulation | Producing multiple role-labeled answers in one context without real agent activation; prohibited by AAF. |
| Product workspace | Separate repository containing one product's code, OKF artifacts, and `.aafe` extensions; it is the working directory and write scope for product-role agents. |
| Workspace root | Parent directory containing a version-pinned `agile-agentic-framework/` checkout and one or more sibling product workspaces. |
| `.aafe` | Explicit product-local additions and overrides to the base framework. |
| OKF | Open Knowledge Format; indexed Markdown concepts with metadata, provenance, and human-readable links. |
| Product Code | Executable implementation and related technical files under `product-code/`. |
| Product artifact | Product knowledge or result evidence under `artefacts/`, not executable Product Code. |
| PBI | Product Backlog Item with stable identity, intended outcome, and observable Acceptance Criteria; near Sprint selection it is normally an appropriately small, valuable, testable vertical slice. |
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
