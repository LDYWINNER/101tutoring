
def processString(string):
    result = string.split('.')
    #print(result)
    letterCount = 0
    final = 0
    for sentence in result:
        sentence = sentence.lstrip(' ')
        words = sentence.split(' ')
        #print(words)
        totalWordCount = len(words)
        for word in words:
            letterCount += (len(word))
            final = letterCount / totalWordCount
        letterCount = 0

        print('{:.1f}'.format(final), end=' ')



# This should print 4.5 3.0
processString("An example. Two")

print()

# This should print 4.4 5.3 4.5
processString("This is the first sentence. The second sentence starts after the period. Then a final sentence")