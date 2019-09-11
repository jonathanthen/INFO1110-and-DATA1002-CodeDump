names = ['Alice', 'Bob', 'Carol']
ages = [32, 51, 15, 5, 25, 48]

def my_zip(ls1,ls2):
    if len(ls1) > len(ls2):
        short_len = len(ls2)
    else:
        short_len = len(ls1)

    ret_list = []
    i = 0
    while i < short_len:
        ret_list.append((names[i],ages[i]))
        i += 1
    return ret_list

z_spam = my_zip(names, ages)
print(z_spam)