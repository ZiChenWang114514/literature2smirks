import json, re, hashlib
from pathlib import Path
root=Path('.')
idx=json.loads((root/'data/book_index.json').read_text(encoding='utf8'))
p=root/'data/rules/rules_demo.json'; d=json.loads(p.read_text(encoding='utf8'))
by={x['entry_id']:x for x in idx}
for r in d['rules']:
 e=by[r['source']['entry_id']]; page=e['pdf_pages'][0]; text=(root/'private/pages'/f'{page:04}.txt').read_text(encoding='utf8')
 norm=re.sub(r'\s+',' ',text).strip()
 # Keep public evidence as a digest and locator, not a long copyrighted excerpt.
 r['evidence_status']='source_general_scheme'
 r['source_evidence']={'source_pdf_pages':e['pdf_pages'],'source_printed_pages':e['printed_pages'],'source_text_sha256':hashlib.sha256(text.encode()).hexdigest(),'source_text_anchor':'chapter title, definition paragraph, and general-scheme region on first chapter page','source_text_characters':len(text),'source_page_has_selectable_text':bool(text.strip()),'evidence_scope':'The named-reaction chapter and its general transformation support the template family; exact substrate graph transcription remains pending.'}
d['description']='100-entry executable scaffold upgraded with source-page evidence locators. These remain general-scheme templates until source structures are transcribed.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print('upgraded',len(d['rules']),'rules')
