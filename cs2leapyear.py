ly = int(input("Enter a year: "))

if ly % 4 == 0:
    if ly % 400 == 0:
        print("The year",ly,"is a leap year.")
    elif ly % 100 == 0:
        print("The year",ly,"is not a leap year.")
    else:
        print("The year",ly,"is a leap year.")
else:
    print("The year",ly,"is not a leap year.")