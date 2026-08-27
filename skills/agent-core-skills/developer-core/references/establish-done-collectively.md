# Establish Done collectively

Read this workflow when producing Increment Documentation, assessing the Definition of Done together, responding to `product-assessment.recorded`, or returning unfinished work at Sprint end.

1. Integrate Product Code and collect each involved Developer's results.
2. Run the relevant automated, manual, regression, and feature checks.
3. Create the Increment Documentation required by the Definition of Done under `artefacts/increment-documentation/`.
4. Review the Definition of Done together and record each criterion with supporting evidence.
5. Signal `increment.documentation-ready` so the Product Owner can perform and record the required product assessment.
6. Address defects before Done. Under the Zero Bug Policy, never reclassify a known unresolved bug as a limitation merely to complete the Increment.
7. Treat Product Owner inspection feedback as a new or updated linked Product Backlog Item. Do not extend the completed PBI with a newly requested product change; repeat affected checks only when an existing Definition of Done criterion remains unsatisfied.
8. After the Product Owner assessment is recorded, let the Developers collectively determine whether every Definition of Done criterion is met.
9. Signal `increment.done` only when the complete check is positive. Keep Done PBI and resolved Bug artifacts in the Sprint Backlog.
10. Before Sprint completion, move every unfinished PBI, Bug, or other work artifact back to `product-backlog/items/`, preserve its identity and history, and let the Product Owner order it. Work that does not meet the Definition of Done is not part of the Increment.

The Product Owner assessment provides product feedback but is not approval or rejection. Release and demonstration decisions remain separate from Done.
