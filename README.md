# Complier_Experiment
complier_experiment

I implement a project about LR parsing with Syntax-directed translation.

change original_str to what you want cal in List Format.

then you will get output like this:

State     State Stack                        Char Stack                              Rest of Char                            Value Stack                             Object Stack(for debug)                 
next action : s5

5         [0, 5]                             [20]                                    ['+', '(', 2, '*', 3, ')', '-', 4, '#']
next action : r8

3         [0, 3]                             ['F']                                   ['+', '(', 2, '*', 3, ')', '-', 4, '#'] [20]                                    [<Parsing.SubClass.F object at 0x00000208DF78F208>]
next action : r6

2         [0, 2]                             ['T']                                   ['+', '(', 2, '*', 3, ')', '-', 4, '#'] [20]                                    [<Parsing.SubClass.T object at 0x00000208DF78FEF0>]
next action : r3

1         [0, 1]                             ['E']                                   ['+', '(', 2, '*', 3, ')', '-', 4, '#'] [20]                                    [<Parsing.SubClass.E object at 0x00000208DF62D780>]
next action : s6

6         [0, 1, 6]                          ['E', '+']                              ['(', 2, '*', 3, ')', '-', 4, '#']
next action : s4

4         [0, 1, 6, 4]                       ['E', '+', '(']                         [2, '*', 3, ')', '-', 4, '#']
next action : s5

5         [0, 1, 6, 4, 5]                    ['E', '+', '(', 2]                      ['*', 3, ')', '-', 4, '#']
next action : r8

3         [0, 1, 6, 4, 3]                    ['E', '+', '(', 'F']                    ['*', 3, ')', '-', 4, '#']              [20, '+', '(', 2]                       [<Parsing.SubClass.E object at 0x00000208DF62D780>, '+', '(', <Parsing.SubClass.F object at 0x00000208DF78F7B8>]
next action : r6

2         [0, 1, 6, 4, 2]                    ['E', '+', '(', 'T']                    ['*', 3, ')', '-', 4, '#']              [20, '+', '(', 2]                       [<Parsing.SubClass.E object at 0x00000208DF62D780>, '+', '(', <Parsing.SubClass.T object at 0x00000208DF6581D0>]
next action : s8

8         [0, 1, 6, 4, 2, 8]                 ['E', '+', '(', 'T', '*']               [3, ')', '-', 4, '#']
next action : s5

5         [0, 1, 6, 4, 2, 8, 5]              ['E', '+', '(', 'T', '*', 3]            [')', '-', 4, '#']  
next action : r8

13        [0, 1, 6, 4, 2, 8, 13]             ['E', '+', '(', 'T', '*', 'F']          [')', '-', 4, '#']                      [20, '+', '(', 2, '*', 3]               [<Parsing.SubClass.E object at 0x00000208DF62D780>, '+', '(', <Parsing.SubClass.T object at 0x00000208DF6581D0>, '*', <Parsing.SubClass.F object at 0x00000208DF6582E8>]
next action : r4

2         [0, 1, 6, 4, 2]                    ['E', '+', '(', 'T']                    [')', '-', 4, '#']                      [20, '+', '(', 6]                       [<Parsing.SubClass.E object at 0x00000208DF62D780>, '+', '(', <Parsing.SubClass.T object at 0x00000208DF658358>]
next action : r3

10        [0, 1, 6, 4, 10]                   ['E', '+', '(', 'E']                    [')', '-', 4, '#']                      [20, '+', '(', 6]                       [<Parsing.SubClass.E object at 0x00000208DF62D780>, '+', '(', <Parsing.SubClass.E object at 0x00000208DF658278>]
next action : s15

15        [0, 1, 6, 4, 10, 15]               ['E', '+', '(', 'E', ')']               ['-', 4, '#']       
next action : r7

3         [0, 1, 6, 3]                       ['E', '+', 'F']                         ['-', 4, '#']                           [20, '+', 6]                            [<Parsing.SubClass.E object at 0x00000208DF62D780>, '+', <Parsing.SubClass.F object at 0x00000208DF658208>]
next action : r6

11        [0, 1, 6, 11]                      ['E', '+', 'T']                         ['-', 4, '#']                           [20, '+', 6]                            [<Parsing.SubClass.E object at 0x00000208DF62D780>, '+', <Parsing.SubClass.T object at 0x00000208DF658320>]
next action : r1

1         [0, 1]                             ['E']                                   ['-', 4, '#']                           [26]                                    [<Parsing.SubClass.E object at 0x00000208DF658358>]
next action : s7

7         [0, 1, 7]                          ['E', '-']                              [4, '#']            
next action : s5

5         [0, 1, 7, 5]                       ['E', '-', 4]                           ['#']               
next action : r8

3         [0, 1, 7, 3]                       ['E', '-', 'F']                         ['#']                                   [26, '-', 4]                            [<Parsing.SubClass.E object at 0x00000208DF658358>, '-', <Parsing.SubClass.F object at 0x00000208DF78FEF0>]
next action : r6

12        [0, 1, 7, 12]                      ['E', '-', 'T']                         ['#']                                   [26, '-', 4]                            [<Parsing.SubClass.E object at 0x00000208DF658358>, '-', <Parsing.SubClass.T object at 0x00000208DF6583C8>]
next action : r2

1         [0, 1]                             ['E']                                   ['#']                                   [22]                                    [<Parsing.SubClass.E object at 0x00000208DF62D748>]
The expression is legal!
四元式如下:
(* , T_2 , F_3 , T_2*3)
(+ , E_20 , T_(2*3) , E_20+(2*3))
(- , E_20+(2*3) , T_4 , E_20+(2*3)-4)
运算结果为:22

Process finished with exit code 0
