# Recursive Examples

# Sum of fractions
def sum_fracs(n):
    if n == 1:
        return 1
    return 1 / n + sum_fracs(n - 1)

# Sum a list
def rsum(nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + rsum(nums[1:])

# Exponentiation #
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        temp = power(base, exponent // 2)
        return temp * temp
    else:
        temp = power(base, exponent // 2)
        return temp * temp * base

# Reverse a string
def rev(s):
    if len(s) == 1:
        return s
    return s[-1] + rev(s[:-1])

# Count occurrences
def count_occurrences(string, ch):
    if len(string) == 0:
        return 0
    if string[0] == ch:
        return count_occurrences(string[1:], ch) + 1
    return count_occurrences(string[1:], ch)

# Find Palindromes
# Palindromes : A word or phrase that can be read backwards and forwards
# Ex) radar, toot, dad, I
# Make 'is_palindrome' which returns True if its argument is a palindrome and False if not

def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

# Replace multiples of 5
# replace_mult5 : Make a function named '~' that takes a list of numbers and replaces all multiples of 5 with a substitute number
# helper func : replace_mult5_helper
# -> take the same two arguments as replace_mult5, plus a third argument that racks what part of the list we have already processed

def replace_mult5(nums, sub):
    replace_mult5_helper(nums, sub, 0)

def replace_mult5_helper(nums, sub, i):
    if i == len(nums):
        return
    if nums[i] % 5 == 0:
        nums[i] = sub
    replace_mult5_helper(nums, sub, i + 1)

#Substitute form
def replace_mult5_helper2(nums, sub, i):
    for i in range(len(nums)):
        if nums[i] % 5 == 0:
            nums[i] = sub

# Find index of character
# Make our own 'index' function
# index function : built-in string method that returns the index of the first occurrence of a character or substring in a string

def rindex(string, target):
    return rindex_helper(string, target, 0)

def rindex_helper(string, target, i):
    if i >= len(string):
        return None
    elif string[i] == target:
        return i
    else:
        return rindex_helper(string, target, i + 1)

# Lab 7 Review
def is_even(n):
    return n % 2 == 0

# Computes n!
# precondition : n >= 0
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

# Computes 0 + 1 + 2 + 3 + ... + n
# precondition : n >= 0
def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)

# Computes 0 + 2 + 4 + ... + n
# precondition : n >= 0
def sum_even_to(n):
    if n == 0:
        return 0
    elif is_even(n):
        return n + sum_even_to(n - 2)
    else:
        return (n - 1) + sum_even_to(n - 3)

# Concatenates the numbers in forward order to form a string
# if n = 9, returns '0123456789'
# if n = 13, returns '012345678910111213'
# precondition : n >= 0
def concat_to(n):
    if n == 0:
        return '0'
    else:
        return concat_to(n - 1) + str(n)

# Concatenates the numbers in reverse order to form a string
# if n = 9, returns '9876543210'
# if n = 13, returns '131211109876543210'
# precondition : n >= 0
def concat_reverse_to(n):
    if n == 0:
        return '0'
    else:
        return str(n) + concat_reverse_to(n - 1)

# Dealing with lists
# Computes the sum of all the elements in the list u
def sum(u):
    if u == []:
        return 0
    else:
        return u[0] + sum(u[1:])

# Computes the sum of all the even elements in the list u
def sum_evens(u):
    if u == []:
        return 0
    elif is_even(u[0]):
        return u[0] + sum_evens(u[1:])
    else:
        return sum_evens(u[1:])

# Finds and returns only the even elements in the list u
def find_evens(u):
    if u == []:
        return []
    elif is_even(u[0]):
        return [u[0]] + find_evens(u[1:])
    else:
        return find_evens(u[1:])



