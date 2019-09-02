import sys

print("V = { " + sys.argv[1] + ", " + sys.argv[2] + ", " + sys.argv[3] + " }")
print("U = { " + sys.argv[4] + ", " + sys.argv[5] + ", " + sys.argv[6] + " }")
dot = (int(sys.argv[1]) * int(sys.argv[4])) + (int(sys.argv[2]) * int(sys.argv[5])) + (int(sys.argv[3]) * int(sys.argv[6]))
print("V . U = " + str(dot))