for line in open("jane_eyre.txt"):
  line_strip = line.rstrip()
  if line_strip.startswith("T"):
    print(len(line_strip))