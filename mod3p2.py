for word in open("pride_and_prejudice.txt"):
  word1 = word.rstrip("\n")
  if not "e" in word1:
    print(word1)