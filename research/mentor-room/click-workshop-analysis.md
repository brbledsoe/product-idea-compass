# Click workshop sources: official guide, separate remote agenda

- The PDF is a print snapshot of Knapp and Zeratsky's Character Foundation Sprint guide, reinforcing the [existing baseline](knapp-zeratsky-baseline.md), rather than establishing a separate workshop method.
- The unattributed CSV supplies practical timeboxes. Both days contain 250 activity minutes and 80 break minutes; day two's final wrap-up timestamp is inconsistent.
- Neither artifact establishes access to the official Click bonus worksheet pack. Preserve the supplied originals and keep any agenda corrections explicitly derived.

Reviewed **2026-09-05**. Sources: [PDF snapshot](sources/click/two-day-workshop-website-snapshot.pdf), all **13 pages visually read** after rendering; [CSV](sources/click/foundation-sprint-remote-agenda-v1.csv), all **47 physical rows** parsed and byte-inspected. PDF page numbers below are printed page numbers; CSV row numbers include headers and the blank separator. No contact, subscription, purchase, or signup action occurred.

## Provenance is clear for the PDF, unresolved for the CSV

PDF p. 1 names **Jake Knapp and John Zeratsky**, founders and general partners at Character Capital. The footer identifies [Character's Foundation Sprint guide](https://www.character.vc/guide/foundation-sprint). Page 13 shows Character Capital LLC's 2026 copyright and contact/subscription controls. Page 2 separately recommends the Miro template, *Click*, and the guide; it does not identify this printout as a bonus pack.

The print header reads `9/5/26, 5:11 PM`. PDF metadata records creation/modification at `2026-09-05 17:12:14 +02:00`, producer Microsoft Print To PDF, and an empty Author field. These support a capture date, **not an original publication date**. This review identifies the supplied snapshot; it does not independently authenticate its download history. All 13 pages have zero extractable text, so text extraction alone would miss its contents.

The CSV contains no author, URL, publication date, or attribution in its rows. Its filename suggests a remote agenda, but resemblance to the guide or another supplied template does not establish authorship. Keep its provenance separate from both Character and the [Mural template investigation](mural-template-access.md), which identifies Jonathan Vardy's template without establishing a connection to this CSV.

## The PDF confirms the baseline and makes facilitation more explicit

| Source pages | Verified method and reusable detail |
|---|---|
| 1-3 | Two-day workshop producing a testable founding hypothesis; up to five people including the real Decider; reserve about six hours per day; use physical or virtual whiteboards and voting supplies. |
| 3-5 | Identify a plainly described customer, consequential problem, capability/insight/motivation, and competing products, workarounds, or inaction. Note-and-Vote means independent silent writing, silent review/voting, then brief debate and the Decider's choice, regardless of votes. |
| 5-7 | Assess classic and custom differentiators; the Decider picks two. Iterate a 2x2 customer-perception comparison honestly, then write two or three practical principles. Combine differentiation and principles into a Mini Manifesto. |
| 8 | Generate alternatives and a one-page explanation/sketch for each. The Decider selects at most seven and assigns letters/colors for consistent comparison. |
| 9-11 | Compare options using four classic lenses plus custom charts, plot one axis at a time, adjust criteria when useful, review patterns and contradictions, and choose a primary approach plus backup. |
| 11-13 | Connect customer, problem, approach, competitors, and differentiators in the hypothesis. Convert predictions into scorecard questions and test prototypes through repeated Design Sprints, revising the hypothesis from customer reactions. |

The four chart defaults are visible on PDF p. 9: customer = problem fit versus ease of use; pragmatic = build speed versus build cost; growth = potential customer count versus ease of adoption; money = potential customer count versus long-term value. They are starting points, not immutable scoring rules (pp. 9-10). Page 10 suggests additional criteria and optionally reusing day one's differentiation chart.

## The agenda changes allocation and omits some mechanics

These are comparisons to the supplied PDF, not claims about the CSV author's intent:

- **Day-one setup and basics:** CSV rows 2-3 add 30 minutes of arrival/introduction. Rows 8-10 split advantages into three ten-minute activities, versus about 20 minutes together in PDF p. 4. Competitors get 15 minutes (row 11), versus about 20 in the guide.
- **Differentiation:** CSV row 17 describes impact/feasibility voting; PDF p. 6 describes relative competitive positioning. Row 18 does not specify the guide's two-differentiator limit or Decider authority. Row 21 allows 45 minutes for plotting versus about 30 in PDF p. 6. Rows 22-24 split values, principles, and manifesto into 20/20/5 minutes; PDF p. 7 gives about 45 minutes to practical principles, then a separate manifesto without a stated duration.
- **Approaches and lenses:** Rows 30-31 split the guide's roughly 60-minute alternatives exercise into 30-minute ideation and summaries. Row 33 adds heatmap review; rows 35 and 40 separately schedule criteria selection/review. No row explicitly preserves the at-most-seven shortlist or letter/color assignment from PDF p. 8. Row 44 combines review and Decider selection into 30 minutes, versus approximately 10 plus five minutes on PDF pp. 10-11.
- **Coverage boundary:** Row 46 budgets 15 minutes for the hypothesis. There is no explicit scorecard or subsequent experiment-planning activity anywhere in the CSV. Those remain necessary follow-through in PDF pp. 11-13. The sparse agenda also does not teach the guide's silence and voting mechanics; absence from the CSV does not prove the facilitator omitted them.

## Schedule and encoding audit

| Derived schedule | Day 1 | Day 2 |
|---|---:|---:|
| Physical rows | 2-25 | 28-47 |
| Timed activity sequence | 10:00-15:30 | 10:00-15:30 through row 46 |
| Activity time, including arrival/introduction | 250 min | 250 min |
| Breaks | 10 + 60 + 10 = 80 min | 10 + 60 + 10 = 80 min |
| Total listed durations | 330 min / 5.5 h | 330 min / 5.5 h |

Every timed row's duration matches its own start/end times. Adjacent times connect except **row 47**, whose zero-minute wrap-up is at **14:45**, after row 46 ends **15:30**. Setting both row-47 times to 15:30 is an inferred repair; it does not allocate actual wrap-up time.

Import considerations:

- Headers repeat at rows **1 and 27**, with `Comments` changing to `Comment`; row **26** is empty. All 47 records have seven fields. Numbering restarts for day two; day-two subnumbers skip 3.1 and 3.3.
- Day-two **3.4** appears at rows **36 and 38**: 15 minutes before lunch plus 45 afterward. Preserve both segments; deleting a supposed duplicate loses scheduled work.
- Rows **4, 14, 20, 29, 34, 39, 45** are zero-duration section markers. Wrap-up rows **25 and 47** also have zero duration, written `0` rather than `0:00`.
- The 4,280-byte file has 47 CRLF-terminated lines and no UTF-8 BOM. Its only non-ASCII byte is **`0x92` at zero-based byte offset 2046**, in row **22**. Windows-1252 decodes it as the right apostrophe in `team's`; strict UTF-8 decoding fails. A replacement glyph in tool output therefore does **not** establish corrupted source content. The bytes are consistent with Windows-1252; they do not prove the exporter used that encoding name.
- Row **33** contains a real trailing tab (`0x09`) inside the activity field.

## Proposed mentor-room use

Use the PDF for methodological requirements and the CSV for optional, resumable timeboxes. Preserve independent contributions and the user's Decider role; require explicit outputs for missing shortlist, voting, scorecard, and experiment steps. Treat criteria, chart positions, and mentor opinions as assumptions until supported by evidence.

A separate [normalized JSON agenda](derived/click/foundation-sprint-remote-agenda-normalized.json) now provides UTF-8 research data with day/source-row identifiers, 44 unique row keys, preserved original IDs and split activities/section markers, a trimmed tab, and an explicitly inferred wrap-up correction retaining the original times. It is derived data, not a corrected source document or new evidence of authorship. The original CSV remains unchanged.
