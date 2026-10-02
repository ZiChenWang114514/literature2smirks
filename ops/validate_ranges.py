"""Probe reaction SMARTS family coverage with near-neighbor and nonmatching inputs."""
import json
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import rdChemReactions
ROOT=Path(__file__).resolve().parents[1]
rows={r['rule_id']:r for f in (ROOT/'data/rules').glob('*.json') for r in json.loads(f.read_text(encoding='utf8')).get('rules',[])}
probes={
 'LSM-SRC-001':{
  'positive':[['CC(=O)CC(=O)OC','CCBr'],['CC(=O)CC(=O)OC','CCCBr']],
  'negative':[['CC(=O)CC(=O)OC','CC'],['CC(=O)CC(=O)OC','c1ccccc1Br']]},
 'LSM-SRC-009':{
  'positive':[['OB(O)c1ccccc1','Brc1ccccc1'],['OB(O)c1ccc(C)cc1','Brc1ccccc1'],['OB(O)c1ccccc1','Brc1ccc(C)cc1']],
  'negative':[['OB(O)c1ccccc1','CC'],['CC','Brc1ccccc1']]},
 'LSM-SRC-015':{
  'positive':[['Brc1ccccc1','C=C'],['COc1ccc(Br)cc1','C=C'],['Brc1ccc(C)cc1','C=C']],
  'negative':[['Brc1ccccc1','CC'],['CC','C=C']]},
}
out={'schema_version':'0.1','description':'Near-neighbor reaction SMARTS coverage probes; not experimental scope claims.','rules':[]}
for rid,p in probes.items():
 rxn=rdChemReactions.ReactionFromSmarts(rows[rid]['reaction_smarts']); rec={'rule_id':rid,'positive':[],'negative':[]}
 for kind,sets in [('positive',p['positive']),('negative',p['negative'])]:
  for rs in sets:
   mols=tuple(Chem.MolFromSmiles(x) for x in rs); n=len(rxn.RunReactants(mols)); rec[kind].append({'reactants':rs,'product_sets':n,'pass':n>0 if kind=='positive' else n==0})
 rec['positive_pass']=all(x['pass'] for x in rec['positive']); rec['negative_pass']=all(x['pass'] for x in rec['negative']); out['rules'].append(rec)
print(json.dumps(out,ensure_ascii=False,indent=2))
