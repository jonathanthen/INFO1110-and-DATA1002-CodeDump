def integer(x):
    digits = list('0123456789')
    
    i = 0
    result = 0
    for digit in x:
        result *= 10

        for d in digits:
            result += digit > d
            print(result)
    return result