# Generador de diapositivas

App web de un solo archivo: sube un documento Word (.docx) y/o pega un enlace de referencia y genera una presentación con esta estructura: Introducción, Tema (con tablas y gráficos), Casos, Importancia, Conclusiones y Recomendaciones.

## Uso
1. Abre `index.html` (o publícalo con GitHub Pages).
2. Sube el .docx y/o pega un enlace y pulsa "Generar diapositivas".
3. Edita el texto haciendo clic en él y exporta a PowerPoint.

## Cómo detecta las secciones
Busca títulos del Word (o del enlace) como Introducción, Casos, Importancia, Conclusiones y Recomendaciones. Lo demás va a "Tema". Las tablas con números se muestran junto a un gráfico de barras. Si faltan títulos, busca frases con palabras clave. No usa IA: extrae y resume las primeras frases de cada sección.

## Publicar en GitHub Pages
Settings > Pages > Branch: main, carpeta / (root).
