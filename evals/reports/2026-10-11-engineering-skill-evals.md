# Evaluation report: engineering-skill evaluations

- Date: 2026-10-11
- Target commits: `6a23bcf` (`solid-design`) and `d19e73a` (`test-pyramid`)
- Candidate: working tree containing `evals/engineering-skills.md`
- Runtime: fresh Codex subagent contexts
- Evaluator: independent calibration agents
- Fixture: scenario-only calibration; no Product Code fixture was created or changed

## Calibration runs

| Case | Candidate | Evidence |
|---|---|---|
| `EVAL-SOLID-001` | passed | The fresh Programmer proposed function-level seams for discount policy, audit formatting, and volatile file/payment details; preserved the one-argument checkout contract; used injected fakes for isolated tests; and explicitly rejected an unjustified class hierarchy. |
| `EVAL-TEST-PYRAMID-001` | passed | The fresh calibration separated infrastructure-free `price_order` unit coverage, the `save_order`–repository contract tests, and exactly two browser/database journeys. It retained Programmer implementation responsibility, Tester independent evidence responsibility, and made no Done claim. |

## Limitations

- The calibration tested the clarity and evaluability of the cases, not an implementation in a disposable Product Code fixture. No test command, handoff, independent execution, or acceptance result is claimed.
- A future candidate run must prepare the described disposable fixture, use separate Programmer and Tester agents for `EVAL-TEST-PYRAMID-001`, and preserve the required code and execution evidence.

## Documentation review

The evaluation guide was updated to list the new suite. The human-documentation map was reviewed: framework architecture, roles, permissions, lifecycle, extension model, and evaluation strategy remain accurate because this adds cases without changing their contracts.
