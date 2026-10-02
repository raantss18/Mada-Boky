from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]/'Livres/T12-S'
(root/'build').mkdir(exist_ok=True)
main=(root/'livre-t12s.tex').read_text()
files=[root/(n+'.tex') for n in re.findall(r'^\\include\{(chapitres/[^}]+)\}',main,re.M)]
parts=[r'''\documentclass[11pt]{book}
\usepackage{preambule/bmt-style}
\usepackage{preambule/bmt-macros}
\usepackage{preambule/bmt-blocks}
\geometry{a4paper,left=1.5cm,right=1.5cm,top=1.5cm,bottom=1.5cm}
\pagestyle{empty}
\begin{document}
''']
items=[]
for f in files:
 s=f.read_text()
 s=re.sub(r'\\input\{(figures/[^}]+)\}',lambda m:(root/(m[1]+'.tex')).read_text(),s)
 for i,m in enumerate(re.finditer(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',s,re.S),1):
  name=f'{len(items)+1:02d} {f.stem} / {i}'
  items.append({'id':len(items)+1,'file':str(f.relative_to(root)),'figure':i})
  color='bmtVetiver' if 'geometrie' in str(f) else 'bmtRaphia' if 'donnees' in str(f) else 'bmtLaterite' if 'algebre' in str(f) else 'bmtIndigo'
  parts.append('\\bmtPartieCouleur{'+color+'}\n\\noindent '+name+'\\par\\bigskip\n\\begin{center}\n'+m.group()+'\n\\end{center}\\clearpage\n')
parts.append(r'''\noindent Accolades et indices\par\bigskip
\[A^n=\underbrace{A\times A\times\cdots\times A}_{n\text{ facteurs}}\]
\[e^{ax}\underbrace{[\varphi'(x)+a\varphi(x)]}_{=0}=0\]
\[\underbrace{1101}_{D}\quad\underbrace{0110}_{6}\quad\underset{x\to+\infty}{\lim} f(x)\]
\end{document}''')
(root/'build/graphics-proof.tex').write_text('\n'.join(parts))
import json
(root/'build/graphics-inventory.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
print(len(items),'figures')
