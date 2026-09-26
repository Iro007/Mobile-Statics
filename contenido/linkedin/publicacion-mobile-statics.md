# LinkedIn · Mobile-Statics

¿Qué tanto explica el procesador el precio de un teléfono? 📱📊

En marzo de 2025, mi compañero Miguel Sanz y yo desarrollamos Mobile-Statics como parte de Estadística II en la Universidad Central de Venezuela.

Trabajamos con un catálogo de móviles disponible en Kaggle, atribuido a Smartprix. El proceso incluyó limpiar campos de texto, tratar datos faltantes, explorar las especificaciones y estudiar la relación entre los GHz del procesador y el precio con Python y SPSS.

De 1.020 registros originales quedaron 865 tras la limpieza inicial y 787 pares completos para la regresión.

Encontramos una correlación positiva moderada (r ≈ 0,594). El modelo lineal explicó alrededor del 35,2 % de la variación observada en el precio.

Lo más valioso fue revisar qué tan bien se sostenía ese resultado. Los residuos presentaron problemas de normalidad y varianza, y algunos valores extremos influyeron bastante en el ajuste. Me quedo con la importancia de revisar los supuestos y comunicar los límites de cada conclusión.

Ahora comparto el proyecto en una web interactiva: puedes filtrar el catálogo, explorar los gráficos, descargar los datos y leer el informe revisado, que incorpora la covarianza y explica todo el proceso.

Son datos históricos y los precios usan una conversión monetaria ilustrativa, detallada en el informe.

🔎 Explora el proyecto: https://iro007.github.io/Mobile-Statics/

¿Qué variable agregarías al análisis: memoria, cámara, batería o marca?

#Estadística #AnálisisDeDatos #RegresiónLineal #Python #UCV
