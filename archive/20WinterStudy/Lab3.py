# Functions with conditionals
# a
def fileType(fileName):
    if fileName.endswith('.py'):
        print('A python program')
    elif fileName.endswith('.java'):
        print('A java program')
    else:
        print('Something other than a python or java program')

userInput = input('Enter file name: ')
fileType(userInput)

# b
# gpa.py
def gradePoint(grade):
    if grade == 'A':
        return 4
    elif grade == 'B':
        return 3
    elif grade == 'C':
        return 2
    elif grade == 'D':
        return 1
    elif grade == 'F':
        return 0

def gradePlus(grade):
    if grade.endswith('+'):
        return gradePoint(grade.strip('+')) + 0.3
    elif grade.endswith('-'):
        return gradePoint(grade.strip('-')) - 0.3
    else:
        return gradePoint(grade)

print(gradePlus('A'))
print(gradePlus('B+'))