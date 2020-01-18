def most_popular(bin):
    if type(bin) != str:
        raise TypeError
    elif bin.isalpha() == True:
        raise ValueError
    else:
        count1 = bin.count("1")
        count0 = bin.count("0")
        if count1 == count0:
            return None
        else:
            if count1 > count0:
                return "1"
            elif count0 > count1:
                return "0"

a = most_popular('10110')   # "1"
b = most_popular('001')     # '0'
c = most_popular('101010')  # None 
#d = most_popular(451)       # TypeError
#e = most_popular('ABCDEF')  # ValueError

print(a)
print(b)
print(c)