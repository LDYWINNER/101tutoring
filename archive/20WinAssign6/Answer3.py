
from string import punctuation

def text_features(file):
    wordNum = {}
    wordCount = 0
    wordLengthCount = 0
    for line in open(file):
        words = line.split(' ')
        for word in words:
            temp = word.strip('\n\t ')
            temp = temp.strip(punctuation).lower()
            if temp != '':
                wordNum.setdefault(temp, 0)
                wordNum[temp] += 1
                wordCount += 1
                wordLengthCount += len(temp)
    #print(wordNum)

    words = list(wordNum.keys())
    words1 = list(wordNum.keys())
    letterCount = list(wordNum.values())
    #print(words)
    #print(letterCount)

    firstWord = 0
    for word in wordNum:
        if wordNum[word] == 1:
            firstWord += 1

    result = []
    temp3 = sorted(letterCount)
    while temp3:
        temp = temp3.pop()
        for word in words1:
            if wordNum[word] == temp and len(word) >= 5:
                temp2 = words1.pop(words1.index(word))
                result.append(temp2)
                result.append(temp)
    #print(result)



    totalWords = sum(letterCount)
    # Result
    print('Total Words', totalWords)
    print('Average Word Length', round(wordLengthCount / wordCount, 2))
    print('Number of Different Words', len(words))
    print('Number of Words Used Once', firstWord)
    print('Type-Token Ratio', round(len(words) / wordCount, 4))
    print('Hapax Legomena Ratio', round(firstWord / wordCount, 4))
    print('Most Frequent Words (word, count):')
    try:
        for i in range(0, 20, 2):
            print(result[i], str(result[i + 1]), end=', ')
    except:
        pass

def sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

text_features('file.txt')
print('\n')
text_features('mystery1.txt')
print('\n')
text_features('mystery2.txt')