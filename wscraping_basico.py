"""Ejercicio 1: Obtener y Analizar HTML. Descarga de HTML y extracción básica.
 
Este ejercicio te ayudará a:
✅ Descargar el contenido de una página web con requests.
✅ Analizar el HTML con BeautifulSoup.
✅ Ver la estructura básica del documento."""

import requests
from bs4 import BeautifulSoup

#url de la pagina a examinar

url = 'https://example.com'

# Realizamos la solicitud GET para obtener el contenido de la pagina
response = requests.get(url)

#verifica si la solicitud fue exitosa
if response.status_code == 200:
    print('Solicitud exitosa')
    
    #analisamos el contenido de la pagina. 
    ## Convierte el contenido de la pagina ("guardado" en response) en un objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    ##mediante notacion de punto accedemos a los difernetes elementos de la pagina:
    #extraer el titulo <title> de la pagina 
    titulo = soup.title.text
    print(f"El titulo de la pagina es: {titulo}")
    
    #extraer el encabezado <h1> de la pagina
    h1_text = soup.h1.text
    print(f"El encabezado de la pagina es: {h1_text}")
    
    #extraer el contenido del parrafo <p> de la pagina
    parrafo = soup.p.text
    print(f"El contenido del parrafo es: {parrafo}")
    
    #extraer el contenido de la etiqueta <a> enlace de la pagina
    a_text = soup.a.text
    print(f"El contenido de la etiqueta <a> es: {a_text}")
    
    #extrer el enlace de la etiqueta <a> de la pagina
    a_url = soup.a["href"]
    print(f"El enlace de la etiqueta <a> es: {a_url}")
    
    
    #imprimimos el contenido de la pagina formateado
    print(soup.prettify())
else:
    print("error en la solicitud")