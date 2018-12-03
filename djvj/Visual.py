import cv2
import sys
import os


class Visual:
    """docstring for ClassName"""

    def __init__(self):
        self.curr_pitch = 0
        # self.curr_pitch = [100, 150, 90, 300, 200, 50]
        # for x in self.curr_pitch:
        #     self.play_video(x)

    def trigger(self):
        print("TRIGGER")
        self.play_video()

    def play_video(self):
        print(self.curr_pitch)
        if self.curr_pitch > 500:
            cv2.destroyAllWindows()
            print("Video 1")
            MY_PATH = os.path.abspath(os.path.dirname(__file__))
            PATH = os.path.join(MY_PATH, "../test/video3.MOV")
            CAP = cv2.VideoCapture(PATH)
            while CAP.isOpened():
                if self.curr_pitch < 500:
                    print("break video 1")
                    break
                RET, frame = CAP.read()
                try:
                    cv2.imshow('video', frame)
                except:
                    pass
                    CAP.release()
                    cv2.destroyAllWindows()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("BREAK")
                    break

        if self.curr_pitch < 500:
            cv2.destroyAllWindows()
            print("Video 2")
            MY_PATH = os.path.abspath(os.path.dirname(__file__))
            PATH = os.path.join(MY_PATH, "../test/VATest.mp4")
            CAP = cv2.VideoCapture(PATH)
            while CAP.isOpened():
                if self.curr_pitch > 500:
                    print("break video 2")
                    break
                RET, frame = CAP.read()
                try:
                    cv2.imshow('video', frame)
                except:
                    pass
                    CAP.release()
                    cv2.destroyAllWindows()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("BREAK")
                    break
