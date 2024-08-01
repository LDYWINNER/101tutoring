# CSE 101 DongYoon Lee
# Email: dongyoon.lee.1@stonybrook.edu

from math import ceil, sqrt

def sift(k, a):
    for i in range(2 * k, len(a), k):
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

def smallest_gap(start_num, end_num):
    res = []
    first = sieve(start_num)
    second = sieve(end_num)
    for i in range(len(second)):
        if second[i] not in first:
            res.append(second[i])
    return smallest(res)

def smallest(a):
    gap = a[1] - a[0]
    for k in range(1, len(a)):
        if a[k + 1] - a[k] < gap:
            gap = a[k + 1] - a[k]
        return gap


print(smallest_gap(5, 12))  # 2

print(smallest_gap(1000, 1020))  # 4

print(smallest_gap(19, 24))
