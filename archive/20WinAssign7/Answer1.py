
wolfieNumDict = {'I': 1, 'IF': 3, 'F': 4, 'IE': 7, 'E': 8, 'ET': 24,
                  'T': 32, 'ES': 56, 'S': 64}
numWolfieDict = dict(zip(wolfieNumDict.values(), wolfieNumDict.keys()))

# Part 1
def arabic2wolfie(num):
    numList = list(numWolfieDict.keys())
    numList.reverse()
    #print(numList)

    temp = num
    finalNum = []
    finalStr = ''
    while temp > 0:
        for num in numList:
            if num <= temp:
                finalNum.append(num)
                temp -= num
                break
            if temp == 0:
                break

    for num in finalNum:
        num = int(num)
        finalStr += numWolfieDict[num]
    return finalStr

# Part 2
numList = list(wolfieNumDict.values())
#print(numList)
def wolfie2arabic(numerals):
    if len(numerals) == 1:
        return wolfieNumDict[numerals]
    elif numList.index(wolfieNumDict[numerals[0]]) < numList.index(wolfieNumDict[numerals[1]]):
        return int(wolfieNumDict[numerals[:2]]) + wolfie2arabic(numerals[2:])
    else:
        return int(wolfieNumDict[numerals[0]]) + wolfie2arabic(numerals[1:])


def main():

    # Part 1
    print("Testing Part 1")
    print('Testing arabic2wolfie() with num = 10: ' + str(arabic2wolfie(10)))
    print('Testing arabic2wolfie() with num = 14: ' + str(arabic2wolfie(14)))
    print('Testing arabic2wolfie() with num = 22: ' + str(arabic2wolfie(22)))
    print('Testing arabic2wolfie() with num = 28: ' + str(arabic2wolfie(28)))
    print('Testing arabic2wolfie() with num = 30: ' + str(arabic2wolfie(30)))
    print('Testing arabic2wolfie() with num = 54: ' + str(arabic2wolfie(54)))
    print()

    # Part 2
    print("Testing Part 2")
    print("Testing wolfie2arabic() with wolfie = 'EII': " + str(wolfie2arabic('EII')))
    print("Testing wolfie2arabic() with wolfie = 'EFII': " + str(wolfie2arabic('EFII')))
    print("Testing wolfie2arabic() with wolfie = 'EEFII': " + str(wolfie2arabic('EEFII')))
    print("Testing wolfie2arabic() with wolfie = 'ETF': " + str(wolfie2arabic('ETF')))
    print("Testing wolfie2arabic() with wolfie = 'ETFII': " + str(wolfie2arabic('ETFII')))
    print("Testing wolfie2arabic() with wolfie = 'TEEFII': " + str(wolfie2arabic('TEEFII')))
    print()


if __name__ == '__main__':
    main()