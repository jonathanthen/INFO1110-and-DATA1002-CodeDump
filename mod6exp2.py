for line in open("jane_eyre_sentences.txt"):
  line_strip = line.rstrip()
  words = line_strip.split()
  long_words = 0
  for word in words:
    if len(word) > 5:
      long_words +=1
  if long_words > 4:
    print(words[-1])