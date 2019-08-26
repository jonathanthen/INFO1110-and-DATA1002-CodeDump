import sys
line = ' '
if len(sys.argv) > 1:
    flag = sys.argv[1]
    if flag == '-a':
        num = 1
        while num <= 100:
            if num%2 != 0:
                line += str(num) + ", "
            num = num + 1
        line = line.rstrip(", ")
        print(line)
    elif flag == '-d':
        num = 99
        while num >= 1:
            if num%2 != 0:
                line += str(num) + ", "
            num = num - 1
        line = line.rstrip(", ")
        print(line)
else:
    sys.exit()