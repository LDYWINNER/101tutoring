# Chap 4
# Iteration as a strategy for solving computational problems

# sort : 구분, 분류하다
# Searching & Sorting : Two fundamental operations performed by almost every information management application

# Linear Search : Most common searching algorithm
# scans a collection from beginning to end to see if it contains a specific item

# Searching algorithm in most basic form : scan through a collection to locate a particular item of interest

# Insertion sort : Most common sorting algorithm
# systematically works through a collection, putting each successive item in its proper place

# Sorting algorithm in most basic form : reorganize collections so they are put in a particular order

# Linear Search & Insertion sort : efficient and work well for small collections of data

# Scalability : 확장성
# developed a notation based on a precise definition of what it means for an algorithm to be scalable

# array : (메모리) 배열, 모음, 무리, 집합체

# Linear Search : a simple process that starts at the front of a list and walks through one item at a time until it finds what it is looking for

# view_list : function : to draw a list on the canvas

# from PythonLabs.IterationLab import *

# Python functions
# isearch(a, 7):
# a : a list to search, 7 : the item to look for, isearch : returns the location of the item

# When the value of an expression is None, the Python Shell doesn't print anything

from PythonLabs.IterationLab import *
from PythonLabs.Tools import RandomList

print(RandomList(5)) # : How to make a list of 5 random integers
print(RandomList(5, 'colors')) # : If we want a list of random strings

# random method (for RandomList class)
# To control whether or not a search will succeed
# Give us a value to search for
# We can specify whether or not we want an item that is in the list
a = RandomList(5, 'cars')
print(a)
a.random('success')
a.random('fail')

# sources : method : To find out what sorts of strings you can request from the RandomList function
print(RandomList.sources())

fish = RandomList(5, 'fish')
print(fish)
type(fish)
# <class 'PythonLabs.Tools.RandomList>
# This name shows that RandomList is defined in the Tools module of the PythonLabs package

# delay(value) : Can speed up the animation by setting a value named 'delay' that is defined in the canvas module
# Canvas.delay = 0.1
# : Setting the animation delay to 0.1 seconds

# isearch : An implementation of the linear search algorithm using a for loop
def isearch(a, x):
    "Use a for loop to search for x"
    for i in range(0, len(a)):
        if a[i] == x:
            return i
    return None

def Isearch(a, x):
    "Use a while loop to search for x"
    i = 0
    while i < len(a):
        if a[i] == x:
            return i
        i += 1
    return None







