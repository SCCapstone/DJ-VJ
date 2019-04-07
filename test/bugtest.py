import operator
class Test:
    def __init__(self):
        self.ops = {
            "<": operator.le,
            ">": operator.gt,
            "=": operator.eq,
        }
        #counter
        self.strike = 0
        #test int
        self.testval = 15
        #test lists of list
        self.testlist = ['<', '20']
        self.templist = [[['>', '0'], ['<', '50']],[['<','80' ], ['>','50']]]
        self.templist2 = [[['<', '80'], ['>', '50']],[['<','30' ], ['>','0']]]
        self.templist3 = [[['<', '300'], ['>', '100']],[['<','800' ], ['>','500']]]

    def check(self):
        #nested for loop for list
        for x in self.templist:
            for y in x:
                print(y)
                #if test value is true in comapared to list int, flag it
                if self.ops[y[0]](self.testval, y[1]):
                    print(y[1])
                    self.strike += 1

                if self.strike >= 2:
                    print("ERROR at ", x)
      
            self.strike = 0
    def check2(self):
        for x in self.templist:
            for y in x:
                if y[0] == self.testlist[0]:
                    if self.ops[y[0]](self.testlist[1], y[1]) or self.ops[y[0]](y[1], self.testlist[1]):
                        print("Flag on", y)



Test = Test()
Test.check2()