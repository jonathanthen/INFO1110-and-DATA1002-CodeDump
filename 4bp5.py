x = float(input("Enter x: "))

for i in range(10):
  x = x-((x**3 + 2)/(3*(x**2)))
  diff = abs(-1.25992104989 - x)
  print(diff)