import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from PIL import Image
import random
import ConversorCodigoBinario.Conversor.Conversor as conversor

#Lectura y almacenamiento del código binario.
with open('ConversorCodigoBinario/CodigoConvertido/binario.txt') as archivo:
    contenido = archivo.read()

print(conversor.texto_a_binario(contenido))
vecBin = []

for n in range(0, len(contenido)):
    vecBin.append(texto_a_binario(contenido[n]))# print(contenido[0:8])