# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

from string import punctuation

def tokenize(s):
    a = []
    for x in s.split():
        a.append(x.strip(punctuation).lower())
    return a

def Total_Words(fn):
    num = 0
    for line in open(fn):
        for word in tokenize(line):
            if word != '':
                num += 1
    return num

def get_average_word_length(fn):
    words = []
    length = 0
    for line in open(fn):
        words += tokenize(line)
    for word in words:
        if word != '':
            length += len(word)
    return (length / Total_Words(fn))

def get_number_of_different_words(fn):
    words = {}
    for line in open(fn):
        for word in (tokenize(line)):
            if word != '':
                words.setdefault(word, 0)
                words[word] += 1
    return len(words.keys())


def get_number_of_unique_words(fn):
    words = {}
    num = 0
    for line in open(fn):
        for word in (tokenize(line)):
            if word != '':
                words.setdefault(word, 0)
                words[word] += 1
    for w in words:
        if words[w] == 1:
            num += 1
    return num

def isort(a):
    for i in range(1, len(a)):
        move_left(a, i)

def move_left(a, j):
    x = a.pop(j)
    while j > 0 and a[j - 1] > x:
        j -= 1
    a.insert(j, x)

def get_most_frequent_words(fn):
    words = {}
    for line in open(fn):
        for word in (tokenize(line)):
            if word != '' and len(word) >= 5:
                words.setdefault(word, 0)
                words[word] += 1
    w = list(words.keys())
    n = list(words.values())
    isort(n)
    print(words)


def text_features(fn):
    print("Total Words ", Total_Words(fn), '\n', end='')
    print("Average Word Length ", '{:.2f}'.format(get_average_word_length(fn)), '\n', end='')
    print("Number of Different Words ", get_number_of_different_words(fn), '\n', end='')
    print("Number of Words Used Once ", get_number_of_unique_words(fn), '\n', end='')
    print("Type-Token Radio ", '{:.4f}'.format(get_number_of_different_words(fn) / Total_Words(fn)), '\n', end='')
    print("Hapax Legomena Ratio ", '{:.4f}'.format(get_number_of_unique_words(fn) / Total_Words(fn)), '\n', end='')
    print()
    print("Most Frequent Words (word, count): ", '\n', end='')
    print(get_most_frequent_words(fn))

text_features('file.txt')
print()
text_features('mystery1.txt')
print()
text_features('mystery2.txt')

