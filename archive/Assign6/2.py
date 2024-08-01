
def flower(fn):
    ssl = ssw = spl = spw = []
    vesl = vesw = vepl = vepw = []
    visl = visw = vipl = vipw = []
    for line in open(fn):
        temp = line.split(',')
        #print(temp)
        if temp[4].strip('\n') == 'Iris-setosa':
            ssl.append(temp[0])
            ssw.append(temp[1])
            spl.append(temp[2])
            spw.append(temp[3])

    total1 = total2 = total3 = total4 = 0
    res1 = res2 = res3 = res4 = 0

    for k in range(5, len(ssl)):
        total1 += float(ssl[k])
        res1 = total1 / (len(ssl) + 1)
    for a in range(5, len(ssw)):
        total2 += float(ssw[a])
        res2 = total2 / (len(ssw) + 1)
    for b in range(5, len(spl)):
        total3 += float(spl[b])
        res3 = total3 / (len(spl) + 1)
    for c in range(5, len(spw)):
        total4 += float(spw[c])
        res4 = total4 / (len(spw) + 1)

    print('Class ', 'Iris-setosa: ', '\n', end='')
    print('Average sepallength: ', res1, '\n', end='')
    print('Average sepalwidth: ', res2, '\n', end='')
    print('Average petallength: ', res3, '\n', end='')
    print('Average petalwidth: ', res4, '\n', end='')


print(flower('irisdata.txt'))