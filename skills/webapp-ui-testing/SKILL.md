---
name: webapp-ui-testing
description: Inspect or test a browser-visible web application through the runtime's built-in interactive browser when available. Use for user-visible implementation checks, independent UI tests, Product Owner Increment inspection, or stakeholder observation; do not use for API, source-level, or non-browser work.
---

# WebApp UI Testing

Use this skill for browser-visible behavior that requires a real user interaction or visual confirmation. It may be used by Programmers, Testers, Product Owners, and Stakeholders within their respective permissions and lifecycle handoffs. Prefer the runtime's built-in interactive browser capability when it is available. This keeps the observation close to the user experience and avoids making a particular vendor tool or browser implementation part of the framework contract.

## Execute browser-visible checks

1. Confirm the target environment, URL or launch path, test data, and expected observable behavior before interacting with the application.
2. Open the application with the built-in interactive browser. Exercise the intended flow through user-visible controls; observe the resulting state, messages, navigation, and relevant layout or accessibility behavior.
3. Record evidence appropriate to the role: environment, viewport or device context when material, preconditions, actions, expected result or observation, actual result, and relevant browser evidence.
4. Use the browser for the parts that are user-visible. Supporting logs, network evidence, or automated checks may help diagnose a result, but never substitute for a claimed executed UI interaction or observation.

## Recover from an unavailable browser capability

- If the browser cannot start, attach, navigate, or perform the requested interaction, first inspect the reported failure and make one focused retry. Correct an evident local precondition such as an unavailable application URL or an expired page state first; otherwise use the retry only to rule out a transient capability failure.
- Do not repeatedly retry, create a replacement agent solely to obtain a browser session, or treat a new session as proof that the original failure did not occur. A runtime may offer a deliberate recovery or resume mechanism; use it only when it preserves the current agent's identity and the required separation of duties.
- If the built-in browser remains unavailable, report the browser-visible check or inspection as blocked with the failure evidence and the completed retry. Continue only independently executable work that does not claim to verify the blocked UI behavior.
- A different browser-control capability may be used only when it is explicitly available in the current runtime and provides equivalent interactive, user-visible evidence. State the capability used in the result.

## Preserve role boundaries and evidence integrity

- Do not infer UI success from source inspection, an HTTP response, a screenshot supplied by another agent, or a Programmer's report.
- A Tester treats a reproducible mismatch as a failed test, preserves the evidence, and retains the existing Bug and independent-retest responsibilities. Missing or unusable browser access is blocked, not passed or inconclusive by default.
- A Programmer may use the browser to verify an implementation, but does not replace the Tester's independent UI evidence or retest.
- A Product Owner uses browser evidence to assess outcome, usability, and resulting product feedback; it does not become technical direction, a Done decision, or an approval gate.
- A Stakeholder uses browser evidence to state observations from its declared perspective and routes resulting feedback through the Product Owner. It does not create product or technical decisions.
