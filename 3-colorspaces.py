import os
import cv2

image_path = os.path.join('.', 'IMG-20211018-WA0004.jpg')

image = cv2.imread(image_path)

image = cv2.resize(image, (800, 500))

imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
imageGRAY = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# imageHLS = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
# imageLAB = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
# imageYUV = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)   

cv2.imshow('Image', image)
cv2.imshow('Image RGB', imageRGB)
cv2.imshow('Image GRAY', imageGRAY)
# cv2.imshow('Image HSV', imageHSV)
# cv2.imshow('Image HLS', imageHLS)
# cv2.imshow('Image LAB', imageLAB)
# cv2.imshow('Image YUV', imageYUV)
cv2.waitKey(0)
cv2.destroyAllWindows()

