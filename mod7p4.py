""" This is some skeleton code for your solution.
    We're creating an empty dictionary at the beginning
    that you can use for the aggregation and we provide the
    code to format the output of your program at the end. """

temp_bins = {}

sc4 = []
sc5 = []
sc6 = []
sc7 = []

is_first_line = True
for row in open("climate_data_Dec2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    date = values[0]
    station = values[2]
    maxtemp = float(values[5])
    bins = float(maxtemp // 5)
    
    if date == "2017-12-25":
      if bins == 4.0:
        sc4.append(station)
      elif bins == 5.0:
        sc5.append(station)
      elif bins == 6.0:
        sc6.append(station)
      elif bins == 7.0:
        sc7.append(station)
      
    if bins not in temp_bins:
      if bins == 4.0:
        temp_bins[bins] = sc4
      elif bins == 5.0:
        temp_bins[bins] = sc5
      elif bins == 6.0:
        temp_bins[bins] = sc6
      elif bins == 7.0:
        temp_bins[bins] = sc7
        
for key in sorted(temp_bins):
  print(key, ":", sorted(temp_bins[key]))