sum = 0
count = 0

while True:
    num = input("")
    if num == "":
        break
    else:
        num = int(num)
        if num > 0 or num < 0:
            sum += num
            count += 1
        elif num == 0:
            continue
        
avg = sum / count
print("The average is {:.2f}".format(avg))
    