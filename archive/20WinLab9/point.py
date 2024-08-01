from math import *

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def polar(self):
        if self.x <= 0:
            return None
        else:
            return sqrt(self.x ** 2 + self.y ** 2), atan(self.y / self.x)


if __name__ == '__main__':
    p1 = Point(1,1)
    p2 = Point(4, 5)
    print(p1)
    print(p1.distance(p2))
    print(p1.polar())
