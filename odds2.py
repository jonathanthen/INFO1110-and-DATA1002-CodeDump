num = 1
line = " "
while num <= 100:
    if num%2 != 0:
        line += str(num) + ", "
    num = num + 1
line = line.rstrip(", ")
print(line)
