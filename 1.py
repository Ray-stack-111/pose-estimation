import cv2
import numpy as np
def video_demo():
    capture = cv2.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow("video", frame)
        c = cv2.waitKey(50)
        if c == 27:
            break
video_demo()
cv2.destroyAllWindows()
