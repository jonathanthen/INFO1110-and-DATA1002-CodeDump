for word in open("pride_and_prejudice.txt"):
  if len(word.rstrip("\n")) > 6:
    print(word)