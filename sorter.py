import sys
try:
    f = open(sys.argv[1] + ".txt", 'r')
except FileNotFoundError:
    print("Error: Cannot find specific file")
    sys.exit()
except IndexError:
    print("Usage: python3 less.py <filename>")
    sys.exit()

lis = []
for word in f:
    lis.append(word.strip())
    lis.sort()
f.close()
print(lis)

f2 = open(sys.argv[1] + "_sorted.txt", 'w')
f2.writelines(lis)
