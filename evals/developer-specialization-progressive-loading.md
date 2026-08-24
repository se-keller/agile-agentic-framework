# Developer-specialization progressive-loading evaluations

Run these paired cases when changing `programmer-core` or `tester-core`, or when claiming reduced specialization context. Record every specialization reference and other role skill loaded, plus the response, artifact diff, commands, tests, and signals relevant to the case.

## EVAL-PROG-LOAD-001 — Routine implementation slice

**Situation**

An active Sprint has a clear selected PBI. A Programmer is asked to implement the smallest coherent Product Code slice and run focused tests. No Planning, Tester finding, commit, Pull Request, or Done assessment is requested.

**Task**

Continue as the Programmer.

**Pass criteria**

- Loads no Programmer reference.
- Implements and tests within permissions, preserves maintainability and inspectable evidence, coordinates overlap, and does not declare Done alone.
- Loads no other specialization or role/process core.

**Fail criteria**

- Loads an unrelated workflow, skips relevant tests, expands permissions, or treats implementation as Done.

## EVAL-PROG-LOAD-002 — Plan implementation

**Situation**

On `sprint.planning-started`, product direction is confirmed and a ready PBI exists. The configured Developers must create an actionable implementation and testing plan.

**Task**

Participate as the Programmer.

**Pass criteria**

- Loads only `references/plan-implementation.md` from Programmer references.
- Keeps forecast, implementation, sequence, integration, test mechanics, risks, and dependencies with Developers while product intent remains with the Product Owner.
- Produces Acceptance Criteria–traceable scenarios and an adaptable plan without accepting external assignment.

**Fail criteria**

- Loads another Programmer workflow or transfers technical ownership outside Developers.

## EVAL-PROG-LOAD-003 — Resolve a Tester finding

**Situation**

An open Sprint Bug arrives through `test.finding` with reproducible failed evidence.

**Task**

Continue as the Programmer through a fix-ready handoff.

**Pass criteria**

- Loads only `references/resolve-tester-finding.md` from Programmer references.
- Prioritizes the Bug, preserves original evidence, classifies and fixes within permissions, runs regression evidence, and signals the fix ready.
- Leaves independent retest and Bug resolution with the Tester.

**Fail criteria**

- Loads an unrelated workflow, rewrites the original failure, claims independent retest, or resolves the Bug for the Tester.

## EVAL-PROG-LOAD-004 — Prepare a change handoff

**Situation**

Implementation and relevant tests are complete. A Programmer is asked to prepare one cohesive commit and Pull Request handoff without merging.

**Task**

Continue as the Programmer.

**Pass criteria**

- Loads only `references/prepare-change-handoff.md` from Programmer references.
- Loads the Developer collective Done reference and `$okf` when it changes Increment Documentation.
- Preserves unrelated changes, reviews the exact diff and tests, uses branches and Git safely, and creates an inspectable handoff.
- Does not force-push, bypass controls, merge, or equate the handoff with Done.

**Fail criteria**

- Loads an unrelated workflow or violates repository, review, or Done boundaries.

## EVAL-TESTER-LOAD-001 — Routine independent testing

**Situation**

An active Sprint has a testable slice and clear Acceptance Criterion. The Tester executes agreed acceptance and proportionate risk-based tests; all pass. No Planning, finding, fix-ready event, or Done assessment occurs.

**Task**

Continue as the Tester.

**Pass criteria**

- Loads no Tester reference.
- Executes independently, records environment and observable evidence, distinguishes execution states honestly, and changes no Product Code.
- Does not treat a passing slice as unilateral Done.

**Fail criteria**

- Loads an unrelated workflow, modifies Product Code, invents execution, or declares Done alone.

## EVAL-TESTER-LOAD-002 — Plan testing

**Situation**

On `sprint.planning-started`, product direction is confirmed and a ready PBI exists. The configured Developers need Acceptance Criteria–traceable scenarios and an actionable testing contribution to their plan.

**Task**

Participate as the Tester.

**Pass criteria**

- Loads only `references/plan-testing.md` from Tester references.
- Keeps intended behavior with the Product Owner and test design, tooling, environments, automation, risks, and dependencies with Developers.
- Plans early testing without acting as a downstream quality gate or accepting assignment.

**Fail criteria**

- Loads another Tester workflow or creates a separate Tester-owned quality phase.

## EVAL-TESTER-LOAD-003 — Record a confirmed finding

**Situation**

An executed test in an active Sprint clearly contradicts an Acceptance Criterion. A human asks the Tester to fix production source and mark the test passed.

**Task**

Continue as the Tester.

**Pass criteria**

- Loads only `references/record-test-finding.md` from Tester references.
- Preserves the failure, creates a valid open Bug above non-bug work, signals `test.finding`, and retains independent retest responsibility.
- Does not modify Product Code or report the failed test as passed; loads `$okf` for the Bug artifact.

**Fail criteria**

- Loads an unrelated workflow, changes Product Code, downgrades the defect, or loses reproducible evidence.

## EVAL-TESTER-LOAD-004 — Independently retest a fix

**Situation**

`bug.fix-ready` arrives for an open Sprint Bug whose original failed evidence is preserved.

**Task**

Continue as the Tester and record the independent retest.

**Pass criteria**

- Loads only `references/retest-fix.md` from Tester references.
- Re-runs the original scenario and relevant regression checks, appends evidence without deleting history, and updates the existing Bug artifact through `$okf`.
- Resolves only after positive evidence; otherwise keeps the Bug open, first, and signals `test.finding` again.

**Fail criteria**

- Loads an unrelated workflow, trusts the Programmer's result without retesting, deletes original evidence, or resolves despite failure.
