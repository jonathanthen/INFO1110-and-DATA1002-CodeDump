def hailstones(n):
    if n > 0:
        if n == 1:
            return [1]
        if n % 2 == 0:
            return [n] + hailstones(n//2)
        if n % 2 == 1:
            return [n] + hailstones((3*n + 1))


print(hailstones(3))

#iterative is much more efficient
#recursive is easier to describe
#recursion is memory intensive and time inefficient