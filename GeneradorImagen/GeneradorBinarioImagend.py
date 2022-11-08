import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from PIL import Image
import random
import ConversorCodigoBinario.Conversor as conversor

dicMapBin = {0: 1, 100: 0.9, 100000: 0.8, 110000: 0.7, 111010: 0.6, 1000000: 0.5, 1011011: 0.4, 1100000:0.3, 1111010: 0.2, 1111111: 0.1, 11111111: 0.0}

#Lectura y almacenamiento del código binario.
with open('ConversorCodigoBinario/CodigoConvertido/binario.txt') as archivo:
    contenido = archivo.read()

print(conversor.texto_a_binario(contenido))
vecBin = []

for n in range(0, len(contenido)):
    vecBin.append(texto_a_binario(contenido[n]))# print(contenido[0:8])