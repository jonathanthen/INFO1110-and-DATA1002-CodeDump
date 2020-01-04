def get_0_to_50(numbers):
    results = []
    for n in numbers:
        if n>= 0 and n < 50:
            results.append(n)

    return results

def get_ez(strings):
    results = []
    for s in strings:
        if len(s) < 2:
            continue
        if s[0] == "E" and s[1] == 'Z':
            results.append(s)

    return results

def is_0_to_50(n):
    if n >= 0 and n < 50:
        return True
    return False

nums = [0, -1, 4, 55, 25, 49, 50]
result = list(filter(is_0_to_50, nums))
print(result)

def is_ez(s):
    if len(s) < 2:
        return False
    if s[0] == 'E' and s[1] == 'Z':
        return True
    return False

strings = ["ezasd", "EZabs", "EZ", "EzZ"]
results = list(filter(is_ez, strings))
print(results)