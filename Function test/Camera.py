import numpy as np
import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()