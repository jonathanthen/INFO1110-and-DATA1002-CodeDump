import sys

lis = []
i = 0

if int(sys.argv[1]) >= len(sys.argv):
    print("Too big!")
else:
    while i < len(sys.argv):
        lis.append(sys.argv[i])
        i += 1
        
    number = int(lis[1])
    print(lis[number])