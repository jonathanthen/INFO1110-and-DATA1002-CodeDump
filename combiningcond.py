for word in open("pride_and_prejudice.txt"):
    if len(word.rstrip("\n")) < 5 and "e" in word and not word.rstrip("\n").endswith("e"):      
      print(word)





word = "well\n"
word_s = word.rstrip("\n")
if len(word_s) < 5 and "e" in word_s and not word_s.endswith("e"):
  print(word_s)