monthly_humidities = {}
is_first_line = True

for row in open("climate_data_2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    city = values[2]
    if city == "Sydney":
      date = values[0]
      month = date.split("-")[1]
      humidity = float(values[12])

      if month in monthly_humidities:
        monthly_humidities[month].append(humidity)
      else:
        monthly_humidities[month] = [humidity]

# Build a dictionary of average humidities
avg_monthly_humidities = {}
for key in monthly_humidities:
  humidities = monthly_humidities[key]
  average_humidity = sum(humidities)/len(humidities)
  avg_monthly_humidities[key] = average_humidity
 
# Aggregate the values to find highest average humidity
max_month = ""
max_average_humidity = -1
for key in avg_monthly_humidities:
  if avg_monthly_humidities[key] > max_average_humidity:
    max_average_humidity = avg_monthly_humidities[key]
    max_month = key

print("Month:", max_month)
print("Maximum average humidity:", max_average_humidity)

monthly_humidities = {}
is_first_line = True

for row in open("climate_data_2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    city = values[2]
    if city == "Sydney":
      date = values[0]
      month = date.split("-")[1]
      humidity = float(values[12])

      if month in monthly_humidities:
        monthly_humidities[month].append(humidity)
      else:
        monthly_humidities[month] = [humidity]

# Aggregate the values in the dictionary
max_average_humidity = -1
max_month = ""
for key in monthly_humidities:
  humidities = monthly_humidities[key]
  average_humidity = sum(humidities)/len(humidities)
  if average_humidity > max_average_humidity:
    max_average_humidity = average_humidity
    max_month = key

print("Month:", max_month)
print("Maximum average humidity:", max_average_humidity)