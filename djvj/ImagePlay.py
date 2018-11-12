"""video playback code"""
import cv2
class Imageplay:
    """plays image within the Test folder"""	
    CAP = cv2.VideoCapture("/Users/omaririchards/Dropbox/Uni/Semesters/Fall 2018/CSCE 490/DJ-VJ/test/VATest.mp4")
    RET, FRAME = CAP.read()
    while 1:
        RET, FRAME = CAP.read()
        cv2.imshow('frame', FRAME)
        if cv2.waitKey(1) & 0xFF == ord('q')  or RET == False:
            CAP.release()
            cv2.destroyAllWindows()
            break
        cv2.imshow('frame', FRAME)

def init():
    """ allows this code to be run from main.py """
    Imageplay().mainloop()
