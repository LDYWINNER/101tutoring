
date = input('Enter date: ')

if int(date[:2]) in [1, 3, 5, 7, 8, 10, 12]:
    if int(date[3:5]) > 31:
        print('\'' + date + '\'', 'is an invalid date')
    else:
        print('\'' + date + '\'', 'is a valid date')
elif int(date[:2]) in [4, 6, 9, 11]:
    if int(date[3:5]) > 30:
        print('\'' + date + '\'', 'is an invalid date')
    else:
        print('\'' + date + '\'', 'is a valid date')

elif int(date[:2]) == 2:
    if int(date[6:]) % 400 == 0:
        if int(date[3:5]) > 29:
            print('\'' + date + '\'', 'is an invalid date')
        else:
            print('\'' + date + '\'', 'is a valid date')
    elif int(date[6:]) % 100 == 0:
        if int(date[3:5]) > 28:
            print('\'' + date + '\'', 'is an invalid date')
        else:
            print('\'' + date + '\'', 'is a valid date')
    elif int(date[6:]) % 4 == 0:
        if int(date[3:5]) > 29:
            print('\'' + date + '\'', 'is an invalid date')
        else:
            print('\'' + date + '\'', 'is a valid date')

    else:
        if int(date[3:5]) > 28:
            print('\'' + date + '\'', 'is an invalid date')
        else:
            print('\'' + date + '\'', 'is a valid date')

