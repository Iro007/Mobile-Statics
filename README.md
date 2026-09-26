# Mobile-Statics — proyecto web

Micrositio estático bilingüe para explorar el proyecto académico de Estadística II.

## Vista local

Abre `index.html` en un navegador moderno. La tabla de datos está en `data.js`. Los gráficos usan Plotly.js desde su CDN, así que requieren conexión a internet.

## Publicación gratuita

Enlace público: https://byirosaleshd.github.io/Mobile-Statics/

GitHub Pages publica la raíz de la rama `gh-pages`. Los archivos de esta carpeta se copian a esa rama mediante `revision_informe/desplegar_web.ps1`. La rama `main` conserva el proyecto histórico. No necesita servidor de pago ni base de datos remota.

## Datos y límites

El explorador filtra el conjunto procesado (`telefono_Act.csv`): 865 filas. La regresión entre GHz y precio usa 787 pares completos. Los diagnósticos de la revisión detectan residuos no normales, heterocedasticidad y observaciones influyentes. La recta se presenta como resumen exploratorio; no se validó su predicción fuera de muestra. Los precios se convierten con un factor ilustrativo de 0,012 USD/INR, sin fecha acreditada. El catálogo conserva un duplicado exacto.

La recta y las métricas del explorador cambian con los filtros; los resultados destacados corresponden al conjunto completo. La comparativa de RAM omite valores superiores a 32 GB y grupos de menos de 5 casos, como se explica junto al gráfico.

El informe revisado sin cédulas, la fuente LaTeX y los resultados numéricos están en `downloads/`. Las gráficas utilizan Plotly.js 2.35.2 desde su CDN. Si no carga, se muestra un aviso y permanecen disponibles el PDF y el CSV.
