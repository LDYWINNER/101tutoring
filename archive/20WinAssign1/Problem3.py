# CSE 101, Assignment 1, Problem 3
# Your name:
# Your SBU email address:

def shapeName(numberOfSides):
    if numberOfSides == 3:
        print('triangle')
    elif numberOfSides == 4:
        print('square')
    elif numberOfSides == 5:
        print('pentagon')
    elif numberOfSides == 6:
        print('hexagon')
    else:
        print('Can\'t tell what shape this is, too many sides!')

print("Testing shapeName(3): ", end="")
shapeName(3)
print()

print("Testing shapeName(4): ", end="")
shapeName(4)
print()

print("Testing shapeName(5): ", end="")
shapeName(5)
print()

print("Testing shapeName(10): ", end="")
shapeName(10)