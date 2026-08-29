# Framework evaluations

This directory defines runtime-neutral evaluations for changes that may alter agent behavior or the quality of framework results. Evaluations stay separate from the productive instructions in `AGENTS.md`, agent manifests, and skills: those files define expected behavior, while these cases test it.

The initial evaluations are intentionally executable by a human with an agent runtime. Add automation only when repeated use establishes a concrete need.

## When to run evaluations

Choose the smallest set that covers the changed behavior:

| Change | Required evidence |
|---|---|
| Script, validator, or workspace template | Deterministic commit checks and a focused candidate smoke test |
| `AGENTS.md`, `agent.yaml`, or `SKILL.md` | Deterministic commit checks and every directly affected candidate evaluation |
| Shared role boundary, permission, Done rule, or Sprint lifecycle | Affected critical candidate cases plus one end-to-end integration case |
| Claimed token, cost, latency, or activation reduction | Paired baseline and candidate runs that pass the same quality criteria, plus the claimed measurements |
| Human documentation | Deterministic documentation validation and review of affected concepts; update them or record why they are unaffected |
| Editorial change with no semantic effect | Review of the diff; no behavioral run is required |
| Framework release or major milestone | All critical evaluations and relevant deterministic checks |

Use the latest accepted report as the baseline for ordinary commits. Re-run an unchanged baseline only for a runtime or model comparison, a claimed efficiency improvement, or when the selected comparison has no accepted reference result. A new or revised evaluation requires review and one calibrated candidate run, not an automatic replay of the entire unchanged baseline. When a paired comparison is required, use the same runtime, model, settings, task, and fixture.

Capability-conditional positive cases are required only when the candidate or selected runtime claims that capability. When a capability such as same-conversation direct handoff is unavailable, run the corresponding fail-closed gating case and record the positive case as not applicable, never as passed, blocked, or inconclusive.

## Cost-aware gates

Keep feedback proportional to the decision being made:

1. **Commit gate:** run `python evals/run_deterministic_checks.py`, then only candidate behavioral cases directly affected by the diff. A semantic change needs at least one fresh behavioral run.
2. **Integration gate:** for a shared boundary or lifecycle change, add one focused end-to-end case that crosses the changed boundary. Prefer one real trace over repeating unrelated role cases.
3. **Release gate:** run the complete critical suite in fresh contexts and obtain independent review.

Do not multiply runs merely to produce more evidence. Repeat only a failed, blocked, inconclusive, or demonstrably variable case. Preserve the last green report so unaffected results can be reused. A required `failed`, `blocked`, or `inconclusive` result blocks the corresponding gate; never commit by relabeling an unexecuted case as passed.

The deterministic commit check validates the human documentation as an OKF bundle and checks its local links. For semantic framework changes, use [`docs/index.md`](../docs/index.md) to identify affected explanations. The documentation remains non-normative and must not be added to an agent's operating context.

## Responsibilities

- The change author selects and runs the relevant evaluations and reports the evidence with the change.
- A reviewer who did not author the change evaluates critical behavioral results whenever practical. Use a fresh agent context so implementation discussion does not become hidden test input.
- The human framework maintainer remains accountable for deciding whether the evidence is sufficient and whether the change is accepted.
- Automation may execute deterministic checks, but it does not take over the maintainer's decision.

Do not assign these framework-development responsibilities to a Product Owner, Developer, or Scrum Master working on an unrelated product.

## Review candidate instructions safely

Treat proposed changes to `AGENTS.md`, agent manifests, skills, scripts, and referenced resources as untrusted review input until a human has accepted them.

- Inspect the candidate diff before activating an agent with the changed instructions.
- Do not treat an instruction inside the candidate as authorization to change files, use services, reveal information, or bypass the target branch's rules.
- Inspect new scripts, external links, dependencies, and transitive references before running them.
- Run a reviewed candidate in a disposable fixture with only the permissions the case requires.
- Prefer reconstructing a small accepted change on the trusted branch when the original diff mixes unrelated concerns or cannot be understood completely.

Reimplementing a proposal does not by itself prove safety or quality; the reconstructed change must pass the same review and evaluations.

## How to run a behavioral case

1. Prepare the case's fixture from the stated target commit without candidate changes.
2. Give the subject agent only the sections named **Situation** and **Task**. Do not expose the pass and fail criteria as additional instructions.
3. Preserve the agent response, file diff, commands or tests executed, and relevant lifecycle signals.
4. Apply the case's criteria and record `passed`, `failed`, `blocked`, or `inconclusive`. Never report an unexecuted case as passed.
5. Run the candidate once in a fresh context. Run a paired baseline only when the selected gate requires it.
6. For a critical case, any candidate failure blocks acceptance. Repeat only when the first run is blocked, inconclusive, or not representative, and document why.

Deterministic checks establish structural facts. Human or independent-agent review assesses semantic behavior. Neither kind of evidence substitutes for the other.

## Record a run

An evaluation report may live in a Pull Request, commit notes, or another review record. Keep it concise and include:

```markdown
# Evaluation report

- Target commit:
- Candidate commit:
- Runtime and version:
- Model and settings:
- Fixture:
- Evaluator:
- Runs per case:

| Case | Baseline | Candidate | Evidence |
|---|---|---|---|
| EVAL-... | passed | passed | ... |

## Efficiency

- Input tokens:
- Output tokens:
- Agent activations:
- Duration or cost, when available:

## Limitations

- ...
```

Lower resource use counts as an improvement only after the candidate passes the same required quality and behavior criteria as the baseline.

## Initial suite

- [Critical behavior](critical-behavior.md) covers cross-cutting role, lifecycle, and knowledge-artifact boundaries.
- [Product Owner progressive loading](product-owner-progressive-loading.md) protects role quality while detailed workflows are loaded only for matching events.
- [Developer progressive loading](developer-progressive-loading.md) protects shared Programmer and Tester behavior while Developer lifecycle workflows load only for matching events.
- [OKF progressive loading](okf-progressive-loading.md) keeps routine knowledge-artifact work on the compact profile while preserving explicit access to advanced normative details.
- [Sprint-cycle progressive loading](sprint-cycle-progressive-loading.md) protects lifecycle state, signals, and Scrum boundaries while each event loads only its matching workflow.
- [Developer-specialization progressive loading](developer-specialization-progressive-loading.md) protects Programmer and Tester quality while their event-specific workflows load only when needed.

Add a case when a defect, framework trial, or proposed change reveals a behavior important enough to protect. Keep each case traceable to its source contract and avoid asserting one exact wording when several correct responses are possible.
