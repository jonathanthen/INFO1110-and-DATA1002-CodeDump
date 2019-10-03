line_count = 0
rainfall = 0

for row in open("climate_data_2017.csv"):
  if line_count > 0:
    values = row.split(",")
    maxtemp = float(values[2])
    if maxtemp > 35:
      rainfall = float(values[3])
  line_count += 1
  
print("Maximum amount of rainfall on hot days:",rainfall, "mm")