nums = [5,3,2,4,10]

def average(ls):
    i = 0
    s = 0
    while i < len(ls):
        s += ls[i]
        i += 1
    avg = s / len(ls)
    return(avg)

summ = average(nums)
print(summ)
