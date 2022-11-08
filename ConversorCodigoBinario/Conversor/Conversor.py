"""Conversor.
Este es un programa que convierte código extraído de
páginas web en código binario almacenándolo en archivos txt con la ruta deseada."""

#Se ingresa de manera manual el archivo a convertir.
# ruta = input("Ingrese si el archivo procede de una página confiable o no: ")
# if ruta == "si" or ruta == "Si" or ruta == "SI" or ruta == "s":
#     print("Ha seleccionado un archivo confiable.")
#     ruta = 'PaginasEscaneadas/Codigos de paginas/PaginasConfiables/'

# elif ruta == "no" or ruta == "No" or ruta == "NO" or ruta == "n":
#     print("Ha seleccionado un archivo no confiable.")
#     ruta = 'PaginasEscaneadas/Codigos de paginas/PaginasNoConfiables/'

# nombre = input("Ingrese el nombre del archivo: ")

# tipo = input("Ingrese el tipo de archivo: ")

# rutaCompleta = ruta + nombre + "." + tipo

# if tipo == 'txt':
#     print("Archivo de tipo txt leído correctamente.")
#     print(rutaCompleta)
#     with open(rutaCompleta) as archivo:
#         contenido = archivo.read()
        
# elif tipo == 'html':
#     print("Archivo de tipo html leído correctamente.")
#     print(rutaCompleta)
#     with open(rutaCompleta) as archivo:
#         contenido = archivo.read()
        
# #Por medio de la función open() se abre el archivo que se desea leer de manera estática.
# with open('ExtractorDeCodigo/IngresoWeb/Web.txt') as archivo:
#     contenido = archivo.read()

#Por medio de la fución ascii_a_binario() se convierte carcateres a binario.
def ascii_a_binario(caracter):
    # Extraer su valor entero
    valor = ord(caracter)
    # Convertirlo a binario
    
    return "{0:08b}".format(valor)
    #return "{0:0>4X}".format(valor) # Para hexadecimales

#Por medio de la función binario_a_ascii() se convierte cadenas de caracteres a código binario.
def texto_a_binario(texto):
    texto_binario = ""  # El resultado
    contador = 0
    for caracter in texto:
        separador = ","
        texto_binario += ascii_a_binario(caracter)
        # Agregar un espacio entre binarios, excepto si es el último carácter
        if contador + 1 < len(texto):
            texto_binario += separador
        contador += 1

        # Agregar un espacio entre binarios, excepto si es el último carácter
    imp = input("Desea imprimir el código binario?: ")
    
    if(imp == "si" or imp == "Si" or imp == "SI" or imp == "s"):
        print("Imprimiendo código extraído de la página web...")
        print(texto_binario)
        return texto_binario
    else:
        print("No se imprimirá el código extraído de la página web.")
        return texto_binario

    
# for n in range(0, len(contenido)):
#     vecBin.append(texto_a_binario(contenido[n]))

# print(vecBin)


# Con la implementación de la segunda fución open se sobre esccribe el resultado de convetir cadenas de texto a código binario.
# with open('ConversorCodigoBinario/CodigoConvertido/binario.txt', 'w') as archivo:
#     archivo.write(texto_a_binario(contenido))
#     print("El archivo se ha convertido correctamente.")

#Imprime el resultado de la extracción de código.
#print(texto_a_binario(contenido))