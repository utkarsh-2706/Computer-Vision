import os
import cv2

image_path = os.path.join('.', 'IMG-20211018-WA0004.jpg')

image = cv2.imread(image_path)

#cv2.imshow('Image', image)
#print(image.shape)

resized_image = cv2.resize(image,(640, 480))
cv2.imshow('Resized Image', resized_image)

cropped_image = resized_image[200:400, 250:450]
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)

cv2.destroyAllWindows()