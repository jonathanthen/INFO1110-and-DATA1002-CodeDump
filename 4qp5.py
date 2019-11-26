import math

x = int(input("Enter x: "))
sum1 = 0

exact = math.exp(x)
for i in range(0,11):
  sum1 += (x**i)/math.factorial(i)

diff = exact - sum1

print("Difference:",diff)
  