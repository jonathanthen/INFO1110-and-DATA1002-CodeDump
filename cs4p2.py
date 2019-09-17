def count_even_elements(x):
    count = 0
    for elem in x:
        if elem % 2 == 0:
            count += 1
    return count

lis = [1, 1, -6, 3, 3, -11]
print(count_even_elements(lis))