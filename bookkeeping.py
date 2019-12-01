item = []
cost = []
itemcount = 0

while True:
    itemcost = input("Enter item and cost: ")

    if len(item) > 0 and itemcost == 'stop':
        break
        
    elif len(item) == 0 and itemcost == 'stop':
        print("No items entered.")
        break
    
    else:
        itemcost = itemcost.split(" ")

        if len(itemcost) > 2 or len(itemcost) < 2:
            print("Invalid input. Requires item and cost.")
            continue
            
        item1 = itemcost[0]
            
        try:
            cost1 = float(itemcost[1])
        except ValueError:
            print("Invalid input. Cost must be numeric.")
            continue

        if cost1 < 0:
            print("Invalid input. {} cannot have negative cost.".format(itemcost[0]))
            continue

        item.append(item1)
        cost.append(cost1)
        itemcount += 1

if len(item) > 0: 
    i = 0
    total = 0
    avgcount = 0
    while i < len(cost):
        total += cost[i]
        i += 1
    avgcost = total/itemcount
    print("The average cost of all items is ${:.2f}.".format(avgcost))

    j = 0
    while j < len(cost):
        if cost[j] > avgcost:
            avgcount += 1
        j += 1
    if avgcount == 1:
        print("There is {} item above average cost.".format(avgcount))
    else:
        print("There are {} items above average cost.".format(avgcount))
