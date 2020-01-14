def greet(name):
  print("Hello,", name)

greet("World")
greet("Foo")
greet("Bar")
greet("USYD")

def add_two_numbers(x, y):
  return x + y
  
print(add_two_numbers(1, 2))

def hi_there():
  print("Hi")
  return
  print("there!")

hi_there()

def main_wind_direction(direction):
  if direction.startswith("N"):
    return "Mostly from the north"
  elif direction.startswith("E"):
    return "Mostly from the east"
  elif direction.startswith("S"):
    return "Mostly from the south"
  elif direction.startswith("W"):
    return "Mostly from the west"
  else:
    return "Not a valid wind direction"

print(main_wind_direction("NNE"))