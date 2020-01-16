def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        return n*factorial(n-1)

fac = factorial(6)
print(fac)