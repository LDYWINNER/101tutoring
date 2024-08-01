def upsideDownPyramid(n):
    i = n
    x = 10
    while i > 0:
        for j in range(x, x + n):
            print(j, end=' ')
        i -= 1
        x += 10
        n -= 1
        print('\n')

upsideDownPyramid(3)
upsideDownPyramid(9)