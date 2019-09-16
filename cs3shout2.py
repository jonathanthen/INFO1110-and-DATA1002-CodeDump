count = 0

while count < 1:
    string = str(input("Enter a string: "))
    string = string.upper()
    if string == "STOP":
        count += 1
    else:
        print(string)