# OKF progressive-loading evaluations

Run these paired cases when changing OKF skill routing or claiming reduced OKF context use. Record every OKF skill and reference file loaded, the artifact diff, and validator output.

## EVAL-OKF-LOAD-001 — Ordinary framework artifact update

**Source contracts:** `okf`, the acting role's manifest and core skills.

**Situation**

An active Sprint has a Developer Plan and Sprint Backlog. A Programmer has completed one focused check and must record attributable evidence, coordination needs, and the next unblocked verification work.

**Task**

Update the affected current-state artifacts and validate the bundle.

**Pass criteria**

- Produces valid, concise updates without changing Product Code or assessing Done.
- Loads `$okf` but not `$okf-advanced` or its specification.
- Preserves existing metadata, workflow state, other Developers' evidence, and current links.

**Fail criteria**

- Loads the advanced skill or specification without an explicit advanced feature.
- Loses required context, metadata, evidence, or structural validity.

## EVAL-OKF-LOAD-002 — Explicit advanced OKF contract

**Source contracts:** `okf`, `okf-advanced`, OKF v0.2 specification.

**Situation**

A human explicitly requests an OKF v0.2 Attested Computation with typed parameters, an executor receipt, a deterministic attester, `stale_after`, multiple sources with credibility signals, and per-claim attribution.

**Task**

Create and validate the requested OKF bundle.

**Pass criteria**

- Loads `$okf`, `$okf-advanced`, and only the relevant specification sections.
- Produces a structurally valid Attested Computation with parameter-only agent input, consistent source IDs and footnotes, and the requested trust and attestation fields.
- Does not invent execution or attestation success when those operations were not actually run.

**Fail criteria**

- Attempts the advanced contract from the compact profile alone or loads the whole specification without need.
- Produces invalid or internally inconsistent advanced fields.
