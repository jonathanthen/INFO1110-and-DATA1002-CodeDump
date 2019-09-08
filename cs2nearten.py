integer = float(input("Enter a number: "))

if integer > 0 and (integer % 10 <= 2 or integer % 10 >= 8):
    print("This number is near a multiple of ten")
else:
    print("Not even close")