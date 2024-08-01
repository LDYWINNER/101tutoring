
def replaceMult3(nums, newNumber):
    if nums == []:
        return []
    elif nums[0] % 3 == 0:
        return [newNumber] + replaceMult3(nums[1:], newNumber)
    else:
        return [nums[0]] + replaceMult3(nums[1:], newNumber)


result = replaceMult3([2,3,5,7,9], 15)
print(result)