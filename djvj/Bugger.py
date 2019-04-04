

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

		## iterates through main momments 
		for x in self.official_momment:
			# iterates through momemnts in momments
			for y in x:
				# compare current momment param to existing momment param 
				if t_param == y[1]:
					# if current momment meets the condition of any existing momments, flag it
					if self.ops[y[2]](self.value, y[3]):
						self.strike += 1
			# if the value is found to be in between two existing condition, return false
			if self.strike >= 2:
				return False

			self.strike = 0

		return True

			#counter that iterates through existing moments 





		