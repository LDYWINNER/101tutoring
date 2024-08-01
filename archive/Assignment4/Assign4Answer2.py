# CSE 101 DongYoon Lee
# Email: dongyoon.lee.1@stonybrook.edu

from math import *
from decimal import Decimal

def average_speed(x1, y1, x2, y2, unit_from, unit_to, t):
    a = (x2 - x1)**2
    b = (y2 - y1)**2
    mid = a + b
    distance = sqrt(mid)

    if unit_from != unit_to:
        if unit_to == 'ft':
            if unit_from == 'km':
                print (((distance / 1.61 * 5280) / t) * 3600)
            elif unit_from == 'mile':
                print (((distance * 5280) / t) * 3600)

        elif unit_to == 'km':
            if unit_from == 'ft':
                print (((distance / 5280 * 1.61) / t) * 3600)
            elif unit_from == 'mile':
                d = distance * 1.61
                dt = Decimal(str(d)) / Decimal(str(t))
                dtt = dt * Decimal(3600)
                print(dtt)
                #print (((distance * 1.61) / t) * 3600)

        elif unit_to == 'mile':
            if unit_from == 'ft':
                print (((distance / 5280) / t) * 3600)
            elif unit_from == 'km':
                print (((distance / 1.61) / t) * 3600)

    else:
        final = ((distance / t) * 3600)
        print(final)


average_speed(0, 0, 3, 4, 'km', 'mile', 1500)
average_speed(0, 0, 12, 5, 'ft', 'km', 13)
average_speed(0, 0, 3, 4, 'mile', 'ft', 1000)
average_speed(0, 0, 12, 5, 'mile', 'km', 13000)
average_speed(0, 0, 3, 4, 'km', 'ft', 2000)
average_speed(0, 0, 3, 4, 'km', 'km', 5000)
# Additional test case
average_speed(0, 0, 12, 13, 'km', 'mile', 2000)