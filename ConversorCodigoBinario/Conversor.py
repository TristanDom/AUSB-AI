"""Conversor.
Este es un programa que convierte código extraído de
páginas web en código binario almacenándolo en archivos txt con la ruta deseada."""

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