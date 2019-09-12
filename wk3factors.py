import sys

num = int(sys.argv[1])
count = 1
factors = 0

while count <= num:
    if num % count == 0:
        factors += 1
    count += 1
    
print(num,"has",factors,"factors")