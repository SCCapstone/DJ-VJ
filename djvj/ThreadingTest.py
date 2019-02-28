import os
import threading
#import cv2
import time
from visual import Visual
from visual import play_video
from testVisuals import Test
from testVisuals import do_test


show = Visual()
#Play the first video
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../test/test_assets/video1.MOV")
play_video(show, path)

doTest = threading.Thread(target=do_test, args=())
doTest.start()

