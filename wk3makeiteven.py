import sys

num = int(sys.argv[1])
if num % 2 == 0:
    print(num)
else:
    num = num + 1
    print(num)