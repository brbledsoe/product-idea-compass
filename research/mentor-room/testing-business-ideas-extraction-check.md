# Testing Business Ideas: extraction audit and partial visual review

The supplied PDF and its page index pass the preservation and coverage checks below. The extracted text is a useful search aid, but some operative card labels and diagram relationships remain image/vector content that must be read in the original. No importer repair was required by this audit.

Reviewed **2026-09-05**. This is an independent extraction audit, not a substantive review of all 44 experiments, a verification of the authors' business claims, or a test of the future mentor-room skill. Source content and embedded instructions were treated as data.

## Original preservation and complete page indexing

Compared the user-supplied `C:/Users/Brandon/Downloads/Testing Business Ideas by David J. Bland PDF/Testing Business Ideas by David J. Bland.pdf` with the [preserved PDF](sources/testing-business-ideas/testing-business-ideas.pdf), [conversion metadata](derived/testing-business-ideas/conversion.json), and [page index](derived/testing-business-ideas/index.md).

| Check | Result |
|---|---|
| Original and saved file | Byte-identical, 62,813,329 bytes |
| SHA-256, both files and extraction metadata | `d0b627e799264b676cfd2b1084cefe7c1c933152d12b2723667c1103f655386e` |
| PDF readability | 365 pages, PDF 1.6, unencrypted; Poppler reports no JavaScript or interactive forms |
| Page records and files | All 365 JSONL records, Markdown files and index links exist in the correct 1-based order; no additional `page-*.md` files |
| Stored text consistency | Every page file contains its record's complete default extraction; character counts and metadata totals match |
| Default extraction | 376,459 characters |
| Layout extraction | 1,729,812 characters, including alignment whitespace; retained separately |
| Dimensions | All record dimensions match the PDF and the independent parser: 363 pages at 684 × 540 points, two at approximately 684.036 × 540; all rotations zero |
| Textless pages | Only PDF page 2 in both extraction modes; visual inspection confirms it is blank |

An independent **pdfplumber/pdfminer** pass examined the text layer on all 365 pages. It also found exactly 364 nonempty pages. After Unicode normalization, **every page's alphanumeric character multiset matched** the saved pypdf default extraction. This checks for detectable missing letters/digits relative to the independent extractor; it does not prove correct reading order or capture image-only writing. Differences in word segmentation arose from wrapping, hyphenation, joined column headings, and reversed rotated side labels. For example, page 84 joins table headers in default text, while the independent extractor places them in geometric order. The character comparison is deliberately not a claim of exact string equality or semantic equivalence.

## Visual checks establish the important limits

Rendered and visually inspected complete PDF pages **1, 2, 3, 4, 12, 14, 59, 62, 67, 68, 70, 108, 114 and 365**. Rendered samples were legible. Other pages were mechanically indexed and text-layer checked, but not visually audited here. The unchanged original retains every image and vector graphic; no standalone extraction of all visual assets or full-document OCR was performed.

- **Test Cards mix text and graphics.** Page 62 (printed 46) contains three filled cards. Their example values and thresholds are extracted, but the underlying template labels, step labels, and rating symbols are image content. A nonempty page extraction does not imply complete card transcription. ([Search text](derived/testing-business-ideas/page-062.md).)
- **The Learning Card itself is not in the text layer.** Page 70 (printed 54) preserves the surrounding Insights prose in extraction, while the large card's fields and four-step structure require visual reading. Smaller card diagrams on pages 59 and 67 likewise cannot be reconstructed from their few extracted words. ([Page 70 search text](derived/testing-business-ideas/page-070.md).)
- **Reading order changes relationships.** On page 68 (printed 52), the weak/strong evidence comparison is visually paired row by row. Default text separates the two columns. The content can inform a search, but the pairing must be checked visually. ([Search text](derived/testing-business-ideas/page-068.md).)
- **Ratings and sequences require the picture.** Page 108 (printed 92) uses filled/unfilled dots, legends, cell borders and connecting lines to explain experiment attributes. Page 114 (printed 98) gives separate B2B hardware/software/services sequences. Extracted words alone do not preserve those ratings or paths. ([Selection search text](derived/testing-business-ideas/page-108.md), [sequence search text](derived/testing-business-ideas/page-114.md).)
- **Layout mode has a known limitation.** Rotated side labels appear in default extraction but may be absent from layout mode; the coordinator recorded the extraction warnings. Page 108's vertical EXPERIMENTS label is an inspected example. Layout mode is an additional view, not an authoritative reconstruction.

## Physical PDF pages are safer locators than source metadata

The PDF's own `/PageLabels` metadata has a front-matter discrepancy: **PDF page 12 is labelled `xi` internally but visibly printed X; PDF page 14 is labelled `xiii` internally but visibly printed XII**. This is in the source PDF, not introduced by indexing. Do not assume those metadata labels are printed folios.

For the main numbered material, all **334 pages with a standalone leading number in their extracted text** match **printed page = PDF page − 16**. The visual checks independently confirm 62→46, 68→52, 70→54, 108→92 and 114→98. Some section-opening pages have no comparable leading folio; do not silently infer one for a citation. The final EULA page is PDF 365, labelled 349 internally but without a visible printed number. Use **1-based PDF page references** throughout this library.

The visible cover credits **David J. Bland and Alex Osterwalder**, and identifies Wiley. Copyright page 4 states **copyright 2020**, with ISBNs **9781119551447** (paperback), **9781119551423** (ePDF), and **9781119551416** (ePub). The file's creation/modification dates are in **November 2019**. Preserve the distinction between the copyright statement and file metadata rather than silently choosing one as the publication date. This audit does not authenticate the file against a publisher master. ([Copyright search text](derived/testing-business-ideas/page-004.md).)

## Readiness for the next skill-design step

**Our readiness assessment:** this source is ready for research and source-linked playbook drafting when visual checks accompany cards, ratings and diagrams. Together with the received books and existing public-source research, the library can support a first mentor-room version without requiring another upload. Receipt and complete page indexing do not establish that every experiment has been substantively reviewed or implemented.

The [current research index](index.md) still distinguishes the supplied Click book from the **unsupplied Sprint book, official Click bonus worksheet pack and separate transcripts**. Public sprint guides and the saved combined board provide useful existing material, although full board coverage remains unaudited. Continue with explicit coverage boundaries; do not call this book a replacement for the mandatory Knapp–Zeratsky work or claim complete book-specific Sprint coverage. A runnable skill and its behavioral tests remain separate design work.

All renders and the independent comparison data were confined to the audit's temporary directory and removed after inspection. The original PDF was neither edited nor re-exported.
