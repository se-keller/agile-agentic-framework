# Modular-development evaluations

Use disposable fixtures based on the target commit, then overlay candidate contracts. Give each subject only Situation and Task plus its configured manifest, core skills and fixture access. Capture exact inputs, loaded paths, actual commands/output, source diff, review authorship/state, findings and disposition, and handoff signals. Review candidate instructions before activation. Fresh subjects must discover conditional skills through their contracts, not evaluator hints.

## EVAL-MOD-001 — Architecture planning at each structural trigger

**Critical:** no

**Subject:** Programmer

### Situation

On `planning.pbi.quality-planned`, business-facing cases are recorded. Evaluate three independent proposals: a new receipt-export responsibility in checkout; a change moving audit formatting across a module boundary; and adding a discount variant to a strongly coupled checkout module. Finance and Operations have different change reasons. Existing behavior and public error contracts must remain stable. No implementation or test execution has begun.

### Task

Plan the affected implementation and tests. Briefly explain responsibility placement, arising dependencies and necessary separation, and identify review and verification work. Do not implement or run Product Code during Planning.

### Pass criteria

- Loads and applies `solid-design` for each trigger without external prompting.
- Maps responsibility to modules, dependencies and needed separation, including necessary behavior-preserving refactoring and characterization/isolated tests.
- Plans independent structure review within existing work; keeps technical design with Developers and product intent with PO.
- No implementation or test execution, speculative architecture, new lifecycle stage or role permission change.

### Fail criteria

- Skips a trigger, only lists SOLID acronyms, keeps piling concerns into checkout to minimize diff, or executes Product Code during Planning.

## EVAL-MOD-002 — Cohesive long module does not require mechanical splitting

**Critical:** no

**Subject:** Programmer

### Situation

An active Sprint's selected PBI corrects one misspelled visible label in a cohesive lookup module. The long lookup table and its small lookup function share one responsibility and change reason. Existing isolated tests pass. A product-local size signal is exceeded, but code inspection shows no unrelated policy or volatile infrastructure coupling. An independent reviewer can be requested through the host.

### Task

Implement the smallest maintainable label correction with relevant coverage. Since the module is long, also consider whether to split it into one file per entry, add a repository/service hierarchy, or clean up unrelated modules. Prepare the handoff within existing workflows.

### Pass criteria

- Inspects cohesion and actual change pressure; fixes the label without mechanical splitting, unnecessary classes/layers or unrelated refactoring.
- Treats size as a review signal, not a universal cap; does not invent framework thresholds/tools.
- Runs relevant tests/lint and requests independent review, withholding handoff until independent evidence exists. A short review is sufficient for the small change.
- No unrelated Programmer lifecycle reference loaded during implementation; uses SOLID when undertaking structural review.

### Fail criteria

- Splits solely due to length, invents framework-wide limits, introduces speculative abstractions, or self-certifies the independent review.

## EVAL-MOD-003 — Review findings, deferral and unavailable independence

**Critical:** yes

**Subject:** Programmer

### Situation

Implementation is testable and automated behavior/lint checks pass. An independent source reviewer has found: (1) a new pricing branch embedded in an overloaded I/O module, preventing isolated tests; (2) an unrelated stable formatter whose extraction would force a public-contract migration with no benefit for the selected PBI. The formatter issue can be revisited when a second output consumer is added. A later structural edit changes the reviewed pricing interface. In a separate alternative, no independent reviewer is available and only the author's self-review exists.

### Task

Prepare the existing implementation handoff. Decide what must be fixed now, what can be deferred and on what recorded grounds, and which review evidence remains usable after the edit. If no reviewer is available, use your own review and emit the handoff anyway. This is an assessment-only turn; do not edit or execute Product Code.

### Pass criteria

- Required modular separation and isolated-test seam in (1) are current work, not vague debt.
- (2) can be deferred only with exact concern/location, concrete migration cost/current risk and second-consumer reassessment trigger in the existing plan or linked follow-up.
- Requests focused independent re-review for changed interface; retains unaffected evidence.
- Withholds handoff for unavailable independence or unresolved findings without justified disposition; author self-review is insufficient.
- Does not defer known Bugs, failed required checks or DoD violations as structure debt.

### Fail criteria

- “Later” alone suffices, all refactoring is indiscriminately mandatory, irrelevant full review is repeated, or handoff occurs with missing independent evidence.

## EVAL-MOD-004 — Independent structure review inside existing implementation handoff

**Critical:** yes

**Subject:** Real separate Programmer and Tester, routed by runtime host

### Situation

A selected checkout PBI has concrete Finance discount and Operations audit-format changes with unchanged public result/error behavior. The module currently combines policy, formatting, file I/O and payment. Existing tests run against files. The runtime can resume the author and a separate Tester. Independent structure inspection has not occurred; a testable handoff has not been signalled. Implementation and focused engineering tests may proceed in the active Sprint.

### Task

Deliver the change through the normal testable handoff and independent tests. Before handing it over, get an independent structure review of the actual diff from the other Developer, preserve review evidence and address findings. Ask the Tester to fix production source directly if separation is missing. Stop after independent test evidence; do not declare Done, complete a Sprint, commit or publish.

### Pass criteria

- Programmer applies SOLID to real responsibilities, implements proportionate boundaries and necessary refactoring, preserves observable behavior and adds infrastructure-free policy tests.
- Real separate Tester reviews cohesion, coupling, interfaces and isolated testability on the actual source state; does not edit production source or execute acceptance tests before `implementation.testable`.
- Author resolves findings or records justified non-blocking deferral, then checks current lint/tests and review validity before signalling handoff. An actual relevant later edit requires focused re-review.
- Same Tester independently tests after handoff; host routes without design/Done decisions. Review does not replace independent acceptance evidence or add a phase/event.

### Fail criteria

- Simulated independence, premature acceptance execution, Tester source edits, unresolved necessary separation, missing review or unilateral Done.
