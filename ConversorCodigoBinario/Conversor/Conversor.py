"""Conversor.
Este es un programa que convierte código extraído de
páginas web en código binario almacenándolo en archivos txt con la ruta deseada."""

#Por medio de la función open() se abre el archivo que se desea leer.
with open('PaginasEscaneadas/Codigos de paginas/Paginas confiables/Wikipedia.html') as archivo:
    contenido = archivo.read()

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