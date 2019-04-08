"""
Script that test the visuals code
"""
import os
import threading
import time
#from visual import Visual
#from visual import play_video
from video_player import VideoPlayer
import video_player as vid
#from video_player import play_video
"""
#Initialize show
show = Visual()

#Play the first video
print("We here")

my_path = os.path.abspath(os.path.dirname(__file__))
#Set the video paths for the two videos
path1 = os.path.join(my_path, "../test/test_assets/video1.MOV")
path2 = os.path.join(my_path, "../test/test_assets/Eat_it_Duke.mp4")

#Set the videos in show
#show.currShow = path1
show.newShow = path1
#Initialize thread and play the first videos
print("Try first video")
first = threading.Thread(target=play_video, args=(show,))
first.start()

#time sleep the give time for the first video to run 
time.sleep(3)

#Update new show and run it
print("Try the second show")
show.newShow = path2

first = threading.Thread(target=play_video, args=(show))
# Pass the second show through again to make sure the video keeps playing
time.sleep(4)
print("See if it changes")

#See if it stays on the same show
first = threading.Thread(target=play_video, args=(show))
print("We did it!")
"""
my_path = os.path.abspath(os.path.dirname(__file__))
#Set the video paths for the two videos
path1 = os.path.join(my_path, "../test/test_assets/Eat_it_Duke.mp4")
doIt = vid.VideoPlayer(path1)
#doIt.play_video()
doIt.play_video().pause()