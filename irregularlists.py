def traverse(ls):
    i = 0
    while i < len(ls):
        j = 0
        while j < len(ls[i]):
            print(ls[i][j], end = " ")
            j += 1
        print()
        i += 1

ls_a = [[1,2], [3,4,5,6], [7,8,9]]
traverse(ls_a)