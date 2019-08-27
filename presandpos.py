for line in open("jane_eyre_sentences.txt"):
 words = line.split()
 if "and" in words:
   pos = words.index("and")
   print(len(words)-pos-1)