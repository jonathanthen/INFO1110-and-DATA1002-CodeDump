avg_temps = {}
is_first_line = True

for row in open("climate_data_2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    maxwind = values[9]
    ninetemp = float(values[11])
    ninehum = float(values[12])
    floorhum = ninehum // 20
    
    dictkey = (maxwind, floorhum)
    
    if dictkey not in avg_temps:
      avg_temps[dictkey] = [ninetemp]
      
    else:
      avg_temps[dictkey].append(ninetemp)

for key in sorted(avg_temps):
  print(key, ":", round(sum(avg_temps[key]) / len(avg_temps[key]),1))