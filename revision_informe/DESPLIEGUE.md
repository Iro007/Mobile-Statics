# Web pública de Mobile-Statics

Despliegue verificado el 26 de septiembre de 2026.

- URL: https://iro007.github.io/Mobile-Statics/
- Repositorio actual: https://github.com/Iro007/Mobile-Statics
- Proveedor: GitHub Pages, repositorio público, sin servidor de pago.
- Fuente de publicación: rama `gh-pages`, carpeta raíz, HTTPS forzado.
- Commit desplegado: `bf6a6073a432eef257895bfb7c773b335466da2a`.
- GitHub Actions: ejecución `36268783514`, concluida con éxito.
- El remoto histórico de Byirosaleshd redirige al propietario actual Iro007.

## Comprobación sobre el enlace público

Se ejecutó `verificar_web.cjs` contra la URL pública, con navegador Edge mediante Playwright: 865 registros, 787 puntos en la regresión, covarianza 93,089, R² 35,2 %, descarga CSV filtrada de 713 filas para precio máximo 500 USD, selección vacía, restablecimiento, cambio español/inglés y vistas de escritorio y móvil sin desbordamiento. Sin errores JavaScript. PDF e imagen social devuelven HTTP 200. Se verificó la dirección canónica.

El informe publicado es la edición revisada sin cédulas. Incluye la fuente LaTeX y los resultados numéricos. La tarjeta social usa el gráfico real y está configurada mediante Open Graph. No se ha enviado ninguna publicación a LinkedIn; el texto listo para copiar está en `contenido/linkedin/publicacion-mobile-statics.md`.

## Actualización

Editar `site/`, revisar localmente y ejecutar `revision_informe/desplegar_web.ps1`. La actualización crea un commit descendiente de la rama pública y realiza un push normal. Usa un índice temporal para no incorporar los otros cambios del proyecto.
