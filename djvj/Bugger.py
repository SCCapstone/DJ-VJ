import operator
"""
Rule
temp_momment = ['pitch', '<', 40]
Single momment
momment = [['pitch', '<', 40]],['pitch', '>', 20]]
Main momment 
main momment = [[['pitch', '<', 40]],['pitch', '>', 20]], [['tempo', '<', 40]],['tempo', '>', 20]]]
"""
conditional_momment = []
official_list = []
pending_list = False

class Bugger:

    def __init__(self, temp_momment, official_momment):
        #current param
        self.t_param = temp_momment[0]
        #sign
        self.t_sign = temp_momment[1]
        #value
        self.t_value = int(temp_momment[2])

        self.official_momment = official_momment

        self.ops = {
            "<": operator.le,
            ">": operator.gt,
            '=': operator.eq,
        }
        #error counter 
        self.strike = 0

    def  rule_check_in_list(self):
        if self.official_momment == []:
            return True
        else:
            for x in self.official_momment:
                self.strike = 0
                for y in x:
                    if y[0] == self.t_param:
                        if self.ops[y[1]](self.t_value, int(y[2])):
                            self.strike += 1
                if self.strike >= 2:
                    return False
            return True

    def rule_check_in_momment(self):
        global conditional_momment

        if conditional_momment == []:
            return True
        else:
            for x in conditional_momment:
                if self.t_param == x[0]:
                    if self.t_sign == x[1]:
                        if self.ops[x[1]](self.t_value, int(x[2])):
                            print("Collision detected this momment will not be added")
                            return False

            return True

def add_rule_to_momment(rule):
    global conditional_momment
    global pending_list

    rule = rule.copy()
    conditional_momment.append(rule)
    pending_list = True

def add_momment_to_momment():
    global conditional_momment
    global official_list

    conditional_momment = conditional_momment.copy()
    official_list_copy = conditional_momment.copy()
    return conditional_momment

def clear_momment_list():
    global conditional_momment

    conditional_momment.clear()

def list_status():
    return pending_list
