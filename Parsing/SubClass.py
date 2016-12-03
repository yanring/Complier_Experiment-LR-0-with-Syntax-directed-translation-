

class E:
    def __init__(self, name):
        value = 0
        self.name = name

    def set_value(self, val):
        self.value = val


class F:
    def __init__(self, name):
        value = 0
        self.name = name

    def set_value(self, val):
        self.value = val


class T:
    def __init__(self, name):
        value = 0
        self.name = name

    def set_value(self, val):
        self.value = val


class SubClass:
    def __init__(self,generator):
        self.generator = generator

    def sub0(self, var_list, name):
        new_e = E(name)
        new_e.value = var_list[0].value
        return new_e

    def sub1(self, var_list, name):
        new_e = E(name)
        new_e.value = var_list[0].value + var_list[2].value
        self.generator.add_expression('+',var_list[0].name,var_list[2].name,new_e.name)
        return new_e

    def sub2(self, var_list, name):
        new_e = E(name)
        new_e.value = var_list[0].value - var_list[2].value
        self.generator.add_expression('-', var_list[0].name, var_list[2].name, new_e.name)
        return new_e

    def sub3(self, var_list, name):
        new_e = E(name)
        new_e.value = var_list[0].value
        return new_e

    def sub4(self, var_list, name):
        new_t = T(name)
        new_t.value = var_list[0].value * var_list[2].value
        self.generator.add_expression('*', var_list[0].name, var_list[2].name, new_t.name)
        return new_t

    def sub5(self, var_list, name):
        new_t = T(name)
        new_t.value = var_list[0].value / var_list[2].value
        self.generator.add_expression('/', var_list[0].name, var_list[2].name, new_t.name)
        return new_t

    def sub6(self, var_list, name):
        new_t = T(name)
        new_t.value = var_list[0].value
        return new_t

    def sub7(self, var_list, name):
        new_f = F(name)
        new_f.value = var_list[1].value
        return new_f

    def sub8(self, var_list, name):
        new_f = F(name)
        new_f.value = var_list[0]
        return new_f
