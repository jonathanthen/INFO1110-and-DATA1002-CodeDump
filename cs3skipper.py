x = -1

while x < 100:
    x += 1
    if (x % 4) == 0 or (x % 7) == 0:
        continue
    print(x)