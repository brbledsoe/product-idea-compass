# Maintaining the mentor-room feedback archive

## Retrieve the smallest useful context

Start at README.md. Match an explicit feedback/iteration ID first, then task ID and test context; use branch/version only as supporting context. Read the matching iteration and any linked points relevant to the current request. Search `iterations/` with `rg` for IDs, topics, source phrases, or task IDs when the index is insufficient.

Reuse the current iteration for follow-up feedback about the same tested version/run. Start a new ITER-NNN record when a revised skill is tested again or a distinct evaluation run begins. Link predecessor and related iterations. A branch switch alone changes neither historical IDs nor what was tested. If the target cannot be inferred reliably, ask one concise question; never silently attach feedback to a different test.

## Record the test before interpreting its feedback

Each iteration identifies its date, evaluation aim, initial user request/test case, stage reached, actual skill/core version when known, repository/worktree, branch, and full commit. Record relevant uncommitted changes separately; a commit does not identify untracked artifacts. Numbering begins with the first iteration recorded in this archive, not an assertion about all prior development.

Record the source task's exact title, stable task ID, and host. Link an existing conversation/message URL when available, otherwise a verified local transcript plus a short phrase or exact locator. Preserve enough of the initial request and feedback in the iteration to understand them if links later stop working. Use task tools to retrieve a known task without depending on its title remaining unchanged. Never invent links or publish a conversation merely to obtain a reference.

Local working-tree files can change after checkout. For each important implementation reference, retain the repository-relative path, full commit and applicable scope in addition to the convenient absolute file link. For evidence not committed or stored durably elsewhere, save only the necessary excerpt or a small labeled snapshot beside the iteration when a later comparison requires it. Do not copy entire transcripts by default. Broken sources remain labeled unavailable; retain their original locator and recorded context.

## Capture one identifiable point at a time

Assign globally unique FB-NNNN IDs by inspecting existing iteration records, not just the index. Never renumber an ID after moving, combining, deferring, or addressing it. A comment with distinct actionable points may become multiple linked entries; related repetition can be appended as another dated observation under the existing point.

Each point records date, iteration, scope (skill behavior, feedback process, or another explicit category), a short topic, Brandon's feedback, source locator, observed context, desired change if stated, current status, related IDs, and dated follow-up history. Separate user reports and direct observations from assistant interpretation or proposed solutions. Mark unknowns explicitly. Product-idea evidence stays in its idea case; link it only when needed to explain a skill problem.

Distinguish the iteration where behavior was observed from the branch/commit where a fix was made and the iteration where it was retested. A fix on another branch never rewrites the original test context. Feedback capture alone does not authorize unrelated implementation; follow the current request and any existing authorization.

## Preserve decisions and outcomes

Keep original feedback intact. Append dated clarification, decisions, implementation references and retest outcomes, then refresh the current status. Use Recorded, Planned, Implemented, Verified, or Deferred. Implemented identifies the concrete change; Verified links a relevant check/retest and states exactly what it established. A successful file/link check is not evidence that a skill-behavior problem has been solved. Keep user review pending when it is pending.

For implementation, link the commit/PR/file and identify the scope of the change. For retesting, link the new iteration and explain the observed outcome. For deferral or a superseding point, retain the reason and cross-reference. Do not mark an entire iteration resolved just because its folder or template exists.

## Update safely across branches and tasks

Use one canonical archive, not per-branch copies. Serialize mutations when multiple tasks might write: acquire a short-lived exclusive `.write-lock` file in this folder, re-read affected files and allocate IDs while holding it, and release it in a finally block. Record the owning task/time in the lock. If it is occupied, wait briefly or report the busy writer; do not delete another writer's lock without establishing that it is stale.

Write the authoritative iteration first using a temporary sibling and replacement, then update README indexes. If an interrupted update leaves the index behind, rebuild it from the iteration records. Preserve intervening entries instead of overwriting a stale copy. A temporary write failure does not justify inventing a new archive elsewhere.

Before finishing, verify unique IDs, matching index entries/statuses, valid internal anchors, and local file links. Label external sources as supplied or inspected; do not claim remote links were checked without checking. Confirm the saved feedback IDs and location briefly. A natural-language comment is sufficient; Brandon does not need to use a special phrase or know this structure.
