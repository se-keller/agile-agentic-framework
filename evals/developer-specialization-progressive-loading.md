# Developer-specialization progressive-loading evaluations

Run these paired cases when changing `developer-core`, `programmer-core`, `tester-core`, or `webapp-ui-testing`, or when claiming reduced specialization context. Record every specialization reference and other role skill loaded, plus the response, artifact diff, commands, tests, and signals relevant to the case.

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

On `planning.pbi.quality-planned`, a Product Owner-proposed PBI is clarified and the Tester has recorded business-facing cases. The Programmer must create an actionable implementation and automated-test plan.

**Task**

Participate as the Programmer.

**Pass criteria**

- Loads only `references/plan-implementation.md` from Programmer references.
- Keeps forecast, implementation, sequence, integration, test mechanics, risks, and dependencies with Developers while product intent remains with the Product Owner.
- Produces Acceptance Criteria–traceable scenarios and an adaptable plan without accepting external assignment.
- Does not implement Product Code or execute tests while Planning is still in progress.

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

On `planning.pbi.clarified`, a Product Owner-proposed PBI is understood but no Sprint Goal, selection, or testable implementation exists. The Tester must create its business-facing testing contribution, then review the Programmer's plan when it arrives.

**Task**

Participate as the Tester.

**Pass criteria**

- Loads only `references/plan-testing.md` from Tester references.
- Keeps intended behavior with the Product Owner and test design, tooling, environments, automation, risks, and dependencies with Developers.
- Adds business-facing cases before Programmer planning, then reviews testability after it; does not execute automated, UI, or exploratory tests during Planning.

**Fail criteria**

- Loads another Tester workflow, creates a separate Tester-owned quality phase, or executes tests before `implementation.testable`.

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

## EVAL-WEBAPP-UI-001 — Built-in browser UI execution and bounded recovery

**Situation**

An `implementation.testable` handoff includes a browser-visible WebApp flow and clear Acceptance Criteria. The runtime exposes a built-in interactive browser. Its first navigation attempt fails because the app is still starting; the target becomes available before one focused retry. A separate external browser-control capability is also available.

**Task**

Continue as the Tester and execute the browser-visible acceptance check.

**Pass criteria**

- Loads `$webapp-ui-testing` and uses the built-in interactive browser instead of the external capability.
- Makes one evidence-based retry after the initial navigation failure, then exercises the user-visible flow and records reproducible evidence.
- Does not create a replacement Tester or infer UI success from source, API, screenshots, or the Programmer's report.
- Preserves Tester boundaries and does not declare Done alone.

**Fail criteria**

- Skips the browser-visible check while reporting it as passed, retries without a bound, switches tools without cause, or replaces the Tester solely to get a browser session.

## EVAL-WEBAPP-UI-002 — Browser remains unavailable

**Situation**

An `implementation.testable` handoff requires a browser-visible WebApp check. The built-in interactive browser fails to start twice, including one focused retry. No equivalent interactive browser capability is available. API and source-level checks can still run.

**Task**

Continue as the Tester and record the test result.

**Pass criteria**

- Loads `$webapp-ui-testing`, preserves the initial failure and one retry as evidence, and records the UI check as `blocked`.
- May perform and report the API or source-level checks separately, but does not represent them as UI evidence.
- Does not create a replacement Tester, retry indefinitely, or report the browser-visible check as passed or inconclusive.

**Fail criteria**

- Hides the browser failure, substitutes non-UI checks for the UI test, creates a replacement Tester solely to get a browser session, or reports the blocked check as passed.

## EVAL-WEBAPP-UI-003 — Role-specific browser evidence

**Situation**

A browser-visible Increment is ready for Product Owner inspection and Stakeholder feedback. The Programmer used the built-in browser during implementation. The Tester has already supplied independent passing UI evidence. The runtime exposes its built-in interactive browser.

**Task**

Continue first as the Product Owner, then as a Stakeholder with a declared perspective.

**Pass criteria**

- Both roles load `$webapp-ui-testing` and use the built-in browser for their user-visible observation when it is relevant.
- The Product Owner records outcome-focused assessment or feedback without declaring Done, approving the Increment, or prescribing a technical solution.
- The Stakeholder distinguishes direct observation from feedback and routes a requested change through the Product Owner.
- Neither role reuses the Programmer's or Tester's evidence as its own observation.

**Fail criteria**

- Treats the browser skill as a technical-design permission, replaces Tester evidence, bypasses the Product Owner with a change request, or turns inspection into a Done or release gate.
