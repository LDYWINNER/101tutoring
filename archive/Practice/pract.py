def isort(a):
    for i in range(1, len(a)):
        print(a[:i], a[i:])
        more_left(a, i)

def more_left(a, j):
    x = a.pop(j)
    while j>0 and a[j-1]>x:
        j -=1
    a.insert(j, x)


