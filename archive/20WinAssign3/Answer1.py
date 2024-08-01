from math import *

def minPerimeter(area):
    temp = []
    temp2 = []
    for x in range(1, area + 1):
        if x not in temp:
            if area % x == 0:
                temp.append([x, int(area / x)])
    for i in range(len(temp) // 2):
        temp.pop()
    #print(temp)

    for pair in temp:
        temp2.append((pair[0] + pair[1]) * 2)
    #print(temp2)

    final = temp2[0]
    for num in temp2:
        if num < final:
            final = num
    #print(final)
    first = temp[temp2.index(final)][0]
    second = temp[temp2.index(final)][1]

    print(final, 'where rectangle sides are', first, 'and', str(second) + '.')

minPerimeter(30)
minPerimeter(101)
minPerimeter(4564320)