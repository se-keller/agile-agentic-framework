---
type: Decision Catalog
title: Design Decisions
description: A catalog of the main architectural choices in AAF, their rationale, tradeoffs, and evidence strength.
status: draft
created: "2026-08-26"
updated: "2026-08-28"
generated: { by: "codex/gpt-5.6", at: "2026-08-28T08:57:39+02:00" }
framework: agile-agentic-framework
decision_state: reconstructed-awaiting-human-verification
---

# Design Decisions

This catalog reconstructs rationale from current contracts, Git history, and evaluation evidence. “Explicit” means the decision is directly stated in a current contract. “Reconstructed” means the motivation is inferred and requires human confirmation.

## D-001 — Keep the framework runtime-neutral

- **Status:** explicit decision; rationale partly reconstructed
- **Decision:** Describe agents, permissions, skills, events, and required delegation capabilities without embedding one vendor's API.
- **Why:** Product and Scrum behavior should remain portable across runtimes. Vendor adapters can evolve without rewriting the role model.
- **Tradeoff:** The runtime must map abstract capabilities to native mechanisms, and unsupported capabilities must fail closed.
- **Evidence:** [`AGENTS.md`](https://github.com/se-keller/agile-agentic-framework/blob/main/AGENTS.md), [agent manifests](https://github.com/se-keller/agile-agentic-framework/tree/main/agents/), commit `df3451e`.

## D-002 — Keep the host infrastructure-only

- **Status:** explicit decision
- **Decision:** The primary context negotiates interaction transport, activates and routes real agents, and performs evidence-backed lifecycle mechanics, but no configured Scrum role.
- **Why:** One context cannot provide credible independence between product, implementation, testing, and facilitation decisions.
- **Tradeoff:** The host needs explicit process contracts and must distinguish deterministic transition checks from role judgment.
- **Evidence:** [`AGENTS.md`](https://github.com/se-keller/agile-agentic-framework/blob/main/AGENTS.md), [workspace template](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/bootstrap-product-development/assets/product-development-skeleton/AGENTS.md), `EVAL-MULTI-001`.

## D-003 — Split static manifests from behavioral skills

- **Status:** reconstructed rationale
- **Decision:** Keep identity, permissions, subscriptions, and required skills in YAML manifests; keep behavior and workflows in Markdown skills.
- **Why:** Runtimes can discover stable configuration without loading full behavior, while humans can review behavioral contracts as readable text.
- **Tradeoff:** Consistency across manifest and skill must be reviewed and evaluated.
- **Evidence:** [agent manifests](https://github.com/se-keller/agile-agentic-framework/tree/main/agents/) and [role cores](https://github.com/se-keller/agile-agentic-framework/tree/main/skills/agent-core-skills/).

## D-004 — Share one Developer core across specializations

- **Status:** explicit decision
- **Decision:** Programmer and Tester are equal Scrum Developers with a shared core plus narrower specialization skills.
- **Why:** Testing and implementation remain one accountable delivery team while retaining distinct permissions and independent evidence.
- **Tradeoff:** The framework must prevent specialization boundaries from becoming separate subteams or unilateral Done authority.
- **Evidence:** [Developer core](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/agent-core-skills/developer-core/SKILL.md), [Programmer core](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/agent-core-skills/programmer-core/SKILL.md), [Tester core](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/agent-core-skills/tester-core/SKILL.md).

## D-005 — Store state as inspectable OKF files

- **Status:** explicit decision; rationale partly reconstructed
- **Decision:** Persist product knowledge, Scrum artifacts, decisions, and results in an indexed Markdown bundle with stable metadata.
- **Why:** Humans and resumed agents need state that survives conversation context, can be diffed, and remains readable without a database tool.
- **Tradeoff:** Agents must maintain indexes, dates, provenance, links, and authoritative file movement.
- **Evidence:** [OKF skill](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/okf/SKILL.md), bootstrap skeleton, commits `7ca627c`, `c16d2dc`, and `aa7dbc6`.

## D-006 — Load detailed workflows progressively

- **Status:** explicit decision
- **Decision:** Start with compact core skills and load one event-specific reference only when needed.
- **Why:** Smaller context reduces irrelevant instructions, token use, and accidental role leakage.
- **Tradeoff:** Routing metadata and progressive-loading evaluations must remain accurate.
- **Evidence:** commits `fcb3358`, `8589cb6`, `1bae998`, `94bcb2a`, and `f62cda3`; progressive-loading evals under [`evals/`](https://github.com/se-keller/agile-agentic-framework/tree/main/evals/).

## D-007 — Isolate product extensions under `.aafe`

- **Status:** explicit decision
- **Decision:** Product-specific additions and overrides live in the product workspace and must be declared explicitly.
- **Why:** Product experiments must not silently mutate reusable framework behavior.
- **Tradeoff:** A reusable lesson requires a deliberate second change in the base repository.
- **Evidence:** [`AGENTS.md`](https://github.com/se-keller/agile-agentic-framework/blob/main/AGENTS.md), [bootstrap workspace instructions](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/bootstrap-product-development/assets/product-development-skeleton/AGENTS.md).

## D-008 — Use an event-driven Sprint lifecycle

- **Status:** explicit framework adaptation
- **Decision:** Advance Sprints through inspectable readiness and completion events instead of a calendar timebox.
- **Why:** Autonomous agent execution needs resumable transition boundaries and may not map cleanly to wall-clock ceremonies.
- **Tradeoff:** This differs from the Scrum Guide's fixed-length Sprint and must remain clearly labeled as an adaptation.
- **Evidence:** [Sprint-cycle skill](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/run-sprint-cycle/SKILL.md), executed by the infrastructure-only host.

## D-009 — Enforce Zero Bug and collective Done

- **Status:** explicit decision
- **Decision:** A known open Bug or failed required test blocks Done; Developers determine Done collectively after Product Owner assessment and complete evidence.
- **Why:** Relabeling defects as limitations would make lifecycle completion untrustworthy. Separating assessment, Done, and release prevents authority collapse.
- **Tradeoff:** A Sprint may remain active or return unfinished work rather than report nominal completion.
- **Evidence:** [Developer Done workflow](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/agent-core-skills/developer-core/references/establish-done-collectively.md), [delivery completion](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/run-sprint-cycle/references/determine-delivery-completion.md), `EVAL-DONE-001`.

## D-010 — Use proportional evaluation gates

- **Status:** explicit decision
- **Decision:** Run deterministic and affected candidate checks per commit, one end-to-end trace for shared boundaries, and the full critical suite for releases.
- **Why:** Full multi-agent baseline/candidate matrices consumed too much runtime quota for routine commits.
- **Tradeoff:** Confidence is accumulated across stored reports; every commit does not independently rerun the complete suite.
- **Evidence:** [evaluation guide](https://github.com/se-keller/agile-agentic-framework/blob/main/evals/README.md), commit `df3451e`, [latest report](https://github.com/se-keller/agile-agentic-framework/blob/main/evals/reports/2026-08-26-multi-agent-commit.md).

## D-011 — Keep documentation non-normative

- **Status:** human-requested decision
- **Decision:** Maintain an OKF documentation bundle for people, but do not make framework execution or agent behavior depend on it.
- **Why:** Explanations can become richer without expanding agent context or creating a second operational source of truth.
- **Tradeoff:** Commit governance must keep explanations aligned with normative files.
- **Evidence:** This documentation initiative and the maintenance rules in [`AGENTS.md`](https://github.com/se-keller/agile-agentic-framework/blob/main/AGENTS.md).

## D-012 — Use PBI-wise handoffs instead of role-wide Planning broadcasts

- **Status:** human-requested decision
- **Decision:** Plan candidates one PBI at a time: Product Owner presentation and clarification, Tester business-facing cases, Programmer implementation plan, then Tester testability review. Delivery likewise proceeds Programmer, independent Tester, Product Owner inspection, and the next PBI. The host routes the sequence; an on-demand Scrum Master facilitates Planning but does not propose the Sprint Goal or own transitions.
- **Why:** Broad simultaneous activation caused roles to act on incomplete information, including premature Tester execution. Explicit handoffs make dependencies visible while retaining separate role agents and Developer self-management.
- **Tradeoff:** Planning has more small transitions and each active PBI is intentionally sequential unless a product explicitly configures a different adaptation.
- **Evidence:** [Sprint-cycle Planning](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/run-sprint-cycle/references/plan-sprint.md), [delivery coordination](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/run-sprint-cycle/references/coordinate-delivery.md), `EVAL-SPRINT-PLANNING-001`.

## D-013 — Let the human choose a capability-gated interaction mode

- **Status:** human-requested decision
- **Decision:** At the start of each runtime session, offer only supported `host`, `transparent-proxy`, and `direct-handoff` modes and let the human select or later change the mode.
- **Why:** Dialog-heavy role work, especially Product Owner discovery, should feel direct without making a same-conversation handoff a portability requirement.
- **Tradeoff:** Runtimes expose different choices, and unsupported direct handoff must fail closed rather than being approximated silently.
- **Evidence:** [interaction skill](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/manage-role-interaction/SKILL.md), workspace host contract, `EVAL-INTERACTION-001`, and `EVAL-INTERACTION-002`.

## D-014 — Use the Scrum Master on demand, not as the lifecycle engine

- **Status:** human-requested decision
- **Decision:** The runtime host owns deterministic state checks, agent routing, and lifecycle signals. A stable Scrum Master agent is activated for Planning facilitation, impediments, Scrum deviations, Review support when needed, Retrospective, and improvement.
- **Why:** Runtime mechanics do not require independent Scrum judgment, while coaching, facilitation, impediment handling, and effectiveness improvement do.
- **Tradeoff:** The boundary between a mechanical transition and facilitative judgment must remain explicit and evaluated.
- **Evidence:** [Scrum Master core](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/agent-core-skills/scrum-master-core/SKILL.md), [Sprint-cycle skill](https://github.com/se-keller/agile-agentic-framework/blob/main/skills/run-sprint-cycle/SKILL.md), `EVAL-SM-PLANNING-001`, and `EVAL-MULTI-001`.
