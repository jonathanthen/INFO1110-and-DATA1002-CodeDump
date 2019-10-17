def shortest(words):
    if len(words) == 0:
        return None
    else:
        i = 0
        word = ""
        total = 999
        while i < len(words):
            w = len(words[i])
            if w < total:
                total = w
                word = words[i]
            i += 1
        return word

dogs = ['Collie', 'Retriever', 'Corgi', 'Labrador', 'Husky', 'Malamute']
print(shortest(dogs))