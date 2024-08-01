
password = 'secret'
userInput = ''
while userInput != password:
    print('What is the password?')
    userInput = input()
print('Yes, the password is ' + password + '. You may enter.')

# Random
from random import *
print(random())

from random import *
print(randint(1, 100))

from random import *
x = randint(1, 100)
print(x)

from random import *
print(uniform(1, 10))

items = [1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print(items)

from random import *
items = [1,2,3,4,5,6,7,8,9,10]
x = sample(items, 1)
print(x)
y = sample(items, 4)
print(y)

from random import *
items = ['Alissa','Alice','Marco','Melissa','Sandra','Steve']
x = sample(items, 1)
print(x)
y = sample(items, 4)
print(y)

# Guess.py
import random
number = random.randint(1, 5)
number_of_guesses = 0
while number_of_guesses < 5:
    print('Guess a number between 1 and 5:')
    guess = input()
    guess = int(guess)
    number_of_guesses += 1
    if guess == number:
        break

# randomones.py
import random
answer = random.randint(1, 6)
guessNum = 0
num1 = 0

while num1 < 2:
    generate = random.randint(1, 6)
    print(generate)
    guessNum += 1
    if generate == 1:
        num1 += 1
print(guessNum)
print()

# nestedloop.py
num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']
for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)
print()

# pyramid.py
for i in range(1, 6):
    for j in range(i):
        print('*', end=' ')
    print('\n', end='')
print()

# whilepyramid.py
i = 1
j = 0
while i < 6:
    while j < i:
        print('*', end=' ')
        j += 1
    print('\n', end='')
    i += 1
    j = 0

# factorial.py
def while_factorial(num):
    i = 1
    total = 1
    while i <= num:
        total *= i
        i += 1
    return total

def for_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

#
print(while_factorial(4))
print(for_factorial(5))