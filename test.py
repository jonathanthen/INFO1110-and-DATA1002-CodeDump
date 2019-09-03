print("I am going home {}, so I can wake up before {}".format("tonight", "daylight"))

y = 5.2
z = int(float(y)) // 2
print(type(z))

n = int(input("Enter the number of parrots: "))
count = 1

while n >= count:
    print("Parrot",count,"is talking")
    count += 1
if count > n:
    print("The parrots have spoken!")

a = 10
b = 20
c = 6
y = ((c > a) or (a > 7)) and ((not (b > 0)) or (b > a)) 
print(y)