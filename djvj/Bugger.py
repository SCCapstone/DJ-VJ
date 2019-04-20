import operator
conditional_moment = []
official_list = []
error_list = []
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
            "=": operator.eq,
        }
        #error counter 
        self.strike = 0

    def  rule_check_in_list(self):
        global error_list
        """ checks if moment is empty"""
        if self.official_moment == []:
            return True
        else:
            """ checks if rule can be found within a range ex: Rule1 < Rule2 < Rule1 = Error"""
            for x in self.official_moment:
                self.strike = 0
                for y in x:
                    if y[0] == self.t_param:
                        if self.ops[y[1]](self.t_value, int(y[2])):
                            error_list.append(y)
                            self.strike += 1
                if self.strike >= 2:
                    self.t_temp_moment.clear()
                    return False
                
                error_list.clear()

            return True

    def rule_check_in_moment(self):
        global error_list
        global conditional_moment
        if conditional_moment == []:
            return True
        else:
            """ checks for overlapping conditions within a single moment"""
            for x in conditional_moment:
                if self.t_param == x[0]:
                    if self.t_sign == x[1]:
                        if self.ops[x[1]](self.t_value, int(x[2])) or self.ops[x[1]](int(x[2]), self.t_value):
                            error_list.append(x)
                            self.t_temp_moment.clear()
                            return False
            return True

def moment_to_list_comapare(mlist):
    global conditional_moment
    global error_list

    print(mlist)

    operation = {
        "<": operator.le,
        ">": operator.gt,
        "=": operator.eq,
    }

    num_of_rule = 0
    num_of_error = 0

    num_of_rule = len(conditional_moment)

    if mlist == []:
        return True
    else:
        """ compares the created momment with existising momments """
        for x in mlist:
            if x == conditional_moment:
                error_list.append(x)
                return False
        for x in mlist:
            for y in x:

                for z in conditional_moment:
                    if y[0] == z[0]:
                        if y[1] == z[1]:
                            if operation[y[1]](int(z[2]), int(y[2])):
                                error_list.append(y)
                                num_of_error += 1
            if num_of_error == num_of_rule:
                return False

            error_list.clear()

        return True

def add_rule_to_moment(rule):
    global conditional_moment
    global pending_list
    global error_list

    error_list.clear()

    rule = rule.copy()
    conditional_moment.append(rule)
    pending_list = True

def add_moment_to_moment():
    global conditional_moment
    global official_list
    global error_list

    error_list.clear()

    conditional_moment = conditional_moment.copy()
    official_list_copy = conditional_moment.copy()
    return conditional_moment

def clear_moment_list():
    global conditional_moment

    conditional_moment.clear()

def remove_rule():
    global conditional_moment
    global error_list
    #if rule was found in the error list, it will be removed also
    if conditional_moment in error_list:
        error_list.remove(conditional_moment)
    #removes rule from moment
    length = len(conditional_moment)
    conditional_moment.remove(conditional_moment[length - 1])

def give_list_of_error():
    global error_list
    return error_list

def give_current_moment():
    global conditional_moment
    return conditional_moment
