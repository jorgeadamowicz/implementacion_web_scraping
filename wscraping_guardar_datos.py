"""
✅ Importamos las bibliotecas necesarias (requests, BeautifulSoup y csv).
✅ Hacemos la solicitud a la URL con requests.get().
✅ Verificamos que la solicitud fue exitosa con response.status_code.
✅ Traducimos el contenido HTML con BeautifulSoup().
✅ Extraemos la información deseada utilizando soup.select() o soup.find_all().
✅ Guardamos los datos extraídos en un archivo .csv usando csv.writer().
✅ Aplicamos .strip() para limpiar los datos antes de guardarlos.

"""
import requests
from bs4 import BeautifulSoup
import csv

#url de la pagina a examinar
url = "https://es.wikipedia.org/wiki/Python"

#hacemos la solicitud HTTP con requests.get()
response = requests.get(url)

#verificamos la solicitud
if response.status_code == 200:
    print(f"Solicitud exitosa\n")
    
    #analizamos el contenido de la pagina con Beautifulsoup. Convirtiendo el HTML en un objeto que podemos recorrer y analizar.
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #obtenemos el contenido de algunos parrafos <div> de la página
    parrafos = soup.select('div#mw-content-text p')

    #guardamos los datos en un archivo .csv
    with open("datos.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        
        #escribimos la fila de los encabezados
        writer.writerow(["Número", "Texto del párrafo"])
        
        #Escribimos los datos en el archivo
        for i, parrafo in enumerate(parrafos [:10], start = 1):
            writer.writerow([i, parrafo.text.strip()])
    print('Datos guardados en "datos.csv" exitosamente!')

else:
    print(f'Error de solicitud: {response.status_code}')
    
        
    
    
    