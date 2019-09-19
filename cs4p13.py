# Based on the height of the tile, you should be able to 
#figure out how many -'s and +|+'s need to be printed out on each line.
import sys

i = 0
h = int(sys.argv[1])
name = sys.argv[2]
name = name.upper()
w = 3 * h
dash = "-"
plus = "+|+"

if h % 2 == 0:
    print("Error: tile height must be an odd number")
else:
    if len(name) > w:
        print("Error: name must fit within {} characters".format(w))
    else:
        
#upper tile
        while i != (h//2):
            px = (2*i) + 1
            dx = (w - (3*px))//2
            i += 1
            print(dash*dx + plus*px + dash*dx)
            
#name tile        
        if len(name) == 6:
            namex = ((w - len(name))//2)
            print(dash*namex + '-' + name + dash*namex)
            
        else:
            namex = ((w - len(name))//2)
            print(dash*namex + name + dash*namex)
        
#lower tile
        i = i - 1
        while i != -1:
            px = (2*i) + 1
            dx = (w - (3*px))//2
            i -= 1
            print(dash*dx + plus*px + dash*dx)
        