# Evaluation report: human and agent documentation boundary

- Date: 2026-10-11
- Candidate: working tree that replaces `evals/README.md` with `evals/AGENTS.md` and removes the nested Product Code README from the bootstrap template
- Fixture: `/private/tmp/aaf-readme-eval.kISH6d/product-development-readme-boundary`
- Evaluator: Codex

## Focused candidate evidence

| Check | Result | Evidence |
|---|---|---|
| Bootstrap README boundary | passed | A fresh `bootstrap.py "README Boundary" --parent <temporary directory> --no-git` workspace contained exactly one `README.md`, at its root. |
| Agent entry-point boundary | passed | The base `AGENTS.md`, evaluation `AGENTS.md`, and generated workspace `AGENTS.md` direct operational content to agent contracts rather than a README. |
| OKF validation | passed | The generated workspace `artefacts/` bundle passed `validate_okf.py`. |
| Deleted-file commit check | passed | `repository_files()` now excludes a tracked file deleted in the working tree, so local-link validation can run before staging the deletion. |
| Deterministic commit checks | passed | `python evals/run_deterministic_checks.py` passed: diff, YAML, local links, bootstrap, placeholders, and OKF validation. |

## Documentation review

The repository and extension model, evaluation strategy, documentation index, decision catalog, and agentic-principles links were updated because their source and layout references changed. The framework guide remains accurate: it already describes the generated root README as human-facing and `AGENTS.md` as the agent entry point. Lifecycle, role, and product-process documentation are unaffected.

## Limitation

This focused run verifies the added nested-README invariant of `EVAL-ENTRY-001`; it is not a replay of that case's separate-agent interaction behavior, which is unaffected by this change.
