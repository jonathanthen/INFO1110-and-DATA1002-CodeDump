import numpy as np

matrix = np.zeros((3,2)).astype('int32')
count = 1
for i in range(3):
    for j in range(2):
        matrix[i][j] = count
        count += 1

for i in range(3):
    for j in range(2):
        print(matrix[i][j], end = " ")
    print()

# int8 maximum value is 127