# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def processFile(fn):
    final = {}
    for line in open(fn):
        final[int(line[0])] = line[1:]
    #print(final)
    for x in range(1, 6):
        print(final[x].strip('\n'))


processFile('input.txt')
