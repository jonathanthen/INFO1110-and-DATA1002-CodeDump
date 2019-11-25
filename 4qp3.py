distance = int(input("Enter distance: "))
steps = int(input("Enter no of steps: "))
total = 0
for i in range(steps):
  distance = distance/2
  total += distance
  
print("Distance travelled:",total)