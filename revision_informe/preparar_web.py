"""Prepara los datos y materiales públicos desde la revisión local."""
from pathlib import Path
import json,shutil,re
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
academic=ROOT.parents[1]/'02_Academico/Estadistica-y-Probabilidad/Trabajo estadistica 2'
mapping={'Nombre':'name','Precio($)':'price','GHz_Procesador':'ghz','Calificación':'rating','RAM':'ram','Memoria':'storage','Capacidad_Batería_mAh':'battery','Velocidad_Carga_W':'charge','Puntaje_Especs':'score','Nombre_Procesador':'processor'}
d=pd.read_csv(ROOT/'telefono_Act.csv').rename(columns=mapping)[list(mapping.values())]
data=json.loads(d.to_json(orient='records',force_ascii=False))
(SITE/'data.js').write_text('window.PHONES = '+json.dumps(data,ensure_ascii=False,allow_nan=False,separators=(',',':'))+';\n',encoding='utf-8')
(SITE/'downloads').mkdir(exist_ok=True)
for ext in ['pdf','tex']:
 shutil.copy2(academic/f'Informe_Mobile_Statics_APA7.{ext}',SITE/'downloads'/f'informe-mobile-statics.{ext}')
shutil.copy2(ROOT/'revision_informe/resultados.json',SITE/'downloads/resultados.json')
(SITE/'.nojekyll').touch()

# El gráfico de portada utiliza todos los pares completos y la recta histórica.
pairs=d.dropna(subset=['price','ghz'])
sx=lambda x:55+(x-1.5)/2.4*445
sy=lambda y:430-y/6000*350
circles=''.join(f'<circle cx="{sx(r.ghz):.2f}" cy="{sy(r.price):.2f}" r="2.2"/>' for r in pairs.itertuples())
svg=f'''<svg viewBox="0 0 560 520" role="img" aria-label="787 pares completos: frecuencia del procesador y precio"><g stroke="#293239" stroke-opacity=".12" stroke-dasharray="3 7"><path d="M55 430H500M55 313H500M55 197H500M55 80H500"/></g><path d="M55 60V430H500" stroke="#293239" stroke-opacity=".4" fill="none"/><g fill="#b57d27" opacity=".55">{circles}</g><path d="M{sx(1.6):.2f} {sy(-780.914107+442.685089*1.6):.2f} L{sx(3.78):.2f} {sy(-780.914107+442.685089*3.78):.2f}" fill="none" stroke="#d25740" stroke-width="2"/><g font-size="11"><text x="55" y="468">1.5 GHz</text><text x="446" y="468">3.9 GHz</text><text x="20" y="435">0</text><text x="7" y="83">6000</text><text x="360" y="65">n = 787 · R² = 0.352</text><text x="70" y="80">USD</text></g></svg>'''
page=(SITE/'index.html').read_text(encoding='utf-8')
page=re.sub(r'<svg viewBox="0 0 560 520".*?</svg>',svg,page,flags=re.S)
page=page.replace('Gráfico decorativo de precio frente a velocidad de procesador','Datos históricos de precio frente a frecuencia del procesador')
page=page.replace('step="50" value="1500"','step="10" value="5760"').replace('step="0.1" value="3.5"','step="0.1" value="3.4"')
page=page.replace('02 / DISTRIBUCIÓN','02 / <span data-i18n="distributionTag">DISTRIBUCIÓN</span>').replace('04 / MUESTRA','04 / <span data-i18n="sampleTag">MUESTRA</span>')
if 'id="regressionStats"' not in page:
 page=page.replace('<div class="chart-grid">','<div class="selection-summary"><p id="regressionStats" aria-live="polite"></p><button class="download" id="resetFilters" data-i18n="reset">Restablecer filtros</button></div><p id="plotError" role="alert" data-i18n="plotError" hidden></p><div class="chart-grid">')
if 'id="materiales"' not in page:
 page=page.replace('<section class="closing">','''<section class="materials wrap" id="materiales"><h2 data-i18n="sourceLabel">Datos históricos y procedencia</h2><p data-i18n="sourceText">Trabajo original: marzo de 2025. Revisión: septiembre de 2026. El catálogo no representa el mercado actual.</p><div class="material-links"><a class="download primary" href="downloads/informe-mobile-statics.pdf" data-i18n="reportLink">Descargar informe revisado (PDF)</a><a href="downloads/informe-mobile-statics.tex" download>LaTeX ↓</a><a href="downloads/resultados.json" download>JSON ↓</a><a href="https://www.kaggle.com/datasets/santoshgupta01/uncleaned-mobile-dataset" target="_blank" rel="noreferrer">Kaggle ↗</a></div></section><section class="closing">''')
if 'property="og:title"' not in page:
 page=page.replace('</head>','''<link rel="canonical" href="https://iro007.github.io/Mobile-Statics/">
  <meta property="og:type" content="website"><meta property="og:locale" content="es_VE">
  <meta property="og:title" content="Mobile-Statics | ¿Qué explica el precio de un teléfono?">
  <meta property="og:description" content="Un proyecto de Ignacio Rosales y Miguel Sanz: explora datos, regresión y aprendizajes de Estadística II en la UCV.">
  <meta property="og:url" content="https://iro007.github.io/Mobile-Statics/">
  <meta property="og:image" content="https://iro007.github.io/Mobile-Statics/social-preview.png">
  <meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="865 registros, 787 pares completos; r = 0,594 y R² = 35,2 %. Ignacio Rosales y Miguel Sanz.">
  <meta name="twitter:card" content="summary_large_image">
  </head>''')
if '<noscript>' not in page:
 page=page.replace('<main>','<main><noscript><p class="wrap">Activa JavaScript para explorar los filtros. Puedes <a href="downloads/informe-mobile-statics.pdf">descargar el informe completo</a>.</p></noscript>')
(SITE/'index.html').write_text(page,encoding='utf-8')

# Tarjeta social de 1200 × 630 basada en el mismo gráfico estadístico.
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig=plt.figure(figsize=(12,6.3),dpi=100,facecolor='#f4f2ed')
fig.text(.055,.89,'MOBILE / STATICS',fontsize=17,fontweight='bold',color='#bc4e36')
fig.text(.055,.67,'¿Qué explica el precio\nde un teléfono?',fontsize=30,fontweight='bold',color='#252b2d',linespacing=1.3)
fig.text(.055,.48,'Un proyecto de Estadística II · UCV',fontsize=13,color='#626965')
fig.text(.055,.29,'865 registros  /  787 pares completos',fontsize=14,color='#252b2d')
fig.text(.055,.21,'r = 0,594    ·    R² = 35,2 %',fontsize=18,color='#bc4e36')
fig.text(.055,.095,'Ignacio Rosales + Miguel Sanz',fontsize=13,color='#252b2d')
ax=fig.add_axes([.60,.18,.36,.57],facecolor='#f4f2ed')
ax.scatter(pairs.ghz,pairs.price,s=10,alpha=.4,color='#9c7b3f',edgecolors='none')
ax.plot([1.6,3.78],[-780.914107+442.685089*1.6,-780.914107+442.685089*3.78],color='#d25740')
ax.set(xlabel='Frecuencia (GHz)',ylabel='Precio convertido (USD)')
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.savefig(SITE/'social-preview.png',dpi=100);plt.close(fig)
print('Datos públicos:',len(data),'pares:',len(pairs))
