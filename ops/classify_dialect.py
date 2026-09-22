"""Classify strict-SMIRKS eligibility using map-set lint only."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def maps(side):
    return {int(x) for x in re.findall(r':(\d+)', side)}

def main():
    report=[]
    for path in (ROOT/'data/rules').glob('*.json'):
        data=json.loads(path.read_text(encoding='utf-8'))
        for row in data.get('rules',[]):
            left,right=row['reaction_smarts'].split('>>')
            lm,rm=maps(left),maps(right)
            eligible=lm==rm
            row['strict_smirks_eligible']=eligible
            row['strict_smirks_lint']={'reactant_maps':sorted(lm),'product_maps':sorted(rm),'unmapped_reactant_maps':sorted(lm-rm),'product_only_maps':sorted(rm-lm),'status':'pass' if eligible else 'needs_review'}
            report.append((row['rule_id'],eligible,sorted(lm-rm)))
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'rules':len(report),'strict_smirks_eligible':sum(x[1] for x in report),'needs_review':sum(not x[1] for x in report),'examples_needing_review':[x for x in report if not x[1]][:8]},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
