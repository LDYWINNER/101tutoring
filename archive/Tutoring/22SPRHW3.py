# Name:
# SBUID:
# Remove the ellipses (...) when writing your solutions.
# ---------------------------- Q1 ---------------------------------------
def reverse_print(lst):
    for i in range(len(lst), 0, -1):
        print(lst[i - 1])

# ---------------------------- Q2 ---------------------------------------
def cross_sum(l1, l2):
    res = []
    for num1 in l1:
        for num2 in l2:
            res.append(num1 + num2)
    print(res)

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.
list = [5, 2, -1, 100]
reverse_print(list) # Should print out 100, -1, 2, 5 (vertical printout allowed)

lst2 = [1, 2, 3]
cross_sum(lst, lst2) # Should print out 6, 7, 8, 3, 4, 6, 0, 1, 2, 101, 102, 103 (vertical allowed)
