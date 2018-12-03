"""video playback code"""
import os
import cv2


MY_PATH = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(MY_PATH, "../test/VATest.mp4")
CAP = cv2.VideoCapture(PATH)
RET, FRAME = CAP.read()
while 1:
	cv2.destroyAllWindows()
    RET, FRAME = CAP.read()
    cv2.imshow('frame', FRAME)
    if cv2.waitKey(1) & 0xFF == ord('q')  or RET == False:
        CAP.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow('frame', FRAME)
