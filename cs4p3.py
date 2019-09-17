def shout(x):
    x = str(x)
    x_upper = x.upper()
    if not x_upper.endswith("!"):
        b = x_upper + "!"
    else:
        b = x_upper
    return b

print(shout("hello!"))