import sys

rules = [
    {"E'": "E"},         #r0
    {"E": "E+T"},       #r1
    {"E": "E-T"},      #r2
    {"E": "T"},        #r3
    {"T": "T*F"},      #r4
    {"T": "T/F"},      #r5
    {"T": "F"},      #r6
    {"F": "(E)"},      #r7
    {"F": "i"},      #r8
]
GOTO_Table =[
    {"E": 1, "T": 2, "F": 3},            #0
    {"E": -1, "T": -1, "F": -1},    #1
    {"E": -1, "T": -1, "F": -1},    #2
    {"E": -1, "T": -1, "F": -1},    #3
    {"E": 10, "T": 2, "F": 3},    #4
    {"E": -1, "T": -1, "F": -1},    #5
    {"E": -1, "T": 11, "F": 3},    #6
    {"E": -1, "T": 12, "F": 3},    #7
    {"E": -1, "T": -1, "F": 13},    #8
    {"E": -1, "T": -1, "F": 14},    #9
    {"E": -1, "T": -1, "F": -1},    #10
    {"E": -1, "T": -1, "F": -1},    #11
    {"E": -1, "T": -1, "F": -1},    #12
    {"E": -1, "T": -1, "F": -1},    #13
    {"E": -1, "T": -1, "F": -1},    #14
    {"E": -1, "T": -1, "F": -1},    #15

]
Action = [
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  #0
    {"(": "-1", ")": "-1", "+": "s6", "-": "s7", "*": "-1", "/": "-1", "i": "-1", "#": "acc"},  #1
    {"(": "-1", ")": "r3", "+": "r3", "-": "r3", "*": "s8", "/": "s9", "i": "-1", "#": "r3"},  #2
    {"(": "-1", ")": "r6", "+": "r6", "-": "r6", "*": "r6", "/": "r6", "i": "-1", "#": "r6"},  #3
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  #4
    {"(": "-1", ")": "r8", "+": "r8", "-": "r8", "*": "r8", "/": "r8", "i": "-1", "#": "r8"},  #5
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  #6
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  #7
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  #8
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  #9
    {"(": "s4", ")":"s15", "+": "s6", "-": "s7", "*": "-1", "/": "-1", "i": "-1", "#": "-1"},  #10
    {"(": "-1", ")": "r1", "+": "r1", "-": "r1", "*": "s8", "/": "s9", "i": "-1", "#": "r1"},  #11
    {"(": "-1", ")": "r2", "+": "r2", "-": "r2", "*": "s8", "/": "s9", "i": "-1", "#": "r2"},  #12
    {"(": "-1", ")": "r4", "+": "r4", "-": "r4", "*": "r4", "/": "r4", "i": "-1", "#": "r4"},  #13
    {"(": "-1", ")": "r5", "+": "r5", "-": "r5", "*": "r5", "/": "r5", "i": "-1", "#": "r5"},  #14
    {"(": "-1", ")": "r7", "+": "r7", "-": "r7", "*": "r7", "/": "r7", "i": "-1", "#": "r7"},  #15
]

#initail
state = 0
state_stack = [0]
original_str = ""
rest_of_str = []
str_stack = []
#next_state = -1
parsing_action = ""
i = 0
avilible_char = ["i", "+", "-", "*", "/","#"]


def query(next_char):
    next_action = Action[state][next_char]
    if next_action=='-1' or next_char not in avilible_char:
        print("Error! We have encounter a invaild char :" + next_char)
        exit(1)
    if next_action == 'acc':
        print("the expression is legal")
        exit(0)
    return next_action


def reduce(index):
    global str_stack
    global state_stack
    global state

    index = int(index)
    pop_times = len(list(rules[index].values())[0].__str__())
    #print("len : "+pop_times.__str__()+list(rules[index].values())[0].__str__())
    for j in range(pop_times):
        state_stack.pop()
        str_stack.pop()
        #print(state_stack)
    #print(rules[index].keys().__str__()[12])
    str_stack.append(rules[index].keys().__str__()[12])
    #print(str_stack)
    #state = GOTO_Table[2]['E']
    state = GOTO_Table[state_stack[-1]][str_stack[-1]]
    state_stack.append(state)
    #符号栈和状态栈入栈
    print('%-10s%-25s%-30s%-20s' %(state.__str__(),state_stack.__str__(),str_stack.__str__() ,rest_of_str.__str__()))


def shift(next_state):
    global state
    str_stack.append(rest_of_str[0])
    rest_of_str.pop(0)
    state_stack.append(int(next_state))
    state = state_stack[-1]
    print('%-10s%-25s%-30s%-20s' %(state.__str__(),state_stack.__str__(),str_stack.__str__() ,rest_of_str.__str__()))


def parsing():
    global i
    while 1:
        #print(rest_of_str[0])
        next_action = query(rest_of_str[0])
        #print("next action : " + next_action)
        next_action_list = list(next_action)
        if next_action_list[0] == 'r':
            reduce(next_action_list[1])
        elif next_action_list[0] == 's':
            shift(next_action_list[1])
        else:
            print("expression illegal")


if __name__ == '__main__':
    original_str = "i+i*i+i"
    rest_of_str = list(original_str)
    rest_of_str.append("#")
    parsing()
    #print(Action[2]["+"])
