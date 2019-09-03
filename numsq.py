animals = ["armadillo", "bear", "kangaroo", "okapi", "squirrel"]
num_sq = 0
index = 0

while index < len(animals):
    item = animals[index]
    if item == 'squirrel':
        num_sq += 1
    index += 1
print("We found:",str(num_sq),"squirrel(s)")