a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
e = int(input("Enter e: "))

num = 0

if a != 7:
    num += a
    if b != 7:
        num += b
        if c != 7:
            num += c
            if d != 7:
                num += d
                if e != 7:
                    num += e
elif b != 7:
    if c != 7:
        num += c
        if d != 7:
            num += d
            if e != 7:
                num += e
elif c != 7:
    if d != 7:
        num += d
        if e != 7:
            num += e
elif d != 7:
    if e != 7:
        num += e
    
    
    
print("The sum is",num)