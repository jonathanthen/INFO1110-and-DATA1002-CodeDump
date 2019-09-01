five = float(input("Enter the number of $5 notes: "))
fifty = float(input("Enter the number of 50c coins: "))
cost = float(input("Enter the cost of an item: "))

total = (five * 5) + (fifty * 0.5)

if total < cost:
    print("There is not enough money to pay for the item.")
else:
    print("There is enough money to pay for the item.")