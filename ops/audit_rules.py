"""Audit rule records without claiming chemical or experimental validity."""
from pathlib import Path
import json
from rdkit import Chem
from rdkit.Chem import rdChemReactions

ROOT=Path(__file__).resolve().parents[1]

def main():
    files=list((ROOT/'data/rules').glob('*.json'))
    summary={'files':{},'source_transcribed_replays':0,'failures':[]}
    for path in files:
        data=json.loads(path.read_text(encoding='utf-8'))
        rows=data.get('rules',[]); out={'total':len(rows),'parse_pass':0,'parse_fail':0,'evidence_status':{}}
        for row in rows:
            status=row.get('evidence_status','unknown'); out['evidence_status'][status]=out['evidence_status'].get(status,0)+1
            try:
                rxn=rdChemReactions.ReactionFromSmarts(row['reaction_smarts'])
                if rxn is None: raise ValueError('ReactionFromSmarts returned None')
                out['parse_pass']+=1
            except Exception as exc:
                out['parse_fail']+=1; summary['failures'].append({'rule_id':row.get('rule_id'),'error':str(exc)})
            for test in row.get('tests',[]):
                if test.get('kind')=='source_scheme_replay_with_constructed_R_group' and test.get('status')=='pass':
                    summary['source_transcribed_replays']+=1
        summary['files'][path.name]=out
    summary['rules_total']=sum(x['total'] for x in summary['files'].values())
    summary['parse_pass']=sum(x['parse_pass'] for x in summary['files'].values())
    summary['parse_fail']=sum(x['parse_fail'] for x in summary['files'].values())
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    if summary['parse_fail']: raise SystemExit(1)

if __name__=='__main__': main()
