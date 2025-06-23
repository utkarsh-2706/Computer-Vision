import numpy as np
import cv2
from PIL import Image

def get_limits(color):
    
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    lowerlimit = np.array([hsvC[0][0][0] - 10, 100, 100])
    upperlimit = np.array([hsvC[0][0][0] + 10, 255, 255])
    
    return lowerlimit, upperlimit


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerlimit, upperlimit = get_limits((0, 255, 255))  # yellow color limits
    
    mask = cv2.inRange(hsvImage, lowerlimit, upperlimit)
    
    mask_ = Image.fromarray(mask)
    box = mask_.getbbox()
    
    if box is not None:
        x1, y1, x2, y2 = box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
    cv2.imshow('Original Frame', frame) 
    cv2.imshow('Mask', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()    

cv2.destroyAllWindows()