numbers = [7, 10, 1, 7]
numbers.remove(7)
print(numbers)

a = 600 + 100
b = "700"
c = 700 + 0.0
d = 700
mixed_list = [a, b, c, d]
mixed_list.remove(700)
mixed_list.remove(700)
mixed_list.remove(700)

print(mixed_list)
print(id(b))
print(id(mixed_list[0]))
# Variable b is left because it is a string
# S while we removedd the numbers

