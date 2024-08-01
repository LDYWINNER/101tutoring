import math
def determineArea(a):
    circle = (a / math.sqrt(3)) ** 2 * math.pi
    triangle = a ** 2 * math.sqrt(3) / 4
    result = circle - triangle
    return round(result, 2)

print(determineArea(5))
print(determineArea(10))