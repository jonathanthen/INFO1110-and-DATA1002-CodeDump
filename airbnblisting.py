house = {}
is_first_line = True
priv = 0
entire = 0

for row in open("sydney_listings.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    room_type = values[1]
    min_nights = values[3]
    last_review = values[5].rstrip("\n")
    if last_review == "":
      last_review = "1/1/1999"
    month = last_review.split("/")[2]
    
    if int(min_nights) >= 2 and int(min_nights) <= 4 and month == '2019':
      if room_type == "Private room":
        priv += 1
      elif room_type == "Entire home/apt":
        entire += 1
    
print("Private room:", priv)
print("Entire home/apt:", entire)