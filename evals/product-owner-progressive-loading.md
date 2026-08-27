# Product Owner progressive-loading evaluations

Run these paired behavioral cases when changing `product-owner-core` or claiming reduced Product Owner context use. In addition to the response and file diff, record which Product Owner reference files the subject loaded.

## EVAL-PO-LOAD-001 — Initial product direction

**Source contracts:** `product-owner-core`, `establish-product-direction.md`, `product-vision-board`, Product Owner manifest.

**Situation**

A freshly bootstrapped product has no confirmed Product Vision or Product Goal. The human says: “Ich möchte eine einfache App, die mir beim Lernen hilft.”

**Task**

Continue as Product Owner.

**Pass criteria**

- Loads `references/establish-product-direction.md` and the `product-vision-board` skill, but not the backlog-management or Increment-inspection reference.
- Briefly distinguishes the simple board from the business-model-oriented extended board, gives useful selection guidance, and lets the human choose before asking field questions.
- Does not invent confirmed product direction, prescribe a technical solution, or modify Product Code.

**Fail criteria**

- Loads an unrelated Product Owner workflow without a need introduced by the response.
- Selects a board variant for the human, treats an assumption as confirmed, or starts designing the solution.

## EVAL-PO-LOAD-004 — Guided extended Product Vision Board

**Source contracts:** `product-owner-core`, `establish-product-direction.md`, `product-vision-board`, `okf`, Product Owner manifest.

**Situation**

A freshly bootstrapped German-language product has no confirmed Product Vision or Product Goal. The human has selected the extended Product Vision Board and says: “Wir möchten kleinen Handwerksbetrieben helfen, ihre kurzfristige Einsatzplanung verlässlicher zu machen. Mehr wissen wir noch nicht.”

**Task**

Continue as Product Owner.

**Pass criteria**

- Works on one board field at a time with no more than three focused questions and waits for the human's answer.
- Uses canonical English field names with German translations in parentheses.
- Distinguishes confirmed knowledge, assumptions, and matters to validate without claiming that human agreement validates a market hypothesis.
- Keeps the human responsible for creative product direction and does not jump ahead to a Product Goal or technical solution.

**Fail criteria**

- Presents the entire board as a long questionnaire or completes fields from invented information.
- Uses only translated headings, conflates artifact confirmation with hypothesis validation, or starts Product Goal discovery before the board is complete.

## EVAL-PO-LOAD-005 — Persist the board and continue to Product Goal

**Source contracts:** `product-owner-core`, `establish-product-direction.md`, `product-vision-board`, `okf`, Product Owner manifest.

**Situation**

The human and Product Owner have completed and explicitly confirmed a German-language extended Product Vision Board. Some statements have supporting evidence, two are assumptions, and one needs validation. No Product Goal exists yet.

**Task**

Persist the Product Vision and continue product-direction discovery.

**Pass criteria**

- Writes a valid OKF `Product Vision` artifact with `vision_board_variant: extended` and current provenance and verification metadata.
- Uses a one-column Markdown table for Vision, a four-column Markdown table for the core fields, and a third four-column Markdown table for Competitors, Revenue Streams, Cost Factors, and Channels.
- Uses English headings with German translations, preserves statement-level knowledge states, and may add useful explanatory sections below the table.
- Attributes Roman Pichler, links the source, and states CC BY-SA 4.0 for the adapted board.
- Starts a separate dialogue for one concrete Product Goal that advances the board and seeks evidence for important hypotheses; it does not invent or silently activate the goal.

**Fail criteria**

- Produces only an unstructured vision statement, omits a board row or attribution, or marks every statement confirmed merely because the human approved the artifact.
- Creates a Product Goal inconsistent with the board, prescribes a technical solution, or fails to use the board's hypotheses as input.

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
