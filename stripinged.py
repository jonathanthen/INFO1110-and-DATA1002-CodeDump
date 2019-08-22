for word in open("pride_and_prejudice.txt"):
  word_s = word.rstrip("\n")
  if word_s.endswith("ing"):
    print(word_s.rstrip("ing"))
  elif word_s.endswith("ed"):
    print(word_s.rstrip("ed"))
  else:
    print(word_s)


word = "troublesome"
print(word)
if len(word) > 10:
  print("The word has more than 10 characters.")
elif len(word) > 5:
  print("The word has more than 5 and fewer than 10 characters.")
else:
  print("The word has fewer than or exactly 5 characters.")

word = "difficult"
print(word)
if len(word) > 10:
  print("The word has more than 10 characters.")
elif len(word) > 5:
  print("The word has more than 5 and fewer than 10 characters.")
else:
  print("The word has fewer than or exactly 5 characters.")

word = "hard"
print(word)
if len(word) > 10:
  print("The word has more than 10 characters.")
elif len(word) > 5:
  print("The word has more than 5 and fewer than 10 characters.")
else:
  print("The word has fewer than or exactly 5 characters.")


word = "Elizabeth"

if word.startswith("a"):
  print("The word starts with 'a'.")
elif word.startswith("A"):
  print("The word starts with 'A'.")
elif word.startswith("e"):
  print("The word starts with 'e'.")
elif word.startswith("E"):
  print("The word starts with 'E'.")
else:
  print("The word starts with neither 'A' or 'E'.")


word = "Jane"

if word.startswith("a"):
  print("The word ends with 'a'.")
else:
  print("The word does not end with an 'a'.")


word = "Bennet"

if word.startswith("B"):
  print("The word starts with 'B'.")
elif word.endswith("t"):
  print("The word ends with 't'.")
  
if word.startswith("B"):
  print("The word starts with 'B'.")
if word.endswith("t"):
  print("The word ends with 't'.")  