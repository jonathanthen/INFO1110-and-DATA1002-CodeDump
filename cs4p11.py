import sys
name = sys.argv[1]
weight = float(sys.argv[2])

cost = 1.3 * weight
cost = '{:.2f}'.format(cost)

print("You've requested delivery to {}. The cost of delivery is ${}.".format(name, cost)  )
