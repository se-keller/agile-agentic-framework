---
name: test-pyramid
description: Design, implement, and review automated test suites using a unit, integration, and acceptance/end-to-end test pyramid. Use when choosing the smallest effective test level, setting test boundaries, or maintaining fast, trustworthy coverage; do not use for detailed acceptance-test techniques that a dedicated skill covers.
---

# Test pyramid

Build confidence at the fastest test level that can expose the relevant defect. Keep tests readable, deterministic where their level permits, and focused on observable behavior rather than implementation accidents. Continuously curate the suite: when a slower test discovers a defect that a lower level could have caught, add or improve the lower-level test when useful.

## Choose the test level

### Unit tests

Use unit tests for individual programming units and their observable behavior. Aim for comprehensive coverage of production-code lines, with 100% line coverage as the default target; document genuine exceptions and do not treat coverage alone as proof of useful assertions.

- Keep each unit test independent of infrastructure: it must not access the internet, filesystem, database, or another external service.
- Use mocks, fakes, stubs, or in-memory collaborators only when they make the unit boundary explicit; do not over-mock internal details.
- Keep the suite in the millisecond range so it can run frequently during development and in continuous integration.
- Programmers create and maintain these tests with the Product Code.

### Integration tests

Use an integration test only to verify the contract between exactly two programming units. Exercise their real connection while keeping their internal implementations out of scope. Assert the agreed inputs, outputs, errors, schema, protocol, or side effects at that boundary—not each component's detailed behavior.

- Use mocks or test doubles for dependencies outside the two units when needed to preserve the boundary.
- Maintain fewer integration tests than unit tests and keep them fast enough for frequent feedback.
- Programmers create and maintain these tests with the Product Code.

### Acceptance and end-to-end tests

Use acceptance or end-to-end tests for a small number of representative user journeys that traverse the relevant user interface, application behavior, and data storage, then return an observable result to the user. Prefer a happy path; usually one or two journeys per feature are enough, depending on its risk and complexity. Create as few of these tests as possible, but as many as needed for confidence in the user-facing flow.

These tests can take longer because browsers, databases, or other dependencies must start. They may also encounter less controllable dependencies such as networks. Make their environment as controlled and reliable as practical, preserve and investigate flaky evidence, and never represent an unstable or unexecuted journey as passing.

Programmers and Testers define and evolve these tests together. The Programmer remains responsible for Product Code and automated acceptance-test implementation; the Tester retains independent execution, user-facing observation, and evidence responsibilities. Keep the technique generic here; load a dedicated acceptance or end-to-end testing skill when one provides the applicable technology-specific workflow.

## Apply the pyramid deliberately

- Prefer many isolated unit tests, fewer contract-focused integration tests, and the smallest useful set of acceptance/end-to-end journeys.
- Run the fast levels first and use them for local feedback. Run broader journeys when their dependencies are available and record any blocked condition honestly.
- Keep all levels aligned with the same business behavior without duplicating every assertion at every level.
- Treat a failing test as a defect signal unless there is evidence that the test itself is wrong or its environment is unavailable. Repair, remove, or quarantine a flaky test only with an explicit explanation; do not normalize unreliability.
- Do not use this skill to change Product Code when the active role lacks that permission, or to replace the Tester's independent testing and retest responsibilities.

## Source

Use [DORA: Test automation](https://dora.dev/capabilities/test-automation/) for the underlying continuous-feedback, fast-suite, developer-and-tester collaboration, acceptance, and test-pyramid guidance.
