from random import *

answer = ['House', 'Cat', 'Dog', 'Sofa', 'Desk', 'Chair', 'Tissue', 'Book', 'Pen', 'Ink', 'Note', 'Bible']

randomAnswer = sample(answer, 1)

print("Welcome to the guessing game. You have 6 attempts to guess the letters in ", end='')
underBar = ('_') * len(randomAnswer[0])
print(underBar)
print(randomAnswer)
attempts = 0
printAttempts = 6
usedInput = []
while attempts <= 6:
    Bar = list(underBar)
    while '_' in Bar:
        Input = input('Enter a letter to guess: ')
        userInput = str(Input)
        usedInput.append(userInput[0])
        i = []
        if userInput[0] in randomAnswer[0]:
            for x in range(len(randomAnswer[0])):
                if userInput[0] == randomAnswer[0][x]:
                    i.append(x)
            for k in i:
                Bar[k] = userInput[0]
            print('\'', userInput[0], '\'', 'is in the word','\n', end='')
            for a in range(len(Bar)):
                print(str(Bar[a]), end='')
            print('   Number of attempts left: ', printAttempts)
            if '_' not in Bar:
                print("You won! The word is", '\'', randomAnswer[0], '\'')

        if usedInput.count(userInput[0]) >= 2:
            attempts -= 1
            printAttempts += 1
            print('You\'ve already guessed', userInput[0])

        if userInput[0] not in randomAnswer[0]:
            printAttempts -= 1
            attempts += 1
            print('There is no', '\'', userInput[0], '\'', 'in the word')
            print()
            print('Number of attempts left: ', printAttempts)

    break
