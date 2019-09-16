odds = []

total = 0
number = 100

while number <= 200:
    if number % 2 == 1:
        odds.append(number)
        total += number
    number += 1

print(total)