

user = int(input('Enter an integer: '))

def evenOdd(num):
    if num == 0:
        return None
    elif num % 2 == 0:
        print('Is even')
    elif num % 2 == 1:
        print('Is odd')


(evenOdd(user))
