
def Solution(array):
    gaps = []
    i = len(array) - 1
    while i > 0:
        for x in range(i - 1, -1, -1):
            gap = array[i] - array[x]
            if gap > 0:
                gaps.append(gap)
        i -= 1
    return biggest(gaps)

def biggest(nums):
    big = nums[0]
    for num in nums:
        if num > big:
            big = num
    return big


print(Solution([23171, 21011, 21123, 21366, 21013, 21367])) #356