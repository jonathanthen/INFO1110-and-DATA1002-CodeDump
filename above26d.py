num_temps = 0
num_above26 = 0

for value in open("temperatures_Jan2017.txt"):
  value_float = float(value)
  num_temps += 1
  if value_float > 26:
    num_above26 += 1
    
if num_above26 == num_temps:
  print("All temperatures are above 26 degrees.")
else:
  print("There is at least one temperature below 26 degrees.")