
def processFile(file):
    for i in range(1, 6):
        for line in open(file):
            if int(line[0]) == i:
                print(line.strip('0123456789\t\n '))
processFile('input.txt')