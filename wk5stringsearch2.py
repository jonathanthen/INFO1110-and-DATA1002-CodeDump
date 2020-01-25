def starts_with(word, chs):
    if word == "":
        return False
    elif len(chs) == 0:
        return False
    else:
        i = 0
        while i < len(chs):
            if word.startswith(chs[i]) == True:
                return True
            i += 1
        return False
		
	# You can put the function you made in part 1 here;
	# It might be helpful when making your search() function!

def search(words, start_chs):
	# Start writing your search() function here!
	newlis = []
	if len(words) == 0 or len(start_chs) == 0:
		return []
	else:
		j = 0
		while j < len(words):
			torf = starts_with(words[j], start_chs)
			if torf == True:
				newlis.append(words[j])
			j += 1
		return newlis