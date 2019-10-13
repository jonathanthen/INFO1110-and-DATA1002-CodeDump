def letter_count(x,y):
    if type(x) != list and type(x) != tuple:
        raise TypeError("First input is not a list or a tuple")
    else:
        i = 0
        v = 0
        c = 0
        while i < len(x):
            if type(x[i]) != str:
                raise InterruptedError("str is not a string!")
            else:
                word = x[i]
                word = word.lower()
                o = 0
                while o < len(word):
                    if word[o] == 'a' or word[o] == 'e' or word[o] == 'i' or word[o] == 'o' or word[o] == 'u':
                        v += 1
                        o += 1
                    else:
                        c += 1
                        o += 1
                i += 1

    if type(y) != str:
        raise TypeError("String state str must be a string!")
    else:
        if y == 'vowels':
            return v
        elif y == 'consonants':
            return c
        else:
            raise ValueError("String state str may only be ‘vowels’ or ‘consonants’.")

lis = ['qwe#$%']
print(letter_count(lis, 'consonants'))
