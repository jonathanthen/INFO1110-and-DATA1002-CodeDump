print("Option A")
aq = int(input("Quantity: "))
ap =int(input("Price: "))
print("")
atotal = float(ap / aq)

print("Option B")
bq = int(input("Quantity: "))
bp =int(input("Price: "))
print("")
btotal = float(bp / bq)

if btotal < atotal:
    print("Option B is cheaper!")
    
elif btotal > atotal:
    print("Option A is cheaper!")
    
else:
    print("They're the same!")