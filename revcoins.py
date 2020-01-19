amount = int(input("Enter a dollar amount: "))
denom = [100, 50, 20, 10, 5, 2, 1]

i = 0
while i < len(denom):
    notes = 0
    while amount >= denom[i]:
        notes += 1
        amount -= denom[i]

    if notes > 0:
        print(str(notes) + " x $" + str(denom[i]))

    i += 1