---
type: Definition of Done
status: stable
created: "{{GENERATED_DATE}}"
updated: "{{GENERATED_DATE}}"
generated: { by: "process:bootstrap-product-development", at: "{{GENERATED_AT}}" }
product: "{{PRODUCT_SLUG}}"
---

# Definition of Done

Work is part of an Increment only when all of the following are true:

- all relevant automated and manual tests pass;
- all regression tests pass and no regression is known;
- affected existing features still work;
- all Acceptance Criteria are fulfilled;
- Product Code is integrated, executable, and usable;
- stack-appropriate linting is configured and all required checks have passed on the final integrated state with zero errors and warnings;
- there are no known unresolved bugs (Zero Bug Policy);
- known limitations are transparent;
- Increment Documentation has been created; and
- the Product Owner has inspected the Increment Documentation, run the Increment when reasonably possible, assessed it against the PBI, Sprint Goal, Product Goal, and Product Vision, and the assessment is recorded.

Product Owner inspection supplies product feedback; it is not approval or rejection. The inspection criterion is fulfilled by completing and recording the assessment, irrespective of whether it produces follow-up work. Developers remain accountable for determining that the Definition of Done is met.

## Linting

Developers select actively maintained linting compatible with every relevant language and component when choosing or expanding the technology stack. The Programmer versions configuration and pins tool versions in the product repository, provides a reproducible automated invocation, and integrates it into existing automated quality checks when available. Setup and a clean run are required before the first testable handoff.

Missing setup, failed, blocked, aborted, or unexecuted checks and open findings prevent Done. Changes to relevant source, tool versions, or configuration require fresh evidence. A successful exit status alone does not establish a clean run.

Do not weaken rules, exclude affected files, or suppress findings to obtain a pass. Legitimate exceptions require a narrow scope, technical rationale, and recorded joint Developer review. Only a jointly reviewed and recorded absence of lintable source or technical files permits non-applicability; reassess when the stack or files change.

## Minimum Increment Documentation

- understandable description of the Increment;
- instructions for trying it;
- test results;
- linting invocation, tool versions, configuration, checked scope, source revision or exact worktree state, and actual results, or the jointly reviewed non-applicability rationale;
- relevant commits, diffs, and Pull Requests;
- known limitations; and
- links to the Product Backlog Item and Sprint Goal.

## After Done

Developers document possible Retrospective topics after declaring the work Done. This follow-up does not change the Increment's Done status.
