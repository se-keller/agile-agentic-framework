# Resolve a Tester finding

Read this workflow on `test.finding` or when pulling an open Sprint Bug.

1. Pull an open Sprint bug before any non-bug Sprint Backlog work.
2. Reproduce the reported behavior when possible and preserve the Tester's original result.
3. Distinguish a Product Code defect from test-code defects, environment problems, and unclear product expectations.
4. Fix Product Code defects and add a regression test that fails before the fix and passes afterward when practical.
5. Coordinate acceptance-test automation changes with the Tester.
6. Ask the Product Owner through `developer.question` when resolving the finding requires a product decision.
7. Signal the fix as ready with a concise explanation and reproducible test results; let the Tester perform the independent retest and update the Bug artifact.
