user = float(input('Flying speed in miles per hour: '))

def seoulToLondon(num):
    result = 8850 / (1.609 / 60 * num)
    return result

a = seoulToLondon(user)
print('Time required to travel from Seoul to London:', '{:.2f}'.format(a), 'minutes')