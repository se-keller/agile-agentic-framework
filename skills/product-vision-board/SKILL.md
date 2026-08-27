---
name: product-vision-board
description: Guide a human step by step through Roman Pichler's simple or extended Product Vision Board and persist the result as the product's Product Vision. Use when establishing, replacing, or substantially revising product direction; do not use for a Product Goal alone.
---

# Product Vision Board

Use this skill as the Product Owner's collaborative discovery format. Keep the creative product direction with the human, expose uncertainty, and use the shared `$okf` skill when writing the Product Vision artifact.

## Let the human choose the board

Before asking board questions, briefly explain both variants and let the human choose:

- **Simple:** Vision, Target Group, Needs, Product, and Business Goals. Prefer it for quickly clarifying the initial product direction without detailing the business model.
- **Extended:** the simple board plus Competitors, Revenue Streams, Cost Factors, and Channels. Use it when business-model assumptions should be explored now, especially for a new or significantly changed business model.

Keep the comparison short. Do not select a variant on the human's behalf. If an existing board already declares its variant, resume that variant unless the human wants to change it.

## Facilitate one field at a time

Work through the chosen board as a dialogue:

1. Discuss one field at a time with one to three focused, open questions.
2. Summarize the proposed field content and its knowledge state, then let the human correct or confirm it before moving on.
3. Start with Vision. Clarify Target Group and Needs before Product, and do not let solution ideas replace the user or customer need. Then cover Business Goals. For the extended board, continue with Competitors, Revenue Streams, Cost Factors, and Channels.
4. Revisit earlier fields when a later answer exposes a conflict. Prioritize multiple Needs and Business Goals. Keep Product to three to five coarse-grained standout capabilities rather than epics, stories, or technical design.
5. Challenge unclear claims and ask what evidence supports them, but never invent users, strategy, evidence, feasibility, or commercial intent.

Use the user's chosen language for the dialogue and content. Field headings always start with the canonical English term. When the chosen language is not English, append a concise translation in parentheses, for example `Target Group (Zielgruppe)`.

Cover these questions in natural language; do not recite them as a questionnaire:

- **Vision:** Why should the product exist, and what positive, enduring change should it create?
- **Target Group:** Which market or segment is addressed, and who are the users and customers?
- **Needs:** Which main problem is solved or benefit created, and what does success look like for users or customers?
- **Product:** What kind of product is it, which three to five high-level capabilities make it stand out, and what feasibility uncertainty matters?
- **Business Goals:** Why should the providing organization invest, which outcomes should result, and what rough targets would demonstrate them?
- **Competitors:** Which alternatives or competitors matter, and what are their relevant strengths and weaknesses?
- **Revenue Streams:** How might the product generate revenue or other direct financial return?
- **Cost Factors:** What are the important costs to develop, market, sell, operate, and service it?
- **Channels:** How will target customers learn about, acquire, or access the product, and which channels already exist?

## Make uncertainty visible

Mark each material statement with one of these states, translated in parentheses when the working language is not English:

- `Confirmed`: established knowledge or a deliberate organizational decision with a stated basis.
- `Assumption`: a plausible claim currently accepted for planning but not validated.
- `To validate`: an open or material claim that requires evidence before it can be relied on.

Ask for the basis of a `Confirmed` statement. Human approval of the wording confirms the artifact; it does not by itself turn an assumption into validated knowledge. Record useful evidence, validation ideas, and unresolved questions below the board when they do not fit clearly inside a cell.

## Write the Product Vision artifact

Persist the completed board at the workspace's configured Product Vision path, normally `artefacts/product-backlog/product-vision.md`. Preserve valid existing OKF metadata and use `type: Product Vision`. Record the selected board variant in frontmatter as `vision_board_variant: simple` or `vision_board_variant: extended`.

Render the board as portable Markdown tables. Use a separate one-column table for Vision so it appears across the full board width, followed by the four-column core table:

```markdown
| Vision (translation when needed) |
|---|
| ... |

| Target Group (translation when needed) | Needs (translation when needed) | Product (translation when needed) | Business Goals (translation when needed) |
|---|---|---|---|
| ... | ... | ... | ... |
```

For the extended board, add this third table below the core table:

```markdown
| Competitors (translation when needed) | Revenue Streams (translation when needed) | Cost Factors (translation when needed) | Channels (translation when needed) |
|---|---|---|---|
| ... | ... | ... | ... |
```

Within each cell, keep entries readable and include their state labels. Use Markdown line breaks or compact lists inside cells when needed. After the tables, add concise Markdown sections for context, rationale, evidence, validation ideas, or open questions when they make the Product Vision more precise. The artifact need not be limited to the tables.

Include this visible attribution, translated if useful without changing the names or links:

> Adapted from the [Product Vision Board](https://www.romanpichler.com/blog/the-product-vision-board/) by [Roman Pichler](https://www.romanpichler.com/). This adapted board is licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0).

Review the whole board with the human for coherence, prioritization, and unsupported certainty. Add human verification to the OKF artifact only after explicit confirmation of the complete current board.

## Continue with the Product Goal

After the Product Vision Board is complete and confirmed, use it as input to establish one concrete current Product Goal. The goal must advance the Vision, remain consistent with the chosen Target Group, Needs, and Business Goals, and create useful evidence for one or more important `Assumption` or `To validate` statements. Collaborate with the human on the goal separately; do not silently derive or activate it.

## Source and license

The Product Vision Board was created by Roman Pichler. This skill adapts the board structure and guidance from the [official article](https://www.romanpichler.com/blog/the-product-vision-board/) and [official tool](https://www.romanpichler.com/tools/product-vision-board/). The adapted Product Vision Board material in this skill is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
