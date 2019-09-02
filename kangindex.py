animals = ["armadillo", "bear", "kangaroo", "okapi", "squirrel"]
index = 0
index_found = None

while index < len(animals):
    item = animals[index]
    if item == "kangaroo":
        index_found = index
        break
    index += 1

if index_found == None:
    print("Not Found.")
else:
    print("Index:",str(index))