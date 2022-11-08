import cv2
import numpy as np
from PIL import Image
#import random
import matplotlib.pyplot as plt

#Lectura y almacenamiento del código binario.
with open('ConversorCodigoBinario/CodigoConvertido/binario.txt') as archivo:
    contenido = archivo.read()


# img1 = np.zeros((10, 8), np.uint8)
# # img2 = 255*np.zeros((10, 8), np.uint8)

# img1[2, 4] = 200
# # img2[3,6] = 200

# cv2.imshow('imgZeros', img1)
# # cv2.imshow('imgOnes', img2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
img = np.random.random((50,50,3))
plt.imshow(img)

doc = Image.fromarray(np.uint8(img))
doc.save('test.jpeg')

img = np.random.random((25,25,3))
plt.imshow(img)