import json
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import rdChemReactions
p=Path('data/rules/rules_demo.json'); d=json.loads(p.read_text(encoding='utf-8'))
reactants={
'substitution':('CCCl','N'), 'carbonyl_reduction':('CC=O',), 'oxidation_alcohol':('CCO',), 'esterification':('CC(=O)O','CO'), 'amide':('CC(=O)Cl','N'), 'grignard':('CC=O','[CH3][Mg]'), 'aldol':('CC=O','CC=O'), 'diels_alder':('C=CC=C','C=C'), 'alkene_hydrogenation':('C=C',), 'alkyne_hydrogenation':('C#C',), 'halide_exchange':('CCCl','[I-]'), 'carbonyl_olefination':('CC=O','C=[P]'), 'epoxidation':('C=C','[O]'), 'ether_cleavage':('COC',), 'decarboxylation':('CC(=O)O',), 'ester_hydrolysis':('CC(=O)OC',), 'nitrile_hydrolysis':('CC#N',), 'nucleophilic_aromatic':('c1ccccc1Cl','N'), 'cross_coupling':('c1ccccc1Br','c1ccccc1B'), 'heck':('c1ccccc1Br','C=C'), 'pericyclic_shift':('C=CCC=C',)
}
for r in d['rules']:
    f=r['template_family']; sm=r['reaction_smarts']; err=None; n=0
    try:
        rxn=rdChemReactions.ReactionFromSmarts(sm)
        if rxn is None: raise ValueError('null reaction')
        rs=[]
        for s in reactants[f]:
            m=Chem.MolFromSmiles(s)
            if m is None: raise ValueError('bad reactant '+s)
            rs.append(m)
        ps=rxn.RunReactants(tuple(rs)); n=len(ps)
        if not ps: raise ValueError('no products')
    except Exception as e: err=str(e)
    r['tests']=[{'kind':'parser_and_smoke','status':'pass' if not err else 'fail','product_sets':n,'error':err}]
    r['validation_status']='pass' if not err else 'fail'
passn=sum(x['validation_status']=='pass' for x in d['rules']); fail=[x for x in d['rules'] if x['validation_status']=='fail']
d['validation']={'tested_at':'2026-09-22','rules_total':len(d['rules']),'parser_smoke_pass':passn,'parser_smoke_fail':len(fail),'note':'Smoke checks validate parsing and at least one product only; they do not validate literature fidelity.'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print(d['validation']); print([(x['rule_id'],x['template_family'],x['tests'][0]['error']) for x in fail[:30]])
