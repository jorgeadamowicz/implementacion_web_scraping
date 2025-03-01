# Web Scraping: Práctica Paso a Paso

Este repositorio contiene una serie de ejercicios prácticos sobre Web Scraping, realizados paso a paso con `requests`, `BeautifulSoup` y el manejo de datos obtenidos de sitios web. El objetivo de esta práctica fue comprender los conceptos básicos del scraping y aplicarlos de manera estructurada.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Requests**: Para obtener el contenido HTML de las páginas web.
- **BeautifulSoup**: Para parsear y analizar el HTML.
- **CSV**: Para almacenar los datos extraídos en archivos estructurados.

## Conceptos Clave Aprendidos

- **Entendimos el DOM**: Estructura de una página web y sus nodos.
- **Usamos `requests`**: Para descargar contenido de una página web.
- **Parseamos con `BeautifulSoup`**: Accediendo a etiquetas HTML.
- **Utilizamos selectores CSS**: (`.select()`, `#id`, `.class`).
- **Iteramos con `for` y `enumerate()`**: Para mostrar contenido estructurado.
- **Guardamos los datos en un archivo CSV**: Con `csv.writer()`.

## Ejercicios Realizados

### 1. Scraping Básico
- Descargamos el contenido de una página web con `requests`.
- Analizamos el HTML con `BeautifulSoup`.
- Extraímos información usando `.title`, `.text`, `.find_all()`.

### 2. Uso de Selectores CSS
- Aplicamos `soup.select()` para buscar elementos con selectores avanzados.
- Filtramos información por etiquetas, clases e IDs.
- Mostramos sólo un subconjunto de datos relevantes.

### 3. Iteración y Extracción de Enlaces
- Extraímos y listamos enlaces de una página web.
- Usamos `href=True` para filtrar enlaces válidos.
- Iteramos con `enumerate()` para numerar los resultados.

### 4. Guardado de Datos en CSV
- Convertimos la información extraída en datos estructurados.
- Guardamos los datos en un archivo `.csv`.
- Utilizamos `csv.writer()` para escribir los datos en filas y columnas.

## Cómo Usarlo
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta los scripts:
   ```bash
   python scraping_basico.py
   ```

## Siguientes Pasos
La siguiente etapa de esta práctica incluirá el uso de **Selenium** para interactuar con páginas web dinámicas y, eventualmente, la creación de una interfaz gráfica con **PyQt**.

---
✍️ *Este proyecto es parte de mi proceso de aprendizaje en Web Scraping. Cualquier sugerencia o mejora es bienvenida.* 🚀

