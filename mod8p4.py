august_data = {}
lis = []
is_first_line = True

for row in open("climate_data_2017_numeric.csv"):
  if is_first_line:
    is_first_line = False
    field_names = row.split(",")
  else:
    values = row.split(",")
    date = values[0]
    month = date.split("-")[1]
    day = date.split("-")[2]
    
    if month != "07":
      if day not in august_data:
        field_dict = {}
        for index in [1, 2, 3, 4, 5, 6, 7, 8]:
          field_name = field_names[index]
          field_value = float(values[index])
          field_dict[field_name] = [field_value]
          august_data[day] = field_dict
      else:
        for index in [1, 2, 3, 4, 5, 6, 7, 8]:
          field_name = field_names[index]
          field_value = float(values[index])
          august_data[day][field_name].append(field_value)
          
print("Available field names:")
for name in field_names[1:]:
  print(name.rstrip("\n"))
  
requested_field = input("Please enter a field name: ")

#Check that the input is valid:
if requested_field not in field_names[1:]:
  print("Invalid field name entered.")
else:
  print("Statistics for field '"+requested_field+"':")
  for key in august_data:
    field = august_data[key][requested_field]
    lis.append(field)

  lmini = []
  lmaxi = []
  for elem in lis:
      mini = min(elem)
      maxi = max(elem)
      lmini.append(mini)
      lmaxi.append(maxi)

  for elem2 in lmini:
    final_mini = min(lmini)
  for elem3 in lmaxi:
    final_maxi = max(lmaxi)

print("  Min:", final_mini, "Max:", final_maxi)
    
#Minimum temperature (C)