s = 0
for value in open("rainfall_March2017.txt"):
  value_float = float(value)
  s += value_float

print("Total rainfall (mm):", s)