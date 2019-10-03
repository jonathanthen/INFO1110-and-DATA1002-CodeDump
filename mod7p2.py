state = {}
is_first_line = True

for row in open("climate_data_Dec2017.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    humidity = float(values[12])
    st = values[1]
    if st in state:
      if humidity >= state[st]:
        state[st] = humidity
    else:
      state[st] = humidity

for st in sorted(state):
  print(st, ":", state[st])