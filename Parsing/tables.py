rules = [
    {"E'": "E"},  # r0
    {"E": "E+T"},  # r1
    {"E": "E-T"},  # r2
    {"E": "T"},  # r3
    {"T": "T*F"},  # r4
    {"T": "T/F"},  # r5
    {"T": "F"},  # r6
    {"F": "(E)"},  # r7
    {"F": "i"},  # r8
]
GOTO_Table = [
    {"E": 1, "T": 2, "F": 3},  # 0
    {"E": -1, "T": -1, "F": -1},  # 1
    {"E": -1, "T": -1, "F": -1},  # 2
    {"E": -1, "T": -1, "F": -1},  # 3
    {"E": 10, "T": 2, "F": 3},  # 4
    {"E": -1, "T": -1, "F": -1},  # 5
    {"E": -1, "T": 11, "F": 3},  # 6
    {"E": -1, "T": 12, "F": 3},  # 7
    {"E": -1, "T": -1, "F": 13},  # 8
    {"E": -1, "T": -1, "F": 14},  # 9
    {"E": -1, "T": -1, "F": -1},  # 10
    {"E": -1, "T": -1, "F": -1},  # 11
    {"E": -1, "T": -1, "F": -1},  # 12
    {"E": -1, "T": -1, "F": -1},  # 13
    {"E": -1, "T": -1, "F": -1},  # 14
    {"E": -1, "T": -1, "F": -1},  # 15
]
Action = [
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  # 0
    {"(": "-1", ")": "-1", "+": "s6", "-": "s7", "*": "-1", "/": "-1", "i": "-1", "#": "acc"},  # 1
    {"(": "-1", ")": "r3", "+": "r3", "-": "r3", "*": "s8", "/": "s9", "i": "-1", "#": "r3"},  # 2
    {"(": "-1", ")": "r6", "+": "r6", "-": "r6", "*": "r6", "/": "r6", "i": "-1", "#": "r6"},  # 3
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  # 4
    {"(": "-1", ")": "r8", "+": "r8", "-": "r8", "*": "r8", "/": "r8", "i": "-1", "#": "r8"},  # 5
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  # 6
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  # 7
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  # 8
    {"(": "s4", ")": "-1", "+": "-1", "-": "-1", "*": "-1", "/": "-1", "i": "s5", "#": "-1"},  # 9
    {"(": "s4", ")": "s15", "+": "s6", "-": "s7", "*": "-1", "/": "-1", "i": "-1", "#": "-1"},  # 10
    {"(": "-1", ")": "r1", "+": "r1", "-": "r1", "*": "s8", "/": "s9", "i": "-1", "#": "r1"},  # 11
    {"(": "-1", ")": "r2", "+": "r2", "-": "r2", "*": "s8", "/": "s9", "i": "-1", "#": "r2"},  # 12
    {"(": "-1", ")": "r4", "+": "r4", "-": "r4", "*": "r4", "/": "r4", "i": "-1", "#": "r4"},  # 13
    {"(": "-1", ")": "r5", "+": "r5", "-": "r5", "*": "r5", "/": "r5", "i": "-1", "#": "r5"},  # 14
    {"(": "-1", ")": "r7", "+": "r7", "-": "r7", "*": "r7", "/": "r7", "i": "-1", "#": "r7"},  # 15
]