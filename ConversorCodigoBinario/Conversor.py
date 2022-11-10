"""Conversor.
Este es un programa que convierte código extraído de
páginas web en código binario almacenándolo en archivos txt con la ruta deseada."""

# Lista vacía para almacenar el código binario.
# listCodBin = []


# Se le asigna el parámetro caracter a la función ascii_a_binario().
def ascii_a_binario(caracter):
    # Extraer su valor entero
    valor = ord(caracter)
    # Convertirlo a binario
    return "{0:08b}".format(valor)
    # return "{0:0>4X}".format(valor) # Para hexadecimales


# Función por mediod de generadores para la conversión de código binario a texto, ejerciendo una mayor eficacia y ahorro de memoria con la generación de objetos iterables.
# Se le asigna el parámetro texto a la función texto_a_binario().
def texto_a_binario(texto):
    for caracter in texto:
        yield ascii_a_binario(caracter)


# Función principal para genera r el código extraído a binario.
# Se le asigna el parámetro codigo a la función mainConversor().
def mainConversor(codigo):
    codConvert = texto_a_binario(codigo)
    # for bin in codConvert:
    #     listCodBin.append(bin)
    # imp = input("¿Desea con el código binario en la consola?: ")
    # if (imp == "si" or imp == "Si" or imp == "SI" or imp == "s"):
    #     print("El código ha sido convertido a binario y almacenado de forma exitosa.")
    #     print("Fin de la impresión del código binario en la consola.")
    #     num = 1
    #     for bin in codConvert:
    #         print(bin)
    # else:
    #     print("El código ha sido convertido a binario y almacenado de forma exitosa.")
    return codConvert