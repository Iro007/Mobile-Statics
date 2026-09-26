"""Genera la fuente LaTeX autónoma y PDF alternativo con idéntico contenido.
El PDF alternativo permite revisar el documento si el compilador integrado falla.
"""
from pathlib import Path
import json, re, sys, html, io
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
from PIL import Image as PILImage

ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent
DEST=ROOT.parents[1]/'02_Academico'/'Estadistica-y-Probabilidad'/'Trabajo estadistica 2'
ASSETS=HERE/'figuras';ASSETS.mkdir(exist_ok=True)
TMP=ROOT/'tmp'/'revision_pdf';TMP.mkdir(parents=True,exist_ok=True)
R=json.loads((HERE/'resultados.json').read_text(encoding='utf-8'))
D=pd.read_csv(HERE/'pares_y_diagnosticos.csv')
import reportlab
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

for name,file in [('TimesAPA','times.ttf'),('TimesAPA-Bold','timesbd.ttf'),('TimesAPA-Italic','timesi.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
plt.rcParams.update({'font.family':'serif','font.serif':['Times New Roman'],'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.2,'savefig.dpi':300})

def num(v,k=3):return f'{v:,.{k}f}'.replace(',','X').replace('.',',').replace('X','.')
def pv(v):return '< 0,001' if v<.001 else '= '+num(v,3)
def esc(s):
 s=str(s)
 for old,new in [('\\',r'\textbackslash{}'),('&',r'\&'),('%',r'\%'),('$',r'\$'),('#',r'\#'),('_',r'\_')]:s=s.replace(old,new)
 return s.replace('²',r'\textsuperscript{2}').replace('≈',r'$\approx$').replace('≤',r'$\leq$').replace('−','-').replace('β',r'$\beta$').replace('α',r'$\alpha$').replace('≥',r'$\geq$')
def coords(x,y):return ' '.join(f'({float(a):.7g},{float(b):.7g})' for a,b in zip(x,y))

# Gráficos completos, sin muestreo de puntos.
PLOTS={}
def finish_plot(key,fig,tex):
 fig.tight_layout();fig.savefig(ASSETS/(key+'.png'));fig.savefig(ASSETS/(key+'.pdf'));plt.close(fig);PLOTS[key]=tex
axis=r'width=\linewidth,height=7cm,tick label style={font=\small},label style={font=\small},grid=major,major grid style={gray!20},scaled ticks=false,ticklabel style={/pgf/number format/fixed},unbounded coords=jump'
points=coords(D.x,D.y)
lineX=np.array([D.x.min(),D.x.max()]);lineY=R['params']['const']+R['params']['x']*lineX
fig,ax=plt.subplots(figsize=(6.5,3.3));ax.scatter(D.x,D.y,s=13,alpha=.55,color='#315b76',edgecolors='none');ax.plot(lineX,lineY,color='#973a29',lw=1.8);ax.set(xlabel='Frecuencia del procesador (GHz)',ylabel='Precio convertido (USD)')
finish_plot('dispersion',fig,r'\begin{tikzpicture}\begin{axis}['+axis+r',xlabel={Frecuencia (GHz)},ylabel={Precio (USD)}]\addplot[only marks,mark size=1pt,blue!50!black,opacity=.55] coordinates {'+points+r'};\addplot[red!60!black,thick] coordinates {'+coords(lineX,lineY)+r'};\end{axis}\end{tikzpicture}')
fig,ax=plt.subplots(figsize=(6.5,3.3));ax.scatter(D.ajuste,D.residuo,s=13,alpha=.55,color='#315b76',edgecolors='none');ax.axhline(0,color='black',lw=1);ax.set(xlabel='Precio ajustado (USD)',ylabel='Residuo (USD)')
finish_plot('residuos',fig,r'\begin{tikzpicture}\begin{axis}['+axis+r',xlabel={Precio ajustado (USD)},ylabel={Residuo (USD)}]\addplot[only marks,mark size=1pt,blue!50!black,opacity=.55] coordinates {'+coords(D.ajuste,D.residuo)+r'};\addplot[black] coordinates {'+coords([D.ajuste.min(),D.ajuste.max()],[0,0])+r'};\end{axis}\end{tikzpicture}')
qq,fit=stats.probplot(D.residuo,dist='norm');qx,qy=qq
fig,ax=plt.subplots(figsize=(6.5,3.3));ax.scatter(qx,qy,s=13,alpha=.6,color='#315b76');ax.plot(qx,fit[0]*qx+fit[1],color='#973a29');ax.set(xlabel='Cuantiles normales teóricos',ylabel='Residuos ordenados (USD)')
finish_plot('qq',fig,r'\begin{tikzpicture}\begin{axis}['+axis+r',xlabel={Cuantiles normales teóricos},ylabel={Residuos (USD)}]\addplot[only marks,mark size=1pt,blue!50!black] coordinates {'+coords(qx,qy)+r'};\addplot[red!60!black] coordinates {'+coords(qx[[0,-1]],(fit[0]*qx+fit[1])[[0,-1]])+r'};\end{axis}\end{tikzpicture}')

B=[]
def page(title=None):
 B.append(('page',None))
 if title:B.append(('h1',title))
def p(text):B.append(('p',text))
def h(text):B.append(('h2',text))
def eq(tex):B.append(('eq',tex))
def table(title,headers,rows,note='',widths=None):B.append(('table',(title,headers,rows,note,widths)))
def figure(title,key,note):B.append(('figure',(title,key,note)))
def ref(text,url=None):B.append(('ref',(text,url)))

# El contenido se mantiene separado del maquetador para facilitar revisiones.
exec((HERE/'contenido.py').read_text(encoding='utf-8'),globals())

PRE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[spanish,es-nodecimaldot]{babel}
\usepackage[margin=1in,headheight=15pt]{geometry}
\usepackage{mathptmx,amsmath,amssymb,booktabs,array,setspace,fancyhdr,ragged2e,titlesec,caption,pgfplots,tikz,hyperref}
\pgfplotsset{compat=1.18}
\hypersetup{hidelinks,pdftitle={Frecuencia del procesador y precio de teléfonos: edición revisada},pdfauthor={Ignacio A. Rosales y Miguel A. Sanz}}
\pagestyle{fancy}\fancyhf{}\fancyhead[R]{\thepage}\renewcommand{\headrulewidth}{0pt}
\doublespacing\setlength{\parindent}{0.5in}\setlength{\parskip}{0pt}
\titleformat{\section}{\normalfont\bfseries\centering}{}{0pt}{}
\titleformat{\subsection}{\normalfont\bfseries}{}{0pt}{}
\titlespacing*{\section}{0pt}{0pt}{0pt}\titlespacing*{\subsection}{0pt}{0pt}{0pt}
\captionsetup{labelfont=bf,textfont=it,labelsep=newline,justification=raggedright,singlelinecheck=false}
\setlength{\emergencystretch}{2em}
\begin{document}
\RaggedRight\setlength{\parindent}{0.5in}
\begin{center}
\vspace*{0.8in}
\textbf{Frecuencia del procesador y precio de teléfonos móviles:\\análisis de covarianza y regresión lineal simple}

\vspace{\baselineskip}
Ignacio A. Rosales y Miguel A. Sanz\\
Universidad Central de Venezuela\\
Facultad de Ciencias Económicas y Sociales\\
Escuela de Estadística y Ciencias Actuariales\\
Estadística II\\
Profesora Sandra Pinto\\
Caracas, marzo de 2025

\vspace{\baselineskip}
Edición revisada: 26 de septiembre de 2026
\end{center}
'''
latex=[PRE]
pdf=[]
styles={
 'p':ParagraphStyle('p',fontName='TimesAPA',fontSize=12,leading=24,firstLineIndent=36,spaceAfter=0,alignment=TA_LEFT),
 'abstract':ParagraphStyle('abstract',fontName='TimesAPA',fontSize=12,leading=24,firstLineIndent=0,spaceAfter=0,alignment=TA_LEFT),
 'h1':ParagraphStyle('h1',fontName='TimesAPA-Bold',fontSize=12,leading=24,alignment=TA_CENTER,spaceAfter=12,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='TimesAPA-Bold',fontSize=12,leading=24,spaceBefore=0,spaceAfter=0,keepWithNext=True),
 'small':ParagraphStyle('small',fontName='TimesAPA',fontSize=10,leading=13),
 'title':ParagraphStyle('title',fontName='TimesAPA-Bold',fontSize=12,leading=24,alignment=TA_CENTER),
 'center':ParagraphStyle('center',fontName='TimesAPA',fontSize=12,leading=24,alignment=TA_CENTER),
 'ref':ParagraphStyle('ref',fontName='TimesAPA',fontSize=12,leading=24,leftIndent=36,firstLineIndent=-36),
 'cap':ParagraphStyle('cap',fontName='TimesAPA-Italic',fontSize=12,leading=20,spaceAfter=7),
 'bold':ParagraphStyle('bold',fontName='TimesAPA-Bold',fontSize=12,leading=20),
}
def para(s,style='p'):return Paragraph(html.escape(s),styles[style])
pdf.extend([Spacer(1,58),para('Frecuencia del procesador y precio de teléfonos móviles: análisis de covarianza y regresión lineal simple','title'),Spacer(1,24)])
for line in ['Ignacio A. Rosales y Miguel A. Sanz','Universidad Central de Venezuela','Facultad de Ciencias Económicas y Sociales','Escuela de Estadística y Ciencias Actuariales','Estadística II','Profesora Sandra Pinto','Caracas, marzo de 2025']:pdf.append(para(line,'center'))
pdf.extend([Spacer(1,24),para('Edición revisada: 26 de septiembre de 2026','center')])
tn=fn=en=0
abstract_pending=False
ref_titles=['A step-by-step guide for creating and formatting APA Style student papers','Least squares','Análisis de regresión lineal simple entre los GHz del procesador y el precio','Latest Uncleaned Mobile Dataset (2024)','OLSResults.HC3_se','statsmodels.stats.diagnostic.het_breuschpagan','scipy.stats.shapiro']
for kind,val in B:
 if kind=='page':latex.append(r'\clearpage');pdf.append(PageBreak())
 elif kind in ('h1','h2'):
  latex.append(('\\section*{' if kind=='h1' else '\\subsection*{')+esc(val)+'}');pdf.append(para(val,kind))
  abstract_pending=(kind=='h1' and val=='Resumen')
 elif kind=='p':
  latex.append((r'\noindent ' if abstract_pending else '')+esc(val)+'\n');pdf.append(para(val,'abstract' if abstract_pending else 'p'));abstract_pending=False
 elif kind=='eq':
  en+=1;latex.append(r'\begin{equation*}'+val+r'\end{equation*}')
  fig=plt.figure(figsize=(6.5,.48));fig.text(.5,.5,'$'+val+'$',ha='center',va='center',fontsize=13);path=TMP/f'eq{en}.png';fig.savefig(path,dpi=240,bbox_inches='tight',pad_inches=.08);plt.close(fig)
  with PILImage.open(path) as im:w0,h0=im.size
  w=min(465,w0*72/240);pdf.extend([Spacer(1,5),Image(str(path),width=w,height=h0*w/w0),Spacer(1,5)])
 elif kind=='table':
  tn+=1;title,headers,rows,note,widths=val
  ncol=len(headers);widths=widths or [468/ncol]*ncol
  latex.append(r'\begin{center}\begin{minipage}{\linewidth}\textbf{Tabla '+str(tn)+r'}\\\textit{'+esc(title)+r'}\\\begin{singlespace}\small')
  latex.append(r'\begin{tabular}{@{}'+''.join(f'p{{{(w-12)/468:.4f}\\linewidth}}' for w in widths)+r'@{}}\toprule')
  latex.append(' & '.join(r'\textbf{'+esc(v)+'}' for v in headers)+r'\\\midrule')
  latex.extend(' & '.join(esc(v) for v in row)+r'\\' for row in rows)
  latex.append(r'\bottomrule\end{tabular}\end{singlespace}')
  if note:latex.append(r'\small\textit{Nota.} '+esc(note))
  latex.append(r'\end{minipage}\end{center}')
  group=[para(f'Tabla {tn}','bold'),para(title,'cap')]
  data=[[para(c,'small') for c in row] for row in [headers]+rows]
  tab=Table(data,colWidths=widths,hAlign='LEFT');tab.setStyle(TableStyle([('LINEABOVE',(0,0),(-1,0),.8,colors.black),('LINEBELOW',(0,0),(-1,0),.5,colors.black),('LINEBELOW',(0,-1),(-1,-1),.8,colors.black),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4)]));group.append(tab)
  if note:group.append(para('Nota. '+note,'small'))
  group.append(Spacer(1,12));pdf.append(KeepTogether(group))
 elif kind=='figure':
  fn+=1;title,key,note=val
  latex.append(r'\begin{center}\begin{minipage}{\linewidth}\textbf{Figura '+str(fn)+r'}\\\textit{'+esc(title)+r'}\par\begin{singlespace}'+PLOTS[key]+r'\end{singlespace}\small\textit{Nota.} '+esc(note)+r'\end{minipage}\end{center}')
  group=[para(f'Figura {fn}','bold'),para(title,'cap'),Image(str(ASSETS/(key+'.png')),width=468,height=468*3.3/6.5),para('Nota. '+note,'small'),Spacer(1,10)];pdf.append(KeepTogether(group))
 elif kind=='ref':
  text,url=val
  textext=esc(text);content=html.escape(text)
  for title in ref_titles:
   textext=textext.replace(esc(title),r'\textit{'+esc(title)+'}');content=content.replace(html.escape(title),'<font name="TimesAPA-Italic">'+html.escape(title)+'</font>')
  latex.append(r'{\setlength{\parindent}{-0.5in}\setlength{\leftskip}{0.5in}'+textext+(r' \url{'+url+'}' if url else '')+r'\par}')
  content+=(f' <link href="{html.escape(url)}">{html.escape(url)}</link>' if url else '')
  pdf.append(Paragraph(content,styles['ref']))
latex.append(r'\end{document}')
texpath=DEST/'Informe_Mobile_Statics_APA7.tex';texpath.write_text('\n'.join(latex),encoding='utf-8')
def footer(c,doc):
 c.saveState();c.setFont('TimesAPA',12);c.drawRightString(540,756,str(doc.page));c.restoreState()
pdfpath=DEST/'Informe_Mobile_Statics_APA7.pdf'
doc=SimpleDocTemplate(str(pdfpath),pagesize=(612,792),leftMargin=72,rightMargin=72,topMargin=72,bottomMargin=72,title='Frecuencia del procesador y precio de teléfonos: edición revisada',author='Ignacio A. Rosales y Miguel A. Sanz',subject='Revisión académica; composición alternativa a partir del mismo contenido de la fuente LaTeX')
doc.build(pdf,onFirstPage=footer,onLaterPages=footer)
(HERE/'contenido_revision.json').write_text(json.dumps(B,ensure_ascii=False,indent=2),encoding='utf-8')
print('Fuente:',texpath,'\nPDF:',pdfpath)
