
alist = []

while True:
    num = float(input("Number: "))
    if num != 0:
        alist.append(num)
    else:
        break

print("Your numbers were:")
for elem in alist:
    print(elem)

# i = 0
# while i < len(alist):
#   print(alist[i])
# i += 1