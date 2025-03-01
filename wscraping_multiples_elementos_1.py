"""
✅ Usamos find_all("p") para obtener todos los párrafos <p> de la página.
✅ Usamos find_all("a") para obtener todos los enlaces <a> y sus URLs (href).
✅ Usamos un bucle for para recorrer y mostrar los resultados numerados."""


import requests
from bs4 import BeautifulSoup

#url de la pagina a examinar

url = 'https://example.com'

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
    for i, parrafos in enumerate(parrafos, start = 1): #utilizamos enumerate para numerar los resultados
        print(f"{i}: {parrafos.text}\n")
        
    #obtenemos todos los enlances <a> de la pagina
    enlaces = soup.find_all("a")
    
    #mostrar los resultados
    print("Enlaces de la pagina:")
    for i, enlaces in enumerate(enlaces, start = 1):
        print(f"{i}: Texto: {enlaces.text} - URL: {enlaces['href']}")
        
else:
    print(f"error de solicitud: {response.stauus_code}")