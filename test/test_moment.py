import unittest
import djvj.moment as moment

class TestMoment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Unit Test: moment")

    def setUp(self):
        self.a_rule = [[['pitch', '<', '4', 'video1']]]
        self.b_rule = [[["time", "<", '2', "video 2"]]]
        self.c_rule = [[["tempo", "=", 3, "video 3"]]]

        self.d_rule = [[["tempo", ">", 5, "video 4"],["tempo", "<",10,"video 4"]]]

    def test_1(self):
        momentv = moment.create_moments(self.a_rule)
        print (momentv)

    def test_2(self):
        momentv = moment.create_moments(self.b_rule)
        print (momentv)

    def test_3(self):
        momentv = moment.create_moments(self.c_rule)
        print (momentv)

    def test_4(self):
        momentv = moment.create_moments(self.d_rule)
        print (momentv)

if __name__ == '__main__':
    unittest.main()



		






