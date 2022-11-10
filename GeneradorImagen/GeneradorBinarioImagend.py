import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from PIL import Image
# import ExtractorDeCodigo.Scripper
# import ConversorCodigoBinario.Conversor
# from skimage import io
# codWeb = ExtractorDeCodigo.Scripper.extraccionCodigoWeb()
# codBin = ConversorCodigoBinario.Conversor.texto_a_binario(codWeb)
# val = codBin.split(",")
# Lectura y almacenamiento del código binario.

# Valores necesarios para la generación de la imagen.

def evaluarValoresMap(listString):
    tam = (500, 500)
    img = np.ones(tam)
    ct = 0
    dicMapBinP = {1: 0, 0.9: 100, 0.8: 100000, 0.7: 110000, 0.6: 111010, 0.5: 1000000,
                  0.4: 1011011, 0.3: 1100000, 0.2: 1111010, 0.1: 1111111, 0.0: 11111111}
    # listString = ['1000001', '1101110', '11100001', '1101100', '1101001', '11111111', '1110011', '1101001', '1110011', '100000', '1100100', '1100101', '100000', '1110000', '11100001', '1100111', '1101001', '1101110', '1100001', '1110011', '100000', '1110111', '1100101', '1100010', '100000', '1110000', '1101111', '1110010', '100000', '1101101', '1100101', '1100100', '1101001', '1101111', '100000', '1100100',
    # '1100101', '100000', '1110010', '1100101', '1100011', '1110101', '1110000', '1100101', '1110010', '1100001', '1100011', '1101001', '11110011', '1101110', '100000', '1100100', '1100101', '100000', '1100100', '1100001', '1110100', '1101111', '1110011', '100000', '1100011', '1101111', '1101110', '100000', '1110111', '1100101', '1100010', '100000', '1110011', '1100011', '1110010', '1100001', '1110000', '1101001']

    # Convertir lista de datos cadena en lista de datos enteros.
    listInt = [int(n) for n in listString]
    # Calcula el número total de elementos de la matriz.
    tamTotMat = tam[1] ** 2
    for y in range(tamTotMat):
        if (len(listInt) < tamTotMat):
            listInt.append(0)
    for i in range(500):
        for j in range(500):
            # print("Coordenadas: ", i, ",", j, " correspondientes a: ", listInt[ct])
            if (listInt[ct] < dicMapBinP[1]):
                # print(listInt[ct], "Tiene el valor de 1")
                img[i, j] = 1
            elif (listInt[ct] >= dicMapBinP[1] and listInt[ct] < dicMapBinP[0.9]):
                # print(listInt[ct], "Tiene el valor de 0.9")
                img[i, j] = 0.9
            elif (listInt[ct] >= dicMapBinP[0.9] and listInt[ct] < dicMapBinP[0.8]):
                # print(listInt[ct], "Tiene el valor de 0.8")
                img[i, j] = 0.8
            elif (listInt[ct] >= dicMapBinP[0.8] and listInt[ct] < dicMapBinP[0.7]):
                # print(listInt[ct], "Tiene el valor de 0.7")
                img[i, j] = 0.7
            elif (listInt[ct] >= dicMapBinP[0.7] and listInt[ct] < dicMapBinP[0.6]):
                # print(listInt[ct], "Tiene el valor de 0.6")
                img[i, j] = 0.6
            elif (listInt[ct] >= dicMapBinP[0.6] and listInt[ct] < dicMapBinP[0.5]):
                # print(listInt[ct], "Tiene el valor de 0.5")
                img[i, j] = 0.5
            elif (listInt[ct] >= dicMapBinP[0.5] and listInt[ct] < dicMapBinP[0.4]):
                # print(listInt[ct], "Tiene el valor de 0.4")
                img[i, j] = 0.4
            elif (listInt[ct] >= dicMapBinP[0.4] and listInt[ct] < dicMapBinP[0.3]):
                # print(listInt[ct], "Tiene el valor de 0.3")
                img[i, j] = 0.3
            elif (listInt[ct] >= dicMapBinP[0.3] and listInt[ct] < dicMapBinP[0.2]):
                # print(listInt[ct], "Tiene el valor de 0.2")
                img[i, j] = 0.2
            elif (listInt[ct] >= dicMapBinP[0.2] and listInt[ct] < dicMapBinP[0.1]):
                # print(listInt[ct], "Tiene el valor de 0.1")
                img[i, j] = 0.1
            elif (listInt[ct] >= dicMapBinP[0.1] and listInt[ct] < dicMapBinP[0.0]):
                # print(listInt[ct], "Tiene el valor de 0.0")
                img[i, j] = 0.0
        # print(listInt[ct])
            ct += 1
    plt.imshow(img, vmin=0, vmax=1)
    plt.waitforbuttonpress(0)
    plt.close()
    plt.imsave('new_1.png',img)

# evaluarValoresMap()
# plt.savefig("GeneradorImagen/imGenBin.png")
