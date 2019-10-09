import sys

try:
    file = open(sys.argv[1])

    for line in file:
        print(line.rstrip("\n"))
        wait = input()
        if wait == "\n":
            print(line.rstrip("\n"))
        elif wait == "q":
            sys.exit()

except FileNotFoundError:
    print("No File Found!")
except IndexError:
    print("No System Argument!")