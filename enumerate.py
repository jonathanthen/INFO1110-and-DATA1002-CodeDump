spam = ['a', 'b', 'c', 'd','e']

def my_enum(ls):
    ret_list = []
    i = 0
    while i < len(ls):
        ret_list.append((i,ls[i]))
        i += 1
    return ret_list

e_spam = my_enum(spam)
print(e_spam)
