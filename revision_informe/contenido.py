# Ejecutado por editar_informe.py: contenido único para LaTeX y PDF de revisión.
page('Resumen')
p('Se revisó la relación entre la frecuencia del procesador y el precio de teléfonos móviles en el proyecto Mobile-Statics, desarrollado para Estadística II. La base original contiene 1.020 registros y 12 variables; la eliminación inicial de filas con valores faltantes deja 865 registros. La extracción de frecuencia produce 78 ausencias adicionales y el ajuste utiliza 787 pares completos. Los precios se convirtieron de rupias indias a dólares mediante el factor fijo 0,012 USD/INR consignado en el cuaderno, sin fuente ni fecha documentadas. Se estimaron covarianza, correlación de Pearson y regresión lineal simple por mínimos cuadrados. La covarianza muestral fue 93,089 GHz·USD, la correlación 0,594 y el coeficiente de determinación 0,352. La pendiente estimada fue 442,685 USD/GHz. La revisión de los residuos mostró desviaciones de normalidad, evidencia de heterocedasticidad y señales de especificación funcional insuficiente. El análisis de sensibilidad identificó influencia de observaciones extremas, mientras que retirar el único duplicado exacto apenas alteró el ajuste. Se concluye que existe una asociación descriptiva positiva en el catálogo analizado, con limitaciones para la inferencia poblacional y la predicción de precios individuales. La edición incorpora el desarrollo de la covarianza, corrige los intervalos del trabajo original y documenta un procedimiento reproducible sin modificar los datos históricos.')
p('Palabras clave: covarianza, regresión lineal simple, teléfonos móviles, frecuencia del procesador, calidad de datos.')
p('Nota de la edición. El estudio se presentó en marzo de 2025. Esta revisión, fechada el 26 de septiembre de 2026, conserva la autoría y la muestra histórica, recalcula el análisis e identifica las correcciones. No actualiza el catálogo al mercado de 2026.')

page('Introducción y objetivos')
p('El precio de un teléfono reúne características técnicas, posicionamiento de marca, configuración, disponibilidad y condiciones comerciales. La frecuencia del procesador, expresada en gigahercios (GHz), es una característica observable que permite formular una pregunta concreta: ¿qué asociación existe entre la frecuencia registrada y el precio dentro de este catálogo? La frecuencia mide ciclos por segundo; no constituye una medida completa del rendimiento ni permite comparar arquitecturas como si fueran equivalentes.')
p('Ignacio A. Rosales y Miguel A. Sanz abordaron esta pregunta mediante un análisis bivariante para Estadística II en la Universidad Central de Venezuela. La revisión conserva ese objetivo y amplía su trazabilidad: documenta cómo se preparó la base, desarrolla la covarianza omitida y distingue el ajuste descriptivo de la validez de sus procedimientos inferenciales.')
h('Objetivo general')
p('Cuantificar e interpretar la asociación entre GHz del procesador y precio convertido a USD, evaluando la adecuación y las limitaciones de una regresión lineal simple en la muestra histórica.')
h('Objetivos específicos')
p('Reconstruir la preparación de las variables; estimar covarianza y correlación sobre los mismos casos; reproducir coeficientes, ANOVA e intervalos; examinar los residuos y los casos influyentes; y comunicar resultados reproducibles con sus límites. No se busca establecer un efecto causal ni recomendar compras actuales.')

page('Fundamentos estadísticos')
p('La covarianza resume si dos variables tienden a apartarse de sus medias en el mismo sentido. Se emplea el divisor n − 1 para la estimación muestral. Su magnitud depende de las unidades: cambiar la moneda modifica la covarianza, aunque una conversión lineal positiva no modifica Pearson ni R². La insesgadez usual del estimador presupone un marco de observaciones independientes e idénticamente distribuidas; aquí no se acredita un muestreo probabilístico.')
eq(r's_{XY}=\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{n-1}')
p('Pearson estandariza esa covariación mediante las desviaciones típicas muestrales. Su signo indica el sentido de la asociación lineal y su valor está comprendido entre −1 y 1. Una asociación estadística no identifica una causa.')
eq(r'r=\frac{s_{XY}}{s_Xs_Y}')
p('El modelo lineal simple expresa el precio como una función afín de la frecuencia más un error. Mínimos cuadrados elige los coeficientes que minimizan la suma de residuos al cuadrado (National Institute of Standards and Technology [NIST], s. f.).')
eq(r'Y_i=\beta_0+\beta_1x_i+\varepsilon_i,\qquad \widehat{\beta}_1=\frac{s_{XY}}{s_X^2}')
p('La normalidad no es necesaria para calcular la recta. Sí interviene, junto con otros supuestos, en la justificación exacta de los intervalos y contrastes clásicos. El tamaño muestral por sí solo no corrige heterocedasticidad, dependencia ni errores de especificación.')

page('Método: procedencia y diseño')
p('El estudio es observacional y utiliza un catálogo disponible, sin selección aleatoria documentada. La unidad de registro es una entrada comercial de teléfono o configuración; no necesariamente un modelo único. No se registran ventas, compradores ni mediciones experimentales de rendimiento. Por ello, las conclusiones se restringen al conjunto disponible.')
p('El README histórico identifica como fuente el conjunto Latest Uncleaned Mobile Dataset (2024), publicado por santoshgupta01 en Kaggle (s. f.). Los materiales de extracción incluidos en el repositorio apuntan a la sección de móviles de Smartprix. Se distingue la procedencia declarada de la ejecución acreditada: disponer de esos scripts no demuestra que los autores hayan realizado la recolección original ni establece la fecha de cada precio.')
p('Los archivos de referencia son mobiles.csv, con 1.020 filas y 12 columnas, app.ipynb, que contiene la preparación, y telefono_Act.csv, con 865 filas y 24 columnas derivadas. El nombre de la publicación en Kaggle incluye 2024; esto no prueba que todas las observaciones correspondan a una misma fecha ni que el archivo local sea idéntico a la versión actualmente publicada.')
p('No se incorporaron datos nuevos. La revisión compara los archivos locales y conserva sus huellas SHA-256 en resultados.json. La reproducción de las variables centrales utiliza el archivo bruto y contrasta sus resultados contra la tabla procesada. Las cifras históricas se cotejan con el informe de Rosales y Sanz (2025).')

page('Preparación de la base de datos')
p('La Tabla 1 resume las etapas y sus tamaños, distinguiendo la selección inicial de la exclusión específica del modelo.')
table('Reconstrucción de la muestra',['Etapa','Operación','Filas'],[
 ['Base original','Lectura de 12 columnas','1.020'],
 ['Selección inicial','Eliminar filas con cualquier valor faltante','865'],
 ['Tabla procesada','Separar campos y convertir unidades; 24 columnas','865'],
 ['Muestra del modelo','Excluir ausencia de GHz; precio disponible en todos','787']],
 'Las 155 exclusiones iniciales contienen puntaje de especificaciones ausente. Los otros faltantes originales se solapan con esas filas; no se suman otra vez.',[105,305,58])
p('La celda de eliminación general del cuaderno equivale a dropna(). Al repetirla, se obtienen exactamente los mismos 865 nombres, en el mismo orden, que en telefono_Act.csv. Los campos de texto conservados se separan por comas: almacenamiento en RAM y memoria; procesador en nombre, núcleos y frecuencia; pantalla en tamaño, resolución y descripción. Batería y carga se extraen reconociendo las unidades mAh y W; las cámaras se separan mediante el carácter &.')
p('La frecuencia se obtiene del tercer componente del campo procesador y de su primer valor numérico. Se reprodujeron las 865 posiciones, incluidos los 78 faltantes. La ausencia del componente puede reflejar un formato no reconocido o información faltante; no se sustituye por cero. Las celdas del cuaderno que exploran otros sitios o todas las parejas de variables no forman parte del ajuste bivariante aquí reconstruido.')

page('Flujo del procesamiento y conversión monetaria')
p('La Figura 1 muestra el recorrido de la base; la selección final exige únicamente las dos variables del ajuste.')
# Diagrama autónomo, con versiones equivalentes en matplotlib y TikZ.
fig,ax=plt.subplots(figsize=(6.5,3.3));ax.set(xlim=(0,10),ylim=(0,5));ax.axis('off')
labels=['CSV original\n1.020 filas · 12 variables','Eliminar 155 filas\ncon datos faltantes','Extraer y convertir\n865 filas · 24 variables','Seleccionar pares completos\n787 casos; 78 sin GHz']
for j,label in enumerate(labels):
 yy=4.4-j*1.12
 ax.text(5,yy,label,ha='center',va='center',bbox={'boxstyle':'square,pad=.5','facecolor':'#f4f4f4','edgecolor':'#444444'},fontsize=11)
 if j<3:ax.annotate('',xy=(5,yy-.75),xytext=(5,yy-.35),arrowprops={'arrowstyle':'->'})
flowtex=r'\begin{tikzpicture}[every node/.style={align=center,font=\small}]'
for j,label in enumerate(labels):
 flowtex+=f'\\node[draw,text width=10cm,minimum height=1cm] (n{j}) at (0,{-j*1.5}) '+'{'+esc(label).replace('\n',r'\\')+'};'
 if j:flowtex+=f'\\draw[->] (n{j-1}.south)--(n{j}.north);'
flowtex+=r'\end{tikzpicture}'
finish_plot('flujo',fig,flowtex)
figure('Recorrido desde los registros originales hasta el modelo','flujo','Reconstrucción local. No se imputaron valores ni se eliminaron casos influyentes en el análisis principal.')
p('El cuaderno elimina el símbolo de rupia y los separadores de miles, convierte el precio a número y lo multiplica por 0,012. Esta operación reproduce los 865 precios finales. El comentario de la celda denomina el factor una tasa de ejemplo: no aporta fuente ni fecha. Los valores en USD son conversiones ilustrativas del catálogo, no cotizaciones actuales ni precios verificados en Estados Unidos.')
eq(r'Y_{\mathrm{USD}}=0{,}012\,Y_{\mathrm{INR}}')

page('Calidad de datos y alcance de la reconstrucción')
p('La Tabla 2 identifica faltantes y problemas de extracción relevantes para interpretar el alcance de la revisión.')
table('Problemas relevantes en la tabla procesada',['Campo o condición','Resultado','Tratamiento'],[
 ['GHz del procesador','78 ausencias','Excluir solo del ajuste bivariante'],
 ['Precio convertido','0 ausencias','Usar conversión histórica'],
 ['Memoria / carga / batería','7 / 89 / 3 ausencias','No condicionan esta muestra'],
 ['Duplicado exacto','1 fila adicional','Conservar y evaluar sensibilidad'],
 ['RAM y sistema operativo','Hay valores mal extraídos','No usarlos como predictores']],
 'Se verifican conteos; el análisis no certifica que cada especificación comercial sea correcta.',[140,133,195])
p('Lava Storm 5G aparece dos veces con igualdad en todas las columnas. La eliminación de duplicados se aplica únicamente en un escenario secundario. Un valor de RAM de 256 GB y etiquetas de tarjeta de memoria dentro de sistema_operativo revelan problemas de extracción. La función histórica de sistema operativo devuelve el primer segmento del texto aunque encuentre Android en otro segmento; esta lógica puede asignar una etiqueta incorrecta.')
p('La reproducción demuestra la selección de registros, la frecuencia y el precio usados por el modelo. No acredita una regeneración exacta de las 24 columnas ni una ejecución continua y limpia de todas las celdas del cuaderno. La eliminación inicial por puntaje ausente, aunque ese puntaje no intervenga en la regresión, puede cambiar la composición de la muestra. Tampoco se conoce el mecanismo de los 78 faltantes de GHz; el análisis de casos completos podría introducir sesgo.')

page('Resultados descriptivos')
p('La Tabla 3 describe las variables centrales sobre los mismos 787 registros usados en el modelo.')
rows=[]
for key,label in [('mean','Media'),('std','Desviación típica muestral'),('min','Mínimo'),('25%','Primer cuartil'),('50%','Mediana'),('75%','Tercer cuartil'),('max','Máximo')]:rows.append([label,num(R['descriptive']['x'][key]),num(R['descriptive']['y'][key])])
table('Descriptivos de los 787 pares completos',['Estadístico','Frecuencia (GHz)','Precio (USD)'],rows,'Todas las medidas se calculan en la misma muestra; no se mezcla la media del catálogo completo con la media del ajuste.',[218,125,125])
p('La frecuencia media es 2,518 GHz y el precio medio convertido es 333,977 USD. La mediana de precio, 239,988 USD, es inferior a la media y el máximo alcanza 5.760 USD. Esta diferencia advierte una distribución con valores altos que pueden influir sobre el ajuste. La frecuencia observada se extiende de 1,60 a 3,78 GHz.')
p('Los promedios de las 865 filas y de los 787 pares responden a subconjuntos diferentes. Las estimaciones de covarianza, correlación, pendiente y residuos que siguen utilizan exclusivamente los pares completos, manteniendo su orden original. Los cálculos se realizan con precisión completa; el redondeo se aplica únicamente al presentarlos.')

page('Estimación de la covarianza')
p('Sean X la frecuencia en GHz e Y el precio convertido a USD. Primero se centran ambas variables restando su respectiva media; después se multiplican las desviaciones de cada teléfono y se suman los productos. Un producto positivo corresponde a desviaciones del mismo signo respecto de sus medias.')
eq(r'n=787,\qquad \bar{x}=2{,}518475,\qquad \bar{y}=333{,}977321')
eq(r'S_{XY}=\sum_{i=1}^{787}(x_i-\bar{x})(y_i-\bar{y})=73167{,}775226')
eq(r's_{XY}=\frac{73167{,}775226}{787-1}=93{,}088773\ \mathrm{GHz}\cdot\mathrm{USD}')
p('La covarianza positiva indica que, en conjunto, las frecuencias superiores a la media tienden a acompañarse de precios superiores a la media. Su magnitud no tiene un límite universal ni equivale a un porcentaje. Al expresar los precios en rupias, la covarianza numérica sería distinta debido al cambio de escala.')
eq(r's_X=0{,}458565,\quad s_Y=342{,}013462,\quad s_X^2=0{,}210282')
eq(r'r=\frac{93{,}088773}{0{,}458565\cdot342{,}013462}=0{,}593544')
eq(r'\widehat{\beta}_1=\frac{93{,}088773}{0{,}210282}=442{,}685089')
p('Las últimas igualdades se verificaron usando valores sin redondear. Así, la covarianza conecta el resumen de asociación con la pendiente del modelo y confirma que ambos procedimientos parten de las mismas observaciones.')

page('Regresión lineal simple')
p('El ajuste por mínimos cuadrados conserva los coeficientes principales del informe histórico. La Figura 2 presenta la dispersión y la recta estimada.')
eq(r'\widehat{Y}=-780{,}914107+442{,}685089X')
figure('Precio y frecuencia con recta de mínimos cuadrados','dispersion','Se representan los 787 pares completos en escala lineal. Los precios son conversiones históricas; la línea no implica causalidad ni exactitud predictiva.')
p('La pendiente describe una diferencia promedio ajustada de aproximadamente 442,69 USD por cada GHz dentro de esta parametrización. No representa el efecto de cambiar físicamente un procesador manteniendo todo lo demás constante. El intercepto negativo corresponde a X = 0, fuera del rango observado, y no describe un precio comercial. Incluso cerca del extremo inferior del rango, el modelo puede producir ajustes negativos, lo que limita su interpretación práctica.')

page('Coeficientes e incertidumbre')
p('Las Tablas 4 y 5 comparan la incertidumbre clásica con la estimación robusta HC3 para los mismos coeficientes.')
table('Estimaciones clásicas y errores robustos HC3',['Parámetro','Estimación','EE clásico','EE HC3'],[
 ['Intercepto',num(R['params']['const']),num(R['se']['const']),num(R['hc3_se'][0])],
 ['Pendiente',num(R['params']['x']),num(R['se']['x']),num(R['hc3_se'][1])]],
 'EE: error estándar. La pendiente se expresa en USD/GHz; el intercepto, en USD. HC3 conserva los coeficientes y cambia la estimación de su incertidumbre.',[144,108,108,108])
table('Intervalos de confianza del 95 % para los coeficientes',['Parámetro','Clásico','Robusto HC3'],[
 ['Intercepto',f'[{num(R["ci"][0][0],2)}; {num(R["ci"][0][1],2)}]',f'[{num(R["hc3_ci"][0][0],2)}; {num(R["hc3_ci"][0][1],2)}]'],
 ['Pendiente',f'[{num(R["ci"][1][0],2)}; {num(R["ci"][1][1],2)}]',f'[{num(R["hc3_ci"][1][0],2)}; {num(R["hc3_ci"][1][1],2)}]']],
 'Se usa t con 785 grados de libertad. Para HC3, esta referencia es una aproximación; no restaura la representatividad de la muestra.',[114,177,177])
p(f'Para H0: pendiente = 0 frente a una alternativa bilateral, el estadístico clásico es t(785) = {num(R["t"]["x"])} y p < 0,001. Con HC3, el intervalo de la pendiente también permanece por encima de cero. Los errores robustos contemplan heterocedasticidad bajo condiciones asintóticas, pero no corrigen dependencia entre registros, selección del catálogo ni una forma funcional incorrecta (statsmodels developers, s. f.-a).')

page('Descomposición de varianza y ANOVA')
p('La Tabla 6 descompone la variabilidad del precio en el componente ajustado y el residual.')
table('ANOVA del modelo histórico reproducido',['Fuente','SC','gl','CM','F'],[
 ['Regresión',num(R['SSR_explained'],3),'1',num(R['SSR_explained'],3),num(R['f'],3)],
 ['Residuo',num(R['SSE'],3),'785',num(R['MSE'],3),'—'],
 ['Total',num(R['syy'],3),'786','—','—']],
 'SC: suma de cuadrados; CM: cuadrado medio. El contraste F clásico se refiere a la pendiente, no a la homocedasticidad. p < 0,001.',[83,121,34,137,93])
eq(r'R^2=\frac{32390283{,}107724}{91940941{,}526146}=0{,}352294')
eq(r's^2=\frac{59550658{,}418422}{785}=75860{,}711361')
eq(r's=\sqrt{s^2}=275{,}428233\ \mathrm{USD}')
p('El modelo resume el 35,229 % de la suma total de desviaciones cuadráticas del precio respecto de su media. El 64,771 % restante corresponde a variabilidad residual, no a un porcentaje de teléfonos ni a una proporción de ocasiones en que el modelo falla. No puede atribuirse íntegramente a variables específicas que no se hayan estudiado.')
p('La ANOVA reproduce el resultado histórico F(1, 785) = 426,970. La identidad entre F y el cuadrado del estadístico t de la pendiente se cumple en esta regresión simple con intercepto. Su significación clásica está condicionada por los supuestos; la descomposición descriptiva de sumas de cuadrados sigue siendo válida algebraicamente.')

page('Intervalos para la media y para un teléfono')
p('Para una frecuencia x0 se distinguen dos objetivos: estimar el precio medio condicional y predecir una nueva observación. El segundo incluye la variabilidad individual y, por ello, es más amplio. Las expresiones siguientes son las clásicas del modelo homocedástico; se muestran para corregir el desarrollo original, sin garantizar cobertura real del 95 % en este catálogo.')
eq(r'S_{XX}=\sum_{i=1}^{n}(x_i-\bar{x})^2=165{,}281770')
eq(r'\widehat{\mu}_0\ \pm\ t_{0{,}975;785}\,s\sqrt{\frac{1}{n}+\frac{(x_0-\bar{x})^2}{S_{XX}}}')
eq(r'\widehat{Y}_0\ \pm\ t_{0{,}975;785}\,s\sqrt{1+\frac{1}{n}+\frac{(x_0-\bar{x})^2}{S_{XX}}}')
p('La Tabla 7 usa s = 275,428233 USD y t crítico = 1,962991. El original confundía la desviación residual con su cuadrado e introducía la suma de cuadrados de regresión en lugar de SXX; ambos errores estrechaban los intervalos.')
rows=[]
for x0,z in zip([2.5,4.5],R['predictions']):rows.append([num(x0,1),num(z['mean'],2),f'[{num(z["mean_ci_lower"],2)}; {num(z["mean_ci_upper"],2)}]',f'[{num(z["obs_ci_lower"],2)}; {num(z["obs_ci_upper"],2)}]'])
table('Intervalos clásicos nominales del 95 % en USD',['GHz','Ajuste','Media condicional','Nueva observación'],rows,'2,5 GHz está dentro del rango; 4,5 GHz es extrapolación y se conserva únicamente para contrastar el ejemplo original.',[42,74,166,186])
p('El límite negativo del intervalo individual a 2,5 GHz carece de sentido económico. Se conserva para evidenciar la limitación del modelo aditivo; truncarlo sin otro fundamento cambiaría el procedimiento. A 4,5 GHz se agrega el riesgo de extrapolar más allá del máximo observado de 3,78 GHz.')

page('Diagnóstico gráfico de residuos')
p('La Figura 3 permite examinar la variabilidad residual y las observaciones extremas a lo largo del ajuste.')
figure('Residuos frente a precios ajustados','residuos','Residuo = precio observado menos precio ajustado. Se conservan todos los casos y se incluye la línea horizontal en cero.')
p('La dispersión de residuos no resulta uniforme y aparece un residuo positivo extremo. La figura ayuda a examinar forma funcional, variabilidad e influencia; por sí sola no determina el mecanismo que produce cada desviación. Un precio muy alto puede ser genuino, corresponder a una edición especial o contener un error: esta revisión no verifica nuevamente cada anuncio.')
p('Los procedimientos de diagnóstico se aplican a los residuos calculados con los 787 casos del modelo. No se utilizan pruebas de normalidad del precio marginal como sustituto de la normalidad de errores, ni un gráfico Q–Q como contraste de igualdad de varianzas. La revisión se apoya en evidencia gráfica y pruebas dirigidas a hipótesis específicas.')

page('Normalidad y especificación del modelo')
p('La Figura 4 compara los residuos con cuantiles normales; la Tabla 8 resume los diagnósticos recalculados.')
figure('Gráfico Q–Q normal de los residuos','qq','La línea es una referencia ajustada a los cuantiles. La separación en la cola superior evidencia una desviación marcada del patrón normal.')
table('Diagnósticos recalculados',['Procedimiento','Estadístico','p'],[
 ['Shapiro–Wilk, residuos',f'W = {num(R["shapiro"]["W"],4)}','< 0,001'],
 ['Breusch–Pagan–Koenker',f'LM(1) = {num(R["bp"]["LM"],3)}',num(R['bp']['p'],4)],
 ['RESET cuadrático, HC3',f'F(1, 784) = {num(R["reset"]["F"],3)}','< 0,001']],
 'α = 0,05. Los tres procedimientos evalúan hipótesis distintas; ninguno certifica representatividad o causalidad.',[264,139,65])
p('El contraste de normalidad usa los residuos del ajuste (The SciPy community, s. f.).')

page('Interpretación de los diagnósticos')
p('Breusch–Pagan–Koenker contrasta la constancia de varianza mediante una regresión auxiliar de los residuos al cuadrado sobre el diseño del modelo. Se utilizó la variante estudiantizada de Koenker, configurada como robusta en statsmodels; su valor p aproximado es 0,0339. A un nivel de 0,05 hay evidencia contra varianza constante, dentro de las condiciones del contraste (statsmodels developers, s. f.-b). Esto sustituye la aplicación incorrecta de la ANOVA como prueba de homocedasticidad.')
p('El contraste RESET añade el cuadrado de los valores ajustados y usa una covarianza HC3. La significación observada señala insuficiencia de la especificación lineal elegida, sin identificar por sí sola una forma alternativa correcta. La frecuencia puede mantener una asociación positiva y, al mismo tiempo, resultar insuficiente para describir el precio con una sola recta.')
p(f'Durbin–Watson vale {num(R["dw"],3)} en el orden de las filas del CSV, coincidiendo con el resultado histórico. Sin un orden temporal o secuencial sustantivo, su cercanía a dos no demuestra independencia. Configuraciones de un mismo fabricante o familia pueden compartir características; no se dispone aquí de un diseño que permita resolver esa posible dependencia.')
p('La conclusión revisada distingue cálculo y uso: la recta y su R² resumen los datos; los intervalos clásicos carecen de una validación de cobertura; HC3 ofrece una comprobación de incertidumbre frente a heterocedasticidad, pero no convierte el ajuste en una herramienta de predicción validada. No se evaluó desempeño fuera de muestra.')

page('Sensibilidad a duplicados e influencia')
p('La Tabla 9 compara el ajuste histórico con tres escenarios de sensibilidad, sin reemplazar el resultado principal.')
table('Cambios del ajuste en escenarios secundarios',['Escenario','n','Pendiente','R²'],[
 [s['escenario'],str(s['n']),num(s['pendiente'],3),num(s['r2'],4)] for s in R['sensitivity']],
 'Pendiente en USD/GHz. Los escenarios se calculan por separado desde la muestra histórica. El criterio de Cook se calcula una sola vez sobre el ajuste principal.',[238,45,100,85])
p('Eliminar el duplicado exacto deja 786 observaciones y modifica mínimamente la pendiente y el R². En cambio, retirar únicamente la observación con mayor distancia de Cook eleva R² de 0,3523 a 0,4973 y reduce la pendiente de 442,685 a 433,639 USD/GHz. La dirección de la asociación persiste, pero su aparente capacidad explicativa es sensible a un caso extremo.')
p(f'El caso de mayor influencia es {R["max_cook"]["name"]}, en la fila {R["max_cook"]["csv_row"]} del CSV contando el encabezado: 2,8 GHz y 5.760 USD; D de Cook = {num(R["max_cook"]["D"],4)}. El umbral exploratorio 4/n = {num(R["cook_threshold"],6)} señala {R["cook_flagged"]} casos. Retirarlos deja 762 observaciones, pendiente 328,380 y R² = 0,5744.')
p('El incremento de R² al retirar casos no prueba que el modelo mejore para el mercado real. La selección utiliza la respuesta y el ajuste, por lo que es una exploración de sensibilidad, no una nueva muestra confirmatoria. Los 787 casos permanecen en el resultado principal y las filas señaladas quedan registradas para revisión.')

page('Discusión')
p('El resultado central del trabajo se reproduce: la asociación lineal entre frecuencia y precio es positiva y moderada. La covarianza añadida muestra cómo esa relación se construye a partir de desviaciones conjuntas y permite recuperar tanto Pearson como la pendiente. Las diferencias respecto de la ecuación histórica se limitan al redondeo; los cambios principales afectan a la justificación de los contrastes y a la amplitud de los intervalos.')
p('Un R² de aproximadamente 35,2 % es una descripción de esta muestra y de esta especificación. La comparación de sensibilidad muestra que el valor depende de observaciones influyentes. Tampoco existe fundamento para trasladarlo directamente a teléfonos actuales, otros países o unidades realmente vendidas. La extracción del catálogo, los registros repetidos y la exclusión por datos faltantes limitan la generalización.')
p('La frecuencia no captura arquitectura, memoria, marca ni otras condiciones comerciales. Incluir más variables podría mejorar la descripción, pero requiere reparar primero su extracción y evaluar dependencia, forma funcional y desempeño fuera de muestra. Cocientes construidos con el propio precio no deben usarse como predictores para después celebrar una correlación artificialmente alta con él.')
p('La revisión deja evidencia de que el proceso de preparación importa tanto como la ecuación. Se lograron reconstruir las variables centrales sin modificar el archivo final; las columnas auxiliares requieren una revisión independiente. La tasa de conversión ilustrativa cambia la escala de precios y covarianza, aunque no la correlación ni R², y debe acompañar cualquier comunicación pública de los resultados.')

page('Conclusiones')
p('En 787 pares completos, la covarianza muestral entre frecuencia del procesador y precio convertido fue 93,089 GHz·USD y Pearson fue 0,594. La recta estimada, precio = −780,914 + 442,685 × GHz, obtuvo R² = 0,3523. Estas cantidades son coherentes entre sí y reproducen el ajuste principal del trabajo de marzo de 2025.')
p('La selección histórica se pudo reconstruir: 1.020 registros originales, 865 después de excluir faltantes iniciales y 787 después de exigir frecuencia disponible. La reconstrucción de GHz y la conversión monetaria coincidieron con el archivo procesado. La documentación no permite asignar a cada registro una fecha de precio ni acreditar un muestreo probabilístico.')
p('Los diagnósticos recalculados muestran residuos alejados de normalidad, evidencia de heterocedasticidad y señales de especificación insuficiente. El intervalo robusto de la pendiente conserva valores positivos, pero la sensibilidad a casos influyentes y las limitaciones del diseño impiden concluir causalidad o capacidad predictiva validada.')
p('El trabajo puede presentarse como una experiencia de preparación de datos, covarianza, regresión y revisión crítica de supuestos. Antes de desarrollar un predictor o recomendar compras, se necesita verificar el catálogo, corregir variables auxiliares, documentar fechas y moneda, ampliar la especificación y evaluar predicciones con datos independientes.')

page('Referencias')
ref('American Psychological Association. (s. f.). A step-by-step guide for creating and formatting APA Style student papers. Psychology Student Network.','https://www.apa.org/ed/precollege/psn/2020/09/apa-style-student-papers')
ref('National Institute of Standards and Technology. (s. f.). Least squares. En NIST/SEMATECH e-Handbook of statistical methods.','https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd431.htm')
ref('Rosales, I. A., & Sanz, M. A. (2025). Análisis de regresión lineal simple entre los GHz del procesador y el precio [Trabajo académico no publicado]. Escuela de Estadística y Ciencias Actuariales, Universidad Central de Venezuela.')
ref('santoshgupta01. (s. f.). Latest Uncleaned Mobile Dataset (2024) [Conjunto de datos]. Kaggle.','https://www.kaggle.com/datasets/santoshgupta01/uncleaned-mobile-dataset')
ref('statsmodels developers. (s. f.-a). OLSResults.HC3_se. statsmodels.','https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLSResults.HC3_se.html')

page('Referencias (continuación)')
ref('statsmodels developers. (s. f.-b). statsmodels.stats.diagnostic.het_breuschpagan. statsmodels.','https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.het_breuschpagan.html')
ref('The SciPy community. (s. f.). scipy.stats.shapiro. SciPy.','https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html')
p('Nota bibliográfica. Las referencias web se verificaron para esta revisión. Se usa s. f. cuando no se acreditó una fecha de publicación. El año 2024 forma parte del título del conjunto y no se usa como fecha verificada de cada observación. El cuaderno app.ipynb y los CSV locales son materiales del proyecto que se identifican en el apéndice de reproducción.')
p('La presentación adopta las pautas generales de APA 7 para trabajos estudiantiles: márgenes de 2,54 cm, cuerpo serif de 12 puntos, doble interlineado, alineación izquierda, sangría de primera línea, numeración superior y referencias con sangría francesa (American Psychological Association, s. f.). Las tablas emplean espaciado más compacto para facilitar su lectura.')

page('Apéndice A: diccionario y trazabilidad')
p('La Tabla 10 documenta las variables del modelo y los campos generados para auditar sus resultados.')
table('Variables utilizadas y campos de auditoría',['Campo','Significado y unidad','Origen'],[
 ['Nombre','Entrada comercial; texto','mobile_name'],
 ['GHz_Procesador / x','Frecuencia; GHz','Tercer segmento de processor'],
 ['Precio($) / y','Precio convertido; USD','price en INR × 0,012'],
 ['ajuste','Precio sobre la recta; USD','Intercepto + pendiente × x'],
 ['residuo','Diferencia observada; USD','y − ajuste'],
 ['cook','Distancia de influencia; sin unidad','Modelo con intercepto'],
 ['fila_csv','Posición física con encabezado','Índice original + 2']],
 'Las variables derivadas de diagnóstico se guardan en pares_y_diagnosticos.csv. Ninguna se añade a los CSV históricos.',[127,205,136])
p('El archivo bruto contiene nombre, precio, calificación, puntaje de especificaciones, conectividad, procesador, almacenamiento, batería, pantalla, cámaras, almacenamiento adicional y sistema operativo. El cuaderno renombra estas columnas y genera campos derivados. Se explica ese recorrido para comprender el origen de las variables; el ajuste no utiliza todas las columnas disponibles.')
p('La reproducción conserva los identificadores comerciales para revisar observaciones influyentes. El documento nuevo no contiene números de cédula, imágenes de la portada anterior ni identificadores personales en sus metadatos. La autoría se expresa únicamente mediante nombres y afiliación académica.')

page('Apéndice B: correcciones del informe original')
p('La Tabla 11 reúne las correcciones que afectan al cálculo y a la interpretación del estudio histórico.')
table('Cambios sustantivos de esta edición',['Elemento','Corrección'],[
 ['Covarianza','Se añade el cálculo con divisor n − 1, unidades y conexiones con r y pendiente.'],
 ['Distribución de contraste','Se usa t con 785 grados de libertad; n ≥ 30 no obliga a utilizar Z.'],
 ['Linealidad','Una pendiente significativa no demuestra una forma lineal adecuada; se agrega RESET robusto.'],
 ['Normalidad','Se examinan los residuos de 787 casos, no la distribución marginal del precio de 865 filas.'],
 ['Homocedasticidad','Se reemplaza la ANOVA como diagnóstico por Breusch–Pagan–Koenker.'],
 ['Independencia','Durbin–Watson no certifica independencia en un catálogo sin orden temporal.'],
 ['Intervalos','Se corrigen s² y SXX, se usa t y se identifica la extrapolación a 4,5 GHz.'],
 ['Interpretación de R²','Se refiere a variabilidad cuadrática, no a porcentaje de ocasiones o de teléfonos.'],
 ['Muestra y privacidad','Se mantiene el ajuste histórico, se añade sensibilidad y se retiran las cédulas.']],
 'La ecuación, ANOVA y R² principales coinciden con el original dentro de su redondeo. Las conclusiones metodológicas se apoyan en cálculos nuevos.',[126,342])

page('Apéndice C: reproducción y verificación')
p('El directorio revision_informe del repositorio contiene analizar.py, editar_informe.py y contenido.py. El primero reconstruye la selección, verifica las variables centrales y recalcula las estimaciones; el segundo genera figuras y documento desde un contenido único; el tercero contiene la redacción. resultados.json conserva cifras de precisión completa, versiones de bibliotecas y huellas de los archivos de entrada.')
p('En un entorno virtual aislado, instalar las versiones de requirements.txt y ejecutar analizar.py desde cualquier carpeta. El script resuelve las rutas respecto de su propia ubicación y no depende del estado interactivo del cuaderno. Sus comprobaciones exigen coincidencia de precios y frecuencias reconstruidos y verifican las identidades entre covarianza, correlación, pendiente, R² y ANOVA.')
p('Ejecutar después editar_informe.py para regenerar las figuras, el PDF de revisión y la fuente Informe_Mobile_Statics_APA7.tex. Esta fuente es autónoma: las coordenadas de los gráficos están incluidas mediante PGFPlots y TikZ, sin archivos externos ni bibliografía que requiera un segundo programa. Abrirla en el editor LaTeX y compilar permite obtener la versión tipográfica de la fuente cuando el compilador esté disponible.')
p('La composición del PDF de revisión se genera desde los mismos bloques de contenido mediante ReportLab; no equivale a una confirmación de compilación LaTeX. El estado del compilador y la revisión visual se registran en VERIFICACION.md. Ambos documentos conservan fórmulas, tablas y resultados; la distribución exacta de páginas puede variar entre motores.')
p('Se registran Python '+R['python_version']+', NumPy '+R['versions']['numpy']+', pandas '+R['versions']['pandas']+', SciPy '+R['versions']['scipy']+' y statsmodels '+R['versions']['statsmodels']+'. Los escenarios de sensibilidad son deterministas y no requieren semilla aleatoria. Las fuentes y los registros originales se conservan sin modificaciones.')
