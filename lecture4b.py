alist = ["me", "I", 5, "it"]
print(alist.index("I"))

print(alist.count(5))
print(alist[1:3])
print(alist[0:3:3])
print(alist[::-1])

blist = list("my dog")
blists = "my dog".split()
print(blists)
astring = ":".join(blists)
print(astring)

print(alist[0])
print(alist[-1])

x=4
clist = [2,1,0]
dlist = [2,3,0]
elist = clist
clist[1] = 3
dlist[1] = 2
print(elist)
x = clist[1]
print(x)

print(alist.pop())
print(alist.reverse())