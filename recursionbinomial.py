def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        return n*factorial(n-1)

def binomial(n, k):
    return (factorial(n) // (factorial(k)*(n-k)))
#will return a float unless you use a floor division
print(binomial(5,3))