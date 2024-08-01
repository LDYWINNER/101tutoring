
def largestBelowValue(numbers, value):
    result = []
    for number in numbers:
        if number < value:
            result.append(number)
    if len(result) == 0:
        return
    return biggest(result)

def biggest(nums):
    final = nums[0]
    for num in nums:
        if num > final:
            final = num
    return final


print(largestBelowValue([31, 5, 71, 53, 40, 17], 40))
print(largestBelowValue([31, 5, 71, 53, 40, 17], 41))
print(largestBelowValue([31, 5, 71, 53, 40, 17], 2))
