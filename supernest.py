def super_nest(ls):
    if type(ls[0]) != list:
        print(ls)
    else:
        return super_nest(ls[0])

super_nest([True])                         # [True]
super_nest([[[1, 2, 3]]])                  # [1, 2, 3]
super_nest([[[[[[[['a', 'b', 'c']]]]]]]])  # ['a', 'b', 'c']