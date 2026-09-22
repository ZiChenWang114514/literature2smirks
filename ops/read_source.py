"""Read local source pages or render them; page numbers are one-based PDF pages."""
from pathlib import Path
import argparse
import json
import re
import fitz

ROOT = Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('pages', help='e.g. 56-65 or 56,58,60')
    ap.add_argument('--render', action='store_true')
    ap.add_argument('--width', type=int, default=1400)
    ap.add_argument('--head', type=int)
    args=ap.parse_args()
    pages=[]
    for part in args.pages.split(','):
        if '-' in part:
            a,b=map(int,part.split('-')); pages.extend(range(a,b+1))
        else: pages.append(int(part))
    manifest=json.loads((ROOT/'private/source_manifest.json').read_text(encoding='utf-8'))
    if args.render:
        doc=fitz.open(manifest['source_path'])
        out=ROOT/'private/renders'; out.mkdir(exist_ok=True)
        for n in pages:
            p=doc[n-1]; path=out/f'{n:04}.png'
            p.get_pixmap(matrix=fitz.Matrix(args.width/p.rect.width,args.width/p.rect.width)).save(path)
            print(path)
    else:
        for n in pages:
            txt=(ROOT/f'private/pages/{n:04}.txt').read_text(encoding='utf-8')
            txt=re.sub(r'[ \t]+',' ',txt)
            txt=re.sub(r'\n\s*\n','\n',txt).strip()
            print(f'\nPDF PAGE {n}; PRINTED PAGE {n-54 if n>=55 else "front matter"}\n'+(txt[:args.head] if args.head else txt))

if __name__=='__main__': main()
