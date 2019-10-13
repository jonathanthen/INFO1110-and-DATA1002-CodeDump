def readlines(path):
    f = open(path, "r")
    result = []
    for line in f:
        result.append(line.rstrip())
    f.close()
    return result

print(readlines("baby.txt"))