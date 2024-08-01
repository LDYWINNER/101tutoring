
def loadSongs(txt):
    result = {}
    for line in open(txt):
        temp = line.split(':')
        #print(temp)
        if temp[1].strip(' \n') not in result:
            result[temp[1].strip(' \n')] = [temp[0]]
        elif temp[1].strip(' \n') in result:
            result[temp[1].strip(' \n')].append(temp[0])
    return result
    #print(result)

print(loadSongs('songs.txt'))
