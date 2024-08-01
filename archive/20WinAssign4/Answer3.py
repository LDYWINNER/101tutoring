def biggest(nums):
    big = nums[0]
    for num in nums:
        if num > big:
            big = num
    return big

def threeMostCommonCharacters(string):
    temp = {}
    result = {}
    letters = string.upper()
    for letter in letters:
        temp.setdefault(letter, 0)
        temp[letter] += 1
    #print(temp)
    letterNum = list(temp.values())
    #print(letterNum)

    numList = []
    a = len(letterNum)
    while len(numList) != a:
        for num in letterNum:
            if num == biggest(letterNum):
                temp = letterNum.pop(letterNum.index(num))
                numList.append(temp)
    #print(numList)


    for num in numList:
        for letter in letters:
            if letters.count(letter) == num:
                result[letter] = str(num)
    #print(result)

    final = list(result.items())
    #print(final)

    for i in range(0, 3):
        #print(final[i])
        print(':'.join(final[i]), end=' ')



threeMostCommonCharacters('Google')
print()
threeMostCommonCharacters('Mississipi')
print()
threeMostCommonCharacters('Daimlerchrysler')