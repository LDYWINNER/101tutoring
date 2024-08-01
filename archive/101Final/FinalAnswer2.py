# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def printing(integer):
    if integer % 15 == 0:
        print("Multiple of 5", "Multiple of 3")
    elif integer % 5 == 0:
        print("Multiple of 5")
    elif integer % 3 == 0:
        print("Multiple of 3")
    else:
        print("Not a multiple of 5 or 3")

# Test
#printing(45)
#printing(10)
#printing(9)
#printing(7)

