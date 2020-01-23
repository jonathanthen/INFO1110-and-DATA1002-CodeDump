#Create a multiplication table
import numpy as np 

grid = np.zeros((5,10)).astype('int32')

for i in range(5):
    for j in range(10):
        grid[i][j] = i * j

for i in range(5):
    for j in range(10):
        print(grid[i][j], end = ' ')
    print("")

print(len(grid))
print(grid)
print(len(grid[0]))
print(grid[1])
print(grid[2][9])