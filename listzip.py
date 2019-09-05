list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["1", "2", "3", "4", "5", "6"]

#create zip object
result = zip(list1, list2)
new_list = list(result)
print(result)
# some weird zip object
print(new_list)

namelist = ["Sunset", "Amber Jewel", "Teagan", "Queen Garnet"]
weightlist = [0.87, 0.972, 0.797, 1.332]
unitcost = [2.99, 6.99, 3.99, 17.99]
pricelist = [2.61, 6.79, 3.18, 23.96]
# present invoice
simplebill = list(zip(namelist, pricelist))
print(simplebill)

fullbill = list(zip(namelist, weightlist, ["kg @ $"]*4, unitcost, ["/kg = $"]*4, pricelist))
print(fullbill)

print(fullbill[1])