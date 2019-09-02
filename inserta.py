countries = ["Malaysia", "Mozambique", "Benin", "Ukraine"]
countries.insert(len(countries), "South Sudan")
print(countries)

letters = ["b", "c", "d"]
letters.insert(0, "a")
print(letters)

index = 4
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Friday", "Saturday"]
days.insert(index, "Thursday")
print(days)

mylist = []
x = 1
while x < 10:
    mylist.insert(len(mylist), x)
    x += 1
print(mylist)

mylist1 = []
x = 1
while x < 10:
    mylist1.insert(0, x)
    x += 1
print(mylist1)