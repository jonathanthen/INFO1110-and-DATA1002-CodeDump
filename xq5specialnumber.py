def special_number(n):
    lis = []
    number = 1

    while len(lis) < n:
        lis.append(number)
        number += 2
        lis.append(number)
        number += 1

    return lis

print(special_number(10))