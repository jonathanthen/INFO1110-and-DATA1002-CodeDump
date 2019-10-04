max_rain_per_state = {}
is_first_line = True

for row in open("climate_data_Dec2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    state = values[1]
    rain = float(values[6])
    humidity = float(values[12])
    if humidity > 60:
      if state in max_rain_per_state:
         max_rain_per_state[state] = max(rain, max_rain_per_state[state])
      else:
        max_rain_per_state[state] = rain
    
print("Maximum rainfall per state on humid days:")
print(max_rain_per_state)