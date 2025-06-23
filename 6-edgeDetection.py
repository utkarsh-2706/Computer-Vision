import os
import cv2
import numpy as np

image_path = os.path.join('.', 'IMG-20211018-WA0004.jpg')

image = cv2.imread(image_path)

image = cv2.resize(image, (800, 500))

img_edge = cv2.Canny(image, 100, 200)

img_egde_dilated = cv2.dilate(img_edge, np.ones((2,2),dtype=np.int8))

img_erode = cv2.erode(img_egde_dilated, np.ones((5,5),dtype=np.int8))

cv2.imshow('Edge Detected Image', img_edge)
cv2.imshow('Dilated Edge Detected Image', img_egde_dilated)
cv2.imshow('Eroded Edge Detected Image', img_erode)
cv2.waitKey(0)
cv2.destroyAllWindows()