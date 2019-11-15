x = float(input("Number to find sqrt of: "))
lower =	 float(input("Lower bound: "))
upper = float(input("Upper bound: "))
niter = int(input("Number of iterations: "))

for n in range(niter):
  guess = (lower + upper) / 2
  guess_sq = pow(guess, 2)

  if guess_sq > x:
    upper = guess
  else:
    lower = guess
  print(n+1, guess)
print("Best guess for the square root:", guess)