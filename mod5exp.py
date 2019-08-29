mystring = "hello           world   "
print(mystring.split(" "))

word = "classic"
for letter in word:
  print(letter)

numbers = [3.14, 1.57, 6.18]
for number in numbers:
  print(number)

numbers = [1.3, 0.8, 2.5, 3.4]
numbers.append(0.5)
print(numbers)
numbers.sort()
print(numbers)

numbers = [1.3, 0.8, 2.5, 3.4]
print(len(numbers))

words = ["Jane", "Eyre"]
numbers = [1.3, 0.8, 2.5, 3.4]
print(words)
print(numbers)

numbers = [1, 2, 3]
words = ['one', 'two']

for word in words:
  print(word)
  for number in numbers:
    print(number)