from pathlib import Path
import re,json
import pymupdf as fitz
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT.parents[1]/'02_Academico'/'Estadistica-y-Probabilidad'/'Trabajo estadistica 2'
OUT=ROOT/'tmp'/'revision_pdf';OUT.mkdir(parents=True,exist_ok=True)
pdf=fitz.open(DEST/'Informe_Mobile_Statics_APA7.pdf')
original=fitz.open(DEST/'Trabajo Estadistica 2 Regresion lineal bivariante (1).pdf')
ids=set(re.findall(r'\b\d{7,9}\b',original[0].get_text()))
text='\n'.join(p.get_text() for p in pdf)
tex=(DEST/'Informe_Mobile_Statics_APA7.tex').read_text(encoding='utf-8')
assert all(x not in text+str(pdf.metadata)+tex for x in ids)
assert not any(ord(c)<32 and c not in '\n\r\t' for c in tex)
# Un control estático no equivale a compilar LaTeX.
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',tex):
 op,name=m.groups()
 if op=='begin':stack.append(name)
 else:assert stack.pop()==name,(name,stack)
assert not stack
outside=[]
for k,p in enumerate(pdf):
 p.get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(OUT/f'pagina-{k+1:02}.png')
 for b in p.get_text('dict')['blocks']:
  if 'lines' not in b:continue
  for l in b['lines']:
   x0,y0,x1,y1=l['bbox']
   if x0<70 or x1>542 or y1>722:outside.append((k+1,[x0,y0,x1,y1]))
for start in range(0,len(pdf),4):
 sheet=Image.new('RGB',(1256,1648),'#cfcfcf')
 for j in range(min(4,len(pdf)-start)):
  im=Image.open(OUT/f'pagina-{start+j+1:02}.png').convert('RGB');im.thumbnail((612,792))
  x=8+(j%2)*628;y=8+(j//2)*824;sheet.paste(im,(x,y));ImageDraw.Draw(sheet).text((x,y+795),f'Página {start+j+1}',fill='black')
 sheet.save(OUT/f'hoja-{start//4+1:02}.png')
summary={'paginas':len(pdf),'sin_cedulas':True,'latex_entornos_equilibrados':True,'lineas_fuera_margen':outside,'metadata':pdf.metadata}
(ROOT/'revision_informe'/'revision_pdf.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
