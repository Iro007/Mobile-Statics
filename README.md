# Mobile-Statics

Proyecto académico de **Estadística II** sobre la relación entre la frecuencia del procesador y el precio de teléfonos móviles. Autores: Ignacio A. Rosales y Miguel A. Sanz, Universidad Central de Venezuela.

## Explora el proyecto

**Web pública:** [Mobile-Statics en GitHub Pages](https://iro007.github.io/Mobile-Statics/)

La web permite filtrar 865 registros y explorar las gráficas. El ajuste principal usa 787 pares completos, con correlación de Pearson `r = 0,594` y `R² = 35,2 %`. Incluye la recta recalculada para cada selección, el PDF, la fuente LaTeX, resultados y datos para descarga.

## Organización

- `site/`: web estática publicada en GitHub Pages desde la raíz de `gh-pages`.
- `entregables/estadistica_ii/`: informe revisado en PDF y fuente LaTeX.
- `contenido/linkedin/`: texto listo para adaptar y publicar en LinkedIn.
- `revision_informe/`: análisis reproducible, diagnósticos, material de despliegue y verificaciones.
- Los CSV, el cuaderno y los archivos originales del proyecto permanecen en su ubicación histórica en la raíz para conservar la compatibilidad con los notebooks y los datos previos.

## Informe y limitaciones

El informe revisado explica la procedencia y transformación de la base, exclusiones, covarianza, regresión, intervalos, diagnóstico de residuos y sensibilidad a observaciones influyentes. El factor de conversión `0,012 USD/INR` es ilustrativo; el cuaderno no documenta su fecha ni fuente. El conjunto es histórico, conserva un registro duplicado y no es una muestra aleatoria. La asociación observada no demuestra causalidad. Los diagnósticos desaconsejan usar la recta para predecir precios individuales.

El PDF se entrega junto a su fuente LaTeX. El compilador integrado usado durante la preparación presentó un error de plataforma antes de procesar la fuente; por eso el PDF se compuso desde los mismos bloques de contenido con ReportLab. Esta diferencia está documentada en `revision_informe/VERIFICACION.md`.

## Reproducir el análisis

Desde la raíz del repositorio, en Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r revision_informe\requirements.txt
.\.venv\Scripts\python.exe revision_informe\analizar.py
.\.venv\Scripts\python.exe revision_informe\editar_informe.py
.\.venv\Scripts\python.exe revision_informe\revisar_pdf.py
.\.venv\Scripts\python.exe revision_informe\preparar_web.py
```

Para previsualizar la web localmente:

```powershell
python -m http.server 8000 --directory site
```

Después de actualizar `site/`, ejecuta `revision_informe/desplegar_web.ps1` para publicar la carpeta en la rama `gh-pages`. El análisis registra controles de consistencia, versiones de Python y huellas de los archivos fuente en `revision_informe/resultados.json`.

## Fuente del catálogo

El README histórico del proyecto atribuye el conjunto de datos a [Latest Uncleaned Mobile Dataset (2024), de santoshgupta01 en Kaggle](https://www.kaggle.com/datasets/santoshgupta01/uncleaned-mobile-dataset). Los materiales de extracción incluidos en el repositorio apuntan a Smartprix. La fuente y fecha de cada precio no están documentadas de forma individual.
