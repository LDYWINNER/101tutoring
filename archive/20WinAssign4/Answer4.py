from random import shuffle

wordList = ['Box', 'Cat', 'Test', 'Game', 'Toilet', 'Pen', 'Card',
            'Note', 'Word', 'Can']

shuffle(wordList)
Answer = wordList[0]
underScoreWord = list('_' * len(Answer))
print('Welcome to the guessing game. You have 6 attempts to guess the letters in '
      + ''.join(underScoreWord))
#print(Answer)
guesses = []
temp = list(Answer)
attemptsLeft = 6
while '_' in underScoreWord:
    guess = input('Enter a letter to guess: ')
    if guess in Answer:
        attemptsLeft -= 1
        if guess in guesses:
            attemptsLeft += 1
            print('You\'ve already guessed ' + guess)
            print('Number of attempts left:', attemptsLeft)
        guesses.append(guess)
        for letter in Answer:
            if letter == guess:
                underScoreWord.pop(Answer.index(letter))
                underScoreWord.insert(Answer.index(letter), letter)
                print('\'' + guess + '\'' + ' is in the word')
                print(''.join(underScoreWord), 'Number of attempts left:', attemptsLeft)

        #print(temp)

    elif guess not in Answer:
        attemptsLeft -= 1
        print('There is no \'' + guess + '\' in the word')
        print('Number of attempts left:', attemptsLeft)

print('You won! The word is \'' + Answer + '\'')