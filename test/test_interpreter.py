"""
"""


import unittest
import threading
import time
import djvj.moment as moment
import djvj.show as show
import djvj.interpreter as interpreter


class TestInterpreter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Unit Test: interpreter")

    @classmethod
    def tearDownClass(cls):
        print('\n')

    def test_1(self):
        # set up list of Moments
        gui_moments = [[['pitch', '<', '500', '/Users/matt/Desktop/Demo/mario theme.mp4']],
                       [['pitch', '>', '500', '/Users/matt/Desktop/Demo/luigi.mp4']]]
        show_moments = moment.create_moments(gui_moments)

        # set up show
        self.test_show_1 = show.Show(show_moments)
        # set up interpreter
        self.test_interpreter = interpreter.Interpreter(self.test_show_1)

        # test_1 show parameter values
        self.test_show_1.curr_param_values = {
            'pitch': 400
        }

        # start interpreter
        interpreter_thread = threading.Thread(
            target=self.test_interpreter.interpret)
        interpreter_thread.start()

        self.assertEqual(self.test_show_1.curr_video,
                         '/Users/matt/Desktop/Demo/mario theme.mp4')

        self.test_show_1.curr_param_values = {
            'pitch': 600
        }

        self.test_interpreter.kill = True


if __name__ == '__main__':
    unittest.main()
