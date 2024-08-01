from math import *

def mersennes(n):
    result = []
    for all in range(2, n + 1):
        if isPrime(all) and (all + 1) in isOnlyTwo(n):
            result.append(all)
    print(result)


def isPrime(a):
    temp = round(sqrt(a))
    for x in range(2, temp):
        if a % x == 0:
            return False
    return True


def isOnlyTwo(b):
    total = []
    temp2 = 2
    while temp2 <= b:
        total.append(temp2)
        temp2 *= 2
    return total




mersennes(1000)
mersennes(1000000)
