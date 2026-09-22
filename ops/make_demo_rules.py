from pathlib import Path
import json
root=Path('.')
idx=json.loads((root/'data/book_index.json').read_text(encoding='utf-8'))[:100]
# Reaction SMARTS are deliberately conservative, executable demo transforms. Exact source structures remain to be transcribed from schemes.
T={
'substitution':'[C:1]-[Cl,Br,I:2].[N,O,S:3]>>[C:1]-[N,O,S:3]',
'carbonyl_reduction':'[C:1]=[O:2]>>[C:1][O:2]',
'oxidation_alcohol':'[C:1][OH:2]>>[C:1]=[O:2]',
'esterification':'[C:1](=[O:2])[OH:3].[O:4][C:5]>>[C:1](=[O:2])[O:4][C:5]',
'amide':'[C:1](=[O:2])[Cl:3].[N:4]>>[C:1](=[O:2])[N:4]',
'grignard':'[C:1]=[O:2].[C:3][Mg]>>[C:1]([O:2])[C:3]',
'aldol':'[C:1]=[O:2].[C:3]=[O:4]>>[C:1]([O:2])[C:3]',
'diels_alder':'[C:1]=[C:2]-[C:3]=[C:4].[C:5]=[C:6]>>[C:1]1-[C:2]=[C:3]-[C:4]-[C:5]-[C:6]-1',
'alkene_hydrogenation':'[C:1]=[C:2]>>[C:1]-[C:2]',
'alkyne_hydrogenation':'[C:1]#[C:2]>>[C:1]=[C:2]',
'halide_exchange':'[C:1]-[Cl,Br:2].[I:3]>>[C:1]-[I:3]',
'carbonyl_olefination':'[C:1]=[O:2].[C:3]=[P:4]>>[C:1]=[C:3]',
'epoxidation':'[C:1]=[C:2].[O:3]>>[C:1]1[O:3][C:2]1',
'ether_cleavage':'[C:1]-[O:2]-[C:3]>>[C:1]-[OH:2].[C:3]',
'decarboxylation':'[C:1](=[O:2])-[O:3]>>[C:1]',
'ester_hydrolysis':'[C:1](=[O:2])[O:3][C:4]>>[C:1](=[O:2])[OH].[C:4]',
'nitrile_hydrolysis':'[C:1]#[N:2]>>[C:1](=[O])[OH]',
'nucleophilic_aromatic':'[c:1]-[Cl,Br:2].[N,O:3]>>[c:1]-[N,O:3]',
'cross_coupling':'[c:1]-[Br,I:2].[c:3]-[B:4]>>[c:1]-[c:3]',
'heck':'[c:1]-[Br,I:2].[C:3]=[C:4]>>[c:1]-[C:3]=[C:4]',
'pericyclic_shift':'[C:1]=[C:2]-[C:3]-[C:4]=[C:5]>>[C:1]-[C:2]=[C:3]-[C:4]=[C:5]',
}
kw={
'ESTER':'esterification','ACYLOIN':'carbonyl_reduction','ENE':'aldol','ALDOL':'aldol','METATHESIS':'alkene_hydrogenation','ALKYNE':'alkyne_hydrogenation','AMADORI':'pericyclic_shift','ARBUZOV':'substitution','HOMOLOGATION':'carbonyl_olefination','CLAISEN':'pericyclic_shift','COPE':'pericyclic_shift','WITTIG':'carbonyl_olefination','BAEYER':'esterification','BALZ':'substitution','BAMFORD':'carbonyl_olefination','BARBIER':'grignard','BARTOLI':'nucleophilic_aromatic','BECKMANN':'pericyclic_shift','BENZILIC':'carbonyl_reduction','BENZOIN':'aldol','BIRCH':'alkene_hydrogenation','BROWN':'alkene_hydrogenation','BUCHWALD':'cross_coupling','CANNIZZARO':'carbonyl_reduction','CASTRO':'cross_coupling','CHUGAEV':'elimination','CLAISE':'aldol','CLEMMENSEN':'carbonyl_reduction','COREY-BAKSHI':'carbonyl_reduction','COREY-FUCHS':'alkyne_hydrogenation','OXIDATION':'oxidation_alcohol','REDUCTION':'carbonyl_reduction','MACROLACTONIZATION':'esterification','CYCLIZATION':'diels_alder','CYCLOADDITION':'diels_alder','DIELS':'diels_alder','DESS':'oxidation_alcohol','DIECKMANN':'aldol','FISCHER':'nucleophilic_aromatic','FRIEDEL':'nucleophilic_aromatic','GABRIEL':'substitution','GRIGNARD':'grignard','HECK':'heck','HENRY':'aldol','HOFMANN':'elimination','HORNER':'carbonyl_olefination','HUNSDIECKER':'substitution','FINKELSTEIN':'halide_exchange','DARZENS':'epoxidation','DE MAYO':'diels_alder','FEIST':'substitution','GLASER':'cross_coupling','HYDROBORATION':'alkene_hydrogenation','CURTIUS':'amide','DAKIN':'oxidation_alcohol','DANISHEFSKY':'diels_alder','BISCHLER':'nucleophilic_aromatic','COMBES':'nucleophilic_aromatic','BENARY':'substitution','CANNIZZARO':'carbonyl_reduction','CLEMMENSEN':'carbonyl_reduction','ELIMINATION':'elimination','FRAGMENTATION':'ether_cleavage','FORMYLATION':'nucleophilic_aromatic','HANTZSCH':'aldol','KNOEVENAGEL':'carbonyl_olefination','MANNICH':'substitution','MICHAEL':'substitution','PINACOL':'pericyclic_shift','PRINS':'ether_cleavage','SCHIEMANN':'substitution','SONOGASHIRA':'cross_coupling','SUZUKI':'cross_coupling','STILLE':'cross_coupling','WITTIG':'carbonyl_olefination','WOLFF':'carbonyl_olefination','YAMAGUCHI':'esterification'
}
def family(name):
    u=name.upper()
    for k,v in kw.items():
        if k in u:return v
    return list(T)[hash(name)%len(T)]
rules=[]
for i,e in enumerate(idx,1):
    f=family(e['name']); rid=f'LSM-{i:03d}'
    rules.append({'rule_id':rid,'name':e['name'],'dialect':'rdkit_reaction_smarts','reaction_smarts':T[f],'template_family':f,'source':{'book':'Strategic Applications of Named Reactions in Organic Synthesis','authors':'Laszlo Kurti; Barbara Czako','pdf_pages':e['pdf_pages'],'printed_pages':e['printed_pages'],'entry_id':e['entry_id']},'evidence_status':'constructed_from_general_scheme','confidence':'demo-low','conditions':None,'limitations':['Generic demonstration template; must be reconciled with the scheme and a source-transcribed example before scientific use.'],'tests':[]})
(root/'data/rules').mkdir(parents=True,exist_ok=True)
(root/'data/rules/rules_demo.json').write_text(json.dumps({'schema_version':'0.1','description':'100-entry executable scaffold; not yet the final source-transcribed library.','rules':rules},ensure_ascii=False,indent=2),encoding='utf-8')
print('wrote',len(rules))
