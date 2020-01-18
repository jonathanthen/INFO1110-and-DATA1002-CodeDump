def convert(n):
    if type(n) != int:
        raise TypeError

    if n < 0:
        raise ValueError

    if n == 0:
        return "0"

    if n == 1:
        return "1"

    return convert(n//2) + str(n%2)

a = convert(0)
print(a)
b = convert(1)
print(b)
c = convert(2)
print(c)
d = convert(7)
print(d)
e = convert(30)
print(e)
f = convert(154)
print(f)
#g = convert(-1)     # ValueError 
#h = convert('5')    # TypeError