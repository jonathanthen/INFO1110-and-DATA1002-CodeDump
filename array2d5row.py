import numpy as np

#Initialise
grid = np.zeros((5,10)).astype('int32')

for x in range(5):
    for y in range (10):
        grid[x][y] = 1

for x in range(5):
    for y in range(10):
        print (grid[x][y], end = " ")
    print("")