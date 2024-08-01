
# < Your name >
# < Your SBU Email >

from math import ceil, sqrt

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

def smallest_gap(start_num, end_num):
    gap = []
    temp = sieveList(start_num, end_num)
    a = 0
    while (a + 1) < len(temp):
        gap.append(temp[a + 1] - temp[a])
        a += 1
    return smallest(gap)

def smallest(nums):
    final = nums[0]
    for num in nums:
        if num < final:
            final = num
    return final

def sieveList(start_num, end_num):
    temp = sieve(end_num)
    sieveResult = []
    for num in temp:
        if num >= start_num:
            sieveResult.append(num)
    return sieveResult


print(smallest_gap(5, 12)) # 2

print(smallest_gap(1000,1020)) # 4

print(smallest_gap(19, 24))