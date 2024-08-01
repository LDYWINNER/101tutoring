# CSE 101 DongYoon Lee
# Email: dongyoon.lee.1@stonybrook.edu



def biggest(u):
    if len(u) == 0:
        return None
    final = u[0]
    for k in range(1, len(u)):
        if u[k] > final:
            final = u[k]

    return final

def largestBelowValue(numbers, value):
    res = []
    for x in range(len(numbers)):
        if numbers[x] < value:
            res.append(numbers[x])
    return biggest(res)


print(largestBelowValue([31, 5, 71, 53, 40, 17], 40))

print(largestBelowValue([31, 5, 71, 53, 40, 17], 41))

print(largestBelowValue([31, 5, 71, 53, 40, 17], 2))