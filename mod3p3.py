for word in open("pride_and_prejudice.txt"):
  if word.startswith("e"):
    if "e" in word:
      print(len(word.rstrip("\n")))
