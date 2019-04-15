import operator

class Bugger:

    def __init__(self, temp_momment, official_momment):
        #current param
        self.t_param = temp_momment[0]
        print("init param: ", self.t_param)
        #sign
        self.t_sign = temp_momment[1]
        print("init sign: ", self.t_sign)
        #value
        self.t_value = int(temp_momment[2])
        print("init t_value: ", self.t_value)

        self.official_momment = official_momment
        print("init official momment: ", self.official_momment)

        self.ops = {
            "<": operator.le,
            ">": operator.gt,
            '=': operator.eq,
        }
        #error counter 
        self.strike = 0
        #main moment that will be used in the show class
        self.official_momment = official_momment
        
    def momment_check(self):
        # if the main momment is empty
        if self.official_momment == []:
            print("Nothing in momment Part 1")
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
                if self.t_param == y[0]:
                    '''
                    if current momment meets the condition of any existing momments, flag it
                    ex:
                    t_value = 3
                    y[3] = 5

                    if tvalue < y[3]
                    flag this as a possible collision 
                    '''
                    if self.ops[y[1]](self.t_value, int(y[2])):
                        self.strike += 1
            
            # if the value is found to be in between two existing condition (strike is equal 2), return false
            if self.strike >= 2:
                return False

            self.strike = 0
        return True

            #counter that iterates through existing moments
    def moment_check2(self):
        # if self.official_momment == []:
        #     print("Nothing in momment Part 2")
        #     return True

        #for x in self.official_momment:
            #for y in x:
                
                #if y == self.t_param:

            # print("X is equal to :", x)
            # for y in x:
            #     print("if", self.t_param, "is equal to", y[0])
            #     if self.t_param == y[0]:
            #         print("Getting inside nested part 1")
            #         if self.t_sign == y[1]:
            #             print("Getting inside nested part 2")
            #             if self.ops[y[1]](self.t_value, int(y[2])) or self.ops[y[1]](int(y[2]), self.t_value):
            #                 return False
        return True