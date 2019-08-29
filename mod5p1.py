count = 0
for line in open("jane_eyre.txt"):
  line_strip = line.rstrip()
  if line_strip.endswith(" end"):
    count += 1
print("There are",count,"lines that end in 'end'.")