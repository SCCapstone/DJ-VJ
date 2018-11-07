"""video playback code"""
import cv2

CAP = cv2.VideoCapture("VATest.mp4")
RET, FRAME = CAP.read()
while 1:
    RET, FRAME = CAP.read()
    cv2.imshow('frame', FRAME)
    if cv2.waitKey(1) & 0xFF == ord('q')  or RET == False:
        CAP.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow('frame', FRAME)
