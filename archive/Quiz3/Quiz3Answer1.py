# CSE 101 DongYoon Lee
# Email: dongyoon.lee.1@stonybrook.edu

def output(number):
    if number % 3 == 0 and number % 4 == 0:
        print("\"Multiple of 3 and 4\"")
    elif number % 4 == 0:
        print("\"Multiple of 4\"")
    elif number % 3 == 0:
        print("\"Multiple of 3\"")
    else:
        print("\"Not a multiple of 3 or 4\"")


output(12)

output(8)

output(5)