# Retest a fix

Read this workflow on `bug.fix-ready` or when explicitly performing an independent retest.

1. Inspect the linked change and original Bug evidence.
2. Re-run the original failing scenario in a suitable environment.
3. Run relevant regression and neighboring-behavior checks.
4. Append the retest result to the same Bug artifact and update its `updated` date without deleting earlier evidence.
5. Set `bug_state: resolved` only when the expected behavior passes and relevant regression checks show no new Bug.
6. If the retest fails or reveals another Bug, keep or return it to `open`, place it at the top of the Sprint Backlog, and signal `test.finding` again.

If a Sprint ends before a Bug is resolved, move the Bug artifact back to `product-backlog/items/` with its identity and evidence intact. Record the return in the Sprint Backlog index and let the Product Owner decide its Product Backlog order. Never leave an open Bug file in a completed Sprint Backlog.
