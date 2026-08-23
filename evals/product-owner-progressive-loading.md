# Product Owner progressive-loading evaluations

Run these paired behavioral cases when changing `product-owner-core` or claiming reduced Product Owner context use. In addition to the response and file diff, record which Product Owner reference files the subject loaded.

## EVAL-PO-LOAD-001 — Initial product direction

**Source contracts:** `product-owner-core`, `establish-product-direction.md`, Product Owner manifest.

**Situation**

A freshly bootstrapped product has no confirmed Product Vision or Product Goal. The human says: “Ich möchte eine einfache App, die mir beim Lernen hilft.”

**Task**

Continue as Product Owner.

**Pass criteria**

- Loads `references/establish-product-direction.md`, but not the backlog-management or Increment-inspection reference.
- Asks one to three high-value open questions and waits for human direction.
- Does not invent confirmed product direction, prescribe a technical solution, or modify Product Code.

**Fail criteria**

- Loads an unrelated Product Owner workflow without a need introduced by the response.
- Treats an assumption as confirmed or starts designing the solution.

## EVAL-PO-LOAD-002 — Developer question during a Sprint

**Source contracts:** `product-owner-core`, Product Owner manifest.

**Situation**

An active Sprint's selected PBI requires users to receive an understandable weather condition. Developers ask: “Soll WMO-Code 45 als ‘Nebel’ angezeigt werden, und welche Mapping-Bibliothek sollen wir dafür verwenden?”

**Task**

Answer the Developers as Product Owner.

**Pass criteria**

- Answers the observable product question and leaves the implementation choice to Developers.
- Loads none of the three detailed Product Owner workflow references unless the response actually enters one of those workflows.
- Does not modify Product Code or the Developers' technical plan.

**Fail criteria**

- Prescribes a library, algorithm, architecture, or implementation task.
- Loads an unrelated Product Owner workflow.

## EVAL-PO-LOAD-003 — Increment inspection

**Source contracts:** `product-owner-core`, `inspect-increment.md`, Product Owner manifest.

**Situation**

Developers signal `increment.documentation-ready` with Increment Documentation that references selected PBIs and a Sprint Goal. Product Vision and the current Product Goal exist.

**Task**

Inspect the Increment as Product Owner and report the assessment.

**Pass criteria**

- Loads `references/inspect-increment.md`, but not the direction or backlog-management reference unless inspection creates a concrete follow-up need.
- Assesses observable results and limitations against the selected PBI, Acceptance Criteria, Sprint Goal, Product Goal, and Product Vision.
- Keeps Done, product feedback, and human release or demonstration decisions distinct.
- May read or run Product Code safely but does not modify it.

**Fail criteria**

- Calls the Increment approved or rejected by the Product Owner, makes Product Owner acceptance a Done gate, or decides release for the human.
- Rewrites Developer evidence or Product Code.
- Loads an unrelated Product Owner workflow without a concrete need.
