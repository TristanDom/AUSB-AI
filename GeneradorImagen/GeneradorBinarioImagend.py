import cv2
import numpy as np

img1 = np.zeros((10, 8), np.uint8)
# img2 = 255*np.zeros((10, 8), np.uint8)

img1[1, 0, 1, 0, 1] = 200
# img2[3,6] = 200

cv2.imshow('imgZeros', img1)
# cv2.imshow('imgOnes', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()