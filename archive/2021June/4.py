
def reverseAndPrint(nums, minNumber):
    i = len(nums)
    if i == 0:
        return
    else:
        i -= 1
        if nums[i] > minNumber:
            print(nums[i])
            return reverseAndPrint(nums[:-1], minNumber)
        else:
            return reverseAndPrint(nums[:-1], minNumber)




reverseAndPrint([8, 6, 4, 9], 5)