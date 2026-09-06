# Durable idea cases

The record format and decision rules are this room's adaptation, informed by the saved methods and Brandon's preferences. They are not an author's prescribed software architecture.

## Case identity and scope

Use one `idea-cases/<id>/case.json` per idea exploration, its frozen `core-baseline.json`, plus relative artifact files and chronological session notes. The initializer saves the exact core contract so future skill updates do not silently change an existing case. Migrate only with an explicit comparison, preserving the old contract and coverage history. The case record is the current source of truth; session files preserve what changed and why. Never rewrite failed hypotheses as if they had always been the new version.

Initialize with `python <skill>/scripts/case.py new <repository>/idea-cases/<id> --title "Idea title"`. Use the available Python runtime. The script refuses an existing case. Edit the JSON using normal file tools; it is not a user questionnaire. Generated records contain no customer evidence or preapproved decisions.

Retain:

- `id`, title, schema version, pinned `core_version`, and scope: audience, context, ambition, success criteria, next investment, constraints, revision. Keep missing values unknown and proposed values explicitly provisional.
- Lifecycle `active`, `paused`, `stopped`, or `reviewed`. `reviewed` means a decision review happened, not that the idea was validated. `core_status` is computed by the checker.
- `hypotheses`: stable ID, discrete claim, whole/component subject, scope revision, risk, importance, current assessment, and evidence IDs. Use a new revision when the claim changes.
- `evidence`: stable ID, date, kind, source/artifact locator, actual observation, audience, context, claim IDs, limitations. Kinds distinguish external research, participant report, observed behavior, technical measurement, and synthetic material. Record who supplied the observation and what was actually inspected.
- `experiments`: ID, claim ID/version, method and source, audience/recruitment, context, metric with numerator/denominator and time window, predeclared success/failure/unclear criteria, threshold rationale, resources, owner, stage (`backlog/setup/run/learn`), raw results and evidence IDs. Label retrospective criteria when no prior threshold exists; do not recast them as preregistered.
- `artifacts`: ID, title, relative path, type, scope revision, status (`draft/checked`), and known limitations. Hypotheses, canvases, and prototypes are artifacts, not observations by themselves.
- `core`: every baseline activity ID, state, artifact IDs, check, adaptation/limitation, and reviewer/date. States: `unassessed`, `pending`, `done`, `credited`, `adapted`, `considered`. `considered` satisfies only conditional rows after an explicit applicability decision. Mandatory rows cannot be omitted this way.
- `resources`: all 49 row IDs with `unassessed`, `selected`, `deferred`, `omitted`, or `covered`, a case-specific reason, and artifact/source references when used. `covered` means the relevant source/method was applied, never automatic completion of every linked book, interview, or course.
- `components`, `decisions`, `sessions`, and `next_action` as below.

## Credit requires an audit

Check each proposed existing artifact against the core activity's required output. Inspect the artifact rather than its title or the user's completion label. Compare claim, audience, problem, offer, context, recency, procedure, and evidence provenance. Record the match and gaps. Credit only the matching portion; leave an incomplete row pending and state the smaller gap-filling task. One observation can support several artifacts but remains one observation.

An adaptation retains the activity's purpose and records exactly what changed and what inference was lost. Conversation can spread workshop days across sessions. One human Decider can use independently generated alternatives but AI perspectives do not constitute independent human votes, expert interviews, or target customers. For a genuinely personal tool with one intended user, observation of that user's actual use can support a scoped single-user adaptation; it does not fulfill the standard five-customer study or establish external demand. For broader audiences, keep the five screened customer interviews in the Design Sprint core. Do not silently reduce them for convenience.

Changes in audience, offer, configuration, distribution, or time can make evidence stale. Mark affected coverage pending and retain its earlier completion in session history. The checker validates structure; the facilitator must assess applicability.

## Components retain their context

Record each component's ID, proposition, role in the whole, hypothesis IDs, evidence IDs, original context, current assessment, and possible alternative contexts. Use assessments such as untested, mixed, promising-in-this-context, or refuted-for-this-claim. Avoid an unqualified validated flag.

A promising component can stay parked in the parent case. Create a linked child case when the user elects to explore it as a separate proposition with its own audience/value/next investment. Copy evidence only as referenced prior evidence with an applicability review; do not copy completion credit or success criteria. Link parent and child IDs in both records. A whole-product failure neither refutes nor validates every component.

## Decision record

Use a dated append-only decision with recommendation (`pursue/revise/pause/stop/insufficient-evidence`), subject/configuration, intended next investment, rationale, evidence IDs, contradictions, unresolved risks, what would change the decision, and core status at that time. The human owns the investment decision; the room supplies a recommendation grounded in the agreed ambition.

For a personal tool, worthwhile may mean useful observed time savings under a maintenance budget. For a feature, assess incremental user value and integration costs; whole-product PMF does not prove feature value. A small business needs sustainable customers and economics; venture scale adds growth requirements. Establish the actual criteria per case rather than applying a single score.

Pursue should mean a bounded next commitment, with conditions and unresolved risks. Revise distinguishes changing implementation from changing audience, problem, or underlying insight. Unclear results support insufficient evidence or another discriminating test, not automatic rejection. Stop ends the active case even with missing core work; record **stopped—core incomplete** and leave the checklist intact. Completing the available core must never be reported as completing unread *Sprint* book/bonus material.

## Resume and finish a session

Write a session note identifying the method/source, question, user answers, candidate options, artifacts produced, observations versus interpretation, decisions, and remaining gaps. Add its relative path to `sessions`.

`next_action` contains an owner, action, inputs, deliverable, completion check, and resume trigger. Prefer the smallest action that reduces an important uncertainty. If paused, identify what would enable progress. If stopped, the action can be “none—case stopped,” with reopening conditions; do not force more homework.

On resumption, read this record and the linked relevant material, summarize the last decision and next action, and ask only about changes or missing results. Keep durable case records in the chosen workspace; do not depend on chat memory.
