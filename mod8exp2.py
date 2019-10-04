hot_cities = {}
is_first_line = True

for row in open("climate_data_Dec2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    temperature = float(values[5])
    state = values[1]
    city = values[2]
    if temperature > 30 and state == "NSW":
      if city not in hot_cities:
        hot_cities[city] = temperature

print("Cities with at least one day above 30 degrees:")
for key in sorted(hot_cities):
  print(key)