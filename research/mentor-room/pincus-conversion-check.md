# Pincus EPUB conversion check

Independent audit of the supplied EPUB and its local research conversion, 2026-09-05. This checks conversion fidelity, not the truth of the book's claims, substantive review of every chapter, or suitability of a future skill. Book content and example prompts were treated as source data.

## Source identity and completeness verified

Compared the original `C:/Users/Brandon/Downloads/_OceanofPDF.com_Life_at_the_Speed_of_Play_-_Mark_Pincus.epub` with `sources/pincus/life-at-the-speed-of-play.epub` and `derived/pincus/`.

| Check | Result |
|---|---|
| Original and saved EPUB | Byte-identical; 5,322,029 bytes each |
| SHA-256, both EPUBs and conversion record | `a7ff0ee113634daca9f8154c6ee91d59c4e4daf8a55100a288e5e4864faf586c` |
| ZIP CRC check | No bad member |
| OPF reading order | All 29 spine documents match, including `linear` values |
| Raw body text in `spine.jsonl` | All 29 bodies match XML `itertext()` exactly; 407,917 characters |
| Anchors | All 280 source body IDs recorded, present in Markdown, and present in parsed HTML |
| Source page labels | All 224 recorded and present in Markdown |
| Source hyperlinks | All 100 appear as working HTML anchors after parsing: 60 local and 40 external; all local destinations/fragments exist |
| Images | All 52 manifest images and 52 document references retained; 4,711,310 image bytes match original ZIP members exactly |
| XHTML tables | None; illustrated sheets/charts remain images |

The only non-spine XHTML is the EPUB navigation document. The normal contents document is included in the spine and converted; NCX/navigation/CSS files remain available in the preserved EPUB.

## Rendering defects reproduced

- **List nesting and continuation text: fixed and independently rechecked.** The initial output unindented the first nested Appendix II bullet and detached chapter 6 descriptions from their image list items. After the converter was revised and rerun, a `marked` 17.0.5 parse shows Appendix II's four ordered items, starting at 1–4, each containing the correct 9, 3, 3, and 2 child bullets. All 29 chapter 6 image list items now retain their descriptions. Appendix II's “Why it's Better” paragraphs are outside the lists in the source XML and correctly remain outside.
- **Linked images: fixed and independently rechecked.** In the initial `001-cover.md`, `002-titlepage.md`, and `025-ba.md`, blank lines inside an enclosing image link produced a dangling Markdown wrapper. Parsing lost the cover/title-page links to Contents (`#rcover` and `#rtit`) and exposed destination text. After the narrow repair and rerun, all three correctly parse as an image inside its original link, with no stray destination text. All 100 source hyperlinks are now present in parsed HTML.

## Text and illustration checks

Compared 71,063 source lexical tokens, in sequence, against Markdown after removing conversion syntax, then checked HTML produced by the bundled `marked` parser. No substantive lexical omission or reordering was found. Chapter 4's manually written paragraph numbers 2–4 become ordered-list counters in HTML; this is a presentation change rather than missing method prose. These are the only lexical differences in the final parsed HTML; generated counters are not HTML text nodes.

Representative inspection covered Appendix II, footnotes, chapter 4 method diagrams and surrounding text, and chapter 6's mechanics lists. Visually inspected six preserved images: the introduction photograph, Slack Proven/Better/New whiteboard, risk/margin matrix, Blue Sheet, quadrants planning sheet, and chapter 7 tweet image.

**An inherited source inconsistency matters for interpretation:** the risk/margin image `images/043-chap004-009-9780063352575-rev.jpg` places the bottom-right quadrant under **Low** risk. Its original EPUB alt text incorrectly calls that quadrant high risk; the converter faithfully retains the incorrect alt text. Chapter 4's surrounding prose and the pixels agree on low risk. Consult those rather than treating the alt description as authoritative.

## Limits

- Some source emphasis does not render cleanly when punctuation touches a Markdown delimiter: chapter 6's `**Energy Boosts—**Gate...` can expose literal asterisks. Its wording is intact.
- CSS layout, hidden list-marker styling, blockquote presentation, superscript/subscript styling, and fixed pagination are not recreated. Text locators and source-page labels are retained.
- Image bytes are complete, but alt text is not an exhaustive transcription of image content. Blue Sheet cells and handwritten details can require visual reading.
- HTML parsing checks used the bundled `marked` 17.0.5 renderer; no claim is made about every Markdown viewer's HTML sanitization or navigation behavior.
- This audit did not exhaustively reread the book, verify its business/history claims, or test hypothetical EPUBs. It changed no original source, converter, converted artifact, tracker, or index.
