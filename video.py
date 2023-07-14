import cv2
import numpy as np

cam = cv2.VideoCapture(0) # link to webcam

while cam.isOpened():
    status, img =cam.read()
    if status is None:
        break 
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    stack = np.hstack((img, rgb))
    cv2.imshow('webcam',stack)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cam.release()    