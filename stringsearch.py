words = ['frosty', 'chocolate', 'milkshake', '', 'glazed', 'raspberry', 'donut'] 
start_chs = ['a', 'b', 'c', 'd']

def starts_with(word, chs):
    i = 0
    while i < len(chs):
        if word[0] == chs[i]:
            return True
        i += 1
    return False

def search(words, start_chs):
    result = []
    i = 0
    while i < len(words):
        if starts_with(words[i], start_chs):
            result.append(words[i])
        i += 1
    return result

filtered_words = search(words, start_chs)