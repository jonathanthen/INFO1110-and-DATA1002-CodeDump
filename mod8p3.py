low_rainfall = {}
is_first_line = True

for row in open("climate_data_2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    state = values[1]
    rainfall = float(values[6])
    date = values[0]
    month = date.split("-")[1]
    
    if state in low_rainfall:
      if month in low_rainfall[state]:
        low_rainfall[state][month].append(rainfall)
      else:
        low_rainfall[state][month] = [rainfall]
    else:
      low_rainfall[state] = {month: [rainfall]}
      
min_rainfall = 0
for state in low_rainfall:
  for month in low_rainfall[state]:
    if min_rainfall < min(low_rainfall[state][month]):
      lstate = state
      lmonth = month
      min_rainfall = min(low_rainfall[state][month])
      
print("Month: " + lmonth)
print("State: " + lstate)