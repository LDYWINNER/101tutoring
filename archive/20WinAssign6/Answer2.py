
temp = {'Iris-setosa':[0, 0, 0, 0], 'Iris-versicolor': [0, 0, 0, 0], 'Iris-virginica':[0, 0, 0, 0]}
setosa = 0
versicolor = 0
virginica = 0

for line in open('irisdata.txt'):
    temp2 = line.split(',')
    #print(temp2)

    if temp2[4] == 'Iris-setosa\n':
        temp['Iris-setosa'][0] += (float(temp2[0]))
        temp['Iris-setosa'][1] += (float(temp2[1]))
        temp['Iris-setosa'][2] += (float(temp2[2]))
        temp['Iris-setosa'][3] += (float(temp2[3]))
        setosa += 1

    elif temp2[4] == 'Iris-versicolor\n':
        temp['Iris-versicolor'][0] += (float(temp2[0]))
        temp['Iris-versicolor'][1] += (float(temp2[1]))
        temp['Iris-versicolor'][2] += (float(temp2[2]))
        temp['Iris-versicolor'][3] += (float(temp2[3]))
        versicolor += 1

    elif temp2[4] == 'Iris-virginica\n':
        temp['Iris-virginica'][0] += float(temp2[0])
        temp['Iris-virginica'][1] += float(temp2[1])
        temp['Iris-virginica'][2] += float(temp2[2])
        temp['Iris-virginica'][3] += float(temp2[3])
        virginica += 1

#print(temp)
print('Class Iris-setosa:')
print('Average sepallength:', round(temp['Iris-setosa'][0] / setosa, 3))
print('Average sepalwidth:', round(temp['Iris-setosa'][1] / setosa, 3))
print('Average petallength:', round(temp['Iris-setosa'][2] / setosa, 3))
print('Average petalwidth:', round(temp['Iris-setosa'][3] / setosa, 3))
print()
print('Class Iris-versicolor:')
print('Average sepallength:', round(temp['Iris-versicolor'][0] / versicolor, 3))
print('Average sepalwidth:', round(temp['Iris-versicolor'][1] / versicolor, 3))
print('Average petallength:', round(temp['Iris-versicolor'][2] / versicolor, 3))
print('Average petalwidth:', round(temp['Iris-versicolor'][3] / versicolor, 3))
print()
print('Class Iris-virginica:')
print('Average sepallength:', round(temp['Iris-virginica'][0] / virginica, 3))
print('Average sepalwidth:', round(temp['Iris-virginica'][1] / virginica, 3))
print('Average petallength:', round(temp['Iris-virginica'][2] / virginica, 3))
print('Average petalwidth:', round(temp['Iris-virginica'][3] / virginica, 3))