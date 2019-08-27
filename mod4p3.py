outercount = 0
for line in open("jane_eyre.txt"):
  line_strip = line.strip()
  innercount = 0
  for word in line_strip.split():
    if not 'e' in word:
      wordcount = len(word)
      innercount += wordcount
      outercount += innercount
  print(innercount)
    