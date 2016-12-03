import sys

from Parsing.SubClass import SubClass, E, F, T
from Parsing.tables import *
from Parsing.Generator import *

# initial variable
state = 0
state_stack = [0]
original_str = ""
rest_of_str = []
str_stack = []
object_stack = []
parsing_action = ""
i = 0
available_char = ["i", "+", "-", "*", "/", "#", "(", ")"]
generator = Generator()


def query(next_char):
    # print(next_char not in available_char and type(next_char)!=int)
    if next_char not in available_char and type(next_char) != int:
        print("Error! We have encounter a invalid char :" + str(next_char))
        exit(1)
    if type(next_char) == int:
        next = 'i'
    else:
        next = next_char
    next_action = Action[state][next]
    if next_action == '-1':
        print("Error! We have encounter a null action , expression is illegal, next can't be :" + str(next_char))
        exit(1)
    if next_action == 'acc':
        print("The expression is legal!")
        print("四元式如下:")
        generator.print()
        print("运算结果为:"+str(value_stack[0]))
        exit(0)
    return next_action


def reduce(index):
    global str_stack
    global state_stack
    global state
    global object_stack
    global value_stack
    index = int(index)
    pop_times = len(list(rules[index].values())[0].__str__())
    var_list = []
    for j in range(pop_times):
        state_stack.pop()
        temp_str = str_stack.pop()
        temp_reduce_var = object_stack.pop()
        if type(temp_reduce_var) == E or type(temp_reduce_var) == F or type(temp_reduce_var) == T:
            var_list.append(temp_reduce_var)  # 记录有哪些被规约掉了,供语义子程序调用
            continue
        var_list.append(temp_reduce_var)  # 记录有哪些被规约掉了,供语义子程序调用
    str_stack.append(rules[index].keys().__str__()[12])
    new_reduce_name = str(str_stack[-1]) + '_'  # 生成非终结符的带下标的名字的前缀
    var_list = var_list[::-1]  # 由于是按出栈的顺序,所以要调转一下
    for each in var_list:
        if type(each) == E or type(each) == F or type(each) == T:
            new_reduce_name += each.name[2:]#去掉已有的前缀
            continue
        new_reduce_name += str(each)  # 生成非终结符的带下标的名字
    sub_class = SubClass(generator)
    temp_reduce_var1 = getattr(sub_class, 'sub' + str(index))(var_list, new_reduce_name)  # 动态调用语义子程序
    object_stack.append(temp_reduce_var1)
    value_stack = []
    for i in object_stack:  # 生成数值栈
        if type(i) == E or type(i) == F or type(i) == T:
            # print(i.value)
            value_stack.append(i.value)
            continue
        value_stack.append(i)
    state = GOTO_Table[state_stack[-1]][str_stack[-1]]
    state_stack.append(state)
    # 符号栈和状态栈入栈
    print('%-10s%-35s%-40s%-40s%-40s%-40s' % (
        state.__str__(), state_stack.__str__(), str_stack.__str__(), rest_of_str.__str__(), value_stack.__str__(),
        object_stack))


def shift(next_state):
    global state

    str_stack.append(rest_of_str[0])
    object_stack.append(rest_of_str[0])
    rest_of_str.pop(0)
    state_stack.append(int(next_state))
    state = state_stack[-1]
    print('%-10s%-35s%-40s%-20s' % (state.__str__(), state_stack.__str__(), str_stack.__str__(), rest_of_str.__str__()))


def parsing():
    global i
    print('%-10s%-35s%-40s%-40s%-40s%-40s' % (
        "State", "State Stack", "Char Stack", "Rest of Char", "Value Stack", "Object Stack(for debug)"))
    while 1:
        # print(rest_of_str[0])
        next_action = query(rest_of_str[0])

        print("next action : " + next_action + '\n')
        next_action_list = list(next_action)
        if next_action_list[0] == 'r':
            reduce(int(''.join(next_action_list[1:])))
        elif next_action_list[0] == 's':
            shift(int(''.join(next_action_list[1:])))
        else:
            print("expression illegal")


if __name__ == '__main__':
    original_str = [20, '+', '(', 2, '*', 3, ')', '-', 4]
    rest_of_str = original_str
    rest_of_str.append('#')
    e = E("h")
    parsing()
