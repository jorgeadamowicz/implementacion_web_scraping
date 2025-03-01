"""
✅ Cambiamos la URL a Wikipedia.
✅ Usamos .strip() para limpiar espacios extra en los textos.
✅ Limitamos la cantidad de párrafos y enlaces mostrados ([:5] y [:10]) para no saturar la terminal.
✅ Filtramos los enlaces con href=True para evitar errores con etiquetas <a> sin URL."""

import requests
from bs4 import BeautifulSoup

#url de la pagina a examinar

url = "https://es.wikipedia.org/wiki/Python"

# Realizamos la solicitud GET para obtener el contenido de la pagina
response = requests.get(url)

#verifica si la solicitud fue exitosa
if response.status_code == 200:
    print('Solicitud exitosa\n')
    
    #analisamos el contenido de la pagina. 
    ## Convierte el contenido de la pagina ("guardado" en response) en un objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #obtenemos todos los parrafos <p> de la pagina
    parrafos = soup.find_all("p")
    
    #mostrar los resultados
    print("Parrafos de la pagina:")
    for i, parrafos in enumerate(parrafos[:5], start = 1):#mostramos solo los 5 primeros parrafos
        print(f"{i}: {parrafos.text.strip()}\n") #strip() elimina los espacios en blanco al inicio y al final
        
    #obtenemos todos los enlances <a> de la pagina
    enlaces = soup.find_all("a", href = True) #filtramos los enlaces con href=True para evitar errores con etiquetas <a> sin URL
    
    #mostrar los resultados
    print("Enlaces de la pagina:")
    for i, enlaces in enumerate(enlaces[:5], start = 1): #utilizamos enumerate para numerar los resultados
        print(f"{i}: Texto: {enlaces.text.strip()} - URL: {enlaces['href']}")
        
else:
    print(f"error de solicitud: {response.stauus_code}")