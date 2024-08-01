
def countList(intList):
    temp = {}
    for int in intList:
        if int not in temp:
            temp[int] = 0

        if int in temp:
            temp[int] += 1



    for a in temp:
        print(str(a) + " count: " + str(temp[a]))


countList([4, 7, 4])
print()
countList([5,8,3,5,10,3,5,9])