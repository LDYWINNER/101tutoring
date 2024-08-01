# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def replaceMult3(nums, newNumber):
    replaceMult3_helper(nums, newNumber, 0)

def replaceMult3_helper(nums, newNumber, i):
    if i == len(nums):
        print(nums)
        return
    if nums[i] % 3 == 0:
        nums[i] = newNumber
    replaceMult3_helper(nums, newNumber, i + 1)


# Test
result = replaceMult3([2,3,5,7,9], 15)
print(result)