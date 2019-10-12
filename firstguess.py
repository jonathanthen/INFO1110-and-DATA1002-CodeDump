x = float(input("Number to find sqrt of: "))
lower =	float(input("Lower bound: "))
upper =	float(input("Upper bound: "))

guess = (lower + upper) / 2
guess_sq = pow(guess, 2)

print("Next guess:", guess)
print("Guess squared:", guess_sq)

x = float(input("Number to find sqrt of: "))
lower =	 float(input("Lower bound: "))
upper = float(input("Upper bound: "))

guess = (lower + upper) / 2
print("First guess:", guess)
guess_sq = pow(guess, 2)

if guess_sq > x:
  upper = guess
  print("Upper bound changed to:", upper)
else:
  lower = guess
  print("Lower bound changed to:", lower)

guess = (lower + upper) / 2
print("Second guess:", guess)
guess_sq = pow(guess, 2)

if guess_sq > x:
  upper = guess
  print("Upper bound changed to:", upper)
else:
  lower = guess
  print("Lower bound changed to:", lower)