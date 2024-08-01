
# A
def gcd(m, n):
    if m == n:
        return n
    elif m < n:
        return gcd(m, n-m)
    elif m > n:
        return gcd(m-n, n)

print(gcd(48, 36))

# B
def find_max(nums):
    if len(nums) == 1:
        return nums[0]
    elif nums[1] > nums[0]:
        return find_max(nums[1:])
    elif nums[1] < nums[0]:
        return find_max([nums[0]] + nums[2:])


print(find_max([1, 7, 4, 5])) # returns 7
print(find_max ([1, 7, 4, 5, 9, 2])) # returns 9

# C
def zip(u, v):
    if len(u) == 1 and len(v) == 1:
        return [u[0], v[0]]
    return [u[0], v[0]] + zip(u[1:], v[1:])

print(zip([1, 2, 3], [4, 5, 6]))

# D
def remove_number(x, nums):
    if len(nums) == 0:
        return []
    elif nums[0] == x:
        return remove_number(x, nums[1:])
    elif nums [0] != x:
        return [nums[0]] + remove_number(x, nums[1:])

print(remove_number(5, [1, 2, 3, 4, 5, 6, 5, 2, 1]))

# E
def removeLetter(string, letter):
    if len(string) == 0:
        return ''
    elif string[0] == letter:
        return removeLetter(string[1:], letter)
    elif string[0] != letter:
        return string[0] + removeLetter(string[1:], letter)

print(removeLetter("test string", "t"))
print(removeLetter("mississipi", "i"))
print(removeLetter("To be or not to be is a question.", "t") )