import sys

h = int(sys.argv[1])
w = 2*h

i = 0
if h > 0:
    box = ""

    while i < h:
        if i == 0 or i == (h - 1):
            box += '+'

            j = 0
            while j < (w-2):
                box += '-'
                j += 1
            box += '+'

            if i == 0 and h > 2:
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