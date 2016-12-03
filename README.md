# Complier_Experiment
complier_experiment

I implement a project about LR parsing with Syntax-directed translation.

change original_str to what you want cal in List Format.

then you will get output like this:




    State     State Stack                        Char Stack                              Rest of Char                            Value Stack              
    next action : s5
    5         [0, 5]                             [20]                                    ['+', '(', 2, '*', 3, ')', '-', 4, '#']
    next action : r8
    3         [0, 3]                             ['F']                                   ['+', '(', 2, '*', 3, ')', '-', 4, '#'] [20]                     
    next action : r6
    2         [0, 2]                             ['T']                                   ['+', '(', 2, '*', 3, ')', '-', 4, '#'] [20]                     
    next action : r3
    1         [0, 1]                             ['E']                                   ['+', '(', 2, '*', 3, ')', '-', 4, '#'] [20]                     
    next action : s6
    6         [0, 1, 6]                          ['E', '+']                              ['(', 2, '*', 3, ')', '-', 4, '#']
    next action : s4
    4         [0, 1, 6, 4]                       ['E', '+', '(']                         [2, '*', 3, ')', '-', 4, '#']
    next action : s5
    5         [0, 1, 6, 4, 5]                    ['E', '+', '(', 2]                      ['*', 3, ')', '-', 4, '#']
    next action : r8
    3         [0, 1, 6, 4, 3]                    ['E', '+', '(', 'F']                    ['*', 3, ')', '-', 4, '#']              [20, '+', '(', 2]        
    next action : r6
    2         [0, 1, 6, 4, 2]                    ['E', '+', '(', 'T']                    ['*', 3, ')', '-', 4, '#']              [20, '+', '(', 2]        
    next action : s8
    8         [0, 1, 6, 4, 2, 8]                 ['E', '+', '(', 'T', '*']               [3, ')', '-', 4, '#']
    next action : s5
    5         [0, 1, 6, 4, 2, 8, 5]              ['E', '+', '(', 'T', '*', 3]            [')', '-', 4, '#']  
    next action : r8
    13        [0, 1, 6, 4, 2, 8, 13]             ['E', '+', '(', 'T', '*', 'F']          [')', '-', 4, '#']                      [20, '+', '(', 2, '*', 3]
    next action : r4
    2         [0, 1, 6, 4, 2]                    ['E', '+', '(', 'T']                    [')', '-', 4, '#']                      [20, '+', '(', 6]        
    next action : r3
    10        [0, 1, 6, 4, 10]                   ['E', '+', '(', 'E']                    [')', '-', 4, '#']                      [20, '+', '(', 6]        
    next action : s15
    15        [0, 1, 6, 4, 10, 15]               ['E', '+', '(', 'E', ')']               ['-', 4, '#']       
    next action : r7
    3         [0, 1, 6, 3]                       ['E', '+', 'F']                         ['-', 4, '#']                           [20, '+', 6]             
    next action : r6
    11        [0, 1, 6, 11]                      ['E', '+', 'T']                         ['-', 4, '#']                           [20, '+', 6]             
    next action : r1
    1         [0, 1]                             ['E']                                   ['-', 4, '#']                           [26]                     
    next action : s7
    7         [0, 1, 7]                          ['E', '-']                              [4, '#']            
    next action : s5
    5         [0, 1, 7, 5]                       ['E', '-', 4]                           ['#']               
    next action : r8
    3         [0, 1, 7, 3]                       ['E', '-', 'F']                         ['#']                                   [26, '-', 4]             
    next action : r6
    12        [0, 1, 7, 12]                      ['E', '-', 'T']                         ['#']                                   [26, '-', 4]             
    next action : r2
    1         [0, 1]                             ['E']                                   ['#']                                   [22]                     
    The expression is legal!
    四元式如下:
    (* , T_2 , F_3 , T_2*3)
    (+ , E_20 , T_(2*3) , E_20+(2*3))
    (- , E_20+(2*3) , T_4 , E_20+(2*3)-4)
    运算结果为:22
