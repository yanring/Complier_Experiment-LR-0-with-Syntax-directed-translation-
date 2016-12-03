class Generator:
    def __init__(self):
        self.four_element_list = []

    def add_expression(self, op, par1, par2, target):
        temp_expression = '(' + str(op) + ' , ' + str(par1) + ' , ' + str(par2) + ' , ' + str(target) + ')'
        self.four_element_list.append(temp_expression)
        pass

    def print(self):
        for i in self.four_element_list:
            print(i)