from pathlib import Path
import re,json
root=Path('.')
p=root/'private/pages'
a=[]
for n in range(56,556,2):
    txt=(p/f'{n:04}.txt').read_text(encoding='utf-8')
    head=re.split(r'\(References|Importance|importance',txt,maxsplit=1)[0]
    name=re.sub(r'\s+',' ',head).strip().lstrip('0123456789 ').strip()
    name=re.sub(r'\s*\n.*','',name)
    a.append({'entry_id':f'KCC{(n-56)//2+1:03d}','name':name,'printed_pages':[n-54,n-53],'pdf_pages':[n,n+1],'reading_status':'indexed','rule_ids':[]})
(root/'data').mkdir(exist_ok=True)
(root/'data/book_index.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
print(len(a)); print('\n'.join(f"{x['entry_id']} | {x['printed_pages'][0]} | {x['name']}" for x in a[:20]))
