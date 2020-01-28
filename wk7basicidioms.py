def longest(words):
    if len(words) == 0:
        return None
    else:
        i = 0
        longestword = words[0]
        while i < len(words):
            if len(words[i]) >= len(longestword):
                longestword = words[i]
            i += 1
        return longestword
    
def shortest(words):
    if len(words) == 0:
        return None
    else:
        j = 0
        shortestword = words[0]
        while j < len(words):
            if len(words[j]) < len(shortestword):
                shortestword = words[j]
            j += 1
        return shortestword

def av_len(words):
    if len(words) == 0:
        return 0
    else:
        k = 0
        total = 0
        while k < len(words):
            total += len(words[k])
            k += 1
        return total/len(words)
    
def start_count(words,ch):
    g = 0
    count = 0
    while g < len(words):
        w = words[g].lower()
        ch = ch.lower()
        if w.startswith(ch):
            count += 1
        g += 1
    return count
        