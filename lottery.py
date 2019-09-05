#Spot the Error
ticket1 = [14, 7, 23, 9]
ticket2 = [40, 3, 4, 38]
lottery = [ticket1, ticket2]

number_drawn = int(input("Enter the next lottery number: "))
if number_drawn in lottery:
    print("You have the number!")
else:
    print("You don't have the number.")