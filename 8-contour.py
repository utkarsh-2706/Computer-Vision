import os
import cv2
import numpy as np

image_path = os.path.join('.', 'birds.png')

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(f'Number of contours found: {len(contours)}')

for cnt in contours:
    print(cv2.contourArea(cnt))
    if(cv2.contourArea(cnt) > 100):
        # (image, contours, contourIdx, color, thickness))
        # cv2.drawContours(image, [cnt], -1, (255, 0, 0), 10)
        
        # boxes around contours 
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

cv2.imshow('Original Image', image)
# cv2.imshow('Thresholded Image', thresh)

cv2.waitKey(0)