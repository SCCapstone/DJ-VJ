"""
test_interpreter tests interpter.py
"""


import unittest
import threading
import time
import djvj.moment as moment
import djvj.show as show
import djvj.interpreter as interpreter


class TestInterpreter(unittest.TestCase):
    """
    interpreter testing class
    """

    @classmethod
    def setUpClass(cls):
        """
        sets up test class
        """

        print("Unit Test: interpreter basic tempo")

    @classmethod
    def tearDownClass(cls):
        """
        deconstructs test class
        """
        print('\n')

    def setUp(self):
        # set up list of Moments
        gui_moments = [[['tempo', '<', '500', './test/test_assets/video1.MOV']],
                       [['tempo', '>', '500', './test/test_assets/video2.mp4']]]
        show_moments = moment.create_moments(gui_moments)

        # set up show
        self.test_show_1 = show.Show(show_moments)
        # set up interpreter
        self.test_interpreter = interpreter.Interpreter(self.test_show_1)

        # start interpreter
        interpreter_thread = threading.Thread(
            target=self.test_interpreter.interpret)
        interpreter_thread.start()

    def tearDown(self):
        self.test_interpreter.kill = True

    def test_1(self):
        """
        test_1 sets show params to < 500
        """

        # test_1 show parameter values
        self.test_show_1.curr_param_values = {
            'tempo': 400
        }
        time.sleep(1)
        self.assertEqual(self.test_show_1.curr_video,
                         './test/test_assets/video1.MOV')

    def test_2(self):
        """
        test_2 sets show params to > 500
        """
        self.test_show_1.curr_param_values = {
            'tempo': 600
        }
        time.sleep(1)
        self.assertEqual(self.test_show_1.curr_video,
                         './test/test_assets/video2.mp4')


if __name__ == '__main__':
    unittest.main()
