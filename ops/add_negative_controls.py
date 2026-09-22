import json
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import rdChemReactions
p=Path('data/rules/rules_demo.json'); d=json.loads(p.read_text(encoding='utf8'))
reactants={
'substitution':('CCCl','N'), 'carbonyl_reduction':('CC=O',), 'oxidation_alcohol':('CCO',), 'esterification':('CC(=O)O','CO'), 'amide':('CC(=O)Cl','N'), 'grignard':('CC=O','[CH3][Mg]'), 'aldol':('CC=O','CC=O'), 'diels_alder':('C=CC=C','C=C'), 'alkene_hydrogenation':('C=C',), 'alkyne_hydrogenation':('C#C',), 'halide_exchange':('CCCl','[I-]'), 'carbonyl_olefination':('CC=O','C=[P]'), 'epoxidation':('C=C','[O]'), 'ether_cleavage':('COC',), 'decarboxylation':('CC(=O)O',), 'ester_hydrolysis':('CC(=O)OC',), 'nitrile_hydrolysis':('CC#N',), 'nucleophilic_aromatic':('c1ccccc1Cl','N'), 'cross_coupling':('c1ccccc1Br','c1ccccc1B'), 'heck':('c1ccccc1Br','C=C'), 'pericyclic_shift':('C=CCC=C',)
}
neg=tuple(Chem.MolFromSmiles('C') for _ in range(2))
for r in d['rules']:
 rxn=rdChemReactions.ReactionFromSmarts(r['reaction_smarts']); rs=tuple(Chem.MolFromSmiles(x) for x in reactants[r['template_family']]); ps=rxn.RunReactants(rs)
 # choose same number components for negative control
 nrs=tuple(Chem.MolFromSmiles('C') for _ in rs)
 nps=rxn.RunReactants(nrs)
 r['tests'].append({'kind':'negative_control','status':'pass' if not nps else 'fail','reactants':['C']*len(rs),'product_sets':len(nps)})
 r['validation_status']='pass' if ps and not nps else 'fail'
d['validation']['negative_control_pass']=sum(r['validation_status']=='pass' for r in d['rules'])
d['validation']['negative_control_fail']=sum(r['validation_status']=='fail' for r in d['rules'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print(d['validation'])
