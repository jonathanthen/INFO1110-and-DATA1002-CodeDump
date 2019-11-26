import math
dx = float(input("Enter an angle x (in degrees): "))
x = dx*math.pi/180
nsteps = int(input("Enter the number of terms in the Taylor Series approximation: "))
sum1 = 0.0 
exact = math.sin(x)
for i in range(0,nsteps+1):
  sum1 += ((-1)**(i))*(x**(2*i+1))/math.factorial(2*i+1)
print("Exact values of sin(x): ",exact)
print("Taylor Series aproximation: ",sum1)