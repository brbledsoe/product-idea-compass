# Mentor room research

The [wayfinder map](../../.scratch/mentor-room/map.md) coordinates this work. A first project-local [mentor-room skill](../../.agents/skills/mentor-room/SKILL.md) is authored; [usage guidance](../../docs/mentor-room.md) explains how to start or resume a case. [Independent behavioral trials and checks](../../docs/mentor-room-validation.md) are complete for this version, including an observed defect and successful correction. A real-idea pilot remains separate.

**Current source batch is capped.** Brandon supplied Testing Business Ideas as the final book for now. The [readiness assessment](source-batch-readiness.md) records the source handoff and its subsequent implementation status. Further uploads are optional.

## Source inventory

[resources.csv](resources.csv) is the unchanged 49-row inventory supplied by Brandon on 2026-09-05. Its descriptions, dates, ranking, and notes are supplied metadata, not verified instructions or research conclusions.

Source: `C:\Users\Brandon\Downloads\product-idea-validation-resources\startup_idea_product_validation_resources.csv`

SHA-256: `60A1E909CFD05E2FCD53FAC2FEE71399E61347914BBD3956F4F95A8B5EB073DB`

## Research notes

### Supplied Click materials

- [Click book method](click-book-method.md): 20 reference IDs with source-stated activities, outputs, exact PDF pages, and chapter/checklist differences. Procedural text and selected diagrams reviewed; not a cover-to-cover review or a finished playbook.
- [Workshop source analysis](click-workshop-analysis.md): all 13 pages of the supplied official Character guide snapshot and all 47 physical CSV rows reviewed. Separates official method from the unattributed agenda's timeboxes and omissions.
- [Mural template access](mural-template-access.md): the supplied public preview is accessible and credited to Jonathan Vardy. Partial canvas inspection; no local copy/export acquired.
- [Received-source manifest](sources/click/manifest.json): original paths, immutable-copy hashes, file sizes, PDF metadata, and text extraction state for this batch.
- [Click PDF](sources/click/click-jake-knapp.pdf) and [page index](derived/click/click-jake-knapp-page-index.tsv): 215-page supplied ebook conversion; reference its 1-based PDF pages, not assumed print pagination. The adjacent JSONL extraction supports page-specific searches and is source data, not instructions.
- [Official guide snapshot](sources/click/two-day-workshop-website-snapshot.pdf): image-only supplied PDF, retained intact; consult the visual analysis above for searchable findings.
- [Original remote agenda](sources/click/foundation-sprint-remote-agenda-v1.csv) and [normalized research data](derived/click/foundation-sprint-remote-agenda-normalized.json): original preserved; derived JSON distinguishes both days, source rows, encoding, repeated IDs, and the explicitly inferred wrap-up time correction.

### Supplied Mark Pincus material

- [Idea development and testing methods](pincus-idea-methods.md): 13 reference IDs for instincts versus ideas, Minimum Idea State, Proven Better New, customer signals, and stopping heuristics. Includes source locations, diagrams, the author's criticism of generated AI examples, and explicit review boundaries.
- [Iteration methods and fit with the core](pincus-iteration-and-fit.md): roadmaps, Bold Beats, manual learning, and new-platform experiments; proposed connections to Click and evidence reuse, plus source-specific metric discrepancies and stage limits.
- [Original EPUB](sources/pincus/life-at-the-speed-of-play.epub) and [source manifest](sources/pincus/manifest.json): supplied file preserved unchanged, with original path, verified hash, and visible edition details.
- [Searchable chapter index](derived/pincus/index.md): all 29 EPUB reading-order documents converted to Markdown, retaining 52 image assets, source anchors/page labels, and working links. Raw source text remains in the adjacent `spine.jsonl`; extraction is not a claim that every narrative or illustration was substantively reviewed.
- [Conversion metadata](derived/pincus/conversion.json) records exact changes and retained assets. For another supplied EPUB, the [importer](tools/import_epub.py) provides the same reference format; validate that file's own content and structure after conversion.
- [Independent conversion audit](pincus-conversion-check.md): verifies source identity, all 29 documents, 52 images, 100 links, and source locators; records corrected rendering defects, minor formatting limits, and an incorrect diagram description inherited from the EPUB.

This book extends the Pincus source collection associated with inventory row 13. It does not mean that the separately listed podcast transcript has been acquired.

### Supplied Pattern Breakers material

- [Opportunity and idea-development methods](pattern-breakers-methods.md): source-grounded inflection and insight stress tests, discovery practices, and the limits of using breakthrough-startup criteria for other worthwhile ideas.
- [Customer evidence, action, and fit with the core](pattern-breakers-evidence-and-fit.md): implementation tests, early customers, learning from surprises, and relevant strategy practices; distinguishes source guidance from proposed connections to Click and Pincus.
- [Original EPUB](sources/pattern-breakers/pattern-breakers.epub) and [source manifest](sources/pattern-breakers/manifest.json): the supplied `.crdownload` passed EPUB archive checks and was preserved byte-for-byte as a local `.epub`. The visible title page credits Mike Maples Jr. and Peter Ziebelman; the internal ebook ISBN differs from the filename.
- [Searchable chapter index](derived/pattern-breakers/index.md): all 28 reading-order sections, including 15 numbered chapters, with source navigation titles, 8 images, and 8 tables. Tables retain row/cell relationships and merged cells as HTML within Markdown. Original source text remains in the adjacent `spine.jsonl`.
- [Conversion metadata](derived/pattern-breakers/conversion.json) and [independent audit](pattern-breakers-conversion-check.md): document preservation checks, source anchors, links, and rendering limits. The EPUB's `pg*` anchors provide source locators; they are not newly generated PDF pages or formal EPUB pagebreak labels.

This book supplements inventory row 9; the separate interview transcript is still unacquired. Its breakthrough-business focus is a conditional lens for the mentor room, not a universal pass/fail standard for every software idea. Knapp–Zeratsky coverage remains mandatory under Brandon's instructions.

### Supplied The Right It material

- [Hypothesis and pretotyping methods](the-right-it-methods.md): Alberto Savoia's market-engagement hypotheses, small experiments, and distinctions between opinions and behavioral evidence, with source locations and explicit review scope.
- [Evidence, decisions, and fit with the core](the-right-it-evidence-and-fit.md): interpreting results, testing variants, planning subsequent experiments, and connections to Click, Sprint, Pincus, and Pattern Breakers. Source numerical heuristics are distinguished from calibrated probabilities or universal validation rules.
- [Original EPUB](sources/the-right-it/the-right-it.epub) and [source manifest](sources/the-right-it/manifest.json): unchanged supplied copy, verified hash, and visible edition details. The book identifies a first edition, digital edition February 2019, with distinct ebook and print ISBNs.
- [Searchable chapter index](derived/the-right-it/index.md): all 39 reading-order sections, including nine chapters, glossary, and separate footnotes; 28 images and 5 source XHTML tables. Source text, page labels, and anchors remain available in `spine.jsonl`; illustrated charts require visual reading.
- [Conversion metadata](derived/the-right-it/conversion.json) and [independent audit](the-right-it-conversion-check.md): source identity, coverage, links, illustration preservation, and any rendering limitations. Conversion alone does not verify the book's anecdotes or numerical claims.

This supplied book strengthens inventory row 16. Its receipt does not establish acquisition or review of every talk or website resource associated with that row. The skill's experiment playbook identifies which combinations are room adaptations.

### Supplied Testing Business Ideas material

- [Assumptions, learning, and decision process](testing-business-ideas-process.md): 16 process references, including the Assumptions Map, Test Card, Learning Card, and evidence review. Visually verified template fields supplement the text extraction; organizational practices are conditional.
- [Experiment library and selection guidance](testing-business-ideas-experiments.md) and [structured inventory](testing-business-ideas-experiment-index.json): all 44 experiments (29 discovery, 15 validation), with source page spans, observable results, and selection questions. Full card text was read; 25 library pages were visually inspected. Source classification/formula inconsistencies are flagged, and graphical ratings have not been converted into scores. This is a library to select from, not a required 44-experiment curriculum.
- [Original PDF](sources/testing-business-ideas/testing-business-ideas.pdf) and [source manifest](sources/testing-business-ideas/manifest.json): unchanged supplied 365-page PDF by David J. Bland and Alex Osterwalder. Copyright states 2020; PDF creation metadata is dated November 2019. Both facts are recorded without inferring one from the other.
- [Searchable page index](derived/testing-business-ideas/index.md): all 365 physical PDF pages, with default and layout text retained separately in `pages.jsonl`. PDF page 2 is blank. Nonempty extracted text does not guarantee that a page's illustrated canvas, ratings, or card labels were captured; consult the original PDF and visual-template notes.
- [Extraction metadata](derived/testing-business-ideas/conversion.json) and [independent extraction audit](testing-business-ideas-extraction-check.md): source hash, complete page coverage, visual checks, and extraction/pagination limits. Physical PDF page numbers are the primary locators; front-matter metadata labels do not consistently match visible printed folios.

The book directly supplies inventory row 19 and supports the method associated with row 18; the separately listed webinar remains unacquired. All original image/vector content is preserved in the PDF. The [PDF indexing tool](tools/import_pdf.py) produces search aids without altering or re-exporting the source.

### Initial public-source investigations

- [Knapp–Zeratsky source baseline](knapp-zeratsky-baseline.md): official sprint activities and outputs, initial board access, and precisely bounded historical source coverage.
- [Character Labs template PDF](assets/character-labs-template-2026-09-05.pdf) and [complete exported activity inventory](knapp-template-coverage.md): actual combined board exported through Miro on 2026-09-05; 114 pages, about 84 MiB. All pages' text and 29 selected visual pages reviewed on 2026-09-06. The inventory maps 15 Foundation and 23 Design Sprint activities plus repeat/revision frames and preserves source variants.
- [Evidence and method overlap](evidence-and-overlap.md): verified selected public method sources, legitimate reuse, and limits on their conclusions.
- [Resource audit](resource-audit.md): complete 49-row inventory classification with a bounded eight-row access audit. Its row states apply to that audit, while the other notes record their own source checks.
- [Supplementary public methods](specialist-methods.md): five operational sessions from ten primary sources: Walling's 5PM and 2/20/200, Torres, Cagan, and Fitzpatrick. Exact reviewed scope and public-only adaptations are explicit.

Findings distinguish direct source content from room adaptations. A source URL alone does not establish that its contents have been read or saved. Five supplied books are held locally: Click, Life at the Speed of Play, Pattern Breakers, The Right It, and Testing Business Ideas. The skill's 49-row routing inventory preserves unavailable resources instead of claiming every expert's full curriculum is acquired.

## Materials available from Brandon

On 2026-09-05 Brandon confirmed access to Click, Sprint, the Click bonus worksheets, and podcast/video transcripts, and offered to share them. The next handoff supplied Click, the official-guide snapshot, a remote agenda, and the Mural link. [That batch's intake is complete](../../.scratch/mentor-room/issues/09-ingest-shared-materials.md). The repeated 49-resource CSV matched the existing copy exactly and was not duplicated.

Sprint, the official Click bonus worksheet pack, and transcripts have not yet been supplied. The snapshot and agenda are useful resources but have not been identified as that bonus pack. With the current batch capped, these are optional future additions rather than upload requests to make now. Define the initial mandatory-core boundary from actual available sources and preserve unreviewed coverage explicitly.

Brandon subsequently supplied *Life at the Speed of Play* as an EPUB and explicitly authorized useful format conversions. Its original and converted references are linked above; future source handoffs can use the same provenance and coverage conventions.

The next handoff supplied *Pattern Breakers*. Its download suffix did not prevent successful EPUB integrity checks or conversion; the original download was left untouched. The saved copy, searchable references, research notes, and audit are linked above.

Brandon then supplied *The Right It*. Its original EPUB, searchable conversion, method references, and audit follow the same source-preservation and coverage conventions and are linked above.

Brandon capped the current batch with *Testing Business Ideas*. Its indexed PDF and research complete this intake batch; the next work is making the researched methods usable in the room, not routine collection of more books.
