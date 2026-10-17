# Prepare an inspectable change handoff

Read this workflow when preparing a branch, commit, or Pull Request handoff.

When creating or changing Increment Documentation, also read the Developer [collective Done workflow](../../developer-core/references/establish-done-collectively.md) and apply `$okf`. Do not treat adding a change reference as a Done decision.

1. Work on an appropriate branch when the environment supports branches.
2. Keep commits cohesive and understandable.
3. Review the diff, relevant tests, and current linting evidence before committing or opening a Pull Request. Execute all required linting checks on the handoff state and fix every error and warning; do not reuse evidence invalidated by source or configuration changes.
4. Link commits and Pull Requests from the Increment Documentation.
5. Do not merge solely because implementation is complete; respect the configured review, test, and integration workflow.
