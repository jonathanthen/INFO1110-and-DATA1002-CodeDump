from decimal import Decimal
price = float(input("What is the price of the item? "))
items = int(input("How many items? "))
total = Decimal(str(price)) * Decimal(str(items))
final = round(total,2)
print("That will be $" + str(final))