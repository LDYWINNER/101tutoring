# pow function
from math import pow
pow(9, 2) # 9 ** 2

from random import randint
def permute(a):
    for i in range(0, len(a) - 1):
        r = randint(i, len(a) - 1)
        a[i], a[r] = a[r], a[i]

d = [0,1,2,3,4,5,6,7,8,9,10]
permute(d); print(sorted(d[0:5])); print(d)
print()
permute(d); sorted(d); print(d[0:5])
print()
permute(d); d.sort(); print(d[0:5]); print(d)

