
# augmented assignment
# sum += x (increment operator)

print(1, 2, 3)
# 1 2 3
print()

# Computer scientists usually begin at 0 instead of 1 when they start assigning labels to thigns

# a[i] : "a sub i"
# sub : subscript

# index method

vowels = ['a', 'e', 'i', 'o', 'u']

print(vowels.index('a'))
print(vowels.index('o'))
print()

# in operator (can be used as a Boolean operator to see if a string is contained\
# inside another one

print('e' in vowels)
print('x' in vowels)

# partial_total: computes the sum of elements in a list, but it uses only the values at the front of the list.

a = [3,4,3,2,1]

# partial_total(3,a) : 10 (3: the number of values to sum)

# range function : used to specify a set of index value
# range(i, j) : " the set of integers from i through j-1

def partial_total(n, a):
    sum = 0
    for i in range(0, n):
        sum += a[i]
    return sum

# i : index variable

# range expression doesn't need a list to be used
# any situation where we need a sequence of integers
# a good occasion to use a for loop with a range expression

from math import sqrt

for i in range(1,11,2):
    print(i, sqrt(i))

# 2 : step size : specifies the distance between successive values

# algorithm animation : help visualize the steps of a computation
# draw 2D pictures in a graphics window called a canvas

# row : 열, column : 행

# using class names a functions
# If we use these names as functions, Python will create an object of that type
# Functions that create objects of a specified class
# "Constructors"

print(str())
print(list())
print(list(range(0, 10)))
print(list(range(10)))

print(list(range(2, 99)))

# Place holder values : None
# None : a special Python object (a natural candidate for the two placeholder values)
# Usage: 1. To introduce a variable before we know what value we want to assign it.
# 2. in situations where we need space for something

worksheet = [None, None] + list(range(2, 100))
print(worksheet)

# + : concatenation

# del statement : removes numbers from the list

greeks = ['a','b','c','d','e']

del greeks[2]
print(greeks)
# ['a','b','d','e']

# sift function
def sift(k, a):
    "Remove multiples of k from list a"
    for i in range(2*k, len(a), k):
        a[i] = None

# k : the value of a newly discovered prime number
# a : reference to the main worksheet

# sieve : top level function
# : the function that can be called, either by a user in an interactive session or from another program, whenever a list of prime numbers is needed

from math import *
# ceil function : returns the smallest integer greater than x
# rounds up to the next whole number

# sieve function
def sieve(n):
    worksheet = [None, None] + list(range(2, n))
    for k in range(2, ceil(sqrt(n))):
        if worksheet[k] is not None:
            sift(k, worksheet)
    return non_nulls(worksheet)

def non_nulls(a):
    "Return a copy of list a with None objects removed"
    res = []
    for x in a:
        if x is not None:
            res.append(x)
    return res

# sys : a standard library : includes a variety of items used to connect a program to the operating system.
# argv : a list containing the collection of arguments that the user typed on the command line
# stands for "argument vector (=list)"

#from sys import argv

#def celsius(f):
    #"Convert temperature f to celsius"
    #return (f - 32) * 5 / 9

#if __name__ == "__main__":
    ##print(argv)
    #t = int(argv[1])
    #print(celsius(t))

# Reads an argument from the command line and passes it to the celsius function.
# if~ : if this file is being run as a command line program, execute the following statement.
# use this if statement when we want to turn a collection of functions into a command line application

# argv : a list of strings
# Even though we type a number on the command line, it is passed to Python as a string of digits.
# Use this if statement because it gives us a choice of running interactively or from the command line.

# When we want to load the file into an interactive session
# from celsius import *
# not being run from the command line
# Because the Boolean expression in if statement becomes False.
# Python will just load the function, but it won't call it yet.
# To convert temp, we just call the function interactively.

# Term Sum

# List : An ordered collection of objects
# Index : A number that specifies a location in a list, if a list has n items, index ranges from 0 to n - 1
# Iteration : A technique for solving a problem by repeating a set of steps
# for loop : A programming construct often used to apply an operation to each item in a collection
# top level function : A function that implements a complete solution to a problem
# helper function : A function designed to solve a small part of a large problem
# range : A built-in function in Python used to generate a sequence of values in a specified range
# ceil : A function from Python's math library that "rounds up" to the nearest integer
# None : A special object that means "no object," (1) used as a place-holder in lists or (2) for variables that will be given a value later

# Kuhn PPT

# Iteration : Code that repeats a list of steps

# In computer science, collections are made by defining a data structure (container) that includes references to objects
# Objects : "a piece of data" + include numbers, strings, dates, ...
# Container : An object that contains other objects

ages = [62, 31, 29, 38]
# Pythons creates an object to represent the list and associates the name 'ages' with the new object (list)

# Any kind of object can be stored in a list

# A list can also be made with no objects
# empty list is still a list
# usually created because the list is needed, but it will be filled later

# Do something with each item in a container
# = "step through" the container to do something to each object
# This type of operation is called 'iteration'

# For loop : the simplest way to "visit" every item in a list

cars = ['Kia', 'Honda', 'Toyota', 'Ford']
for car in cars:
    print(car + ' ' + str(len(car)))
    print(car, len(car)) # the same

# can only concatenate string to string

def sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Debugger in Python
# help trace the execution of a program
# usually used to help find bugs

# Index : used to refer to the numerical position of an element in a list

# Index method : indicates the position of an element in a list

scores = [32, 53, 92]
scores.index(92)

#scores.index(34)
# ValueError: 34 is not in list

print(83 in scores)
print()

vowels = ['a', 'e', 'i', 'o', 'u']
letter = 'e'
if letter in vowels:
    print('That letter is at index ' + str(vowels.index(letter)) + '.')
else:
    print('That letter is not in the list.')

# range(n) : "The sequence of integers starting from zero and ranging up to, but not including n."

print()

def partial_total(nums, k):
    total = 0
    for i in range(k):
        total += nums[i]
    return total

nums = list(range(10))
print(nums)

# class : what kind of data an object can store

# In general, if a class name is used as a function, Python will create an object of that class
# called "Constructor"
# they construct new objects
a = list()
b = str(50)
print(a)
print(b)
print()

# Cannot pass a floating-point value to range function

# floor function
# rounds a floating-point value down to the nearest integer

# += can also be used to concatenate one string to the end of another
# can also be used to append one list to another
alphabets = ['a', 'b']
alphabets += ['c', 'd', 'e']
print(alphabets)

# Abstraction : save and reuse the defined function
# no need to worry about the details of the function

# lower() : method for strings
# makes a copy of a given string and changes all the uppercase letters to lowercase

# upper() : the opposite of lower()

# strings are immutable / unchangeable objects
# To convert a string into lowercase, we must make a lowercase copy of it and replace the original string with the new one

def count_vowels(word):
    for letter in word.lower():
        print(letter)

(count_vowels('apple'))

# In python, a list can contain objects of any type
# A list is an object
# A list can contain other lists

print('Hi' * 3)
# HiHiHi
print([0] * 3)
# [0, 0, 0]
# The * notation with strings and lists is essentially a form of concatenation

print()

print(list(range(10, -1, -1)))
# [10, 9, ..., 0]
# -1 is non-inclusive, so until 0

# string slicing
number = "123-456-7890"
print(number[0:3])
# 123
print(number[0:5])
# 123-4
print(number[4:6])
# 45
print(number[4:7])
#456

# Assign 2 Revision

def seriesSum(n, totalTerms):
    sum = 0
    nextNum = n
    for i in range(0, totalTerms):
        sum += nextNum
        nextNum = (nextNum * 10) + n
    return sum

def printZ(n):
    result_str = ''
    for row in range(0, n):
        for column in range(0, n):
            if (((row == 0 or row == n - 1) and column >= 0 and column <= n - 1) or row + column == n - 1):
                result_str = result_str + '*'
            else:
                result_str = result_str + ' '
        result_str = result_str + '\n'
    print(result_str)

printZ(8)
printZ(4)

def isNumberPrime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
        return True

# While loop

# A while loop implements the repeated execution of code based on a given Boolean Condition

# The code that is in a while block will execute as long as the while statement evaluates to True

# while : repeats indefinitely until it evaluates to False

# While loops are especially useful if you don't know how many times you will need to repeat something when you wrtie the code

#password = 'secret'
#userInput = ''
#while userInput != password:
#    print('What is the password?')
#    userInput = input()
#print('Yes, the password is ' + password + '. You may enter')

# using random module
from random import *
# * means everything
# all classes and functions

# random() : generates a random floating point number between 0 and 1
print(random())
# These numbers are called "pseudorandom"
# means "not truly random"

print(randint(1, 100))
# generates and prints a random integer between 1 and 100 (not 99)
# Or
x = randint(1, 100)
print(x)

# uniform() : a function that generates a random floating point number between a and b
# print(uniform(a, b))
print(uniform(1, 100))
print()

from random import *
items = [1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print(items)
# mixing up a list, like you are shuffling a deck of cards
print()

from random import *
items = [1,2,3,4,5,6,7,8,9,10]
x = sample(items, 1)
print(x[0])
y = sample(items, 4)
print(y)
# Can use the random functions with lists of strings, too

# Break Statement : alter the flow of a normal loop
# Terminates the loop in which you call break
# Causes the program to flow immediately to the next statement after the body of the loop
# If you call 'break' inside a nested loop, break will stop the innermost loop, but keep executing the outer loop

print()

#import random
#number = random.randint(1, 5)
#number_of_guesses = 0
#while number_of_guesses < 5:
#    print('Guess a number between 1 and 5: ')
#    guess = input()
#    guess = int(guess)
#    number_of_guesses += 1
#    if guess == number:
#        break
# Generates a random number between 1 and 5
# Then it asks the user to guess the number
# If they guess wrong, the user gets asked to guess again
# After 5 wrong guesses, the program ends

# Another form of assignment statement
total_generated: int = 0
print(total_generated)
# 0

# pyramid.py
for i in range(1, 6):
    for j in range(i):
        print("*", end='')
    print("\n", end='')

# whilePyramid.py (mine)
line_num = 0
while line_num < 5:
    line_num += 1
    print('*' * line_num)

# whilePyramid.py (Kuhn Example Solution)
i = 1
while i < 6:
    j = 0
    while j < i:
        print('*', end='')
        j += 1
    i += 1
    print('\n', end='')
