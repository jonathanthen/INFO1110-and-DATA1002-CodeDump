humidcities = {}
is_first_line = True

for row in open("climate_data_Dec2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    ninehum = float(values[12])
    date = values[0]
    count = 0
    
    if date not in humidcities and (ninehum > 80):
      humidcities[date] = [ninehum]
    elif date in humidcities and(ninehum > 80):
      humidcities[date].append(ninehum)
      
for dateelem in humidcities:      
  for elem in humidcities[date]:
    count += 1
    break

print("There were",(count),"days with 9am humidity levels over 80%.")