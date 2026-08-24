# Framework evaluations

This directory defines runtime-neutral evaluations for changes that may alter agent behavior or the quality of framework results. Evaluations stay separate from the productive instructions in `AGENTS.md`, agent manifests, and skills: those files define expected behavior, while these cases test it.

The initial evaluations are intentionally executable by a human with an agent runtime. Add automation only when repeated use establishes a concrete need.

## When to run evaluations

Choose the smallest set that covers the changed behavior:

| Change | Required evidence |
|---|---|
| Script, validator, or workspace template | Relevant deterministic checks and a focused smoke test |
| `AGENTS.md`, `agent.yaml`, or `SKILL.md` | Every affected behavioral evaluation |
| Shared role boundary, permission, Done rule, or Sprint lifecycle | All critical behavioral evaluations |
| Claimed token, cost, latency, or activation reduction | Paired baseline and candidate runs that pass the same quality criteria, plus the claimed measurements |
| Editorial change with no semantic effect | Review of the diff; no behavioral run is required |
| Framework release or major milestone | All critical evaluations and relevant deterministic checks |

Run a baseline from the unchanged target commit before a candidate when the change claims an improvement or may subtly alter behavior. Change one coherent concern at a time, then repeat the same evaluations with the same runtime, model, settings, task, and fixture.

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
5. Repeat the run with the candidate change under the same conditions.
6. For a critical case, any candidate failure blocks acceptance. Repeat a critical or variable case in fresh contexts when one run is not representative; document the number of runs.

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

Add a case when a defect, framework trial, or proposed change reveals a behavior important enough to protect. Keep each case traceable to its source contract and avoid asserting one exact wording when several correct responses are possible.
