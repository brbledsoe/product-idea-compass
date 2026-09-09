# First app improvement to test: explicit cleaning acceptance

2026-09-09 · A10 · Proposed X04 · Scope revision 3 · No trial run

**On hold as of session 9.** Brandon reports the cleaner abandoned the existing completion features because they were too difficult and annoying, and the test-sheet assignment was unclear. There is no task to run this test or fill in its rows now. First understand the existing completion friction; see [the current session](../sessions/2026-09-09-09-completion-abandonment.md). The original proposal below is retained as history, not the current handoff.

## What we know

Brandon says the existing family app does not really have explicit acceptance/decline for a cleaning. His wording was qualified (“not necessarily”); the implementation has not been inspected. The app already shows/notifies upcoming work and supports completion checklists/photo evidence. Mom still seeks verbal confirmation. This supplies a plausible explanation to test, not proof of causation.

| Stage | Current account | Proposed change to examine |
| --- | --- | --- |
| Job appears | Cleaner sees upcoming work | Keep the existing notification and job details |
| Commitment | Family seeks confirmation outside the app | Cleaner proactively accepts the specified day/window or reports inability by an agreed cutoff |
| No answer or decline | Mom currently owns the problem; no backup owner | Keep the job visibly unconfirmed and use the existing human response; do not imply coverage |
| Completion and readiness | Checklist/photos followed by family walkthrough | Retain this workflow during an acceptance-only test |

Competitor reference: Turno documents explicit acceptance/rejection and configured backup offers. This makes acceptance an existing market feature; any local benefit does not by itself establish commercial differentiation. See E45 and its [official workflow](https://help.turno.com/en/articles/8576288-as-a-host-what-do-i-do-after-accepting-a-bid), reviewed 2026-09-09. No comparative product-use study has occurred.

## Hypothesis H22

If the primary cleaner proactively confirms a specific cleaning window and Mom can see that confirmation, Mom needs fewer messages/calls solely to establish whether the cleaner will attend.

This is narrower than H18/X03: it does not require or demonstrate backup fulfillment, an owner being fully off duty, arrival, cleaning quality or actual completion. X03 remains in the backlog because no backup owner is agreed.

## Proposed two-cleaning test

Use the Bland–Osterwalder [Test Card structure](../../../research/mentor-room/testing-business-ideas-process.md), adapted to a small manual workflow observation. No completed sprint or field study is claimed.

1. Brandon, Mom and the cleaner agree on a simple response convention, practical response deadline and where Mom sees the answer. Use their current messaging channel initially. A manually sent job notice is allowed but its sender's effort must be counted; do not hide new coordination work.
2. For each of the next two eligible ordinary jobs, the cleaner responds to the notice by the agreed cutoff: “Accepted: [cleaning day and window]” or “I cannot take this job.” Missing information stays unconfirmed. A changed booking/window needs a fresh confirmation.
3. Record response time, confirmation-chasing calls/messages by Mom before and after acceptance, and the time spent by everyone else requesting, recording or relaying the answer. Keep normal walkthroughs and responses to missed/uncovered work.

Suggested notice, to adapt with participants before use:

> Cleaning needed: [day], between [start] and [finish]. Please confirm by [agreed cutoff] whether you can take this job. Reply with the day/window you accept, or tell us you cannot take it.

### Record actual observations

| Job | Day/window and response cutoff | Explicit response/time | Mom's confirmation-chasing calls/messages | Other coordination/reporting minutes | What still needed attention? |
| --- | --- | --- | --- | --- | --- |
| 1 | Pending | Not run | Not measured | Not measured | Not observed |
| 2 | Pending | Not run | Not measured | Not measured | Not observed |

If readily available, record comparable recent confirmation messages/time as a baseline, marking recalled amounts as estimates. Without that baseline, do not claim a quantified reduction. Notice preparation, setup, reminders and forwarding count as effort even if someone besides Mom performs them.

### Proposed interpretation rules, to agree before running

- **Encouraging initial signal:** two eligible accepted jobs, both confirmed by their cutoffs without Mom chasing, and no further attendance-confirmation chasing afterward. Examine total effort before calling this worthwhile.
- **Against the proposed mechanism:** clear timely acceptance arrives but Mom still needs the same confirmation contacts, or the response convention itself requires repeated chasing. Find the reason rather than assuming a button fixes it.
- **Unclear/mixed:** fewer than two accepted jobs, unavailable records, changed circumstances, or effort merely transferred without a usable comparison. A prompt decline is useful information, but it does not test reassurance after acceptance or prove coverage.

These are provisional local learning criteria, not published thresholds or reliable population estimates. Dates, participant agreement and cutoffs are not yet set. No provider has been contacted by the facilitator. No software implementation is required to draft or observe this manual process; it does not establish the eventual app's usability or automation reliability.

## Next action and decision

Brandon's proposed task: agree the response convention and try it on two cleaning jobs, then bring the two observation rows back. If a trial is not practical, report that constraint so a recorded-workflow comparison can be used instead.

Facilitator's next task after actual results: assess whether explicit commitment addresses confirmation uncertainty, whether the effort is acceptable, and whether a small acceptance/decline feature is worth prototyping. If the problem persists after acceptance, distinguish unreliable attendance, stale status and insufficient trust before adding more reminders. Independent host demand, competitive advantage and business economics remain untested.
