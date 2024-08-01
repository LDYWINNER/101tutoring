# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def flower(fn):
    sl = sw = pl = pw = []
    for line in open(fn):
        temp = line.split(',')
        sl.append(temp[0])
        sw.append(temp[1])
        pl.append(temp[2])
        pw.append(temp[3])

        total1 = total2 = total3 = total4 = 0
        res1 = res2 = res3 = res4 = 0
        for k in range(5, len(sl)):
            total1 += float(sl[k])
            res1 = total1 / len(sl)
        for a in range(5, len(sw)):
            total2 += float(sw[a])
            res2 = total2 / len(sw)
        for b in range(5, len(pl)):
            total3 += float(pl[b])
            res3 = total3 / len(pl)
        for c in range(5, len(pw)):
            total4 += float(pw[c])
            res4 = total4 / len(pw)

    print('Class ' + temp[4].strip('\n') + '\n', end='')
    print('Average sepallength: ', res1, '\n', end='')
    print('Average sepalwidth: ', res2, '\n', end='')
    print('Average petallength: ', res3, '\n', end='')
    print('Average petalwidth: ', res4, '\n', end='')


print(flower('irisdata.txt'))


