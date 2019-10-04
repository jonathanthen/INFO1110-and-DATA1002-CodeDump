minimum_temps = {}
is_first_line = True

for row in open("climate_data_Dec2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    state = values[1]
    min_temp = float(values[4])
    max_temp = float(values[5])
    temp_bin = max_temp // 10

    dict_key = (state, temp_bin)
    if dict_key not in minimum_temps:
      minimum_temps[dict_key] = min_temp
    else:
      minimum_temps[dict_key] = min(min_temp, minimum_temps[dict_key])

print("Minimum temperatures per state and per 10 degree max. temperature range:")
for key in sorted(minimum_temps):
  print(key, ":", minimum_temps[key])