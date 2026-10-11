# Engineering-skill evaluations

Run these cases when changing [`solid-design`](../skills/solid-design/SKILL.md) or [`test-pyramid`](../skills/test-pyramid/SKILL.md). Prepare the stated disposable fixture and give the subject only the **Situation** and **Task** sections. Capture the response, diff, commands, test output, and loaded skills. Use a fresh agent context for each candidate run.

## EVAL-SOLID-001 — SOLID without object-oriented ceremony

**Critical:** no  
**Subject:** Programmer  
**Source contracts:** [`solid-design`](../skills/solid-design/SKILL.md), [`programmer-core`](../skills/agent-core-skills/programmer-core/SKILL.md), [Programmer manifest](../agents/programmer/agent.yaml)

### Situation

A JavaScript checkout module exports one function. It calculates a total from an order, formats an audit record, writes that record to a file, and sends the order to a payment provider. Finance requests a new discount rule; Operations separately requests a change to the audit-record format. Existing callers expect the same checkout result and error behavior. Focused tests exist but currently must write to a filesystem and cannot run in isolation.

### Task

> As the Programmer, make the smallest maintainable change that supports the requested Finance and Operations changes. Preserve existing observable checkout behavior and add focused automated coverage. Do not introduce a class hierarchy merely to satisfy a design principle.

### Pass criteria

- Uses the SOLID skill and identifies Finance and Operations as distinct reasons for change or actors.
- Separates the discount policy, audit formatting, and volatile filesystem/payment details at proportionate boundaries while preserving the checkout contract.
- Uses a language-appropriate seam such as functions, data contracts, or dependency parameters; it does not introduce unnecessary classes, inheritance, or nominal interfaces.
- Adds or updates focused automated tests that verify the changed behavior without filesystem or network access where the test is intended as a unit test.
- Explains any retained coupling or trade-off in terms of the concrete change rather than speculative flexibility.

### Fail criteria

- Treats every function as requiring a class or interface, or adds indirection with no identified change pressure.
- Leaves unrelated actor-owned concerns coupled while claiming SRP compliance.
- Breaks the established checkout contract, omits focused test evidence, or expands permissions.

## EVAL-TEST-PYRAMID-001 — Classify test levels and preserve Developer boundaries

**Critical:** no  
**Subject:** Programmer and Tester as separate agents  
**Source contracts:** [`test-pyramid`](../skills/test-pyramid/SKILL.md), [`programmer-core`](../skills/agent-core-skills/programmer-core/SKILL.md), [`tester-core`](../skills/agent-core-skills/tester-core/SKILL.md), [Programmer manifest](../agents/programmer/agent.yaml), [Tester manifest](../agents/tester/agent.yaml)

### Situation

A Python web shop adds a promotional-price feature. `price_order` is pure business logic. `save_order` persists an order through a repository. A checkout route renders the result in a browser and reads it back from a test database. Current coverage has only slow browser tests, including duplicate edge-case assertions, and no clear failure evidence for a malformed repository response. The Product Owner supplied business-facing acceptance criteria for a successful discounted checkout and an understandable rejection of an invalid promotion.

### Task

> Work as the separate Programmer and Tester. Produce and implement a proportionate automated test plan for this feature, then provide the testable handoff and independent testing evidence within your respective permissions.

### Pass criteria

- Both agents load the test-pyramid skill and retain their distinct responsibilities and permissions.
- The Programmer adds isolated, infrastructure-free unit coverage for `price_order`, aiming for complete relevant line coverage and using doubles only at the boundary.
- The Programmer adds fewer, fast integration tests that verify only the contract between `save_order` and its repository, with dependencies outside that pair replaced as needed; the tests do not retest detailed pricing logic.
- Programmer and Tester jointly define a minimal acceptance/end-to-end set: the successful discounted user journey and, if justified by risk or complexity, the invalid-promotion journey. The journey covers the relevant UI, application behavior, and test data store.
- The Programmer implements and executes automated acceptance coverage; the Tester independently executes the agreed user-facing check after `implementation.testable`, records outcome evidence, and changes no Product Code.
- The result distinguishes unit, integration, and acceptance/end-to-end evidence, keeps the fast levels runnable frequently, and does not report blocked, failed, or unexecuted work as passed.

### Fail criteria

- A unit test uses filesystem, network, database, or other infrastructure.
- An integration test spans more than two programming units or asserts the detailed implementation of either unit rather than their contract.
- Browser journeys duplicate every unit edge case, acceptance coverage is treated as a Tester-only downstream phase, or the Tester edits Product Code.
- Either agent collapses role boundaries, claims an unexecuted result, or declares the Increment Done alone.
