# Workspace bootstrap evaluation

- **Target:** `c2b14406aa0e782562a426e536d5a1937c6bef7c`
- **Candidate:** working tree
- **Runtime/model:** local Python 3 bootstrap execution
- **Fixture:** fresh temporary directory under `/private/tmp`
- **Evaluator:** Codex
- **Run count:** 1

| Case | Result | Evidence |
|---|---|---|
| Fresh workspace bootstrap | passed | `bootstrap.py 'Workspace Test' --parent <temporary-directory> --no-git` created sibling `agile-agentic-framework/` and `product-development-workspace-test/` directories. |
| Framework identity pin | passed | The generated `.aafe/aafe.yaml` recorded the public repository URL, sibling path `../agile-agentic-framework`, and the cloned checkout's exact `HEAD` commit `c2b14406aa0e782562a426e536d5a1937c6bef7c`. |
| Product write boundary | passed | Generated product `AGENTS.md` requires product-role agents to start in the product directory, restrict their write scope there, and treat the sibling framework checkout as read-only. |

## Limitations

This deterministic behavioral run verifies generated topology and contracts. It does not prove a particular runtime can enforce filesystem permissions; runtimes must apply the declared product-directory write restriction.
