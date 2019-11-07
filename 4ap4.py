distance = int(input("Distance between cameras (km): "))
time = int(input("Time taken (mins): "))

speed = distance / time
speedlimit = speed * 60

if speedlimit > 70:
  print("Speed limit broken!")
else:
  print("Under the speed limit.")