"""Index the supplied PDF locally; source pages and text never enter git."""
from pathlib import Path
import argparse
import hashlib
import json
import datetime
import fitz

ROOT = Path(__file__).resolve().parents[1]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf', type=Path)
    args = ap.parse_args()
    source = args.pdf.resolve()
    private = ROOT / 'private'
    texts = private / 'pages'
    texts.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(source)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text(sort=True)
        (texts / f'{i+1:04}.txt').write_text(text, encoding='utf-8')
        pages.append({'pdf_page': i+1, 'characters': len(text),
                      'text_sha256': hashlib.sha256(text.encode()).hexdigest(),
                      'dimensions': list(page.rect), 'text_read': False,
                      'visual_review': False})
    manifest = {'source_path': str(source), 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                'page_count': len(doc), 'metadata': doc.metadata, 'pages': pages}
    (private / 'source_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in manifest.items() if k != 'pages'}, ensure_ascii=False, indent=2))
    print('FIRST PAGES')
    for i in range(7,18):
        print(f'PDF PAGE {i+1}\n' + doc[i].get_text(sort=True))

if __name__ == '__main__':
    main()
