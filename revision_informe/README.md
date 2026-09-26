# Revisión académica de Mobile-Statics

## Entregables

En la carpeta académica `Trabajo estadistica 2`:

- `Informe_Mobile_Statics_APA7.tex`: fuente autónoma con coordenadas de todas las figuras, tablas y referencias incluidas.
- `Informe_Mobile_Statics_APA7.pdf`: edición académica revisada; el recuento definitivo figura en `revision_pdf.json`.

El PDF se compone desde los mismos bloques de contenido mediante ReportLab. No se presenta como una exportación del compilador LaTeX integrado: ese compilador falla al resolver directorios del entorno antes de leer el documento. El editor se conserva abierto. Los PDF anteriores permanecen intactos.

## Regenerar en Windows

Desde la raíz del repositorio:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r revision_informe\requirements.txt
.\.venv\Scripts\python.exe revision_informe\analizar.py
.\.venv\Scripts\python.exe revision_informe\editar_informe.py
.\.venv\Scripts\python.exe revision_informe\revisar_pdf.py
```

No hace falta recrear el entorno si ya existe. La composición PDF utiliza las fuentes Times New Roman de Windows. Para otra ubicación, ajustar `DEST` en `editar_informe.py` y `revisar_pdf.py`; el análisis estadístico resuelve sus entradas respecto de la raíz del repositorio.

## Fuente y cálculos

- `analizar.py`: lee `mobiles.csv`, `telefono_Act.csv` y las huellas del cuaderno; reconstruye los pares y calcula el modelo.
- `contenido.py`: redacción compartida entre PDF y LaTeX.
- `editar_informe.py`: genera tablas, figuras y ambos documentos; las figuras se guardan en PNG y PDF vectorial. No ejecuta scraping.
- `resultados.json`: todas las cifras sin redondear, controles, versiones y SHA-256 de las entradas.
- `pares_y_diagnosticos.csv`: 787 filas con frecuencia, precio, ajuste, residuo, Cook y fila original.
- `revisar_pdf.py`: controles de privacidad, márgenes de texto y estructura estática de LaTeX; prepara páginas y hojas de contacto en `tmp/revision_pdf`.

Las identidades de covarianza, Pearson, pendiente, R² y ANOVA están verificadas; la regresión se coteja contra SciPy y los intervalos contra sus fórmulas directas. El análisis principal conserva el duplicado. Los escenarios de sensibilidad son independientes y no modifican el CSV original.

## Pendientes para una publicación posterior

La web y el texto de LinkedIn no se cambian en esta etapa. Deben actualizarse para indicar la conversión ilustrativa de moneda, la procedencia declarada y los diagnósticos recalculados. Antes de publicar un PDF, utilizar esta edición sin cédulas y no las copias históricas.
