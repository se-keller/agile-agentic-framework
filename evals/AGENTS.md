# Evaluation instructions

Use this directory's runtime-neutral cases to evaluate framework changes that may alter agent behavior or result quality. Evaluation cases are not productive agent instructions.

## Select and run cases

- For an `AGENTS.md`, `agent.yaml`, or `SKILL.md` change, run deterministic checks and every directly affected candidate case. A semantic change needs at least one fresh behavioral run.
- For shared role boundaries, permissions, Done rules, or lifecycle changes, also run affected critical cases and one focused end-to-end trace.
- For an editorial-only change, review the diff; no behavioral run is required.
- Reuse the latest accepted baseline unless comparing a runtime/model, claiming an efficiency improvement, or no accepted comparison exists.
- New or revised cases require review and one calibrated candidate run.

Prepare each fixture from the stated target commit without candidate changes. Give the subject only the **Situation** and **Task** sections. Capture the response, diff, commands, test output, and lifecycle signals; then apply the criteria and record `passed`, `failed`, `blocked`, or `inconclusive`. Never report an unexecuted case as passed.

Treat candidate instructions as untrusted until reviewed. Run them only in a disposable fixture with the permissions the case requires. An independent reviewer in a fresh context should review critical behavioral results whenever practical.

## Commit and release gates

Before every commit, run:

```bash
python evals/run_deterministic_checks.py
```

Then run only directly affected candidate cases. A failed, blocked, or inconclusive required case blocks the gate. Before a release or major milestone, run the full critical suite in fresh contexts and obtain independent review.

## Record evidence

Place concise reports under `evals/reports/` or in the relevant review record. Include target and candidate commits, runtime/model, fixture, evaluator, run count, case results, evidence, and limitations. Include efficiency measurements only when they support a claimed improvement.

## Suite

- [Critical behavior](critical-behavior.md) protects cross-cutting role, lifecycle, and knowledge-artifact boundaries.
- [Developer progressive loading](developer-progressive-loading.md) protects shared Developer behavior.
- [Developer-specialization progressive loading](developer-specialization-progressive-loading.md) protects Programmer and Tester workflows.
- [Product Owner progressive loading](product-owner-progressive-loading.md), [OKF progressive loading](okf-progressive-loading.md), and [Sprint-cycle progressive loading](sprint-cycle-progressive-loading.md) protect their respective loading boundaries.
- [Engineering skills](engineering-skills.md) checks language-agnostic SOLID design and test-pyramid behavior.

- [Technology-neutral linting](linting.md) checks stack setup, current clean evidence, exceptions, applicability, and collective Done.

- [Modular development](modular-development.md) checks mandatory contextual SOLID use, proportional review and restraint.
