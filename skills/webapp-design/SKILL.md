---
name: webapp-design
description: Design or review accessible, modern, platform-neutral web application interfaces. Use for user-facing layout, navigation, visual hierarchy, theming, components, or interaction patterns; do not use to prescribe a product's technical implementation.
---

# WebApp Design

Create an interface that is clear, efficient, accessible, and recognizably suited to the product. Preserve established product identity and component conventions. When these are absent, make restrained, coherent choices rather than copying the visual language of a platform or design system.

This is a Scrum Team skill. Developers use it to make and review implementation decisions. Product Owners use it to clarify user needs, information priorities, and observable design expectations; they do not prescribe implementation, libraries, markup, or other technical solutions.

## Accessibility is the baseline

Target [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/). It is technology-neutral and applies to web applications on desktop and mobile.

- Use native semantic controls and structure where they express the intended interaction; add ARIA only where native semantics are insufficient.
- Make every function keyboard-operable. Keep focus visible, logically ordered, and unobscured. Do not convey meaning through colour, position, or an icon alone.
- Give controls clear visible labels where space permits. Icon-only controls need an accessible name and a tooltip when the meaning is not immediately obvious.
- Design text, non-text controls, errors, status changes, and empty states to be perceivable and understandable. Preserve readable contrast, text resizing, and reflow.
- Meet the WCAG 2.2 AA minimum target size of 24 by 24 CSS pixels. Prefer approximately 44 by 44 CSS pixels for important touch targets when the task and information density allow it.
- Respect reduced-motion preferences. Motion may support understanding but must not be the only way to understand or operate an interface.

## Make the layout fit the task

- Work mobile-first. Adapt content density, columns, and navigation to available space and the user task; do not merely scale a desktop arrangement down.
- Derive navigation from information architecture. Keep a small set of high-value destinations visible; place secondary or infrequent destinations in an overflow menu. Do not hide core functions behind a menu.
- Use tabs for switching between related peer views within a context, not as a substitute for actions or primary navigation.
- Make the primary action of a view easy to identify and name it for the outcome it produces. A floating action button is appropriate only when adding or creating is the dominant action in that context.
- Use a clear visual hierarchy, deliberate whitespace, and a limited number of competing actions. Design useful loading, empty, success, and error states rather than treating them as afterthoughts.

## Make a coherent visual system

- Use reusable tokens for colour roles, typography, spacing, shape, elevation, and interaction states. Avoid isolated literal values that make themes and brand changes inconsistent.
- Support light and dark appearance intentionally; default to the user's system preference. Offer an explicit appearance setting when it suits the product or an existing preferences model.
- Keep component states and feedback consistent: default, hover, focus, active, disabled, selected, loading, success, and error states must remain distinguishable without relying only on colour.
- Use Material 3, Fluent 2, and Apple Human Interface Guidelines as sources of tested patterns, not as templates to copy. Choose a pattern because it fits the product's information architecture and users; do not combine conflicting conventions without a clear reason.

## Collaborate and review

- Product Owners express users, goals, priorities, content, constraints, and observable acceptance expectations. Developers decide how to implement the design and raise trade-offs or ambiguities early.
- Before calling a user-facing design change complete, review the relevant small and large viewports, keyboard flow and focus, light and dark appearance, and non-happy-path states.
- When a trade-off prevents the baseline, make it explicit and seek a product decision rather than silently reducing accessibility or discoverability.

## References

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the normative accessibility baseline.
- [Material 3](https://m3.material.io/), [Fluent 2](https://fluent2.microsoft.design/), and [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) are supplementary pattern references.
