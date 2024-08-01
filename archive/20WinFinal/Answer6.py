
def modifyString(string):
    result = ''
    temp = {}
    for letter in string:
        temp.setdefault(letter, 0)
        temp[letter] += 1
        result += letter * temp[letter]

    print(result)



modifyString('ohoh')
modifyString('repetitive')