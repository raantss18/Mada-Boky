#!/usr/bin/env python3
"""Inventory TeX blocks, exercises, figures and prose; no semantic pass implied.

Run after source edits, then reconcile the generated list with the manuscript.
An item can contain several subquestions/claims, all within its recorded span.
The source hash permits detecting a changed item; ordinal IDs stay stable if the
block order is retained. The parser is deliberately conservative about prose.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = {'definition':'definition','propriete':'property','theoreme':'property',
         'demonstration':'proof','exemple':'example','corrige':'correction',
         'visualisation':'figure','revision':'claim','methode':'claim',
         'remarque':'claim','avertissement':'claim','erreurclassique':'claim',
         'notepourlaclasse':'section','devoir':'section'}
WRAPPERS = {'automatismes','situation','entrainement','jecherche','jemeteste','plusloin','annales'}

def sha(s): return hashlib.sha256(s.encode()).hexdigest()

def inventory_file(f):
    raw=f.read_text(); s=re.sub(r'(?m)(?<!\\)%.*$', lambda m:' '*len(m[0]), raw)
    prefix=(re.search(r'\\label\{(t11s-c\d+)\}',s) or [None,None])[1] or f.stem
    items=[]; spans=[]; counts={}
    def add(kind,start,end,identity=None,extra=None):
        counts[kind]=counts.get(kind,0)+1
        identity=identity or f'{prefix}-{kind}-{counts[kind]:03}'
        item={'id':identity,'kind':kind,'location':f'{f.relative_to(ROOT)}:{s.count(chr(10),0,start)+1}',
              'source_path':str(f.relative_to(ROOT)),'start_line':s.count('\n',0,start)+1,
              'end_line':s.count('\n',0,end)+1,'content_sha256':sha(raw[start:end]),
              'dependencies':[prefix] if identity!=prefix else []}
        if extra:item.update(extra)
        items.append(item); return item
    add('section',0,len(s),prefix,{'environment':'source-unit'})
    # Balanced environments, including figures inside teacher corrections.
    stack=[]; envs=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        action,name=m.groups()
        if action=='begin':stack.append((name,m.start()))
        else:
            if not stack or stack[-1][0]!=name:raise ValueError(f'{f}: mismatched {name}')
            _,start=stack.pop();envs.append((start,m.end(),name))
    if stack:raise ValueError(f'{f}: unclosed environments')
    for start,end,name in sorted(envs):
        if name in KINDS:
            kind=KINDS[name]; label=re.search(r'\\label\{([^}]+)\}',s[start:end])
            identity=label[1] if kind=='correction' and label else None
            add(kind,start,end,identity,{'environment':name});spans.append((start,end))
        elif name=='tikzpicture' and not any(a<=start<end<=b and n=='visualisation' for a,b,n in envs):
            add('figure',start,end,extra={'environment':name})
        elif name in WRAPPERS:
            block=s[start:end]
            if name in {'automatismes','jecherche','jemeteste'} and '\\exo' not in block and '\\item' in block:
                label=re.search(r'\\label\{([^}]+)\}',block)
                add('exercise',start,end,label[1] if label else None,{'correction_id':'sol-'+label[1] if label else None,'subquestions_included':True});spans.append((start,end))
            else:add('section',start,end,extra={'environment':name})
    for m in re.finditer(r'\\exo(?:\[[^\]]*\])?\s*\\label\{([^}]+)\}',s):
        start=m.start(); candidates=[len(s)]
        for x in re.finditer(r'\\exo(?:\[|\\label)|\\begin\{corrige\}|\\(?:sub)?section\*?\{|\\end\{(?:automatismes|situation|entrainement|jecherche|jemeteste|plusloin|annales)\}',s[m.end():]):
            candidates.append(m.end()+x.start());break
        end=min(candidates); add('exercise',start,end,m[1],{'correction_id':'sol-'+m[1],'subquestions_included':True});spans.append((start,end))
    for m in re.finditer(r'\\item\[([^]]+)\]([^\n]*)',s):
        if f.stem=='glossaire':
            add('definition',m.start(),m.end(),extra={'environment':'glossary-entry'});spans.append((m.start(),m.end()))
    for m in re.finditer(r'\\(?:sub)?section\*?\{[^}]*\}',s):
        add('section',m.start(),m.end());spans.append((m.start(),m.end()))
    # Every remaining prose paragraph is retained as an inline-claim group.
    chars=list(s)
    for a,b in spans:chars[a:b]=' '* (b-a)
    rest=''.join(chars)
    for m in re.finditer(r'[^\n]+(?:\n(?!\s*\n)[^\n]+)*',rest):
        block=m[0].strip()
        cleaned=re.sub(r'\\(?:label|phantomsection|setcounter|renewcommand|markboth|addcontentsline|input|bmtchapitre)\b.*','',block)
        if re.search(r'[A-Za-zÀ-ÿ]{3}',cleaned) and not all(x.strip().startswith('\\') for x in block.splitlines()):
            add('claim',m.start(),m.end(),extra={'environment':'inline-prose'})
    return items

files=sorted(list(ROOT.glob('chapitres/*/*.tex'))+list(ROOT.glob('annexes/*.tex'))+list(ROOT.glob('front/*.tex'))+[ROOT/'livre-t11s.tex'])
items=[]
for f in files:items.extend(inventory_file(f))
ids=[i['id'] for i in items]
assert len(ids)==len(set(ids)), 'Duplicate IDs'
for i in items:
    if i['kind']=='exercise':assert i['correction_id'] in ids, f'Missing correction: {i["id"]}'
(ROOT/'review/inventory.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
old=json.loads((ROOT/'project/exercise-matrix.json').read_text())
known={i['id']:i for i in old}; matrix=[]
for i in items:
    if i['kind']!='exercise':continue
    record=known.get(i['id'],{'id':i['id'],'title':i['id'],'origin':'original',
          'demand':'prerequisite recall' if i['id'].endswith('-auto') else 'formative reasoning'})
    record.update(correction_id=i['correction_id'],source_path=i['source_path'],subquestions_included=True)
    matrix.append(record)
(ROOT/'project/exercise-matrix.json').write_text(json.dumps(matrix,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'items':len(items),'exercises':len(matrix),
       'kinds':{k:sum(i['kind']==k for i in items) for k in sorted({i['kind'] for i in items})}},ensure_ascii=False))
