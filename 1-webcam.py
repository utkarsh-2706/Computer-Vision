import cv2
import os

video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Error: Could not open webcam.")
    exit()
    
while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    cv2.imshow('Webcam Feed', frame)
    
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()