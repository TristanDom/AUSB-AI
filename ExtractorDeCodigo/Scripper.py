import requests
from bs4 import BeautifulSoup
import requests 

#Código de extracción de código de una página web, con el uso de la librería de beautifulsoup4, para el sistema de sistema de reconocimiento de sítios maliciosos por medio de mapeo y análisis de imágenes por medio de inteligencia artificial.

#Realización de función para la extracción de código de una página web, enlazada al archivo principal por medio de módulos y paquetes.
def extraccionCodigoWeb():
    #Ingreso de la página web a extraer el código.
    url = input("Ingrese la página web a extraer el código: ")
    #Petición de la página web.
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    #Impresión del código de la página web.
    imp = input("Desea imprimir el código extraído de la página web?: ")
    #Impresión de decisión de impresión del código extraído de la página web.
    if(imp == "si" or imp == "Si" or imp == "SI" or imp == "s"):
        print("Imprimiendo código extraído de la página web...")
        print(soup.prettify())
        #Retorno del código extraído de la página web.
        return soup.prettify()
    else:
        #Mensaje de no impresión del código extraído de la página web.
        print("No se imprimirá el código extraído de la página web.")
        #Retorno del código extraído de la página web.
        return soup.prettify()