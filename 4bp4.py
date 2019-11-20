S = int(input("Enter S: "))
x = float(input("Enter x: "))
n = int(input("Enter n: "))

for iterations in range(n):
  x = x + ((S/x)-x)/2
  print(x)