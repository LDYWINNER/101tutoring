# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def isort(a):
    for i in range(1, len(a)):
        move_left(a, i)

def move_left(a, j):
    x = a.pop(j)
    while j > 0 and a[j - 1] > x:
        j -= 1
    a.insert(j, x)

def threeMostCommonCharacters(string):
    count = {}
    word = string.upper()
    for i in range(len(word)):
        count.setdefault(word[i], 0)
        if word[i] in word:
            count[word[i]] += 1
    #print(count)
    num = list(count.values())
    words = list(count.keys())
    isort(num)
    num.reverse()
    #print(num)
    #print(words)
    k = 0
    l = []
    while k < 3:
        for x in range(len(words)):
            if count[words[x]] == num[k]:
                if words[x] not in l:
                    print(words[x], ':', num[k], ', ', end='')
                    k += 1
                    l.append(words[x])
                    break


(threeMostCommonCharacters("Google"))
print('\n', end='')
(threeMostCommonCharacters("Mississipi"))
print('\n', end='')
(threeMostCommonCharacters("Daimlerchrysler"))