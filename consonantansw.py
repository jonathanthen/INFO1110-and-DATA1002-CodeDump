

def consonant(ch):
    return len(ch) == 1 and not (ch == 'a' or ch == 'e' or ch == 'i' or ch =='u')

b = consonant('d')
a = consonant('e')
print(b)
print(a)