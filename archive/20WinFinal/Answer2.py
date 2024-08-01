
num = int(input('Enter a integer: '))

if num % 3 == 0 and num % 5 == 0:
    print('Multiple of 5', 'Multiple of 3')
elif num % 3 == 0:
    print('Multiple of 3')
elif num % 5 == 0:
    print('Multiple of 5')
else:
    print('Not a multiple of 5 or 3')