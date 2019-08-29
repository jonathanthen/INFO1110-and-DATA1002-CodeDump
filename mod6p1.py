for line in open("jane_eyre_sentences.txt"):
  line = line.lower()
  words = line.split()
  if "the" in words:
    print(words.index("the"))
  else:
    print("missing")