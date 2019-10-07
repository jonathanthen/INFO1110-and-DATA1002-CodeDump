import sys
h = int(sys.argv[1])
w = h * 2

i = 0
box = ""

while i < h:
    if i == 0 or i == (h - 1):
        box += '+'

        j = 0
        while j < (w-2):
            box += '-'
            j += 1
        box += '+'
        if i == 0:
            box += '\n'
    else:
        box += '|'
        k = 0
        while k < (w - 2):
            box += ' '
            k += 1
        box += '|\n'

    i += 1

print(box)