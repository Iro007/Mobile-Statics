# Verificación de la revisión — 26 de septiembre de 2026

## Resultados comprobados

- Selección reproducida: 1.020 → 865 → 787 observaciones.
- Coincidencia de los 865 nombres y su orden tras la eliminación inicial de faltantes.
- Precios convertidos y frecuencias reconstruidos: coincidencia en 865 posiciones, incluidos los faltantes de GHz.
- Covarianza muestral: 93,08877255186863 GHz·USD; suma de productos centrados: 73.167,77522576874.
- Pearson: 0,5935439718526685; R²: 0,35229444652264086.
- Intercepto: −780,9141071697542; pendiente: 442,6850892729704.
- Identidades verificadas contra NumPy y ajuste independiente de SciPy; ANOVA y dos tipos de intervalos contrastados contra las fórmulas directas.
- Pruebas aplicadas a los residuos de 787 casos: Shapiro–Wilk, Breusch–Pagan–Koenker y RESET cuadrático con HC3.
- Sensibilidad calculada sin modificar los archivos originales.

## Privacidad y presentación

- PDF, texto LaTeX y metadatos comprobados contra los números de cédula de la portada histórica: no aparecen.
- Portada e imágenes completamente nuevas, sin incorporar páginas del PDF anterior.
- Texto sin líneas fuera de los márgenes, según los límites de página analizados con PyMuPDF.
- Páginas renderizadas y revisadas visualmente; figuras completas, tablas legibles y fórmulas sin símbolos sustituidos.
- Formato de trabajo estudiantil APA 7: Times New Roman 12, interlineado doble, márgenes de 2,54 cm, sangría de primera línea, resumen sin sangría, numeración superior derecha, referencias con sangría francesa y títulos en cursiva.
- El detalle automático y el recuento definitivo están en `revision_pdf.json`.
- Presentación exportada de Canva: 33 diapositivas, archivo PPTX íntegro y cero números etiquetados como CI en el texto de las diapositivas o notas. La portada se revisó visualmente en Canva después de eliminar los dos números y preservar los nombres.
- La revisión de identificadores en el PPTX cubre los campos de texto de las diapositivas y notas; no ejecuta OCR sobre imágenes incorporadas.

## Compilación LaTeX: bloqueada por el entorno

Se solicitó abrir la fuente en el editor integrado y se invocó su compilador dos veces (portada inicial y documento completo). Ambos intentos fallaron antes de procesar el documento:

```text
Unable to find standard directories for platform
```

No se instaló otro sistema TeX ni se alteró la configuración de la aplicación. La fuente permanece disponible en el editor. Se comprobó estáticamente el equilibrio de entornos y la ausencia de caracteres de control, pero esto **no equivale a una compilación exitosa**.

El PDF entregado fue compuesto con ReportLab desde los mismos bloques de contenido utilizados para generar el `.tex`. No es una exportación LaTeX y no debe describirse como tal. Los gráficos del PDF se generaron con Matplotlib; la fuente contiene coordenadas equivalentes de PGFPlots/TikZ para ser autónoma. La paginación puede variar al compilar la fuente con un entorno funcional.

## Alcance pendiente

Queda pendiente compilar el `.tex` en un entorno funcional y revisar ese PDF específico. El texto, el análisis y el PDF alternativo están entregados. No se ha actualizado ni publicado la web o la publicación de LinkedIn en esta etapa.
