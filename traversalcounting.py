def init_trace(grid, size):
    count = 1
    for x in range(size):
        for y in range(size):
            grid[ x ] [ y ] = count
            count += 1

def printing(grid, size):
    for x in range(size):
        for y in range(size):
            print(grid[x][y], end = " ")
        print("")

print(init_trace((2,2), 4))
