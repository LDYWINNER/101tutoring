# CSE 101 DongYoon Lee
# Email: dongyoon.lee.1@stonybrook.edu

from math import *

def sift(k, a):
    for i in range(2*k, len(a), k):
        a[i] = None

def non_nulls(a):
    res = []
    for x in a:
        if x is not None:
            res.append(x)
    return res

def sieve(n):
    worksheet = [None, None] + list(range(2, n))

    for k in range(2, ceil(sqrt(n))):
        if worksheet[k] is not None:
            sift(k, worksheet)
    return non_nulls(worksheet)

def biggest(a):
    x = a[0]
    for k in a:
        if k > x:
            x = k
    return x

def largestGap(n):
    nums = sieve(n)
    result = []
    for n in range(len(nums) - 1):
        sub = int(nums[n+1]) - int(nums[n])
        result.append(sub)
    return biggest(result)

print(largestGap(100))
print(largestGap(1000))
print(largestGap(10000))
# Additional test case
print(largestGap(100000))