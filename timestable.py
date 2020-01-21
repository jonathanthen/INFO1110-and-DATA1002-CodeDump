import numpy as np

def times_tables(n):
    big_list = []
    i = 1
    while i <= n:
        j = i
        small_list = []
        while j <= i*n:
            small_list.append(j)
            j += i
        big_list.append(small_list)
        i += 1

    return big_list

grid = times_tables(3)
print(grid)

#for line in grid:
#   print(line)

def numpy_table(n):
    grid = np.zeros((n,n)).astype("int32")

    for i in range(n):
        for j in range(n):
            grid[i][j] = (i+1)*(j+1)

    for i in range(n):
        for j in range(n):
            print(grid[i][j], end = ' ')
        print("")

numpy_table(3)