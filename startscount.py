def start_count(words, ch):
    if len(words) == 0:
        return None
    else:
        i = 0
        count = 0
        
        while i < len(words):
            if words[i].startswith(ch):
                count += 1
            i += 1
        
        
        return count

dogs = ['Collie', 'Retriever', 'Corgi', 'Labrador', 'Husky', 'Malamute']
print(start_count(dogs, 'C'))