import unittest
import threading
#import audio_listener as audio
#import interpreter as interpreter
import video_player as video_player
import show as show

class Testing(unittest.TestCase):

	def test_video(self):
		SHOW = show.SHOW("")
		SHOW.curr_video = os.path.join(my_path, "../test/test_assets/Eat_it_Duke.mp4")
		SHOW.video_player.play_video()

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

	