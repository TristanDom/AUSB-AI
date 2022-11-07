"""Conversor.
Este es un programa que convierte código extraído de
páginas web en código binario almacenándolo en archivos txt con la ruta deseada."""

with open('PaginasEscaneadas/Codigos de paginas/Paginas confiables/Wikipedia.html') as archivo:
    contenido = archivo.read()
    #print(contenido)

def ascii_a_binario(letra):
    # Extraer su valor entero
    valor = ord(letra)
    # Convertirlo a binario
    return "{0:08b}".format(valor)

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

# with open('/home/hunter/Documentos/AUSB/PaginasEscaneadas/Codigos de paginas/Paginas confiables/resultariobinario.txt', 'w') as archivo:
#     archivo.write(texto_a_binario(contenido))

print(texto_a_binario(contenido))