import os
import cv2
import numpy as np

image_path = os.path.join('.', 'whiteboard.png')

image = cv2.imread(image_path)
image = cv2.resize(image, (800, 500))

#line - (image, start_point, end_point, color, thickness)
cv2.line(image, (100, 200), (300, 450), (0, 255, 0), 5)

#rectangle - (image, start_point, end_point, color, thickness)
cv2.rectangle(image, (100, 200), (300, 450), (255, 0, 0), 5)

#circle - (image, center, radius, color, thickness)
cv2.circle(image, (400, 300), 50, (0, 0, 255), 5)

#text - (image, text, org, font, font_scale, color, thickness)
cv2.putText(image, 'Hello OpenCV', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 55), 2)  

cv2.imshow('Original Image', image) 
cv2.waitKey(0)