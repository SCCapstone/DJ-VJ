"""
Runs a simple unit test for the pickle package.
Passes a value to the pickler, and makes sure that the value
stays the same after being pickled and unpickled.
"""

import unittest
import pickle


def pickle_it(param):
    """mimics the file creation/load functions in the djvj_GUI.py file"""
    # create the file
    with open("test.djvj", "wb") as f:
        pickle.dump(param, f)

    # load the file
    with open("test.djvj", "rb") as f:
        data = pickle.load(f)

    # return its contents
    return data


class MyTest(unittest.TestCase):
    """runs the tesets"""

    def test(self):
        """uses the assertEqual python unittest to make sure they're the same"""
        value = "If pitch < 100"
        print("Starting value: ", value)
        self.assertEqual(pickle_it(value), value)
        print("Returned: ", pickle_it(value))


if __name__ == '__main__':
    unittest.main()
