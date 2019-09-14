multiples = []

number = -100

while number < 100:
    if number % 7 == 0:
        multiples.append(number)
    number += 1

print(multiples)