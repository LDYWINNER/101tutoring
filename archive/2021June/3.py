
def modifyFile(file):
    for line in open(file):
        temp = line.split(" ")
        a = ""
        a += (line.strip('\n'))
        a += (" = ")
        temp1 = (temp[2]).strip('\n')

        if temp[1] == '+':
            a += str(int(temp[0]) + int(temp1))
        elif temp[1] == '*':
            a += str(int(temp[0]) * int(temp1))
        elif temp[1] == '-':
            a += str(int(temp[0]) - int(temp1))

        print(a)



modifyFile('input.txt')