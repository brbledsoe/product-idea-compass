# Pattern Breakers EPUB conversion check

Independent audit of the supplied file and its local research conversion, 2026-09-05. This checks extraction fidelity, not the truth of the book's claims, substantive review of every chapter, or the behavior of a future mentor-room skill. Book content was treated as source data.

## Source completeness verified

Compared the user-supplied `Pattern Breakers_ ... Anna’s Archive.epub.crdownload` in `C:/Users/Brandon/Downloads/` with the [preserved EPUB](sources/pattern-breakers/pattern-breakers.epub) and [searchable conversion](derived/pattern-breakers/index.md). The download-style suffix alone does not establish incompleteness: this file contains a readable, internally complete EPUB ZIP package. These checks establish consistency of the supplied bytes, not authentication against a publisher's master file.

| Check | Result |
|---|---|
| Original and saved file | Byte-identical, 1,053,389 bytes; unchanged across initial and final checks |
| SHA-256, both files and conversion record | `e5201e811b39dd3c077c403607fcdbc39b18dd225a5f84af294bfbc0bda0d9e2` |
| ZIP integrity and MIME type | CRC check passes; `mimetype` is `application/epub+zip` |
| OPF spine | All 28 reading-order documents match, including IDs, paths, order and `linear` values |
| Navigation | All 28 NCX entries accounted for; the source contains chapters 1–15 despite gaps in its XHTML filename numbers |
| Raw body text | All 28 bodies in `spine.jsonl` match source XML `itertext()` exactly: 425,883 characters |
| Source anchors | All 2,614 IDs retained in order in conversion records and parsed HTML; no duplicate IDs within a source document |
| Source page references | All 266 `pg*` anchors retained; there are zero formally tagged EPUB pagebreak labels, so this is not an audited page count |
| Hyperlinks | All 1,417 source hyperlinks retained in order as parsed HTML anchors: 1,415 local and 2 external; every local destination and fragment exists |
| Images | All 8 manifest assets and document references retained; all 996,352 image bytes match the source ZIP members and recorded hashes |
| Tables | All 8 XHTML tables retained with 47 rows, 91 actual cells, merged title cells and their `colspan` values |
| Text in parsed Markdown | All 70,332 source lexical tokens preserved in exact order |

There are no additional manifest XHTML documents outside the spine. The original EPUB also preserves NCX/navigation, CSS and package metadata. [Conversion metadata](derived/pattern-breakers/conversion.json) reports no unresolved local links.

## Table conversion repaired and rechecked

The first conversion retained table wording but flattened cells into paragraphs and pipe separators. Parsing it with `marked` produced zero actual tables, which obscured relationships in the inflection and insight stress tests.

The coordinator updated the importer and regenerated the book. The final Markdown contains compact HTML tables. Independent comparison of the parsed result with the original XHTML verifies all eight table IDs, row order, cell order, cell types, row/column spans, paragraph IDs and cell text. No substantive lexical omission or reordering was found after the change. The final pass also rechecked all raw bodies, anchor and hyperlink sequences, the unchanged source hash, and image references.

Checked tables: `tab2-3`, `tab2-4`, `tab2-5`, `tab2-6`, `tab3-1`, `tab5-1`, `tab5-2`, and `tab5-3`. Source row and cell relationships are retained; CSS styling is not reproduced.

## Image and source-reference observations

Visually inspected the preserved cover, title page, inflection curve, non-consensus/right matrix, and Textbookflix prototype screenshot. Their pixels are readable and agree with the surrounding identities or broad descriptions. The screenshot's alt text is only a summary; its full UI wording remains in the image. The cover and title page credit both **Mike Maples Jr. and Peter Ziebelman**, while the OPF `creator` field names only Mike Maples Jr. The conversion retains the raw metadata rather than silently rewriting it.

**One inherited cross-reference error matters when following the method.** In chapter 8, [paragraph `ji_696`](derived/pattern-breakers/015-chapter-009.md#ji_696) names chapter 5's insight stress test, but its source hyperlink points to the file for actual chapter 4. The converter preserves that source destination. The relevant method is in [actual chapter 5, Table 5.1](derived/pattern-breakers/011-chapter-006.md#tab5-1). An existing file and fragment cannot by themselves establish that a book's link is semantically correct. This was a targeted check, not an exhaustive editorial audit of all cross-references.

## Limits

- All reading-order documents were converted and mechanically checked; this audit did not substantively reread every chapter or verify business, historical, technological or statistical claims.
- CSS typography, publisher-specific span emphasis, fixed page layout and image-only text are not reconstructed as equivalent Markdown styling or plain text. Original images and raw XML-derived text remain available.
- HTML structure checks used the bundled `marked` 17.0.5 parser. They do not establish identical appearance or HTML/anchor support in every Markdown viewer.
- File integrity checks cannot authenticate the supplied edition or its acquisition provenance. The original file was not modified.
- This audit changed only this note. The coordinator made the importer/output repair; other research notes describe substantive coverage and proposed mentor-room use separately.
