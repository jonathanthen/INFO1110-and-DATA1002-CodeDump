import sys

p1 = str(input("Player 1 name: "))
p2 = str(input("Player 2 name: "))
secret = int(sys.argv[1])

while True:
    g1 = int(input("{}, what is your guess? ".format(p1)))
    if g1 > secret:
        print("Lower")
    elif g1 < secret:
        print("Higher")
    elif g1 == secret:
        print("{} wins!".format(p1))
        break
    g2 = int(input("{}, what is your guess? ".format(p2)))
    if g2 > secret:
        print("Lower")
    elif g2 < secret:
        print("Higher")
    elif g2 == secret:
        print("{} wins!".format(p2))
        break