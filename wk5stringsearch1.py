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