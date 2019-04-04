

class Bugger:

	def __init__(self, temp_momment, official_momment):
		#current param
		self.t_param = temp_momment[1]
        #sign
        self.t_sign = temp_momment[2]
        #value
        self.t_value = temp_momment[3]

        self.ops = {
            "<": operator.le,
            ">": operator.gt,
            '=': operator.eg,
        }
        #error counter 
        self.strike = 0
        #main moment that will be used in the show class
        self.official_momment = official_momment

	def momment_check(self):
		# if the main momment is empty
		if official_momment != True:
			return True
		'''
		Iterates through the lists within the list
		  List1.   List2    List2
		[[A,B,C], [D,E,F], [G,H,I]]
		'''
		for x in self.official_momment:
			'''
			Iterates through the objects within a single list
			 Object1 Object2 Object3
			[A,      B,      C]
			'''
			for y in x:
				'''
				compare current momment param to existing momment param
				ex:
				Pitch = Pitch 
				''' 
				if t_param == y[1]:
					'''
					if current momment meets the condition of any existing momments, flag it
					ex:
					t_value = 3
					y[3] = 5

					if tvalue < y[3]
					flag this as a possible collision 
					'''
					if self.ops[y[2]](self.value, y[3]):
						self.strike += 1
			
			# if the value is found to be in between two existing condition (strike is equal 2), return false
			if self.strike >= 2:
				return False

			self.strike = 0

		return True

			#counter that iterates through existing moments 





		