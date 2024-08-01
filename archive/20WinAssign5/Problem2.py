
# Failed
def scrabble_sort(stringList):
    temp = {}
    result = []
    for string in stringList:
        temp[string] = len(string)
    print(temp)
    nums = list(temp.values())
    nums.sort()
    print(nums)

    for num in nums:
        for string in temp:
            if string in result:
                pass
            elif len(string) == num:
                result.append(string)
    #print(result)

    result.reverse()
    while result:
        temp1 = []
        temp = result.pop()
        for num in nums:
            if nums.count(num) > 1 and len(temp) == num:
                temp1.append(temp)
                temp1.sort()
                temp1.reverse()
        for word in temp1:
            result.append(word)

    print(result)



from PythonLabs.RecursionLab import *
a = RandomList(20, 'words')
#print(a)
scrabble_sort(a)
#print(a)
