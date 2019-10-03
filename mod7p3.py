wind_direction = {}
is_first_line = True

for row in open("climate_data_Dec2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    winddir = values[9]
    date = values[0]
    
    if "2017-12-26" not in date:
      if winddir not in wind_direction:
        wind_direction[winddir] = 0
        
    else:
      if winddir in wind_direction:
        wind_direction[winddir] += 1
      else:
        wind_direction[winddir] = 1

for winddir in sorted(wind_direction):
  print(winddir, ":", wind_direction[winddir])