# Issue tracker: Local Markdown

Wayfinder maps live at `.scratch/<effort>/map.md`, with one child issue per file under `issues/NN-<slug>.md`. This repository uses the local fallback specified by wayfinder; no remote tracker was configured when this effort began.

## Wayfinding operations

- Each issue carries `Type:`, `Labels:`, `Status:`, `Assignee:`, `Parent:`, and `Blocked by:` lines.
- Status is `open`, `claimed`, or `resolved`. An open issue with no assignee is unclaimed.
- Parent points to the map. Blocking lists issue numbers in the same directory, or `none`.
- The frontier contains open, unassigned issues whose blockers are all resolved, ordered by number.
- Claim by saving `Status: claimed` and an assignee before starting work.
- Resolve by appending an `## Answer`, setting `Status: resolved`, and adding a named link with a one-line gist under the map's Decisions so far.
- Issue titles are the human-facing names. Reference them by linked title rather than bare number.

Research assets live in `research/<effort>/` and are linked from the resolving issue.
