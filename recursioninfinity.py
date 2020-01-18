#Ingredients of recursive function:
# 1) Base Case (Stop Function)
# 2) Recursive Part (Break soln down into smaller sub problems)

# Recursion is memory hungry
def spam(n):
    print(n)
    if n == 0:
        return n
    return spam(n-1)


ham = spam(3)
print(ham)
#ham is 0