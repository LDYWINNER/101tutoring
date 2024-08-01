
def seriesSum(n, totalTerms):
    result = 0
    for i in range(totalTerms):
        result += (n * ones(i + 1))
    return result

def ones(a):
    if a == 1:
        return 1
    return (10 ** (a-1)) + ones(a - 1)

print(seriesSum(3, 5))
print(seriesSum(4, 10))
print(seriesSum(9, 25))

#print(ones(5))
