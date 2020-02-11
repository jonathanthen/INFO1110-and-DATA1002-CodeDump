import sys

try:
    f = open(sys.argv[1])
except FileNotFoundError:
    print("Error: Cannot open specified file.")
    sys.exit()
except IndexError:
    print("Usage: python3 less.py <filename>")
    sys.exit()
try: 
    sentence = f.readline().rstrip()
    print(sentence)
    while True:
        inp = input()
        if inp == "q":
            break
        elif inp == "":
            sentence = f.readline().rstrip()
            if sentence == "":
                break
            print(sentence)
except EOFError:
    sys.exit()