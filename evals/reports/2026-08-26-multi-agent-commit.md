# Evaluation report: minimal multi-agent execution

- Date: 2026-08-26
- Target commit: `f62cda351932df25b19e6a8e4cc8cb6282a2e8f8`
- Candidate: the commit containing this report
- Runtime: native Codex subagents
- Model and settings: inherited from the runtime host; exact values were not exposed

## Commit gate

| Case | Baseline | Candidate | Evidence |
|---|---|---|---|
| Deterministic commit checks | not required | passed | Diff, YAML, Markdown links, bootstrap placeholders, and OKF validation passed. |
| `EVAL-PO-001` | passed | passed | The Product Owner changed no Product Code and left the technical approach with Developers. |
| `EVAL-TEST-001` | passed | passed | A real failing test remained failed; the Tester created and prioritized `BUG-0001`, changed no production source, and retained independent retest responsibility. |
| `EVAL-SM-001` | passed | passed | The Scrum Master refused individual assignment and left the Developer Plan and technical sequence with Developers. |
| `EVAL-OKF-001` | passed | passed | A ready PBI and index entry passed full-bundle validation with 0 errors and 0 warnings. |
| `EVAL-OKF-002` | passed | passed | Stable and unknown metadata were preserved, stale verification was removed, and validation passed with 0 errors and 0 warnings. |
| `EVAL-ENTRY-001` | not required; revised evaluation with calibrated candidate run | passed | Host `/root/eval_entry_candidate` started Product Owner `/root/eval_entry_candidate/fixture_product_owner`. The Product Owner received workspace `AGENTS.md`, its manifest and core skill without using the human `README.md` as operating input; it inspected `.aafe`, artifact state, and Product Code before asking its first discovery questions. A marked follow-up resumed the same ID. Bootstrap and OKF validation passed. |
| `EVAL-MULTI-001` | no accepted reference result | passed | Host `/root/eval_multi_candidate` used distinct Product Owner, Scrum Master, Programmer, and Tester agents and resumed their IDs across lifecycle events. Programmer checks passed 5/5; independent Tester checks passed 7/7. |
| `EVAL-SPRINT-LOAD-001` | not required | passed | The `EVAL-MULTI-001` trace loaded only `plan-sprint.md` before `sprint.started`. |

`EVAL-SPRINT-LOAD-002` through `004` were not selected: their routing references and event-specific behavior were unchanged by this candidate. No unexecuted case is reported as passed.

## Multi-agent trace

- Product Owner: `/root/eval_multi_candidate/product_owner`
- Scrum Master: `/root/eval_multi_candidate/scrum_master`
- Programmer: `/root/eval_multi_candidate/programmer`
- Tester: `/root/eval_multi_candidate/tester`
- Lifecycle observed: `product-direction.ready`, `sprint.planning-requested`, `sprint.planning-started`, `sprint.started`, `developer.work-available`, `implementation.testable`, first independent test result
- Stop boundary: the run stopped before Done, Review, or Retrospective.

## Limitations

- Exact token, cost, model, and reasoning settings were not exposed by the runtime.
- The Tester could not perform a real 375×667 browser rendering in that fixture, and no freshness threshold was defined. These did not block the first independent acceptance result requested by `EVAL-MULTI-001`.
- Early runs with incomplete fixtures and runs interrupted by the usage limit were discarded and are not counted as evidence.
