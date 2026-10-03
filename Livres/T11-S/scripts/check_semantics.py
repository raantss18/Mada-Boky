#!/usr/bin/env python3
"""Structural reconciliation; does not certify the semantic review."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/'review/inventory.json').read_text());ids={i['id'] for i in items}
assert len(ids)==len(items)
labels=[];references=[];question_labels=[]
files=sorted(list(ROOT.glob('chapitres/*/*.tex'))+list(ROOT.glob('annexes/*.tex'))+list(ROOT.glob('front/*.tex'))+[ROOT/'livre-t11s.tex'])
for f in files:
    s=re.sub(r'(?m)(?<!\\)%.*$','',f.read_text())
    labels+=re.findall(r'\\label\{([^}]+)\}',s)
    references+=re.findall(r'\\(?:ref|cref|Cref)\{([^}]+)\}',s)
    question_labels+=re.findall(r'\\exo(?:\[[^\]]*\])?\s*\\label\{([^}]+)\}',s)
assert len(labels)==len(set(labels)), 'Duplicate TeX labels'
assert set(references)<=set(labels),set(references)-set(labels)
assert set(question_labels)<={i['id'] for i in items if i['kind']=='exercise'}
for i in items:
    assert set(i.get('dependencies',[]))<=ids,('Unknown dependency',i['id'])
    if i['kind']=='exercise':assert i['correction_id'] in ids
matrix=json.loads((ROOT/'project/exercise-matrix.json').read_text())
assert {i['id'] for i in matrix}=={i['id'] for i in items if i['kind']=='exercise'}
curriculum=json.loads((ROOT/'project/curriculum-map.json').read_text())
assert not curriculum['missing_links']
for r in curriculum['requirements']:
    assert r['teaching_items'] and r['teaching_sections']
    assert set(r['teaching_items']+r['exercises']+r['worked_examples']+[a['id'] for a in r['assessment']])<=ids
for f in ['ds1-analyse','ds2-algebre','ds3-geometrie','ds4-donnees','sujet-a','sujet-b']:
    f=next(ROOT.rglob(f+'.tex'));s=re.sub(r'\\begin\{corrige\}.*?\\end\{corrige\}','',f.read_text(),flags=re.S)
    assert sum(map(int,re.findall(r'\\bareme\{(\d+) points\}',s)))==20
print(json.dumps({'inventory_items':len(items),'exercise_correction_pairs':len(matrix),
      'curriculum_rows':len(curriculum['requirements']),'unique_tex_labels':len(labels),
      'references_resolved':len(references),'assessment_totals':[20]*6,
      'checker_sha256':hashlib.sha256((ROOT/'scripts/check_gates.py').read_bytes()).hexdigest()},indent=2))
