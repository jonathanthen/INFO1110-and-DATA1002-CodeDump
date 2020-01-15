def total_rainfall(filename):
  total = 0
  for line in open(filename):
    line = line.strip()
    total += float(line)
  return total

def count_rainfall(filename):
  count = 0
  for line in open(filename):
    count += 1
  return count

def max_rainfall(filename):
  maximum = 0
  for line in open(filename):
    line = line.strip()
    maximum = max(maximum, float(line))
  return maximum

def average_rainfall(filename):
  return total_rainfall(filename) / count_rainfall(filename)

print("Please choose an aggregation. It must be one of:")
print("1. sum")
print("2. max")
print("3. average")

choice = int(input("Choice [1-3]: "))

if choice == 1:
  result = total_rainfall('rainfall.txt')
  print("Total:", result)
elif choice == 2:
  result = max_rainfall('rainfall.txt')
  print("Maximum:", result)
elif choice == 3:
  result = average_rainfall('rainfall.txt')
  print("Average:", result)
else:
  print("Invalid selection!")