lis = []

while True:
    word = input("")
    if word == "":
        break

    else:
        lis.append(word) 
i = 0
while i < len(lis):
    if i == 0 or i % 2 == 0:
        print(lis[i])
    i += 1
        
print("")
j = 0
while j < len(lis):
    if j % 2 == 1:
        print(lis[j])
    j += 1