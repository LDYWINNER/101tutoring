# 1
def calculateArea(width, height):
    return width * height
# Take input from the user
width = float(input('Enter width in inches: '))
height = float(input('Enter height in inches: '))
# Call the function and store the calculated area
area = calculateArea(width, height)
print('The total area in inches is: ', area)
# Now print the area with 2 decimal precision.
print('The total area in inches is: ', '{:.2f}'.format(area))

# 2
def countertop(sideLength):
    """
    Compute the area of a square countertop with a missing wedge. The parameter x is
    the length of one side of the square.
    """
    square = sideLength ** 2 # area of the full square
    triangle = ((sideLength / 2) ** 2) / 2 # area of the missing wedge
    return square - triangle

user_Input = float(input('Enter the side length: '))

result = countertop(user_Input)

print(result)

# 3
def celsius(f):
    return (f - 32) * 5 / 9

# 4
from math import pi
def sphereVolume(n):
    return (4 / 3) * (n ** 3) * pi

print(sphereVolume(2.0))
print(sphereVolume(5.0))


