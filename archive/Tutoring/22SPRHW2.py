# Name:
# SBUID:
# Remove the ellipses (...) when writing your solutions.
import math
# ---------------------------- Q1 ---------------------------------------
# TODO: Implement quad(a,b,c) that returns the solution in human-readable form.
#       Unlike the quiz, the square roots should be computed explicitly using
#       math.sqrt().
#       You MUST use a try-except block to handle imaginary units.
def quad(a, b, c):
    temp1 = -b
    temp2 = b ** 2 - 4 * a * c
    try:
        res = math.sqrt(temp2)
    except:
        res = "i*" + str(math.sqrt(-1 * temp2))
    final1 = str(temp1) + " + " + str(res) + " OVER " + str(2 * a)
    final2 = str(temp1) + " - " + str(res) + " OVER " + str(2 * a)
    return final1 + ", " + final2



# ---------------------------- Q2 ---------------------------------------
# TODO: Implement get_negatives() that returns the string containing all the
#       negative numbers in the list. The negative numbers should be separated
#       by commas. E.g., "-4, -5, -6, -7"
def get_negatives(lst):
    res = []
    for num in lst:
        if num < 0:
            res.append(num)
    if len(res) == 0:
        return ""
    else:
        result_string = ""
        for r in res:
            result_string += (str(r) + ", ")
        return result_string

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.
a = 1
b = 4
c = 5
print("Q1: " + quad(a, b, c)) # Should print out "Q1: -4+i*2 OVER 2, -4-i*2 OVER 2"

lst = [1, 2, 3, -4, -5, -6, -7]
print("Q2: " + get_negatives(lst)) # Should print out "Q2: -4, -5, -6, -7"
