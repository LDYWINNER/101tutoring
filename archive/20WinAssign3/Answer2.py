from math import *

def isPrime(num):
    for i in range(2, round(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def goldbachConjecture(evenNum):
    temp = []
    result = []
    for i in range(2, evenNum // 2):
        temp.append([i, evenNum - i])
    #print(temp)

    for pair in temp:
        if isPrime(pair[0]) and isPrime(pair[1]):
            result.append([pair[0], pair[1]])
    #print(result)

    for answer in result:
        print(evenNum, '=', answer[0], '+', answer[1], '(both are primes)')


(goldbachConjecture(38))
print()
(goldbachConjecture(44))
print()
(goldbachConjecture(56))
