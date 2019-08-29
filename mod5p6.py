t = False

for num in open("min_temperatures_2016.txt"):
  numfloat = float(num)
  if not t:
    maxnum = numfloat
    t = True
    
  else:
    maxnum = max(maxnum, numfloat)
    
print(maxnum)