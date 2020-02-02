def hailstones(n):
    lis = []
    lis.append(n)
    if n == 1:
        return lis
    else:
        if n % 2 == 0:
            return lis + hailstones(n/2)
        elif n % 2 == 1:
            return lis + hailstones((3*n) + 1)
        