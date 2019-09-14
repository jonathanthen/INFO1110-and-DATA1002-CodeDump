multiples = []

number = 200

while number >= 0:
    if number % 13 == 0:
        multiples.append(number)
    number -= 1

print(multiples)