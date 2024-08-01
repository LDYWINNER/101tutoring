
def threeMostCommonCharacters(string):
    word = string.upper()
    #print(word)
    wordNum = []
    wordLetter = []
    for letter in word:
        if letter not in wordLetter:
            wordLetter.append(letter)
            wordNum.append(word.count(letter))
    #print(wordNum)
    #print(wordLetter)

    wordNum.sort()
    #print(wordNum)

    temp = []
    for num in range(len(wordNum)):
        tempNum = wordNum.pop()
        for letter in wordLetter:
            if word.count(letter) == tempNum and letter not in temp:
                temp.append(letter)
    #print(temp)

    print(temp[0]+':'+str(word.count(temp[0]))+',', temp[1]+':'+str(word.count(temp[1]))+',',
          temp[2]+':'+str(word.count(temp[2]))+',', temp[3]+':'+str(word.count(temp[3])))


threeMostCommonCharacters('Hyundaimotorcompany')
print()
threeMostCommonCharacters('Mississipi')
print()
threeMostCommonCharacters('Daimlerchrysler')