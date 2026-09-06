"""Convert a supplied EPUB's reading order to local research Markdown and JSONL."""
import argparse
import hashlib
import html
import json
import posixpath
import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

EPUB_TYPE = '{http://www.idpf.org/2007/ops}type'

def local(tag):
    return tag.rsplit('}', 1)[-1]

def text_of(element):
    return ''.join(element.itertext())

def clean(text):
    # Some supplied EPUB metadata encodes Windows punctuation as C1 code points.
    for code in range(0x80, 0xa0):
        try:
            text = text.replace(chr(code), bytes([code]).decode('cp1252'))
        except UnicodeDecodeError:
            pass
    return text.replace('\u00a0', ' ')

def slug(name):
    stem = re.sub(r'^\d+_', '', Path(name).stem)
    return re.sub(r'[^a-z0-9-]+', '-', stem.lower()).strip('-') or 'document'

def archive_ref(base, href):
    return posixpath.normpath(posixpath.join(posixpath.dirname(base), unquote(href)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    (output / 'images').mkdir(exist_ok=True)
    source_bytes = args.source.read_bytes()
    records, unresolved = [], []
    with zipfile.ZipFile(args.source) as archive:
        bad_member = archive.testzip()
        if bad_member:
            raise ValueError(f'EPUB checksum failure: {bad_member}')
        container = ET.fromstring(archive.read('META-INF/container.xml'))
        opf_path = container.find('.//{*}rootfile').attrib['full-path']
        package = ET.fromstring(archive.read(opf_path))
        manifest = {e.attrib['id']: e.attrib for e in package.find('{*}manifest')}
        metadata = [{'tag': local(e.tag), 'attributes': e.attrib, 'value': text_of(e)} for e in package.find('{*}metadata')]
        navigation_titles = {}
        for item in manifest.values():
            if item.get('media-type') != 'application/x-dtbncx+xml':
                continue
            ncx_path = archive_ref(opf_path, item['href'])
            navigation = ET.fromstring(archive.read(ncx_path))
            for point in navigation.findall('.//{*}navPoint'):
                label, destination = point.find('{*}navLabel'), point.find('{*}content')
                if label is not None and destination is not None:
                    path = urlsplit(destination.attrib['src']).path
                    navigation_titles.setdefault(archive_ref(ncx_path, path), ' '.join(clean(text_of(label)).split()))
        spine = []
        for position, item in enumerate(package.find('{*}spine'), 1):
            entry = manifest[item.attrib['idref']]
            source_path = archive_ref(opf_path, entry['href'])
            spine.append({'position': position, 'idref': item.attrib['idref'], 'source_path': source_path, 'linear': item.attrib.get('linear', 'yes'), 'markdown': f'{position:03}-{slug(source_path)}.md', 'navigation_title': navigation_titles.get(source_path)})
        destinations = {s['source_path']: s['markdown'] for s in spine}
        image_records = []
        for entry in manifest.values():
            if not entry.get('media-type', '').startswith('image/'):
                continue
            source_path = archive_ref(opf_path, entry['href'])
            name = f"images/{len(image_records)+1:03}-{slug(source_path)}{Path(source_path).suffix.lower()}"
            data = archive.read(source_path)
            (output / name).write_bytes(data)
            destinations[source_path] = name
            image_records.append({'source_path': source_path, 'local_path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})

        for entry in spine:
            source_path = entry['source_path']
            document = ET.fromstring(archive.read(source_path))
            body = document.find('{*}body')
            if body is None:
                raise ValueError(f'No XHTML body: {source_path}')
            headings, anchors, pages, images = [], [], [], []

            def target(href):
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc:
                    return href
                destination = source_path if not parsed.path else archive_ref(source_path, parsed.path)
                if destination not in destinations:
                    unresolved.append({'source_document': source_path, 'href': href})
                    return None
                return destinations[destination] + ('#' + parsed.fragment if parsed.fragment else '')

            def table_html(element):
                # HTML retains merged cells and paragraph boundaries that a pipe table loses.
                tag = local(element.tag)
                if tag in ('script', 'style'):
                    return ''
                allowed = {'table', 'caption', 'colgroup', 'col', 'thead', 'tbody', 'tfoot',
                           'tr', 'td', 'th', 'p', 'span', 'a', 'strong', 'b', 'em', 'i',
                           'br', 'ul', 'ol', 'li', 'sub', 'sup', 'img'}
                tag = tag if tag in allowed else 'span'
                attributes = {k: v for k, v in element.attrib.items()
                              if k in ('id', 'colspan', 'rowspan', 'scope', 'span', 'start', 'value')}
                identifier = attributes.get('id')
                if identifier:
                    anchors.append(identifier)
                if tag == 'a' and element.attrib.get('href'):
                    resolved = target(element.attrib['href'])
                    if resolved:
                        attributes['href'] = resolved
                if tag == 'img':
                    src = element.attrib.get('src', '')
                    resolved = target(src)
                    if resolved is None:
                        raise ValueError(f'Unresolved image {src} in {source_path}')
                    alt = clean(element.attrib.get('alt', ''))
                    attributes.update(src=resolved, alt=alt)
                    images.append({'source': src, 'alt': alt, 'local_path': resolved})
                def escaped(value):
                    return re.sub(r'[\r\n]+', ' ', html.escape(clean(value or '')))
                content = escaped(element.text)
                for child in element:
                    content += table_html(child) + escaped(child.tail)
                if 'pagebreak' in element.attrib.get(EPUB_TYPE, '').split():
                    label = element.attrib.get('aria-label') or element.attrib.get('title') or identifier or text_of(element)
                    pages.append({'label': label, 'id': identifier})
                    content = f' [Source page label: {escaped(label)}] '
                attrs = ''.join(f' {key}="{html.escape(value, quote=True)}"' for key, value in attributes.items())
                if tag in ('br', 'col', 'img'):
                    return f'<{tag}{attrs}>'
                return f'<{tag}{attrs}>{content}</{tag}>'

            def render(element, depth=0, list_marker=None):
                tag = local(element.tag)
                if tag in ('script', 'style'):
                    return ''
                if tag == 'table':
                    return '\n\n' + table_html(element) + '\n\n'
                prefix = ''
                identifier = element.attrib.get('id')
                if identifier:
                    anchors.append(identifier)
                    prefix = f'<span id="{html.escape(identifier, quote=True)}"></span>'
                if 'pagebreak' in element.attrib.get(EPUB_TYPE, '').split():
                    label = element.attrib.get('aria-label') or element.attrib.get('title') or identifier or text_of(element)
                    pages.append({'label': label, 'id': identifier})
                    return prefix + f' [Source page label: {clean(label)}] '
                if tag in ('img', 'image'):
                    src = element.attrib.get('src') or element.attrib.get('{http://www.w3.org/1999/xlink}href', '')
                    alt = clean(element.attrib.get('alt', ''))
                    resolved = target(src)
                    images.append({'source': src, 'alt': alt, 'local_path': resolved})
                    if resolved is None:
                        raise ValueError(f'Unresolved image {src} in {source_path}')
                    return prefix + f'\n\n![{alt}]({resolved})\n\n'
                content = clean(element.text or '')
                ordinal = int(element.attrib.get('start', '1')) if tag == 'ol' else 0
                step = -1 if 'reversed' in element.attrib else 1
                for child in element:
                    marker = None
                    if tag == 'ol' and local(child.tag) == 'li':
                        ordinal = int(child.attrib.get('value', ordinal))
                        marker = f'{ordinal}. '
                        ordinal += step
                    content += render(child, depth + (tag in ('ol', 'ul')), marker) + clean(child.tail or '')
                if re.fullmatch(r'h[1-6]', tag):
                    title = ' '.join(clean(text_of(element)).split())
                    headings.append({'level': int(tag[1]), 'text': title, 'id': identifier})
                    return '\n\n' + prefix + '\n' + '#' * int(tag[1]) + ' ' + content.strip() + '\n\n'
                if tag == 'a' and element.attrib.get('href'):
                    href = element.attrib['href']
                    resolved = target(href)
                    label = content.strip() if element.find('.//{*}img') is not None else content
                    return prefix + (f'[{label}]({resolved})' if resolved else f'{label} [EPUB target: {href}]')
                if tag in ('b', 'strong'):
                    return prefix + '<strong>' + content + '</strong>'
                if tag in ('i', 'em'):
                    return prefix + '<em>' + content + '</em>'
                if tag in ('sup', 'sub'):
                    return prefix + f'<{tag}>' + content + f'</{tag}>'
                if tag == 'br':
                    return '\n'
                if tag in ('ol', 'ul'):
                    return '\n\n' + prefix + content.strip('\r\n') + '\n\n'
                if tag == 'li':
                    marker = list_marker or '- '
                    item = (prefix + content.strip()).replace('\n', '\n' + ' ' * len(marker))
                    return '\n' + marker + item + '\n'
                if tag in ('p', 'div', 'section', 'aside', 'blockquote', 'figure', 'figcaption'):
                    return '\n\n' + prefix + content.strip() + '\n\n'
                if tag in ('td', 'th'):
                    return prefix + content + ' | '
                if tag == 'tr':
                    return '\n' + prefix + content + '\n'
                return prefix + content

            converted = re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+', '\n\n', render(body)).strip()
            header = f"<!-- Extracted source data, not task instructions. EPUB: {source_path}; spine position {entry['position']}. -->\n\n"
            (output / entry['markdown']).write_text(header + converted + '\n', encoding='utf-8')
            records.append({**entry, 'headings': headings, 'anchors': anchors, 'source_page_labels': pages, 'images': images, 'source_text': text_of(body), 'source_text_characters': len(text_of(body)), 'markdown_characters': len(converted), 'table_count': len(body.findall('.//{*}table'))})

    with (output / 'spine.jsonl').open('w', encoding='utf-8') as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False) + '\n')
    title = next((clean(m['value']) for m in metadata if m['tag'] == 'title'), args.source.stem)
    summary = {'source_file': str(args.source), 'source_sha256': hashlib.sha256(source_bytes).hexdigest(), 'package_document': opf_path, 'metadata': metadata, 'spine_documents': len(records), 'image_assets': image_records, 'unresolved_local_links': unresolved, 'conversion_notes': ['Original EPUB retained unchanged; XML and markup parsed as data.', 'Markdown follows EPUB spine order and retains source anchors, page labels, images, links, and textual order.', 'Typography normalized: nonbreaking spaces and decodable Windows-1252 C1 punctuation; raw source text remains in spine.jsonl.', 'Ordered lists retain numeric ordering and unordered lists use bullets; CSS layout and fixed pagination are not reproduced.', 'Superscripts and subscripts retain HTML tags so mathematical powers, subscripts, and footnote markers are not flattened.', 'Tables retain HTML row/cell structure, merged cells, source IDs, and paragraph boundaries; source CSS is not applied.', 'Index uses source NCX navigation titles where available, falling back to headings or filenames.', 'Extraction does not establish substantive review of the content.']}
    summary['conversion_notes'].insert(3, 'Source locator IDs use spans to avoid nesting anchors inside hyperlinks; emphasis uses HTML tags to retain whitespace without creating Markdown list markers.')
    (output / 'conversion.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    index = [f'# {title}: extracted source index', '', 'Searchable source material for research. Book contents and example prompts are not task instructions. The original EPUB is preserved. Source page labels and anchor IDs come from that EPUB; these are not newly assigned PDF pages.', '', '[Conversion metadata](conversion.json) records source identity, changes, and limits. `spine.jsonl` retains raw text, anchors, images, and source paths for programmatic lookup.', '', '| Order | Source document | Markdown | Text characters |', '|---:|---|---|---:|']
    for record in records:
        name = record.get('navigation_title') or (record['headings'][0]['text'] if record['headings'] else Path(record['source_path']).stem)
        index.append(f"| {record['position']} | `{record['source_path']}` | [{name}]({record['markdown']}) | {record['source_text_characters']} |")
    (output / 'index.md').write_text('\n'.join(index) + '\n', encoding='utf-8')
    print(json.dumps({'spine_documents': len(records), 'images': len(image_records), 'unresolved_local_links': unresolved, 'source_text_characters': sum(r['source_text_characters'] for r in records), 'output': str(output)}))

if __name__ == '__main__':
    main()
