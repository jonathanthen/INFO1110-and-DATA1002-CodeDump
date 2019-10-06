import sys
h = int(sys.argv[1])
w = h * 2

i = 2
print("+" + "-"*(w-2) + "+")
while i < h:
    print("|" + " "*(w-2) + "|")
    i += 1

print("+" + "-"*(w-2) + "+")