---
name: okf-advanced
description: Apply advanced Open Knowledge Format v0.2 features that require normative specification detail. Use only when a task explicitly requires sources or per-claim attribution, source credibility signals or usage windows, stale_after, Attested Computation contracts, executors, receipts or attesters, external bundle exchange, migration, or version conformance. Always combine with `okf`; never use for ordinary framework artifacts or routine validation.
---

# Advanced Open Knowledge Format

Use this skill together with `$okf`. Keep the compact `$okf` profile authoritative for ordinary concepts, indexes, lifecycle fields, workflow fields, trust metadata, links, and validation.

Resolve [the OKF v0.2 specification](references/SPEC.md) relative to this `SKILL.md`. Consult only the part required by the explicit advanced feature:

- `sources`, credibility signals, usage windows, or per-claim footnotes: §5.1.
- `stale_after`: §5.5.
- Advanced path or mirrored-reference questions: §6.2–6.3.
- Attested Computations, parameter binding, executors, receipts, and attesters: §10.
- External exchange or strict conformance: §3, §11, and §12.
- Migration from OKF v0.1: §13.

Find section boundaries first with `rg -n '^##|^###' references/SPEC.md`, then read only the required section range. Do not preload the whole specification.
