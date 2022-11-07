"""Conversor.
Este es un programa que convierte código extraído de
páginas web en código binario almacenándolo en archivos txt con la ruta deseada."""

#Se ingresa de manera el archivo a convertir.
ruta = input("Ingrese si el archivo procede de una página confiable o no: ")
if ruta == "si" or ruta == "Si" or ruta == "SI" or ruta == "s":
    print("Ha seleccionado un archivo confiable.")
    ruta = 'PaginasEscaneadas/Codigos de paginas/PaginasConfiables/'

elif ruta == "no" or ruta == "No" or ruta == "NO" or ruta == "n":
    print("Ha seleccionado un archivo no confiable.")
    ruta = 'PaginasEscaneadas/Codigos de paginas/PaginasNoConfiables/'

nombre = input("Ingrese el nombre del archivo: ")

tipo = input("Ingrese el tipo de archivo: ")

rutaCompleta = ruta + nombre + "." + tipo

if tipo == 'txt':
    print("Archivo de tipo txt leído correctamente.")
    print(rutaCompleta)
    with open(rutaCompleta) as archivo:
        contenido = archivo.read()
        
elif tipo == 'html':
    print("Archivo de tipo html leído correctamente.")
    print(rutaCompleta)
    with open(rutaCompleta) as archivo:
        contenido = archivo.read()
        
# #Por medio de la función open() se abre el archivo que se desea leer.
# with open('Wikipedia.html') as archivo:
#     contenido = archivo.read()

#Por medio de la fución ascii_a_binario() se convierte carcateres a binario.
def ascii_a_binario(letra):
    # Extraer su valor entero
    valor = ord(letra)
    # Convertirlo a binario
    return "{0:08b}".format(valor)

#Por medio de la función binario_a_ascii() se convierte cadenas de caracteres a código binario.
def texto_a_binario(texto):
    texto_binario = ""  # El resultado
    contador = 0
    for letra in texto:
        texto_binario += ascii_a_binario(letra)
        # Agregar un espacio entre binarios, excepto si es el último carácter
        # if contador + 1 < len(texto):
        #     texto_binario += separador
        contador += 1
    return texto_binario

# print(texto_a_binario(contenido))

#Con la implementación de la segunda fución open se sobre esccribe el resultado de convetir cadenas de texto a código binario.
with open('GeneradorImagen/resultariobinario.txt', 'w') as archivo:
     archivo.write(texto_a_binario(contenido))

print(texto_a_binario(contenido))