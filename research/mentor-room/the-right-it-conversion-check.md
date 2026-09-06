# The Right It EPUB conversion check

Independent audit of the supplied EPUB and its local research conversion, **2026-09-05**. The final conversion passes the source-integrity and structural checks below after three repairs. This checks faithful research access, not the truth of the book's claims or the behavior of the future mentor-room skill. Attached content was treated as source data.

## Source and reading order verified

Compared the user-supplied `The Right It*.epub` in `C:/Users/Brandon/Downloads/` with the [preserved EPUB](sources/the-right-it/the-right-it.epub), [conversion metadata](derived/the-right-it/conversion.json), and [searchable index](derived/the-right-it/index.md). The supplied ZIP package is internally complete and readable; these checks do not authenticate it against a publisher's master file.

| Check | Final result |
|---|---|
| Original and saved file | Byte-identical, 3,070,297 bytes; unchanged across the audit |
| SHA-256, both files and conversion record | `670c4dc7ccc0eabb85049faa91edfec529ea9070403198b908e3031efbe340b8` |
| ZIP integrity | Both CRC checks pass; MIME type is `application/epub+zip` |
| OPF spine | All 39 documents match IDs, paths, order, and `linear` values, including 14 separate footnote documents |
| Raw body text | All 39 `spine.jsonl` bodies equal source XML `itertext()` exactly: 384,899 characters |
| IDs and page labels | All 437 source IDs retained in order, with no within-document duplicates; all 267 EPUB pagebreak labels retained |
| Source hyperlinks | All 211 retained in order with their visible labels: 203 local, 8 external; every local target/fragment exists |
| Images | All 28 manifest assets and reading-order references retained; 3,428,235 image bytes match the source members and recorded hashes |
| Tables | All 5 preserved as tables: 36 rows, 90 cells, with source order, cell types, spans and text intact |
| Lists | All 12 ordered lists, 14 unordered lists and 97 list items retain their nesting and text order |
| Superscripts/subscripts | All 6 superscripts and the single subscript retained, including the exponent in the chapter 1 formula |
| Parsed text | All 69,207 source lexical tokens retained in order after excluding the conversion's explicit page-label annotations |

The EPUB also contains **`OEBPS/text/nav.xhtml` outside the spine**. It remains in the preserved original, rather than receiving a separate Markdown document. Its 71 contents entries, 3 landmarks and 267 page-list links all resolve to retained reading-order targets. The NCX independently supplies 71 navigation entries, also checked against source destinations. All other manifest XHTML documents belong to the 39-document spine. CSS and packaging metadata remain available in the original.

## Three conversion defects were repaired

The coordinator changed the importer and regenerated this book; this audit changed only this note.

1. **Formula semantics:** ordinary inline `<sup>`/`<sub>` elements had been flattened. Chapter 1's `2` raised to `n` would have appeared as `2n`; chapter 7's `It` subscript `1` also lost its distinction. The final output preserves these tags and all superscript footnote markers. ([Chapter 1](derived/the-right-it/009-chapter-1.md#page_20), [chapter 7](derived/the-right-it/017-chapter-7.md#page_187).)
2. **Link nesting:** generated ID-only anchors inside source hyperlink labels produced invalid nested `<a>` elements, including the Prelude heading. Locators now use `<span id>`; IDs and links remain unchanged, and all source link labels match after parsing. ([Prelude](derived/the-right-it/006-prelude.md#_idParaDest-1).)
3. **False list nesting:** leading spaces inside source italics made the concluding Go/Drop choices parse as extra unordered lists. Semantic `<em>`/`<strong>` markup now preserves emphasis and whitespace without introducing list syntax. The final list counts and nested relationships match the source. ([Chapter 9 recap](derived/the-right-it/019-chapter-9.md#page_231).)

Tables were separately compared in chapters 4, 5, 6 (two tables), and 7. The final verification used the bundled **`marked` 17.0.5** parser and parsed its resulting HTML; it did not merely count Markdown delimiters. GFM adds six autolinks to existing plain URL/email text, producing **217 parsed hyperlinks** while preserving all 211 source links. Those additional links contain no newly acquired source material and were not followed.

## Images and edition observations

Visually inspected the [cover](derived/the-right-it/images/001-cover.jpg), [title page](derived/the-right-it/images/028-titlepage.jpg), [TRI Meter](derived/the-right-it/images/009-image159.jpg), [Right/Wrong It region diagram](derived/the-right-it/images/023-p187.jpg), and [recap flowchart](derived/the-right-it/images/017-image230.jpg). They remain readable. The title page credits **Alberto Savoia**, *The Right It: Why So Many Ideas Fail and How to Make Sure Yours Succeed*, **HarperOne**, an imprint of HarperCollins. The OPF records the shorter title and publisher HarperCollins; it is preserved without editorial rewriting.

The [copyright document](derived/the-right-it/024-copyright.md#_copy) identifies **first edition, digital edition February 2019**, ebook ISBN **978-0-06-288467-1**, print ISBN **978-0-06-288465-7**, and version **01092019**. OPF metadata separately records a January 3, 2019 date and Calibre metadata. Those package dates should not silently replace the edition statement.

The meter's percentages, region labels and recap arrows are image content, not extracted text: most source image alt attributes say only `image`, and some are empty. The audit verifies legibility and preservation, not calibration of the meter or the method's predictive accuracy. **The other 23 images were byte-checked but not visually reviewed.**

## Limits

- All reading-order bodies were mechanically checked; this audit did not substantively reread the book, validate historical or statistical claims, or editorially verify every cross-reference.
- Publisher CSS, fixed layout, ornamental rules and alphabetic list-marker styling are not reproduced. The three spaced-asterisk section separators in chapter 5 render as horizontal rules; their section separation remains visible. Other text punctuation was retained in the token comparison.
- Explicit page-label annotations can interrupt words that span source pages. The original uninterrupted raw body text remains searchable in `spine.jsonl`; labels are retained source locators, not newly generated pagination.
- Inline HTML support and appearance depend on the Markdown viewer. Passing the checked parser does not establish identical rendering everywhere.
- Original bytes, source prompts, and publisher notices were preserved as data. No external destinations or embedded instructions were executed.
