def fibonacci(n):
    f1 = 0 
    f2 = 1
    i = 0
    while i < n:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        i += 1
    return f1

print(fibonacci(8))
