#!/usr/bin/env python3
"""Rebind reviewed PE rows to their exact teaching sections and current IDs.

This is a fixed semantic mapping recorded by the reviewer, not keyword-based
evidence of curriculum compliance. New requirements require a new source audit.
"""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
groups={1:{1:[1],3:[2,16,17],4:[3]},2:{0:[4],1:[5],2:[7]},3:{0:[6],1:[6],2:[6]},4:{0:[8,9,11],1:[10],2:[12]},5:{0:[15,18],1:[14],2:[13]},6:{0:[37,38,40],1:[39],2:[41]},7:{0:[34],1:[35],2:[34]},8:{0:[19],1:[20],2:[21,22],3:[23,24]},9:{0:[25],1:[25],2:[26]},10:{0:[29,30],1:[31,32],2:[33]},11:{0:[27,28],1:[27,28],2:[28]},12:{0:[42,43,44,45],1:[46,48],2:[47,48],3:[49,36]},13:{0:[50],1:[51],2:[51]},14:{0:[52,53],1:[55],2:[54,55,56]},15:{0:[57],1:[58],2:[59],3:[60]},16:{0:[67,68],1:[69],2:[70,71]},17:{0:[61,62],1:[63],2:[64,65,66]},18:{0:[79],1:[72,73],2:[74,75],3:[76,77,78]},19:{0:[80],1:[81],2:[82,83,84]},20:{0:[85],1:[86],2:[85],3:[87]}}
d=json.loads((ROOT/'project/curriculum-map.json').read_text())
inv=json.loads((ROOT/'review/inventory.json').read_text());ids={i['id'] for i in inv}
for r in d['requirements']:
    n=int(r['id'][-3:]);ch=int(r['exercises'][0][6:8])
    f=next(ROOT.glob(f'chapitres/*/ch{ch:02}-*.tex'));s=f.read_text()
    starts=[(m.start(),m[1]) for m in re.finditer(r'\\section\{([^}]+)\}',s)]
    headings=[starts[idx][1] for idx,reqs in groups[ch].items() if n in reqs]
    r['teaching_sections']=headings;selected=[]
    for i in inv:
        if i['source_path']!=str(f.relative_to(ROOT)) or i['kind'] not in ['definition','property','proof','example','claim','exercise']:continue
        at=sum(len(x)+1 for x in s.splitlines()[:i['start_line']-1])
        heading=next((h for pos,h in reversed(starts) if pos<=at),None)
        if heading in headings:selected.append(i['id'])
    r['teaching_items']=selected
    assert headings and selected,(r['id'],headings,selected)
    for i in r['exercises']+r['worked_examples']+[x['id'] for x in r['assessment']]:assert i in ids,i
    r['coverage']='passed'
(ROOT/'project/curriculum-map.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(f"{len(d['requirements'])} PE rows linked to actual teaching sections, worked corrections, and formative/summative tasks.")
