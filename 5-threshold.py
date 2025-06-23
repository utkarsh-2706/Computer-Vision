import os
import cv2

image_path = os.path.join('.', 'IMG-20211018-WA0004.jpg')

image = cv2.imread(image_path)

image = cv2.resize(image, (800, 500))
imageGRAY = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bulrred_image = cv2.medianBlur(imageGRAY, 5) 
ret, thresh1 = cv2.threshold(bulrred_image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Image', image)
cv2.imshow('Image GRAY', imageGRAY)
cv2.imshow('Threshold', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()