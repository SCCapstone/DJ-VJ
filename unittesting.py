import unittest
import threading
import djvj.audio_listener as audio
import djvj.interpreter as interpreter
import djvj.video_player as video_player
import djvj.show as show

class Testing(unittest.TestCase):

	def test_video(self):
		SHOW = show.SHOW("")
		my_path = os.path.abspath(os.path.dirname(__file__))
		SHOW.curr_video = os.path.join(my_path, "../test/test_assets/Eat_it_Duke.mp4")
		SHOW.video_player.play_video()

suite = unittest.TestLoader().loadTestsFromTestCase(Testing)
unittest.TextTestRunner(verbosity=2).run(suite)

	