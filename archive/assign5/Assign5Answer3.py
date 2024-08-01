# CSE 101 DongYoon Lee
# Email: dongyoon.lee.1@stonybrook.edu

# If m = n, it returns n
# If m < n, it returns gcd(m, n-m)
# If m > n, it returns gcd(m-n, n)
#
def gcd(m, n):
    if m == n:
        return n
    elif m < n:
        return gcd(m, n-m)
    elif m > n:
        return gcd(m-n, n)

#Own test case
print(gcd(30, 36))
print()

# find_max([1, 7, 4, 5] returns 7
# find_ max ([1, 7, 4, 5, 9, 2] returns 9
#
def find_max(u):
    if len(u) == 1:
        return u[0]
    else:
        if u[0] < u[1]:
            return find_max(u[1:])
        else:
            return find_max([u[0]] +u[2:])

print(find_max([1, 7, 4, 5, 9, 2]))
#Own test case
print(find_max([9, 3, 5, 21, 11, 46]))
print()

# zip([1, 2, 3], [4, 5, 6]) returns [1, 4, 2, 5, 3, 6]
#
def zip(u, v):
    if len(u) == 1 and len(v) == 1:
        return [u[0], v[0]]
    elif len(u) == len(v):
        return [u[0], v[0]] + zip(u[1:], v[1:])

print(zip([1, 2, 3], [4, 5, 6]))
#Own test case
print(zip([3, 4, 6, 2, 6], [7, 4, 2, 7, 2]))
print()

# remove_number(5, [1, 2, 3, 4, 5, 6, 5, 2, 1]) returns [1, 2, 3, 4, 6, 2, 1]
#
def remove_number(x, nums):
    if x not in nums:
        return nums
    elif nums[0] == x and nums[-1] == x:
        return nums[1:-1]
    elif nums[0] != x and nums[-1] == x:
        return [nums[0]] + remove_number(x, nums[1:-1])
    elif nums[0] == x and nums[-1] != x:
        return remove_number(x, nums[1:-1]) + [nums[-1]]
    elif nums[0] != x and nums[-1] != x:
        return [nums[0]] + remove_number(x, nums[1:-1]) + [nums[-1]]

print(remove_number(5, [1, 2, 3, 4, 5, 6, 5, 2, 1]))
#Own test case
print(remove_number(2, [5, 6, 2, 1, 6, 7, 8, 2]))
print()

def removeLetter(string, letter):
    if str(letter) not in string:
        return string
    elif string[0] == str(letter) and string[-1] == str(letter):
        return string[1:-1]
    elif string[0] != str(letter) and string[-1] == str(letter):
        return string[0] + removeLetter(string[1:-1], letter)
    elif string[0] == str(letter) and string[-1] != str(letter):
        return removeLetter(string[1:-1], letter) + string[-1]
    elif string[0] != str(letter) and string[-1] != str(letter):
        return string[0] + removeLetter(string[1:-1], letter) + string[-1]

print(removeLetter("test string", "t"))
print(removeLetter("mississipi", "i"))
print(removeLetter("To be or not to be is a question.", "t"))
#Own test case
print(removeLetter("hand phone designer", "e"))
