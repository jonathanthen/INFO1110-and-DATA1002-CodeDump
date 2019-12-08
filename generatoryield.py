def add(x, y, z):
    total = 0
    yield(total)
    total += x
    yield(total)
    total += y
    yield(total)

f2 = add(1,2,3)
print(f2.__next__())
print(f2.__next__())
print(f2.__next__())