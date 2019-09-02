# file = open("filename.txt", "r/w/a")

import sys

filename = sys.argv[1]
letter = sys.argv[2]
lis = []

file = open("whales.txt", "r") #can put filename since i set a variable
line = file.readline()

while line != "":
    line_lower = line.lower()
    linestrip = line_lower.rstrip("\n")
    if letter in linestrip[0]:
        print(linestrip)
    line = file.readline()


