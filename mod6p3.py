for line in open("jane_eyre_sentences.txt"):
  line_strip = line.rstrip()
  words = line_strip.split()
  if len(words) > 10:
    print(" ".join(words[:3]) + " [..] " + " ".join(words[-3:]))

for line in open("jane_eyre_sentences.txt"):
  line_strip = line.rstrip()
  words = line_strip.split()

  new_words = words[2:-2]
  new_words1 = new_words[::2]
  print(" ".join(new_words1))