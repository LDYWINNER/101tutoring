def isort(a):
    for i in range(1, len(a)):
        move_left(a, i)

def move_left(a, j):
    x = a.pop(j)
    while j > 0 and a[j - 1] > x:
        j -= 1
    a.insert(j, x)

def threeMostCommonCharacters(string):
    word = list(string.upper())
    num = []
    finalList = []
    for k in range(len(word)):
        if word[k] not in finalList:
            finalList.append(word[k])
            letterCount = int(word.count(word[k]))
            finalList.append(letterCount)
            num.append(letterCount)
    #print(finalList)

    isort(num)
    num.reverse()
    #print(num)
    #print(num[0], num[1], num[2])

    i = 0
    while i < 3:
        for y in range(1, len(finalList), 2):
            if finalList[y] == num[i]:
                letter = finalList.pop(y - 1)
                number = finalList.pop(y - 1)
                print(str(letter) + ':' + str(number), end=', ')
                i += 1
                break
    print()

threeMostCommonCharacters("Google")
threeMostCommonCharacters("Mississipi")
threeMostCommonCharacters("Daimlerchrysler")
threeMostCommonCharacters("Management")