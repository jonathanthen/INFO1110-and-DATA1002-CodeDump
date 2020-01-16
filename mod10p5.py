def process_line(filename):
  counter = 0
  for line in open(filename):
    line = line.strip()
    temp = float(line)
    if temp > 35:
      counter += 1
  return counter

hot_days = 0

result1 = process_line('temperatures_2015.txt')
result2 = process_line('temperatures_2016.txt')

hot_days = result1 + result2

print("Number of hot days:", hot_days)