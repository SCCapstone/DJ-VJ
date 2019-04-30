import unittest
import djvj.moment as moment

class TestMoment(unittest.TestCase):
	def test_setUp(self):
		self.a_rule = ["param", ">",1,"video 1"]
		self.b_rule = ["time", "<",2,"video 2"]
		self.c_rule = ["tempo", "=",3,"video 3"]

		self.d_rule = [["tempo", ">",5,"video 4"],["tempo", "<",10,"video 4"]]

	def test_1(self):
		momentv = moment.create_moments(a_rule)
		print(moment)

	def test_2(self):
		momentv = moment.create_moments(b_rule)
		print(moment)

	def test_3(self):
		momentv = moment.create_moments(c_rule)
		print(moment)

	def test_4(self):
		momentv = moment.create_moments(c_rule)
		print(moment)




		






