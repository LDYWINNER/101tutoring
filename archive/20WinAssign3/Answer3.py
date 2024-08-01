
startPoint = int(input('Enter initial odometer reading: '))
distanceTemp = 0
fuelTemp = 0
temp3 = []
temp3.append(startPoint)
i = -1
while True:
    temp = input('Enter leg info (odometer reading, fuel used) : ')
    if temp == '':
        break

    else:
        midPoint = int(temp.split()[0])
        fuel = int(temp.split()[1])
        distanceTemp = midPoint
        temp3.append(midPoint)
        fuelTemp += fuel
        i += 1
        temp2 = round(((temp3[i + 1] - (temp3[i])) / fuel), 1)
        print(temp2, 'km per liter')


traveled = distanceTemp - startPoint
result = round(traveled / fuelTemp, 1)
print('Total distance traveled =', traveled, 'km. Total fuel used =', fuelTemp,
      'liters.\n' + 'Fuel Efficiency =', result, 'km per liter.')