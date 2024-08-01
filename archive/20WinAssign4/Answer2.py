from math import *

def average_speed(x1, y1, x2, y2, unit_from, unit_to, t):
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if unit_to == unit_from:
        return distance / t * 3600
    else:
        if unit_to == 'ft':
            if unit_from == 'mile':
                distance *= 5280
                return distance / t * 3600
            elif unit_from == 'km':
                distance *= (5280 / 1.61)
                return distance / t * 3600
        elif unit_to == 'km':
            if unit_from == 'ft':
                distance *= (1.61 / 5280)
                return distance / t * 3600
            elif unit_from == 'mile':
                distance *= 1.61
                return distance / t * 3600
        elif unit_to == 'mile':
            if unit_from == 'km':
                distance /= 1.61
                return distance / t * 3600
            elif unit_from == 'ft':
                distance /= 5280
                return distance / t * 3600


print(average_speed(0, 0, 3, 4, 'km', 'mile', 1500)) #7.453416149068322
print(average_speed(0, 0, 12, 5, 'ft', 'km', 13)) #1.0977272727272729
print(average_speed(0, 0, 3, 4, 'mile', 'ft', 1000)) #95040.0
print(average_speed(0, 0, 12, 5, 'mile', 'km', 13000)) #5.796
print(average_speed(0, 0, 3, 4, 'km', 'ft', 2000)) #29515.527950310556
print(average_speed(0, 0, 3, 4, 'km', 'km', 5000)) #3.6