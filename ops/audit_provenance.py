"""Audit provenance, controls, and declared scope for Literature2SMIRKS rules."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    failures=[]; stats={"rules":0,"source_page_evidence":0,"positive_controls":0,"negative_controls":0,"source_transcribed":0,"source_general_scheme":0,"strict_eligible":0,"needs_review":0}
    for path in sorted((ROOT/'data'/'rules').glob('*.json')):
        data=json.loads(path.read_text(encoding='utf-8'))
        for row in data.get('rules',[]):
            stats['rules'] += 1
            ev=row.get('evidence_status','unknown'); stats[ev]=stats.get(ev,0)+1
            src=row.get('source',{}); se=row.get('source_evidence',{})
            if not src.get('pdf_pages') or not src.get('printed_pages') or not src.get('entry_id'):
                failures.append((row.get('rule_id'),'missing source page or entry id'))
            else: stats['source_page_evidence'] += 1
            tests=row.get('tests',[])
            if any(t.get('kind') in {'parser_and_smoke','source_scheme_replay_with_constructed_R_group'} and t.get('status')=='pass' for t in tests): stats['positive_controls'] += 1
            else: failures.append((row.get('rule_id'),'missing passing positive/replay control'))
            if any(t.get('kind')=='negative_control' and t.get('status')=='pass' for t in tests): stats['negative_controls'] += 1
            else: failures.append((row.get('rule_id'),'missing passing negative control'))
            if not row.get('limitations'): failures.append((row.get('rule_id'),'missing limitations'))
            if row.get('strict_smirks_eligible') is True: stats['strict_eligible'] += 1
            elif row.get('strict_smirks_lint',{}).get('status')=='needs_review': stats['needs_review'] += 1
    print(json.dumps({"stats":stats,"failures":failures},ensure_ascii=False,indent=2))
    return 1 if failures else 0
if __name__=='__main__': raise SystemExit(main())
