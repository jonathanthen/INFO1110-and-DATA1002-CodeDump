
def range_difference(ls):
    i = 0
    mini = 9999
    maxi = -4

    if type(ls) != list and type(ls) != tuple:
        return None
    elif ls == ():
        return None
    elif ls == []:
        return None
    else:
        while i < len(ls):
            if type(ls[i]) != int:
                return None
            else:
                if mini > ls[i]:
                    mini = ls[i]
                elif maxi < ls[i]:
                    maxi = ls[i]
            i += 1
        diff = abs(maxi - mini)
        return diff
    
print(range_difference([-4, -5, -6, -100]))
            