import sys

try:
    f = open(sys.argv[1])
except FileNotFoundError:
    print("Error: Cannot find specific file")
    sys.exit()
except IndexError:
    print("Usage: python3 less.py <filename>")
    sys.exit()

print(f.readline())
while True:
    inp = input()
    if inp == "q":
        break
    elif inp == "":
        print(f.readline())
    else:
        print("Press enter for next line")