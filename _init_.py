import ExtractorDeCodigo.Scripper
import ConversorCodigoBinario.Conversor

listBin = []
#Impresión de información acerca del código.
print("""Bienvenid@ al sistema de reconocimiento de sítios maliciosos por medio de mapeo y análisis de imágenes por medio de inteligencia artificial, este sistema se encuentra en fase de desarrollo, por lo que no se recomienda su uso en entornos de producción, el sistema se encuentra bajo licencia GNU GPL v3.0., este sistema se encuentra en desarrollo por la autoría de Tristán Domínguez 'https://github.com/'""")
#Mensaje de confirmación de uso del sistema.
resp = input("¿Desea continuar con el proceso de reconocimiento de sítios maliciosos?: ")
#Toma de decisión de uso del sistema.
if(resp == "si" or resp == "Si" or resp == "SI" or resp == "s"):
    print("Iniciando proceso de reconocimiento de sítios maliciosos...")
    print("Iniciando proceso de extracción de código...")
    #Llamado de la función de extracción de código de la página web y almacenado del código extraído en la variable 'codigo'.
    codWeb = ExtractorDeCodigo.Scripper.extraccionCodigoWeb()    
    print("Iniciando proceso de conversión de código a binario...")
    #Llamado de la función de conversión de código a binario y almacenado del código binario en la variable 'codigoBinario'.
    # codBin = ConversorCodigoBinario.Conversor.texto_a_binario(codWeb)
    codBin = ConversorCodigoBinario.Conversor.mainConversor(codWeb)
else:
    print("No se iniciará el proceso de reconocimiento de sítios maliciosos.")
    exit()

for bin in codBin:
    listBin.append(bin)


