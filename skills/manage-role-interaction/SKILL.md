---
name: manage-role-interaction
description: Select and enforce how the runtime host, human, and configured role agents communicate during a product-development session. Use at session entry, when the human changes interaction mode, when a role needs human dialogue, or when routing a reply back to an active role.
---

# Manage Role Interaction

Apply this process skill as the runtime host. It governs conversation transport only; it never grants the host a Scrum accountability or expands a role's permissions.

## Select a supported mode

At the first product interaction of each runtime session, inspect the runtime's actual conversation capabilities. If the human has not already selected a mode for this session, offer only the supported modes and let the human choose:

- `host`: Role agents provide attributable results to the host. The host explains or synthesizes them to the human and routes relevant human replies back to the same role instance. The host must not invent, replace, or decide role-owned content.
- `transparent-proxy`: The host presents the active role's user-facing message with its display name and without materially rewriting it. The next human reply is delivered unchanged to that same role instance. The host may separately report routing, permission, safety, or runtime failures.
- `direct-handoff`: The runtime transfers the visible conversation to the active role agent while preserving its identity and relevant conversation state. Offer this mode only when the runtime can perform and later release a real same-conversation handoff. A separate task, a role label, or host impersonation does not count as a direct handoff.

Keep the selection as runtime session state rather than product knowledge. The human may change it at any time. Do not silently downgrade an unavailable selected mode; explain the missing capability and ask the human to choose from the remaining modes.

## Preserve one conversational owner

1. Keep at most one active user-facing role at a time, identified by its preserved runtime agent ID.
2. Queue questions from background agents instead of allowing simultaneous competing prompts.
3. Route a human reply addressed to the active role back to that same instance. Do not replace it while it remains resumable.
4. Let the active role release the conversation when its current dialogue is complete or a lifecycle handoff requires another role.
5. In `direct-handoff`, let the runtime return control to the host before activating the next conversational owner. In the other modes, keep the host as transport throughout.
6. Attribute role-authored content and host-authored transport or synthesis accurately. Never present a host-created answer or a role label as output from a separately executed role.

Transmit only a role's intended user-facing payload. Never expose private reasoning, tool traces, internal control messages, credentials, or other non-user-facing runtime data merely because proxy mode is selected.

Background work may continue when safe, but only the conversational owner may ask the human a blocking question. Urgent human input may always address the host and change or end the current mode.

## Fail closed

- If an active role cannot be started or resumed, stop the affected dialogue and lifecycle transition. Do not simulate the role in the host.
- If direct conversation control is lost, preserve the last confirmed role ID and pending question. Ask the human before switching to another supported mode or replacement role.
- Interaction mode changes transport, not authorization, artifact ownership, lifecycle boundaries, or independence requirements.
