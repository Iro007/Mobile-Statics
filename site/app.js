(() => {
  const phones = window.PHONES || [];
  const $ = (id) => document.getElementById(id);
  const colors = { coral: '#e96850', gold: '#e9a642', slate: '#50605d', grid: '#e9e7df', text: '#737973' };
  let lang = 'es';
  let filtered = phones.slice();
  const copy = {
    es: {navAnalysis:'Explorar datos',navMethod:'Método',heroLabel:'Una lectura estadística del mercado móvil',heroTitle:'¿Cuánto cuesta<br>un gigahercio?',heroSub:'Exploramos 865 teléfonos y ponemos a prueba una pregunta sencilla: ¿los procesadores más rápidos se asocian con precios más altos?',byline:'Ignacio Rosales + Miguel Sanz <span class="muted">· Estadística II</span>',scroll:'Ver qué encontramos',statPhones:'teléfonos analizados',statCases:'casos completos en la regresión',statR:'correlación de Pearson',statNote:'Una asociación interesante. Un modelo que exige cautela.',findEyebrow:'EL HALLAZGO',findTitle:'La señal está ahí.<br>La historia es más compleja.',finding1Title:'Más GHz, mayor precio asociado',finding1Text:'Observamos una asociación positiva moderada (r = 0,594) entre la frecuencia del procesador y el precio. El resultado describe estos datos; no demuestra que la frecuencia, por sí sola, cause el precio.',finding2Title:'Un tercio de la variación',finding2Text:'La recta resume el 35,2 % de la variabilidad observada en el precio. El 64,8 % restante queda fuera de este modelo de una sola variable.',finding3Title:'La limitación también es un resultado',finding3Text:'El informe reporta que los residuos no cumplen normalidad ni homocedasticidad. Por eso esta recta sirve para explorar la asociación, pero no para hacer predicciones confiables.',finding3Badge:'USAR CON CAUTELA',analysisEyebrow:'EXPLORA EL CONJUNTO',analysisTitle:'Los datos, en tus manos.',analysisSub:'Filtra el catálogo y compara las características principales. El precio está expresado en dólares según la base procesada.',filterPrice:'Precio máximo',filterRating:'Calificación mínima',showing:'modelos visibles',download:'Descargar CSV',chartScatterTag:'ASOCIACIÓN',scatterTitle:'Velocidad y precio',scatterNote:'Cada punto es un modelo. La curva punteada muestra una tendencia suavizada, no una predicción del precio individual.',distTitle:'Rango de precios',distNote:'La distribución es asimétrica; unos pocos modelos premium elevan el extremo superior.',compareTag:'COMPARACIÓN',compareTitle:'RAM y precio',compareNote:'La mediana ayuda a comparar grupos sin dejar que los precios extremos dominen el resumen.',tableTitle:'Modelos del catálogo',rows:'filas',thModel:'MODELO',thPrice:'PRECIO',thRam:'RAM',thBattery:'BATERÍA',thRating:'RATING',methodEyebrow:'CÓMO LO HICIMOS',methodTitle:'De una tabla cruda<br>a una pregunta clara.',methodText:'El proyecto partió de un catálogo de teléfonos recopilado desde la web. Limpiamos y transformamos variables, exploramos las especificaciones y ajustamos una regresión lineal simple entre GHz del procesador y precio.',repoLink:'Ver código y materiales',step1Title:'Recolección y limpieza',step1Text:'Catálogo web de teléfonos · 865 filas procesadas',step2Title:'Exploración descriptiva',step2Text:'Frecuencias, distribuciones y relaciones entre especificaciones',step3Title:'Regresión lineal simple',step3Text:'Precio ~ frecuencia del procesador · 787 observaciones completas',step4Title:'Revisión de supuestos',step4Text:'Normalidad y varianza de residuos: límites documentados en el informe',closingEyebrow:'LO QUE NOS DEJÓ',closingTitle:'Un buen análisis también<br>sabe dónde detenerse.',closingText:'La estadística aplicada no consiste solo en encontrar una relación. También implica comprobar si el modelo aguanta y comunicar qué no puede responder.',footerText:'Trabajo académico · Estadística II · UCV · 2025',xAxisGHz:'Frecuencia (GHz)',yAxisPrice:'Precio (USD)',models:'modelos',medianPrice:'Mediana',rowLabel:'filas',downloadName:'mobile-statics-datos-limpios.csv'},
    en: {navAnalysis:'Explore data',navMethod:'Method',heroLabel:'A statistical look at the mobile market',heroTitle:'What does one<br>gigahertz cost?',heroSub:'We explored 865 phones and tested a simple question: are faster processors associated with higher prices?',byline:'Ignacio Rosales + Miguel Sanz <span class="muted">· Statistics II</span>',scroll:'See what we found',statPhones:'phones analyzed',statCases:'complete regression cases',statR:'Pearson correlation',statNote:'An interesting association. A model that calls for caution.',findEyebrow:'THE FINDING',findTitle:'The signal is there.<br>The story is more complex.',finding1Title:'More GHz, higher associated price',finding1Text:'We observe a moderate positive association (r = 0.594) between processor frequency and price. This describes these data; it does not show that frequency alone causes a higher price.',finding2Title:'One third of price variation',finding2Text:'The line summarizes 35.2% of the observed price variation. The remaining 64.8% falls outside this one-variable model.',finding3Title:'A limitation is a finding too',finding3Text:'The report states that residuals fail the normality and homoscedasticity assumptions. The line helps explore the association, but should not be used for reliable predictions.',finding3Badge:'USE WITH CAUTION',analysisEyebrow:'EXPLORE THE DATASET',analysisTitle:'Explore the data.',analysisSub:'Filter the catalog and compare key specifications. Prices are shown in US dollars as recorded in the processed dataset.',filterPrice:'Maximum price',filterRating:'Minimum rating',showing:'models shown',download:'Download CSV',chartScatterTag:'ASSOCIATION',scatterTitle:'Speed and price',scatterNote:'Each point is a phone model. The dotted curve shows a smoothed trend, not an individual price prediction.',distTitle:'Price range',distNote:'The distribution is skewed; a few premium models extend the upper tail.',compareTag:'COMPARISON',compareTitle:'RAM and price',compareNote:'The median compares groups without letting extreme prices dominate the summary.',tableTitle:'Catalog models',rows:'rows',thModel:'MODEL',thPrice:'PRICE',thRam:'RAM',thBattery:'BATTERY',thRating:'RATING',methodEyebrow:'HOW WE DID IT',methodTitle:'From a raw table<br>to a clear question.',methodText:'The project began with a web-collected phone catalog. We cleaned and transformed variables, explored specifications, and fitted a simple linear regression between processor GHz and price.',repoLink:'View code and materials',step1Title:'Collection and cleaning',step1Text:'Web phone catalog · 865 processed rows',step2Title:'Descriptive exploration',step2Text:'Frequencies, distributions, and relationships between specifications',step3Title:'Simple linear regression',step3Text:'Price ~ processor frequency · 787 complete observations',step4Title:'Assumption checks',step4Text:'Residual normality and variance: limits documented in the report',closingEyebrow:'WHAT WE LEARNED',closingTitle:'Good analysis also knows<br>when to stop.',closingText:'Applied statistics is not only about finding a relationship. It also means checking whether a model holds up and communicating what it cannot answer.',footerText:'Academic project · Statistics II · UCV · 2025',xAxisGHz:'Frequency (GHz)',yAxisPrice:'Price (USD)',models:'models',medianPrice:'Median',rowLabel:'rows',downloadName:'mobile-statics-clean-data.csv'}
  };
  Object.assign(copy.es, {
    heroSub:'Analizamos 865 registros de teléfonos para estudiar si la frecuencia del procesador se asocia con su precio.',
    finding3Text:'La revisión detectó residuos alejados de normalidad, heterocedasticidad y casos influyentes. El ajuste describe una asociación; no se ha validado como predictor de nuevos precios.',
    analysisSub:'Precios históricos convertidos con un factor ilustrativo de 0,012 USD/INR, sin fecha documentada. Los gráficos cambian con los filtros; las cifras del encabezado corresponden al estudio completo.',
    scatterNote:'Se muestran todos los pares completos seleccionados en escala lineal. La recta se recalcula con los filtros. Asociación no implica causalidad.',
    compareNote:'Cajas por RAM: se omiten valores superiores a 32 GB por problemas de extracción y grupos con menos de 5 casos. Son datos históricos, no especificaciones verificadas.',
    methodText:'Partimos de un conjunto de datos de Kaggle atribuido a Smartprix. El cuaderno eliminó 155 filas con datos faltantes, separó campos de texto y convirtió precios. De 865 registros, 78 no tienen GHz: la regresión utiliza 787 pares.',
    step1Title:'Origen y preparación',step1Text:'Kaggle / Smartprix · 1.020 filas → 865 tras excluir faltantes',
    reportLink:'Descargar informe revisado (PDF)',sourceLabel:'Datos históricos y procedencia',
    sourceText:'Trabajo original: marzo de 2025. Revisión: septiembre de 2026. El catálogo no representa el mercado actual; conserva un duplicado exacto. La web permite explorar, no recomendar compras.',
    reset:'Restablecer filtros',regressionLabel:'Ajuste de la selección',empty:'No hay modelos con estos filtros. Prueba otra selección.',
    plotError:'No se pudieron cargar los gráficos. Recarga la página; puedes consultar el informe y descargar los datos.',
    distributionTag:'DISTRIBUCIÓN',sampleTag:'MUESTRA',previewLabel:'Los 12 precios más bajos de la selección',
    heroLabel:'Una lectura estadística de un catálogo de móviles',thRam:'RAM registrada',download:'CSV filtrado'
  });
  Object.assign(copy.en, {
    heroSub:'We analyzed 865 phone records to study whether processor frequency is associated with price.',
    finding3Text:'The revision found non-normal residuals, heteroscedasticity, and influential observations. The fit describes an association; it has not been validated to predict new prices.',
    analysisSub:'Historical prices converted with an illustrative 0.012 USD/INR factor, with no documented date. Charts respond to filters; headline results describe the full study.',
    scatterNote:'All selected complete pairs are shown on a linear scale. The fitted line updates with the filters. Association does not imply causation.',
    compareNote:'RAM box plots omit values above 32 GB due to extraction issues and groups with fewer than 5 cases. These are historical records, not verified specifications.',
    methodText:'We used a Kaggle dataset attributed to Smartprix. The notebook removed 155 incomplete rows, split text fields, and converted prices. Of the 865 retained records, 78 lack GHz: the regression uses 787 pairs.',
    step1Title:'Source and preparation',step1Text:'Kaggle / Smartprix · 1,020 rows → 865 after missing-data exclusions',
    reportLink:'Download revised report (PDF, Spanish)',sourceLabel:'Historical data and provenance',
    sourceText:'Original project: March 2025. Revision: September 2026. This catalog does not represent today’s market and retains one exact duplicate. Use it to explore, not for shopping advice.',
    reset:'Reset filters',regressionLabel:'Fit for selected records',empty:'No models match these filters. Try another selection.',
    plotError:'Charts could not load. Reload the page; the report and downloadable data remain available.',
    distributionTag:'DISTRIBUTION',sampleTag:'SAMPLE',previewLabel:'The 12 lowest prices in the selection',
    heroLabel:'A statistical look at a mobile phone catalog',thRam:'Recorded RAM',download:'Filtered CSV'
  });
  const t = (key) => copy[lang][key] || copy.es[key] || key;
  const valid = (value) => typeof value === 'number' && Number.isFinite(value);
  const escapeHTML = (value) => String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function regress(data) {
    const n=data.length;if(n<2)return null;
    const mx=data.reduce((s,p)=>s+p.ghz,0)/n,my=data.reduce((s,p)=>s+p.price,0)/n;
    const sxx=data.reduce((s,p)=>s+(p.ghz-mx)**2,0),syy=data.reduce((s,p)=>s+(p.price-my)**2,0);
    const sxy=data.reduce((s,p)=>s+(p.ghz-mx)*(p.price-my),0);
    if(sxx===0||syy===0)return null;
    const slope=sxy/sxx;return {n,slope,intercept:my-slope*mx,r:sxy/Math.sqrt(sxx*syy),r2:sxy*sxy/(sxx*syy),cov:sxy/(n-1)};
  }
  const money = (n) => '$' + Math.round(n).toLocaleString(lang === 'es' ? 'es-VE' : 'en-US');
  const layout = (xTitle, yTitle, extra={}) => ({ autosize:true, margin:{l:54,r:16,t:9,b:46}, paper_bgcolor:'transparent', plot_bgcolor:'transparent', font:{family:'DM Sans, sans-serif',size:10,color:colors.text}, xaxis:{title:{text:xTitle,font:{size:10}},gridcolor:colors.grid,zerolinecolor:colors.grid,linecolor:colors.grid,tickfont:{size:9}}, yaxis:{title:{text:yTitle,font:{size:10}},gridcolor:colors.grid,zerolinecolor:colors.grid,linecolor:colors.grid,tickfont:{size:9}}, showlegend:false, ...extra });
  function sample(data, max=700) { if(data.length<=max)return data; const step=data.length/max; return Array.from({length:max},(_,i)=>data[Math.floor(i*step)]); }
  function updateCharts() {
    const good = filtered.filter(p=>valid(p.price));
    const pair = good.filter(p=>valid(p.ghz));
    const points=pair,model=regress(pair);
    const fmt=(v,k=3)=>v.toLocaleString(lang==='es'?'es-VE':'en-US',{minimumFractionDigits:k,maximumFractionDigits:k});
    $('regressionStats').textContent=model?`${t('regressionLabel')} · n = ${model.n} · r = ${fmt(model.r)} · R² = ${fmt(model.r2*100,1)} % · Cov = ${fmt(model.cov)} GHz·USD`:`${t('regressionLabel')} · n = ${pair.length} · —`;
    $('plotError').hidden=!!window.Plotly;
    if (!window.Plotly) return;
    const tracesScatter=[{x:points.map(p=>p.ghz),y:points.map(p=>p.price),text:points.map(p=>p.name),mode:'markers',type:'scatter',hovertemplate:'%{text}<br>GHz: %{x:.2f}<br>USD: $%{y:,.2f}<extra></extra>',marker:{size:6,color:colors.gold,opacity:.6}}];
    if(model){const xx=[Math.min(...pair.map(p=>p.ghz)),Math.max(...pair.map(p=>p.ghz))];tracesScatter.push({x:xx,y:xx.map(x=>model.intercept+model.slope*x),mode:'lines',type:'scatter',line:{color:colors.coral,width:2},hoverinfo:'skip'});}
    Plotly.react('scatter',tracesScatter,layout(t('xAxisGHz'),t('yAxisPrice'),{yaxis:{title:{text:t('yAxisPrice'),font:{size:10}},gridcolor:colors.grid,type:'linear',tickprefix:'$',tickformat:',.0f'},xaxis:{title:{text:t('xAxisGHz'),font:{size:10}},gridcolor:colors.grid,range:[1.5,3.9],dtick:.5}}),{responsive:true,displayModeBar:false});
    const vals=good.map(p=>+p.price).filter(Number.isFinite);
    Plotly.react('priceDist',[{x:vals,type:'histogram',nbinsx:26,marker:{color:colors.coral,line:{width:1,color:'#fbfaf7'}},hovertemplate:'$%{x:,.0f}<br>%{y} '+t('models')+'<extra></extra>'}],layout(t('yAxisPrice'),t('models'),{xaxis:{title:{text:t('yAxisPrice'),font:{size:10}},gridcolor:colors.grid,tickprefix:'$',tickformat:',.0f'},yaxis:{title:{text:t('models'),font:{size:10}},gridcolor:colors.grid}}),{responsive:true,displayModeBar:false});
    const groups=new Map();
    good.forEach(p=>{if(!valid(p.ram))return;const r=Math.round(p.ram);if(r>32)return;if(!groups.has(r))groups.set(r,[]);groups.get(r).push(p.price)});
    const ram=[...groups.entries()].sort((a,b)=>a[0]-b[0]).filter(x=>x[1].length>=5);
    const traces=ram.map(([r,v])=>({y:v,x:Array(v.length).fill(r+' GB'),type:'box',name:r+' GB',boxpoints:false,fillcolor:'#e9a64233',line:{color:colors.slate,width:1.5},marker:{color:colors.coral}}));
    Plotly.react('ram',traces,layout('RAM',t('yAxisPrice'),{showlegend:false,yaxis:{title:{text:t('yAxisPrice'),font:{size:10}},gridcolor:colors.grid,tickprefix:'$',tickformat:',.0f'},xaxis:{title:{text:'RAM',font:{size:10}},gridcolor:colors.grid}}),{responsive:true,displayModeBar:false});
  }
  function updateTable() {
    const rows=filtered.slice().sort((a,b)=>(+a.price)-(+b.price)).slice(0,12);
    $('phones').innerHTML=rows.length?rows.map(p=>`<tr><td title="${escapeHTML(p.name)}">${escapeHTML(p.name)}</td><td>${money(p.price)}</td><td>${valid(p.ghz)?p.ghz.toFixed(2):'—'}</td><td>${valid(p.ram)?p.ram.toLocaleString()+' GB':'—'}</td><td>${valid(p.battery)?Math.round(p.battery).toLocaleString()+' mAh':'—'}</td><td>${valid(p.rating)?p.rating.toFixed(2):'—'}</td></tr>`).join(''):`<tr><td colspan="6">${t('empty')}</td></tr>`;
    $('tableCount').textContent=`${rows.length} / ${filtered.length} · ${t('previewLabel')}`;
  }
  function update() {
    const cap=+$('priceFilter').value, rating=+$('ratingFilter').value;
    $('priceOut').textContent=money(cap); $('ratingOut').textContent=rating.toFixed(1).replace('.',lang==='es'?',':'.');
    filtered=phones.filter(p=>+p.price<=cap && +p.rating>=rating);
    $('count').textContent=filtered.length.toLocaleString(lang==='es'?'es-VE':'en-US');
    updateCharts(); updateTable();
  }
  function setLang(next) {
    lang=next; document.documentElement.lang=lang; $('language').textContent=lang==='es'?'EN':'ES';
    document.querySelectorAll('[data-i18n]').forEach(el=>{const value=t(el.dataset.i18n);if(value.includes('<'))el.innerHTML=value;else el.textContent=value;});
    update();
  }
  $('priceFilter').addEventListener('input',update); $('ratingFilter').addEventListener('input',update);
  $('language').addEventListener('click',()=>setLang(lang==='es'?'en':'es'));
  $('resetFilters').addEventListener('click',()=>{$('priceFilter').value='5760';$('ratingFilter').value='3.4';update();});
  $('download').addEventListener('click',()=>{
    const cols=[['name','Modelo'],['price','Precio_USD'],['ghz','GHz_Procesador'],['rating','Calificacion'],['ram','RAM_GB'],['storage','Memoria_GB'],['battery','Bateria_mAh'],['charge','Carga_W'],['score','Puntaje_Especs'],['processor','Procesador']];
    const esc=(v)=>{let s=v==null?'':String(v);if(typeof v==='string'&&/^[=+@-]/.test(s))s="'"+s;return /[",\n]/.test(s)?'"'+s.replaceAll('"','""')+'"':s;};
    const csv='\ufeff'+cols.map(c=>esc(c[1])).join(',')+'\r\n'+filtered.map(p=>cols.map(c=>esc(p[c[0]])).join(',')).join('\r\n');
    const url=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download=t('downloadName');a.click();URL.revokeObjectURL(url);
  });
  setLang('es');
})();
