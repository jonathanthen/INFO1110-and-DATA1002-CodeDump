for value in open("temperatures_Jan2017.txt"):
  value_float = float(value)
  if value_float > 90:
    value_C = (value_float - 32)* 5/9 
    print(value_C)