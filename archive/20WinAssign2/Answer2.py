
def printZ(n):
    lineNum = 1
    while lineNum <= n:
        if lineNum == 1 or lineNum == n:
            print('*' * n, end='')
            print('\n', end='')
        else:
            print((' ' * (n - lineNum) + '*' + ' ' * (lineNum - 1)), end='')
            print('\n', end='')
        lineNum += 1



printZ(3)
printZ(10)


def ones(a):
    if a == 1:
        return 1
    return (10 ** (a - 1) + ones(a - 1))

def seriesSum(n, t):
    total = 0
    x = 1
    while x < (t + 1):
        total += (n * ones(x))
        x += 1
    return total

print(seriesSum(3, 5))
print(seriesSum(4, 10))
print(seriesSum(9, 25))