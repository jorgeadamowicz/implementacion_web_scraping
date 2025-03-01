"""
✅ Cambiamos la URL a Wikipedia para aplicar selectores CSS en un sitio real.
✅ Utilizamos soup.select() en lugar de find_all() para hacer búsquedas más avanzadas.
✅ Usamos selectores CSS como "div#mw-content-text" para extraer contenido específico.
✅ Aplicamos a[href] para obtener solo los enlaces que contienen un atributo href.
✅ Limitamos la cantidad de elementos mostrados [:5] y [:10] para no saturar la terminal.
✅ Aplicamos .strip() a los textos para eliminar espacios en blanco innecesarios.
"""

import requests
from bs4 import BeautifulSoup

#url de la pagina a examinar
url = "https://es.wikipedia.org/wiki/Python"

#hacemos la solicitud HTTP con requests.get()
response = requests.get(url)

#verificamos la solicitud
if response.status_code == 200:
    print('Solicitud exitosa\n')
    
    #analizamos el contenido de la pagina con Beautifulsoup. Convirtiendo el HTML en un objeto que podemos recorrer y analizar.
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #Utilizamos selectores CSS para encontrar elementos específicos.
    #obtenemos el encabezado <h1> de la página
    titulo = soup.select_one('h1')
    print(f"El titulo de la página es:{titulo.text.strip()}\n")
    
    #obtenemos el contenido de algunos parrafos <p> de la página
    parrafos = soup.select('p')
    print(f"\nPrimeros 3 parrrafos de la página:")
    for i, parrafo in enumerate(parrafos[:3], start = 1):
        print(f"{i}: {parrafo.text.strip()}\n")
        
    #buscamos enlaces dentro de un <div> específico
    enlaces = soup.select('div#mw-content-text a[href]')
    print(f"\nPrimeros 5 enlaces de la página:")
    for i, enlace in enumerate(enlaces[:5], start = 1):
        print(f"{i}: {enlace.text.strip()}- URL: {enlace['href']}")
        
else:
    print(f"Error de solicitud: {response.status_code}")
    
    
"""
Reglas útiles de selectores CSS en BeautifulSoup:

"h1" → Encuentra todos los encabezados <h1>.
"p" → Encuentra todos los párrafos <p>.
"div p" → Encuentra todos los párrafos <p> dentro de un <div>.
"#contenido" → Encuentra el elemento con id="contenido".
"div#contenido" → Encuentra el <div> que tiene id="contenido".
".clase" → Encuentra todos los elementos con class="clase".
"div.clase" → Encuentra un <div> con class="clase".
"a" → Encuentra todos los enlaces <a>.
"a[href]" → Encuentra todos los enlaces <a> que tengan un href.
"ul li" → Encuentra todos los elementos <li> dentro de una <ul>.
"""
    
