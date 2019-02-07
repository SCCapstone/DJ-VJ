"""
This test file tests the get_pitch function found in the Pitch class
which takes in a frequency in Hz and converts it to its musical
note representation
"""

import unittest
import djvj.pitch as pitch


class TestFreqToNote(unittest.TestCase):
    """
    This is the test case for the get_pitch function
    """

    @classmethod
    def setUpClass(cls):
        print("Unit Test: freq_to_note")

    def setUp(self):
        # values referenced from here: http://pages.mtu.edu/~suits/notefreqs.html
        self.test_1 = 440  # A4
        self.test_2 = 16.35  # C0 lowest musical note notation
        # in between D#0 and E0, should round down to D#0, lowest pitch humans can hear
        self.test_3 = 20
        self.test_4 = 261.63  # C4, middle C
        self.test_5 = 7902.13  # B8 highest musical note notation
        self.test_6 = 20000.01  # highest pitch humans can hear
        self.test_7 = 84  # in between E2 and F2, should round down to E2 b/c difference is closer
        self.test_8 = 85  # in between E2 and F2, should round up to F2 , b/c difference is closer

    def test_1(self):  # pylint: disable=E0202
        """
        This method calls the get_pitch method on the test_1
        """

        # test 1
        self.test_1 = pitch.get_pitch(self.test_1)
        self.assertEqual(self.test_1, "A4")

    def test_2(self):  # pylint: disable=E0202
        """
        This method calls the get_pitch method on the test_2
        """

        # test 2
        self.test_2 = pitch.get_pitch(self.test_2)
        self.assertEqual(self.test_2, "C0")

    def test_3(self):  # pylint: disable=E0202
        """
        This method calls the get_pitch method on the test_3
        """
        # test 3
        self.test_3 = pitch.get_pitch(self.test_3)
        self.assertEqual(self.test_3, "D#0")

    def test_4(self):  # pylint: disable=E0202
        """
        This method calls the get_pitch method on the test_4
        """
        # test 4
        self.test_4 = pitch.get_pitch(self.test_4)
        self.assertEqual(self.test_4, "C4")

    def test_5(self):  # pylint: disable=E0202
        """
        This method calls the get_pitch method on the test_5
        """
        # test 5
        self.test_5 = pitch.get_pitch(self.test_5)
        self.assertEqual(self.test_5, "B8")

    def test_6(self):  # pylint: disable=E0202
        """
        This method calls the get_pitch method on the test_6
        """
        # test 6
        self.test_6 = pitch.get_pitch(self.test_6)
        self.assertEqual(self.test_6, "")

    def test_7(self):  # pylint: disable=E0202
        """
        This method calls the get_pitch method on the test_7
        """
        # test 7
        self.test_7 = pitch.get_pitch(self.test_7)
        self.assertEqual(self.test_7, "E2")

    def test_8(self):  # pylint: disable=E0202
        """
        This method calls the get_pitch method on the test_8
        """
        # test 8
        self.test_8 = pitch.get_pitch(self.test_8)
        self.assertEqual(self.test_8, "F2")


if __name__ == '__main__':
    unittest.main()
