for word in open("pride_and_prejudice.txt"):
  if word.rstrip("\n").endswith("e"):
    length = len(word.rstrip("\n"))
    print(length)

word = "extraordinary"

if len(word) > 6:
  print("That's a long word")
  
if word == "remarkable":
  print("exceptional!")



word = "persuasion"

if word.startswith("p"):
  print("There is a 'p' at the beginning.")
  
if word.endswith("p"):
  print("There's a 'p' at the end.")


word = "insupportable"

if "a" in word:
  print("There is an 'a'.")
  
if "support" in word:
  print("We can also use 'in' with multiple characters.")