max_sofar = 0
for value in open("rainfall_Feb2017.txt"):
  value_float = float(value)
  max_sofar = max(max_sofar, value_float)
 
print("Maximum daily rainfall (mm):", max_sofar)