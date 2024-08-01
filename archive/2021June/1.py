import re
answer = r'\w+[\.\w+]?[@]\w*\.(edu|com)$'
guess = []
guess.append('test123@stonybrook.edu')
guess.append('some.name@gmail.com')
guess.append('a@b.com')
guess.append('shouldfail@home.org')
guess.append('no spaces allowed @gmail.com')
for i in guess:
    if re.search(answer, i):
        print('True')
    else:
        print('False')
print()


import re
answer = r'for( )+\w+( )+in( )+\w+[range\w+\(\)\,\ \-]+:$'
guess = []
guess.append('for car in cars:')
guess.append('for x in range(0, 10):')
guess.append('for   y in range(0, 10):')
guess.append('for my_var in someList:')
guess.append('for x in range(100, 10, -5):')

guess.append('for x in range(0,1)')
guess.append('for in range(0,10):')
guess.append('far car in cars:')
guess.append('in car for cars:')

for i in guess:
    if re.search(answer, i):
        print('True')
    else:
        print('False')