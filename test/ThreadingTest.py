import os
import threading
#import cv2
import time
from visual import Visual
from visual import play_video
from testVisuals import Test
from testVisuals import do_test
from testVisuals2 import Test2
from testVisuals2 import try_again

show = Visual()
#Play the first video
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../test/test_assets/video1.MOV")
#play_video(show, path)
show.currShow = path
play_video = threading.Thread(target=play_video, args=(show, show.currShow))
doTest = threading.Thread(target=try_again, args=())
play_video.start()
doTest.start()
doTest.join()
print("They done")

