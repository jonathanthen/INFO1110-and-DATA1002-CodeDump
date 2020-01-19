def writer(filename, lines):
    if type(filename) != str or type(lines) != list:
        raise TypeError

    f = open(filename, "wt")

    for x in lines:
        if type(x) != str:
            raise ValueError("Cannot write non-string value to file.")

        f.write(x)
        f.write("\n")

    f.close