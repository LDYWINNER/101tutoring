
def find_minimum(nums):
    result = nums[0]
    for num in nums:
        if num < result:
            result = num
    return result

print(find_minimum([5, 7, 3, 10, 15, 1, 5]))
print(find_minimum([5, -4, 3, 10, 0, 5]))