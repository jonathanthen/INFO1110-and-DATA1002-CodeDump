import numpy as np

#Initialise
grid = np.zeros((2,2)).astype('int32')

# Traversal to ASSIGN the initial value
for x in range(2):
    for y in range(2):
        grid [ x ] [ y ] = 1 

# Traversal to DISPLAY values
for x in range(2):
    for y in range(2):
        print(grid [x] [y], end = " ")
    print("")

