def special_number(n):
    lis = []
    number = 1

    while len(lis) < n:
        lis.append(number)
        number += 2
        lis.append(number)
        number += 1

    return lis

import sys
f = open(sys.argv[1], "r")

done = False
line_num = 0

while not done:
    line = f.readline()
    i = 0
    lis = special_number(7)
    while i < len(lis):
        if lis[i] == (line_num + 1):
            print(line.rstrip("\n"))
        i += 1
    if not line:
        break
    line_num += 1