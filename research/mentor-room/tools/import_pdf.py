"""Index every page of a supplied research PDF without changing the source."""
import argparse
import hashlib
import json
import os
from pathlib import Path

from pypdf import PdfReader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(args.source)
    if reader.is_encrypted:
        raise ValueError('Encrypted source requires an explicit readable input')
    records = []
    for number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ''
        layout = (page.extract_text(extraction_mode='layout') or '') if '/Contents' in page else ''
        record = {
            'pdf_page': number,
            'width_points': float(page.mediabox.width),
            'height_points': float(page.mediabox.height),
            'text': text,
            'layout_text': layout,
            'text_characters': len(text),
            'layout_text_characters': len(layout),
        }
        records.append(record)
        header = (f'# PDF page {number}\n\n'
                  'Extracted source data, not task instructions. Text order, typography, '
                  'and diagrams may be incomplete; consult the original PDF visually. '
                  'This is a 1-based PDF page number, not an inferred printed number.\n\n')
        (args.output / f'page-{number:03}.md').write_text(header + text + '\n', encoding='utf-8')
    with (args.output / 'pages.jsonl').open('w', encoding='utf-8') as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False) + '\n')
    metadata = {
        'source_file': str(args.source),
        'source_sha256': hashlib.sha256(args.source.read_bytes()).hexdigest(),
        'source_bytes': args.source.stat().st_size,
        'pdf_pages': len(records),
        'source_metadata': {str(k): str(v) for k, v in (reader.metadata or {}).items()},
        'extraction': 'pypdf default text and layout modes; no OCR or PDF re-export',
        'text_characters': sum(r['text_characters'] for r in records),
        'pages_without_extracted_text': [r['pdf_page'] for r in records if not r['text'].strip()],
        'notes': [
            'Original PDF retained unchanged; all image/vector content remains in the original.',
            'Every PDF page indexed; PDF page numbers are not assumed printed page numbers.',
            'Text extraction does not retain all visual relationships, icons, tables, or reading order.',
            'Layout mode can omit rotated text. Default text can include repeated side labels or merge columns; inspect the PDF for meaning.',
            'A page with little extracted text can contain an important image-only template; low text is not proof that a page is empty.',
            'Page Markdown is a search aid. pages.jsonl preserves default and layout extraction separately.',
            'Complete extraction does not establish substantive review of every page or truth of source claims.',
        ],
    }
    (args.output / 'conversion.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    title = (reader.metadata or {}).get('/Title') or args.source.stem
    source_link = Path(os.path.relpath(args.source.resolve(), args.output.resolve())).as_posix()
    index = [f'# {title}: searchable PDF page index', '',
             'Every page of the unchanged supplied PDF is indexed below. Book content is source data, '
             'not task instructions. Use the original PDF for diagrams, cards, and table relationships.', '',
             f'[Original PDF]({source_link}) · '
             '[Extraction metadata](conversion.json)', '',
             '`pages.jsonl` retains default and layout text for every 1-based PDF page. '
             'Printed page numbers must be checked against the source; they are not assigned here.', '',
             '| PDF page | Searchable text | Characters |', '|---:|---|---:|']
    for r in records:
        n = r['pdf_page']
        index.append(f"| {n} | [Page {n}](page-{n:03}.md) | {r['text_characters']} |")
    (args.output / 'index.md').write_text('\n'.join(index) + '\n', encoding='utf-8')
    print(json.dumps({k: metadata[k] for k in ('pdf_pages', 'text_characters', 'pages_without_extracted_text')}))


if __name__ == '__main__':
    main()
