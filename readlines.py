def readlines(path):
    lis = []
    lines = open(path)
    for line in lines:
        path.rstrip("\n")
        lis.append(line)

    return lis

print(readlines("baby.txt"))





