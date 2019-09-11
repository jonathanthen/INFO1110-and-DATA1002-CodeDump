a_spam = ['a', 'b', 'c', 'd']
b_spam = ['W', 'X', 'Y', 'Z']

def my_zip(ls1,ls2):
    ret_list = []
    i = 0
    while i < len(ls1) or i < len(ls2):
        ret_list.append((a_spam[i],b_spam[i]))
        i += 1
    return ret_list

z_spam = my_zip(a_spam, b_spam)
print(z_spam)