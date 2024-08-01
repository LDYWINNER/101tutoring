# Write a function 'what_order(lst)' that receives a non-empty list of numbers and returns
# one of the following three integer values.
#
# Zero (0), when the list is sorted in ascending order
# One (1), when the list is sorted in descending order
# Two (2), when the list is not sorted
# Here are the rules:
#
# You may assume that the list will always have length at least two.
# You should only use a single loop (for or while).
# In addition to the code, provide a documentation that clearly describes your algorithm
# (description should not be too general or ambiguous).
# A sequence of same numbers is considered to be in ascending order.
# Here are some example input/outputs:
#
# Input: [5, 2, 1, 0],    Output: 1
# Input: [2, 3, 4, 19],  Output: 0
# Input: [0, 0, 0, 0],    Output: 0
# Input: [4, 3, 6, 2],    Output: 2

def what_order(lst):
    a = -1
    b = lst[0]

    for i in range(1, len(lst)):
        if a == 0 and lst[i] >= b or i == 1 and lst[i] >= b:            # if block: ascending order
            a = 0
            b = lst[i]
        elif a == 1 and lst[i] < b or i == 1 and lst[i] < b:
            a = 1
            b = lst[i]
        else:
            a = 2
            break
    return a

test1 = [5, 2, 1, 0]
test2 = [2, 3, 4, 19]
test3 = [0, 0, 0, 0]
test4 = [4, 3, 6, 2]

print(what_order(test1))
print(what_order(test2))
print(what_order(test3))
print(what_order(test4))

# Question 2
# You are given a number 'x' and a list of numbers 'lst' in descending order.
# Suppose you wish to insert 'x' into 'lst' so that the resulting list will remain in descending order.
# Describe your approach to achieve this.
# Note that I'm not asking you to write a code (although it's okay to provide one if you wish),
# but to write a plain English description

def find_location(lst, x):
    for i in range(len(lst)):
        if lst[i] <= x:
            lst.insert(i, x)
            return lst

temp = [10, 6, 3, 1]
temp_x = 5
print(find_location(temp, temp_x))
