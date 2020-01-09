line_counter = 0
with open('quotes_by_EWD.txt', 'r') as input_file:
  for line in input_file:
    words = line.rstrip().split()
    found = False
    for word in words:
      lower_w = word.rstrip(',;.').lower()
      if lower_w == 'programmer' or lower_w == 'programming':
        found = True
    if found:
      char_counter = 0
      for ch in line:
        if ch.isalpha():
          char_counter += 1
      print(str(line_counter) + ':' + str(char_counter), words[-1].rstrip(',;.'))
    line_counter += 1