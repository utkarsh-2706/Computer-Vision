import os
import cv2

image_path = os.path.join('.', 'IMG-20211018-WA0004.jpg')

image = cv2.imread(image_path)

image = cv2.resize(image, (800, 500))


k_size = 7
blurred_image = cv2.blur(image, (k_size, k_size))
gaussian_blurred_image = cv2.GaussianBlur(image, (k_size, k_size), 3)
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Gaussian Blurred Image', gaussian_blurred_image)
cv2.waitKey(0)

k_size = 100
while(k_size > 0):
    blurred_image = cv2.blur(image, (k_size, k_size))
    cv2.imshow('Blurred Image', blurred_image)
    k_size -= 1
    cv2.waitKey(40)
    
cv2.destroyAllWindows()

webcam = cv2.VideoCapture(0)
k_size = 100
while k_size>0:
    ret, frame = webcam.read()
    
    blurred_frame = cv2.blur(frame, (k_size, k_size))
    cv2.imshow('Blurred Webcam Feed', blurred_frame)
    cv2.waitKey(40)
    k_size -= 1
    
webcam.release()    
cv2.destroyAllWindows()
