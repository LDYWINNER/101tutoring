
def loadAuthors(txt):
    result = {}
    for line in open(txt):
        temp = line.split('-')
        print(temp)
        author = temp[1].strip(" \n")

        if author not in result:
            result[author] = [temp[0]]
        elif author in result:
            result[author].append(temp[0])

    return result


print(loadAuthors('authors.txt'))
