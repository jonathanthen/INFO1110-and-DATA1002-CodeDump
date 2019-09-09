a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == b and b == c:
    print("The sum is",0)
elif b == c:
    print("The sum is",str(a))
elif a == c:
    print("The sum is",str(b))
elif a == b:
    print("The sum is",str(c))
else:
    sum = a + b + c
    print("The sum is",str(sum))