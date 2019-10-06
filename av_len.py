def av_len(words):
    if len(words) == 0:
        return None
    else:
        i = 0
        total = 0
        
        while i < len(words):
            total += len(words[i])
            i += 1
        
        avg = total / i
        return avg

dogs = ['Collie', 'Retriever', 'Corgi', 'Labrador', 'Husky', 'Malamute']
print(av_len(dogs))