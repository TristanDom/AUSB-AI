import requests
from bs4 import BeautifulSoup
import requests 

#Realización de función para la extracción de código de una página web, enlazada al archivo principal por medio de módulos y paquetes.
def extraccionCodigoWeb():
    #Ingreso de la página web a extraer el código.
    url = input("Ingrese la página web a extraer el código: ")
    #Petición de la página web.
    r = requests.get(url)
    #Extracción del código de la página web.
    soup = BeautifulSoup(r.content, 'html.parser')
    #Impresión del código de la página web.
    imp = input("Desea imprimir el código extraído de la página web?: ")
    
    if(imp == "si" or imp == "Si" or imp == "SI" or imp == "s"):
        print("Imprimiendo código extraído de la página web...")
        print(soup.prettify())
        return soup.prettify()
    else:
        print("No se imprimirá el código extraído de la página web.")
        return soup.prettify()

# # URL a la página la cual se desea extraer el código.
# url = input("Ingrese la ruta de la página web: ")
# #url = "https://blogthinkbig.com/etiquetas-html-importantes-memorizar"
  
# #Mandar solicitud a la página y asignarla a una variable.
# result = requests.get(url)

# #Almacenar el contenido de la página en una variable.
# content = result.text

# #Crear un objeto BeautifulSoup con el contenido de la página.
# soup = BeautifulSoup(content, 'lxml')

# #Imprimir el código de la página con un formato legible.
# # print(soup.prettify())

# with open('ExtractorDeCodigo/IngresoWeb/Web.txt', 'w') as archivo:
#     archivo.write(soup.prettify())
#     print("La página se ha extraído correctamente.")