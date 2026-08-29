# Evaluation report: interaction modes and host lifecycle

- Date: 2026-08-28
- Target commit: `6e372d9ef6145d8ef32cd9cd12f63a9a5060ea60`
- Candidate: the commit containing this report
- Runtime: Codex native subagents with stable follow-up identifiers; no same-conversation direct handoff
- Model and settings: inherited from the runtime host; exact values were not exposed
- Fixture: disposable workspace at `/private/tmp/aaf-eval-QUjkFh/product-development-interaction-evaluation`
- Runs per case: one accepted candidate run

## Commit and integration gates

| Case | Baseline | Candidate | Evidence |
|---|---|---|---|
| Deterministic commit checks | reused from the latest accepted report | passed | Diff, YAML, local links, bootstrap, placeholders, and OKF validation passed. |
| `EVAL-ENTRY-001` | reused | passed | The generated human and agent entry points remained separate, capability-gated interaction selection was available, and a distinct Product Owner inspected the workspace and began discovery. |
| `EVAL-INTERACTION-001` | revised case; calibrated candidate run | passed | The [preserved proxy trace](traces/2026-08-28-transparent-proxy.md) records capabilities, session mode, exact intended and visible payloads, the character-identical human reply and forwarded content, stable IDs, follow-up, and absence of replacement or private output. |
| `EVAL-INTERACTION-002` | new case; calibrated candidate run | passed | A host offered only `host` and `transparent-proxy` after explaining that same-conversation direct handoff was unavailable; it did not silently downgrade or impersonate the Product Owner. |
| `EVAL-INTERACTION-003` | not applicable | not applicable | This runtime has no verified same-conversation handoff capability, so only the required fail-closed gating case was run. |
| `EVAL-SM-001` | reused | passed | Scrum Master refused Sprint start, PBI assignment, and Tester routing while accepting facilitation of a testability disagreement and preserving Developer self-management. |
| `EVAL-SM-PLANNING-001` | revised case; calibrated candidate run | passed | In the integration trace the host sequenced Planning, the Product Owner proposed selection and Goal, Developers planned and forecast, and the Scrum Master facilitated without routing or transitions. |
| `EVAL-DONE-001` / `EVAL-SPRINT-LOAD-003` | reused / revised | passed | With an open Bug and failed required test, the host loaded only delivery completion, withheld Done and completion signals, kept the Bug prioritized, and treated Scrum Master attention only as response to the requested Scrum deviation. |
| `EVAL-SPRINT-001` / `EVAL-SPRINT-LOAD-004` | reused / revised | passed | The host loaded only Sprint closing, emitted `sprint.completed`, left no active Sprint, and did not create or start another Sprint despite ready backlog work. |
| `EVAL-SPRINT-LOAD-002` | revised case; calibrated candidate run | passed | The host loaded only delivery coordination, resumed the preserved Product Owner for a product question, preserved safe parallel progress, and did not activate the Scrum Master for routine routing. |
| `EVAL-MULTI-001` / `EVAL-SPRINT-LOAD-001` | revised cases; end-to-end integration | passed | The [preserved multi-agent trace](traces/2026-08-28-multi-agent-sprint.md) records distinct resumable role IDs, activation and follow-up order, lifecycle signals, phase-specific references, authorship, interruption recovery, and negative boundary evidence. |

## End-to-end trace

- Product Owner: `/root/eval_combined_e2e/product_owner`
- Scrum Master: `/root/eval_combined_e2e/scrum_master`
- Programmer: `/root/eval_combined_e2e/programmer`
- Tester: `/root/eval_combined_e2e/tester`
- Lifecycle observed: `sprint.planning-requested`, `sprint.planning-started`, PBI-wise planning handoffs, `sprint.started`, `developer.work-available`, `implementation.testable`, `implementation.tested`
- Host actions: readiness and artifact inspection, role routing, and evidence-backed lifecycle signals only
- Scrum Master actions: Planning facilitation only; no role activation, routing, transition, product decision, technical decision, or artifact authorship
- Programmer result: four automated tests passed; both acceptance commands produced the specified exit status and streams
- Independent Tester result: both acceptance commands, all four tests, and one exploratory alternate-role case passed; no Bug was created
- Stop boundary: first independent Tester result; no Increment, PBI, or Sprint Done claim was made

The first implementation turn was interrupted by a workspace credit limit. After credits returned, the host verified that no partial Product Code existed and resumed the same Programmer identifier. No replacement role or host simulation was used.

## Documentation review

The documentation map was reviewed. Architecture, framework guide, Sprint lifecycle, agentic principles, framework-building guidance, design decisions, evaluation strategy, glossary, and index were updated for the new interaction modes and host/Scrum-Master boundary. `repository-and-extension-model.md` was reviewed and remains unaffected because the repository layout and extension precedence did not change.

## Limitations

- Exact token, duration, cost, model, and reasoning settings were not exposed.
- Positive direct-handoff behavior remains unexecuted and is explicitly not applicable on this runtime.
- The disposable product example was a small Python CLI and is evidence for interaction, identity, role, and lifecycle behavior rather than WebApp UI behavior.
