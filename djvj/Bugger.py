import operator
conditional_moment = []
official_list = []
pending_list = False

class Bugger:

    def __init__(self, temp_moment, official_moment):
        #moment
        self.t_temp_moment = temp_moment
        #current param
        self.t_param = temp_moment[0]
        #sign
        self.t_sign = temp_moment[1]
        #value
        self.t_value = int(temp_moment[2])

        self.official_moment = official_moment

        self.ops = {
            "<": operator.le,
            ">": operator.gt,
            '=': operator.eq,
        }
        #error counter 
        self.strike = 0
        self.strike2 = 0

    def  rule_check_in_list(self):
        if self.official_moment == []:
            return True
        else:

            for x in self.official_moment:
                self.strike = 0
                for y in x:
                    if y[0] == self.t_param:
                        if self.ops[y[1]](self.t_value, int(y[2])):
                            self.strike += 1
                if self.strike >= 2:
                    return False

            return True

    def rule_check_in_moment(self):
        global conditional_moment

        if conditional_moment == []:
            return True
        else:
            for x in conditional_moment:
                if self.t_param == x[0]:
                    if self.t_sign == x[1]:
                        if self.ops[x[1]](self.t_value, int(x[2])):
                            print("Collision detected this moment will not be added")
                            return False

            return True

def moment_to_list_comapare(mlist):
    global conditional_moment

    if mlist == []:
        return True
    else:
        for x in mlist:
            if x == conditional_moment:
                print("there is a momment like this that already exist")
                return False
        return True

def add_rule_to_moment(rule):
    global conditional_moment
    global pending_list

    rule = rule.copy()
    conditional_moment.append(rule)
    pending_list = True

def add_moment_to_moment():
    global conditional_moment
    global official_list

    conditional_moment = conditional_moment.copy()
    official_list_copy = conditional_moment.copy()
    return conditional_moment

def clear_moment_list():
    global conditional_moment

    conditional_moment.clear()

def list_status():
    return pending_list
