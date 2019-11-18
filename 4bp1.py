num1 = int(input("Enter first number: "))
num2 = int(input("Enter last number: "))

for num in range(num1, num2 + 1):
  if num % 2 == 0:
    print(num, "is even")
  else:
    print(num, "is odd")